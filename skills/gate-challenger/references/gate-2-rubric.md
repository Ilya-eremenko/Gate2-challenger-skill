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
- every issue must be self-contained for a reader who has not opened the source document: state what is wrong, why it matters for the gate decision, and what decision consequence follows
- write `issue` and explanatory `evidence` in Russian by default; preserve English only for source section names, metric names, product names, exact quotes, schema keys, and status values
- avoid mixed-language explanations such as `approval unsafe`, `proof gap`, `decision-ready`, or `blocker-grade`; use natural Russian wording instead
- write each issue as a human-readable mini-argument: context, broken decision test, and gate consequence
- prefer two compact sentences over one overloaded sentence when the issue contains both a proof gap and an approval consequence
- readability is a presentation layer: do not create an extra Layer 1 issue, split a root cause, or upgrade severity only because the explanation can include more detail
- when extra detail supports an already-selected Layer 1 blocker, put it in `evidence` instead of promoting it to another issue
- readability and deduplication must not suppress distinct block consequences required by the rubric; the same root cause may appear in different blocks when the decision consequence is different
- evidence must include the section or table name plus the exact values, thresholds, dates, user segments, or claims being compared
- do not cite a section name without explaining what in that section proves the issue
- when evidence is a contradiction, include both sides of the contradiction in the evidence field
- evidence should connect the cited facts explicitly: source A says the target or claim, source B shows the result or dependency, and the final clause explains why that comparison proves the issue
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
- when willingness-to-use-again or repeat-use evidence is weak or declining, preserve the direction and exact rates rather than citing only a generic retention or analytics concern
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
- when end-state ambition and gate criteria disagree, preserve both sides of the mismatch and the concrete threshold or allowance that creates it
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
- do not narrow a broad model-transparency issue to only conversion ramp or take rate when the document also has unreconciled GMV, revenue, cannibalization, retention, subsidy, baseline, or topline components
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

## Gate 2 Layer 2 Atomic Rubric

# Layer 2 Rubric

Layer 2 is the closed-world, detailed diagnostic pass.

Layer 2 is atomic and diagnostic.

For each atomic question:

- reason internally as `PASS`, `PARTIAL`, or `FAIL`
- answer externally as `YES`, `PARTIAL`, or `NO`
- provide evidence
- always provide a short issue statement; use `No material issue` only when the answer is `YES` and there is no meaningful weakness

Mapping rule:

- `PASS` -> `YES`
- `PARTIAL` -> `PARTIAL`
- `FAIL` -> `NO`

For every atomic question, the reasoning must answer three things even if the output remains compact:

1. what exactly is being checked
2. what evidence the conclusion depends on
3. what decision-relevant consequence follows from `PASS`, `PARTIAL`, or `FAIL`

Layer 2 is not meant to enumerate every imaginable risk in the document. Its role is to provide repeatable, evidence-rich detail for explicit weak links and to support later synthesis through evidence rather than replace Layer 1 on style alone.

Materiality threshold:

- answer `PARTIAL` or `NO` only when the issue changes approval safety, validation strength, or the block verdict
- if an atomic check finds only a plausible nuance, generic completeness concern, or already-covered concern, answer `YES` with `No material issue` or use `same duplicate family; local angle:`
- suppress non-central extras such as broad prioritization, softer-alternative comparison, generic projected-upside concern, generic downside-sensitivity absence, or generic segment mapping weakness unless the document's decision thesis depends on that point
- answer every atomic check internally, but emit a standalone Layer 2 issue only when the weakness is concrete, decision-relevant, and not already represented by a stronger nearby issue
- generic weak-link checks default to `YES` / `No material issue` unless there is a specific contradiction, threshold miss, formula gap, unresolved dependency, unsupported scaling leap, or inconsistent risk control
- do not emit generic standalone issues for broad target clarity, segment mapping, projected upside, softer alternatives, or downside sensitivity when they only restate a stronger nearby issue
- every atomic question must still be answered against its own decision test
- if there is concrete evidence for a problem-bearing atomic check, record the issue even when the same family is also covered elsewhere
- when a problem-bearing atomic check repeats the same family, use `same duplicate family; local angle:` only when the local consequence is materially different; do not turn the issue into `YES` / `No material issue` if that would hide a real decision defect, but do not create a second standalone issue for the same defect
- for explicit weak-link checks covering target clarity, segment mapping, current-state significance, prioritization, softer alternatives, approval boundary, planning-vs-validation, metric reconciliation, changed monetization, downside scenarios, external dependency classification, problem drift, or supporting-section caution, must not suppress it as generic when evidence shows a decision-relevant weakness
- for softer-alternative checks, declared strategic fit or stakeholder approval is not enough for `YES` when the chosen path adds mandatory adoption, closure, regulatory, churn, abuse, or resource risk; answer against whether the high-risk path is justified versus lower-risk alternatives

Layer 2 output budget:

- emit at most the two strongest distinct issue families per Atomic checks block; if more families are present, choose the ones most likely to change approval safety or block verdict
- additional atomic checks should reference the selected family in evidence rather than create another issue
- if a third family is truly blocker-grade and independent, keep it only when it is not evidence for either selected family and would change the block status by itself
- family consolidation should happen before formatting, not after the output is already written
- selected issue families are a pre-output control, not an optional writing style
- only the selected representative atomic answer gets full standalone issue text
- each selected representative issue must be self-contained for a reader who has not opened the source document
- selected representatives must state what is wrong, why it matters for the gate decision, and what decision consequence follows
- avoid label-only issue text such as `proxy-validation:` without a plain-language explanation
- write selected representative `issue` and explanatory `evidence` in Russian by default; preserve English only for source section names, metric names, product names, exact quotes, schema keys, status values, and duplicate-family keys
- when using duplicate-family keys such as `proxy-validation` or `dependency-readiness`, first write a Russian explanation of the problem, then add the key only as a compact label if useful
- if a duplicate-family key is useful, attach it to a plain-language explanation rather than leaving it as the issue itself
- write selected representative issues as mini-arguments: context, broken atomic decision test, and gate consequence
- readability is a presentation layer: do not create an extra standalone atomic issue, split a duplicate family, or upgrade a block status only because the explanation can include more detail
- when extra detail supports an already-selected duplicate family, put it in `evidence` or `same duplicate family` wording instead of promoting it to another issue
- evidence must include section or table name plus the exact values, thresholds, dates, user segments, or claims being compared
- do not cite a section name without explaining what in that section proves the issue
- when evidence is a contradiction, include both sides of the contradiction in the evidence field
- evidence should connect the cited facts explicitly: source A says the target or claim, source B shows the result or dependency, and the final clause explains why that comparison proves the issue
- non-selected repeated atomic answers must use `same duplicate family; see <family>`
- do not add a second local-angle issue sentence for the same family

Specificity anchors:

- preserve exact threshold mechanics when the document gives thresholds, expected results, actual results, or conflicting break conditions
- preserve the specific row, year, driver, or formula detail when criticizing model reconciliation, yearly rows, ramp assumptions, conversion, availability, or take-rate logic
- preserve fraud and lower-commission mechanics when proxy validation or monetization evidence is used to support a different target-state behavior

Global rules:

- Treat appendix, FAQ, legal, compliance, analytics comments, support tables, and operating notes as first-class evidence.
- Do not require a specific section title when the needed logic is provable elsewhere.
- Do not reward a familiar section title when the logic under it is weak.
- Future tests or planned work do not count as present proof for the current gate.
- avoid restating the same insight as separate standalone failures across multiple atomic questions; when a later question touches an already-covered concern, use the local angle only, for example: "same prerequisite gap, here specifically affecting test-vs-rollout gating."

## 1. Problem framing and significance

- Can the reviewer identify the target segment, pain, and intended behavior change without restoring missing logic by inference?
- Are segment size, segment-specific pains, and segment-specific solution mapping clear when the document uses broad user groups?
- Is significance grounded in a quantified current-state problem rather than mainly in projected upside?
- If several problem statements coexist, are they prioritized rather than blended into one vague rationale?
- Can the core Gate 2 decision thesis be traced back to the decision-critical Gate 1 hypotheses?
- For each decision-critical hypothesis, are the expected result, actual result, and conclusion aligned?
- If strategic alignment is claimed, is the chosen path justified against softer alternatives?
- Is evidence from one segment, one use case, or one flow being stretched to justify a different segment, use case, or flow?

## 2. Solution quality and logic

- Is it clear which exact user, pain, and gate-stage problem the initiative solves?
- Are user pain, business-control pain, and operational risk separated rather than combined as one problem?
- If materially different pains, use cases, or value propositions are combined into one solution story, does the document show how the same product path solves each one?
- Does the roadmap read as a segment -> pain -> solution chain rather than a feature inventory?
- Does each central hypothesis use a validation method that actually answers the decision question?
- If a claim concerns mandatory or scaled behavior, is the evidence drawn from that same behavior rather than from an optional or opt-in proxy?
- Is the causal mechanism from solution elements to metric movement explicit rather than implied?
- Is the current flow / CJM / key user path clear enough to judge adoption or conversion claims when those claims are central?
- When adoption, conversion, mandatory usage, CRM/API integration, or rollout behavior is central, are the MLP path and end-state path explicit enough to evaluate the claim?

## 3. Scope of work and implementation plan

- Is the roadmap sequence supported by the dependency picture, rather than faster than readiness allows?
- Does each major milestone have explicit prerequisites rather than only a target date?
- Are unresolved foundational dependencies treated as decision-relevant weaknesses rather than as neutral future work?
- Are key prerequisites already solved, in progress, only planned, or outside team control, and is that status reflected honestly in the roadmap?
- Are rollout checkpoints tied to operational, legal, compliance, tooling, integration, or abuse-readiness constraints where those constraints matter?
- Are resources, ownership, delivery capacity, and horizontal dependencies secured for the work being approved now?

Scope resource rule:

- headcount, support, billing, legal, T&S, anti-fraud, API, and partner-team dependencies must be assessed in Layer 2 even if they are already mentioned in Layer 1

## 4. Success criteria and metrics

- Is the approval boundary clear: what exactly is being approved now, and what remains future evidence?
- Is each claimed success criterion measurable and tied to the actual decision question?
- Do success criteria prove the stated user pains or value propositions were solved, rather than measuring only funnel conversion, operational readiness, support load, or risk absence?
- Is there an explicit threshold where the document claims validation rather than observation, and do thresholds exist for the decision-critical claims?
- When a threshold exists, do the actual observed results meet it?
- Are planning statements, scope declarations, or roadmap commitments kept separate from validation?
- Are output claims supported by input or proxy metrics that plausibly explain how the result was achieved?
- Are Metric definitions, toplines, horizons, and baselines reconciled before they support the decision?
- If take rate, price, commission, subsidy, or monetization terms change across horizons, is there evidence for the changed value rather than only evidence for the current value?
- Are the success criteria strong enough for the stated end-state ambition?

Threshold answer rule:

- do not infer a Gate 1 validation threshold from later Gate 3 criteria; require the original expected result or threshold for that validation step
- answer `YES` only when thresholds exist for the decision-critical claims, not merely because some thresholds exist somewhere in the document
- answer `PARTIAL` when some thresholds exist but the strongest decision claims still lack explicit decision rules
- answer `NO` when validation is claimed without thresholds for the central claims

## 5. Traction model credibility

- Can the expected impact be reconstructed from concrete drivers and evidence rather than from topline assertion?
- When a model has a formula, yearly rows, scenario rows, or driver decomposition, do important rows reconcile with the formula and stated drivers?
- Are horizons, adoption lag, and learning periods consistent with the roadmap and rollout plan?
- Does the model rely on aggressive step-changes, unsupported baselines, or assumptions outside funded scope?
- Does the model treat evidence for a current value as proof for a changed value in take rate, price, commission, subsidy, or monetization terms?
- If equal or stable commission/take-rate economics are used to dismiss cannibalization risk, but the document later assumes a lower target commission, lower price, subsidy, or changed monetization term, is that contradiction resolved?
- monetization/cannibalization contradiction can appear in Traction and Consistency when each has a distinct consequence; Traction: model economics are unsupported or internally inconsistent
- Is the evidence behind the model directional or definitive, and does the document keep the conclusion at the same strength level?
- Are Quotes, surveys, CSAT, and benchmarks treated as supporting signals rather than decisive proof for central business claims?
- Is the financial case resilient to downside scenarios already visible in the document?

## 6. Key assumptions and risks completeness

- Are the killer assumptions explicit, and are validated assumptions separated from remaining hypotheses?
- Do mitigations control the risk, rather than merely acknowledge it?
- Owners may be named, but are risk mitigations implemented or committed beyond planning language?
- Do supporting sections surface unresolved legal, compliance, abuse, operational, or integration constraints that materially affect rollout readiness?
- Are external dependencies classified as secured, in progress, contingent, or outside team control?
- Does the document define a scenario in which the model or rollout thesis stops holding together?

Risk answer rule:

- distinguish risk discovery/visibility, control maturity, and centrality in the decision narrative
- if major risks are visible but controls are immature or only planned, answer `PARTIAL`, not `YES` with `No material issue`
- if legal, compliance, abuse, moderation, support, or integration constraints are visible but not central enough in the decision narrative, state that gap explicitly
- if cancellation, fraud, AML, regulator, or abuse break conditions use inconsistent thresholds across sections, name the specific threshold conflict

## 7. Consistency

- Can the reviewer restore a continuous chain of `segment -> pain -> hypotheses -> solution -> roadmap -> metrics -> impact` without major logical jumps?
- Check whether the problem definition drifts across the document, or stays stable from pain to solution to monetization and risk logic.
- Do target, fact, and conclusion stay aligned across sections?
- Do ambition, metrics, roadmap, traction, and risks describe the same end-state, or do they pull in different directions?
- If equal or stable commission/take-rate economics are used to dismiss cannibalization risk, but the document later assumes a lower target commission, lower price, subsidy, or changed monetization term, record a contradiction.
- monetization/cannibalization contradiction can appear in Traction and Consistency when each has a distinct consequence; Consistency: risk defense contradicts target economics
- When supporting sections and main narrative disagree, is the disagreement visible in the decision logic rather than ignored?

Duplicate-localization rule:

- use local-angle wording to avoid duplicate penalties when the same issue family affects distinct atomic checks

## Aggregation reminder

Layer 2 block aggregation unit is the whole Atomic checks block, not the individual atomic question.

Do not count atomic failures directly as final blockers without first aggregating them back into the Atomic checks block status.

Use Layer 2 block statuses as:

- `PASS` when the atomic checks show no blocker-grade or material evidence gaps
- `PARTIAL` when the block is mostly coherent, but one or more decision-critical proof points remain incomplete
- `FAIL` when the atomic failures expose a blocker-grade contradiction, missing proof, broken validation method, broken causal chain, or unresolved foundational dependency
