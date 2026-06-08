# Stage Detection

Use this before loading any stage-specific rubric.

Return this internal routing record:

```text
document_stage: GATE_2 | STREAM_REVIEW_1 | STREAM_REVIEW_2_PLUS | GATE_3 | UNKNOWN | FRAGMENT
stage_confidence: HIGH | MEDIUM | LOW
stage_evidence:
- <section/table/phrase proving the stage>
stage_conflicts:
- <signals that point to another stage, if any>
routing_decision: gate_2_rubric | stream_review_1_rubric | stream_review_2_plus_rubric | gate_3_rubric | ask_user | fragment_review
```

## Gate 2 Signals

Prefer `GATE_2` when the body of the document shows several of these signals:

- title contains `Gate 2`
- current review is Gate 2
- previous review is Gate 1
- FAQ asks for estimated date and success criteria for Gate 3
- document focuses on Gate 1 continuity, planned traction, MLP / end-state scope, initial risks, and Gate 3 commitments
- traction section asks for planned traction and changes compared to the Gate 1 draft traction model
- the decision asks whether the initiative should receive investment to build or validate the MLP

## 1st Stream Review Signals

Prefer `STREAM_REVIEW_1` when the body of the document shows several of these signals:

- title contains `Stream review 1` or `1st Stream Review`
- current review is Current SR or Stream review 1
- previous review is Previous SR, not Gate 1 or Gate 2
- FAQ asks for the overall idea behind the stream
- FAQ asks what specific issues are being solved, the development roadmap, and `progress by the moment`
- FAQ asks for a development roadmap for 1+ year aligned with the Tech peer
- FAQ asks for the success criteria and estimated date for the next SR
- the document focuses on discovery results, validated product ideas, planned traction, resources, roadmap, and IC readiness
- traction section asks for planned traction of the initiative and current plan / fact deviation using Green <=25%, Yellow:25%-50%, Red > 50%
- the decision asks whether discovery has produced enough validated product ideas and evidence to continue the stream toward the next SR

## 2+ Stream Review Signals

Prefer `STREAM_REVIEW_2_PLUS` when the body of the document shows several of these signals:

- title contains `Stream review 2+`, `2nd Stream Review`, or `SR 2+`
- current review is Current SR after a previous stream review
- previous review is Previous SR, not Gate 1 or Gate 2
- FAQ asks for the overall idea behind the stream and updates compared to the previous SR
- FAQ asks what specific issues are being solved, the development roadmap, and `progress by the moment`
- FAQ asks for a development roadmap for 1+ year aligned with the Tech peer
- FAQ asks for planned traction and current plan / fact deviation using Green <=10%, Yellow:10%-20%, Red > 20%
- FAQ asks what concerns should be discussed based on the traffic-light section
- FAQ 7 says approvals may be skipped only when previous approvals remain valid and there are no significant changes in context, expenses, costs, product decisions, or business decisions
- FAQ asks for success criteria and estimated date for the next SR
- the decision asks whether plan / fact results, backlog updates, traction model changes, resource assumptions, and next-period commitments are safe for the next quarterly or semiannual stream iteration

Do not require PMF, Gate 4, baseline transfer, customer-experience ledgers, or production-scale evidence for `STREAM_REVIEW_2_PLUS` unless the document itself claims that scope.

## Gate 3 Signals

Prefer `GATE_3` when the body of the document shows several of these signals:

- title contains `Gate 3`
- current review is Gate 3
- previous review is Gate 2
- FAQ asks about progress on last commitments / MLP
- FAQ asks for scaling goals, PMF criteria, and Gate 4
- FAQ asks about customer experience, Contact Rate, CSAT / CES, NPS, or customer feedback
- Gate 3 traction traffic-light thresholds are present: Green <= 10%, Yellow 10%-30%, Red > 30%
- document asks for the next deep dive before Gate 4
- document asks when discovery will be completed and the product will move to baseline status
- the decision asks whether production / MLP facts justify continuation or scale

Stage separation rule:

- If the title and body point to `Stream review 2+`, prefer `STREAM_REVIEW_2_PLUS` over `GATE_3` when the central ask is plan / fact review, backlog update, traction model update, resources, or next SR commitments.
- Prefer `GATE_3` only when the body asks the Gate 3 question: whether production / MLP facts justify continuation, scale, PMF, Gate 4 readiness, or baseline transfer.
- Template instruction examples mentioning Gate 3 thresholds do not override the current review title, current / previous review table, FAQ wording, or actual traffic-light thresholds.

## Fragment Signals

Prefer `FRAGMENT` when:

- only one or two sections are present
- the text looks like an excerpt, screenshot transcription, or copied fragment
- the core gate chain is structurally missing
- the document contains local claims but no decision context

In fragment mode:

- use `routing_decision: fragment_review`
- force `stage_confidence: LOW` unless the fragment stage is unmistakable
- do not present the verdict as a full-document gate decision

## Unknown Or Ambiguous Stage

Use `UNKNOWN` when the stage cannot be determined safely.

Ambiguity rules:

- If title and body disagree, prefer body evidence and report the conflict.
- If the current review and next-gate FAQ disagree, report the conflict.
- If Gate 2, 1st Stream Review, 2+ Stream Review, and Gate 3 signals overlap but the requested decision is unclear, use `routing_decision: ask_user`.
- If stage remains uncertain after normalization, do not guess. Ask the user whether to run Gate 2, 1st Stream Review, 2+ Stream Review, or Gate 3 rubric.

## Routing Decision

Use:

- `gate_2_rubric` only when `document_stage: GATE_2`
- `stream_review_1_rubric` only when `document_stage: STREAM_REVIEW_1`
- `stream_review_2_plus_rubric` only when `document_stage: STREAM_REVIEW_2_PLUS`
- `gate_3_rubric` only when `document_stage: GATE_3`
- `fragment_review` when the input is incomplete and a full verdict would be unsafe
- `ask_user` when the document is not fragmentary but the stage remains ambiguous

Do not start Layer 1, Layer 2, or Layer 3 until the stage is detected.
