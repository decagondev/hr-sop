"""Step S9: Debrief and make the selection decision  (owner: Hiring Manager)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S9'
TITLE = 'Debrief and make the selection decision'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S9")
    return True

def run(ctx):
    log("MANUAL step — owner: Hiring Manager")
    log('Convene a structured debrief to reconcile scores against the anchors — not to reach consensus by social pressure — and make a documented, job-related decision. Retain the records.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: The decision and its rationale are documented and stored; the selection-rate is checked against the 4/5 rule.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
