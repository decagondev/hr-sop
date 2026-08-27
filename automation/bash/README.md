# Bash runner — Hire for an open role: requisition to signed contract

Zero-dependency runner for `SOP-HR-002`.

```bash
./run.sh --dry-run     # safe: prints the plan, runs nothing
./run.sh               # run, prompting at manual + destructive steps
./run.sh --yes         # CI: auto-approve manual + destructive gates
./run.sh --from S3     # resume from a step
```

Destructive steps require typing `YES` (or `--yes`). Prose verifications become confirm prompts; wire in real check commands where you can.
