# Verdict Policy

## Vocabulary

Final decisions and layer-level rollups use exactly one of:

- `APPROVE`
- `NEED_EVIDENCE`
- `REJECT`

Layer 1 dimensions and Layer 2 Atomic checks blocks use exactly one of:

- `PASS`
- `PARTIAL`
- `FAIL`

Layer 2 atomic answers use exactly one of:

- `YES`
- `PARTIAL`
- `NO`

## Definitions

### What counts as a blocker

Treat an issue as blocker-grade when:

- the document does not provide the logic or evidence needed to make a safe gate decision
- the available data is not sufficient to support the stated decision or conclusion
- the available data and the conclusion drawn from it contradict each other
- rollout realism depends on unresolved foundational dependencies

### What counts as an evidence gap

Treat an issue as `NEED_EVIDENCE` when:

- the available proof is too weak for a decision-ready conclusion
- the logic of the document is directionally coherent, but one or two key proof points are still missing
- the claims may be plausible, but the current evidence does not make them decision-safe

### Evidence ladder

Classify evidence for central claims in this order of strength:

1. `hard evidence / observed product behavior`
2. `experiment / pilot result`
3. `operational signal`
4. `customer feedback / survey / CSAT`
5. `benchmark / competitor reference`
6. `narrative assumption / management belief`

Rules:

- survey, CSAT, benchmark, and qualitative feedback are supporting evidence, not decisive proof on their own
- status statements such as `validated`, `done`, `on track`, or `confirmed` are claims, not evidence
- directional evidence can support only directional conclusions, not definitive approval-ready ones

## Hypothesis validation rules

- do not count a hypothesis as validated if the validation method does not answer the actual decision question
- do not count future tests or planned validation as proof for the current gate
- do not treat optional or opt-in behavior as proof of mandatory or scaled behavior when those are different claims
- if the target is not met and the conclusion is stronger than the fact, treat it as an inconsistency
- if the threshold is missing, a hypothesis may be observed but not fully validated
- if some thresholds exist but the decision-critical claims lack thresholds, treat the threshold evidence as partial rather than validated
- do not infer a Gate 1 validation threshold from later Gate 3 criteria; require the original expected result or threshold for that validation step
- answer `YES` only for threshold sufficiency when thresholds exist for the decision-critical claims, not merely when some thresholds exist
- a hypothesis cannot be treated as validated without `method + threshold + actual result + conclusion consistent with result`

## Evidence quality rules

- do not increase confidence for numbers shown without decision relevance
- do not treat the existence of a pilot or launch as proof of PMF or rollout readiness by itself
- do not treat customer quotes as sufficient proof for central business claims
- when the evidence is only directional, the conclusion must also remain directional
- if take rate, price, commission, subsidy, or monetization terms change across horizons, evidence for the current value does not validate the changed value
- changed value assumptions require their own support; otherwise they remain directional or speculative
- if equal or stable commission/take-rate economics are used to dismiss cannibalization risk, but the document later assumes a lower target commission, lower price, subsidy, or changed monetization term, record a contradiction rather than only an unsupported changed-value issue

## Completeness of blockers

- appendix, FAQ, legal, compliance, anti-fraud, moderation, analytics comments, support tables, and operating notes are first-class evidence
- if the main narrative says `ready`, `done`, or `blockers removed`, but supporting sections show unresolved dependencies, trust the supporting sections
- legal, compliance, anti-fraud, moderation, operational tooling, and integration constraints can be blocker-grade even when they sit outside the main narrative
- if cancellation, fraud, AML, regulator, or abuse break conditions use inconsistent thresholds across sections, name the specific threshold conflict

## Severity calibration

- `HIGH`: breaks the decision thesis or makes approval unsafe
- `MEDIUM`: materially weakens trust in a substantial part of the case
- `LOW`: improvement only, not gate-blocking if the rest of the evidence is strong

Only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues should be promoted into final blockers.

## Layer 1 dimension policy

Layer 1 is the primary decision-critical review.

Assign `FAIL` to a Layer 1 dimension when the document has a blocker-grade failure in that dimension.

Examples:

- the document does not allow the reviewer to reconstruct a reliable `Gate 1 hypothesis -> expected result -> fact -> conclusion` chain
- the segment -> pain -> solution logic is broken
- the roadmap depends on unresolved foundational dependencies
- the traction logic is not reconstructable from evidence

Assign `PARTIAL` when the logic is directionally coherent but the proof is insufficient.

For Gate 1 hypothesis coverage specifically:

- do not require a separately titled Gate 1 section if the hypothesis chain is explicit enough to reconstruct elsewhere
- prefer `PARTIAL` over `FAIL` when the hypotheses are present but fragmented, partially incomplete, or supported only directionally
- prefer `FAIL` when the hypotheses cannot be reliably restored, when the method does not test the thesis, or when the stated status materially contradicts the facts shown

Assign `PASS` when the dimension is decision-ready and does not contain blocker-grade gaps.

## Layer 2 atomic-to-block policy

Layer 2 evaluates atomic questions as `YES`, `PARTIAL`, or `NO`, after reasoning internally in `PASS / PARTIAL / FAIL`, then aggregates them into one Atomic checks block status.

Assign the Layer 2 Atomic checks block status as follows:

- `FAIL` if the atomic failures expose a blocker-grade contradiction, missing proof, broken validation method, or unresolved foundational dependency that would independently block approval
- `PARTIAL` if the block is mostly coherent but one or two decision-critical proof points remain incomplete
- `PASS` if the atomic review does not reveal blocker-grade or material evidence gaps

Use judgment, but prefer consistency over generosity.

Layer 2 breadth calibration:

- do not let high-recall diagnostic breadth alone force `REJECT`
- repeated atomic failures from the same issue family count as one decision problem for verdict aggregation
- when many Layer 2 failures are generic checklist weaknesses but the product logic is directionally coherent, prefer `NEED_EVIDENCE` unless there is a blocker that makes the current gate unsafe

## Layer verdict aggregation

Apply these rules separately to Layer 1 and Layer 2 using their dimension / Atomic checks block statuses:

- if `FAIL` blocks are `2 or more` -> layer verdict = `REJECT`
- if `FAIL` blocks are exactly `1` -> layer verdict = `NEED_EVIDENCE`
- if `PARTIAL` blocks are more than half of all blocks -> layer verdict = `NEED_EVIDENCE`
- otherwise -> layer verdict = `APPROVE`

When applying these thresholds, first consolidate repeated `FAIL` blocks that are driven by the same issue family; if the consolidated decision problem is removable by concrete evidence or validation and the rest of the logic is directional, the layer verdict may remain `NEED_EVIDENCE`.

After duplicate-family consolidation, a final verdict may override raw layer `REJECT` to final `NEED_EVIDENCE` when failures are mostly evidence-remediable and the initiative is not structurally impossible or unsafe.

## Final verdict synthesis

Use the raw layer verdicts as hard inputs. Keep the raw layer verdicts intact as diagnostic outputs.

### `APPROVE`

Assign only if all of the following are true:

- the document is a full Gate 2 document rather than a fragment
- Layer 1 = `APPROVE`
- Layer 2 = `APPROVE`
- the key logic chain is closed
- central hypotheses are reflected and tested with suitable methods
- evidence is sufficient for the main claims
- substantial contradictions are absent
- roadmap and dependencies are realistic
- blocker-grade issues are absent

### `NEED_EVIDENCE`

Assign when:

- the idea still appears viable
- the overall logic could still hold
- but one or two key proof points are not yet closed
- or there is a limited number of decision-critical blockers that can plausibly be removed by concrete evidence or validation
- prefer `NEED_EVIDENCE` when the product logic is directionally coherent and the main weakness is missing proof, unclosed validation, or unproven scale readiness

### `REJECT`

Assign when any of the following is true:

- Layer 1 = `REJECT`
- Layer 2 = `REJECT`
- the central logic is broken
- key hypotheses are not represented or not actually tested
- the evidence does not support the core claims
- the validation method misses the main thesis
- the roadmap depends on unresolved foundational blockers
- contradictions are systematic rather than local

Reject calibration:

- reserve `REJECT` for blockers that make the current gate unsafe even after feasible evidence collection
- do not assign `REJECT` solely because the diagnostic layers found many plausible extra concerns
- if the main issue family is evidence insufficiency and the initiative could be re-evaluated with concrete validation, prefer `NEED_EVIDENCE` over `REJECT`

## Promotion rule for final summary

The final summary is stricter than the layer sections:

- only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues may appear in `blockers`
- non-blocking weaknesses must remain in Layer 1 / Layer 2 details
- if final verdict = `APPROVE`, include only non-mandatory `critical_improvements`

When blocker-grade issues are promoted after merge:

- each final blocker should appear only once
- each final blocker should identify its origin as one of:
  - `covered_by_l2`
  - `novel_from_l1`
  - `confirmed_by_both`
- promotion should use the merged interpretation of overlapping Layer 1 and Layer 2 issues, not duplicate raw issue text

## Confidence guidance

Use:

- `LOW` when the input is fragmentary, when key hypotheses cannot be safely checked, or when decision-critical linkages are missing
- `MEDIUM` when the document is full, but part of the central conclusion rests on weak evidence, unresolved dependencies, or material inconsistencies
- `HIGH` only when the document is full, key hypotheses are testable and actually tested, major contradictions are absent, and blockers are immaterial

If the user provided only a fragment rather than a full Gate 2 document:

- prefer refusing a full final verdict
- if a fragment review is still requested, force `LOW` confidence
- explicitly mark the result as provisional and incomplete
