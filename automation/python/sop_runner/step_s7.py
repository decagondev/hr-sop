"""Step S7: Administer job-related assessments  (owner: Recruiter / Talent Acquisition)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S7'
TITLE = 'Administer job-related assessments'
DESTRUCTIVE = False
IDEMPOTENT = True
    # guardrail: Use a validated, job-related assessment applied identically to all candidates.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S7")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('ats assessment send --candidates ./shortlist.csv --assessment "$ASSESSMENT_ID" --if-not-sent')

def verify(ctx):
    log("verify: The same assessment is sent to all candidates for the role and results are recorded.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
