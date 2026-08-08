# ERA V5 Evidence Bundle

| Requirement | Result | Evidence |
|---|---|---|
| Tokenizer Integrity | PASS | `manifests/tokenizer.json + tokenizer.sha256` |
| Evaluation Firewall | PASS | `eval shard excluded from packer` |
| Packing Correctness | PASS | `manifests/batches.json` |
| Mixture Compliance | PASS | `manifests/mixture_actual.json` |
| Opus Audit Trail | PASS | `manifests/opus_decisions.json` |
| Crash Recovery | PASS | `checkpoints/checkpoint-0002.json; ledgers/consumption.json` |
| Replay | PASS | `manifests/replay.json` |
| Learning Trace | PASS | `ledgers/learning.json` |
| Throughput | PASS | `performance.json` |
