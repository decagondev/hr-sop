---
name: automate-sop-hr-002
description: "Automate the 'Hire for an open role: requisition to signed contract' SOP (hr) by driving its bundled Python runner and Ansible role. Use when the user wants to automatically run, schedule, or CI-execute hire for an open role: requisition to signed contract, run a single automated step, or types /automate-sop-hr-002. Enforces the safety gates: nothing destructive runs without explicit opt-in, every step is verified, and failures roll back. Prefer these bundled scripts over improvised commands."
argument-hint: "[dry|ci|force] [step <ID>]"
allowed-tools: Bash
---

# Automate: Hire for an open role: requisition to signed contract

Drive the bundled automation for this SOP. **Read `rules.md` before running
anything** — those rules are what keep an automated run safe. The executable
assets live under `scripts/python/` (a `sop_runner` package) and
`scripts/ansible/` (a role + `playbook.yml`).

## Choosing the tool

- **Python runner** (`scripts/python`): procedural steps, app/API calls, anything
  that isn't infrastructure convergence. Entry point:
  ```bash
  cd scripts/python
  python -m sop_runner --dry-run     # preflight everything
  python -m sop_runner               # run interactively
  python -m sop_runner --from <ID>   # resume
  python -m sop_runner --yes         # CI (still won't skip explicit gates)
  ```
- **Ansible role** (`scripts/ansible`): infrastructure/config steps.
  ```bash
  cd scripts/ansible
  ansible-playbook -i inventory.ini playbook.yml --check          # dry run
  ansible-playbook -i inventory.ini playbook.yml --tags <ID>      # one step
  ansible-playbook -i inventory.ini playbook.yml -e confirm_destructive=true
  ```

Some steps are marked `partial` — automate the mechanical part and hand the
judgement part back to the user.

## Slash commands

- `/automate-sop-hr-002` — run the whole automatable procedure interactively.
- `/automate-sop-hr-002 dry` — preflight/`--check` only; change nothing.
- `/automate-sop-hr-002 step <ID>` — run one step (ids: S1, S4, S5, S7, S13, S16, S18).
- `/automate-sop-hr-002 ci` — non-interactive run (auto-confirm pauses, no destructive).

Parse `$ARGUMENTS`: `dry` → dry-run/check; `ci` → non-interactive, no destructive;
`force` → allow destructive **only** with explicit user authorisation; `step <ID>`
→ run just that step via `--from`/`--tags`.

## Before you finish

Confirm the SOP's successful-outcome criteria, report every change made, and note
any `TODO` you hit where the generated script needs a human to complete it.
