# 2+ Stream Review Rubric

## Purpose

Use this rubric after the coordinator determines that the input is a 2+ Stream Review / 2nd Stream Review document.

2+ Stream Review answers a recurring stream-control decision question:

```text
Did the team prove, with plan / fact results from the current period, that previous
SR commitments were closed or honestly revised, backlog and traction changes follow
from evidence, and the next quarterly or semiannual stream commitments are safe to approve?
```

This rubric is stage-specific. It should be combined with the shared evidence standard, consistency rules, verdict policy, output contract, synthesis contract, and adversarial review rules that are common to all gates.

Do not duplicate common checks here unless 2+ Stream Review changes the decision test.

Do not require PMF, Gate 4, baseline transfer, or production-scale evidence unless the document claims that scope.

## 2+ Stream Review Decision Boundary

Before scoring dimensions, identify exactly what the document asks the committee to approve:

- continuation of the stream for the next quarter or half-year
- no new approval, only financial monitoring
- additional resources, budget, HC, support, or cross-functional capacity
- updated backlog or roadmap scope
- updated traction model, financial summary, cost allocation, or Kismet treatment
- validation commitments, go / no-go rules, and review cadence before the next SR
- reuse of previous approvals because no significant context, expense, cost, product, or business decision changed

Approval must be scoped. `APPROVE` for 2+ Stream Review does not automatically mean production scale, PMF, Gate 4 readiness, or baseline transfer. It means the current period's plan / fact results, updated model, and next-period commitments are safe within the approval scope shown by the document.

The final synthesis should explicitly separate:

- `approval_scope`: what stream continuation, backlog change, resource ask, financial monitoring, or roadmap step is safe to approve now
- `not_approved_scope`: what remains unproven, broader than current plan / fact evidence, or outside this SR decision
- `next_sr_conditions`: commitments, metric thresholds, go / no-go rules, controls, and review date required before the next SR

## 2+ Stream Review Internal Artifacts

Build these artifacts internally before Layer 1, Layer 2, and Layer 3 verdicting.

### 1. Previous SR Commitment Ledger

For every decision-critical previous SR commitment capture:

- original commitment
- owner, expected date, expected result, and threshold where available
- status: delivered / partially_delivered / missed / changed / not_traceable
- actual result or current fact
- reason for miss or change
- whether the change is justified by new facts or only by narrative reframing
- consequence for backlog, roadmap, traction, resources, risks, and next SR

Hard rules:

- A changed commitment is not a weakness by itself. It becomes a weakness when the change is unexplained, hides a proof gap, or the document still asks approval as if the commitment was delivered.
- A previous SR summary is not enough; the decision-critical commitments must be traceable.

### 2. Plan-Fact And Traction Deviation Ledger

For each material plan / fact claim capture:

- metric, period, baseline, plan, fact, and deviation calculation
- input metric / output metric relationship
- traffic-light color and threshold used
- reason for deviation or plan change
- whether the explanation is evidence-backed, directional, or only asserted
- change format when applicable: `metric / previous plan / current plan / reason for change`
- decision consequence for continuation, resources, financial monitoring, or next SR conditions

Hard rules:

- A green traffic light is not proof by itself.
- Yellow or red signals must be reflected in the main approval logic, not only in FAQ 6.
- The actual 2+ SR traction thresholds are Green <=10%, Yellow:10%-20%, Red > 20%; Gate 3 example thresholds in template instructions do not determine the stage or the 2+ SR result.

### 3. Backlog And Roadmap Update Ledger

For every material backlog or roadmap update capture:

- product idea, segment, need, feature, timeline, and expected impact on metrics
- current progress by the moment
- what changed versus the previous SR
- plan / fact evidence or learning that caused the change
- Tech peer alignment status
- dependencies, owner, resource need, and readiness check
- whether the item is in the approved scope for the next period

Hard rules:

- A backlog item is not evidence of learning unless the document connects it to current-period facts or validated changes.
- A 1+ year roadmap should follow from plan / fact learning and dependency readiness, not only from ambition.

### 4. Finance, Resource, And Approval Carry-Forward Ledger

For each material resource, cost, finance, or approval claim capture:

- IC request type: new request / additional request / no request / financial monitoring
- resource, HC, support, and cross-functional capacity need
- cost allocation logic and match to 3Sigma where relevant
- financial summary, Increment / ToBe P&L, Kismet triggers, and 12M costs where relevant
- Analytics semaphore, InvCo / FBP validation, and Vertical support
- previous approvals reused or refreshed
- context, expense, cost, product, or business changes since previous approval
- caveats, owners, controls, and decision consequence

Hard rules:

- FAQ 7 may be skipped only when previous approvals remain valid and there are no significant changes in context, expenses, costs, product decisions, or business decisions.
- Previous approval carry-forward is unsafe when the approval context changed but caveats are not revalidated.

### 5. Next SR Commitment And Cadence Ledger

For each next-period commitment capture:

- next SR or financial monitoring date
- quarterly or semiannual cadence
- commitment, hypothesis, owner, metric, threshold, and expected result
- go / no-go rule or escalation trigger
- monitoring control before the next SR
- whether low-risk status and lack of significant deviation justify semiannual cadence

Hard rules:

- Next SR commitments must be concrete enough for the next committee to judge plan / fact closure.
- Semiannual cadence requires low-risk status and no material deviation; otherwise the document should define closer monitoring or quarterly review.

### 6. Consistency Matrix

Cross-check:

- stream-control spine: product vision -> limited input drivers -> current plan / fact -> learning -> next-period commitments
- previous SR -> commitments -> plan / fact -> learning -> backlog -> roadmap -> metrics -> traction -> resources -> risks -> next SR
- previous SR promise and current status
- current fact and author conclusion
- backlog update and plan / fact evidence
- roadmap and unresolved dependencies
- product vision and chosen input metrics
- limited input-driver focus and the full traction model
- traction changes and finance / resource ask
- traffic-light concerns and main narrative confidence
- skipped approvals and actual context changes
- next SR commitments and weakest open proof points

Hard rule:

- If target, fact, and conclusion disagree, reduce the consistency judgment even when each section is individually well written.
- Strong local detail does not compensate for a missing stream-control spine. If the reviewer cannot reconstruct the high-level product logic, the limited input drivers being managed, the current plan / fact result, and the next-period commitments as one chain, reduce the consistency judgment.

## Layer 1: 2+ Stream Review Decision-Critical Dimensions

Layer 1 is the broad decision narrative review. Assign each dimension `PASS`, `PARTIAL`, or `FAIL`.

For each dimension:

- output up to 3 decision-relevant issues
- prefer one broad issue per root cause
- cite concrete source sections, values, dates, thresholds, traffic lights, commitments, and contradictions
- write human-facing issue explanations in Russian by default

### 1. Previous SR Continuity And Current Decision Boundary

Review whether the current SR can be safely connected to the previous SR decision.

`PASS` when:

- previous SR commitments, expected results, and current IC request are reconstructable
- the current decision boundary is explicit
- continuation, additional request, no-request monitoring, resource ask, and future evidence are not blurred
- changes since the previous SR are explained by facts

`PARTIAL` when the chain is mostly recoverable but fragmented, or the ask is clear while some boundary conditions are implied.

`FAIL` when the reviewer cannot determine what was promised at the previous SR, what was achieved now, or what exactly is being approved.

Look for:

- previous SR summarized without commitment-level traceability
- current ask broader than current plan / fact evidence
- additional resources requested before deviations and learning justify them
- semiannual next review implied without low-risk and no-deviation support

### 2. Plan-Fact Results And Commitment Closure

Review whether the team closed or honestly revised previous SR commitments.

`PASS` when:

- every decision-critical commitment is tracked as delivered, partially delivered, missed, or changed
- plan and fact are compared for target input and output metrics
- deviations have evidence-backed reasons
- missed or changed items are reflected in backlog, traction, resources, risks, or next SR conditions

`PARTIAL` when plan / fact evidence is directionally useful but some commitments, thresholds, or reasons remain incomplete.

`FAIL` when missed commitments are hidden, rewritten without evidence, or treated as neutral future work while the document asks for continuation as if the plan was met.

Look for:

- progress claims that are actually future commitments
- traffic-light color not reconciled with deviation
- plan changes without previous value, current value, and reason
- author conclusion stronger than actual facts

### 3. Product Learning, Backlog, And Roadmap Update

Review whether the updated backlog and 1+ year roadmap follow from current-period learning.

`PASS` when:

- stream idea, target segments, user needs, features, timelines, and metric impact are updated where facts require it
- the high-level product vision is reconstructable before reading detailed feature descriptions
- current progress is separated from future roadmap
- backlog changes are connected to plan / fact evidence, customer or operational learning, or validated hypotheses
- roadmap stages are linked to user value / capabilities and output metrics
- Tech peer alignment, dependencies, owners, and readiness checks are reflected where relevant

`PARTIAL` when the roadmap is directionally coherent but learning-to-backlog linkage, dependency status, or resource readiness is incomplete.

`FAIL` when the backlog is mainly a feature inventory or the roadmap continues a prior plan despite missed commitments, unresolved dependencies, or unreflected learning.

Look for:

- no explanation of what changed versus previous SR
- detailed product vision without a clear helicopter view of the stream's product bet, target segment, and value mechanism
- roadmap faster than dependency readiness allows
- features not tied to user need or metric impact
- Tech peer alignment missing where roadmap feasibility depends on it

### 4. Success Criteria, Metrics, And Next SR Commitments

Review whether current success criteria and next SR commitments are measurable enough for accountability.

`PASS` when:

- success criteria are explicit for each decision-critical issue or roadmap item
- thresholds exist where the document claims validation or plan closure
- actual results are compared with thresholds
- a limited set of decision-driving input metrics is identified and tied to the product vision
- input metrics explain output metrics
- FAQ 8 defines next SR date, commitments, hypotheses, owners, thresholds, and go / no-go rules

`PARTIAL` when metrics are measurable but only partially tied to the stream decision, product vision, or next SR accountability.

`FAIL` when success criteria measure activity, roadmap completion, or operational readiness while the document claims product value, business impact, or plan closure.

Look for:

- validation claims without thresholds
- too many traction drivers or input metrics without a small set of levers the team will actually manage next period
- input metrics that are measurable but not clearly connected to the product vision or output metric
- plan statements counted as evidence
- next SR commitments too vague to be checked later
- no escalation trigger when deviation is material

### 5. Traction, Finance, And Resource Credibility

Review whether the updated stream impact and finance case are credible after current-period facts.

`PASS` when:

- planned traction can be reconstructed from input metrics, output metrics, baselines, horizons, formulas, and drivers
- the traction model separates the few decision-driving input metrics from supporting diagnostics or appendix detail
- current plan / fact, Traction YTD deviation, traffic-light color, Analytics semaphore, InvCo / FBP validation, and Vertical support are reflected in the decision logic
- financial summary, Increment / ToBe case, cost allocation, Kismet triggers, and resources are consistent with the approved stream scope
- changed planned values use `metric / previous plan / current plan / reason for change`

`PARTIAL` when the model is directionally plausible but important drivers, deltas, validations, or resource assumptions remain incomplete.

`FAIL` when the traction / finance case is internally inconsistent, materially wider than plan / fact evidence, or hides weak incremental economics behind a positive total case.

Look for:

- unexplained step-changes in adoption, revenue, GMV, margin, costs, HC, support load, or output metrics
- large traction tables that do not identify the limited input drivers behind next-period impact
- yellow / red validation signals absent from the main narrative
- cost allocation not linked to future impact or 3Sigma
- resource ask not connected to next-period commitments

### 6. Risks, Validations, And Approval Carry-Forward

Review whether risks and cross-functional approvals make the next stream period safe.

`PASS` when:

- killer assumptions and traffic-light concerns are explicit
- yellow / red lines are explained in FAQ 6 and main decision logic
- FAQ 7 approvals are refreshed when material context changed, or skipped only when the template's skip condition is satisfied
- T&S, support, moderation, marketing, billing, tax, legal, accounting, finance, HR, strategy, pricing, Tech, vertical, and domain-owner comments are reflected where relevant
- mitigations are controls or committed actions with owners, not only awareness statements

`PARTIAL` when risks are visible but controls, owners, approval caveats, or decision consequences are incomplete.

`FAIL` when unresolved legal, operational, financial, technical, or stakeholder constraints materially affect the next-period approval but are not integrated into the stream decision.

Look for:

- approval dates without caveats or conditions
- old approvals reused despite changed context, expenses, costs, product decisions, or business decisions
- external dependencies not classified
- mitigations that only restate the risk
- no scenario where the traction, roadmap, or stream thesis stops holding

### 7. Consistency And Evidence Proportionality

Review whether the full 2+ SR story is coherent:

```text
product vision -> limited input drivers -> current plan / fact -> learning -> next-period commitments
previous SR -> commitments -> plan / fact -> learning -> backlog -> roadmap -> metrics -> traction -> resources -> risks -> next SR
```

`PASS` when the stream-control spine and the full SR chain can be restored without major inference and the IC ask is aligned with the proof boundary.

`PARTIAL` when the story is mostly coherent but has weakly linked or fragmented pieces.

`FAIL` when different sections defend different stream scopes, plan / fact conclusions, resource needs, economics, readiness levels, or next SR commitments.

Look for:

- detailed local answers without a compact, committee-readable helicopter view
- executive summary more confident than FAQ 3, FAQ 6, FAQ 7, finance, or validation comments
- product vision, input metrics, and next-period work describing different theories of impact
- plan / fact evidence narrower than requested approval
- roadmap not aligned with traction model, resources, or traffic-light concerns
- next SR commitments not connected to remaining hypotheses and current deviations

## Layer 2: 2+ Stream Review Atomic Checks

Layer 2 is the closed-world diagnostic pass. Answer every atomic question as `YES`, `PARTIAL`, or `NO`, then aggregate back to Atomic checks block statuses using the common verdict policy.

Use 2+ SR duplicate-family keys when useful: `previous-sr-continuity`, `plan-fact-reconciliation`, `commitment-closure`, `backlog-learning-link`, `roadmap-readiness`, `traction-delta`, `traffic-light-reflection`, `finance-resource-fit`, `approval-carry-forward`, `next-sr-conditions`, `cadence-justification`, `scope-proof-boundary`, `stream-control-spine`, `driver-focus`, `vision-metric-coupling`, and `plan-fact-memory`.

### 1. Previous SR Continuity And Current Decision Boundary

- Are previous SR commitments, expected results, owners, and dates explicitly stated or reconstructable?
- Can the current-period summary be connected to the previous SR and the next-period ask as one concise stream-control story?
- Is the current IC request clear: new request, additional request, no request, or financial monitoring?
- Does the document separate what can be approved now from what remains future evidence?
- Are changes since the previous SR justified by facts rather than narrative reframing?
- Is the next review cadence clear: quarterly or semiannual?
- If semiannual cadence is proposed, does the document show low-risk status and no material deviation?
- If the current ask is broader than previous scope, is the approval boundary explicit?

### 2. Plan-Fact Results And Commitment Closure

- Are all decision-critical previous SR commitments tracked as delivered, partially delivered, missed, or changed?
- Are plan and fact shown for the target input and output metrics of the current period?
- Does the plan / fact view preserve continuity of metrics and work from the previous SR into the next SR plan?
- Are deviation calculations, periods, baselines, and thresholds clear enough to verify the traffic-light color?
- Are missed or changed commitments explained with specific decision-relevant reasons?
- Are deviations reflected in backlog, roadmap, traction, resources, risks, or next SR commitments?
- Are current progress claims separated from future roadmap commitments?
- Are author conclusions consistent with actual plan / fact results?

### 3. Product Learning, Backlog, And Roadmap Update

- Is it clear what changed in stream idea, target segments, user needs, features, or value proposition since the previous SR?
- Can the reviewer reconstruct the high-level product vision before reading detailed feature-level plans?
- Is each material backlog change tied to plan / fact evidence, customer learning, operational learning, or validated hypotheses?
- Does each central roadmap item identify user segment, need, feature, timeline, and impact on metrics?
- Is the 1+ year roadmap focused on user value and capabilities delivered, not just feature inventory?
- Is current progress by the moment explicitly separated from future roadmap?
- Does the roadmap sequence follow dependency readiness rather than only target dates?
- Are Tech peer alignment, owners, resources, and readiness checks shown where relevant?
- Are unresolved dependencies classified as solved, in progress, planned, contingent, or outside team control?

### 4. Success Criteria, Metrics, And Next SR Commitments

- Is each success criterion measurable and tied to the actual stream decision question?
- Do success criteria prove the stated user pain, product value, or business impact rather than only activity or delivery progress?
- Is there an explicit threshold where the document claims validation or plan closure?
- When a threshold exists, do actual results meet it?
- Are planning statements, scope declarations, and roadmap commitments kept separate from validation?
- Are input metrics, output metrics, baselines, horizons, and plan / fact reconciled?
- Does the document identify a limited set of key input metrics or drivers the team will manage next period?
- Are the chosen input metrics explicitly connected to the product vision and output metric?
- Does FAQ 8 define next SR date, commitments, hypotheses to validate, owners, thresholds, and go / no-go criteria?
- Are monitoring triggers or escalation rules defined when deviation or risk is material?

### 5. Traction, Finance, And Resources

- Can expected impact be reconstructed from concrete drivers and evidence rather than topline assertion?
- Do important model rows reconcile with formulas, baselines, driver decomposition, scenario rows, and horizons?
- Does the traction model explain why the selected input drivers, not the full metric catalog, are the levers for next-period impact?
- Are current-period plan / fact values and Traction YTD deviation reconciled with the traffic-light color?
- Does the document apply 2+ SR thresholds: Green <=10%, Yellow:10%-20%, Red > 20%?
- Are Analytics semaphore, InvCo / FBP validation, Tech solution validation, and Vertical support conclusions reflected in the main narrative?
- If traffic-light lines are yellow or red, are details, comments, links, and decision consequences provided in FAQ 6 and the main case?
- If planned values changed since the previous IC or previous SR, are previous value, current value, and reason for change provided?
- Does cost allocation across Verticals follow future impact and match the 3Sigma card where relevant?
- Are financial summary, Increment / ToBe case, Kismet triggers, and resources consistent with the approved stream scope?
- Is the resource ask tied to next-period commitments and delivery capacity?
- Is the financial case resilient to downside scenarios already visible in the document?

### 6. Risks, Validations, And Approval Carry-Forward

- Are killer assumptions explicit, and are validated assumptions separated from remaining hypotheses?
- Are yellow or red traffic-light concerns reflected in FAQ 6 and the main approval logic?
- Do mitigations control the risk rather than merely acknowledge it?
- Are owners, dates, and committed actions present for material risk mitigations?
- Are FAQ 7 approvals refreshed when context, expenses, costs, product decisions, or business decisions changed?
- If FAQ 7 is skipped, does the document prove previous approvals remain valid under the template skip condition?
- Are alignment / approval comments interpreted, rather than treated as green just because a date exists?
- Are Legal, Tax, Accounting, Billing, Support, Moderation, T&S, Antifraud, Marketing, HR, Strategy, Pricing, Tech peer, Vertical, and domain-owner caveats included where relevant?
- Are external dependencies classified as secured, in progress, contingent, or outside team control?
- Does the document define a scenario in which the traction model, roadmap, or stream thesis stops holding together?

### 7. Consistency And Evidence Proportionality

- Can the reviewer restore a continuous chain of `previous SR -> commitments -> plan / fact -> learning -> backlog -> roadmap -> metrics -> traction -> resources -> risks -> next SR` without major logical jumps?
- Can the reviewer also restore the stream-control spine of `product vision -> limited input drivers -> current plan / fact -> learning -> next-period commitments` without major logical jumps?
- Does the stream problem definition stay stable from FAQ 1 through FAQ 2, traction, finance, and risks?
- Do target, fact, and conclusion stay aligned across sections?
- Do ambition, metrics, roadmap, resources, and risks describe the same stream scope?
- Are supporting-section cautions visible in the main decision narrative rather than ignored?
- Are next SR commitments tied to the remaining hypotheses, current deviations, and weakest proof points?
- Does the document avoid using current-period directional signals as proof for broader scale, PMF, Gate 4 readiness, or baseline transfer unless those claims are explicitly evidenced?

## 2+ Stream Review Adversarial Lenses

Layer 3 should use these as stage-specific pressure prompts in addition to the common adversarial rubric. They are examples, not mandatory labels.

### Plan-Fact Laundering

Check whether missed commitments, underperformance, delayed roadmap items, or changed plan values are reframed as learning without showing the actual plan / fact consequence.

### Plan-Fact Memory Break

Check whether plan / fact from the previous period, changed input metrics, changed roadmap work, and next SR commitments are presented as separate facts rather than one continuous accountability chain.

### Backlog Momentum Bias

Check whether the stream continues the same roadmap or adds features despite facts that should narrow, stop, reprioritize, or revalidate the backlog.

### Traffic-Light Insulation

Check whether yellow / red analytics, traction, finance, tech, or vertical signals are parked in traffic-light sections but do not change the approval request, resources, or next SR conditions.

### Approval Carry-Forward Risk

Check whether previous approvals are reused despite material changes in context, expenses, costs, product decisions, business decisions, roadmap, risk profile, or cost allocation.

### Cadence Gaming

Check whether the document asks for a semiannual review cycle while deviations, unresolved dependencies, or high-risk assumptions call for quarterly review or closer monitoring.

### Resource-First Continuation

Check whether the document asks for additional resources, HC, budget, or cross-functional capacity before current plan / fact closure and next-period commitments justify that ask.

### Next SR Ambiguity

Check whether the document avoids concrete next SR commitments, thresholds, owners, go / no-go rules, or failure scenarios, leaving the next committee unable to judge whether this SR's commitments were met.

## Final 2+ Stream Review Verdict Calibration

Use the shared verdict policy, then apply these 2+ SR-specific checks.

Assign `APPROVE` only when:

- the 2+ SR document is complete
- previous SR commitments are reconstructable
- plan / fact results support the requested approval scope
- the stream-control spine is reconstructable: product vision, focused input drivers, current plan / fact, learning, and next-period commitments fit together
- deviations and changed planned values are evidence-backed and reflected in backlog, traction, resources, risks, and next SR conditions
- input metrics are focused enough for next-period management and explicitly connected to the product vision and output metric
- traction, finance, resources, and traffic lights are internally consistent
- approval carry-forward is valid or refreshed where material context changed
- next SR commitments and cadence are concrete enough for accountability
- no blocker-grade contradiction or unresolved foundational dependency remains

Assign `NEED_EVIDENCE` when:

- the stream remains directionally viable
- the requested approval scope can be narrowed safely
- one or two proof points remain open, such as plan / fact reconciliation, driver focus, vision-metric coupling, traffic-light explanation, resource support, approval carry-forward, or next SR conditions
- the missing evidence is concrete and plausibly obtainable before the next SR or before additional resources are consumed

Assign `REJECT` when:

- previous SR commitments were materially missed or rewritten without evidence
- plan / fact results do not support the requested continuation, resources, or financial monitoring
- the document cannot connect product vision, input drivers, plan / fact results, and next-period commitments well enough to define what continuation means
- traction or financial case is structurally unsupported or contradicts current-period facts
- roadmap depends on unresolved foundational blockers
- cross-functional, legal, finance, support, or technical constraints make the requested next-period approval unsafe
- next SR commitments are too vague to make the next review accountable
