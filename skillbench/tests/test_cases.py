import tempfile
import unittest
from pathlib import Path

from skillbench.cases import discover_cases


class DiscoverCasesTests(unittest.TestCase):
    def test_matches_originals_to_etalon_by_tokens(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            benchmark_dir = Path(tmp_dir) / "benchmark"
            original_dir = benchmark_dir / "original"
            etalon_dir = benchmark_dir / "Эталоны" / "normalized"
            original_dir.mkdir(parents=True)
            etalon_dir.mkdir(parents=True)

            (original_dir / "TRX_SE.md").write_text("source", encoding="utf-8")
            (original_dir / "PWS.md").write_text("source", encoding="utf-8")
            (etalon_dir / "SE TRX bench.md").write_text("etalon", encoding="utf-8")
            (etalon_dir / "PWS bench.md").write_text("etalon", encoding="utf-8")

            cases = discover_cases(benchmark_dir)

        self.assertEqual(["pws", "trx-se"], [case.name for case in cases])
        self.assertEqual("PWS.md", cases[0].original_path.name)
        self.assertEqual("PWS bench.md", cases[0].etalon_path.name)
        self.assertEqual("TRX_SE.md", cases[1].original_path.name)
        self.assertEqual("SE TRX bench.md", cases[1].etalon_path.name)

    def test_uses_non_normalized_etalon_dir_when_needed(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            benchmark_dir = Path(tmp_dir) / "benchmark"
            original_dir = benchmark_dir / "original"
            etalon_dir = benchmark_dir / "Эталоны"
            original_dir.mkdir(parents=True)
            etalon_dir.mkdir(parents=True)

            (original_dir / "Genai.md").write_text("source", encoding="utf-8")
            (etalon_dir / "Genai bench.md").write_text("etalon", encoding="utf-8")

            cases = discover_cases(benchmark_dir)

        self.assertEqual(1, len(cases))
        self.assertEqual("genai", cases[0].name)
        self.assertEqual("Genai bench.md", cases[0].etalon_path.name)


if __name__ == "__main__":
    unittest.main()
