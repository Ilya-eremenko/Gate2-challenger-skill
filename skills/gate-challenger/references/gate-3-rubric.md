# Gate 3 Rubric

## Purpose

Use this rubric after the coordinator determines that the input is a Gate 3 / SR 2 initiative defense document.

Gate 3 answers a different decision question from Gate 2:

```text
Did the team prove, with production / MLP evidence, customer feedback, traction deltas,
and delivery readiness, that the initiative should continue toward scale, PMF validation,
Gate 4, and eventual baseline transfer?
```

This rubric is stage-specific. It should be combined with the shared evidence standard, consistency rules, verdict policy, output contract, synthesis contract, and adversarial review rules that are common to all gates.

Do not duplicate common checks here unless Gate 3 changes the decision test.

## Gate 3 Decision Boundary

Before scoring dimensions, identify exactly what the document asks the committee to approve:

- continuation of discovery / MLP learning
- additional investment or resources
- scaling to new segments, cohorts, categories, regions, platforms, or traffic share
- financial monitoring without new approval
- PMF recognition or partial PMF recognition
- Gate 4 readiness path
- transition toward baseline status

Approval must be scoped. `APPROVE` does not automatically mean full scale, PMF reached, Gate 4 ready, or baseline transfer approved.

The final synthesis should explicitly separate:

- `approved_scope`: what is safe to approve now
- `not_approved_scope`: what remains unproven or out of scope
- `gate_4_conditions`: evidence, milestones, and go / no-go rules required before Gate 4 or baseline transfer

## Gate 3 Internal Artifacts

Build these artifacts internally before Layer 1, Layer 2, and Layer 3 verdicting.

### 1. Gate 2 Commitment Ledger

For every Gate 2 / SR 1 commitment, capture:

- original commitment
- owner, expected date, and expected result / threshold
- MLP scope connected to the commitment
- delivered / partially delivered / missed / changed
- actual production or production-equivalent result
- reason for miss or change
- whether the change is justified by new evidence or only narrative reframing
- decision consequence for Gate 3

Hard rule:

- A changed commitment is not a weakness by itself. It becomes a weakness when the change is not explained by evidence, when the miss hides a decision-critical proof gap, or when the document still asks for scale as if the commitment was closed.

### 2. Production Evidence Ledger

For each central claim based on the MLP or launch, capture:

- launch environment: production / production-equivalent / pilot / fake-door / survey / other
- launch date, duration, rollout size, segment, cohort, category, region, platform, and traffic share
- user behavior observed
- target behavior required by the scaling request
- metric result, threshold, and conclusion
- whether evidence comes from the same behavior and segment that the scaling request relies on

Hard rule:

- Production launch existence is not proof of PMF, scale readiness, or baseline transfer by itself.

### 3. Customer Experience Ledger

For each meaningful customer signal, capture:

- signal type: Contact Rate, CSAT, CES, NPS, survey, interview, support feedback, complaint, churn / cancellation reason, app review, sales feedback, or other
- customer segment and journey stage
- sample size, period, and collection method when available
- positive signal, negative signal, and unresolved pain
- linked product fix or operational fix
- owner, timeline, status, and observed post-fix effect
- whether the signal proves the original pain was reduced or only shows general satisfaction / intent

Hard rule:

- Customer quotes, surveys, CSAT, and NPS are supporting evidence. They are not decisive proof for scale, retention, monetization, or PMF unless connected to observed behavior and thresholds.

### 4. Scale Readiness Map

For each scaling step, capture:

- scale unit: segment, cohort, geography, category, vertical, platform, traffic share, partner group, or all users
- prerequisite capabilities
- product, tech, analytics, support, billing, moderation, T&S, antifraud, legal, tax, accounting, finance, marketing, pricing, HR, strategy, and vertical readiness where relevant
- status: solved / in progress / planned / outside team control
- Tech peer alignment status
- go / no-go checkpoint
- funded-scope status
- consequence if the prerequisite fails

Hard rule:

- Roadmap stages and dates do not prove scaling readiness. Unresolved foundational prerequisites must be treated as gating constraints.

### 5. Traction And Financial Delta Ledger

For each material business or financial change since Gate 2, capture:

- metric or financial line
- Gate 2 plan
- current plan
- actual production result where available
- reason for change
- evidence type behind the change
- impact on Increment and ToBe cases
- impact on cost allocation, HC, support scenario, and Kismet triggers
- whether the model distinguishes validated assumptions, directional evidence, expert assumptions, and open hypotheses

Hard rules:

- The model must be checked against observed product behavior, rollout timing, adoption lag, support ramp-up, and unresolved dependencies.
- Positive ToBe economics cannot hide weak or negative incremental economics.
- Support scenario assumptions must be reconciled with scale, customer experience, support load, and cost allocation.

### 6. Validation Traffic Light Ledger

Capture:

- Analytics semaphore and validation comments
- Traction YTD deviation using Gate 3 thresholds: Green <= 10%, Yellow 10%-30%, Red > 30%
- InvCo / FBP validation
- Vertical support for horizontal cases
- links required by yellow / red signals
- whether yellow / red signals are reflected in the main decision narrative

Hard rule:

- A green traffic light is not proof by itself. A yellow or red signal must be explained in the main approval logic, not buried in a table.

## Layer 1: Gate 3 Decision-Critical Dimensions

Layer 1 is the broad decision narrative review. Assign each dimension `PASS`, `PARTIAL`, or `FAIL`.

For each dimension:

- output up to 3 decision-relevant issues
- prefer one broad issue per root cause
- cite concrete source sections, values, dates, thresholds, traffic lights, commitments, and contradictions
- write human-facing issue explanations in Russian by default

### 1. Gate 2 Continuity And Gate 3 Decision Boundary

Review whether the document preserves a reliable chain from Gate 2 to Gate 3.

`PASS` when:

- Gate 2 product idea, problem, solution, USP, strategic fit, goals, commitments, hypotheses, success criteria, and expected MLP outcomes are reconstructable
- the Gate 3 ask is explicit
- continuation, scale, PMF, Gate 4, and baseline transfer are not blurred
- changes since Gate 2 are explained by evidence

`PARTIAL` when the chain is mostly recoverable but fragmented, or the ask is clear while some boundary conditions are implied.

`FAIL` when the reviewer cannot determine what was promised at Gate 2, what was proven by Gate 3, or what exactly is being approved now.

Look for:

- Gate 2 commitments rewritten without evidence
- PMF or scale language stronger than the MLP evidence allows
- hidden approval of a broader product, segment, risk profile, or economics than the document proves
- press release or executive-summary drift versus Gate 2 appendices

### 2. MLP Launch Fact Base And Progress Against Gate 2 Commitments

Review whether the MLP was actually launched and whether Gate 2 commitments were closed.

`PASS` when:

- launch date, environment, scope, rollout population, cohorts, regions, categories, platforms, traffic share, and segments are clear where decision-relevant
- every Gate 2 commitment is tracked as delivered, partially delivered, missed, or changed
- actual results are compared with expected outcomes or thresholds
- author conclusions match the facts

`PARTIAL` when launch happened and evidence is directionally useful, but scope, comparison to thresholds, or commitment tracking is incomplete.

`FAIL` when launch evidence is missing, not production-equivalent for the claims being made, or materially narrower than the requested scale.

Look for:

- fake-door, survey, or optional-flow evidence used as if it proved production scale
- limited cohort results stretched to all segments
- missed commitments described as neutral future work
- no clear actual-vs-threshold comparison

### 3. Production Performance And Metric Quality

Review whether production behavior supports the product and business claims.

`PASS` when:

- key user journeys have production funnel metrics
- behavioral metrics are shown where relevant: adoption, conversion, retention, repeat usage, frequency, liquidity, cancellation, churn, supply, demand, approval rate, fraud rate, support load, or other relevant metrics
- output metrics, input metrics, proxy metrics, and counter-metrics are defined and connected to the impact mechanism
- metrics show whether the original user pain was reduced

`PARTIAL` when metrics are useful but mostly directional, incomplete for key journeys, or only partially tied to the original pain.

`FAIL` when the metrics do not test the behavior required by the Gate 3 ask.

Look for:

- funnel health treated as proof that the user pain is solved
- output growth without input driver evidence
- counter-metrics missing from a risk-bearing rollout
- negative signals excluded from the decision narrative
- observed first use used as proof of retention or repeat behavior

### 4. Customer Experience And Feedback Closure

Review whether customer experience evidence is decision-ready.

`PASS` when:

- Contact Rate, CSAT / CES, NPS, survey, support, and qualitative feedback are shown where relevant
- feedback is tied to segments, journeys, and time periods
- negative feedback is quantified and included in the main decision logic
- major feedback themes are linked to product or operational fixes with owners, dates, status, and observed post-fix impact

`PARTIAL` when feedback is present but weakly tied to fixes, segments, or the original pain.

`FAIL` when customer experience is absent, selectively positive, disconnected from product fixes, or contradicted by support / churn / cancellation signals.

Look for:

- customer feedback presented only as quotes or anecdotes
- no connection between feedback and roadmap changes
- support or complaint burden ignored in scale readiness
- satisfaction metrics used as PMF proof without behavior, retention, or threshold support

### 5. Post-MLP Solution Learning, Adjustments, And New Hypotheses

Review whether the team learned from MLP facts and updated the solution honestly.

`PASS` when:

- the document identifies what worked, what did not work, and why
- post-MLP segment -> pain -> solution -> metric linkage is explicit
- MLP, scaling version, target-state product, and out-of-scope areas are separated
- new hypotheses have validation method, threshold, timeline, and owner
- the impact mechanism from fixes / scaling steps to input and output metrics is explicit

`PARTIAL` when learning is plausible but incomplete, or new hypotheses lack some validation mechanics.

`FAIL` when the document converts MLP evidence into readiness for a materially different target product without proof.

Look for:

- feature list replacing learning synthesis
- MLP evidence used to support a different behavior, segment, or risk profile
- future validation described as current proof
- no owner or threshold for new hypotheses

### 6. Scaling Roadmap, PMF Criteria, Gate 4 Path, And Baseline Transition

Review whether the next 1-2 years, PMF criteria, and Gate 4 path are decision-ready.

`PASS` when:

- scaling goals and rollout logic are clear by segment, cohort, category, geography, platform, traffic share, or another relevant unit
- roadmap stages are framed as user value / capabilities delivered, not only features
- each stage has expected metric impact and go / no-go checks
- PMF status is explicit: reached, partially reached, or expected later
- PMF criteria, validation milestones, dates, and thresholds are explicit
- next deep dive before Gate 4 is defined where relevant
- Gate 4 success criteria and expected date are clear
- baseline transfer depends on discovery completion, ownership, monitoring, support, and financial readiness

`PARTIAL` when the roadmap is directionally useful but PMF, Gate 4, or baseline-transfer rules are incomplete.

`FAIL` when scale is requested without decision-ready PMF criteria, dependency readiness, or Gate 4 / baseline conditions.

Look for:

- scale approval blurred with PMF proof
- roadmap faster than dependencies
- no Tech peer alignment for the roadmap
- unresolved prerequisites treated as generic risks
- baseline transition claimed before operating model and monitoring are clear

### 7. Traction, Support Scenario, And Financial Delta Since Gate 2

Review whether the updated business case is credible after launch.

`PASS` when:

- traction and financial model are explicitly compared with Gate 2
- changes use the format `metric / previous plan / current plan / reason for change`
- changes are grounded in MLP facts, production metrics, customer feedback, or clearly labeled assumptions
- expected impact can be reconstructed from input drivers, rollout timing, adoption lag, and learning period
- support scenario is included and reconciled with scale, customer experience, support load, HC, and costs
- Increment and ToBe cases are separated
- revenue attribution and BRF / TRF / LTM treatment are clear where relevant
- Kismet triggers and approval scope are consistent with the IC request

`PARTIAL` when the model is directionally coherent but key deltas, support assumptions, or downside scenarios are incomplete.

`FAIL` when the model relies on unsupported step-changes, hides incremental economics, ignores visible risks, or contradicts rollout readiness.

Look for:

- sharp jumps in adoption, conversion, retention, take rate, supply, GMV, revenue, margin, costs, or support load without validated drivers
- positive ToBe masking weak Increment
- cost allocation not matching future impact or 3Sigma card
- yellow / red Traction YTD deviation not reflected in the decision logic
- finance summary inconsistent with traction, roadmap, resources, or risks

### 8. IC Request, Validations, Cross-Functional And GTM Readiness

Review whether the requested decision is operationally and organizationally safe.

`PASS` when:

- IC request is clear: new request, additional request, no request, or financial monitoring
- resources, cost allocation, ownership, and cross-functional work match the roadmap
- approvals and caveats from Analytics, InvCo / FBP, Verticals, Legal, Tax, Accounting, Billing, Support, Moderation, T&S, Antifraud, Marketing, HR, Strategy, Pricing, Tech peer, and affected domains are reflected where relevant
- prior approvals are reused only when the document proves there were no material changes in context, expenses, costs, product decisions, or business decisions
- mitigations are actual controls, not only awareness or future discovery

`PARTIAL` when readiness is plausible but some approvals, owners, costs, or controls remain incomplete.

`FAIL` when unresolved cross-functional constraints are decision-relevant but absent from the main approval logic.

Look for:

- formal `approved` status with caveats hidden in comments
- horizontal vertical support missing for impact, cost allocation, or UX
- dependencies outside team control treated as solved
- resources insufficient for the next roadmap stage
- GTM risks described without control or owner

### 9. Consistency And Evidence Proportionality

Review whether the document's facts and conclusions stay aligned.

`PASS` when the reviewer can restore a continuous chain:

```text
Gate 2 commitments -> MLP launch -> production facts -> customer feedback ->
insights -> product changes -> roadmap -> PMF / Gate 4 -> traction ->
finance -> resources -> risks -> approval scope
```

`PARTIAL` when the chain is mostly recoverable but some important claims are only directional or fragmented.

`FAIL` when the document systematically overclaims relative to the evidence, or when main narrative, appendices, traffic lights, finance summary, analyst validation, and cross-functional reviews contradict each other.

Look for:

- supporting sections more cautious than the executive summary
- actual facts, thresholds, and conclusions misaligned
- MLP facts supporting only a narrow scope while the ask implies broad scale
- traction promise exceeding roadmap and rollout timing
- PMF or baseline transfer claimed from evidence that supports only continued discovery

## Layer 2: Gate 3 Atomic Checks

Layer 2 is the detailed diagnostic pass. Answer each atomic check as `YES`, `PARTIAL`, or `NO`, then aggregate back to the block status.

Use shared duplicate-family consolidation. Suggested Gate 3 duplicate-family keys:

- `gate3-boundary`
- `commitment-delta`
- `production-scope`
- `mlp-to-scale-leap`
- `customer-feedback-closure`
- `pmf-overclaim`
- `gate4-readiness`
- `baseline-transfer`
- `support-scenario`
- `financial-delta`
- `traffic-light-reconciliation`
- `approval-carry-forward`
- `vertical-support`

### 1. Gate 2 Continuity And Gate 3 Decision Boundary

- Is the original product idea, problem, solution, USP, goals, strategic fit, and key output metrics clearly summarized?
- Are Gate 2 / SR 1 commitments, hypotheses, success criteria, and expected MLP outcomes explicitly stated?
- Is the Gate 3 / SR 2 decision request clear?
- Does the document separate continuation, scale approval, PMF validation, Gate 4 readiness, and baseline transfer?
- Are press release and executive-summary changes since Gate 2 explained by evidence?
- Are changes since Gate 2 justified by new facts rather than narrative reframing?

### 2. MLP Launch Fact Base And Commitments

- Was the MLP launched in production or production-equivalent environment?
- Are MLP scope, launch date, duration, rollout population, traffic share, segments, regions, categories, cohorts, or platforms clear where relevant?
- Are all Gate 2 commitments tracked as delivered / partially delivered / missed / changed?
- Are missed or changed commitments explained with specific decision-relevant reasons?
- Are actual results compared with Gate 2 expected outcomes or thresholds?
- Are author conclusions consistent with the actual facts?
- Is the evidence from the same segment and behavior that the scaling request relies on?

### 3. Production Performance And Metric Quality

- Are production funnel metrics shown for key user journeys?
- Are behavioral metrics reported where applicable: adoption, conversion, retention, repeat usage, frequency, liquidity, cancellation, churn, approval quality, fraud, or support load?
- Are output metrics, input metrics, proxy metrics, and counter-metrics defined and connected to the product logic?
- Do metrics show that the original user pain was reduced?
- Are negative signals included in the decision narrative?
- Are metric definitions, baselines, horizons, thresholds, and toplines reconciled?
- Does the document avoid treating first-use, optional, or proxy behavior as proof of scaled or mandatory behavior?

### 4. Customer Experience And Feedback Closure

- Are Contact Rate, CSAT / CES, NPS, survey results, support feedback, and qualitative feedback shown where relevant?
- Are feedback signals tied to specific segments, cohorts, journeys, or production periods?
- Are sample size, period, and collection method clear enough for the claim strength?
- Are negative feedback themes quantified and reflected in the decision logic?
- Is each major feedback theme linked to a fix, owner, timeline, current status, and observed post-fix effect?
- Does feedback prove reduction of the original pain, or only general satisfaction / intent?
- Are support load, complaints, churn, cancellations, or unresolved customer pain reflected in scale readiness?

### 5. Post-MLP Solution Learning, Adjustments, And New Hypotheses

- Is there a clear segment -> pain -> solution -> metric linkage after MLP launch?
- Did the team identify which parts of the solution worked, which did not, and why?
- Are MLP version, scaling version, target-state product, and out-of-scope areas separated?
- Are new hypotheses explicitly formulated?
- Does each new hypothesis have a validation method, success threshold, timeline, and owner?
- Does the document avoid using MLP evidence to overclaim readiness for a materially different target-state product?
- Is the impact mechanism explicit: how proposed fixes or scaling steps change input metrics and then output metrics?

### 6. Scaling Roadmap, PMF, Gate 4, And Baseline Transition

- Are scaling goals for the next 1-2 years clearly described?
- Is rollout logic clear by segment, cohort, geography, category, platform, traffic share, or another relevant unit?
- Is the roadmap focused on user value and capabilities delivered, not just feature lists?
- Does each roadmap stage explain expected metric impact?
- Is roadmap alignment with Tech peer stated where relevant?
- Are PMF criteria explicitly defined?
- Is PMF status clear: reached, partially reached, or expected later?
- Are PMF milestones, target dates, thresholds, and go / no-go rules clear?
- Are Gate 4 expectations, success criteria, and expected date defined?
- Is the next deep dive before Gate 4 defined where relevant?
- Are baseline-transfer conditions explicit?
- Does the roadmap distinguish prerequisites for next test, prerequisites for scaling, and later optimizations?

### 7. Traction, Support Scenario, And Financial Delta

- Is the updated traction model compared with Gate 2 / SR 1 model?
- Are changed planned values shown as `metric / previous plan / current plan / reason for change`?
- Are changes driven by MLP evidence, production metrics, customer feedback, or clearly labeled assumptions?
- Can expected impact be reconstructed from observed input metrics and roadmap levers?
- Are sharp jumps in adoption, conversion, retention, take rate, supply, GMV, revenue, margin, costs, or support load explained by validated drivers?
- Does the model account for learning period, adoption lag, rollout constraints, and operational ramp-up?
- Does the model distinguish validated assumptions, directional evidence, expert assumptions, and open hypotheses?
- Is support scenario provided and reconciled with scale, support capacity, HC, costs, and customer experience?
- Are downside scenarios and break conditions defined?
- Are Increment and ToBe economics separated and consistent?
- Is revenue attribution explicit: direct, A/B test, analytical allocation, or not trackable / zero?
- Is treatment in BRF / TRF / LTM clear?
- Are Kismet triggers checked and consistent with the IC request?
- Is financial summary consistent with traction, resources, cost allocation, and rollout plan?

### 8. IC Request, Validations, Cross-Functional And GTM Readiness

- Is the IC request clear: new request, additional request, no request, or financial monitoring?
- Are requested resources, cost allocation, ownership, and cross-functional capacity consistent with the roadmap?
- Are Analytics semaphore, Traction YTD deviation, InvCo / FBP validation, and Vertical support shown where relevant?
- Is Traction YTD deviation calculated using Gate 3 thresholds: Green <= 10%, Yellow 10%-30%, Red > 30%?
- Are yellow / red traffic lights explained in the main decision narrative?
- For horizontal cases, do Verticals confirm impact estimates, cost allocation, and UX acceptability?
- If prior approvals are reused, does the document prove no material changes in context, expenses, costs, product decisions, or business decisions?
- Are Legal, Tax, Accounting, Billing, Support, Moderation, T&S, Antifraud, Marketing, HR, Strategy, Pricing, Tech peer, and affected domain caveats included where relevant?
- Are unresolved cross-functional risks decision-relevant constraints rather than generic risks?
- Are mitigations actual controls rather than awareness or future discovery?
- Can the team deliver the next roadmap stage with the resources and dependencies described?

### 9. Consistency And Evidence Proportionality

- Can the full Gate 3 chain be restored without major logical jumps?
- Do problem statement, post-MLP solution, target segments, and roadmap stay aligned?
- Do MLP facts support the claimed scaling ambition?
- Do success criteria, customer feedback, and traction match the described impact mechanism?
- Does traction promise more than roadmap, rollout timing, support scenario, and dependencies can realistically deliver?
- Are main narrative, appendices, traffic lights, analyst validation, finance summary, and cross-functional reviews consistent?
- When supporting sections are more cautious than the executive summary, is that tension reflected in the final decision logic?
- Are actual facts, thresholds, and conclusions aligned?
- Is PMF, Gate 4 readiness, or baseline transfer claimed only at the strength supported by evidence?

## Layer 3: Gate 3 Adversarial Lenses

Layer 3 should use the shared adversarial output shape, but add these Gate 3-specific lenses.

### MLP Evidence Laundering

Check whether a narrow MLP, optional behavior, survey, fake-door, small cohort, or early production signal is converted into a broad scale, PMF, baseline, or financial approval claim.

### Ask Versus Proven Scope

Check whether the IC ask approves a broader product boundary, segment, category, cost base, risk profile, or economic model than the evidence proves.

### PMF Overclaiming

Check whether PMF is claimed from early adoption, satisfaction, or operational metrics without retention, repeat behavior, willingness-to-pay, supply / demand quality, or other product-specific PMF criteria.

### Gate 4 And Baseline Trap

Check whether the document implies a path to baseline transfer while ownership, support, monitoring, finance treatment, and operating model remain unproven.

### Support Scenario Realism

Check whether support load, moderation, billing, disputes, refunds, cancellations, antifraud, T&S, and operational incident response are scaled in the model and resourced in the roadmap.

### Increment Versus ToBe Masking

Check whether positive ToBe economics, existing business baseline, cumulative cash flow, or allocated revenue hides weak incremental economics or unresolved attribution.

### Validation Traffic Light Suppression

Check whether yellow / red analytics, traction, finance, or vertical-support signals are acknowledged in tables but absent from the decision narrative.

### Approval Carry-Forward Risk

Check whether approvals from prior gates are reused despite material changes in context, expenses, product decisions, business decisions, roadmap, risk profile, or cost allocation.

### Scale Readiness Compound Risk

Check whether multiple individually manageable risks become unsafe together: weak CX plus support ramp-up, rollout speed plus tech dependency, financial target plus adoption lag, or legal / billing caveat plus category expansion.

## Final Gate 3 Verdict Calibration

Use the shared verdict policy, then apply these Gate 3-specific checks.

Assign `APPROVE` only when:

- the Gate 3 document is complete
- the Gate 2 commitment chain is reconstructable
- production / MLP evidence supports the requested approval scope
- customer experience evidence is sufficient for the requested scale
- traction and financial deltas are evidence-backed and internally consistent
- support scenario and cross-functional readiness match the roadmap
- PMF, Gate 4, and baseline-transfer claims are scoped to evidence
- no blocker-grade contradiction or unresolved foundational dependency remains

Assign `NEED_EVIDENCE` when:

- the initiative remains directionally viable
- the requested approval scope can be narrowed safely
- one or two proof points remain open, such as customer feedback closure, PMF thresholds, scale readiness, support scenario, traffic-light reconciliation, or financial delta support
- the missing evidence is concrete and plausibly obtainable before scale, Gate 4, or baseline transfer

Assign `REJECT` when:

- the MLP / production evidence does not support the core continuation or scale thesis
- Gate 2 commitments were materially missed or rewritten without evidence
- PMF, Gate 4, or baseline transfer is claimed without proof
- traction or financial case is structurally unsupported or contradicts production facts
- roadmap depends on unresolved foundational blockers
- cross-functional, legal, finance, support, or GTM constraints make the requested approval unsafe
