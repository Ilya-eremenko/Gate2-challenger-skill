# Verdict Policy

## Verdict vocabulary

Every block-level, layer-level, and final decision must use exactly one of:

- `APPROVE`
- `NEED_EVIDENCE`
- `REJECT`

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
- a hypothesis cannot be treated as validated without `method + threshold + actual result + conclusion consistent with result`

## Evidence quality rules

- do not increase confidence for numbers shown without decision relevance
- do not treat the existence of a pilot or launch as proof of PMF or rollout readiness by itself
- do not treat customer quotes as sufficient proof for central business claims
- when the evidence is only directional, the conclusion must also remain directional

## Completeness of blockers

- appendix, FAQ, legal, compliance, anti-fraud, moderation, analytics comments, support tables, and operating notes are first-class evidence
- if the main narrative says `ready`, `done`, or `blockers removed`, but supporting sections show unresolved dependencies, trust the supporting sections
- legal, compliance, anti-fraud, moderation, operational tooling, and integration constraints can be blocker-grade even when they sit outside the main narrative

## Severity calibration

- `HIGH`: breaks the decision thesis or makes approval unsafe
- `MEDIUM`: materially weakens trust in a substantial part of the case
- `LOW`: improvement only, not gate-blocking if the rest of the evidence is strong

Only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues should be promoted into final blockers.

## Layer 1 block policy

Layer 1 is the primary decision-critical review.

Assign `REJECT` to a Layer 1 block when the document has a blocker-grade failure in that block.

Examples:

- the document does not allow the reviewer to reconstruct a reliable `Gate 1 hypothesis -> expected result -> fact -> conclusion` chain
- the segment -> pain -> solution logic is broken
- the roadmap depends on unresolved foundational dependencies
- the traction logic is not reconstructable from evidence

Assign `NEED_EVIDENCE` when the logic is directionally coherent but the proof is insufficient.

For Gate 1 hypothesis coverage specifically:

- do not require a separately titled Gate 1 section if the hypothesis chain is explicit enough to reconstruct elsewhere
- prefer `NEED_EVIDENCE` over `REJECT` when the hypotheses are present but fragmented, partially incomplete, or supported only directionally
- prefer `REJECT` when the hypotheses cannot be reliably restored, when the method does not test the thesis, or when the stated status materially contradicts the facts shown

Assign `APPROVE` when the block is decision-ready and does not contain blocker-grade gaps.

## Layer 2 atomic-to-block policy

Layer 2 evaluates atomic questions as `YES` or `NO`, after reasoning internally in `PASS / PARTIAL / FAIL`, then aggregates them into one block verdict.

Assign the Layer 2 block verdict as follows:

- `REJECT` if the atomic failures expose a blocker-grade contradiction, missing proof, broken validation method, or unresolved foundational dependency that would independently block approval
- `NEED_EVIDENCE` if the block is mostly coherent but one or two decision-critical proof points remain incomplete
- `APPROVE` if the atomic review does not reveal blocker-grade or material evidence gaps

Use judgment, but prefer consistency over generosity.

## Layer verdict aggregation

Apply these rules separately to Layer 1 and Layer 2 using their block verdicts:

- if `REJECT` blocks are `2 or more` -> layer verdict = `REJECT`
- if `REJECT` blocks are exactly `1` -> layer verdict = `NEED_EVIDENCE`
- if `NEED_EVIDENCE` blocks are more than half of all blocks -> layer verdict = `NEED_EVIDENCE`
- otherwise -> layer verdict = `APPROVE`

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
