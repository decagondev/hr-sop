# Hire for an open role: requisition to signed contract

`SOP-HR-002` · v1.0.0 · **approved** · domain: hr

Take an approved hiring need from an open requisition through sourcing, structured selection, a conditional offer, compliant screening, and a fully executed employment agreement — consistently, defensibly, and with the candidate experience and legal obligations handled at every step.

> **Reproducibility: 100/100 (grade A)** — this package was compiled by [sop-forge](https://) v1.0.0 from a single source model, so every artifact below is consistent with every other.

## Start here

- **Open `site/index.html`** in a browser — the interactive guide and mini-course.
- **Read `sop/sop.md`** for the full written procedure.
- **Present `slides/index.html`** to walk a team through it.

## The procedure at a glance

18 steps · 7 roles. Ends at: initiate right-to-work and hand off to onboarding.

S1. **Open and document the requisition** — Hiring Manager
S2. **Approve headcount and budget** — Compensation / Finance Approver *(decision)*
S3. **Finalize the job description and selection criteria** — Recruiter / Talent Acquisition
S4. **Source candidates** — Recruiter / Talent Acquisition
S5. **Screen applications** — Recruiter / Talent Acquisition
S6. **Recruiter phone screen** — Recruiter / Talent Acquisition
S7. **Administer job-related assessments** — Recruiter / Talent Acquisition
S8. **Conduct structured interviews** — Interview Panel
S9. **Debrief and make the selection decision** — Hiring Manager *(decision)*
S10. **Complete reference checks** — Recruiter / Talent Acquisition
S11. **Approve compensation and extend a conditional verbal offer** — Recruiter / Talent Acquisition
S12. **Candidate response and negotiation** — Candidate *(decision)*
S13. **Disclose, authorize, and run the background check** — HR Business Partner
S14. **Adjudicate the results** — HR Business Partner *(decision)*
S15. **Run FCRA adverse action (only if withdrawing)** — HR Business Partner *(decision)*
S16. **Extend the formal written offer** — HR Business Partner
S17. **Countersign and execute the agreement** — HR Business Partner
S18. **Initiate right-to-work and hand off to onboarding** — HR Business Partner

## Roles

- **Hiring Manager** — Owns the role, its requirements, and the final selection decision.
- **Recruiter / Talent Acquisition** — Drives the process end to end and owns the candidate experience.
- **HR Business Partner** — Oversees process compliance, recordkeeping, and offer/contract governance.
- **Interview Panel** — Conducts structured interviews and completes anchored scorecards.
- **Compensation / Finance Approver** — Approves headcount, budget, and the compensation package.
- **Legal / Compliance** — Reviews non-standard offer terms and the employment agreement.
- **Candidate** — External party; responds to the offer and completes required documents.

## What's in this package

**Read & present**

| File | What it's for |
| --- | --- |
| `sop/sop.md` | The SOP itself — the full written procedure. |
| `site/index.html` | Interactive docs site with a built-in mini-course. Open in a browser. |
| `slides/index.html` | Self-contained slide deck for walking a room through the process. |
| `training/` | Facilitator guide, run checklist, and quick-reference for training people. |
| `summary-card.html` | One-page printable summary card. |
| `timeline.html` | Gantt-style timeline of effort across the steps. |
| `role-checklists.md` | Per-role checklists — each role's slice of the procedure. |
| `raci.md` | RACI-style responsibility matrix (who is Responsible / Accountable / Consulted). |
| `poster.html` | Large-format wall poster of the flow. |

**Run & automate**

| File | What it's for |
| --- | --- |
| `automation/python/` | Runnable Python automation scaffold with a step per SOP step. |
| `automation/ansible/` | Ansible playbook scaffold. |
| `automation/bash/` | Bash runner scaffold. |
| `automation/terraform/` | Terraform scaffold. |
| `skills/follow-*.skill` | A Claude skill that lets an AI *follow* this procedure step by step. |
| `skills/automate-*.skill` | A Claude skill that *automates* the procedure's runnable steps. |
| `.github/workflows/` | GitHub Actions workflow that validates the SOP on push. |

**Data & diagrams**

| File | What it's for |
| --- | --- |
| `slides/deck.json` | Structured slide data behind the deck. |
| `coverage.json` | Coverage matrix — which steps have verification, rollback, automation. |
| `coverage.md` | The coverage matrix rendered as Markdown. |
| `steps.csv` | The step table as CSV for spreadsheets. |
| `sop.json` | The full procedure as structured JSON (the machine-readable IR). |
| `diagrams/flow.dot` | Graphviz source for the flow diagram (`dot -Tsvg`). |
| `diagrams/flow.mmd` | Mermaid source for the flow diagram. |
| `badges/` | SVG status badges (reproducibility, coverage, lint). |

## Standards & compliance

This procedure is written against:

- Title VII of the Civil Rights Act
- Age Discrimination in Employment Act (ADEA)
- Americans with Disabilities Act (ADA)
- EEOC Uniform Guidelines on Employee Selection Procedures (29 CFR Part 1607)
- EEOC recordkeeping (29 CFR 1602.14)
- Fair Credit Reporting Act (FCRA)
- Ban-the-box / fair-chance laws
- Immigration Reform and Control Act (IRCA) / Form I-9
- GDPR / CCPA (candidate data)

## Keep these human

Automation supports this procedure but does not decide it. These points require human judgement:

- **S2 Approve headcount and budget**
- **S9 Debrief and make the selection decision**
- **S12 Candidate response and negotiation**
- **S14 Adjudicate the results**
- **S15 Run FCRA adverse action (only if withdrawing)**

## Regenerate

Everything here is generated from one source model. To rebuild after editing it:

```bash
sopkit validate --ir sop-hr-002.sop.yaml          # confirm it still scores grade A
sopkit build --ir sop-hr-002.sop.yaml --out . --targets all
```

---
*Generated by sop-forge v1.0.0. Reproducibility 100/100 (grade A). Not legal advice — confirm domain- and jurisdiction-specific rules.*
