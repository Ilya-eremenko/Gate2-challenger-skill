import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "skills" / "gate-challenger"
SKILL_PATH = SKILL_DIR / "SKILL.md"
LAYER_1_RUBRIC_PATH = SKILL_DIR / "references" / "gate-2-rubric.md"
LAYER_2_RUBRIC_PATH = SKILL_DIR / "references" / "gate-2-rubric.md"
LAYER_3_RUBRIC_PATH = SKILL_DIR / "references" / "common-adversarial-rubric.md"
OUTPUT_CONTRACT_PATH = SKILL_DIR / "references" / "common-output-contract.md"
VERDICT_POLICY_PATH = SKILL_DIR / "references" / "common-verdict-policy.md"
SYNTHESIS_CONTRACT_PATH = SKILL_DIR / "references" / "common-synthesis-contract.md"
GATE_3_RUBRIC_PATH = SKILL_DIR / "references" / "gate-3-rubric.md"
STREAM_REVIEW_1_RUBRIC_PATH = SKILL_DIR / "references" / "stream-review-1-rubric.md"
STREAM_REVIEW_2_PLUS_RUBRIC_PATH = (
    SKILL_DIR / "references" / "stream-review-2-plus-rubric.md"
)
STAGE_DETECTION_PATH = SKILL_DIR / "references" / "stage-detection.md"


class Gate2ChallengerInstructionTests(unittest.TestCase):
    def test_skill_is_renamed_to_gate_challenger_and_routes_by_stage(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "name: gate-challenger",
            "document_stage: GATE_2 | STREAM_REVIEW_1 | STREAM_REVIEW_2_PLUS | GATE_3 | UNKNOWN | FRAGMENT",
            "Read [stage-detection.md](references/stage-detection.md)",
            "Gate 2 -> [gate-2-rubric.md](references/gate-2-rubric.md)",
            "1st Stream Review -> [stream-review-1-rubric.md](references/stream-review-1-rubric.md)",
            "2+ Stream Review -> [stream-review-2-plus-rubric.md](references/stream-review-2-plus-rubric.md)",
            "Gate 3 -> [gate-3-rubric.md](references/gate-3-rubric.md)",
            "Do not start Layer 1, Layer 2, or Layer 3 until the stage is detected",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_skill_loads_only_selected_stage_rubric_after_routing(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Context loading discipline",
            "Do not read, preload, summarize, or skim any stage-specific rubric before the routing record is complete",
            "After routing, read exactly one selected stage-specific rubric",
            "Do not open the other stage rubrics for examples, calibration, duplicate-family keys, or adversarial lenses",
            "Layer 3 uses the common adversarial rubric plus the same selected stage-specific rubric only",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_stage_detection_has_gate_2_sr1_gate_3_and_ambiguity_rules(self):
        text = STAGE_DETECTION_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "document_stage: GATE_2 | STREAM_REVIEW_1 | STREAM_REVIEW_2_PLUS | GATE_3 | UNKNOWN | FRAGMENT",
            "routing_decision: gate_2_rubric | stream_review_1_rubric | stream_review_2_plus_rubric | gate_3_rubric | ask_user | fragment_review",
            "FAQ asks for estimated date and success criteria for Gate 3",
            "title contains `Stream review 1` or `1st Stream Review`",
            "FAQ asks for the success criteria and estimated date for the next SR",
            "title contains `Stream review 2+`, `2nd Stream Review`, or `SR 2+`",
            "Green <=10%, Yellow:10%-20%, Red > 20%",
            "FAQ asks about progress on last commitments / MLP",
            "Green <= 10%, Yellow 10%-30%, Red > 30%",
            "If title and body disagree, prefer body evidence and report the conflict",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_stream_review_2_plus_rubric_contains_stage_specific_contract(self):
        text = STREAM_REVIEW_2_PLUS_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Use this rubric after the coordinator determines that the input is a 2+ Stream Review / 2nd Stream Review document.",
            "previous SR -> commitments -> plan / fact -> learning -> backlog -> roadmap -> metrics -> traction -> resources -> risks -> next SR",
            "Previous SR Commitment Ledger",
            "Plan-Fact And Traction Deviation Ledger",
            "Backlog And Roadmap Update Ledger",
            "Layer 1: 2+ Stream Review Decision-Critical Dimensions",
            "Layer 2: 2+ Stream Review Atomic Checks",
            "Do not require PMF, Gate 4, baseline transfer, or production-scale evidence unless the document claims that scope.",
            "plan-fact-reconciliation",
            "cadence-justification",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_stream_review_1_rubric_contains_stage_specific_contract(self):
        text = STREAM_REVIEW_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Use this rubric after the coordinator determines that the input is a 1st Stream Review / SR 1 initiative defense document.",
            "discovery -> validated product ideas -> solution -> progress -> roadmap -> metrics -> traction -> resources -> risks -> next SR",
            "Discovery Evidence Ledger",
            "Validated Product Ideas Ledger",
            "Progress, Roadmap, And Resource Map",
            "Layer 1: 1st Stream Review Decision-Critical Dimensions",
            "Layer 2: 1st Stream Review Atomic Checks",
            "Do not require production / MLP evidence unless the document claims production progress, rollout readiness, or scale.",
            "stream-discovery-evidence",
            "next-sr-conditions",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_gate_3_rubric_contains_stage_specific_contract(self):
        text = GATE_3_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "approved_scope",
            "not_approved_scope",
            "gate_4_conditions",
            "Customer Experience Ledger",
            "support scenario",
            "Traction YTD deviation using Gate 3 thresholds",
            "Approval Carry-Forward Risk",
            "baseline transfer",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_common_output_contract_is_stage_aware(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "document_stage",
            "stage_detection",
            "approval_scope",
            "not_approved_scope",
            "next_gate_conditions",
            "For 1st Stream Review",
            "`next_sr_conditions`",
            "For Gate 3",
            "`gate_4_conditions`",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_1_requires_dimension_specific_non_duplicate_issues(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "dimension-specific",
            "Do not restate the same blocker",
            "primary block",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_user_journey_is_required_when_adoption_or_conversion_is_central(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "MLP path",
            "end-state path",
            "adoption, conversion, mandatory usage",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_contains_added_gate_2_weak_link_checks(self):
        text = LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "quantified current-state problem",
            "softer alternatives",
            "approval boundary",
            "Metric definitions, toplines, horizons, and baselines",
            "Quotes, surveys, CSAT, and benchmarks",
            "downside scenarios",
            "Owners may be named",
            "secured, in progress, contingent, or outside team control",
            "problem definition drifts",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_internal_artifacts_feed_specific_output_checks(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "planning statements labeled as validation",
            "evidence-type proportionality",
            "owner, funded scope, implemented control, and contingent external dependency",
            "problem-definition drift and metric/topline reconciliation",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_1_keeps_detailed_subclaims_out_of_dimension_issues(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "detailed sub-claims belong in Layer 2",
            "do not split one underlying blocker",
            "same evidence pattern",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_segmentation_requires_size_pain_and_solution_mapping(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "segment size",
            "segment-specific pains",
            "segment-specific solution mapping",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_metric_checks_cover_changed_monetization_terms(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "take rate, price, commission, subsidy, or monetization terms",
            "changed value",
            "current value",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_preserves_specific_decision_test_not_umbrella_only(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "specific decision test",
            "umbrella diagnosis",
            "unmet success criterion",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_dedup_allows_repeat_only_for_distinct_decision_consequence(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "distinct decision consequence",
            "root cause",
            "do not repeat it as a new issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_missing_user_journey_can_affect_solution_and_scope_separately(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "adoption logic untestable",
            "scope/dependency readiness impossible to judge",
            "record both consequences",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_threshold_yes_requires_decision_critical_thresholds(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "thresholds exist for the decision-critical claims",
            "some thresholds exist",
            "answer `YES` only",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_bundles_l2_details_under_broad_decision_blockers(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "bundle related Layer 2-level observations under a broader Layer 1 decision blocker",
            "missed funnel thresholds",
            "optional-pilot-to-mandatory-rollout leap",
            "planning statements treated as validation",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_names_segment_pain_solution_linkage(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "segment -> pain -> solution linkage",
            "broad Layer 1 issue",
            "roadmap or feature list is not tied to distinct segments and pains",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_1_model_transparency_covers_core_drivers(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "model-transparency issue",
            "GMV, revenue, cannibalization, retention, subsidies, take rate, or conversion ramp",
            "validated drivers",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_2_uses_local_angle_to_avoid_duplicate_atoms(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "local angle only",
            "avoid restating the same insight as separate standalone failures",
            "same prerequisite gap, here specifically affecting test-vs-rollout gating",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_defaults_to_one_or_two_issues_per_dimension(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "Default to 1-2 Layer 1 issues per dimension",
            "Use 3 issues only when there are three independent decision blockers",
            "not evidence for each other",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_mlp_end_state_journey_uses_exact_missing_phrase(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "MLP/end-state journey is missing or not evaluable",
            "makes adoption behavior untestable",
            "makes test-vs-rollout readiness impossible to judge",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_scope_checks_resources_and_capacity(self):
        text = LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Are resources, ownership, delivery capacity, and horizontal dependencies secured for the work being approved now?",
            "headcount, support, billing, legal, T&S, anti-fraud, API, and partner-team dependencies",
            "assessed in Layer 2 even if they are already mentioned in Layer 1",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_2_risk_visibility_control_and_centrality_are_separate(self):
        text = LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "risk discovery/visibility",
            "control maturity",
            "centrality in the decision narrative",
            "answer `PARTIAL`, not `YES` with `No material issue`",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_2_duplicate_family_suppression_is_explicit(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "duplicate family",
            "central closure not tested",
            "end-state path/API gap",
            "projected ramp not explained by validated inputs",
            "10% evidence does not validate 15% monetization",
            "mitigations are plans, not controls",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_summary_mode_defaults_to_executive_summary(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Default `summary` output is a plain executive summary for a top-management reader",
            "Хотите расширенную версию с блокерами и доказательствами?",
            "Do not use schema keys such as `blockers`, `blocker_id`, `origin`, `severity`",
            "what can be approved, what cannot be approved yet",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_summary_mode_progressively_reveals_structured_and_full_outputs(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "ask whether the user wants the expanded structured final synthesis",
            "Хотите полный разбор по слоям?",
            "The structured final synthesis is the expanded summary format",
            "reuse the already computed synthesis and layer artifacts",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_summary_restores_decision_context_without_domain_specific_questions(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "restore the decision context before listing reasons",
            "what changed or what current fact makes the requested decision necessary",
            "the author's causal logic from problem to proposed answer",
            "which part is already proven and which part goes beyond proven evidence",
            "Do not hardcode domain-specific recovery, regulation, partner, or pricing questions",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_summary_evidence_bullets_are_proof_chains(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Every `Краткие доказательства` bullet must be a proof chain",
            "`source -> fact -> interpretation -> decision consequence`",
            "must not end with only a fact, number, quote, or section reference",
            "explain why this evidence proves the problem",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_summary_runs_reader_comprehension_pass(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Run a final reader-comprehension pass",
            "would understand what happened without opening the document",
            "every evidence bullet connects the fact to the decision risk",
            "rewrite the answer before returning if the proof chain is unclear",
            "do not add new issues during this pass",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_solution_l1_links_segment_pain_solution_when_feature_inventory_is_used(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "if Solution quality is `FAIL`",
            "segment -> pain -> solution linkage",
            "feature inventory",
            "business-control pain",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_solution_or_traction_l1_flags_missing_repeat_use_evidence(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "repeat use, retention, same-seller return behavior, or willingness-to-use-again",
            "missing, weak, or contradicted by analytics",
            "include a Layer 1 issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_traction_l1_prefers_one_reconstructability_issue_for_model_drivers(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "Prefer one broad Layer 1 traction issue",
            "model reconstructability",
            "treat a changed 10% -> 15% monetization or take-rate assumption as evidence",
            "unless it is the only material traction weakness",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_duplicate_family_references_same_family_before_local_angle(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "same duplicate family; local angle:",
            "do not create a fresh standalone issue",
            "use that prefix before the block-specific consequence",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_2_requires_materiality_before_partial_or_no(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "answer `PARTIAL` or `NO` only when the issue changes approval safety, validation strength, or the block verdict",
            "plausible nuance, generic completeness concern, or already-covered concern",
            "answer `YES` with `No material issue` or use `same duplicate family; local angle:`",
            "suppress non-central extras",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_success_metrics_must_prove_user_pain_resolution(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "whether success criteria prove the stated user pains or value propositions were solved",
            "funnel conversion, operational readiness, support load, or risk absence",
            "not direct evidence that user pains were solved",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_solution_flags_overloaded_pains_and_use_cases(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "materially different pains, use cases, or value propositions are combined into one solution story",
            "same product path solves each one",
            "user convenience, business monetization, transaction control, risk reduction, fraud or cancellation control, and strategic share growth",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_traction_checks_model_rows_against_formula_and_drivers(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "formula, yearly rows, scenario rows, or driver decomposition",
            "important rows reconcile with the formula and stated drivers",
            "cannot be traced to drivers, baselines, or assumptions",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_monetization_cannibalization_conflicts_are_consistency_issues(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "equal or stable commission/take-rate economics",
            "dismiss cannibalization risk",
            "later assumes a lower target commission, lower price, subsidy, or changed monetization term",
            "record a contradiction",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_rollout_aggressiveness_can_be_l1_traction_issue(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "adoption, GMV, revenue, or order ramp depends on rollout speed",
            "faster than unresolved dependencies allow",
            "record it as a Layer 1 Traction issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_threshold_specificity_cannot_use_future_gate_criteria_as_past_validation(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "do not infer a Gate 1 validation threshold from later Gate 3 criteria",
            "original expected result or threshold for that validation step",
            "cancellation, fraud, AML, regulator, or abuse break conditions use inconsistent thresholds",
            "name the specific threshold conflict",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_materiality_is_concise_but_not_silent(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "every atomic question must still be answered against its own decision test",
            "concrete evidence for a problem-bearing atomic check",
            "record the issue even when the same family is also covered elsewhere",
            "do not turn the issue into `YES` / `No material issue`",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_explicit_weak_link_checks_are_not_suppressed_as_generic(self):
        text = LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "explicit weak-link checks",
            "target clarity, segment mapping, current-state significance, prioritization, softer alternatives",
            "approval boundary, planning-vs-validation, metric reconciliation, changed monetization",
            "downside scenarios, external dependency classification, problem drift, or supporting-section caution",
            "must not suppress it as generic",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_1_solution_flags_proxy_validation_not_full_transaction_behavior(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "interest, entry-point click, survey intent, or other proxy behavior",
            "full paid, accepted, uncancelled transaction behavior",
            "include a Solution Layer 1 issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_1_keeps_l2_only_details_as_evidence_unless_dimension_verdict_changes(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "user-pain success-metric gaps, row-level model reconciliation, and granular threshold details",
            "stay in Layer 2 unless they independently change the dimension verdict",
            "cite them as evidence under a broader Layer 1 blocker",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_monetization_cannibalization_contradiction_can_repeat_with_local_consequence(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "monetization/cannibalization contradiction can appear in Traction and Consistency",
            "Traction: model economics are unsupported or internally inconsistent",
            "Consistency: risk defense contradicts target economics",
            "use local-angle wording to avoid duplicate penalties",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_standalone_issue_requires_not_stronger_nearby_duplicate(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "answer every atomic check internally, but emit a standalone Layer 2 issue only when",
            "not already represented by a stronger nearby issue",
            "local consequence is materially different",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_generic_weak_links_need_specific_decision_defect(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "generic weak-link checks default to `YES` / `No material issue` unless",
            "specific contradiction, threshold miss, formula gap, unresolved dependency, unsupported scaling leap, or inconsistent risk control",
            "do not emit generic standalone issues for broad target clarity, segment mapping, projected upside, softer alternatives, or downside sensitivity",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_promotes_pws_style_findings_when_they_change_dimension_verdict(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "promote to Layer 1 when they independently change the dimension verdict",
            "overloaded pains/use cases",
            "funnel/ops metrics do not measure solved user pain",
            "unexplained model-row or formula mismatch",
            "commission/cannibalization contradiction",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_pws_detail_anchors_preserve_specifics_for_partial_matches(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "preserve exact threshold mechanics",
            "specific row, year, driver, or formula detail",
            "fraud and lower-commission mechanics",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_output_budget_limits_distinct_issue_families_per_block(self):
        combined = (
            LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "Layer 2 output budget",
            "emit at most the two strongest distinct issue families per Atomic checks block",
            "additional atomic checks should reference the selected family in evidence rather than create another issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_2_pre_output_duplicate_family_keys_are_required(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "assign a duplicate-family key before writing Layer 2 output",
            "dependency-readiness",
            "proxy-validation",
            "monetization-contradiction",
            "cancellation-boundary",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_specificity_prompts_cover_segment_success_and_model_rows(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "different segment readiness, rollout path, or blocker profile",
            "success metrics mainly measure funnel or operational health",
            "specific year, row, or model component cannot be reconciled",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_verdict_policy_distinguishes_reject_from_need_evidence_when_logic_is_directional(self):
        text = VERDICT_POLICY_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "do not let high-recall diagnostic breadth alone force `REJECT`",
            "prefer `NEED_EVIDENCE` when the product logic is directionally coherent",
            "reserve `REJECT` for blockers that make the current gate unsafe even after feasible evidence collection",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_2_selected_family_output_is_structural_not_advisory(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "selected issue families are a pre-output control, not an optional writing style",
            "only the selected representative atomic answer gets full standalone issue text",
            "non-selected repeated atomic answers must use `same duplicate family; see <family>`",
            "do not add a second local-angle issue sentence for the same family",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_layer_1_remaining_pws_like_misses_are_named_generally(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "buyer readiness is confirmed without an original threshold",
            "too many distinct pains/use cases are combined into one solution narrative",
            "one traction model row cannot be transparently reconciled with the formula",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_synthesis_can_override_raw_reject_to_need_evidence_after_family_consolidation(self):
        synthesis_path = SYNTHESIS_CONTRACT_PATH
        combined = (
            VERDICT_POLICY_PATH.read_text(encoding="utf-8")
            + "\n"
            + synthesis_path.read_text(encoding="utf-8")
        )

        required_phrases = [
            "after duplicate-family consolidation",
            "override raw layer `REJECT` to final `NEED_EVIDENCE`",
            "failures are mostly evidence-remediable",
            "not structurally impossible or unsafe",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_selected_issues_are_self_contained_for_human_readers(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "each selected representative issue must be self-contained for a reader who has not opened the source document",
            "state what is wrong, why it matters for the gate decision, and what decision consequence follows",
            "avoid label-only issue text such as `proxy-validation:` without a plain-language explanation",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_evidence_explains_context_not_only_section_reference(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "evidence must include section or table name plus the exact values, thresholds, dates, user segments, or claims being compared",
            "do not cite a section name without explaining what in that section proves the issue",
            "when evidence is a contradiction, include both sides of the contradiction in the evidence field",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_issues_are_written_as_readable_mini_arguments(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "write each issue as a human-readable mini-argument",
            "prefer two compact sentences over one overloaded sentence",
            "evidence should connect the cited facts explicitly",
            "source A says the target or claim, source B shows the result or dependency",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_readability_does_not_expand_issue_set_or_verdict(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "Readable issue text must not change the evaluator's decisions",
            "use readability rules to explain already-selected issues, not to discover extra issues",
            "do not add a new Layer 1 issue, Layer 2 standalone issue, final blocker, severity upgrade, or verdict upgrade",
            "preserve duplicate-family and output-budget limits before applying the readability pass",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_explanatory_fields_default_to_plain_russian(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "Human-facing explanatory fields must be written in Russian by default",
            "`reason`, `suggestion`, `issue`, `evidence`, `merged_interpretation`, and `why_difference`",
            "Do not write mixed-language sentences such as `approval unsafe`, `proof gap`, `decision-ready`, or `blocker-grade` when a natural Russian phrase is available",
            "English is allowed only for schema keys, status values, canonical block names, metric names, section titles, product names, duplicate-family keys, and exact source quotes",
            "Use Russian explanations for duplicate-family labels: write the label only after a Russian sentence that explains the problem",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_common_analysis_anglicisms_have_russian_replacements(self):
        combined = (
            SKILL_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "`readiness` -> `готовность`",
            "`approval boundary` -> `граница текущего решения`",
            "`fakedoor` -> `фейкдор-тест` or `имитационный вход`",
            "`target solution` -> `целевая версия решения`",
            "`blockers` -> `блокирующие проблемы`",
            "`scaled rollout` -> `масштабный запуск`",
            "If an English term is a source quote or metric name, keep it in `evidence` but explain its meaning in Russian in the surrounding sentence",
            "Do not write full explanatory sentences in English inside human-facing fields",
            "Before returning the answer, scan `reason`, `issue`, `evidence`, `merged_interpretation`, and `why_difference` and rewrite any English explanatory sentence into Russian",
            "Questions may remain in English when they are canonical atomic checks, but their `issue` explanations must be Russian",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_strategic_fit_does_not_replace_softer_alternative_check(self):
        text = LAYER_2_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "declared strategic fit or stakeholder approval is not enough for `YES`",
            "mandatory adoption, closure, regulatory, churn, abuse, or resource risk",
            "justified versus lower-risk alternatives",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_readability_dedup_preserves_distinct_block_consequences(self):
        combined = (
            LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "readability and deduplication must not suppress distinct block consequences required by the rubric",
            "the same missing MLP/end-state journey can appear in Solution for adoption testability and in Scope for test-vs-rollout readiness",
            "same root cause may appear in different blocks when the decision consequence is different",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_specific_readability_preserves_key_numeric_mismatches(self):
        text = LAYER_1_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "preserve the direction and exact rates",
            "preserve both sides of the mismatch and the concrete threshold or allowance",
            "do not narrow a broad model-transparency issue to only conversion ramp or take rate",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_final_blockers_include_human_readable_proof_gap_and_consequence(self):
        combined = (
            OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "final blocker reason must name the broken claim, the proof gap, and the approval consequence",
            "blocker evidence must provide enough local context to understand criticality without opening the document",
            "include the specific threshold miss, unresolved dependency, model assumption, or contradictory claim that makes the blocker material",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_final_blocker_reason_and_evidence_are_mini_arguments(self):
        text = OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "write final blocker `reason` as a readable mini-argument",
            "first name the decision claim, then the missing or contradictory proof, then the gate consequence",
            "write blocker `evidence` as a short proof chain with source context",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_synthesis_compares_main_narrative_confidence_to_supporting_sections(self):
        synthesis_path = SYNTHESIS_CONTRACT_PATH
        combined = SKILL_PATH.read_text(encoding="utf-8") + "\n" + synthesis_path.read_text(encoding="utf-8")

        required_phrases = [
            "main narrative confidence",
            "supporting-section confidence",
            "confidence mismatch",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)

    def test_preflight_requires_git_freshness_before_review(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Version freshness preflight",
            "scripts/check_git_freshness.py",
            "git checkout is up to date with its upstream",
            "Do not start Layer 1 or Layer 2",
            "local fallback or intentional benchmark run",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_workflow_runs_layer_3_adversarial_worker(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Layer 3 worker: adversarial business and committee-risk review",
            "Read [common-adversarial-rubric.md](references/common-adversarial-rubric.md)",
            "Layer 3 must not read Layer 1 or Layer 2 output",
            "Only the Synthesizer reads all three artifacts",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_3_is_prompt_first_not_a_hard_checklist(self):
        text = LAYER_3_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "prompt-first adversarial reviewer",
            "not a hard checklist",
            "Use the lenses below as examples and pressure prompts",
            "do not force every lens to produce an issue",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_3_contains_adversarial_business_lenses(self):
        text = LAYER_3_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "Accounting / governance",
            "Attribution",
            "Incentives",
            "Operational failure modes",
            "Evidence laundering",
            "Scenario gaming",
            "Metric gaming / quality of growth",
            "Hidden downside / compound risks",
            "Organizational constraints",
            "Stakeholder misalignment",
            "Scope creep",
            "Ask vs proof mismatch",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_3_includes_devils_advocate_inspired_examples_without_wiki_dependency(self):
        text = LAYER_3_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "extra or sustained resources while baseline evidence is weak",
            "multi-product or multi-stream PMF asymmetry",
            "output commits without committed input drivers",
            "cumulative vs incremental masking",
            "revenue and gross-profit visibility",
            "platformization trap",
            "single fragile assumption",
            "These are examples, not required labels",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_layer_3_includes_committee_memory_and_segment_quality_examples(self):
        text = LAYER_3_RUBRIC_PATH.read_text(encoding="utf-8")

        required_phrases = [
            "prior IC commitment / baseline reset",
            "material tax/accounting caveat not modeled as scenario",
            "dominant partner or segment-quality substitution gap",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_synthesis_can_promote_novel_layer_3_issues_only_with_evidence(self):
        combined = (
            SYNTHESIS_CONTRACT_PATH.read_text(encoding="utf-8")
            + "\n"
            + VERDICT_POLICY_PATH.read_text(encoding="utf-8")
            + "\n"
            + OUTPUT_CONTRACT_PATH.read_text(encoding="utf-8")
        )

        required_phrases = [
            "layer_3",
            "novel_from_l3",
            "concrete document evidence",
            "changes what can be safely approved now",
            "do not promote generic adversarial concerns",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
