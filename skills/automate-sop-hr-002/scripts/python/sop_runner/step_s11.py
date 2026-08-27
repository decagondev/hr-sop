"""Step S11: Approve compensation and extend a conditional verbal offer  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S11'
TITLE = 'Approve compensation and extend a conditional verbal offer'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S11")
    return True

def run(ctx):
    log("MANUAL step — owner: Recruiter / Talent Acquisition")
    log('Confirm the package is approved and within band, then extend a verbal offer that is explicitly conditional on clearing screening and right-to-work checks. Follow up in writing summarizing the key terms.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Compensation is approved and within band; the conditional verbal offer and its terms are confirmed by email.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
