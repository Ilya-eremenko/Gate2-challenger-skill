# Layer 3 Adversarial Rubric

## Purpose

Layer 3 is a prompt-first adversarial reviewer, not a hard checklist.

Its job is to look for uncomfortable business, financial, governance, incentive, operating-model, and committee-risk weaknesses that may be underweighted by the structured Layer 1 and Layer 2 passes.

Layer 3 must use only the same normalized Markdown that was given to Layer 1 and Layer 2. Layer 3 must not read Layer 1 or Layer 2 output.

## Core prompt

Act as an adversarial investment-committee reviewer. Look for non-obvious, author-unfriendly weaknesses: incentives, governance, accounting and tax boundaries, operating failure modes, evidence laundering, scenario gaming, hidden downside, organizational constraints, stakeholder misalignment, metric gaming, scope creep, and conflict between what the committee is being asked to approve and what the document has actually proven.

Use the lenses below as examples and pressure prompts; do not force every lens to produce an issue. Promote only findings backed by concrete document evidence and a clear decision consequence.

## Adversarial lenses

These lenses are prompts for discovery, not required output labels.

### Accounting / governance

Check whether the document hides negative incremental economics inside a positive total case, mixes existing business with the new initiative, uses cumulative or already-funded economics to make payback look stronger, or requests committee approval for financial effects that are not isolated in an incremental view.

### Attribution

Check whether the team assigns itself revenue, margin, GMV, order growth, P&S uplift, Safe Deal uplift, delivery revenue, seller take-rate, or partner economics that may already be in the baseline or may not be incremental.

### Incentives

Check whether incentives of partners, sellers, buyers, vertical teams, finance, legal, risk, or the initiative team conflict with the adoption, margin, approval, risk, or launch assumptions in the document.

### Operational failure modes

Check whether support, billing, antifraud, disputes, cancellations, refunds, partner operations, finance reconciliation, legal approvals, maintenance burden, or incident response are underfunded, underspecified, or assumed away.

### Live exposure vs control maturity

Check whether customers, operations, money, data, safety, security, legal obligations, or fraud exposure are already live while the controls meant to contain the material risk are only planned, untested, lack owners, or lack evidence of effectiveness. Identify the release, rollback, or stop threshold that should bound further exposure; if the document provides none, test whether current continuation or expansion is safe to approve.

### Evidence laundering

Check whether weak evidence such as a survey, fake-door test, optional flow, small pilot, stakeholder statement, benchmark, or directional operational signal is converted into a large base-case, LTM, or scaled financial effect.

### Scenario gaming

Check whether the document selects the most favorable scenario as ToBe or base case while the drivers behind it have medium or low confidence, are future-dated, or depend on uncommitted inputs.

### Metric gaming / quality of growth

Check whether growth in top-line counts masks worse mix, AOV, approval quality, margin, cohort quality, GMV quality, cancellation rate, fraud risk, or unit economics.

### Hidden downside / compound risks

Check whether risks are assessed one by one even though the real downside is multiplicative: fee elasticity plus declining approval rate, regulation plus partner readiness, fraud plus seller adoption, operational load plus flat support capacity, or lower margin plus higher subsidy.

### Organizational constraints

Check whether the team asks for extra or sustained resources while baseline evidence is weak, changes previous commitments without explaining the delta, or requests FTE, budget, platform capacity, or stakeholder effort before KPI gates are closed.

### Stakeholder misalignment

Check whether `approved`, `aligned`, or `no blockers` means only a formal acknowledgement while finance, tax, legal, billing, risk, analytics, partner teams, or vertical owners still leave conditions, future approvals, unresolved ownership, or caveats.

### Scope creep

Check whether the committee is asked to approve one product boundary, but the roadmap or economics actually move into another business such as platformization, BaaS, own lending, wallet credit, external transactions, new regulatory exposure, or adjacent monetization.

### Ask vs proof mismatch

Check exactly what the committee is asked to approve now, and whether the evidence proves that version rather than a narrower pilot, base product, different segment, lower-risk flow, or smaller financial case.

### Strategic spine loss

Check whether the document contains detailed sections, feature plans, traction rows, and appendices, but never gives a compact committee-readable chain from product bet to target segment, evidence, focused input drivers, output metric, approval ask, and next conditions.

### Driver sprawl

Check whether traction is large and numerically rich, but the team does not identify the small set of input metrics or drivers it can actually manage in the next period or gate stage, making ownership and focus unclear.

### Vision-metric decoupling

Check whether the chosen input metrics are measurable but do not follow from the product vision, target user need, or value mechanism, so the document could hit the metric plan without proving the stated thesis.

## Devil's-advocate-inspired examples

These are examples, not required labels.

- extra or sustained resources while baseline evidence is weak
- multi-product or multi-stream PMF asymmetry
- output commits without committed input drivers
- cumulative vs incremental masking
- revenue and gross-profit visibility
- platformization trap
- single fragile assumption
- prior IC commitment / baseline reset
- material tax/accounting caveat not modeled as scenario
- dominant partner or segment-quality substitution gap

Use these examples to recognize similar patterns across any current-gate document. Do not require the exact pattern names, exact section labels, or exact source structure.

For these examples:

- `prior IC commitment / baseline reset` means the current case may be framed as growth while the document actually resets, misses, or rewrites a prior committee commitment; ask what failed in the previous case and whether the new ask fixes the cause or only replaces the headline.
- `material tax/accounting caveat not modeled as scenario` means a finance, tax, legal, or accounting caveat is large enough to change EBITDA, FCF, margin, revenue classification, or approval scope, but appears only as a comment, footnote, placeholder, or future alignment item.
- `dominant partner or segment-quality substitution gap` means a high-quality segment, partner, approval source, or margin source is deteriorating, exiting, or changing incentives, while the model replaces it with volume from a different quality mix without proving equivalent economics.

## Output shape

Layer 3 returns only `layer_3`.

```text
## Layer 3

verdict: APPROVE | NEED_EVIDENCE | REJECT
adversarial_findings:
- id: A<n>
  lens: <short lens name>
  issue: <readable issue in Russian; name the approval claim, the weak proof or contradiction, and the decision consequence>
  evidence: <section/table/FAQ/appendix source plus the concrete fact, number, date, dependency, or wording that proves the issue>
  severity: HIGH | MEDIUM | LOW
  promotion_test: <why this changes what can be safely approved now, or why it should remain a non-promoted concern>
```

Rules:

- write `issue`, `evidence`, and `promotion_test` in Russian by default
- do not output an issue only because a lens exists
- do not output generic concerns that could be said about any initiative
- every `HIGH` or `MEDIUM` finding must contain concrete document evidence and explain how it changes what can be safely approved now
- use `LOW` for useful but non-blocking improvements, especially when the concern is plausible but not proven by the document
- prefer fewer, sharper findings over broad lists of speculative concerns
- if Layer 3 finds no decision-relevant adversarial issue, write one `No material adversarial issue` record with `severity: LOW`
