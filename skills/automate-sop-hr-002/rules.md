# Automation rules for Hire for an open role: requisition to signed contract

These rules hold for every automated run. They exist so an automated execution is
as safe as a careful human one.

1. **Verify or revert.** After each step, confirm its verification passed. On
   failure, roll back that step and stop — never continue past a failed check.
2. **Destructive is opt-in.** No steps are currently marked destructive; re-check the SOP before assuming so.
3. **Dry-run first when unsure.** If you can't predict the effect, run the Python
   `--dry-run` or Ansible `--check` slice before the real thing.
4. **One tool per step.** Use the Python runner for procedural/app logic and the
   Ansible role for infrastructure/config convergence. Don't reimplement a step
   inline when a bundled task exists.
5. **Idempotence.** Prefer re-runnable operations; if a task isn't yet idempotent
   (has a `TODO`), say so before running it in anger.
6. **Report, don't bury.** Summarise what ran, what changed, and what to check.
