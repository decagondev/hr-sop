# Hire for an open role: requisition to signed contract — Python runner

Idempotent step runner generated from the SOP.

```bash
python -m sop_runner --dry-run   # preflight all steps
python -m sop_runner              # run interactively
python -m sop_runner --yes        # non-interactive (CI)
```

Each `step_*.py` has `preflight/run/verify/rollback`. Fill the `TODO`s where the IR lacked concrete commands.
