#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path


DEFAULT_SKILL_PATH = Path("skills") / "gate-challenger"


class GitFreshnessError(Exception):
    def __init__(self, message: str, exit_code: int = 1):
        super().__init__(message)
        self.exit_code = exit_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify that the gate-challenger skill checkout is current."
    )
    parser.add_argument(
        "--repo",
        help=(
            "Path to the Gate-challenger git checkout. Defaults to "
            "$GATE_CHALLENGER_REPO, then $GATE2_CHALLENGER_REPO, then the checkout containing this script."
        ),
    )
    parser.add_argument(
        "--path",
        help=(
            "Path whose local modifications should be rejected. Defaults to "
            "skills/gate-challenger when it exists, otherwise the whole repo."
        ),
    )
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="Skip git fetch before comparing HEAD with the upstream branch.",
    )
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow local modifications in the checked path.",
    )
    return parser


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise GitFreshnessError(
            f"git {' '.join(args)} failed in {repo}: {detail}", exit_code=2
        )
    return result.stdout.strip()


def script_skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def candidate_repo(args_repo: str | None) -> Path:
    if args_repo:
        return Path(args_repo).expanduser().resolve()

    env_repo = os.environ.get("GATE_CHALLENGER_REPO") or os.environ.get("GATE2_CHALLENGER_REPO")
    if env_repo:
        return Path(env_repo).expanduser().resolve()

    return script_skill_dir()


def resolve_repo_root(candidate: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(candidate), "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        raise GitFreshnessError(
            "Cannot verify git freshness because the skill is not inside a git "
            f"checkout: {candidate}\n"
            "Run this script with --repo /path/to/Gate2-challenger or set "
            "GATE_CHALLENGER_REPO.",
            exit_code=2,
        )
    return Path(result.stdout.strip()).resolve()


def default_check_path(repo: Path) -> str:
    if (repo / DEFAULT_SKILL_PATH).exists():
        return str(DEFAULT_SKILL_PATH)
    return "."


def require_clean_path(repo: Path, pathspec: str) -> None:
    status = run_git(
        repo,
        "status",
        "--porcelain",
        "--untracked-files=all",
        "--",
        pathspec,
    )
    if status:
        raise GitFreshnessError(
            f"Local checkout has local modifications under {pathspec}:\n"
            f"{status}\n"
            "Use a clean checkout before review, or pass --allow-dirty only for "
            "intentional local testing."
        )


def upstream_ref(repo: Path) -> str:
    try:
        return run_git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    except GitFreshnessError as exc:
        raise GitFreshnessError(
            "Cannot verify git freshness because the current branch has no "
            "upstream. Set an upstream branch, then rerun the check.",
            exit_code=2,
        ) from exc


def fetch_upstream(repo: Path, upstream: str) -> None:
    branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    if branch == "HEAD":
        raise GitFreshnessError(
            "Cannot verify git freshness from a detached HEAD checkout.",
            exit_code=2,
        )

    remote = run_git(repo, "config", "--get", f"branch.{branch}.remote")
    if remote == ".":
        return

    try:
        run_git(repo, "fetch", "--quiet", remote)
    except GitFreshnessError as exc:
        raise GitFreshnessError(
            f"Failed to fetch {remote} before checking {upstream}: {exc}",
            exit_code=2,
        ) from exc


def rev_count(repo: Path, range_spec: str) -> int:
    return int(run_git(repo, "rev-list", "--count", range_spec))


def require_up_to_date(repo: Path, upstream: str) -> str:
    local = run_git(repo, "rev-parse", "HEAD")
    remote = run_git(repo, "rev-parse", upstream)
    base = run_git(repo, "merge-base", "HEAD", upstream)

    if local == remote:
        return local[:12]

    ahead = rev_count(repo, f"{upstream}..HEAD")
    behind = rev_count(repo, f"HEAD..{upstream}")

    if local == base:
        raise GitFreshnessError(
            f"Local checkout is behind {upstream} by {behind} commit(s).\n"
            f"Run: git -C {repo} pull --ff-only"
        )
    if remote == base:
        raise GitFreshnessError(
            f"Local checkout is ahead of {upstream} by {ahead} commit(s). "
            "Use the canonical upstream version before review."
        )

    raise GitFreshnessError(
        f"Local checkout has diverged from {upstream} "
        f"({ahead} ahead, {behind} behind). Resolve it before review."
    )


def check_freshness(
    repo_candidate: Path,
    pathspec: str | None = None,
    fetch: bool = True,
    allow_dirty: bool = False,
) -> tuple[Path, str, str, str]:
    repo = resolve_repo_root(repo_candidate)
    checked_path = pathspec or default_check_path(repo)

    if not allow_dirty:
        require_clean_path(repo, checked_path)

    upstream = upstream_ref(repo)
    if fetch:
        fetch_upstream(repo, upstream)

    short_sha = require_up_to_date(repo, upstream)
    return repo, checked_path, upstream, short_sha


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        repo, checked_path, upstream, short_sha = check_freshness(
            candidate_repo(args.repo),
            pathspec=args.path,
            fetch=not args.no_fetch,
            allow_dirty=args.allow_dirty,
        )
    except GitFreshnessError as exc:
        print(str(exc), file=sys.stderr)
        return exc.exit_code

    print(
        "git freshness OK: "
        f"{repo} at {short_sha} matches {upstream}; checked {checked_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
