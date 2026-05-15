from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

from skillbench import __version__
from skillbench.cases import BenchmarkCase, discover_cases
from skillbench.llm import OpenAICompatibleLLMClient
from skillbench.pipeline import load_prompts, run_case


DEFAULT_BENCHMARK_DIR = Path("benchmark")
DEFAULT_RUNS_DIR = Path("skillbench") / "runs"
DEFAULT_ANALYSIS_PROMPT = "Промпт для оценки документов сравниваемыми моделями.txt"
DEFAULT_JUDGE_PROMPT = "LLM-as-a-judge для оценки v2.txt"


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "list-cases":
            return _list_cases(args)
        if args.command == "run":
            return _run(args)
        if args.command == "show-run":
            return _show_run(args)
    except Exception as exc:
        print(f"skillbench: error: {exc}", file=sys.stderr)
        return 1

    parser.print_help()
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="skillbench",
        description="Run benchmark-driven LLM skill evaluation and prompt improvement.",
    )
    parser.add_argument("--version", action="version", version=f"skillbench {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    list_cases = subparsers.add_parser("list-cases", help="List discovered benchmark cases")
    list_cases.add_argument("--benchmark-dir", type=Path, default=DEFAULT_BENCHMARK_DIR)

    run = subparsers.add_parser("run", help="Run one or more benchmark cases")
    run.add_argument("--benchmark-dir", type=Path, default=DEFAULT_BENCHMARK_DIR)
    run.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    run.add_argument("--case", help="Case name from list-cases. Omit to run all cases.")
    run.add_argument("--run-id", help="Optional stable run id for reproducible output paths.")
    run.add_argument("--analysis-prompt", type=Path)
    run.add_argument("--judge-prompt", type=Path)
    run.add_argument("--improver-prompt", type=Path)
    run.add_argument(
        "--evaluated-model",
        default=os.environ.get("SKILLBENCH_EVALUATED_MODEL", "gpt-5.2"),
    )
    run.add_argument(
        "--judge-model",
        default=os.environ.get("SKILLBENCH_JUDGE_MODEL", "gpt-5.2"),
    )
    run.add_argument(
        "--improver-model",
        default=os.environ.get("SKILLBENCH_IMPROVER_MODEL", "gpt-5.2"),
    )

    show_run = subparsers.add_parser("show-run", help="Print a saved run artifact")
    show_run.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    show_run.add_argument("--run-id", required=True)
    show_run.add_argument("--case", required=True)
    show_run.add_argument(
        "--artifact",
        default="improvement_report.md",
        choices=[
            "candidate_layer_1.md",
            "candidate_layer_2.md",
            "judge_result.md",
            "improvement_report.md",
            "proposed_analysis_prompt.md",
            "proposed_judge_prompt.md",
            "metadata.json",
        ],
    )
    return parser


def _list_cases(args: argparse.Namespace) -> int:
    for case in discover_cases(args.benchmark_dir):
        print(f"{case.name}\t{case.original_path}\t{case.etalon_path}")
    return 0


def _run(args: argparse.Namespace) -> int:
    benchmark_dir = args.benchmark_dir
    analysis_prompt = args.analysis_prompt or benchmark_dir / DEFAULT_ANALYSIS_PROMPT
    judge_prompt = args.judge_prompt or benchmark_dir / DEFAULT_JUDGE_PROMPT
    prompts = load_prompts(analysis_prompt, judge_prompt, args.improver_prompt)
    cases = _select_cases(discover_cases(benchmark_dir), args.case)
    llm = OpenAICompatibleLLMClient()

    for case in cases:
        result = run_case(
            case,
            prompts,
            llm,
            args.runs_dir,
            run_id=args.run_id,
            evaluated_model=args.evaluated_model,
            judge_model=args.judge_model,
            improver_model=args.improver_model,
        )
        print(f"{result.case_name}\t{result.case_dir}")
    return 0


def _show_run(args: argparse.Namespace) -> int:
    artifact_path = args.runs_dir / args.run_id / args.case / args.artifact
    print(artifact_path.read_text(encoding="utf-8"))
    return 0


def _select_cases(cases: list[BenchmarkCase], requested_name: str | None) -> list[BenchmarkCase]:
    if requested_name is None:
        return cases
    for case in cases:
        if case.name == requested_name:
            return [case]
    available = ", ".join(case.name for case in cases) or "none"
    raise ValueError(f"Unknown case '{requested_name}'. Available cases: {available}")
