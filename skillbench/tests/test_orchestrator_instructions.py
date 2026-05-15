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
        self.assertIn("Judge Agent receives evaluator output, etalon, and judge prompt", text)

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
