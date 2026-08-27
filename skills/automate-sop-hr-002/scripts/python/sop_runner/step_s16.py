"""Step S16: Extend the formal written offer  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S16'
TITLE = 'Extend the formal written offer'
DESTRUCTIVE = False
IDEMPOTENT = True
    # guardrail: The offer letter must match the approved compensation and the verbal offer.
    # guardrail: Route non-standard terms (equity, severance, non-compete) to Legal before sending.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S16")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('esign send --template employment-agreement --candidate "$CANDIDATE_ID" --fields ./offer-terms.json --deadline "$ACCEPT_BY" --idempotency-key "$CANDIDATE_ID-offer"')

def verify(ctx):
    log("verify: The sent offer matches approved terms; non-standard terms were reviewed by Legal; an acceptance deadline is set.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
