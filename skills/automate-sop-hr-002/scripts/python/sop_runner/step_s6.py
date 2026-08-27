"""Step S6: Recruiter phone screen  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S6'
TITLE = 'Recruiter phone screen'
DESTRUCTIVE = False
IDEMPOTENT = False


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S6")
    return True

def run(ctx):
    log("MANUAL step — owner: Recruiter / Talent Acquisition")
    log('Hold a consistent phone/video screen with each shortlisted candidate to confirm fit, motivation, logistics, and compensation expectations.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Each candidate is screened with the same core questions; notes are recorded in the ATS.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
