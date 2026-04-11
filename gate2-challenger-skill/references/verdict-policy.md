# Verdict Policy

## Verdict vocabulary

Every block-level and layer-level decision must use exactly one of:

- `APPROVE`
- `NEED_EVIDENCE`
- `REJECT`

## Definitions

### What counts as a blocker

Treat an issue as blocker-grade when:

- the document does not provide the data needed to make a decision
- the available data is not sufficient to support the stated decision or conclusion
- the data and the conclusions drawn from that data contradict each other

### What counts as an evidence gap

Treat an issue as `NEED_EVIDENCE` when:

- the available proof is too weak for a decision-ready conclusion
- the logic of the document cannot be restored without filling gaps by inference
- the claims may be directionally plausible, but they are not decision-safe without stronger support

### What does not count as evidence

Do not treat the following as evidence:

- claims or conclusions without research, measurements, or concrete numbers behind them
- status statements such as `on track` or `done` when only the current metric is shown but the target is missing
- phrases like `we checked` or `we validated` without method, result, and conclusion
- isolated numbers that do not prove causality, model quality, or decision validity on their own

## Layer 1 block policy

Layer 1 is the primary decision-critical review.

Assign `REJECT` to a Layer 1 block when the document has a blocker-grade failure in that block.

Examples:

- the document does not contain an explicit Gate 1 hypotheses block
- the segment -> pain -> solution logic is broken
- the roadmap and metrics contradict the claimed impact mechanism
- the traction logic is not reconstructable

Assign `NEED_EVIDENCE` when the logic is directionally coherent but the proof is insufficient.

Assign `APPROVE` when the block is decision-ready and does not contain blocker-grade gaps.

## Layer 2 atomic-to-block policy

Layer 2 evaluates atomic questions as `YES` or `NO`, then aggregates them into one block verdict.

Assign the Layer 2 block verdict as follows:

- `REJECT` if the atomic failures expose a blocker-grade contradiction, omission, or missing proof that would independently block approval
- `NEED_EVIDENCE` if the block is mostly coherent but lacks enough evidence, specificity, or causal support
- `APPROVE` if the atomic review does not reveal blocker-grade or material evidence gaps

Use judgment, but prefer consistency over generosity.

## Layer verdict aggregation

Apply these rules separately to Layer 1 and Layer 2 using their block verdicts:

- if `REJECT` blocks are `2 or more` -> layer verdict = `REJECT`
- if `REJECT` blocks are exactly `1` -> layer verdict = `NEED_EVIDENCE`
- if `NEED_EVIDENCE` blocks are more than half of all blocks -> layer verdict = `NEED_EVIDENCE`
- otherwise -> layer verdict = `APPROVE`

## Final verdict synthesis

Synthesize the final verdict from the two layer verdicts:

- if Layer 1 = `REJECT` or Layer 2 = `REJECT` -> final verdict = `REJECT`
- else if Layer 1 = `NEED_EVIDENCE` or Layer 2 = `NEED_EVIDENCE` -> final verdict = `NEED_EVIDENCE`
- else -> final verdict = `APPROVE`

## Promotion rule for final summary

The final summary is stricter than the layer sections:

- only blocker-grade issues may appear in `blockers`
- non-blocking weaknesses must remain in Layer 1 / Layer 2 details
- if final verdict = `APPROVE`, include only non-mandatory `critical_improvements`

## Confidence guidance

Use:

- `HIGH` when the document contains direct evidence and internal consistency across the main blocks
- `MEDIUM` when the verdict is clear but some evidence is indirect or partial
- `LOW` when the verdict depends on sparse evidence, ambiguous wording, or unresolved internal contradictions

If the user provided only a fragment rather than a full Gate 2 document:

- prefer refusing a full final verdict
- if a fragment review is still requested, force `LOW` confidence
- explicitly mark the result as provisional and incomplete
