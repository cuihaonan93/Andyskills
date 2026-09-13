---
name: dashixiong-baozhuang
description: Evidence-preserving manuscript diagnosis and revision for academic drafts. Use when the user asks to improve, upgrade, package, restructure, or prepare a manuscript for submission without changing the underlying study. Audits claims, evidence, reporting completeness, language, figures, references, and journal compliance; produces a traceable revision and author action list.
---

# Manuscript Diagnosis and Evidence-Preserving Revision

Use this Skill to improve how a completed or near-complete study is communicated. Treat every stronger sentence as a claim that must remain within the supplied evidence.

## Non-negotiable boundaries

- Do not invent or alter data, experiments, analyses, mechanisms, citations, figures, methods, uncertainty, or conclusions.
- Do not convert a proposed analysis into a completed analysis. Mark it as an author action.
- Do not call a contribution novel, first, superior, robust, general, causal, or mechanism-revealing unless the evidence and current literature support that exact claim.
- Do not promise a journal quartile, acceptance, impact, or publication outcome.
- Preserve numbers, units, equations, terminology, reference intent, and qualification unless the author verifies a correction.
- Separate observed result, supported interpretation, hypothesis, and recommendation.

## Routing

- Use `nature-polishing` for sentence-level academic editing after technical claims are stable.
- Use `nature-citation` and `nature-ref-verifier` for citation support and bibliographic verification.
- Use `nature-figure`, `nature-data`, and `nature-statistics` for their respective audits.
- Use the installed document Skill for DOCX editing and its render-and-verify workflow. Academic document scripts use the absolute `NatureSkills` interpreter.
- Use `dashixiong-innovation` when the task is research opportunity generation, `dashixiong-mofang` for reference-paper decomposition and a new research blueprint, and `dashixiong-sci` for drafting from verified author materials.

## Workflow

### 1. Establish scope

Inspect only files identified by the user or directly required for the named manuscript. Determine the target journal, requested deliverables, editable sections, language, and whether tracked changes or a clean revision is required. If no journal is specified, use a neutral single-column manuscript format and do not guess journal rules.

### 2. Build an evidence ledger

For each consequential claim, record:

| Claim | Evidence location | Status | Allowed action |
|---|---|---|---|
| Verbatim or normalized claim | Figure/table/result/method/citation | supported / overextended / missing / uncertain | retain / narrow / query / author action |

Flag inconsistencies between abstract, results, figures, discussion, and conclusion. A missing result cannot be repaired by prose.

### 3. Diagnose the manuscript

Audit four dimensions:

1. **Argument**: research question, contribution, logic, claim-evidence correspondence, limitations.
2. **Reproducibility**: data provenance, parameters, baselines, controls, uncertainty, software, seeds, and validation details appropriate to the field.
3. **Presentation**: structure, terminology, tables, figures, captions, equations, and language.
4. **Compliance**: target-journal instructions, citations, data/code availability, ethics, disclosures, and reporting standards.

Prioritize issues by scientific consequence, not cosmetic visibility.

### 4. Revise within evidence

- Reorganize sections and paragraphs to expose the real question, method, evidence, and bounded contribution.
- Narrow unsupported claims instead of decorating them.
- Add missing methodological detail only when it is present in author materials or confirmed by the author.
- Suggest additional analyses, figures, or experiments in a separate action list; never write them as completed work.
- Describe mechanisms only when independently supported. Otherwise label them as hypotheses and state alternative explanations.
- Verify current journal instructions from an authoritative source when formatting matters.

### 5. Deliver traceably

Default deliverables are:

- revised manuscript or section;
- change log with reason and evidence impact;
- unresolved author queries;
- recommended analyses or reporting additions, explicitly marked as not yet performed;
- submission-readiness checklist.

For DOCX output, preserve the source document, write a new filename, render it, inspect every page, and correct layout defects before delivery. Do not overwrite unless explicitly requested.

## Acceptance check

- Every strengthened claim has identifiable evidence.
- No proposed work is presented as completed.
- Observations, interpretations, hypotheses, and limitations remain distinct.
- References and journal requirements are verified or visibly marked unverified.
- The revision log allows the author to review substantive changes.

See `references/revision-method.md` and `assets/diagnostic-report-template.md` for the detailed audit and report structure.
