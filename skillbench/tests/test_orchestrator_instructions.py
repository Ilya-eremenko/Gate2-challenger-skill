import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = REPO_ROOT / "skills" / "skillbench-orchestrator" / "SKILL.md"
README_PATH = REPO_ROOT / "skillbench" / "README.md"


class SkillbenchOrchestratorInstructionTests(unittest.TestCase):
    def test_skill_file_has_required_orchestration_sections(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "name: skillbench-orchestrator",
            "Evaluator Agent",
            "Judge Agent",
            "Improvement Planner",
            "Prompt/Skill Editor Agent",
            "Data flow",
            "Approval gate",
            "Anti-overfit rules",
            "Artifacts",
            "evaluator_result.md",
            "evaluator_layers.md",
            "judge_result.md",
            "improvement_plan.md",
            "approved_changes.md",
            "post_change_summary.md",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_skill_keeps_etalon_out_of_evaluator_context(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("Evaluator Agent must not receive the etalon", text)
        self.assertIn("Judge Agent receives only normalized Layer 1 and normalized Layer 2", text)

    def test_judge_uses_only_extended_layers_not_summary(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "only normalized Layer 1 and normalized Layer 2 from this extended output are admissible evaluator material",
            "plain executive summary, structured final synthesis, and merged block assessment must not be sent to the Judge Agent",
            "Extract only normalized Layer 1 and normalized Layer 2 from the extended evaluator output",
            "do not use executive summary or final synthesis as scoring evidence",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_orchestrator_collects_layer_3_as_diagnostic_artifact(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "including its Layer 1 worker, Layer 2 worker, Layer 3 worker, and synthesizer",
            "Return the full extended output: final synthesis, normalized Layer 1, normalized Layer 2, normalized Layer 3, and merged block assessment",
            "Save normalized Layer 3 to `evaluator_layer_3.md`",
            "`evaluator_layer_3.md`: normalized Layer 3 extracted from `evaluator_result.md`; diagnostic benchmark material, not scoring material",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_3_drives_qualitative_improvements_not_score_credit(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "normalized Layer 3 is not admissible evaluator material for Judge Agent scoring until the benchmark etalon contains Layer 3",
            "Judge Agent must not receive normalized Layer 3 for current L1/L2-only etalons",
            "Layer 3 can generate qualitative improvement proposals, not score improvements",
            "If an etalon issue is missed by Layer 1 / Layer 2 but found in Layer 3, record it as a qualitative improvement opportunity rather than giving Judge credit",
            "Do not change the score or Judge input because Layer 3 found an etalon issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_readme_documents_codex_local_and_api_modes(self):
        text = README_PATH.read_text(encoding="utf-8")

        self.assertIn("codex-local", text)
        self.assertIn("api", text)
        self.assertIn("Python CLI does not directly spawn Codex subagents", text)

    def test_instructions_do_not_claim_cli_can_spawn_codex_agents(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + README_PATH.read_text(encoding="utf-8")
        ).lower()

        forbidden_phrases = [
            "python cli directly spawn codex",
            "cli directly spawn codex",
            "python3 -m skillbench run --mode codex-local",
        ]
        for phrase in forbidden_phrases:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
