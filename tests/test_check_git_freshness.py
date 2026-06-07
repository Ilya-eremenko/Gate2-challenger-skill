import importlib.util
import io
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    REPO_ROOT
    / "skills"
    / "gate-challenger"
    / "scripts"
    / "check_git_freshness.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("check_git_freshness", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(cwd, *args):
    return subprocess.run(
        ["git", "-C", str(cwd), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def configure_identity(repo):
    git(repo, "config", "user.email", "tests@example.com")
    git(repo, "config", "user.name", "Gate Challenger Tests")


def commit_skill_change(repo, text):
    skill_path = repo / "skills" / "gate-challenger" / "SKILL.md"
    skill_path.parent.mkdir(parents=True, exist_ok=True)
    skill_path.write_text(text, encoding="utf-8")
    git(repo, "add", "skills/gate-challenger/SKILL.md")
    git(repo, "commit", "-m", "Update skill")


def create_repo_with_remote(root):
    remote = root / "origin.git"
    subprocess.run(
        ["git", "init", "--bare", str(remote)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    repo = root / "repo"
    subprocess.run(
        ["git", "clone", str(remote), str(repo)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    configure_identity(repo)
    git(repo, "switch", "-c", "main")
    commit_skill_change(repo, "initial\n")
    git(repo, "push", "-u", "origin", "main")
    return repo, remote


def run_main(module, args):
    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        exit_code = module.main(args)
    return exit_code, stdout.getvalue(), stderr.getvalue()


class CheckGitFreshnessTests(unittest.TestCase):
    def test_clean_checkout_at_upstream_passes(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo, _remote = create_repo_with_remote(Path(tmp_dir))

            exit_code, stdout, stderr = run_main(
                module, ["--repo", str(repo), "--no-fetch"]
            )

        self.assertEqual(0, exit_code, stderr)
        self.assertIn("git freshness OK", stdout)

    def test_checkout_behind_upstream_fails(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            repo, remote = create_repo_with_remote(root)
            updater = root / "updater"
            subprocess.run(
                ["git", "clone", str(remote), str(updater)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            configure_identity(updater)
            git(updater, "switch", "main")
            commit_skill_change(updater, "remote update\n")
            git(updater, "push")

            exit_code, _stdout, stderr = run_main(module, ["--repo", str(repo)])

        self.assertNotEqual(0, exit_code)
        self.assertIn("behind", stderr)
        self.assertIn("git -C", stderr)
        self.assertIn("pull --ff-only", stderr)

    def test_dirty_skill_files_fail(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            repo, _remote = create_repo_with_remote(Path(tmp_dir))
            skill_path = repo / "skills" / "gate-challenger" / "SKILL.md"
            skill_path.write_text("local edit\n", encoding="utf-8")

            exit_code, _stdout, stderr = run_main(
                module, ["--repo", str(repo), "--no-fetch"]
            )

        self.assertNotEqual(0, exit_code)
        self.assertIn("local modifications", stderr)
        self.assertIn("skills/gate-challenger", stderr)


if __name__ == "__main__":
    unittest.main()
