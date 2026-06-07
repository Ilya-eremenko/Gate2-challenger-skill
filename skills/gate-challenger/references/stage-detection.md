# Stage Detection

Use this before loading any stage-specific rubric.

Return this internal routing record:

```text
document_stage: GATE_2 | GATE_3 | UNKNOWN | FRAGMENT
stage_confidence: HIGH | MEDIUM | LOW
stage_evidence:
- <section/table/phrase proving the stage>
stage_conflicts:
- <signals that point to another stage, if any>
routing_decision: gate_2_rubric | gate_3_rubric | ask_user | fragment_review
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
- If Gate 2 and Gate 3 signals are both present but the requested decision is unclear, use `routing_decision: ask_user`.
- If stage remains uncertain after normalization, do not guess. Ask the user whether to run Gate 2 or Gate 3 rubric.

## Routing Decision

Use:

- `gate_2_rubric` only when `document_stage: GATE_2`
- `gate_3_rubric` only when `document_stage: GATE_3`
- `fragment_review` when the input is incomplete and a full verdict would be unsafe
- `ask_user` when the document is not fragmentary but the stage remains ambiguous

Do not start Layer 1, Layer 2, or Layer 3 until the stage is detected.
