---
name: dashixiong-innovation
description: Evidence-grounded research-gap analysis and research-opportunity design from papers, a DOI, a literature set, or a research topic. Use for WWH paper decomposition, gap mapping, novelty-risk assessment, falsifiable candidate studies, feasibility ranking, and advisor-ready research opportunity reports.
---

# Evidence-Grounded Research Opportunity Design

Use literature to generate testable research opportunities, not declarations of guaranteed novelty. Treat every candidate as a provisional hypothesis until the search is refreshed and the proposal survives expert and practical review.

## Boundaries

- A small literature set cannot establish that no prior work exists. Use `not found in the searched corpus`, never `first` or `unprecedented`, unless a documented comprehensive search supports it.
- Do not rank papers or ideas by citation count, journal label, or recency alone. Consider relevance, study quality, directness, correction/retraction status, and field-specific evidence.
- Do not manufacture gaps by misrepresenting a paper's scope or limitations.
- Do not assume a new model, combination, application, or benchmark is scientifically useful. Require a reasoned mechanism or decision need and a discriminating evaluation.
- Include null outcomes, alternative explanations, resource limits, and failure criteria.
- Never promise graduation, publication, a journal tier, or impact.

## Routing

- Use `nature-academic-search` for literature discovery and documented search records.
- Use `nature-reader` for full-paper, figure-aware reading and `nature-downloader` for lawful acquisition.
- Use `nature-citation` or `nature-ref-verifier` before finalizing citations.
- Use the document and presentation Skills only when the user requests DOCX or PPTX artifacts. Their Python work uses the absolute `NatureSkills` interpreter.
- Use `dashixiong-mofang` for a deep blueprint based on 1-3 reference papers. Use `dashixiong-sci` only after research evidence exists.

## Workflow

### 1. Define the decision

Record the research domain, intended decision or scientific question, population/system, operating envelope, available data and facilities, time/resources, and exclusions. When these are unknown, state assumptions or ask only for information that materially changes the analysis.

### 2. Build a reproducible literature corpus

Record databases/tools, query strings, dates, filters, included/excluded records, access limitations, and version of the corpus. Start from user-supplied sources; expand only as needed. Do not impose an arbitrary fixed paper count.

### 3. Decompose evidence with WWHL

For each source capture:

- **Why:** stated problem, context, and motivation.
- **What:** claims and findings with exact evidence location.
- **How:** data, design, assumptions, baselines, metrics, and validation.
- **Limits:** author-reported and independently identified limitations.

Distinguish source facts from your inference.

### 4. Construct a gap map

Classify gaps when useful as evidence, scope, method, efficiency, realism, disagreement, reproducibility, translation, or decision gaps. For each gap include supporting and contradicting sources, affected boundary, confidence, consequence, and what observation would close the gap.

Absence of papers in a query may be a search limitation, not a research gap.

### 5. Generate candidate studies

Candidates may involve application transfer, assumption relaxation, integration, comparison, new measurement, new theory, or a null/replication study. Each candidate must contain:

- precise research question and falsifiable hypothesis;
- provenance from the gap map;
- independent contribution and decision value;
- data, tools, controls, baselines, and evaluation design;
- expected observations under competing explanations;
- feasibility, dependencies, ethical/safety constraints, and cost;
- failure criteria, negative-result value, limitations, and next action;
- provisional novelty confidence and the search needed to strengthen it.

### 6. Rank transparently

Use a decision matrix whose weights reflect the user's objective. Typical dimensions are scientific importance, evidence strength, novelty confidence, feasibility, discriminating power, reproducibility, time, cost, and risk. Show weights, scores, uncertainty, and sensitivity to changed weights. Do not hide subjective judgments inside a single total.

### 7. Deliver

Default output is a concise Markdown report containing corpus scope, WWHL cards, gap map, candidate matrix, top candidate protocols, critical unknowns, and immediate validation actions. Generate Word or PPT only when requested, using the applicable artifact Skill and visual verification workflow.

## Acceptance check

- Literature facts have locatable sources.
- Novelty statements match the documented search scope.
- Each candidate is falsifiable and has a fair baseline or control.
- Alternative explanations and null outcomes are explicit.
- Feasibility claims reflect actual resources.
- The next experiment or search can materially change the decision.

See `references/methodology.md` and `references/report-template.md`.
