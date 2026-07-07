---
name: gate-challenger
description: Use when reviewing a Gate 2, 1st Stream Review, 2+ Stream Review, or Gate 3 initiative defense document, product defense memo, investment committee package, or approval package and you need a fast stage-aware approval decision with blocker-focused reasoning.
---

# Gate Challenger

## Overview

Review a Gate 2, 1st Stream Review, 2+ Stream Review, or Gate 3 defense document in six passes:

0. Coordinator: input normalization and preflight
1. Stage detector: determine `document_stage: GATE_2 | STREAM_REVIEW_1 | STREAM_REVIEW_2_PLUS | GATE_3 | UNKNOWN | FRAGMENT`
2. Layer 1 worker: stage-specific decision-critical block review
3. Layer 2 worker: stage-specific atomic weak-link review
4. Layer 3 worker: adversarial business and committee-risk review using common and stage-specific lenses
5. Synthesizer: blocker-first final verdict with approval scope

Core principle: make the decision from logic and evidence, not from document polish.

## Execution model

The five passes are separate responsibilities, not one blended review.

- The main agent acts as Coordinator and Synthesizer.
- Layer 1 worker, Layer 2 worker, and Layer 3 worker are independent evaluation tasks that must receive the same normalized Markdown, canonical block taxonomy, and evidence standard.
- When subagent tools are available and runtime policy allows agent delegation, run Layer 1 worker, Layer 2 worker, and Layer 3 worker as separate parallel subagents by default.
- If runtime policy requires explicit user permission for subagents, ask once before review: `Run Layer 1, Layer 2, and Layer 3 as parallel subagents?`
- If subagents are unavailable or forbidden, execute the same Layer 1, Layer 2, and Layer 3 worker responsibilities locally, keep their artifacts separate, and state that local fallback was used.
- Do not let Layer 1 read Layer 2 or Layer 3 output, Layer 2 read Layer 1 or Layer 3 output, or Layer 3 read Layer 1 or Layer 2 output. Layer 3 must not read Layer 1 or Layer 2 output. Only the Synthesizer reads all three artifacts.

## Required evaluation rules

Apply these rules in every review:

- Do not reward the document for having section headers without actual logic.
- Prefer logical consistency over surface completeness.
- Penalize contradictions across problems, hypotheses, solutions, roadmap, metrics, traction, and risks.
- Distinguish between validated evidence and narrative assumptions.
- Do not silently reconstruct missing proof in favor of the document.
- Numbers, targets, and roadmap dates are not proof by themselves.
- Supporting sections such as appendix, FAQ, legal, compliance, risk, analytics comments, operating notes, and support tables are first-class evidence.
- The absence of a specific heading is not a problem if the needed logic is demonstrated elsewhere.
- The presence of familiar headings is not a strength if the logic under them is weak.

## Anti-overfitting guardrails

Use any calibration example only for failure-mode discovery.

- Do not optimize the review toward a single sample document.
- Do not hardcode blocker patterns taken from one example.
- Do not require specific names, figures, appendix structures, section labels, or threshold styles.
- Do not assume strong documents must share the same outline.
- Evaluate general principles: evidence quality, validation-method fitness, dependency completeness, consistency, and risk completeness.

## When to use

Use this skill when the user asks for any of the following:

- review a Gate 2, 1st Stream Review, 2+ Stream Review, or Gate 3 product defense
- decide approve / reject / need evidence
- assess initiative defense quality quickly
- find only the blockers in a strategy or defense document
- evaluate whether prior gate hypotheses, commitments, and success criteria are reflected and confirmed
- determine whether plan / fact results, production / MLP evidence, or stream commitments support continuation, scaling, PMF claims, Gate 4 readiness, next SR commitments, or baseline transfer

Do not use it for:

- editing or rewriting the defense document
- comparing multiple separate files line by line
- reviewing Gate 1 documents directly

## Input contract

This skill can work with:

- pasted text
- a Markdown file
- a PDF file that must be converted to Markdown first

Before starting, collect two settings from the user if they were not already provided:

1. review mode: `standard` or `extended`
2. debug stages: `on` or `off` (default `off`)

Mode mapping:

- `standard` -> `summary`
- `extended` -> `detailed`

Default language for the response is Russian.

Language rule for all user-visible analysis:

- Human-facing explanatory fields must be written in Russian by default.
- This applies to `reason`, `suggestion`, `issue`, `evidence`, `merged_interpretation`, and `why_difference`.
- Do not write mixed-language sentences such as `approval unsafe`, `proof gap`, `decision-ready`, or `blocker-grade` when a natural Russian phrase is available.
- English is allowed only for schema keys, status values, canonical block names, metric names, section titles, product names, duplicate-family keys, and exact source quotes.
- Use Russian explanations for duplicate-family labels: write the label only after a Russian sentence that explains the problem.

Common analysis wording replacements:

- `readiness` -> `готовность`
- `approval boundary` -> `граница текущего решения`
- `fakedoor` -> `фейкдор-тест` or `имитационный вход`
- `target solution` -> `целевая версия решения`
- `blockers` -> `блокирующие проблемы`
- `scaled rollout` -> `масштабный запуск`
- If an English term is a source quote or metric name, keep it in `evidence` but explain its meaning in Russian in the surrounding sentence.
- Do not write full explanatory sentences in English inside human-facing fields.
- Before returning the answer, scan `reason`, `issue`, `evidence`, `merged_interpretation`, and `why_difference` and rewrite any English explanatory sentence into Russian.
- Questions may remain in English when they are canonical atomic checks, but their `issue` explanations must be Russian.

## Preflight: document completeness

Before dispatching Layer 1, Layer 2, and Layer 3, the coordinator must verify whether the user likely provided a full gate defense document rather than a fragment.

Signals that the input may be incomplete:

- only one or two sections are present
- the text looks like an excerpt, screenshot transcription, or copied fragment
- key parts of the `problem -> hypotheses -> solution -> roadmap -> metrics -> evidence -> risks` chain are structurally missing
- the document has local claims, but there is no surrounding decision context

Behavior:

- if the input is clearly incomplete, prefer refusing a full final verdict and ask for the complete document
- if the user explicitly wants a fragment review anyway, allow a provisional assessment only
- in fragment mode, do not present the verdict as full-document grade
- in fragment mode, force `confidence: LOW`
- if the core decision chain is missing, do not upgrade the fragment to a full-strength gate decision
- if key logic is only implied, do not build it on the author's behalf
- explicitly say that the result is partial and limited by incomplete input

## Workflow

### Step 0: Coordinator normalization and preflight

#### Version freshness preflight

Before starting a review, verify that the local `gate-challenger` git checkout is up to date with its upstream.

- Run `python3 scripts/check_git_freshness.py` when this skill package is inside the canonical git checkout.
- If the installed skill is a copied package and not itself inside git, run `python3 scripts/check_git_freshness.py --repo /path/to/Gate2-challenger` from this package, or ask the user for the canonical checkout path.
- The check must confirm that the git checkout is up to date with its upstream and that `skills/gate-challenger` has no local modifications.
- Do not start Layer 1 or Layer 2 until this preflight passes; the same preflight also blocks Layer 3.
- If the check cannot run because git, network fetch, or the canonical checkout is unavailable, stop and tell the user what must be updated. Continue only if the user explicitly says this is a local fallback or intentional benchmark run.

If the user did not explicitly specify the review mode:

- ask which mode to use: `standard` or `extended`
- treat `standard` as `summary`
- treat `extended` as `detailed`

If the input is a PDF file:

- run `python3 scripts/pdf_to_md_docling.py <path-to-pdf>`
- use the produced Markdown file from `review-documents/` next to the source PDF as the review input
- analyze the Markdown content, not the original PDF

If `docling` is not installed or the conversion script cannot import it:

- do not continue with a partial PDF review
- tell the user that PDF-to-Markdown conversion requires `docling`
- offer the user to install `docling`, then resume the review after conversion

If the input is already a Markdown file:

- read and analyze the Markdown file directly

If the input is pasted text:

- analyze the pasted text directly

Coordinator requirements:

- normalize the input exactly once
- determine `full document` vs `fragment` exactly once
- Read [stage-detection.md](references/stage-detection.md) and determine the stage exactly once before loading a stage-specific rubric
- emit this internal routing record before any layer work:
  - `document_stage: GATE_2 | STREAM_REVIEW_1 | STREAM_REVIEW_2_PLUS | GATE_3 | UNKNOWN | FRAGMENT`
  - `stage_confidence: HIGH | MEDIUM | LOW`
  - `stage_evidence`
  - `stage_conflicts`
  - `routing_decision: gate_2_rubric | stream_review_1_rubric | stream_review_2_plus_rubric | gate_3_rubric | ask_user | fragment_review`
- Do not start Layer 1, Layer 2, or Layer 3 until the stage is detected
- if routing is ambiguous, ask the user whether to run Gate 2, 1st Stream Review, 2+ Stream Review, or Gate 3 rubric instead of guessing
- Context loading discipline:
  - Do not read, preload, summarize, or skim any stage-specific rubric before the routing record is complete
  - After routing, read exactly one selected stage-specific rubric
  - Do not open the other stage rubrics for examples, calibration, duplicate-family keys, or adversarial lenses
  - Layer 3 uses the common adversarial rubric plus the same selected stage-specific rubric only
- load exactly one stage-specific rubric after routing:
  - Gate 2 -> [gate-2-rubric.md](references/gate-2-rubric.md)
  - 1st Stream Review -> [stream-review-1-rubric.md](references/stream-review-1-rubric.md)
  - 2+ Stream Review -> [stream-review-2-plus-rubric.md](references/stream-review-2-plus-rubric.md)
  - Gate 3 -> [gate-3-rubric.md](references/gate-3-rubric.md)
- pass the same normalized Markdown and same stage routing record to Layer 1, Layer 2, and Layer 3
- use one canonical block taxonomy from the selected stage rubric
- use one evidence standard across all stages
- before any verdicting, build four mandatory internal reasoning artifacts:
  - `Hypothesis ledger`: hypothesis, why it matters, validation method, expected result / threshold, actual observed result, author conclusion, reviewer conclusion, status
  - `Evidence ladder`: classify central claims as hard evidence, experiment / pilot result, operational signal, customer feedback / survey / CSAT, benchmark / competitor reference, or narrative assumption
  - `Dependency map`: milestone, prerequisites, status of each prerequisite, control, funded-scope status, blocker severity
  - `Consistency matrix`: cross-check problem, segment, solution, validation, metrics, traction, roadmap, blockers, and legal / ops / risk constraints
- when converting internal artifacts into Layer 1, Layer 2, and Layer 3 output:
  - `Hypothesis ledger` must flag planning statements labeled as validation
  - `Evidence ladder` must preserve evidence-type proportionality, especially when surveys, CSAT, quotes, or benchmarks support central business claims
  - `Dependency map` must distinguish owner, funded scope, implemented control, and contingent external dependency
  - `Consistency matrix` must include problem-definition drift and metric/topline reconciliation
  - `Consistency matrix` must also include confidence mismatch between main narrative confidence and supporting-section confidence
- treat appendix and supporting sections as valid sources for any of the four internal artifacts
- keep these artifacts internal; they guide reasoning but are not printed in `standard`

### Step 1: Run Layer 1 worker

Read the selected stage-specific rubric and evaluate the top-level Layer 1 blocks.
Do not open any other stage-specific rubric during Layer 1.

Important:

- for Gate 2, the Gate 1 hypotheses presence check is part of Layer 1
- for 1st Stream Review, the discovery results and validated product ideas chain is part of Layer 1
- for 2+ Stream Review, previous SR commitments, plan / fact results, backlog updates, traction deltas, and next SR commitments are part of Layer 1
- for Gate 3, the Gate 2 commitment and MLP progress chain is part of Layer 1
- do not require an explicitly titled prior-gate section if the hypothesis / commitment chain is reconstructable elsewhere
- Layer 1 dimension statuses are `PASS`, `PARTIAL`, or `FAIL`
- if a Layer 1 dimension status is `PASS`, output only non-blocking residual issues, or one `No material issue` record when there is no meaningful weakness
- Layer 1 returns only `layer_1`
- Layer 1 does not compute a final verdict
- Layer 1 does not write a free-form summary
- Layer 1 may raise a novel cross-sectional blocker when the document-level logic breaks in a way that is not captured by any single Layer 2 atomic check

### Step 2: Run Layer 2 worker

Read the selected stage-specific rubric and evaluate the Layer 2 atomic questions.
Do not open any other stage-specific rubric during Layer 2.

Then aggregate the Layer 2 atomic results back into Atomic checks block statuses.

Before writing the Layer 2 output, assign a duplicate-family key before writing Layer 2 output for every non-`YES` atomic answer. Use stable semantic keys such as `dependency-readiness`, `proxy-validation`, `monetization-contradiction`, `cancellation-boundary`, `threshold-mismatch`, `model-reconstructability`, `segment-path-mixing`, and `risk-control-maturity`. If the selected stage rubric defines stage-specific duplicate-family keys, use only the keys from that selected rubric; do not open another stage rubric to borrow keys. Select the strongest representative issue per family inside each Atomic checks block; later atomic checks in the same family should reference that selected family in evidence instead of creating another standalone issue unless the local consequence is materially different.

This family selection is mandatory: selected issue families are a pre-output control, not an optional writing style. Only the selected representative atomic answer gets full standalone issue text. Non-selected repeated atomic answers must use `same duplicate family; see <family>` and do not add a second local-angle issue sentence for the same family.

Important:

- Layer 2 returns only `layer_2`
- Layer 2 Atomic checks block statuses are `PASS`, `PARTIAL`, or `FAIL`
- Layer 2 atomic answers are `YES`, `PARTIAL`, or `NO`
- Layer 2 does not compute a final verdict
- Layer 2 does not write a free-form summary
- the Atomic checks block status embedded in the `layer_2` heading is the Layer 2 aggregate for that block

### Step 3: Run Layer 3 worker

Read [common-adversarial-rubric.md](references/common-adversarial-rubric.md) and evaluate adversarial business, financial, governance, incentive, operating-model, and committee-risk weak spots.
Then use only the adversarial lenses from the same selected stage-specific rubric already chosen by the routing record, if that selected rubric includes them. Do not open any other stage-specific rubric during Layer 3.

Important:

- Layer 3 returns only `layer_3`
- Layer 3 must not read Layer 1 or Layer 2 output
- Layer 3 is prompt-first and uses its lenses as examples, not as mandatory checklist rows
- Layer 3 does not compute the final verdict
- Layer 3 does not repeat Layer 1 or Layer 2 unless the adversarial lens changes the approval consequence
- Layer 3 findings are promotable only when they are backed by concrete document evidence and explain why the concern changes what can be safely approved now

### Step 4: Run synthesizer

Read [common-verdict-policy.md](references/common-verdict-policy.md) and [common-synthesis-contract.md](references/common-synthesis-contract.md).

The synthesizer must:

- read `layer_1`, `layer_2`, and `layer_3` as structured intermediate artifacts
- preserve raw Layer 1 dimension statuses and Layer 2 Atomic checks block statuses as diagnostic outputs
- treat raw Layer 3 findings as diagnostic outputs, not as automatic final blockers
- deduplicate overlapping issues before writing final blockers
- analyze meaningful differences between the three layers
- use `merged_block_assessment` to explain how broad Layer 1 judgment and detailed Layer 2 evidence fit together
- add Layer 3 findings only when they are novel, evidence-backed, and change the safe approval boundary
- prefer supporting sections over optimistic narrative when they materially disagree
- preserve a confidence mismatch when supporting sections are materially more cautious than the main narrative
- promote only blocker-grade `HIGH` issues and clearly decision-relevant `MEDIUM` issues to the final blockers list
- avoid re-reviewing the document from scratch when the needed evidence already exists in the layer artifacts

Use it in this order:

1. assign dimension statuses in Layer 1
2. aggregate Layer 1 to a layer verdict
3. assign atomic results in Layer 2
4. aggregate Layer 2 atomic results to Atomic checks block statuses
5. aggregate Layer 2 to a layer verdict
6. run Layer 3 adversarial review and return `layer_3`
7. merge Layer 1, Layer 2, and Layer 3 interpretations using the synthesis contract
8. synthesize the final verdict from the raw layer verdicts and promotable Layer 3 findings
9. promote only blocker-grade merged issues and evidence-backed `novel_from_l3` findings to the final summary

### Step 5: Format the response

Read [common-output-contract.md](references/common-output-contract.md) and follow it exactly.

Formatting rules:

- `standard` / `summary` mode: output the investment-committee style narrative summary first, then ask whether the user wants the short blocker/evidence version
- if the user says yes to the short blocker/evidence version, show the structured final synthesis and then ask whether the user wants the full layer-by-layer analysis
- if the user says yes to the full analysis, show the `extended` / `detailed` output using the existing layer artifacts when available
- `extended` / `detailed` mode: output final synthesis, then normalized Layer 1, then normalized Layer 2, then normalized Layer 3, then merged block assessment
- `debug stages=on`: make Layer 1, Layer 2, and Layer 3 sections explicit even when the user asked for a compact answer

## Review discipline

When evidence is weak:

- do not silently fill gaps with assumptions
- do not infer validation where the document only makes claims
- do not treat future tests or planned validation as proof for the current gate
- if target, fact, and conclusion do not align, downgrade consistency and evidence strength
- downgrade to `NEED_EVIDENCE` or `REJECT` based on the verdict policy

When the final verdict is `APPROVE`:

- still include critical non-blocking improvements in the final synthesis
- keep them clearly separate from blockers

## Anti-patterns

Never do the following:

- do not invent causes beyond the data in the document
- do not treat the presence of numbers as proof that the model is credible
- do not treat a roadmap as proof that delivery is realistic
- do not treat phrases like `we checked`, `on track`, `done`, `validated`, or `confirmed` as evidence without method, threshold, result, and conclusion
- do not count customer quotes, survey sentiment, CSAT, or benchmark references as decisive proof for central business claims on their own
- do not let evidence from an optional flow prove a different mandatory-flow thesis
- do not output `APPROVE` only because every block contains some answer
- do not retell the document section by section instead of evaluating it
