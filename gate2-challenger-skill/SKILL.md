---
name: gate2-challenger
description: Use when reviewing a Gate 2 initiative defense document, product defense memo, or approval package and you need a fast approval decision with blocker-focused reasoning instead of reading the full document line by line.
---

# Gate2-challenger

## Overview

Review a Gate 2 defense document in four passes:

0. Input normalization: if the input is a PDF file, convert it to Markdown first
1. Layer 1: decision-critical block review
2. Layer 2: atomic question review
3. Final synthesis: blocker-first verdict

Core principle: make the decision from logic and evidence, not from document polish.

## Required evaluation rules

Apply these rules in every review:

- Do not reward the document for having section headers without actual logic.
- Prefer logical consistency over surface completeness.
- Penalize contradictions across problems, solutions, roadmap, metrics, and traction.
- Distinguish between validated evidence and narrative assumptions.

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

1. output mode: `summary` or `detailed`
2. debug stages: `on` or `off` (default `off`)

Default language for the response is Russian.

## Preflight: document completeness

Before Layer 1, verify that the user likely provided a full Gate 2 document rather than a fragment.

Signals that the input may be incomplete:

- only one or two sections are present
- the text looks like an excerpt, screenshot transcription, or copied fragment
- key parts of a Gate 2 defense are structurally missing
- the document has local claims, but there is no surrounding decision context

Behavior:

- if the input is clearly incomplete, prefer refusing a full final verdict and ask for the complete document
- if the user explicitly wants a fragment review anyway, allow a provisional assessment only
- in fragment mode, do not present the verdict as full-document grade
- in fragment mode, force `confidence: LOW`
- explicitly say that the result is partial and limited by incomplete input

## Workflow

### Step 0: Normalize the input

If the input is a PDF file:

- run `python3 scripts/pdf_to_md_docling.py <path-to-pdf>`
- use the produced Markdown file from `../review-documents/` as the review input
- analyze the Markdown content, not the original PDF

If `docling` is not installed or the conversion script cannot import it:

- do not continue with a partial PDF review
- tell the user that PDF-to-Markdown conversion requires `docling`
- offer the user to install `docling`, then resume the review after conversion

If the input is already a Markdown file:

- read and analyze the Markdown file directly

If the input is pasted text:

- analyze the pasted text directly

### Step 1: Run Layer 1

Read [layer-1-rubric.md](references/layer-1-rubric.md) and evaluate the top-level blocks.

Important:

- the Gate 1 hypotheses presence check is part of Layer 1
- if the document does not contain an explicit Gate 1 hypotheses block, that Layer 1 block must be `REJECT`
- if a Layer 1 block verdict is `APPROVE`, do not output issues for that block

### Step 2: Run Layer 2

Read [layer-2-rubric.md](references/layer-2-rubric.md) and evaluate the atomic questions.

Then aggregate the Layer 2 atomic results back into dimension-block verdicts.

### Step 3: Apply verdict policy

Read [verdict-policy.md](references/verdict-policy.md).

Use it in this order:

1. assign block verdicts in Layer 1
2. aggregate Layer 1 to a layer verdict
3. assign atomic results in Layer 2
4. aggregate Layer 2 atomic results to block verdicts
5. aggregate Layer 2 to a layer verdict
6. synthesize the final verdict

### Step 4: Format the response

Read [output-contract.md](references/output-contract.md) and follow it exactly.

Formatting rules:

- `summary` mode: output only final synthesis
- `detailed` mode: output final synthesis, then Layer 1, then Layer 2
- `debug stages=on`: make Layer 1 and Layer 2 sections explicit even when the user asked for a compact answer

## Review discipline

When evidence is weak:

- do not silently fill gaps with assumptions
- do not infer validation where the document only makes claims
- downgrade to `NEED_EVIDENCE` or `REJECT` based on the verdict policy

When the final verdict is `APPROVE`:

- still include critical non-blocking improvements in the final synthesis
- keep them clearly separate from blockers

## Anti-patterns

Never do the following:

- do not invent causes beyond the data in the document
- do not treat the presence of numbers as proof that the model is credible
- do not treat a roadmap as proof that delivery is realistic
- do not treat phrases like `we checked`, `on track`, or `done` as evidence without method, results, and conclusion
- do not output `APPROVE` only because every block contains some answer
- do not retell the document section by section instead of evaluating it
