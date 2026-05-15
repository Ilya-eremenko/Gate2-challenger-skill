import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from skillbench.cli import main


class CliTests(unittest.TestCase):
    def test_list_cases_prints_discovered_cases(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            benchmark_dir = Path(tmp_dir) / "benchmark"
            original_dir = benchmark_dir / "original"
            etalon_dir = benchmark_dir / "Эталоны"
            original_dir.mkdir(parents=True)
            etalon_dir.mkdir(parents=True)

            (original_dir / "PWS.md").write_text("source", encoding="utf-8")
            (etalon_dir / "PWS bench.md").write_text("etalon", encoding="utf-8")

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = main(["list-cases", "--benchmark-dir", str(benchmark_dir)])

        self.assertEqual(0, exit_code)
        self.assertIn("pws", stdout.getvalue())

    def test_show_run_prints_existing_run_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            run_dir = tmp_path / "runs" / "run-1" / "pws"
            run_dir.mkdir(parents=True)
            (run_dir / "judge_result.md").write_text("score: 90", encoding="utf-8")

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exit_code = main(
                    [
                        "show-run",
                        "--runs-dir",
                        str(tmp_path / "runs"),
                        "--run-id",
                        "run-1",
                        "--case",
                        "pws",
                        "--artifact",
                        "judge_result.md",
                    ]
                )

        self.assertEqual(0, exit_code)
        self.assertIn("score: 90", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
