# Output Contract

## Output modes

Accepted user-facing modes:

- `standard`
- `extended`

Internal formatting aliases:

- `standard` -> `summary`
- `extended` -> `detailed`

The skill must also support:

- `debug stages`: `on` or `off`
- default is `off`

Internal reasoning artifacts such as the hypothesis ledger, evidence ladder, dependency map, and consistency matrix remain hidden unless the user explicitly asks for internal reasoning dumps. Their existence must not change the external output schema below.

## Status vocabulary

Final verdicts use:

- `APPROVE`
- `NEED_EVIDENCE`
- `REJECT`

Layer 1 dimensions and Layer 2 Atomic checks blocks use:

- `PASS`
- `PARTIAL`
- `FAIL`

Layer 2 atomic answers use:

- `YES`
- `PARTIAL`
- `NO`

Layer 3 returns `layer_3` with:

- `verdict: APPROVE | NEED_EVIDENCE | REJECT`
- `adversarial_findings`

Issue severity uses:

- `HIGH`
- `MEDIUM`
- `LOW`

## Language policy

Human-facing explanatory fields must be written in Russian by default.

This applies to `reason`, `suggestion`, `issue`, `evidence`, `merged_interpretation`, and `why_difference`.

Rules:

- Do not write mixed-language sentences such as `approval unsafe`, `proof gap`, `decision-ready`, or `blocker-grade` when a natural Russian phrase is available.
- English is allowed only for schema keys, status values, canonical block names, metric names, section titles, product names, duplicate-family keys, and exact source quotes.
- Keep schema keys exactly as specified: `verdict`, `confidence`, `blockers`, `reason`, `evidence`, `issue`, `merged_block_assessment`, and status values remain unchanged.
- Translate explanatory wording: use `решение об одобрении небезопасно` instead of `approval unsafe`, `пробел в доказательствах` instead of `proof gap`, `достаточно для решения` instead of `decision-ready`, and `блокирующая проблема` instead of `blocker-grade`.
- Use Russian explanations for duplicate-family labels: write the label only after a Russian sentence that explains the problem.
- If the source document uses English section names, metric names, product names, or quoted phrases, keep them exactly when needed for evidence.

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

## Summary mode

In `summary` mode, use progressive disclosure by default.

Default `summary` output is a plain executive summary for a top-management reader.

Default `summary` output is an investment-committee style narrative assessment for a top-management reader, not the structured synthesis schema. It should read like a committee member's written opinion: decision first, then the case for that decision, short evidence, and practical recommendations.

### Default investment committee summary format

```text
## Оценка документа

**Рекомендация: <простое решение на русском: одобрить / одобрить ограниченно / запросить доказательства / не одобрять полный план>.**

<2-3 абзаца: восстанови контекст решения простым языком: что документ просит одобрить, какой текущий факт или изменение делает этот запрос нужным, какая логика автора связывает проблему с предлагаемым решением, что уже доказано, и чем текущий запрос шире доказанного base case. Если документ просит одобрить масштабирование, ресурсы, финансовый uplift или новый сценарий, явно отдели это от уже подтвержденного продукта.>

## Почему оценка именно такая

1. **<причина простым управленческим языком>**
<2-4 предложения: что именно не закрыто, почему это важно для решения, что может сломаться, если одобрить сейчас. Если используешь термин из документа, сразу объясни его по-русски.>
Краткие доказательства:
- <FAQ / Appendix / table>: <факт или цифра> -> <что это означает> -> <почему это подтверждает проблему для решения>
- <FAQ / Appendix / table>: <факт или цифра> -> <что это означает> -> <что может быть ошибочно одобрено без дополнительной проверки>

2. **<следующая причина>**
<то же: объяснение + краткие доказательства>

<Обычно 4-6 причин. Не добавляй причину без конкретного доказательства и последствий для решения.>

## Рекомендация инвестиционного комитета

**<Одно предложение: что именно можно одобрить сейчас и что нельзя одобрять без условий.>**

Что можно одобрить сейчас:
- <ограниченный следующий шаг / проверка / пилот / ресурс на валидацию>

Что не стоит одобрять сейчас:
- <полный rollout / полный uplift case / включение в базовый финансовый план без условий>

## Что нужно улучшить в документе

1. **<улучшение>**
<практическое объяснение: что переписать, разделить, пересчитать или доказать>

2. **<улучшение>**
<практическое объяснение>

## Итог

<1 короткий абзац: итоговое управленческое решение и условие возврата на комитет.>

Хотите расширенную версию с блокерами и доказательствами?
```

Rules:

- Write for a top-management reader who does not want to learn evaluation terminology.
- Write as a professional investment committee assessment, not as a rubric report.
- Decision first: the first substantive sentence must say what should be approved, not approved, or approved conditionally.
- Separate the proven base case from the requested new growth / scaling / resource / financial-uplift case whenever the document mixes them.
- In the opening assessment, restore the decision context before listing reasons.
- Decision context means: what the document asks to approve, what changed or what current fact makes the requested decision necessary, the author's causal logic from problem to proposed answer, which part is already proven and which part goes beyond proven evidence.
- Do not hardcode domain-specific recovery, regulation, partner, or pricing questions. Derive the context from the document's own problem statement, facts, trend changes, dependencies, and requested approval.
- Do not use schema keys such as `blockers`, `blocker_id`, `origin`, `severity`, `covered_by_l2`, or `merged_block_assessment`.
- Do not expose canonical block names unless they are translated or explained in plain Russian.
- Do not use English evaluation terms when a natural Russian phrase exists.
- Do not leave opaque English or business shorthand unexplained. If the source uses terms such as `partner readiness`, `pre-scoring`, `credit bureau data`, `antifraud`, `legal approvals`, `uplift`, `rollout`, `base case`, `Scenario 3`, `fee elasticity`, `churn`, `PMF`, `BNPL`, `Classified`, or `go/no-go`, either translate them or explain them immediately in Russian.
- Prefer this pattern for technical terms: `<source term> — <plain Russian explanation>`. Example: `pre-scoring — предварительная оценка пользователя до оформления кредита, которая должна предсказать вероятность одобрения`.
- For every major reason, answer three questions in the text: what exactly is not closed, why it matters for the investment decision, and what could break if the committee approves now.
- Every `Краткие доказательства` bullet must be a proof chain.
- Use this proof-chain shape: `source -> fact -> interpretation -> decision consequence`.
- A proof bullet must not end with only a fact, number, quote, or section reference.
- Each proof bullet must explain why this evidence proves the problem, not merely show that the source contains a related number.
- Use short proof chains under `Краткие доказательства`: cite the section, cite the concrete fact or number, interpret what it means, then explain why the fact matters for the committee decision. Do not cite a section name alone.
- Explain the verdict in business language: what can be approved, what cannot be approved yet, what proof is missing, and what decision consequence follows.
- Keep the default summary substantive but readable: usually 900-1600 words for a full document, shorter only when the source is small or fragmentary.
- Use a clear written style: remove filler, avoid repeated wording, prefer direct verbs, and rewrite awkward rubric phrasing into natural Russian. Do not add a separate tone-analysis section.
- End with exactly one follow-up question: ask whether the user wants the expanded structured final synthesis.
- If the review is fragmentary, explicitly say that the conclusion is provisional and limited by incomplete input.
- If the user explicitly asked for the structured schema, or answers yes to the expanded blocker/evidence question, output the structured final synthesis below.
- After showing the structured final synthesis in response to a user yes, ask: `Хотите полный разбор по слоям?`
- If the user answers yes to the full-analysis question, output the detailed mode: final synthesis, Input Doc, Layer 1, Layer 2, Layer 3, and merged block assessment.
- Do not rerun the review only because the user asks for the expanded or full version; reuse the already computed synthesis and layer artifacts when they are available in the conversation.
- If `debug stages=on`, skip the narrative summary and use detailed mode with explicit Layer 1, Layer 2, and Layer 3 sections.

### Reader-comprehension pass

Run a final reader-comprehension pass before returning `summary` output.

Check that a top-management reader would understand what happened without opening the document:

- the opening assessment explains the decision context before the issue list
- every major reason connects the broken or unproven claim to the approval consequence
- every evidence bullet connects the fact to the decision risk
- technical terms, source metrics, and business shorthand are translated or explained at first use
- proof bullets do not stop at a raw number, quote, or section name
- the final recommendation states what can be approved now, what cannot be approved yet, and what evidence would change that

If any item fails, rewrite the answer before returning if the proof chain is unclear, context is missing, or evidence reads like a detached citation.

This is a presentation pass: do not add new issues during this pass, do not change severities, and do not upgrade or downgrade the verdict only because the wording became clearer.

### Final synthesis format

The structured final synthesis is the expanded summary format.

The structured final synthesis is the short blocker/evidence summary. Use it only when:

- the user explicitly asks for a structured/technical output
- the user answers yes to the default summary follow-up
- `extended` / `detailed` output needs the final synthesis section before Layer 1 and Layer 2

```text
verdict: APPROVE | NEED_EVIDENCE | REJECT
confidence: HIGH | MEDIUM | LOW
blockers:
- blocker_id: B<n>
  block: <canonical block name>
  severity: HIGH | MEDIUM | LOW
  reason: <readable blocker statement with the term, plain explanation, and decision consequence>
  origin: covered_by_l2 | novel_from_l1 | novel_from_l3 | confirmed_by_both
  evidence:
    - <quote / section / fragment reference>

critical_improvements:
- improvement_id: I<n>
  block: <canonical block name>
  suggestion: <non-blocking but high-value improvement>
  evidence:
    - <quote / section / fragment reference>
```

Rules:

- only blocker-grade issues may appear in `blockers`
- non-blocking weaknesses must not appear in `blockers`
- if final verdict is `APPROVE`, include `critical_improvements`
- `critical_improvements` are important but non-mandatory
- do not include internal layer refs in the final synthesis; keep them only in diagnostic sections
- when the review is fragmentary, keep the wording explicitly provisional and force `LOW` confidence
- final blocker reason must name the broken claim, the proof gap, and the approval consequence
- blocker evidence must provide enough local context to understand criticality without opening the document
- include the specific threshold miss, unresolved dependency, model assumption, or contradictory claim that makes the blocker material
- write final blocker `reason` as a readable mini-argument, not as a rubric label: first name the decision claim, then the missing or contradictory proof, then the gate consequence
- write blocker `evidence` as a short proof chain with source context: `<section/table> says <claim or target>; <section/table> shows <fact/result>; therefore <why the gap is material>`
- use `origin: novel_from_l3` only when the Layer 3 finding has concrete document evidence, changes what can be safely approved now, and is not already covered by Layer 1 or Layer 2
- do not promote generic adversarial concerns from Layer 3 into `blockers`
- Expand unclear terms inside `reason`, not only in `evidence`. Bad: `depends on partner readiness and pre-scoring`. Good: `depends on whether banks and BNPL partners have confirmed launch terms, API integration, traffic capacity, and whether pre-scoring can reliably predict approval before the user sees an offer`.
- Avoid label-only blocker reasons such as `dependency-readiness`, `proxy-validation`, `planning-vs-validation`, or `model-assumption-readiness`. These labels may remain only as internal duplicate-family keys, not as user-facing explanations.
- write `reason` and `evidence` explanations in Russian, except exact source text, metric names, product names, schema keys, and status values

## Detailed mode

In `detailed` mode, output:

1. final synthesis
2. one `Input Doc` line
3. normalized Layer 1
4. normalized Layer 2
5. normalized Layer 3
6. merged block assessment

If `debug stages = on`, keep Layer 1, Layer 2, Layer 3, and merged block assessment explicitly visible as separate sections even if the user asks for a compact diagnostic response.

Detailed mode readability rules:

- Treat detailed mode as the full human-readable analysis, not as a raw rubric dump.
- Preserve the required statuses, canonical block names, questions, and schema fields, but make every `issue`, `evidence`, `promotion_test`, `merged_interpretation`, and `why_difference` understandable without knowing the rubric.
- When a block uses a technical or source term, explain it the first time it appears in that block. For example, do not write only `partner readiness`; write that this means confirmed partner launch terms, API integration, traffic capacity, commercial terms, and operational ownership.
- Do not leave compact diagnostic labels as the only explanation. Phrases like `same duplicate family; see proxy-validation` are acceptable only after the representative issue in the same block has already explained the underlying problem in Russian.
- In Layer 1 and merged block assessment, prefer a short paragraph-level explanation of the block consequence over a terse label. The reader should understand what cannot be approved, what evidence is missing, and what should change in the document.
- In Layer 2, keep the atomic questions, but make non-`YES` answers concrete: state which claim is being tested, what fact fails to prove it, and why that matters for the gate decision.
- In Layer 3, keep the adversarial lens names, but write each finding as a concrete mini-argument tied to document evidence and the committee decision.
- Use the same writing-quality pass as summary mode: remove filler, avoid repeated wording, replace awkward rubric phrases with clear Russian, and keep the tone professional and investment-committee oriented.

## Readability is a presentation layer

Readable issue text must not change the evaluator's decisions.

- use readability rules to explain already-selected issues, not to discover extra issues
- do not add a new Layer 1 issue, Layer 2 standalone issue, final blocker, severity upgrade, or verdict upgrade only because a longer explanation can be written
- if a readable explanation reveals that two issues share the same root cause, consolidate them rather than split them
- preserve duplicate-family and output-budget limits before applying the readability pass
- when a detail belongs only as proof for a broader blocker, keep it in `evidence` instead of promoting it to a separate issue
- this does not suppress distinct block consequences required by the rubric; for example, the same missing MLP/end-state journey can appear in Solution for adoption testability and in Scope for test-vs-rollout readiness

## Normalized Layer 1 format

Layer 1 output must match the normalized benchmark format.

```text
**Input Doc:** [INPUT_DOC_URL](INPUT_DOC_URL)

## Layer 1

verdict: APPROVE | NEED_EVIDENCE | REJECT
dimension:

### Problem framing and segments: PASS | PARTIAL | FAIL

- id: 1
  issue: <short decision-relevant issue>
  evidence: <quote / section / fragment reference>
  severity: HIGH | MEDIUM | LOW
```

Rules:

- print the `Input Doc` line once before `## Layer 1`
- the `verdict` line in this section is the Layer 1 rollup verdict, not a second independent final verdict
- use exactly seven dimensions in the canonical order
- dimension status must be `PASS`, `PARTIAL`, or `FAIL`
- max 3 issues per dimension
- Default to 1-2 Layer 1 issues per dimension
- Use 3 issues only when there are three independent decision blockers that are not evidence for each other
- only decision-relevant issues
- Layer 1 may raise a cross-sectional dimension-level issue when the decision narrative breaks across sections
- every issue should preserve the specific decision test behind the problem instead of only an umbrella diagnosis
- every issue must be self-contained for a reader who has not opened the source document
- each issue must state what is wrong, why it matters for the gate decision, and what decision consequence follows
- write `issue` and explanatory `evidence` in Russian, while preserving exact source labels, metric names, product names, and quoted text
- prefer two compact sentences in `issue`: sentence 1 explains the broken decision test in plain language; sentence 2 explains why this changes approval safety
- evidence must include section or table name plus the exact values, thresholds, dates, user segments, or claims being compared
- do not cite a section name without explaining what in that section proves the issue
- when evidence is a contradiction, include both sides of the contradiction in the evidence field
- evidence should read like a mini-proof, for example: `FAQ 5 sets seller readiness threshold at 60% for B2C White, but reports 44% for Enterprise and 58% for C2C without a clean B2C White result; this is why the "confirmed" conclusion is not decision-safe`
- use separate Layer 1 issues for the same root cause only when each issue has a distinct decision consequence; otherwise do not repeat it as a new issue
- bundle related Layer 2-level observations under a broader Layer 1 decision blocker when they support one gate failure
- keep missed funnel thresholds, buyer/seller activation misses, the optional-pilot-to-mandatory-rollout leap, planning statements treated as validation, and take-rate / monetization assumption changes as evidence under the broad Layer 1 issue unless each has a distinct decision consequence
- Prefer one broad Layer 1 traction issue for model reconstructability; treat a changed 10% -> 15% monetization or take-rate assumption as evidence under that issue unless it is the only material traction weakness
- when MLP and end-state path are not explicit enough, write the issue as `MLP/end-state journey is missing or not evaluable`; in Solution state that it makes adoption behavior untestable, and in Scope state that it makes test-vs-rollout readiness impossible to judge
- useful specific tests include missing threshold, missing user journey, unmet success criterion, unreconciled topline, or unresolved prerequisite
- if dimension status is `PASS`, output only non-blocking residual issues, or one `No material issue` record when there is no meaningful weakness
- every issue must contain `id`, `issue`, `evidence`, and `severity`

## Normalized Layer 2 format

Layer 2 output must match the normalized benchmark format.

```text
## Layer 2

### Atomic checks - Problem framing and segments: PASS | PARTIAL | FAIL

- question: <full atomic question>
  answer: YES | PARTIAL | NO
  evidence: <quote / section / fragment reference>
  issue: <gap, weakness, or "No material issue">
```

Rules:

- use exactly seven Atomic checks blocks in the canonical order
- Atomic checks block status must be `PASS`, `PARTIAL`, or `FAIL`
- every atomic question must be present
- every atomic answer must be `YES`, `PARTIAL`, or `NO`
- `issue` is always required
- use `No material issue` only when answer is `YES` and there is no meaningful weakness
- answer `PARTIAL` or `NO` only when the issue changes approval safety, validation strength, or the block verdict
- if an atomic check finds only a plausible nuance, generic completeness concern, or already-covered concern, answer `YES` with `No material issue` or use `same duplicate family; local angle:`
- suppress non-central extras unless the document's decision thesis depends on that point
- answer every atomic check internally, but emit a standalone Layer 2 issue only when the weakness is concrete, decision-relevant, and not already represented by a stronger nearby issue
- generic weak-link checks default to `YES` / `No material issue` unless there is a specific contradiction, threshold miss, formula gap, unresolved dependency, unsupported scaling leap, or inconsistent risk control
- do not emit generic standalone issues for broad target clarity, segment mapping, projected upside, softer alternatives, or downside sensitivity when they only restate a stronger nearby issue
- Layer 2 output budget: emit at most the two strongest distinct issue families per Atomic checks block
- additional atomic checks should reference the selected family in evidence rather than create another issue
- assign a duplicate-family key before writing Layer 2 output; examples include `dependency-readiness`, `proxy-validation`, `monetization-contradiction`, `cancellation-boundary`, `threshold-mismatch`, `model-reconstructability`, `segment-path-mixing`, and `risk-control-maturity`
- selected issue families are a pre-output control, not an optional writing style
- only the selected representative atomic answer gets full standalone issue text
- each selected representative issue must be self-contained for a reader who has not opened the source document
- selected representatives must state what is wrong, why it matters for the gate decision, and what decision consequence follows
- avoid label-only issue text such as `proxy-validation:` without a plain-language explanation
- if an issue uses a duplicate-family key, follow it with a plain-language explanation in the same sentence
- prefer `issue` wording that explains the local decision test before the family name when the family label would be opaque to a human reader
- write selected representative `issue` text in Russian; duplicate-family keys may remain in English only as compact labels after the Russian explanation
- evidence must include section or table name plus the exact values, thresholds, dates, user segments, or claims being compared
- do not cite a section name without explaining what in that section proves the issue
- when evidence is a contradiction, include both sides of the contradiction in the evidence field
- non-selected repeated atomic answers must use `same duplicate family; see <family>`
- do not add a second local-angle issue sentence for the same family
- every atomic question must still be answered against its own decision test
- if there is concrete evidence for a problem-bearing atomic check, record the issue even when the same family is also covered elsewhere
- when a problem-bearing atomic check repeats the same family, use `same duplicate family; local angle:` only when the local consequence is materially different; do not turn the issue into `YES` / `No material issue` if that would hide a real decision defect, but do not create a second standalone issue for the same defect
- avoid restating the same insight as separate standalone failures; if a repeated concern is relevant, state the local angle only, for example "same prerequisite gap, here specifically affecting test-vs-rollout gating"
- if an insight repeats the same duplicate family, reference it as evidence rather than a new `issue`
- if the same duplicate family repeats and a local consequence must still be recorded, write `same duplicate family; local angle:` and use that prefix before the block-specific consequence; do not create a fresh standalone issue
- duplicate family examples: central closure not tested; end-state path/API gap; projected ramp not explained by validated inputs; 10% evidence does not validate 15% monetization; mitigations are plans, not controls
- monetization/cannibalization contradiction can appear in Traction and Consistency when local consequences differ: Traction: model economics are unsupported or internally inconsistent; Consistency: risk defense contradicts target economics; use local-angle wording to avoid duplicate penalties
- preserve exact threshold mechanics, the specific row, year, driver, or formula detail, and fraud and lower-commission mechanics when those details determine whether a match is partial or complete
- the Atomic checks block status is the Layer 2 aggregate for that block; do not output a separate aggregate section

## Normalized Layer 3 format

Layer 3 output must match the normalized benchmark format.

```text
## Layer 3

verdict: APPROVE | NEED_EVIDENCE | REJECT
adversarial_findings:
- id: A<n>
  lens: <short lens name>
  issue: <concrete adversarial issue>
  evidence: <section / table / FAQ / appendix source plus exact fact>
  severity: HIGH | MEDIUM | LOW
  promotion_test: <why this changes what can be safely approved now, or why it should remain diagnostic>
```

Rules:

- Layer 3 returns only `layer_3`
- use the lens names as discovery prompts, not as a forced checklist
- every `HIGH` or `MEDIUM` finding must cite concrete document evidence
- `promotion_test` must explain the committee consequence in plain Russian
- if the issue does not change what can be safely approved now, keep it diagnostic or move it to `critical_improvements`
- do not promote generic adversarial concerns from Layer 3 into final blockers
- avoid repeating a Layer 1 or Layer 2 issue unless the Layer 3 angle changes the decision consequence
- write `issue`, `evidence`, and `promotion_test` in Russian by default, while preserving exact source names, product names, and metric labels

## Merged block assessment format

```text
merged_block_assessment:
- block: <canonical block name>
  l1_status: PASS | PARTIAL | FAIL
  l2_status: PASS | PARTIAL | FAIL
  agreement_status: CONFIRMED | REFINED | DOWNGRADED | CONFLICT
  merged_interpretation: <short resolved statement>
  why_difference: <required for DOWNGRADED | CONFLICT>
  blocker_origin: covered_by_l2 | novel_from_l1 | novel_from_l3 | confirmed_by_both | none
  merged_sources:
    - layer: L1 | L2 | L3
      ref: <issue id | question text>
```

Rules:

- `agreement_status` is required for every block
- `why_difference` is required when `agreement_status` is `DOWNGRADED` or `CONFLICT`
- `merged_block_assessment` explains how broad Layer 1 judgment, detailed Layer 2 evidence, and promotable Layer 3 findings were reconciled
- `merged_block_assessment` does not replace the raw Layer 1, Layer 2, and Layer 3 outputs

## Canonical block names

Use exactly these seven block names in Layer 1, Layer 2, and merged block assessment:

1. Problem framing and segments
2. Solution quality and logic
3. Scope of work and implementation plan
4. Success criteria and metrics
5. Traction model credibility
6. Key assumptions and risks completeness
7. Consistency
