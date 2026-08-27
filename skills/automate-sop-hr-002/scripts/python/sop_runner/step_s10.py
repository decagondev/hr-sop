"""Step S10: Complete reference checks  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S10'
TITLE = 'Complete reference checks'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S10")
    return True

def run(ctx):
    log("MANUAL step — owner: Recruiter / Talent Acquisition")
    log('Run consistent, job-related reference checks on the selected candidate and record the results before making the offer conditional.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: References are completed with consistent questions and results are recorded.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
