# Layer 1 Rubric

Layer 1 is the broad, open-world review of the document as a decision narrative.

Layer 1 is block-level only. No atomic questions in the output.

For each block:

- assign `APPROVE`, `NEED_EVIDENCE`, or `REJECT`
- identify whether the block is a blocker
- output up to 3 decision-relevant issues
- prefer block-level, chain-level, and consistency-level issues over checklist-style detail
- ground judgments in the internal reasoning artifacts rather than in section presence
- if block verdict = `APPROVE`, do not output `top_issues`

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
- whether the `segment -> pain -> expected behavior change` logic is explicit
- whether the decision-critical Gate 1 hypotheses are reconstructable
- whether the document's ambition fits the demonstrated problem significance

Decision rule:

- `APPROVE` when the central problem, target segment, and Gate 1 hypothesis chain can be reconstructed without filling gaps by inference
- `NEED_EVIDENCE` when the chain is mostly recoverable, but important links are fragmented, weakly evidenced, or only directionally supported
- `REJECT` when the problem thesis, segment thesis, or Gate 1 hypothesis chain is not decision-safe to reconstruct

Look for:

- mixed segments or mixed pains with no clear logic
- evidence from one segment being used to justify another segment
- strong business ambition with weak proof that the problem matters for the stated target
- hypothesis status stronger than the facts shown

### 2. Solution quality and logic

Review:

- whether the solution addresses the stated pain for the stated segments
- whether there is a clear `segment -> pain -> solution` linkage
- whether the impact mechanism is understandable
- whether the current flow, CJM, or user path is sufficiently clear when adoption or conversion is central
- whether validation methods actually test the hypothesis they are claimed to test

Look for:

- features listed without causal logic
- multiple unrelated use cases collapsed into one story
- optional or opt-in evidence being used to justify mandatory or scaled behavior
- future validation being used as if it already proved the thesis

### 3. Scope of work and implementation plan

Review:

- whether MLP, end state, and out-of-scope areas are clear
- whether the roadmap follows from current status rather than aspiration alone
- whether each major milestone is supported by a believable dependency chain
- whether rollout logic includes control points and readiness checks
- whether hidden foundational blockers are surfaced

Look for:

- gray zones in scope
- milestones that rely on unresolved prerequisites
- dependencies outside team control being treated as if already solved
- legal, compliance, ops, tooling, integration, or anti-abuse constraints relegated to notes but ignored in the core plan

### 4. Success criteria and metrics

Review:

- whether success metrics are explicit and measurable
- whether thresholds are tied to the actual decision question
- whether actual results are shown and matched to the threshold
- whether the solution -> input metrics -> output metrics linkage is credible
- whether the success criteria are strong enough for the stated end-state ambition

Look for:

- metrics with no causal story
- thresholds missing while conclusions sound definitive
- actual results missing while the document claims validation
- weak criteria being used to support a strong approval claim

### 5. Traction model credibility

Review:

- whether the expected impact can be reconstructed from evidence rather than topline aspiration
- whether the team can realistically influence the drivers in the model
- whether horizons, baseline, cannibalization, subsidy, and retention assumptions are coherent
- whether rollout and learning lag are reflected in the model
- whether step-changes are justified by new evidence rather than by narrative optimism

Look for:

- unexplained jumps
- traction beyond roadmap capacity
- assumptions used in the model but absent from scope or validation
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
