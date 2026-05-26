---
name: gate2-challenger
description: Use when reviewing a Gate 2 initiative defense document, product defense memo, or approval package and you need a fast approval decision with blocker-focused reasoning instead of reading the full document line by line.
---

# Gate2-challenger

## Overview

Review a Gate 2 defense document in four passes:

0. Coordinator: input normalization and preflight
1. Layer 1 worker: decision-critical block review
2. Layer 2 worker: atomic weak-link review
3. Synthesizer: blocker-first final verdict

Core principle: make the decision from logic and evidence, not from document polish.

## Execution model

The four passes are separate responsibilities, not one blended review.

- The main agent acts as Coordinator and Synthesizer.
- Layer 1 worker and Layer 2 worker are independent evaluation tasks that must receive the same normalized Markdown, canonical block taxonomy, and evidence standard.
- When subagent tools are available and runtime policy allows agent delegation, run Layer 1 worker and Layer 2 worker as separate parallel subagents by default.
- If runtime policy requires explicit user permission for subagents, ask once before review: `Run Layer 1 and Layer 2 as parallel subagents?`
- If subagents are unavailable or forbidden, execute the same Layer 1 and Layer 2 worker responsibilities locally, keep their artifacts separate, and state that local fallback was used.
- Do not let Layer 1 read Layer 2 output, or Layer 2 read Layer 1 output. Only the Synthesizer reads both artifacts.

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

- review a Gate 2 product defense
- decide approve / reject / need evidence
- assess initiative defense quality quickly
- find only the blockers in a strategy or defense document
- evaluate whether Gate 1 hypotheses are reflected and confirmed

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

Before dispatching Layer 1 and Layer 2, the coordinator must verify whether the user likely provided a full Gate 2 document rather than a fragment.

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

Before starting a review, verify that the local `gate2-challenger` git checkout is up to date with its upstream.

- Run `python3 scripts/check_git_freshness.py` when this skill package is inside the canonical git checkout.
- If the installed skill is a copied package and not itself inside git, run `python3 scripts/check_git_freshness.py --repo /path/to/Gate2-challenger` from this package, or ask the user for the canonical checkout path.
- The check must confirm that the git checkout is up to date with its upstream and that `skills/gate2-challenger` has no local modifications.
- Do not start Layer 1 or Layer 2 until this preflight passes.
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
- pass the same normalized Markdown to both Layer 1 and Layer 2
- use one canonical block taxonomy across all stages
- use one evidence standard across all stages
- before any verdicting, build four mandatory internal reasoning artifacts:
  - `Hypothesis ledger`: hypothesis, why it matters, validation method, expected result / threshold, actual observed result, author conclusion, reviewer conclusion, status
  - `Evidence ladder`: classify central claims as hard evidence, experiment / pilot result, operational signal, customer feedback / survey / CSAT, benchmark / competitor reference, or narrative assumption
  - `Dependency map`: milestone, prerequisites, status of each prerequisite, control, funded-scope status, blocker severity
  - `Consistency matrix`: cross-check problem, segment, solution, validation, metrics, traction, roadmap, blockers, and legal / ops / risk constraints
- when converting internal artifacts into Layer 1 and Layer 2 output:
  - `Hypothesis ledger` must flag planning statements labeled as validation
  - `Evidence ladder` must preserve evidence-type proportionality, especially when surveys, CSAT, quotes, or benchmarks support central business claims
  - `Dependency map` must distinguish owner, funded scope, implemented control, and contingent external dependency
  - `Consistency matrix` must include problem-definition drift and metric/topline reconciliation
  - `Consistency matrix` must also include confidence mismatch between main narrative confidence and supporting-section confidence
- treat appendix and supporting sections as valid sources for any of the four internal artifacts
- keep these artifacts internal; they guide reasoning but are not printed in `standard`

### Step 1: Run Layer 1 worker

Read [layer-1-rubric.md](references/layer-1-rubric.md) and evaluate the top-level blocks.

Important:

- the Gate 1 hypotheses presence check is part of Layer 1
- do not require an explicitly titled Gate 1 section if the hypothesis chain is reconstructable elsewhere
- Layer 1 dimension statuses are `PASS`, `PARTIAL`, or `FAIL`
- if a Layer 1 dimension status is `PASS`, output only non-blocking residual issues, or one `No material issue` record when there is no meaningful weakness
- Layer 1 returns only `layer_1`
- Layer 1 does not compute a final verdict
- Layer 1 does not write a free-form summary
- Layer 1 may raise a novel cross-sectional blocker when the document-level logic breaks in a way that is not captured by any single Layer 2 atomic check

### Step 2: Run Layer 2 worker

Read [layer-2-rubric.md](references/layer-2-rubric.md) and evaluate the atomic questions.

Then aggregate the Layer 2 atomic results back into Atomic checks block statuses.

Before writing the Layer 2 output, assign a duplicate-family key before writing Layer 2 output for every non-`YES` atomic answer. Use stable semantic keys such as `dependency-readiness`, `proxy-validation`, `monetization-contradiction`, `cancellation-boundary`, `threshold-mismatch`, `model-reconstructability`, `segment-path-mixing`, and `risk-control-maturity`. Select the strongest representative issue per family inside each Atomic checks block; later atomic checks in the same family should reference that selected family in evidence instead of creating another standalone issue unless the local consequence is materially different.

This family selection is mandatory: selected issue families are a pre-output control, not an optional writing style. Only the selected representative atomic answer gets full standalone issue text. Non-selected repeated atomic answers must use `same duplicate family; see <family>` and do not add a second local-angle issue sentence for the same family.

Important:

- Layer 2 returns only `layer_2`
- Layer 2 Atomic checks block statuses are `PASS`, `PARTIAL`, or `FAIL`
- Layer 2 atomic answers are `YES`, `PARTIAL`, or `NO`
- Layer 2 does not compute a final verdict
- Layer 2 does not write a free-form summary
- the Atomic checks block status embedded in the `layer_2` heading is the Layer 2 aggregate for that block

### Step 3: Run synthesizer

Read [verdict-policy.md](references/verdict-policy.md) and [synthesis-contract.md](references/synthesis-contract.md).

The synthesizer must:

- read `layer_1` and `layer_2` as structured intermediate artifacts
- preserve raw Layer 1 dimension statuses and Layer 2 Atomic checks block statuses as diagnostic outputs
- deduplicate overlapping issues before writing final blockers
- analyze meaningful differences between the two layers
- use `merged_block_assessment` to explain how broad Layer 1 judgment and detailed Layer 2 evidence fit together
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
6. merge Layer 1 and Layer 2 block interpretations using the synthesis contract
7. synthesize the final verdict from the raw layer verdicts
8. promote only blocker-grade merged issues to the final summary

### Step 4: Format the response

Read [output-contract.md](references/output-contract.md) and follow it exactly.

Formatting rules:

- `standard` / `summary` mode: output the investment-committee style narrative summary first, then ask whether the user wants the short blocker/evidence version
- if the user says yes to the short blocker/evidence version, show the structured final synthesis and then ask whether the user wants the full layer-by-layer analysis
- if the user says yes to the full analysis, show the `extended` / `detailed` output using the existing layer artifacts when available
- `extended` / `detailed` mode: output final synthesis, then normalized Layer 1, then normalized Layer 2, then merged block assessment
- `debug stages=on`: make Layer 1 and Layer 2 sections explicit even when the user asked for a compact answer

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
