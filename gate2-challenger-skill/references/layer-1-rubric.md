# Layer 1 Rubric

Layer 1 is the broad, open-world review of the document as a decision narrative.

Layer 1 is block-level only. No atomic questions in the output.

For each block:

- assign `APPROVE`, `NEED_EVIDENCE`, or `REJECT`
- identify whether the block is a blocker
- output up to 3 decision-relevant issues
- prefer block-level, chain-level, and consistency-level issues over checklist-style detail
- Layer 1 may raise a cross-sectional issue even when it does not map cleanly to one Layer 2 atomic question
- Layer 1 should not duplicate Layer 2 atomic detail
- if block verdict = `APPROVE`, do not output `top_issues`

## Blocks

### 1. Problem framing and significance

Review:

- what the initiative is trying to solve
- why the problem matters
- whether the target segments are clear
- whether business / product impact is explained
- whether the document fits Avito strategy
- whether Gate 1 hypotheses are explicitly traceable and confirmed

Decision rule:

- do not require a separate section titled around Gate 1 hypotheses
- `APPROVE` when the document clearly lets you reconstruct `Gate 1 hypothesis -> expected result -> fact -> conclusion`
- `NEED_EVIDENCE` when the Gate 1 hypotheses can be reconstructed, but they are fragmented, partially incomplete, or the conclusions are weakly supported
- `REJECT` when the document does not let you reliably reconstruct what was being validated since Gate 1, or when the stated status of hypotheses materially contradicts the facts shown

Look for:

- missing or vague problem statement
- mixed segments or mixed pains with no clear logic
- no explicit statement of what changed since Gate 1
- Gate 1 hypotheses mentioned only as narrative, without a reliable `hypothesis -> result -> conclusion` chain

### 2. Solution quality and logic

Review:

- whether the solution addresses the stated pain for the stated segments
- whether there is a clear segment -> pain -> solution linkage
- whether the impact mechanism is understandable

Look for:

- features listed without causal logic
- multiple unrelated use cases collapsed into one story
- solution disconnected from the validated hypotheses

### 3. Scope of work and implementation plan

Review:

- whether MLP, end state, and out-of-scope areas are clear
- whether the roadmap is credible
- whether rollout logic is explicit
- whether risks and mitigations are reflected in the plan

Look for:

- gray zones in scope
- roadmap promises with no sequencing logic
- rollout not connected to validation or control points

### 4. Success criteria and metrics

Review:

- whether success metrics are explicit
- whether metrics map to the problem and solution
- whether the mechanism from solution to input metrics to output metrics is credible

Look for:

- metrics with no causal story
- business metrics that do not match the initiative
- outputs named without input drivers

### 5. Traction model credibility

Review:

- whether expected impact can be reconstructed
- whether the team can realistically influence the drivers
- whether the model matches scope, rollout, and learning lag

Look for:

- unexplained jumps
- traction beyond roadmap capacity
- assumptions used in the model but absent from scope

### 6. Key assumptions and risks completeness

Review:

- whether critical assumptions are named
- whether validated assumptions are separated from hypotheses
- whether the document explains what must be tested first

Look for:

- risk register with no prioritization
- assumptions with no source
- no failure scenario for the model

### 7. Consistency

Review:

- whether the full chain stays coherent:
  `segment -> pain -> solution -> roadmap -> metrics -> impact`

Look for:

- changing target segments across sections
- scope conflicting with roadmap
- metrics contradicting the impact story
- traction contradicting rollout timing

## Evidence standard

For every issue, cite concrete evidence:

- direct quotes
- section names
- specific phrases from the document

Do not treat narrative claims as validated evidence unless the document itself provides proof or results.
