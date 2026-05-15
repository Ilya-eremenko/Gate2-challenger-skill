# Layer 1 Rubric

Layer 1 is the broad, open-world review of the document as a decision narrative.

Layer 1 is dimension-level only. No atomic questions in the output.

For each block:

- assign `PASS`, `PARTIAL`, or `FAIL`
- identify whether the block is a blocker
- output up to 3 decision-relevant issues
- Default to 1-2 Layer 1 issues per dimension
- Use 3 issues only when there are three independent decision blockers that are not evidence for each other
- prefer dimension-level, chain-level, and consistency-level issues over checklist-style detail
- make every issue dimension-specific; Do not restate the same blocker across multiple blocks unless each restatement adds a distinct decision consequence
- when one weakness cuts across several blocks, choose the primary block for the main issue and use other blocks only for separate evidence, dependency, metric, or consistency consequences
- do not split one underlying blocker into several Layer 1 issues just because the same evidence pattern appears in several sections
- if the same root cause appears in another block without a distinct decision consequence, do not repeat it as a new issue
- bundle related Layer 2-level observations under a broader Layer 1 decision blocker when they support the same gate failure
- detailed sub-claims belong in Layer 2 unless they change the dimension-level decision safety of the block
- do not promote missed funnel thresholds, buyer/seller activation misses, the optional-pilot-to-mandatory-rollout leap, planning statements treated as validation, or take-rate / monetization assumption changes into separate Layer 1 issues when they are evidence for the same broader decision blocker
- user-pain success-metric gaps, row-level model reconciliation, and granular threshold details should stay in Layer 2 unless they independently change the dimension verdict; cite them as evidence under a broader Layer 1 blocker
- promote to Layer 1 when they independently change the dimension verdict: overloaded pains/use cases, funnel/ops metrics do not measure solved user pain, unexplained model-row or formula mismatch, or commission/cannibalization contradiction
- Prefer one broad Layer 1 traction issue for model reconstructability across GMV, revenue, cannibalization, retention, subsidies, baseline, take rate, and conversion ramp; treat a changed 10% -> 15% monetization or take-rate assumption as evidence under that issue unless it is the only material traction weakness
- preserve the specific decision test behind a broad blocker, such as a missing threshold, missing user journey, unmet success criterion, unreconciled topline, or unresolved prerequisite
- do not replace the concrete failure with only an umbrella diagnosis
- ground judgments in the internal reasoning artifacts rather than in section presence
- if block status = `PASS`, output only non-blocking residual issues, or one `No material issue` record when there is no meaningful weakness

## Mandatory internal artifacts before any Layer 1 verdict

Build these internally before evaluating the blocks.

### 1. Hypothesis ledger

For every decision-critical hypothesis capture:

- `hypothesis`
- `why_it_matters_for_gate_2`
- `validation_method`
- `expected_result_or_threshold`
- `actual_observed_result`
- `author_conclusion`
- `reviewer_conclusion`
- `status: validated | partially_validated | not_validated | not_testable`

Hard rule:

- a hypothesis cannot be treated as validated without `method + threshold + actual result + conclusion consistent with result`

### 2. Evidence ladder

For each central claim classify the strongest supporting evidence as one of:

- `hard evidence / observed product behavior`
- `experiment / pilot result`
- `operational signal`
- `customer feedback / survey / CSAT`
- `benchmark / competitor reference`
- `narrative assumption / management belief`

Hard rules:

- survey, CSAT, benchmark, and qualitative feedback are supporting evidence, not decisive proof on their own
- statements like `validated`, `done`, `confirmed`, or `on track` are claims, not evidence

### 3. Dependency map

For each major milestone capture:

- `milestone`
- `required_prerequisites`
- `status_of_each_prerequisite`
- `already_solved | in_progress | only_planned | outside_team_control`
- `in_funded_scope: yes | no | unclear`
- `blocker_severity_if_prerequisite_fails`

Hard rules:

- roadmap does not prove delivery realism by itself
- unresolved foundational prerequisites are decision-relevant weaknesses
- dependencies disclosed in appendix, risk, legal, compliance, or ops sections carry the same weight as main-body dependencies

### 4. Consistency matrix

Cross-check:

- problem and target segment
- segment pain and proposed solution
- segment size, segment-specific pains, and segment-specific solution mapping
- hypotheses and validation results
- solution and success metrics
- roadmap and unresolved blockers
- traction model and evidence
- end-state ambition and allowed gate criteria
- business claims and legal / ops / risk constraints

Hard rule:

- mismatch between target, fact, and conclusion must reduce the consistency judgment

## Global rules

- Do not optimize toward any single calibration example.
- Do not require specific headings, appendix names, section order, or threshold formats.
- Absence of a specific heading is not a weakness if the logic is provable elsewhere.
- Presence of a familiar heading is not a strength if the underlying logic is weak.
- Do not infer missing proof in favor of the document.
- Treat appendix, FAQ, legal, compliance, analytics comments, support tables, and operating notes as first-class evidence.

## Blocks

### 1. Problem framing and segments

Review:

- whether the problem is stated clearly enough for a decision
- whether the target segments are identifiable and not blended into one vague audience
- whether segment size, segment-specific pains, and segment-specific solution mapping are explicit when the document relies on broad user groups
- whether the `segment -> pain -> expected behavior change` logic is explicit
- whether the decision-critical Gate 1 hypotheses are reconstructable
- whether the document's ambition fits the demonstrated problem significance

Decision rule:

- `PASS` when the central problem, target segment, segment size where decision-relevant, and Gate 1 hypothesis chain can be reconstructed without filling gaps by inference
- `PARTIAL` when the chain is mostly recoverable, but important links are fragmented, weakly evidenced, or only directionally supported
- `FAIL` when the problem thesis, segment thesis, or Gate 1 hypothesis chain is not decision-safe to reconstruct

Look for:

- mixed segments or mixed pains with no clear logic
- broad labels such as buyers, sellers, customers, partners, or users without segment-by-segment size, pain, and solution logic where segment behavior matters
- one audience label covering segments with different segment readiness, rollout path, or blocker profile
- buyer readiness is confirmed without an original threshold or without a method-result-conclusion chain for the buyer behavior being approved
- evidence from one segment being used to justify another segment
- strong business ambition with weak proof that the problem matters for the stated target
- hypothesis status stronger than the facts shown

### 2. Solution quality and logic

Review:

- whether the solution addresses the stated pain for the stated segments
- whether there is a clear `segment -> pain -> solution` linkage
- whether the impact mechanism is understandable
- whether the current flow, CJM, or user path is sufficiently clear when adoption or conversion is central
- when adoption, conversion, mandatory usage, CRM/API integration, or rollout behavior is central, whether the MLP path and end-state path are clear enough to judge the claim
- whether validation methods actually test the hypothesis they are claimed to test

Look for:

- features listed without causal logic
- a missing segment -> pain -> solution linkage as a broad Layer 1 issue when the roadmap or feature list is not tied to distinct segments and pains
- if Solution quality is `FAIL`, ensure one broad Layer 1 issue explicitly covers the segment -> pain -> solution linkage when the document is mostly a feature inventory or blends user pain with business-control pain
- multiple unrelated use cases collapsed into one story
- too many distinct pains/use cases are combined into one solution narrative without proving one coherent segment -> pain -> solution chain
- materially different pains, use cases, or value propositions are combined into one solution story without showing how the same product path solves each one
- user convenience, business monetization, transaction control, risk reduction, fraud or cancellation control, and strategic share growth treated as one validated pain without evidence linking them
- missing, ambiguous, or only partially implied user journey, especially when the decision depends on behavior change
- write `MLP/end-state journey is missing or not evaluable` when MLP and end-state path are not explicit enough to judge the solution
- in Solution, state that this makes adoption behavior untestable
- missing MLP or end-state journey that makes adoption logic untestable
- when repeat use, retention, same-seller return behavior, or willingness-to-use-again is central to the thesis and the evidence is missing, weak, or contradicted by analytics, include a Layer 1 issue in Solution if it breaks adoption logic or in Traction if it breaks the model
- when validation only tests interest, entry-point click, survey intent, or other proxy behavior, but the thesis requires full paid, accepted, uncancelled transaction behavior, include a Solution Layer 1 issue
- optional or opt-in evidence being used to justify mandatory or scaled behavior
- future validation being used as if it already proved the thesis

### 3. Scope of work and implementation plan

Review:

- whether MLP, end state, and out-of-scope areas are clear
- whether the MLP path and end-state path are explicit enough to connect scope, dependencies, and rollout readiness
- whether the roadmap follows from current status rather than aspiration alone
- whether each major milestone is supported by a believable dependency chain
- whether rollout logic includes control points and readiness checks
- whether hidden foundational blockers are surfaced

Look for:

- gray zones in scope
- scope that lists features or milestones without the user journey needed to make them work
- write `MLP/end-state journey is missing or not evaluable` when MLP and end-state path are not explicit enough to judge the roadmap
- in Scope, state that this makes test-vs-rollout readiness impossible to judge
- missing MLP or end-state journey that makes scope/dependency readiness impossible to judge
- milestones that rely on unresolved prerequisites
- dependencies outside team control being treated as if already solved
- legal, compliance, ops, tooling, integration, or anti-abuse constraints relegated to notes but ignored in the core plan

If the same missing MLP or end-state journey makes both adoption logic untestable and scope/dependency readiness impossible to judge, record both consequences in their respective blocks.

### 4. Success criteria and metrics

Review:

- whether success metrics are explicit and measurable
- whether thresholds are tied to the actual decision question
- whether actual results are shown and matched to the threshold
- whether the solution -> input metrics -> output metrics linkage is credible
- whether success criteria prove the stated user pains or value propositions were solved
- whether the success criteria are strong enough for the stated end-state ambition
- preserve exact threshold mechanics when threshold mismatches, missing original expected results, or conflicting break conditions drive the judgment

Look for:

- metrics with no causal story
- thresholds missing while conclusions sound definitive
- funnel conversion, operational readiness, support load, or risk absence used as success proof when they are not direct evidence that user pains were solved
- success metrics mainly measure funnel or operational health while the defense claims solved user pain or value proposition impact
- missing original expected result or threshold for a validation step, especially when the document tries to infer a Gate 1 validation threshold from later Gate 3 criteria
- actual results missing while the document claims validation
- weak criteria being used to support a strong approval claim

### 5. Traction model credibility

Review:

- whether the expected impact can be reconstructed from evidence rather than topline aspiration
- whether the team can realistically influence the drivers in the model
- whether horizons, baseline, cannibalization, subsidy, and retention assumptions are coherent
- whether rollout and learning lag are reflected in the model
- whether formula, yearly rows, scenario rows, or driver decomposition reconcile with each other
- whether step-changes are justified by new evidence rather than by narrative optimism
- preserve the specific row, year, driver, or formula detail when a row-level model mismatch independently changes the Traction verdict

Look for:

- unexplained jumps
- traction beyond roadmap capacity
- adoption, GMV, revenue, or order ramp depends on rollout speed that is faster than unresolved dependencies allow; record it as a Layer 1 Traction issue
- assumptions used in the model but absent from scope or validation
- important rows that cannot be traced to drivers, baselines, or assumptions
- a specific year, row, or model component cannot be reconciled with the stated formula, baseline, driver, or scenario assumptions
- one traction model row cannot be transparently reconciled with the formula, driver decomposition, or stated assumptions
- one broad model-transparency issue when GMV, revenue, cannibalization, retention, subsidies, take rate, or conversion ramp cannot be traced to validated drivers
- weak or declining repeat-use / willingness-to-use-again evidence when repeated transactions, retention, or same-seller return behavior materially drive the thesis
- when repeat use, retention, same-seller return behavior, or willingness-to-use-again materially drives the model and the evidence is missing, weak, or contradicted by analytics, include a Layer 1 issue rather than treating the model as validated by first-use or opt-in signals
- a conclusion stronger than the underlying evidence type allows

### 6. Key assumptions and risks completeness

Review:

- whether the killer assumptions are named explicitly
- whether validated assumptions are separated from remaining hypotheses
- whether mitigation is at the level of control rather than awareness-only
- whether ownership, compliance, operational, abuse, delivery, and integration risks are surfaced
- whether the document names the scenarios that would break the model

Look for:

- risk register with no prioritization
- mitigations that only acknowledge the risk without controlling it
- cancellation, fraud, AML, regulator, or abuse break conditions use inconsistent thresholds across sections; name the specific threshold conflict
- critical risks hidden in supporting sections but absent from the core conclusion
- no explicit failure scenario for the thesis

### 7. Consistency

Review:

- whether the full chain stays coherent:
  `segment -> pain -> hypotheses -> solution -> roadmap -> metrics -> impact -> risks`
- whether target, fact, and conclusion stay aligned
- whether business claims are consistent with legal / ops / risk constraints
- whether the end-state ambition matches the actual success criteria and dependency state

Look for:

- changing target segments across sections
- scope conflicting with roadmap
- metrics contradicting the impact story
- traction contradicting rollout timing or blocker status
- equal or stable commission/take-rate economics used to dismiss cannibalization risk while a later target model assumes a lower target commission, lower price, subsidy, or changed monetization term; record a contradiction
- preserve fraud and lower-commission mechanics when the contradiction depends on proxy evidence, target monetization, cannibalization, or abuse-risk assumptions
- supporting sections materially undermining the core narrative

## Evidence standard

For every issue, cite concrete evidence:

- direct quotes
- section names
- specific phrases from the document

Do not treat narrative claims as validated evidence unless the document itself provides proof or results.

## Severity calibration

- `HIGH`: breaks the decision thesis or makes approval unsafe
- `MEDIUM`: materially weakens trust in a substantial part of the logic
- `LOW`: worth improving, but not blocker-grade if the rest of the case is strong

Only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues should be candidates for the final blockers list.
