# Hire for an open role: requisition to signed contract

**ID:** SOP-HR-002  ·  **Version:** 1.0.0  ·  **Status:** approved  ·  **Domain:** hr
**Owner:** Talent Acquisition  ·  **Effective:** 2026-01-15  ·  **Review:** annual
**Approvers:** Head of Talent Acquisition, HR Business Partner, Legal / Compliance
**Standards:** Title VII of the Civil Rights Act, Age Discrimination in Employment Act (ADEA), Americans with Disabilities Act (ADA), EEOC Uniform Guidelines on Employee Selection Procedures (29 CFR Part 1607), EEOC recordkeeping (29 CFR 1602.14), Fair Credit Reporting Act (FCRA), Ban-the-box / fair-chance laws, Immigration Reform and Control Act (IRCA) / Form I-9, GDPR / CCPA (candidate data)

> Reproducibility: **100/100 (grade A)** · automatable steps ≈ 19%

## 1. Purpose & scope

Take an approved hiring need from an open requisition through sourcing, structured selection, a conditional offer, compliant screening, and a fully executed employment agreement — consistently, defensibly, and with the candidate experience and legal obligations handled at every step.

**In scope:**
- Requisition creation and headcount/budget approval
- Job description and job-related selection criteria
- Sourcing, application screening, and interviews
- Structured evaluation, selection, and reference checks
- Conditional offer, FCRA-compliant background screening, and adverse action
- Offer, negotiation, and execution of the employment agreement
- Initiation of right-to-work (Form I-9) and handoff to onboarding

**Out of scope:**
- Day-one onboarding and orientation (see SOP-HR-001)
- Long-range workforce planning and headcount strategy
- Independent contractor / 1099 engagements
- Immigration sponsorship and visa petitions

**Successful outcome:**
- A qualified candidate hired through a consistent, documented, defensible process
- A fully executed employment agreement on file
- Right-to-work verification initiated with a clean handoff to onboarding

**KPIs / how success is measured:**
- Time-to-fill (requisition approved to offer accepted)
- Time-to-hire (candidate entry to offer accepted)
- Offer acceptance rate
- Selection-stage adverse-impact ratio (4/5 rule)
- Scorecard completion rate

## 2. Roles

| Role | Responsibilities |
| --- | --- |
| **Hiring Manager** | Owns the role, its requirements, and the final selection decision; Defines job-related criteria and participates in structured interviews |
| **Recruiter / Talent Acquisition** | Drives the process end to end and owns the candidate experience; Sources, screens, coordinates interviews, and extends offers |
| **HR Business Partner** | Oversees process compliance, recordkeeping, and offer/contract governance; Owns FCRA adverse action and right-to-work verification |
| **Interview Panel** | Conducts structured interviews and completes anchored scorecards; Provides evidence-based, job-related evaluations |
| **Compensation / Finance Approver** | Approves headcount, budget, and the compensation package; Confirms the offer sits within the approved band |
| **Legal / Compliance** | Reviews non-standard offer terms and the employment agreement; Advises on adverse action and jurisdictional requirements |
| **Candidate** | External party; responds to the offer and completes required documents |

## 3. Prerequisites

- **Skills:** Structured interviewing and scorecard calibration, Working knowledge of EEOC, FCRA, and I-9 obligations
- **Access:** ATS with permission to create requisitions and post roles, Approved offer-letter and employment-agreement templates, Background-screening (CRA) account with disclosure/authorization forms
- **Tools:** ats, cra-api, e-signature, e-verify
- **Materials:** Interview scorecard templates with behavioral anchors (BARS), Standalone FCRA disclosure and authorization document (single purpose)
- **Inputs:** Approved workforce plan, Job architecture and compensation bands, Interview scorecard templates, Employment agreement templates

## 4. Safety & compliance

- **Compliance:** Evaluate every candidate for the same role against the same job-related criteria, in the same order; do not discriminate on protected characteristics. _(Title VII; ADEA; ADA)_
- **Compliance:** Interviews, tests, and screens are selection procedures — keep them job-related and consistent with business necessity, and monitor adverse impact (4/5 rule). _(EEOC Uniform Guidelines on Employee Selection Procedures (29 CFR Part 1607))_
- **Data:** Candidate and employee personal data must have a lawful basis, limited access, and defined retention; retain selection records at least one year (two years for federal contractors). _(29 CFR 1602.14; GDPR / CCPA)_
- **Compliance:** A background check via a CRA requires a standalone written disclosure and separate authorization; an adverse decision requires the two-step FCRA process (pre-adverse notice with the report and a Summary of Rights, a reasonable waiting period, then a final adverse-action notice). _(Fair Credit Reporting Act (15 U.S.C. 1681))_
- **Compliance:** Where fair-chance law applies, delay any criminal-history inquiry until after a conditional offer, and apply an EEOC individualized assessment (nature of the offense, time elapsed, job-relatedness). _(Ban-the-box / fair-chance laws)_
- **Legal:** Verify employment eligibility with Form I-9 — Section 1 no later than the first day of work, Section 2 within three business days of the start date; run E-Verify if enrolled. _(IRCA / Form I-9 (INA 274A))_
- **Accessibility:** Offer and honor reasonable accommodations to candidates with disabilities throughout the process. _(ADA)_

## 5. Procedure

### S1 — Open and document the requisition

`semi-automated` · automatable: **partial** via `ats` · idempotent

**Owner:** Hiring Manager  ·  **Est.** 60m

Capture the confirmed hiring need as a requisition in the ATS: role, level, reporting line, justification, target start, and the business case. This is the record everything else hangs off.

**Inputs:** Approved workforce plan
**Outputs:** Requisition record

**Commands:**

```bash
ats req upsert --external-id "$REQ_KEY" --role "$ROLE_TITLE" --level "$LEVEL" --manager "$HM" --justification-file ./business-case.md
```

**✔ Verify:** A requisition record exists in the ATS with role, level, reporting line, and business case.

> Keep the business case job-related; it anchors the selection criteria.

### S2 — Approve headcount and budget

`decision`

**Owner:** Compensation / Finance Approver  ·  **Est.** 30m

Finance / compensation reviews the requisition against headcount plan and budget and either approves it to open or returns it. No sourcing happens before approval.

**Inputs:** Requisition record
**Outputs:** Approved requisition

**Decision:**
- If _Headcount and budget approved_ → go to **S3 (Finalize the job description and selection criteria)**
- If _Not approved — revise or defer_ → go to **S1 (Open and document the requisition)**

**✔ Verify:** The requisition shows an approval record with approver, date, and budgeted band.
**☎ Escalate:** If budget is contested, escalate to the department head and HRBP.

### S3 — Finalize the job description and selection criteria

`manual`

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 90m

With the hiring manager, turn the requisition into an approved job description and a structured scorecard: 6–12 job-related competencies, each with behavioral anchors. Requirements must be necessary for the role.

**Inputs:** Approved requisition, Job architecture and compensation bands
**Outputs:** Approved job description, Interview scorecard kit

**✔ Verify:** Every listed requirement is job-related and consistent with business necessity; the scorecard defines competencies with behavioral anchors.
**Guardrails:** Avoid criteria that exclude protected groups without business necessity.

### S4 — Source candidates

`semi-automated` · automatable: **partial** via `ats` · idempotent

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 240m

Post the role to the required internal and external channels and run sourcing and referrals to build a diverse, qualified pipeline. Honor any internal-posting or pay-transparency requirements.

**Inputs:** Approved job description
**Outputs:** Candidate pipeline

**Commands:**

```bash
ats job post --req "$REQ_ID" --channels internal,careers,linkedin --pay-range "$PAY_RANGE" --idempotency-key "$REQ_ID-post"
```

**✔ Verify:** The role is posted to all required channels and a candidate pipeline is building in the ATS.

> Include the pay range where pay-transparency law requires it.

### S5 — Screen applications

`semi-automated` · automatable: **partial** via `ats` · idempotent

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 180m

Review applicants against the same job-related criteria and shortlist. Do not ask about criminal history at this stage where fair-chance law applies.

**Inputs:** Candidate pipeline
**Outputs:** Screened shortlist

**Commands:**

```bash
ats screen run --req "$REQ_ID" --criteria ./job-related-criteria.yaml --log ./screening-log.csv
```

**✔ Verify:** All applicants are screened against the same criteria and screening decisions are logged.
**Guardrails:** Do not ask about criminal history on the application (ban-the-box / fair-chance).; Screen every applicant against the same job-related criteria and log decisions.

### S6 — Recruiter phone screen

`manual`

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 180m

Hold a consistent phone/video screen with each shortlisted candidate to confirm fit, motivation, logistics, and compensation expectations.

**Inputs:** Screened shortlist
**Outputs:** Qualified shortlist

**✔ Verify:** Each candidate is screened with the same core questions; notes are recorded in the ATS.

### S7 — Administer job-related assessments

`semi-automated` · automatable: **partial** via `ats` · idempotent

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 60m

Where the role calls for it, administer the same validated, job-related assessment to every candidate and record results. Skip only if no assessment is used for this role.

**Inputs:** Qualified shortlist
**Outputs:** Assessment results

**Commands:**

```bash
ats assessment send --candidates ./shortlist.csv --assessment "$ASSESSMENT_ID" --if-not-sent
```

**✔ Verify:** The same assessment is sent to all candidates for the role and results are recorded.
**Guardrails:** Use a validated, job-related assessment applied identically to all candidates.

### S8 — Conduct structured interviews

`manual`

**Owner:** Interview Panel  ·  **Est.** 240m

Run structured panel interviews using the same core questions for every candidate, scoring against the BARS scorecard. Offer reasonable accommodations on request.

**Inputs:** Qualified shortlist, Interview scorecard kit
**Outputs:** Completed scorecards

**✔ Verify:** Every interviewer completes an anchored scorecard with evidence notes; the same core questions were used.
**☎ Escalate:** Accommodation requests go to the HRBP for prompt handling.
**Guardrails:** Ask all candidates the same core questions; score against the anchors.

### S9 — Debrief and make the selection decision

`decision`

**Owner:** Hiring Manager  ·  **Est.** 60m

Convene a structured debrief to reconcile scores against the anchors — not to reach consensus by social pressure — and make a documented, job-related decision. Retain the records.

**Inputs:** Completed scorecards, Assessment results
**Outputs:** Selection decision record, Selected candidate

**Decision:**
- If _A suitable candidate is selected_ → go to **S10 (Complete reference checks)**
- If _No suitable candidate — re-open sourcing_ → go to **S4 (Source candidates)**

**✔ Verify:** The decision and its rationale are documented and stored; the selection-rate is checked against the 4/5 rule.

### S10 — Complete reference checks

`manual`

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 60m

Run consistent, job-related reference checks on the selected candidate and record the results before making the offer conditional.

**Inputs:** Selected candidate
**Outputs:** Reference check results

**✔ Verify:** References are completed with consistent questions and results are recorded.

### S11 — Approve compensation and extend a conditional verbal offer

`manual`

**Owner:** Recruiter / Talent Acquisition  ·  **Est.** 60m

Confirm the package is approved and within band, then extend a verbal offer that is explicitly conditional on clearing screening and right-to-work checks. Follow up in writing summarizing the key terms.

**Inputs:** Selection decision record, Job architecture and compensation bands
**Outputs:** Approved compensation, Verbal conditional offer

**✔ Verify:** Compensation is approved and within band; the conditional verbal offer and its terms are confirmed by email.
**☎ Escalate:** Out-of-band compensation requires comp_approver sign-off before the offer is extended.

### S12 — Candidate response and negotiation

`decision`

**Owner:** Candidate  ·  **Est.** 30m

The candidate accepts, negotiates, or declines the conditional offer. Route accordingly; re-approve compensation for any counter-offer.

**Inputs:** Verbal conditional offer
**Outputs:** Offer acceptance (verbal)

**Decision:**
- If _Offer accepted_ → go to **S13 (Disclose, authorize, and run the background check)**
- If _Counter-offer — re-approve and re-issue_ → go to **S11 (Approve compensation and extend a conditional verbal offer)**
- If _Declined — revisit the shortlist_ → go to **S9 (Debrief and make the selection decision)**

**✔ Verify:** The candidate's response is recorded; any negotiated changes are captured before proceeding.

### S13 — Disclose, authorize, and run the background check

`semi-automated` · automatable: **partial** via `cra-api` · idempotent

**Owner:** HR Business Partner  ·  **Est.** 30m

Provide the standalone FCRA disclosure and obtain separate written authorization, then order the background check via the CRA. Keep the conditional offer in place while screening runs.

**Inputs:** Offer acceptance (verbal)
**Outputs:** Signed disclosure and authorization, Background check report

**Commands:**

```bash
cra-api order --candidate "$CANDIDATE_ID" --package standard --auth-file ./signed-authorization.pdf --idempotency-key "$CANDIDATE_ID-$REQ_ID"
```

**✔ Verify:** A signed standalone disclosure and authorization are on file before the report is ordered; the report is stored securely.
**Guardrails:** Never order the report before a signed standalone disclosure and authorization are on file.; The disclosure must be a single-purpose document, not embedded in the application.; Store background data securely with access limited to need-to-know.

### S14 — Adjudicate the results

`decision`

**Owner:** HR Business Partner  ·  **Est.** 45m

Review the background and reference results. If nothing disqualifying is found, proceed to the written offer. If there is potentially disqualifying information, apply an individualized assessment and enter adverse action.

**Inputs:** Background check report, Reference check results
**Outputs:** Adjudication decision

**Decision:**
- If _Clears — no disqualifying, job-related information_ → go to **S16 (Extend the formal written offer)**
- If _Potentially disqualifying information found_ → go to **S15 (Run FCRA adverse action (only if withdrawing))**

**✔ Verify:** The adjudication applies job-relatedness and an individualized assessment; the rationale is documented.

### S15 — Run FCRA adverse action (only if withdrawing)

`decision`

**Owner:** HR Business Partner  ·  **Est.** 90m

Send the pre-adverse-action notice with a copy of the report and the Summary of Rights, wait a reasonable period for dispute (best practice at least five business days; some jurisdictions longer), then either restore the offer or send the final adverse-action notice.

**Inputs:** Adjudication decision
**Outputs:** Adverse action record

**Decision:**
- If _Dispute resolved in the candidate's favor or record corrected_ → go to **S16 (Extend the formal written offer)**
- If _Adverse action upheld — offer rescinded, revisit the shortlist_ → go to **S9 (Debrief and make the selection decision)**

**✔ Verify:** Both notices are documented with dates and the waiting period is observed; no irreversible internal action is taken during the waiting period.
**☎ Escalate:** Legal reviews any contested or borderline adverse action before the final notice.
**Guardrails:** Do not mark the candidate rejected or backfill the role during the waiting period.

### S16 — Extend the formal written offer

`semi-automated` · automatable: **partial** via `e-signature` · idempotent

**Owner:** HR Business Partner  ·  **Est.** 60m

Issue the written offer letter / employment agreement matching the approved compensation and the verbal terms, with an acceptance deadline. Route any non-standard terms to Legal first.

**Inputs:** Adjudication decision, Approved compensation, Employment agreement templates
**Outputs:** Executed-ready offer letter, Employment agreement draft

**Commands:**

```bash
esign send --template employment-agreement --candidate "$CANDIDATE_ID" --fields ./offer-terms.json --deadline "$ACCEPT_BY" --idempotency-key "$CANDIDATE_ID-offer"
```

**✔ Verify:** The sent offer matches approved terms; non-standard terms were reviewed by Legal; an acceptance deadline is set.
**Guardrails:** The offer letter must match the approved compensation and the verbal offer.; Route non-standard terms (equity, severance, non-compete) to Legal before sending.

### S17 — Countersign and execute the agreement

`manual`

**Owner:** HR Business Partner  ·  **Est.** 30m

On candidate signature, countersign to fully execute the employment agreement and confirm the start date. This is the signed contract that completes the hire.

**Inputs:** Employment agreement draft
**Outputs:** Fully executed employment agreement

**✔ Verify:** Candidate signature and employer countersignature are on file; the start date is confirmed.

### S18 — Initiate right-to-work and hand off to onboarding

`semi-automated` · automatable: **partial** via `e-verify` · idempotent

**Owner:** HR Business Partner  ·  **Est.** 45m

Start Form I-9 and (if enrolled) E-Verify, and hand the new hire to onboarding. Section 1 is due no later than the first day; Section 2 within three business days of the start date.

**Inputs:** Fully executed employment agreement
**Outputs:** Initiated Form I-9, Onboarding handoff package

**Commands:**

```bash
everify case ensure --employee "$EMPLOYEE_ID" --start-date "$START_DATE"
```

**✔ Verify:** Form I-9 is initiated and the onboarding handoff package is delivered to the onboarding owner.
**Guardrails:** Section 1 no later than the first day; Section 2 within three business days of start.; Do not use I-9 to pre-screen work authorization before offer acceptance.; Never open a duplicate E-Verify case for the same employee.

> I-9 Section 2 and day-one tasks complete in onboarding (SOP-HR-001).

## 6. Definitions

- **ATS:** Applicant Tracking System — the system of record for the requisition and candidates.
- **CRA:** Consumer Reporting Agency — third party that produces the background report under the FCRA.
- **BARS:** Behaviorally Anchored Rating Scale — defined behavior for each score on the interview scorecard.
- **Conditional offer:** An offer contingent on clearing screening and right-to-work checks.
- **Adverse action:** A decision not to hire based on a background report, triggering FCRA notices.
- **At-will:** Employment either party may end at any time, subject to law and any contract terms.

## 7. References

- EEOC — Background Checks: What Employers Need to Know (eeoc.gov)
- EEOC Uniform Guidelines on Employee Selection Procedures, 29 CFR Part 1607
- FTC/CFPB — A Summary of Your Rights Under the Fair Credit Reporting Act
- USCIS — Form I-9, Employment Eligibility Verification (uscis.gov/i-9)

## 7a. Related procedures

- **successor**: `SOP-HR-001` (at S18) — Day-one onboarding and I-9 completion continue in the onboarding SOP.

## 9. Change log

| Version | Date | Author | Summary |
| --- | --- | --- | --- |
| 1.0.0 | 2026-01-15 | Talent Acquisition | First approved version; research-grounded end-to-end hiring SOP. |
