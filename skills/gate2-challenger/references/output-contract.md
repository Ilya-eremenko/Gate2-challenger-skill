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
- Default to 1-2 Layer 1 issues per dimension
- Use 3 issues only when there are three independent decision blockers that are not evidence for each other
- only decision-relevant issues
- Layer 1 may raise a cross-sectional dimension-level issue when the decision narrative breaks across sections
- every issue should preserve the specific decision test behind the problem instead of only an umbrella diagnosis
- use separate Layer 1 issues for the same root cause only when each issue has a distinct decision consequence; otherwise do not repeat it as a new issue
- bundle related Layer 2-level observations under a broader Layer 1 decision blocker when they support one gate failure
- keep missed funnel thresholds, buyer/seller activation misses, the optional-pilot-to-mandatory-rollout leap, planning statements treated as validation, and take-rate / monetization assumption changes as evidence under the broad Layer 1 issue unless each has a distinct decision consequence
- Prefer one broad Layer 1 traction issue for model reconstructability; treat a changed 10% -> 15% monetization or take-rate assumption as evidence under that issue unless it is the only material traction weakness
- when MLP and end-state path are not explicit enough, write the issue as `MLP/end-state journey is missing or not evaluable`; in Solution state that it makes adoption behavior untestable, and in Scope state that it makes test-vs-rollout readiness impossible to judge
- useful specific tests include missing threshold, missing user journey, unmet success criterion, unreconciled topline, or unresolved prerequisite
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
- answer `PARTIAL` or `NO` only when the issue changes approval safety, validation strength, or the block verdict
- if an atomic check finds only a plausible nuance, generic completeness concern, or already-covered concern, answer `YES` with `No material issue` or use `same duplicate family; local angle:`
- suppress non-central extras unless the document's decision thesis depends on that point
- answer every atomic check internally, but emit a standalone Layer 2 issue only when the weakness is concrete, decision-relevant, and not already represented by a stronger nearby issue
- generic weak-link checks default to `YES` / `No material issue` unless there is a specific contradiction, threshold miss, formula gap, unresolved dependency, unsupported scaling leap, or inconsistent risk control
- do not emit generic standalone issues for broad target clarity, segment mapping, projected upside, softer alternatives, or downside sensitivity when they only restate a stronger nearby issue
- Layer 2 output budget: emit at most the two strongest distinct issue families per Atomic checks block
- additional atomic checks should reference the selected family in evidence rather than create another issue
- assign a duplicate-family key before writing Layer 2 output; examples include `dependency-readiness`, `proxy-validation`, `monetization-contradiction`, `cancellation-boundary`, `threshold-mismatch`, `model-reconstructability`, `segment-path-mixing`, and `risk-control-maturity`
- selected issue families are a pre-output control, not an optional writing style
- only the selected representative atomic answer gets full standalone issue text
- non-selected repeated atomic answers must use `same duplicate family; see <family>`
- do not add a second local-angle issue sentence for the same family
- every atomic question must still be answered against its own decision test
- if there is concrete evidence for a problem-bearing atomic check, record the issue even when the same family is also covered elsewhere
- when a problem-bearing atomic check repeats the same family, use `same duplicate family; local angle:` only when the local consequence is materially different; do not turn the issue into `YES` / `No material issue` if that would hide a real decision defect, but do not create a second standalone issue for the same defect
- avoid restating the same insight as separate standalone failures; if a repeated concern is relevant, state the local angle only, for example "same prerequisite gap, here specifically affecting test-vs-rollout gating"
- if an insight repeats the same duplicate family, reference it as evidence rather than a new `issue`
- if the same duplicate family repeats and a local consequence must still be recorded, write `same duplicate family; local angle:` and use that prefix before the block-specific consequence; do not create a fresh standalone issue
- duplicate family examples: central closure not tested; end-state path/API gap; projected ramp not explained by validated inputs; 10% evidence does not validate 15% monetization; mitigations are plans, not controls
- monetization/cannibalization contradiction can appear in Traction and Consistency when local consequences differ: Traction: model economics are unsupported or internally inconsistent; Consistency: risk defense contradicts target economics; use local-angle wording to avoid duplicate penalties
- preserve exact threshold mechanics, the specific row, year, driver, or formula detail, and fraud and lower-commission mechanics when those details determine whether a match is partial or complete
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
