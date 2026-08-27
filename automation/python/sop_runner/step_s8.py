"""Step S8: Conduct structured interviews  (owner: Interview Panel)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S8'
TITLE = 'Conduct structured interviews'
DESTRUCTIVE = False
IDEMPOTENT = False
    # guardrail: Ask all candidates the same core questions; score against the anchors.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S8")
    return True

def run(ctx):
    log("MANUAL step — owner: Interview Panel")
    log('Run structured panel interviews using the same core questions for every candidate, scoring against the BARS scorecard. Offer reasonable accommodations on request.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Every interviewer completes an anchored scorecard with evidence notes; the same core questions were used.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
