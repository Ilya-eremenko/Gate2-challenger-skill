# Synthesis Contract

## Purpose

The synthesizer combines broad Layer 1 judgment, detailed Layer 2 evidence, and Layer 3 adversarial committee-risk findings.

It is not a fourth independent review pass. Its job is to merge, explain, deduplicate, and promote.

## Inputs

The synthesizer reads:

- `layer_1`
- `layer_2`
- `layer_3`
- Layer 2 Atomic checks block statuses embedded in `layer_2`
- the canonical block names shared across the layers
- the fragment / full-document flag determined by the coordinator

The synthesizer must treat these layer artifacts as the primary evidence source for merge decisions.

## Merge statuses by block

For each block, assign exactly one merge status:

- `CONFIRMED` when Layer 2 confirms the main Layer 1 status
- `REFINED` when Layer 1 is directionally correct but Layer 2 adds important detail or sharper evidence
- `DOWNGRADED` when Layer 1 was too optimistic and Layer 2 exposes a blocker-grade contradiction, missing proof, or unresolved dependency
- `CONFLICT` when the layers materially disagree and the difference must be explained explicitly

`why_difference` is required for `DOWNGRADED` and `CONFLICT`.

## Override rules

Layer 2 may refine or override Layer 1 only when it introduces explicit evidence of one of the following:

- a blocker-grade contradiction
- missing proof for a key claim or conclusion
- a validation method that does not test the actual thesis
- a causal chain that cannot be restored without inference
- an unresolved foundational dependency or readiness constraint

Layer 2 must not override Layer 1 when:

- the difference is only stylistic or wording-level
- the difference is local and non-blocking
- the additional detail does not materially change the decision safety of the block

## Preserving the value of Layer 1

Layer 1 is an open-world, broad review of the decision narrative.

This means:

- Layer 1 may raise a cross-sectional blocker even if no single Layer 2 atomic question captures it directly
- the synthesizer must preserve such an issue as `novel_from_l1` when it remains decision-relevant after merge
- the synthesizer must not discard a Layer 1 issue solely because Layer 2 did not ask the exact same question

## Preserving the value of Layer 3

Layer 3 is a prompt-first adversarial review of business, governance, accounting, attribution, incentive, operating-model, and committee-risk weaknesses.

This means:

- Layer 3 may raise an issue as `novel_from_l3` when the issue is not already captured by Layer 1 or Layer 2
- the synthesizer may promote `novel_from_l3` only when the finding has concrete document evidence and changes what can be safely approved now
- the synthesizer must not promote a Layer 3 finding only because it is uncomfortable, plausible, or rhetorically strong
- do not promote generic adversarial concerns that are not anchored in the document's own numbers, commitments, roadmap, stakeholder comments, economics, or evidence gaps
- if a Layer 3 issue is useful but not decision-changing, keep it as a critical improvement or diagnostic note rather than a final blocker

## Supporting-section priority

Supporting sections have the same evidentiary weight as the main narrative.

Apply these rules:

- if appendix, FAQ, legal, compliance, anti-fraud, moderation, analytics notes, support tables, or ops notes reveal unresolved blockers, treat that evidence as fully decision-relevant
- if the main narrative says `ready`, `done`, or `validated`, but supporting sections materially contradict it, the merged interpretation must reflect the contradiction
- compare main narrative confidence with supporting-section confidence; a material confidence mismatch is itself a consistency signal when the decision depends on the disputed claim
- preserve the confidence mismatch in `merged_block_assessment` when supporting sections are materially more cautious than the main narrative
- when target, fact, and conclusion disagree, prefer the factual evidence over the narrative summary

## Deduplication rules

The final summary must not contain duplicate blockers.

Apply these rules:

- if Layer 1 and Layer 2 describe the same underlying blocker, merge them into one final blocker
- merged blockers may cite multiple source refs from different layers
- if the issues are meaningfully different, do not merge them merely because they belong to the same block
- final blocker promotion must use the merged interpretation, not a raw copy of every layer issue

## Final synthesis constraints

The synthesizer must:

- preserve raw Layer 1 dimension statuses and Layer 2 Atomic checks block statuses as separate diagnostic outputs
- preserve raw `layer_3` findings as diagnostic outputs
- use `merged_block_assessment` only for explanation, deduplication, and blocker promotion
- compute the final verdict from the raw layer verdicts according to `verdict-policy.md`
- after duplicate-family consolidation, override raw layer `REJECT` to final `NEED_EVIDENCE` when failures are mostly evidence-remediable and the initiative is not structurally impossible or unsafe
- promote only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues
- avoid inventing new blocker causes that are absent from both the document evidence and the layer artifacts
- before promoting a Layer 3 issue, verify that its `promotion_test` explains the approval consequence rather than only naming an adversarial lens
