# Output Contract

## Output modes

Accepted user-facing modes:

- `standard`
- `extended`

Internal formatting aliases:

- `standard` -> `summary`
- `extended` -> `detailed`

The skill must also support:

- `debug stages`: `on` or `off`
- default is `off`

Internal reasoning artifacts such as the hypothesis ledger, evidence ladder, dependency map, and consistency matrix remain hidden unless the user explicitly asks for internal reasoning dumps. Their existence must not change the external output schema below.

## Status vocabulary

Final verdicts use:

- `APPROVE`
- `NEED_EVIDENCE`
- `REJECT`

Layer 1 dimensions and Layer 2 Atomic checks blocks use:

- `PASS`
- `PARTIAL`
- `FAIL`

Layer 2 atomic answers use:

- `YES`
- `PARTIAL`
- `NO`

Issue severity uses:

- `HIGH`
- `MEDIUM`
- `LOW`

## Summary mode

In `summary` mode, output only the final synthesis section.

### Final synthesis format

```text
verdict: APPROVE | NEED_EVIDENCE | REJECT
confidence: HIGH | MEDIUM | LOW
blockers:
- blocker_id: B<n>
  block: <canonical block name>
  severity: HIGH | MEDIUM | LOW
  reason: <short blocker statement>
  origin: covered_by_l2 | novel_from_l1 | confirmed_by_both
  evidence:
    - <quote / section / fragment reference>

critical_improvements:
- improvement_id: I<n>
  block: <canonical block name>
  suggestion: <non-blocking but high-value improvement>
  evidence:
    - <quote / section / fragment reference>
```

Rules:

- only blocker-grade issues may appear in `blockers`
- non-blocking weaknesses must not appear in `blockers`
- if final verdict is `APPROVE`, include `critical_improvements`
- `critical_improvements` are important but non-mandatory
- do not include internal layer refs in the final synthesis; keep them only in diagnostic sections
- when the review is fragmentary, keep the wording explicitly provisional and force `LOW` confidence

## Detailed mode

In `detailed` mode, output:

1. final synthesis
2. one `Input Doc` line
3. normalized Layer 1
4. normalized Layer 2
5. merged block assessment

If `debug stages = on`, keep Layer 1, Layer 2, and merged block assessment explicitly visible as separate sections even if the user asks for a compact diagnostic response.

## Normalized Layer 1 format

Layer 1 output must match the normalized benchmark format.

```text
**Input Doc:** [INPUT_DOC_URL](INPUT_DOC_URL)

## Layer 1

verdict: APPROVE | NEED_EVIDENCE | REJECT
dimension:

### Problem framing and segments: PASS | PARTIAL | FAIL

- id: 1
  issue: <short decision-relevant issue>
  evidence: <quote / section / fragment reference>
  severity: HIGH | MEDIUM | LOW
```

Rules:

- print the `Input Doc` line once before `## Layer 1`
- the `verdict` line in this section is the Layer 1 rollup verdict, not a second independent final verdict
- use exactly seven dimensions in the canonical order
- dimension status must be `PASS`, `PARTIAL`, or `FAIL`
- max 3 issues per dimension
- only decision-relevant issues
- Layer 1 may raise a cross-sectional dimension-level issue when the decision narrative breaks across sections
- if dimension status is `PASS`, output only non-blocking residual issues, or one `No material issue` record when there is no meaningful weakness
- every issue must contain `id`, `issue`, `evidence`, and `severity`

## Normalized Layer 2 format

Layer 2 output must match the normalized benchmark format.

```text
## Layer 2

### Atomic checks - Problem framing and segments: PASS | PARTIAL | FAIL

- question: <full atomic question>
  answer: YES | PARTIAL | NO
  evidence: <quote / section / fragment reference>
  issue: <gap, weakness, or "No material issue">
```

Rules:

- use exactly seven Atomic checks blocks in the canonical order
- Atomic checks block status must be `PASS`, `PARTIAL`, or `FAIL`
- every atomic question must be present
- every atomic answer must be `YES`, `PARTIAL`, or `NO`
- `issue` is always required
- use `No material issue` only when answer is `YES` and there is no meaningful weakness
- the Atomic checks block status is the Layer 2 aggregate for that block; do not output a separate aggregate section

## Merged block assessment format

```text
merged_block_assessment:
- block: <canonical block name>
  l1_status: PASS | PARTIAL | FAIL
  l2_status: PASS | PARTIAL | FAIL
  agreement_status: CONFIRMED | REFINED | DOWNGRADED | CONFLICT
  merged_interpretation: <short resolved statement>
  why_difference: <required for DOWNGRADED | CONFLICT>
  blocker_origin: covered_by_l2 | novel_from_l1 | confirmed_by_both | none
  merged_sources:
    - layer: L1 | L2
      ref: <issue id | question text>
```

Rules:

- `agreement_status` is required for every block
- `why_difference` is required when `agreement_status` is `DOWNGRADED` or `CONFLICT`
- `merged_block_assessment` explains how broad Layer 1 judgment and detailed Layer 2 evidence were reconciled
- `merged_block_assessment` does not replace the raw Layer 1 and Layer 2 outputs

## Canonical block names

Use exactly these seven block names in Layer 1, Layer 2, and merged block assessment:

1. Problem framing and segments
2. Solution quality and logic
3. Scope of work and implementation plan
4. Success criteria and metrics
5. Traction model credibility
6. Key assumptions and risks completeness
7. Consistency
