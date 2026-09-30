# Archetype (A-16)

**Archetype** is a repository of inspectable prompt architectures, packaged prompt systems, legacy GPT archetypes, and standalone prompt specifications.

The reusable core is **Construct**: a set of 20 Markdown prompt specifications for construct design, comparison, evaluation, information and knowledge work, judgment, modeling, learning, prioritization, validation, workflow design, and related tasks. Its current packaged distribution is [`Construct v0.9.18`](Construct/Construct_v.0.9.18.zip).

The repository also contains packaged systems for **Citation**, **Systematic Review**, and **Visual Art**, with their human-readable prompt sources checked in under [`Prompts/`](Prompts).

[Get Started](#get-started) · [Packaged Systems](#packaged-systems) · [Construct](#construct) · [Construct Modules](#construct-modules) · [Standalone Prompts](#standalone-prompts) · [Legacy Archetypes](#legacy-archetypes) · [Repository Layout](#repository-layout)

## Get Started

This repository is primarily Markdown prompt specifications plus packaged ZIP artifacts. There is no repository-wide build or install command.

### Use the source prompts directly

- For the reusable core, choose a module from [`Prompts/Construct/`](Prompts/Construct).
- For Citation, use [`Prompts/CT.md`](Prompts/CT.md).
- For Systematic Review, use [`Prompts/SR.md`](Prompts/SR.md).
- For Visual Art, use [`Prompts/VA.md`](Prompts/VA.md).
- For older standalone archetypes, browse [`GPTs/`](GPTs).
- Additional standalone prompt specifications are available under [`Prompts/`](Prompts).

Supply the selected prompt to the LLM/GPT environment you use in the way that environment accepts system, custom-instruction, or prompt content.

### Use a packaged artifact

The repository currently contains four versioned ZIP artifacts:

- [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip)
- [`Citation_v.0.1.1.zip`](Plugins/Citation_v.0.1.1.zip)
- [`Systematic_Review_v.0.1.7.zip`](Plugins/Systematic_Review_v.0.1.7.zip)
- [`Visual_Art_v.0.1.0.zip`](Plugins/Visual_Art_v.0.1.0.zip)

Import or load a ZIP only with a host that supports the package format you are using. The repository does not define a universal installer or runtime for these archives, so the checked-in Markdown sources are the portable, inspectable reference where a corresponding source prompt is available.

## Packaged Systems

| System | Package | Human-readable source | Scope |
|---|---|---|---|
| Construct | [`v0.9.18`](Construct/Construct_v.0.9.18.zip) | [`Prompts/Construct/`](Prompts/Construct) | General-purpose reasoning, representation, knowledge, decision, validation, and workflow architectures |
| Citation | [`v0.1.1`](Plugins/Citation_v.0.1.1.zip) | [`CT.md`](Prompts/CT.md) | Scholarly reference, evidence linkage, attribution, provenance, verification, and citation governance |
| Systematic Review | [`v0.1.7`](Plugins/Systematic_Review_v.0.1.7.zip) | [`SR.md`](Prompts/SR.md) | Systematic review and evidence-synthesis workflows, appraisal, synthesis, reporting, reproducibility, and updating |
| Visual Art | [`v0.1.0`](Plugins/Visual_Art_v.0.1.0.zip) | [`VA.md`](Prompts/VA.md) | Visual-art practice spanning perception, conception, research, design, making, critique, exhibition, preservation, professional practice, and learning |

## Construct

Construct is the repository's reusable core prompt architecture. It is organized as standalone Markdown specifications rather than executable software modules.

Each module frames a problem domain as a system: it defines key distinctions, entities and relationships, operating or evaluation models, uncertainty and evidence considerations, governance concerns, and workflows. The modules can be used independently from [`Prompts/Construct/`](Prompts/Construct), while the ZIP provides the versioned packaged distribution.

### Design intent

- **Reusable core:** the modules cover general reasoning and workflow primitives rather than a single task or persona.
- **Inspectable sources:** every checked-in core module is readable as Markdown.
- **Independent or combined use:** a module can be used directly, or the packaged Construct artifact can be used where supported.
- **Explicit boundaries:** the prompts repeatedly distinguish neighboring concepts instead of treating them as interchangeable.
- **Evidence and governance:** many modules include provenance, uncertainty, validation, monitoring, or governance as first-class concerns.

## Construct Modules

| Code | Module | Primary focus |
|---|---|---|
| C | [Construct](Prompts/Construct/C.md) | Archetypal personas, generative identity systems, and construct design |
| D | [Difference](Prompts/Construct/D.md) | Distinction, contrast, comparison, boundaries, and meaningful non-sameness |
| E | [Evaluation](Prompts/Construct/E.md) | Evidence, measurement, causal analysis, value judgments, and metaevaluation |
| F | [Format](Prompts/Construct/F.md) | Representation, encoding, schemas, interoperability, and transformation |
| G | [Gist](Prompts/Construct/G.md) | Minimum-sufficient meaning, compression, relevance, and faithful summarization |
| I | [Information](Prompts/Construct/I.md) | Information architecture, semantics, retrieval, provenance, and governance |
| J | [Judgement](Prompts/Construct/J.md) | Disciplined assessment, uncertainty, calibration, and decision support |
| K | [Knowledge](Prompts/Construct/K.md) | Knowledge frontiers, evidence, synthesis, exploration, and revision |
| L | [Learning](Prompts/Construct/L.md) | Learning science, memory, skill acquisition, transfer, and metacognition |
| M | [Model](Prompts/Construct/M.md) | Abstraction, formalization, simulation, validation, and model evolution |
| N | [Name](Prompts/Construct/N.md) | Naming, terminology, identifiers, namespaces, and nomenclature |
| O | [Openness](Prompts/Construct/O.md) | Access, transparency, interoperability, commons, licensing, and governance |
| P | [Priority](Prompts/Construct/P.md) | Prioritization, allocation, sequencing, triage, and portfolio decisions |
| Q | [Question](Prompts/Construct/Q.md) | Inquiry, information seeking, diagnosis, sequencing, and question quality |
| R | [Ranking](Prompts/Construct/R.md) | Comparative judgment, scoring, ordering, selection, and ranking governance |
| S | [Similarity](Prompts/Construct/S.md) | Resemblance, equivalence, correspondence, matching, and justified likeness |
| T | [Taxonomy](Prompts/Construct/T.md) | Classification, terminology, semantic structure, and knowledge organization |
| U | [Uniqueness](Prompts/Construct/U.md) | Identity, rarity, originality, discriminability, and provenance |
| V | [Validity](Prompts/Construct/V.md) | Verification, validation, evidence, assurance, and warranted reliance |
| W | [Workflow](Prompts/Construct/W.md) | Workflow discovery, orchestration, execution, observability, and optimization |

## Standalone Prompts

The top-level [`Prompts/`](Prompts) directory also contains standalone prompt specifications outside the Construct module set:

- [`CT.md`](Prompts/CT.md) — Citation
- [`RS.md`](Prompts/RS.md)
- [`SR.md`](Prompts/SR.md) — Systematic Review
- [`ST.md`](Prompts/ST.md)
- [`TR.md`](Prompts/TR.md)
- [`VA.md`](Prompts/VA.md) — Visual Art

## Repository Layout

```text
archetype/
├── Construct/
│   └── Construct_v.0.9.18.zip
├── Plugins/
│   ├── Citation_v.0.1.1.zip
│   ├── Systematic_Review_v.0.1.7.zip
│   └── Visual_Art_v.0.1.0.zip
├── Prompts/
│   ├── Construct/                    # 20 source modules: C-G and I-W
│   ├── CT.md
│   ├── RS.md
│   ├── SR.md
│   ├── ST.md
│   ├── TR.md
│   └── VA.md
├── GPTs/                            # legacy standalone archetype library
├── tests/
│   └── test_readme.py               # README local-link guard
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml         # runs the README link guard in CI
├── A_Avatar.png
├── LICENSE                          # Apache License 2.0
└── README.md
```

## Legacy Archetypes

[`GPTs/`](GPTs) is the repository's library of standalone archetype prompts. It includes domain specialists, creative practices, specialized workflows, perspectives, and simulations of named people.

These prompts can be used independently from Construct and the packaged systems. They remain separate because they are primarily task-, perspective-, or persona-specific, while Construct is the reusable general-purpose prompt architecture.

Named-person prompts are simulations or perspective prompts, not the people represented. Inclusion in the repository is not an endorsement, and a prompt's subject label does not establish authority, factual accuracy, or evidentiary status.
