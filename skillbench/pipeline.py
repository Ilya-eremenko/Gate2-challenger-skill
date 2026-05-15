from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re

from skillbench.cases import BenchmarkCase
from skillbench.documents import read_document
from skillbench.llm import LLMClient


DEFAULT_IMPROVER_PROMPT = """You improve a benchmark-driven LLM skill system.

Your goal is not to game one judge result. Improve the analysis prompt and the judge prompt so the evaluated model finds real decision-critical issues more reliably, and the judge scores candidate answers more consistently against the etalon.

Return:
1. A concise improvement report.
2. Generalizable analysis prompt changes.
3. Generalizable judge prompt changes.
4. Overfitting risks and rejected case-specific changes.
5. The next full analysis prompt inside <analysis_prompt>...</analysis_prompt>.
6. The next full judge prompt inside <judge_prompt>...</judge_prompt>.
"""


@dataclass(frozen=True)
class Prompts:
    analysis_layer_1: str
    analysis_layer_2: str
    judge: str
    improver: str = DEFAULT_IMPROVER_PROMPT


@dataclass(frozen=True)
class RunResult:
    run_id: str
    case_name: str
    case_dir: Path


def load_prompts(
    analysis_prompt_path: Path,
    judge_prompt_path: Path,
    improver_prompt_path: Path | None = None,
) -> Prompts:
    analysis_prompt = Path(analysis_prompt_path).read_text(encoding="utf-8")
    judge_prompt = Path(judge_prompt_path).read_text(encoding="utf-8")
    improver_prompt = (
        Path(improver_prompt_path).read_text(encoding="utf-8")
        if improver_prompt_path is not None
        else DEFAULT_IMPROVER_PROMPT
    )
    layer_1, layer_2 = _split_analysis_prompt(analysis_prompt)
    return Prompts(layer_1, layer_2, judge_prompt, improver_prompt)


def run_case(
    case: BenchmarkCase,
    prompts: Prompts,
    llm: LLMClient,
    runs_dir: Path,
    *,
    run_id: str | None = None,
    evaluated_model: str,
    judge_model: str,
    improver_model: str,
) -> RunResult:
    run_id = run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    case_dir = Path(runs_dir) / run_id / case.name
    case_dir.mkdir(parents=True, exist_ok=True)

    original_text = read_document(case.original_path)
    etalon_text = read_document(case.etalon_path)

    candidate_l1 = llm.complete(
        task="evaluated_layer_1",
        system=prompts.analysis_layer_1,
        user=_analysis_user_prompt(case, original_text, "Layer 1"),
        model=evaluated_model,
    )
    candidate_l2 = llm.complete(
        task="evaluated_layer_2",
        system=prompts.analysis_layer_2,
        user=_analysis_user_prompt(case, original_text, "Layer 2"),
        model=evaluated_model,
    )
    judge_result = llm.complete(
        task="judge",
        system=prompts.judge,
        user=_judge_user_prompt(candidate_l1, candidate_l2, etalon_text),
        model=judge_model,
    )
    improvement_report = llm.complete(
        task="improver",
        system=prompts.improver,
        user=_improver_user_prompt(
            prompts=prompts,
            original_text=original_text,
            etalon_text=etalon_text,
            candidate_l1=candidate_l1,
            candidate_l2=candidate_l2,
            judge_result=judge_result,
        ),
        model=improver_model,
    )

    proposed_analysis_prompt = _extract_tag(improvement_report, "analysis_prompt") or (
        prompts.analysis_layer_1 + "\n\n" + prompts.analysis_layer_2
    )
    proposed_judge_prompt = _extract_tag(improvement_report, "judge_prompt") or prompts.judge

    artifacts = {
        "candidate_layer_1.md": candidate_l1,
        "candidate_layer_2.md": candidate_l2,
        "judge_result.md": judge_result,
        "improvement_report.md": improvement_report,
        "proposed_analysis_prompt.md": proposed_analysis_prompt,
        "proposed_judge_prompt.md": proposed_judge_prompt,
    }
    for filename, content in artifacts.items():
        (case_dir / filename).write_text(content, encoding="utf-8")

    metadata = {
        "run_id": run_id,
        "case": case.name,
        "original_path": str(case.original_path),
        "etalon_path": str(case.etalon_path),
        "models": {
            "evaluated": evaluated_model,
            "judge": judge_model,
            "improver": improver_model,
        },
        "artifacts": sorted(artifacts),
    }
    (case_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    return RunResult(run_id=run_id, case_name=case.name, case_dir=case_dir)


def _split_analysis_prompt(prompt: str) -> tuple[str, str]:
    marker = re.search(r"(?im)^#\s*Промпт\s*2\b", prompt)
    if marker is None:
        return (
            prompt + "\n\nReturn only Layer 1.",
            prompt + "\n\nReturn only Layer 2.",
        )
    return prompt[: marker.start()].strip(), prompt[marker.start() :].strip()


def _analysis_user_prompt(case: BenchmarkCase, original_text: str, layer: str) -> str:
    return f"""Input Doc: {case.original_path}
Requested output: {layer}

Initiative defense document:
{original_text}
"""


def _judge_user_prompt(candidate_l1: str, candidate_l2: str, etalon_text: str) -> str:
    return f"""Candidate Layer 1:
{candidate_l1}

Candidate Layer 2:
{candidate_l2}

Etalon:
{etalon_text}
"""


def _improver_user_prompt(
    *,
    prompts: Prompts,
    original_text: str,
    etalon_text: str,
    candidate_l1: str,
    candidate_l2: str,
    judge_result: str,
) -> str:
    return f"""Analysis prompt for Layer 1:
{prompts.analysis_layer_1}

Analysis prompt for Layer 2:
{prompts.analysis_layer_2}

Judge prompt:
{prompts.judge}

Original document:
{original_text}

Etalon answer:
{etalon_text}

Candidate Layer 1:
{candidate_l1}

Candidate Layer 2:
{candidate_l2}

Judge result:
{judge_result}

Improve both the evaluated analysis prompt and the judge prompt. Prefer general benchmark-quality improvements over case-specific score gaming.
"""


def _extract_tag(text: str, tag: str) -> str | None:
    match = re.search(rf"<{tag}>\s*(.*?)\s*</{tag}>", text, flags=re.DOTALL)
    if match is None:
        return None
    return match.group(1).strip()
