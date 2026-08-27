"""Step S4: Source candidates  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S4'
TITLE = 'Source candidates'
DESTRUCTIVE = False
IDEMPOTENT = True


def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S4")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('ats job post --req "$REQ_ID" --channels internal,careers,linkedin --pay-range "$PAY_RANGE" --idempotency-key "$REQ_ID-post"')

def verify(ctx):
    log("verify: The role is posted to all required channels and a candidate pipeline is building in the ATS.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
