---
name: skillbench-orchestrator
description: Use when running a local Codex benchmark loop for improving the gate2-challenger skill with evaluator, judge, and editor subagents, while preserving benchmark integrity and anti-overfitting guardrails.
---

# Skillbench Orchestrator

## Purpose

Run a local `codex-local` benchmark loop for improving `gate2-challenger`.

This skill is an orchestration procedure for Codex. It is not a Python CLI mode. The Python `skillbench` package may list cases and inspect saved artifacts, but the Codex orchestrator is responsible for launching subagents, collecting outputs, writing improvement plans, and enforcing approval gates.

## Defaults

- `benchmark_dir`: `benchmark`
- `case_order`: all discovered cases, processed sequentially
- `approval_gate`: on
- `evaluator_skill`: `gate2-challenger`
- `review_mode`: `extended`
- `debug_stages`: `on`
- `runs_dir`: `skillbench/runs`

## Roles

### Evaluator Agent

Applies `gate2-challenger` to one original document.

Rules:

- Evaluator Agent must not receive the etalon, judge prompt, previous judge result, or expected score.
- Use `review_mode: extended` and `debug stages: on`.
- Run the `gate2-challenger` workflow as the evaluated object, including its Layer 1 worker, Layer 2 worker, and synthesizer.
- Return the full extended output: final synthesis, normalized Layer 1, normalized Layer 2, and merged block assessment.
- Do not propose prompt, skill, rubric, or judge changes.

### Judge Agent

Scores one evaluator output against the benchmark etalon.

Rules:

- Judge Agent receives evaluator output, etalon, and judge prompt.
- Compare only against the etalon and the judge prompt.
- Return score, verdict, matched issues, missed issues, false positives, and explanation.
- Do not propose changes to `gate2-challenger`, the judge prompt, or the benchmark.

### Improvement Planner

The main Codex orchestrator owns this role.

Rules:

- Analyze evaluator output and judge result after each case.
- Separate evaluator-quality issues from judge-measurement issues.
- Write `improvement_plan.md` with proposed changes and anti-overfit reasoning.
- Ask the user to approve the plan before any editor agent changes files.
- Do not start the next case until the current case has either an approved improvement step or an explicit skip decision.

### Prompt/Skill Editor Agent

Applies an approved improvement plan.

Rules:

- Only run after explicit user approval of `improvement_plan.md`.
- May edit `skills/gate2-challenger/SKILL.md`, `skills/gate2-challenger/references/`, and the judge prompt file referenced by the current run.
- Do not edit benchmark originals or etalons unless the approved plan explicitly identifies a benchmark data defect.
- Return `post_change_summary.md` with changed files, rationale, and verification notes.
- Do not revert unrelated user changes.

## Data flow

For each benchmark case:

1. Discover cases with `python3 -m skillbench list-cases --benchmark-dir benchmark` or equivalent local inspection.
2. Create `skillbench/runs/<run-id>/<case>/`.
3. Send only the original document and evaluator settings to Evaluator Agent.
4. Save evaluator output to `evaluator_result.md`.
5. Send evaluator output, etalon, and judge prompt to Judge Agent.
6. Save judge output to `judge_result.md`.
7. Improvement Planner writes `improvement_plan.md`.
8. Approval gate: ask the user whether to apply the plan, skip changes for this case, or stop the run.
9. If approved, send only the approved plan and relevant files to Prompt/Skill Editor Agent.
10. Save applied-change notes to `approved_changes.md` and `post_change_summary.md`.
11. Continue to the next case sequentially.

## Approval gate

Before any file-changing editor work, show the user:

- case name and artifact directory
- judge score and verdict, if available
- evaluator issues to fix
- judge prompt changes, if any
- anti-overfit assessment
- exact files proposed for editing

The default is to wait for user approval. If the user does not approve, do not edit files.

## Anti-overfit rules

- Improve evaluator quality, not just judge score.
- Do not teach `gate2-challenger` to memorize one etalon.
- Prefer general improvements to evidence handling, layer separation, rubric clarity, synthesis, and output contracts.
- Judge prompt changes are allowed only for a measurement error: incorrect scoring, unjustified penalty, missed valid match, unstable application of its own rules, or ambiguous matching policy.
- Never weaken the judge prompt merely because the evaluator got a low score.
- Every judge prompt change must state why the judge was wrong, not why a higher score is desired.
- If a proposed change helps one case but likely harms other cases, mark it as overfit risk and do not apply it by default.

## Artifacts

Write these files under `skillbench/runs/<run-id>/<case>/`:

- `evaluator_result.md`: full extended `gate2-challenger` output.
- `judge_result.md`: judge score, verdict, matches, misses, false positives, and explanations.
- `improvement_plan.md`: planned evaluator and judge improvements with anti-overfit reasoning.
- `approved_changes.md`: user decision and approved scope.
- `metadata.json`: case name, paths, timestamps, role settings, and artifact list.
- `post_change_summary.md`: files changed by the editor agent, rationale, and verification.

## Improvement plan format

Use this structure for `improvement_plan.md`:

```markdown
# Improvement Plan: <case>

## Case Result

- Score:
- Verdict:
- Main evaluator misses:
- Main false positives:

## Evaluator Improvements

- Proposed change:
- General quality reason:
- Files:
- Overfit risk:

## Judge Prompt Corrections

- Proposed change:
- Measurement error:
- Files:
- Overfit risk:

## Rejected Changes

- Rejected change:
- Reason:

## Approval Request

- Apply:
- Skip:
- Stop:
```

## Failure handling

- If evaluator output is incomplete, rerun Evaluator Agent once with the same constraints and note the retry in `metadata.json`.
- If judge output omits score or misses required sections, rerun Judge Agent once and ask it to follow the judge prompt exactly.
- If a case cannot be read, skip it only after writing a short failure note in that case artifact directory.
- If benchmark matching is ambiguous, stop and ask the user which etalon belongs to the original.
