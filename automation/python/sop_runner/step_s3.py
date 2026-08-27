"""Step S3: Finalize the job description and selection criteria  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S3'
TITLE = 'Finalize the job description and selection criteria'
DESTRUCTIVE = False
IDEMPOTENT = False
    # guardrail: Avoid criteria that exclude protected groups without business necessity.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S3")
    return True

def run(ctx):
    log("MANUAL step — owner: Recruiter / Talent Acquisition")
    log('With the hiring manager, turn the requisition into an approved job description and a structured scorecard: 6–12 job-related competencies, each with behavioral anchors. Requirements must be necessary for the role.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Every listed requirement is job-related and consistent with business necessity; the scorecard defines competencies with behavioral anchors.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
