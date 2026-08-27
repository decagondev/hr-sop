"""Step S15: Run FCRA adverse action (only if withdrawing)  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S15'
TITLE = 'Run FCRA adverse action (only if withdrawing)'
DESTRUCTIVE = False
IDEMPOTENT = False
    # guardrail: Do not mark the candidate rejected or backfill the role during the waiting period.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S15")
    return True

def run(ctx):
    log("MANUAL step — owner: HR Business Partner")
    log('Send the pre-adverse-action notice with a copy of the report and the Summary of Rights, wait a reasonable period for dispute (best practice at least five business days; some jurisdictions longer), then either restore the offer or send the final adverse-action notice.')
    confirm("Confirm you have completed this step")

def verify(ctx):
    log("verify: Both notices are documented with dates and the waiting period is observed; no irreversible internal action is taken during the waiting period.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
