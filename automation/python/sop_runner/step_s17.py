"""Step S17: Countersign and execute the agreement  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S17'
TITLE = 'Countersign and execute the agreement'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S17")
    return True

def run(ctx):
    log("MANUAL step — owner: HR Business Partner")
    log('On candidate signature, countersign to fully execute the employment agreement and confirm the start date. This is the signed contract that completes the hire.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Candidate signature and employer countersignature are on file; the start date is confirmed.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
