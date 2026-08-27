"""Step S12: Candidate response and negotiation  (owner: Candidate)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S12'
TITLE = 'Candidate response and negotiation'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S12")
    return True

def run(ctx):
    log("MANUAL step — owner: Candidate")
    log('The candidate accepts, negotiates, or declines the conditional offer. Route accordingly; re-approve compensation for any counter-offer.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: The candidate's response is recorded; any negotiated changes are captured before proceeding.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
