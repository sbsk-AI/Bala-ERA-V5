# ERA V5 — Training Data Execution System

This repository turns the ERA V5 mixture/curriculum proposal into a small, deterministic Training Data Execution System.

## One-command demonstration

```bash
python run_demo.py
```

The command generates `submission_artifacts/` from the implementation. Nothing in `evidence.json` or `evidence.md` is manually asserted; the evidence is derived from the run.

## Test

```bash
python tests/test_invariants.py
```

## Architecture

`documents.json` → immutable tokenized shards/manifests → mixture schedule and protected floors → OPUS decisions → packing/masks/positions → batches → consumption ledger → learning ledger → checkpoint → deliberate crash → resume → replay → fork → audit/performance → evidence bundle.

The implementation is intentionally small. It is designed to demonstrate reproducibility, auditability and execution semantics rather than model scale.

## Generated evidence

- `submission_artifacts/run.log`
- `submission_artifacts/evidence.json`
- `submission_artifacts/evidence.md`
- `submission_artifacts/manifests/`
- `submission_artifacts/ledgers/`
- `submission_artifacts/checkpoints/`
- `submission_artifacts/performance.json`

The existing ERA V5 design remains the policy layer: 100% capability mixture, Indic/programming/reasoning/long-context protected floors, staged curriculum, and data-quality controls.
