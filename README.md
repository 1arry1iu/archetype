# Archetype (A-16)

**Archetype** is a repository of inspectable prompt architectures, packaged prompt systems, and legacy GPT archetypes.

The reusable core is **Construct**: a set of 20 Markdown prompt specifications for construct design, comparison, evaluation, information and knowledge work, judgment, modeling, learning, prioritization, validation, workflow design, and related tasks. Its human-readable source is under [`Prompts/Construct/`](Prompts/Construct), and its current packaged distribution is [`Construct v0.9.18`](Construct/Construct_v.0.9.18.zip).

The repository also contains domain-specific prompt systems under [`Prompts/`](Prompts) and versioned package artifacts under [`Plugins/`](Plugins).

[Get Started](#get-started) · [Packaged Systems](#packaged-systems) · [Source Prompt Systems](#source-prompt-systems) · [Construct](#construct) · [Modules](#construct-modules) · [Legacy Archetypes](#legacy-archetypes) · [Repository Layout](#repository-layout)

## Get Started

This repository is primarily Markdown prompt specifications plus packaged ZIP artifacts. There is no repository-wide build or install command.

### Use the source prompts directly

- For the reusable Construct core, choose a module from [`Prompts/Construct/`](Prompts/Construct).
- For Citation, Research, Systematic Review, Synthesis, Theory, and Visual Art, browse the source prompts in [`Prompts/`](Prompts).
- For older standalone archetypes, browse [`GPTs/`](GPTs).

Supply the selected prompt to the LLM/GPT environment you use in the way that environment accepts system, custom-instruction, or prompt content.

### Use a packaged artifact

The repository currently contains four versioned ZIP artifacts:

- [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip)
- [`Citation_v.0.1.1.zip`](Plugins/Citation_v.0.1.1.zip)
- [`Systematic_Review_v.0.1.7.zip`](Plugins/Systematic_Review_v.0.1.7.zip)
- [`Visual_Art_v.0.1.0.zip`](Plugins/Visual_Art_v.0.1.0.zip)

Import or load a ZIP only with a host that supports the package format you are using. The repository does not define a universal installer or runtime for these archives, so the checked-in Markdown sources are the portable, inspectable reference.

## Packaged Systems

| System | Package | Human-readable source | Scope |
|---|---|---|---|
| Construct | [`v0.9.18`](Construct/Construct_v.0.9.18.zip) | [`Prompts/Construct/`](Prompts/Construct) | General-purpose reasoning, representation, knowledge, decision, validation, and workflow architectures |
| Citation | [`v0.1.1`](Plugins/Citation_v.0.1.1.zip) | [`CT.md`](Prompts/CT.md) | Citation, reference, provenance, evidence linkage, attribution, and bibliographic integrity |
| Systematic Review | [`v0.1.7`](Plugins/Systematic_Review_v.0.1.7.zip) | [`SR.md`](Prompts/SR.md) | Systematic-review and evidence-synthesis architecture |
| Visual Art | [`v0.1.0`](Plugins/Visual_Art_v.0.1.0.zip) | [`VA.md`](Prompts/VA.md) | Visual-art practice spanning perception, conception, research, design, making, critique, exhibition, preservation, professional practice, and learning |

The package artifacts and source prompts are stored separately: ZIP distributions live under `Construct/` or `Plugins/`, while inspectable Markdown sources live under `Prompts/`.

## Source Prompt Systems

In addition to the Construct modules, the repository contains standalone source prompt systems under [`Prompts/`](Prompts):

| Code | System | Source |
|---|---|---|
| CT | Citation | [`Prompts/CT.md`](Prompts/CT.md) |
| RS | Research | [`Prompts/RS.md`](Prompts/RS.md) |
| SR | Systematic Review | [`Prompts/SR.md`](Prompts/SR.md) |
| ST | Synthesis | [`Prompts/ST.md`](Prompts/ST.md) |
| TR | Theory | [`Prompts/TR.md`](Prompts/TR.md) |
| VA | Visual Art | [`Prompts/VA.md`](Prompts/VA.md) |

Citation, Systematic Review, and Visual Art currently have corresponding versioned ZIP packages under `Plugins/`. Research, Synthesis, and Theory are currently checked in as source prompts without a corresponding ZIP artifact in this repository revision.

## Construct

Construct is the repository's reusable core prompt architecture. It is organized as standalone Markdown specifications under [`Prompts/Construct/`](Prompts/Construct), rather than executable software modules.

Each module frames a problem domain as a system: it defines key distinctions, entities and relationships, operating or evaluation models, uncertainty and evidence considerations, governance concerns, and workflows. The modules can be used independently from `Prompts/Construct/`, while the ZIP under `Construct/` provides the versioned packaged distribution.

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

`H` is not a checked-in Construct source module in this repository revision.

## Core Tools

The shorthand table below includes only mappings that correspond to paths checked into the current repository.

| Shorthand | Prompt | Function |
|---|---|---|
| A's | [Archetypes](https://github.com/1arry1iu/archetype/tree/main/GPTs) | Legacy specialist, creative-practice, workflow, perspective, and named-person archetypes |
| C | [Construct](https://github.com/1arry1iu/archetype/tree/main/Prompts/Construct) | Reusable core prompt architecture; packaged distribution is under `Construct/` |

## Categories

| Category | GPTs |
|---|---|
| [Construct core](#construct) | [Core modules](#construct-modules) |
| [Packaged systems](#packaged-systems) | [Versioned ZIP artifacts](Plugins) |
| [Source prompt systems](#source-prompt-systems) | [Citation, Research, Systematic Review, Synthesis, Theory, and Visual Art](Prompts) |
| [Legacy archetypes](#legacy-archetypes) | [Standalone archetype library](GPTs) |

## Repository Layout

```text
archetype/
├── Construct/
│   └── Construct_v.0.9.18.zip       # versioned Construct package
├── GPTs/                            # legacy standalone archetype library
├── Plugins/
│   ├── Citation_v.0.1.1.zip         # versioned Citation package
│   ├── Systematic_Review_v.0.1.7.zip# versioned Systematic Review package
│   └── Visual_Art_v.0.1.0.zip       # versioned Visual Art package
├── Prompts/
│   ├── Construct/                   # 20 Construct source modules: C-G and I-W
│   ├── CT.md                        # Citation source prompt
│   ├── RS.md                        # Research source prompt
│   ├── SR.md                        # Systematic Review source prompt
│   ├── ST.md                        # Synthesis source prompt
│   ├── TR.md                        # Theory source prompt
│   └── VA.md                        # Visual Art source prompt
├── tests/
│   └── test_readme.py               # README path/link guard
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml         # runs the README path/link guard in CI
├── A_Avatar.png
├── LICENSE                          # Apache License 2.0
└── README.md
```

## Legacy Archetypes

[`GPTs/`](GPTs) is the repository's library of standalone archetype prompts. It includes domain specialists, creative practices, specialized workflows, perspectives, and simulations of named people.

These prompts can be used independently from Construct and the packaged systems. They remain separate because they are primarily task-, perspective-, or persona-specific, while Construct is the reusable general-purpose prompt architecture.

Named-person prompts are simulations or perspective prompts, not the people represented. Inclusion in the repository is not an endorsement, and a prompt's subject label does not establish authority, factual accuracy, or evidentiary status.
