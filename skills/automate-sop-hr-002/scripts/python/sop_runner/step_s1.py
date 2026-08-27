"""Step S1: Open and document the requisition  (owner: Hiring Manager)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S1'
TITLE = 'Open and document the requisition'
DESTRUCTIVE = False
IDEMPOTENT = True


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S1")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('ats req upsert --external-id "$REQ_KEY" --role "$ROLE_TITLE" --level "$LEVEL" --manager "$HM" --justification-file ./business-case.md')

def verify(ctx):
    log("verify: A requisition record exists in the ATS with role, level, reporting line, and business case.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
