"""Step S2: Approve headcount and budget  (owner: Compensation / Finance Approver)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S2'
TITLE = 'Approve headcount and budget'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S2")
    return True

def run(ctx):
    log("MANUAL step — owner: Compensation / Finance Approver")
    log('Finance / compensation reviews the requisition against headcount plan and budget and either approves it to open or returns it. No sourcing happens before approval.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: The requisition shows an approval record with approver, date, and budgeted band.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
