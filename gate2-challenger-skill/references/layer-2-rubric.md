# Layer 2 Rubric

Layer 2 is the closed-world, detailed diagnostic pass.

Layer 2 is atomic and diagnostic.

For each atomic question:

- reason internally as `PASS`, `PARTIAL`, or `FAIL`
- answer externally as `YES` or `NO`
- provide evidence
- if `NO`, provide a short issue statement

Mapping rule:

- `PASS` -> `YES`
- `PARTIAL` -> `NO`
- `FAIL` -> `NO`

For every atomic question, the reasoning must answer three things even if the output remains compact:

1. what exactly is being checked
2. what evidence the conclusion depends on
3. what decision-relevant consequence follows from `PASS`, `PARTIAL`, or `FAIL`

Layer 2 is not meant to enumerate every imaginable risk in the document. Its role is to provide repeatable, evidence-rich detail for explicit weak links and to refine or challenge Layer 1 through that evidence rather than replace Layer 1 on style alone.

Global rules:

- Treat appendix, FAQ, legal, compliance, analytics comments, support tables, and operating notes as first-class evidence.
- Do not require a specific section title when the needed logic is provable elsewhere.
- Do not reward a familiar section title when the logic under it is weak.
- Future tests or planned work do not count as present proof for the current gate.

## 1. Problem framing and significance

- Can the reviewer identify the target segment, pain, and intended behavior change without restoring missing logic by inference?
- Can the core Gate 2 decision thesis be traced back to the decision-critical Gate 1 hypotheses?
- For each decision-critical hypothesis, are the expected result, actual result, and conclusion aligned?
- Is evidence from one segment, one use case, or one flow being stretched to justify a different segment, use case, or flow?

## 2. Solution quality and logic

- Does each central hypothesis use a validation method that actually answers the decision question?
- If a claim concerns mandatory or scaled behavior, is the evidence drawn from that same behavior rather than from an optional or opt-in proxy?
- Is the causal mechanism from solution elements to metric movement explicit rather than implied?
- Is the current flow / CJM / key user path clear enough to judge adoption or conversion claims when those claims are central?

## 3. Scope of work and implementation plan

- Does each major milestone have explicit prerequisites rather than only a target date?
- Are unresolved foundational dependencies treated as decision-relevant weaknesses rather than as neutral future work?
- Are key prerequisites already solved, in progress, only planned, or outside team control, and is that status reflected honestly in the roadmap?
- Are rollout checkpoints tied to operational, legal, compliance, tooling, integration, or abuse-readiness constraints where those constraints matter?

## 4. Success criteria and metrics

- Is each claimed success criterion measurable and tied to the actual decision question?
- Is there an explicit threshold where the document claims validation rather than observation?
- When a threshold exists, do the actual observed results meet it?
- Are output claims supported by input or proxy metrics that plausibly explain how the result was achieved?
- Are the success criteria strong enough for the stated end-state ambition?

## 5. Traction model credibility

- Can the expected impact be reconstructed from concrete drivers and evidence rather than from topline assertion?
- Are horizons, adoption lag, and learning periods consistent with the roadmap and rollout plan?
- Does the model rely on aggressive step-changes, unsupported baselines, or assumptions outside funded scope?
- Is the evidence behind the model directional or definitive, and does the document keep the conclusion at the same strength level?

## 6. Key assumptions and risks completeness

- Are the killer assumptions explicit, and are validated assumptions separated from remaining hypotheses?
- Do mitigations control the risk, rather than merely acknowledge it?
- Do supporting sections surface unresolved legal, compliance, abuse, operational, or integration constraints that materially affect rollout readiness?
- Does the document define a scenario in which the model or rollout thesis stops holding together?

## 7. Consistency

- Can the reviewer restore a continuous chain of `segment -> pain -> hypotheses -> solution -> roadmap -> metrics -> impact` without major logical jumps?
- Do target, fact, and conclusion stay aligned across sections?
- Do ambition, metrics, roadmap, traction, and risks describe the same end-state, or do they pull in different directions?
- When supporting sections and main narrative disagree, is the disagreement visible in the decision logic rather than ignored?

## Aggregation reminder

Layer 2 block aggregation unit is the whole dimension bundle, not the individual atomic question.

Do not count atomic failures directly as final blockers without first aggregating them back into the block verdict.
