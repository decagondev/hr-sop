"""
Orchestrator for: Hire for an open role: requisition to signed contract
Runs each step: preflight -> run -> verify. On verify failure, rolls back and stops.

Usage:
    python -m sop_runner            # run all steps
    python -m sop_runner --yes      # auto-confirm destructive steps (CI)
    python -m sop_runner --from S3  # resume from a step id
    python -m sop_runner --dry-run  # preflight only
"""
import argparse
import sys
from . import step_s1
from . import step_s2
from . import step_s3
from . import step_s4
from . import step_s5
from . import step_s6
from . import step_s7
from . import step_s8
from . import step_s9
from . import step_s10
from . import step_s11
from . import step_s12
from . import step_s13
from . import step_s14
from . import step_s15
from . import step_s16
from . import step_s17
from . import step_s18

STEPS = [
    step_s1,
    step_s2,
    step_s3,
    step_s4,
    step_s5,
    step_s6,
    step_s7,
    step_s8,
    step_s9,
    step_s10,
    step_s11,
    step_s12,
    step_s13,
    step_s14,
    step_s15,
    step_s16,
    step_s17,
    step_s18
]

def main():
    ap = argparse.ArgumentParser(description='Hire for an open role: requisition to signed contract')
    ap.add_argument("--yes", action="store_true", help="auto-confirm destructive steps")
    ap.add_argument("--from", dest="start", help="resume from this step id")
    ap.add_argument("--dry-run", action="store_true", help="preflight only")
    args = ap.parse_args()
    ctx = {"assume_yes": args.yes}

    started = args.start is None
    for mod in STEPS:
        if not started:
            if mod.STEP_ID == args.start:
                started = True
            else:
                continue
        print(f"\n=== {mod.STEP_ID}: {mod.TITLE} ===")
        if not mod.preflight(ctx):
            print(f"preflight failed for {mod.STEP_ID}"); sys.exit(1)
        if args.dry_run:
            continue
        try:
            mod.run(ctx)
        except SystemExit:
            raise
        except Exception as e:
            print(f"run failed for {mod.STEP_ID}: {e}")
            mod.rollback(ctx); sys.exit(1)
        if not mod.verify(ctx):
            print(f"VERIFY FAILED for {mod.STEP_ID} — rolling back")
            mod.rollback(ctx); sys.exit(1)
        print(f"✔ {mod.STEP_ID} ok")
    print("\n✅ SOP complete")

if __name__ == "__main__":
    main()
