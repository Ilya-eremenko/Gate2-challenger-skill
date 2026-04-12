# Output Contract

## Output modes

The skill must ask for output mode if the user did not specify it:

- `summary`
- `detailed`

The skill must also support:

- `debug stages`: `on` or `off`
- default is `off`

## Summary mode

In `summary` mode, output only the final synthesis section.

## Detailed mode

In `detailed` mode, output:

1. final synthesis
2. Layer 1
3. Layer 2
4. Layer 2 aggregate
5. merged block assessment

## Final synthesis format

```text
verdict: APPROVE | NEED_EVIDENCE | REJECT
confidence: HIGH | MEDIUM | LOW
blockers:
- blocker_id: B<n>
  block: <name>
  severity: HIGH | MEDIUM | LOW
  reason: <short blocker statement>
  origin: covered_by_l2 | novel_from_l1 | confirmed_by_both
  evidence:
    - <quote / section / fragment reference>

critical_improvements:
- improvement_id: I<n>
  block: <name>
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

## Layer 1 format

```text
layer_1:
- block: <name>
  verdict: APPROVE | NEED_EVIDENCE | REJECT
  blocker: YES | NO
  top_issues:
    - issue_id: L1-<block>-<n>
      severity: HIGH | MEDIUM | LOW
      issue_description: <short decision-relevant issue>
      evidence:
        - <quote / section / fragment reference>
```

Rules:

- no atomic questions
- max 3 issues per block
- only decision-relevant issues
- Layer 1 may raise a cross-sectional block-level issue when the decision narrative breaks across sections
- if block verdict = `APPROVE`, omit `top_issues`

## Layer 2 format

Atomic section:

```text
layer_2:
- block: <name>
  checks:
    - question_id: L2-<block>-<n>
      question: <full atomic question>
      result: YES | NO
      evidence:
        - <quote / section / fragment reference>
      issue: <required if result = NO>
```

Aggregated section:

```text
layer_2_aggregate:
- block: <name>
  verdict: APPROVE | NEED_EVIDENCE | REJECT
  blocker: YES | NO
  promoted_issues:
    - ref: <question_id>
      severity: HIGH | MEDIUM | LOW
      issue_description: <short summary>
```

Rules:

- atomic checks are always `YES | NO`
- `issue` is required when `result = NO`
- `promoted_issues` summarize the atomic issues that shaped the block verdict

## Merged block assessment format

```text
merged_block_assessment:
- block: <name>
  l1_verdict: APPROVE | NEED_EVIDENCE | REJECT
  l2_verdict: APPROVE | NEED_EVIDENCE | REJECT
  agreement_status: CONFIRMED | REFINED | DOWNGRADED | CONFLICT
  merged_interpretation: <short resolved statement>
  why_difference: <required for DOWNGRADED | CONFLICT>
  blocker_origin: covered_by_l2 | novel_from_l1 | confirmed_by_both | none
  merged_sources:
    - layer: L1 | L2
      ref: <issue_id | question_id>
```

Rules:

- `agreement_status` is required for every block
- `why_difference` is required when `agreement_status` is `DOWNGRADED` or `CONFLICT`
- `merged_block_assessment` explains how broad Layer 1 judgment and detailed Layer 2 evidence were reconciled
- `merged_block_assessment` does not replace the raw layer verdicts

## Debug stages behavior

If `debug stages = on`, keep Layer 1, Layer 2, Layer 2 aggregate, and merged block assessment explicitly visible as separate sections even if the user asks for a more compact diagnostic response.
