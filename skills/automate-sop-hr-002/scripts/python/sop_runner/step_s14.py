"""Step S14: Adjudicate the results  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S14'
TITLE = 'Adjudicate the results'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S14")
    return True

def run(ctx):
    log("MANUAL step — owner: HR Business Partner")
    log('Review the background and reference results. If nothing disqualifying is found, proceed to the written offer. If there is potentially disqualifying information, apply an individualized assessment and enter adverse action.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: The adjudication applies job-relatedness and an individualized assessment; the rationale is documented.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
