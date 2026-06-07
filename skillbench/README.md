# skillbench

`skillbench` supports two benchmark-driven improvement modes for LLM skills.

## Modes

### codex-local

`codex-local` is the primary mode for this repository. It is a Codex skill-driven workflow implemented by `skills/skillbench-orchestrator/SKILL.md`.

In this mode, the current Codex orchestrator runs benchmark cases sequentially with subagents:

```text
original document
  -> Evaluator Agent running gate-challenger in extended mode
  -> Judge Agent using etalon + judge prompt
  -> Improvement Planner in the orchestrator
  -> approved Prompt/Skill Editor Agent changes
  -> next case
```

Python CLI does not directly spawn Codex subagents. Use the `skillbench-orchestrator` skill when you want the local Codex loop.

### api

`api` is the fallback mode for batch runs and regression tests. It uses the OpenAI-compatible chat completions API from the Python CLI.

It runs this loop:

```text
analysis prompt + original document
  -> evaluated model
  -> candidate Layer 1 / Layer 2
  -> judge model + etalon + judge prompt
  -> score and error analysis
  -> improver model
  -> proposed analysis prompt and judge prompt updates
```

## API Usage

List benchmark cases:

```bash
python3 -m skillbench list-cases --benchmark-dir benchmark
```

Run one case:

```bash
OPENAI_API_KEY=... \
SKILLBENCH_EVALUATED_MODEL=gpt-5.2 \
SKILLBENCH_JUDGE_MODEL=gpt-5.2 \
SKILLBENCH_IMPROVER_MODEL=gpt-5.2 \
python3 -m skillbench run --benchmark-dir benchmark --case trx-se
```

Run artifacts are saved under `skillbench/runs/<run-id>/<case>/`:

- `candidate_layer_1.md`
- `candidate_layer_2.md`
- `judge_result.md`
- `improvement_report.md`
- `proposed_analysis_prompt.md`
- `proposed_judge_prompt.md`
- `metadata.json`

Inspect an artifact:

```bash
python3 -m skillbench show-run \
  --run-id 20260508T120000Z \
  --case trx-se \
  --artifact improvement_report.md
```

## Environment

The live client uses the OpenAI-compatible chat completions API:

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL` (optional, defaults to `https://api.openai.com/v1`)
- `SKILLBENCH_EVALUATED_MODEL`
- `SKILLBENCH_JUDGE_MODEL`
- `SKILLBENCH_IMPROVER_MODEL`
