---
name: dashixiong-sci
description: Draft or restructure scientific manuscript sections from author-provided, verified research materials. Use for SCI manuscript drafting, bilingual author-review drafts, section planning, claim-evidence mapping, and journal-aware Word output when methods, results, figures, and citations are available.
---

# Evidence-Bounded Scientific Manuscript Drafting

Draft from verified author materials. A manuscript is an auditable argument built from research evidence, not a fixed sentence template.

## Required boundaries

- Never invent data, analyses, significance, trends, mechanisms, figures, methods, citations, novelty, or conclusions.
- Do not automatically scan the working directory. Inspect only files identified by the user or clearly required by the named task.
- Do not fill research background or references from memory. Search and verify when authorized; otherwise mark the gap.
- Do not force a mechanism. Separate observation, supported interpretation, hypothesis, and alternative explanation.
- Do not force a fixed abstract sentence count, section count, recent-reference percentage, or publisher layout. Follow the current target-journal instructions; otherwise use a neutral structure.
- Do not claim OpenFAST-level fidelity, universality, causality, robustness, or generalization from training loss or a narrow benchmark. Apply domain-specific evidence standards.
- Never treat a provisional model architecture as the permanent default.

## Routing

- Use `nature-writing` when its Nature-style manuscript architecture is requested, and `nature-polishing` for language editing.
- Use `nature-academic-search`, `nature-citation`, and `nature-ref-verifier` for literature and citation work.
- Use `nature-statistics`, `nature-data`, and `nature-figure` for specialized reporting.
- Use the installed document Skill for DOCX creation/editing and page rendering. Academic scripts must call `C:\Users\15382\anaconda3\envs\NatureSkills\python.exe` explicitly.
- Use `dashixiong-mofang` before drafting when the user only has reference papers and no completed study evidence. Use `dashixiong-baozhuang` for revising an existing manuscript.

## Intake: build a research evidence packet

Collect or derive only from supplied files:

| Packet item | Minimum content |
|---|---|
| Scope | research question, system/population, conditions, exclusions |
| Methods | data provenance, design, software/equipment, parameters, controls, reproducibility details |
| Results | verified tables/figures/statistics, units, uncertainty, failures, negative results |
| Contributions | author-stated contribution candidates and comparison basis |
| Literature | verified sources and the propositions they support |
| Target | journal/article type, current instructions, language, deliverables |

Missing methods may be marked for author completion. Missing results block Results, Discussion, Conclusion, and result-bearing abstract claims.

## Build a claim-evidence map

Before drafting, map each intended claim to a result, method, figure/table, or verified citation. Assign one status: supported, qualified, disputed, missing, or author confirmation required. Draft only supported or explicitly qualified claims.

## Drafting workflow

1. **Methods:** write reproducible facts from the packet; preserve exact parameter values and provenance.
2. **Results:** report observations in an order tied to the research questions. Include uncertainty and failure cases.
3. **Discussion:** compare with verified literature, explain only what evidence supports, consider alternatives, and state limitations.
4. **Conclusion:** answer the declared questions without adding new evidence or expanding scope.
5. **Introduction:** synthesize the problem, evidence landscape, bounded gap, and study objective; organize literature by question, not chronology.
6. **Title and abstract:** write last so their claims match the completed evidence map.

The actual section order and labels must follow the article type and target journal.

## Placeholders

Use explicit markers:

- `[AUTHOR INPUT REQUIRED: ...]` for missing factual detail.
- `[ANALYSIS NOT RUN: ...]` for proposed analysis.
- `[CITATION TO VERIFY: proposition]` for unsupported background.
- `[CLAIM EXCEEDS EVIDENCE: ...]` for overreach.
- `[FIGURE DESCRIPTION REQUIRED]` when the figure was not inspected.

Never use a paper title alone as a bibliographic placeholder that looks like a verified citation.

## Wind-turbine identification guardrail

For turbine-modeling manuscripts, keep the learned plant and controller separate. Report causal free rollout, held-out turbine designs and operating conditions, dynamics/frequency/load/stability metrics, uncertainty, and paired closed-loop comparison using the same verified ROSCO bundle. Treat Koopman, DKN, neural operators, and other architectures as hypotheses selected through reproducible comparison, not fixed conclusions.

## Output and artifact verification

Default output is a Markdown draft plus the claim-evidence ledger and author query list. Generate English/Chinese versions only when requested; the Chinese version is for author review and must retain the same claim boundaries.

For DOCX output:

- preserve the original and use a new filename unless overwrite is explicit;
- use a verified journal template only when supplied or obtained from an authoritative current source;
- use neutral single-column formatting otherwise;
- render every page, inspect figures/tables/equations/headers, and correct defects;
- report unresolved placeholders and unverified citations with the file.

## Acceptance check

- Every substantive claim maps to evidence or a visible qualifier.
- Abstract and conclusion contain no claims absent from Results/Discussion.
- Methods are reproducible to the extent allowed by supplied information.
- Mechanisms and causal language meet the design's evidence standard.
- Citations support nearby propositions and are bibliographically verified.
- Scope limits, uncertainty, negative results, and unresolved placeholders remain visible.
- Output follows the current target format or is explicitly neutral.

See `references/evidence-packet.md` for working tables.
