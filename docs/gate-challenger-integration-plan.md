# Gate Challenger Integration Plan

## Objective

Expand the previous `gate2-challenger` skill into one `gate-challenger` skill that:

1. normalizes the input document once
2. detects the gate / review stage
3. applies shared review rules once
4. routes to the correct stage-specific rubric
5. synthesizes a blocker-first verdict with stage-aware approval scope

Gate 2 and Gate 3 should share the same evidence standard, output contract, synthesis logic, duplicate-family logic, and adversarial review mechanics. Only stage-specific decision tests should live in stage-specific rubric files.

## Implemented State

The package has been migrated to a routed Gate Challenger shape:

- `skills/gate-challenger/SKILL.md` routes documents by stage before running review layers
- `references/stage-detection.md` defines Gate 2 / Gate 3 / fragment / unknown routing
- `references/gate-2-rubric.md` preserves the previous Gate 2 Layer 1 and Layer 2 checks in one stage file
- `references/gate-3-rubric.md` contains Gate 3-specific decision tests
- `references/common-output-contract.md`, `references/common-synthesis-contract.md`, `references/common-verdict-policy.md`, and `references/common-adversarial-rubric.md` hold shared review mechanics

The Gate 3 rubric is staged in:

- `skills/gate-challenger/references/gate-3-rubric.md`

## Target Package Shape

Recommended final layout:

```text
skills/gate-challenger/
  SKILL.md
  references/
    common-evidence-standard.md
    common-output-contract.md
    common-synthesis-contract.md
    common-verdict-policy.md
    common-adversarial-rubric.md
    stage-detection.md
    gate-2-rubric.md
    gate-3-rubric.md
  scripts/
    check_git_freshness.py
    pdf_to_md_docling.py
```

During migration, keep the existing directory until tests and prompts are updated. Rename only after the new routing behavior is verified.

## Common Layer Extraction

Move gate-neutral material out of the current Gate 2 files.

### Common Evidence Standard

Extract:

- do not reward section headers without logic
- prefer consistency over surface completeness
- distinguish validated evidence from narrative assumptions
- evidence ladder
- hypothesis validation rules
- dependency map rules
- consistency matrix rules
- supporting sections as first-class evidence
- duplicate-family consolidation rules
- Russian language rule for human-facing analysis

### Common Output Contract

Keep shared:

- `verdict`
- `confidence`
- `document_stage`
- `stage_detection`
- Layer 1 / Layer 2 / Layer 3 diagnostic outputs
- merged block assessment
- final blockers
- critical improvements
- evidence needed

Add stage-aware fields:

- `approval_scope`
- `not_approved_scope`
- `next_gate_conditions`

For Gate 3, map these to:

- `approved_scope`
- `not_approved_scope`
- `gate_4_conditions`

### Common Synthesis Contract

Keep:

- Layer 1 / Layer 2 / Layer 3 merge rules
- blocker promotion rules
- duplicate blocker merge rules
- Layer 3 promotion test

Make vocabulary gate-neutral:

- replace hardcoded `Gate 2` with `current gate`
- replace `Gate 1 hypothesis` with `prior gate hypotheses / commitments` unless a Gate 2-specific rubric requires Gate 1

### Common Adversarial Rubric

Keep universal lenses:

- accounting / governance
- attribution
- incentives
- operational failure modes
- evidence laundering
- scenario gaming
- metric gaming / quality of growth
- hidden downside / compound risks
- organizational constraints
- stakeholder misalignment
- scope creep
- ask vs proof mismatch

Move Gate 2-only examples into `gate-2-rubric.md`.

Add Gate 3-only lenses from `gate-3-rubric.md`.

## Stage Detection

Create `references/stage-detection.md` with deterministic routing guidance.

Recommended output:

```text
document_stage: GATE_2 | GATE_3 | UNKNOWN | FRAGMENT
stage_confidence: HIGH | MEDIUM | LOW
stage_evidence:
- <section/table/phrase proving the stage>
stage_conflicts:
- <signals that point to another stage, if any>
routing_decision: gate_2_rubric | gate_3_rubric | ask_user | fragment_review
```

Gate 2 signals:

- title contains `Gate 2`
- current review is Gate 2
- FAQ asks for estimated date and success criteria for Gate 3
- document focuses on Gate 1 continuity, planned traction, MLP / end-state scope, initial risks, and Gate 3 commitments

Gate 3 signals:

- title contains `Gate 3`
- current review is Gate 3
- previous review is Gate 2
- FAQ asks about progress on last commitments / MLP
- FAQ asks for PMF criteria and Gate 4
- FAQ asks for customer experience
- Gate 3 Traction YTD thresholds are present: Green <= 10%, Yellow 10%-30%, Red > 30%
- document asks for next deep dive before Gate 4 or baseline transfer

Ambiguity rule:

- If title and body disagree, prefer body evidence and report the conflict.
- If stage remains uncertain after normalization, do not guess. Ask the user whether to run Gate 2 or Gate 3 rubric.
- If the input is fragmentary, run only a provisional fragment review with `confidence: LOW`.

## Gate 2 Refactor

Rename current Gate 2-specific files logically:

- `layer-1-rubric.md` -> `gate-2-rubric.md` or merge Layer 1 / Layer 2 into one stage file
- keep Gate 2-specific checks for:
  - Gate 1 continuity
  - problem framing and segments
  - solution quality and logic
  - MLP / end-state scope
  - planned traction
  - Gate 3 success criteria

Avoid copying common rules into the Gate 2 rubric after extraction.

## Gate 3 Addition

Use `references/gate-3-rubric.md` as the starting Gate 3 stage file.

Gate 3-specific emphasis:

- Gate 2 commitment ledger
- production / MLP evidence
- customer experience and feedback closure
- post-MLP learning and new hypotheses
- PMF criteria
- Gate 4 path
- baseline transition
- support scenario
- traction / financial delta since Gate 2
- approval carry-forward
- validation traffic-light reconciliation

## SKILL.md Workflow Update

Rewrite the high-level workflow as:

1. Coordinator normalizes input and checks freshness
2. Coordinator determines full document vs fragment
3. Coordinator detects stage using `stage-detection.md`
4. Coordinator loads common evidence / output / verdict rules
5. Coordinator loads stage-specific rubric:
   - Gate 2 -> `gate-2-rubric.md`
   - Gate 3 -> `gate-3-rubric.md`
6. Layer 1 evaluates decision-critical stage dimensions
7. Layer 2 evaluates stage atomic checks
8. Layer 3 evaluates common adversarial lenses plus stage-specific lenses
9. Synthesizer merges outputs and returns a stage-aware verdict

## Tests And Benchmarks

Add instruction tests before changing behavior:

- Gate 2 document routes to Gate 2 rubric
- Gate 3 document routes to Gate 3 rubric
- mixed title/body stage signals produce a conflict and cautious routing
- fragment input does not receive a full gate verdict
- Gate 3 output includes approval scope and Gate 4 conditions
- Gate 3 customer experience gaps are not swallowed by generic product metrics
- common checks are not duplicated as repeated final blockers

Likely test locations:

- `skillbench/tests/test_gate2_challenger_instructions.py`
- new test file `skillbench/tests/test_gate_challenger_stage_routing.py`

## Migration Steps

1. Add Gate 3 rubric reference file. Completed.
2. Add tests for stage detection and Gate 3 output expectations. Completed.
3. Extract common evidence / verdict / synthesis material into common reference files. Partially completed: verdict, synthesis, output, and adversarial mechanics are common; common evidence remains in `SKILL.md` and stage rubrics.
4. Convert current Gate 2 Layer 1 and Layer 2 files into a Gate 2 stage rubric. Completed.
5. Add `stage-detection.md`. Completed.
6. Rewrite `SKILL.md` around routing rather than assuming Gate 2. Completed.
7. Update output contract with `document_stage`, `approval_scope`, `not_approved_scope`, and `next_gate_conditions`. Completed.
8. Update benchmark / skillbench expectations. Completed for instruction tests and orchestrator naming.
9. Rename package directory from `gate2-challenger` to `gate-challenger`. Completed.
10. Update README install instructions and skill metadata. Completed.
11. Run tests and a dry review on one Gate 2 document, then compare with prior results. In progress.

## Open Decisions

- Whether to keep Layer 1 and Layer 2 as separate files per gate or combine each gate into one `gate-N-rubric.md`.
- Whether final public output should always show `approved_scope` / `not_approved_scope`, or only for Gate 3 and later.
- Whether `Gate 2` should preserve the old output schema exactly for backward benchmark compatibility.
- Whether the installed personal skill should be renamed immediately or after benchmark parity is confirmed.
