import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def run():
    subprocess.run([sys.executable, str(ROOT/"run_demo.py")], check=True)
    out=ROOT/"submission_artifacts"
    assert (out/"evidence.json").exists()
    ev=json.loads((out/"evidence.json").read_text())
    assert all(v["result"]=="PASS" for v in ev.values())
    batches=json.loads((out/"manifests"/"batches.json").read_text())
    assert batches
    for b in batches:
        for s in b["samples"]:
            assert s["sample_id"].startswith("tr-")
            assert len(s["input_ids"])==16
            assert len(s["loss_mask"])==16
            assert len(s["attention_mask"])==16
            assert len(s["position_ids"])==16
            assert all(m==0 or a==1 for m,a in zip(s["loss_mask"],s["attention_mask"]))
    replay=json.loads((out/"manifests"/"replay.json").read_text())
    assert all(x["match"] for x in replay)
    cons=json.loads((out/"ledgers"/"consumption.json").read_text())
    assert [x["ledger_offset"] for x in cons]==list(range(len(cons)))
    print("ALL INVARIANT TESTS PASSED")
if __name__=="__main__": run()
