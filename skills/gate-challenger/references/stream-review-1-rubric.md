# 1st Stream Review Rubric

## Purpose

Use this rubric after the coordinator determines that the input is a 1st Stream Review / SR 1 initiative defense document.

1st Stream Review answers a Gate-2-like decision question for a stream:

```text
Did the team prove, with discovery evidence and validated product ideas, that the
stream's traction model, resources, and roadmap are decision-ready for the current
IC ask and for the next Stream Review path?
```

This rubric is stage-specific. It should be combined with the shared evidence standard, consistency rules, verdict policy, output contract, synthesis contract, and adversarial review rules that are common to all gates.

Do not duplicate common checks here unless 1st Stream Review changes the decision test.

## 1st Stream Review Decision Boundary

Before scoring dimensions, identify exactly what the document asks the committee to approve:

- continuation of discovery
- validation of selected product ideas
- resources or funding for the next stream period
- development roadmap for 1+ year
- traction and financial model used for IC planning
- horizontal or vertical cost allocation
- conditions and commitments before the next SR

Approval must be scoped. `APPROVE` for 1st Stream Review does not automatically mean production scale, PMF, 2+ Stream Review readiness, Gate 3 readiness, or baseline transfer. It means the discovery-backed stream plan is safe within the approval scope shown by the document.

The final synthesis should explicitly separate:

- `approval_scope`: what stream scope, product ideas, resources, or roadmap steps are safe to approve now
- `not_approved_scope`: what remains unproven or outside the current SR 1 evidence
- `next_sr_conditions`: evidence, milestones, go / no-go rules, controls, and validation commitments required before the next SR

Do not require production / MLP evidence unless the document claims production progress, rollout readiness, or scale.

## 1st Stream Review Internal Artifacts

Build these artifacts internally before Layer 1, Layer 2, and Layer 3 verdicting.

### 1. Discovery Evidence Ledger

For every decision-critical discovery claim capture:

- discovery question or hypothesis
- target segment, pain, and expected behavior change
- method: interview, survey, fake-door test, prototype, concierge test, analytics cut, operational observation, benchmark, or other
- sample, period, channel, and limitations where available
- expected result / threshold
- actual observed result
- author conclusion
- reviewer conclusion
- status: validated / partially_validated / invalidated / still_open / not_testable

Hard rules:

- A discovery claim cannot be treated as validated without `method + expected result or threshold + actual result + conclusion consistent with result`.
- Invalidated hypotheses are not a weakness by themselves. They become a weakness when the document hides them, ignores their consequence for roadmap / traction, or still asks approval as if they were validated.
- Survey, interview, benchmark, and stakeholder feedback are supporting evidence. They do not prove scale, monetization, retention, or production readiness by themselves.

### 2. Validated Product Ideas Ledger

For every product idea that the stream asks IC to accept capture:

- product idea
- segment and pain it solves
- validation evidence
- behavior or metric it is expected to change
- current confidence level
- remaining hypothesis or risk
- impact on roadmap, resources, traction, or next SR commitments

Hard rules:

- A product idea is not validated just because it appears in the roadmap.
- A feature list is not a solution thesis unless it preserves the `segment -> pain -> product idea -> behavior change -> metric` chain.
- Evidence from an optional or low-risk discovery proxy cannot prove mandatory, paid, high-risk, or scaled behavior unless the document explains the bridge.

### 3. Progress, Roadmap, And Resource Map

For each major roadmap or progress claim capture:

- current progress by the moment
- milestone and target date
- user value or capability delivered by the milestone
- owner and required resources
- Tech peer / TDR / tech solution validation status
- horizontal dependencies and vertical support where relevant
- status of prerequisites: solved / in progress / planned / contingent / outside team control
- whether the prerequisite is in the funded scope
- consequence if the prerequisite fails

Hard rules:

- Roadmap dates do not prove delivery realism.
- Progress claims must be separated from future commitments.
- A 1+ year roadmap should follow from discovery learning and dependency readiness, not only from ambition.
- If the recommended TTM from initiative start to 1st Stream Review exceeds 3 months, the document should explain what was learned during the extra time and why the evidence remains current enough for the decision.

### 4. Traction, Finance, And Traffic Light Ledger

For each material business or financial claim capture:

- input metric, output metric, baseline, horizon, and formula / driver
- plan / fact where the current period is shown
- Traction YTD deviation and traffic-light color
- Analytics semaphore and validation conclusion
- InvCo / FBP validation
- Vertical support for horizontal cases
- cost allocation logic and match to 3Sigma where relevant
- financial summary, Increment / ToBe P&L, Kismet triggers, and resource ask where relevant
- whether yellow / red traffic-light concerns are reflected in the main decision narrative

Hard rules:

- A green traffic light is not proof by itself.
- A yellow or red signal must be explained in the main approval logic, not buried in FAQ 6.
- The traction model must be reconstructable from drivers and evidence, not only from topline aspiration.
- Resource and cost assumptions must match the approved stream scope.

### 5. Consistency Matrix

Cross-check:

- discovery -> validated product ideas -> solution -> progress -> roadmap -> metrics -> traction -> resources -> risks -> next SR
- target segment and product idea
- discovery fact and author conclusion
- roadmap and unresolved dependencies
- traction model and resource ask
- traffic-light concerns and main narrative confidence
- IC ask and proof boundary

Hard rule:

- If target, fact, and conclusion disagree, reduce the consistency judgment even when each section is individually well written.

## Layer 1: 1st Stream Review Decision-Critical Dimensions

Layer 1 is the broad decision narrative review. Assign each dimension `PASS`, `PARTIAL`, or `FAIL`.

For each dimension:

- output up to 3 decision-relevant issues
- prefer one broad issue per root cause
- cite concrete source sections, values, dates, thresholds, traffic lights, commitments, and contradictions
- write human-facing issue explanations in Russian by default

### 1. Discovery thesis, problem, and segments

Review whether the stream's discovery thesis is decision-ready.

`PASS` when:

- target segments, pains, segment size where relevant, and intended behavior changes are reconstructable
- discovery questions / hypotheses are visible
- validated, partially validated, invalidated, and still-open hypotheses are separated
- the stream ambition fits the demonstrated problem significance

`PARTIAL` when the chain is mostly recoverable but fragmented, weakly evidenced, or only directionally supported.

`FAIL` when the reviewer cannot safely reconstruct the stream problem thesis or the discovery basis for selected product ideas.

Look for:

- broad stream idea with no segment-specific pain
- discovery methods named without results, thresholds, or limitations
- invalidated hypotheses hidden while their roadmap or traction consequence remains
- evidence from one segment or use case stretched to another
- strategic fit used instead of discovery proof

### 2. Validated product ideas and solution logic

Review whether the product ideas being defended actually follow from discovery evidence.

`PASS` when:

- each central product idea maps to a segment, pain, behavior change, metric, and validation result
- the current solution path and target-state path are clear enough to evaluate adoption or conversion claims
- business benefit, user value, operational control, and risk reduction are separated when they rely on different evidence

`PARTIAL` when ideas are plausible but some links in the product-idea evidence chain are weak or implied.

`FAIL` when the document is mostly a feature inventory, a roadmap list, or a narrative ambition without validated product logic.

Look for:

- feature list presented as validated product ideas
- multiple unrelated pains or value propositions collapsed into one stream story
- survey or interview interest used as proof of paid, repeated, mandatory, or scaled behavior
- future validation treated as current proof
- no clear user journey where adoption or conversion is central

### 3. Scope, progress, resources, and roadmap

Review whether current progress and future roadmap are believable for the current SR 1 approval.

`PASS` when:

- progress by the moment is shown separately from future scope
- MLP / near-term stream scope, end state, and out-of-scope areas are clear where relevant
- roadmap for 1+ year is linked to user value / capabilities and output metrics
- major milestones have prerequisites, owners, resources, and readiness checks
- Tech peer, TDR, tech solution validation, vertical support, and horizontal dependencies are reflected where relevant

`PARTIAL` when the roadmap is directionally coherent but readiness, resources, or dependency status is incomplete.

`FAIL` when the roadmap depends on unresolved foundational prerequisites or resources that are not secured for the requested scope.

Look for:

- roadmap faster than dependency readiness allows
- progress claims that are actually future commitments
- resource ask not connected to milestones and output metrics
- dependencies outside team control treated as solved
- risk, legal, support, billing, analytics, or vertical constraints hidden outside the roadmap

### 4. Success criteria and metrics

Review whether success criteria prove the stream's decision claims.

`PASS` when:

- success criteria are explicit for each decision-critical problem or product idea
- thresholds are present where the document claims validation
- actual discovery or progress results are compared with expected results
- input metrics explain output metrics
- FAQ 8 defines the next SR date, commitments, and hypotheses to validate

`PARTIAL` when metrics are measurable but only partially tied to the stream's core decision question.

`FAIL` when success criteria measure activity, funnel health, or operational readiness while the document claims validated product value or business impact.

Look for:

- validation claims without thresholds
- plan statements or roadmap commitments counted as evidence
- success metrics that do not test whether the user pain was reduced
- plan / fact, baseline, metric definitions, or horizons not reconciled
- next SR conditions too vague to hold the team accountable

### 5. Traction, finance, and resource credibility

Review whether the expected stream impact is reconstructable and financially coherent.

`PASS` when:

- planned traction can be reconstructed from input metrics, output metrics, baselines, horizons, and drivers
- Analytics semaphore, Traction YTD deviation, InvCo / FBP validation, and vertical support are reflected in the decision logic
- financial summary, Increment / ToBe case, cost allocation, Kismet triggers, and resource assumptions are consistent with the stream scope
- model assumptions are classified by evidence strength

`PARTIAL` when the model is directionally plausible but important drivers or validations remain incomplete.

`FAIL` when the traction / finance case is a topline aspiration, internally inconsistent, or materially broader than the discovery evidence and roadmap can support.

Look for:

- unexplained step-changes in adoption, revenue, GMV, margin, cost, HC, or output metrics
- changed plan values without evidence-backed reasons
- yellow / red validation signals absent from the main narrative
- cost allocation not linked to future impact
- positive ToBe case hiding weak incremental economics or uncommitted resources

### 6. Risks, alignments, and IC readiness

Review whether the document surfaces decision-critical risks and approvals.

`PASS` when:

- killer assumptions are explicit
- validated assumptions are separated from remaining hypotheses
- traffic-light concerns are explained
- T&S, support, moderation, marketing, billing, tax, legal, accounting, finance, HR, strategy, pricing, Tech, vertical, and domain-owner comments are reflected where relevant
- mitigations are controls or committed actions with owners, not only awareness statements

`PARTIAL` when risks are visible but controls, owners, or decision consequences are incomplete.

`FAIL` when unresolved legal, operational, financial, technical, or stakeholder constraints materially affect the current approval but are not integrated into the stream decision.

Look for:

- approvals recorded as dates without conditions or risk comments
- external dependencies not classified
- mitigations that only restate the risk
- yellow / red traffic-light issues hidden in FAQ 6
- no scenario where the traction, roadmap, or stream thesis stops holding

### 7. Consistency

Review whether the full SR 1 story is coherent:

```text
discovery -> validated product ideas -> solution -> progress -> roadmap -> metrics -> traction -> resources -> risks -> next SR
```

`PASS` when the chain can be restored without major inference and the IC ask is aligned with the proof boundary.

`PARTIAL` when the story is mostly coherent but has weakly linked or fragmented pieces.

`FAIL` when different sections defend different stream scopes, target segments, resource needs, economics, or readiness levels.

Look for:

- stream idea drift between FAQ 1, FAQ 2, traction, finance, and risks
- validated discovery evidence narrower than the requested approval
- roadmap not aligned with traction model, resources, or traffic-light concerns
- supporting sections materially more cautious than the executive summary
- next SR conditions not connected to remaining hypotheses

## Layer 2: 1st Stream Review Atomic Checks

Layer 2 is the closed-world diagnostic pass. Answer every atomic question as `YES`, `PARTIAL`, or `NO`, then aggregate back to Atomic checks block statuses using the common verdict policy.

Use SR 1 duplicate-family keys when useful: `stream-discovery-evidence`, `product-idea-validation`, `progress-vs-roadmap`, `resource-readiness`, `traffic-light-reflection`, `next-sr-conditions`, `scope-proof-boundary`, and `plan-fact-reconciliation`.

### 1. Discovery framing and evidence

- Can the reviewer identify the target segment, pain, and intended behavior change without restoring missing logic by inference?
- Are discovery questions, methods, sample / period, expected result or threshold, actual result, and conclusion shown for the decision-critical claims?
- Are validated, partially validated, invalidated, and still-open hypotheses separated?
- Are invalidated hypotheses reflected in roadmap, traction, scope, or risk decisions?
- Is significance grounded in current-state evidence rather than mainly projected upside?
- If several problem statements coexist, are they prioritized rather than blended into one stream rationale?
- Is evidence from one segment, use case, or flow being stretched to justify a different one?
- If the SR 1 timing exceeds the recommended 3 months from initiative start, does the document explain what was learned and why the evidence is still current?

### 2. Validated product ideas and solution logic

- Is each product idea tied to a specific segment, pain, expected behavior change, and metric?
- Does each central product idea use a validation method that actually answers the decision question?
- Are user value, business benefit, operational control, and risk reduction separated when their evidence differs?
- If materially different pains, use cases, or value propositions are combined, does the document show how the same product path solves each one?
- If a claim concerns paid, repeated, mandatory, integrated, or scaled behavior, is the evidence drawn from comparable behavior rather than an optional discovery proxy?
- Is the causal mechanism from product idea to input metrics and output metrics explicit?
- Is the current flow / CJM / user path clear enough to judge adoption or conversion claims when central?
- Are future validation steps kept separate from already validated product ideas?

### 3. Scope, progress, roadmap, and resources

- Is current progress by the moment explicitly separated from future roadmap commitments?
- Does the roadmap sequence follow dependency readiness rather than only target dates?
- Does each major milestone have prerequisites, owners, resources, and readiness checks?
- Are prerequisites classified as solved, in progress, planned, contingent, or outside team control?
- Are Tech peer alignment, TDR, tech solution validation, analytics, support, billing, legal, T&S, anti-fraud, API, and partner-team dependencies reflected where relevant?
- Are resources, HC, support capacity, delivery capacity, and horizontal dependencies secured for the work being approved now?
- Are rollout or development checkpoints tied to legal, operational, tooling, integration, or abuse-readiness constraints where those constraints matter?
- Is the 1+ year roadmap focused on user value / capabilities and impact on output metrics rather than feature inventory?

### 4. Success criteria and metrics

- Is the approval boundary clear: what exactly is being approved now, and what remains future evidence for the next SR?
- Is each success criterion measurable and tied to the actual stream decision question?
- Do success criteria prove the stated user pains or value propositions were addressed, rather than measuring only activity, funnel conversion, operational readiness, support load, or risk absence?
- Is there an explicit threshold where the document claims validation rather than observation?
- When a threshold exists, do actual results meet it?
- Are planning statements, scope declarations, and roadmap commitments kept separate from validation?
- Are input metrics, output metrics, baselines, horizons, and plan / fact reconciled?
- Does FAQ 8 define next SR date, commitments, hypotheses to validate, and go / no-go criteria?

### 5. Traction, finance, and traffic lights

- Can expected impact be reconstructed from concrete drivers and evidence rather than topline assertion?
- Do important model rows reconcile with formulas, baselines, driver decomposition, scenario rows, and horizons?
- Are current-period plan / fact values and Traction YTD deviation reconciled with the traffic-light color?
- Are Analytics semaphore, InvCo / FBP validation, Tech solution validation, and vertical support conclusions reflected in the main narrative?
- If traffic-light lines are yellow or red, are details, comments, links, and decision consequences provided in FAQ 6 and the main case?
- If planned values changed since the previous IC or initiative start, are previous value, current value, and reason for change provided?
- Does cost allocation across Verticals follow future impact and match the 3Sigma card where relevant?
- Are financial summary, Increment / ToBe case, Kismet triggers, and resources consistent with the approved stream scope?
- Is the financial case resilient to downside scenarios already visible in the document?

### 6. Risks, alignments, and controls

- Are killer assumptions explicit, and are validated assumptions separated from remaining hypotheses?
- Do mitigations control the risk rather than merely acknowledge it?
- Are owners, dates, and committed actions present for material risk mitigations?
- Do supporting sections surface unresolved legal, compliance, abuse, operational, integration, finance, pricing, or vertical constraints that materially affect readiness?
- Are external dependencies classified as secured, in progress, contingent, or outside team control?
- Are alignment / approval comments interpreted, rather than treated as green just because a date exists?
- Does the document define a scenario in which the traction model, roadmap, or stream thesis stops holding together?

### 7. Consistency

- Can the reviewer restore a continuous chain of `discovery -> validated product ideas -> solution -> progress -> roadmap -> metrics -> traction -> resources -> risks -> next SR` without major logical jumps?
- Does the problem definition stay stable from FAQ 1 through FAQ 2, traction, finance, and risks?
- Do target, fact, and conclusion stay aligned across sections?
- Do ambition, metrics, roadmap, resources, and risks describe the same stream scope?
- Are supporting-section cautions visible in the main decision narrative rather than ignored?
- Are next SR commitments tied to the remaining hypotheses and weakest proof points?

## 1st Stream Review Adversarial Lenses

Layer 3 should use these as stage-specific pressure prompts in addition to the common adversarial rubric. They are examples, not mandatory labels.

### Discovery laundering

Check whether interviews, survey intent, stakeholder optimism, or prototype feedback are converted into validated product ideas, roadmap confidence, or financial uplift without thresholds and comparable behavior.

### Stream scope creep

Check whether the committee is asked to approve a broad stream, platform, resource base, or financial case while discovery evidence validates only a narrow product idea, segment, or lower-risk flow.

### Resource-first approval

Check whether the document asks for HC, budget, tech capacity, vertical effort, or support load before the product ideas and next SR validation gates justify those resources.

### Roadmap as evidence

Check whether a 1+ year roadmap is used to make the case look complete even though the actual discovery proof, dependencies, or traffic-light concerns do not support it.

### Traffic-light insulation

Check whether yellow / red analytics, finance, tech, or vertical signals are parked in the traffic-light table or FAQ 6 but do not change the main approval request.

### Next SR ambiguity

Check whether the document avoids concrete next SR commitments, thresholds, go / no-go rules, or failure scenarios, leaving the next committee unable to judge whether SR 1 commitments were met.
