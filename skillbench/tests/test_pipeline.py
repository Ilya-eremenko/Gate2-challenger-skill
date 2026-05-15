import json
import tempfile
import unittest
from pathlib import Path

from skillbench.cases import BenchmarkCase
from skillbench.llm import FakeLLMClient
from skillbench.pipeline import Prompts, run_case


class PipelineTests(unittest.TestCase):
    def test_run_case_saves_candidate_judge_improvement_and_prompt_versions(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            original = tmp_path / "TRX_SE.md"
            etalon = tmp_path / "SE TRX bench.md"
            original.write_text("Original Gate 2 document", encoding="utf-8")
            etalon.write_text("Ideal Layer 1 and Layer 2 answer", encoding="utf-8")

            llm = FakeLLMClient(
                {
                    "evaluated_layer_1": "candidate L1",
                    "evaluated_layer_2": "candidate L2",
                    "judge": "score: 48\nmissed: user journey",
                    "improver": (
                        "## Improvement Report\n"
                        "Improve both prompts without case-specific leakage.\n\n"
                        "<analysis_prompt>\nnew analysis prompt\n</analysis_prompt>\n\n"
                        "<judge_prompt>\nnew judge prompt\n</judge_prompt>\n"
                    ),
                }
            )

            result = run_case(
                BenchmarkCase("trx-se", original, etalon),
                Prompts(
                    analysis_layer_1="analysis L1 prompt",
                    analysis_layer_2="analysis L2 prompt",
                    judge="judge prompt",
                    improver="improver prompt",
                ),
                llm,
                tmp_path / "runs",
                run_id="fixed-run",
                evaluated_model="eval-model",
                judge_model="judge-model",
                improver_model="improver-model",
            )

            case_dir = tmp_path / "runs" / "fixed-run" / "trx-se"
            metadata = json.loads((case_dir / "metadata.json").read_text(encoding="utf-8"))
            files = {
                path.name: path.read_text(encoding="utf-8")
                for path in case_dir.iterdir()
                if path.suffix in {".md", ".json"}
            }

        self.assertEqual(case_dir, result.case_dir)
        self.assertEqual("candidate L1", files["candidate_layer_1.md"])
        self.assertEqual("candidate L2", files["candidate_layer_2.md"])
        self.assertIn("score: 48", files["judge_result.md"])
        self.assertIn("Improve both prompts", files["improvement_report.md"])
        self.assertEqual("new analysis prompt", files["proposed_analysis_prompt.md"])
        self.assertEqual("new judge prompt", files["proposed_judge_prompt.md"])
        self.assertEqual("trx-se", metadata["case"])
        self.assertEqual(
            {
                "evaluated": "eval-model",
                "judge": "judge-model",
                "improver": "improver-model",
            },
            metadata["models"],
        )
        self.assertEqual(
            ["evaluated_layer_1", "evaluated_layer_2", "judge", "improver"],
            [call.task for call in llm.calls],
        )
        self.assertIn("candidate L1", llm.calls[2].user)
        self.assertIn("judge prompt", llm.calls[3].user)


if __name__ == "__main__":
    unittest.main()
