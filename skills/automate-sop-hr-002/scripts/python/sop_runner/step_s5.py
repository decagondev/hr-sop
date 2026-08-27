"""Step S5: Screen applications  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S5'
TITLE = 'Screen applications'
DESTRUCTIVE = False
IDEMPOTENT = True
    # guardrail: Do not ask about criminal history on the application (ban-the-box / fair-chance).
    # guardrail: Screen every applicant against the same job-related criteria and log decisions.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S5")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('ats screen run --req "$REQ_ID" --criteria ./job-related-criteria.yaml --log ./screening-log.csv')

def verify(ctx):
    log("verify: All applicants are screened against the same criteria and screening decisions are logged.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
