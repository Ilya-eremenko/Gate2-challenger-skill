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
