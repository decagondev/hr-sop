"""Step S18: Initiate right-to-work and hand off to onboarding  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S18'
TITLE = 'Initiate right-to-work and hand off to onboarding'
DESTRUCTIVE = False
IDEMPOTENT = True
    # guardrail: Section 1 no later than the first day; Section 2 within three business days of start.
    # guardrail: Do not use I-9 to pre-screen work authorization before offer acceptance.
    # guardrail: Never open a duplicate E-Verify case for the same employee.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S18")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('everify case ensure --employee "$EMPLOYEE_ID" --start-date "$START_DATE"')

def verify(ctx):
    log("verify: Form I-9 is initiated and the onboarding handoff package is delivered to the onboarding owner.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
