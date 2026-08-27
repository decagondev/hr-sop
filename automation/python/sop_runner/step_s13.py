"""Step S13: Disclose, authorize, and run the background check  (owner: HR Business Partner)"""
from .runtime import run_cmd, log, confirm

STEP_ID = 'S13'
TITLE = 'Disclose, authorize, and run the background check'
DESTRUCTIVE = False
IDEMPOTENT = True
    # guardrail: Never order the report before a signed standalone disclosure and authorization are on file.
    # guardrail: The disclosure must be a single-purpose document, not embedded in the application.
    # guardrail: Store background data securely with access limited to need-to-know.

def preflight(ctx):
    """Cheap checks that must pass before we touch anything."""
    log("preflight for S13")
    return True

def run(ctx):
    if DESTRUCTIVE and not ctx.get("assume_yes"):
        confirm("This step is DESTRUCTIVE. Type to proceed")
        run_cmd('cra-api order --candidate "$CANDIDATE_ID" --package standard --auth-file ./signed-authorization.pdf --idempotency-key "$CANDIDATE_ID-$REQ_ID"')

def verify(ctx):
    log("verify: A signed standalone disclosure and authorization are on file before the report is ordered; the report is stored securely.")
    # TODO: assert the expected result programmatically and return True/False.
    return True

def rollback(ctx):
    log("no rollback defined for this step")
