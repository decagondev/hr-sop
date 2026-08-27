---
name: follow-sop-hr-002
description: "Execute the 'Hire for an open role: requisition to signed contract' standard operating procedure (hr) step by step, as a careful operator. Use this whenever the user wants to run, perform, walk through, or be guided through hire for an open role: requisition to signed contract — or types /sop-hr-002. Announces each step, does the work or tells the user exactly what to do, runs the verification before advancing, and rolls back on failure. Do not skip the verification gates — they are the point."
argument-hint: "[context or starting step id]"
---

# Run: Hire for an open role: requisition to signed contract

You are executing a standard operating procedure as a disciplined operator, not
summarising it. The full, authoritative procedure is in
`references/sop.md` — **read it fully before you start**. This SKILL.md is the
operating discipline; the reference is the content.

**Version 1.0.0 · hr · owner: Talent Acquisition**

## The operating loop (do this for every step, in order)

For each step, work the same four beats — this is what makes the run reproducible:

1. **Announce.** State the step id, title, who owns it, and what it will do.
2. **Act.** Either perform it (if it's yours to do and safe) or give the user the
   exact action to take. For automatable steps, prefer the bundled runner/playbook
   from the automation skill if it's available, rather than improvising commands.
3. **Verify.** Run the step's verification and report the result plainly. **A step
   is not done until its verification passes.** If there's no verification in the
   SOP, say so and get the user to confirm the expected output before advancing.
4. **Handle failure.** If verify fails, do **not** proceed. Perform the step's
   rollback, report what happened, and either retry or escalate per the SOP.

## Guardrails

- No steps are marked destructive, but still confirm before any irreversible action.
- Respect roles: if a step belongs to a role the user hasn't taken, flag it and
  ask who is doing it rather than silently doing it yourself.
- Honour every safety/compliance note in the SOP — those aren't optional.
- If the situation drifts outside the SOP's stated scope, stop and say so. Don't
  invent procedure; a flagged gap is safer than a confident guess.
- Decision steps: evaluate the branch condition explicitly, tell the user which
  branch you're taking and why, then jump to that step.

## Steps in this SOP

1. **S1 — Open and document the requisition** (automatable)
2. **S2 — Approve headcount and budget** (manual, decision)
3. **S3 — Finalize the job description and selection criteria** (manual)
4. **S4 — Source candidates** (automatable)
5. **S5 — Screen applications** (automatable)
6. **S6 — Recruiter phone screen** (manual)
7. **S7 — Administer job-related assessments** (automatable)
8. **S8 — Conduct structured interviews** (manual)
9. **S9 — Debrief and make the selection decision** (manual, decision)
10. **S10 — Complete reference checks** (manual)
11. **S11 — Approve compensation and extend a conditional verbal offer** (manual)
12. **S12 — Candidate response and negotiation** (manual, decision)
13. **S13 — Disclose, authorize, and run the background check** (automatable)
14. **S14 — Adjudicate the results** (manual, decision)
15. **S15 — Run FCRA adverse action (only if withdrawing)** (manual, decision)
16. **S16 — Extend the formal written offer** (automatable)
17. **S17 — Countersign and execute the agreement** (manual)
18. **S18 — Initiate right-to-work and hand off to onboarding** (automatable)

## Starting

`$ARGUMENTS` may carry context or a step id to resume from. If it names a step,
start there; otherwise start at the first step. If the user only wants a single
step, do just that one — announce, act, verify — and stop.

Keep a running note of which steps passed so the user can see progress. At the
end, confirm the successful-outcome criteria from the SOP were met.
