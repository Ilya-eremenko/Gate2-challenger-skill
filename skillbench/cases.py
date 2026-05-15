from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


SUPPORTED_ORIGINAL_SUFFIXES = {".md", ".txt", ".docx", ".dotx"}
SUPPORTED_ETALON_SUFFIXES = {".md", ".txt", ".csv"}
STOP_TOKENS = {"bench", "benchmark", "normalized", "etalon", "эталон"}


@dataclass(frozen=True)
class BenchmarkCase:
    name: str
    original_path: Path
    etalon_path: Path


def discover_cases(benchmark_dir: Path) -> list[BenchmarkCase]:
    benchmark_dir = Path(benchmark_dir)
    original_dir = benchmark_dir / "original"
    if not original_dir.exists():
        raise FileNotFoundError(f"Original documents directory does not exist: {original_dir}")

    etalon_files = _collect_etalon_files(benchmark_dir)
    original_files = sorted(
        path
        for path in original_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_ORIGINAL_SUFFIXES
    )

    cases: list[BenchmarkCase] = []
    for original_path in original_files:
        original_tokens = _tokens(original_path.stem)
        etalon_path = _best_etalon_match(original_tokens, etalon_files)
        if etalon_path is None:
            continue
        cases.append(
            BenchmarkCase(
                name=_case_name(original_path.stem),
                original_path=original_path,
                etalon_path=etalon_path,
            )
        )

    return sorted(cases, key=lambda case: case.name)


def _collect_etalon_files(benchmark_dir: Path) -> list[Path]:
    candidates: list[Path] = []
    for etalon_dir in (benchmark_dir / "Эталоны" / "normalized", benchmark_dir / "Эталоны"):
        if not etalon_dir.exists():
            continue
        candidates.extend(
            path
            for path in etalon_dir.iterdir()
            if path.is_file() and path.suffix.lower() in SUPPORTED_ETALON_SUFFIXES
        )
        if candidates:
            return sorted(candidates)
    return []


def _best_etalon_match(original_tokens: set[str], etalon_files: list[Path]) -> Path | None:
    best_path: Path | None = None
    best_score = 0.0
    for etalon_path in etalon_files:
        etalon_tokens = _tokens(etalon_path.stem)
        overlap = original_tokens & etalon_tokens
        if not overlap:
            continue
        score = len(overlap) / len(original_tokens | etalon_tokens)
        if score > best_score:
            best_score = score
            best_path = etalon_path
    return best_path


def _case_name(value: str) -> str:
    return "-".join(_ordered_tokens(value))


def _tokens(value: str) -> set[str]:
    return set(_ordered_tokens(value))


def _ordered_tokens(value: str) -> list[str]:
    raw_tokens = re.findall(r"[A-Za-zА-Яа-я0-9]+", value.lower())
    return [token for token in raw_tokens if token not in STOP_TOKENS]
