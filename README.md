# Archetype (A-16)

**Archetype** is a repository of inspectable prompt architectures, packaged prompt systems, legacy GPT archetypes, and small prompt utilities.

The reusable core is **Construct**: a set of 20 Markdown prompt specifications for construct design, comparison, evaluation, information and knowledge work, judgment, modeling, learning, prioritization, validation, workflow design, and related tasks. Its current packaged distribution is [`Construct v0.9.18`](Construct/Construct_v.0.9.18.zip).

The repository also has a separate [`Plugins/`](Plugins) area for domain-specific packaged systems. The first checked-in domain package is [`Visual Art v0.1.0`](Plugins/Visual%20Art/Visual_Art_v.0.1.0.zip), with its human-readable source at [`VA.md`](Plugins/Visual%20Art/Prompts/VA.md).

[Get Started](#get-started) · [Packaged Systems](#packaged-systems) · [Construct](#construct) · [Modules](#construct-modules) · [Legacy Archetypes](#legacy-archetypes) · [Utilities](#core-tools) · [Repository Layout](#repository-layout)

## Get Started

This repository is primarily Markdown prompt specifications plus packaged ZIP artifacts. There is no repository-wide build or install command.

### Use the source prompts directly

- For the reusable core, choose a module from [`Construct/Prompts/`](Construct/Prompts).
- For Visual Art, use [`Plugins/Visual Art/Prompts/VA.md`](Plugins/Visual%20Art/Prompts/VA.md).
- For older standalone archetypes, browse [`GPTs/`](GPTs).
- For compact utilities, see [`Block/B`](Block/B) and [`Hack/CONN.md`](Hack/CONN.md).

Supply the selected prompt to the LLM/GPT environment you use in the way that environment accepts system, custom-instruction, or prompt content.

### Use a packaged artifact

The repository currently contains two versioned ZIP artifacts:

- [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip)
- [`Visual_Art_v.0.1.0.zip`](Plugins/Visual%20Art/Visual_Art_v.0.1.0.zip)

Import or load a ZIP only with a host that supports the package format you are using. The repository does not define a universal installer or runtime for these archives, so the checked-in Markdown sources are the portable, inspectable reference.

## Packaged Systems

| System | Package | Human-readable source | Scope |
|---|---|---|---|
| Construct | [`v0.9.18`](Construct/Construct_v.0.9.18.zip) | [`Construct/Prompts/`](Construct/Prompts) | General-purpose reasoning, representation, knowledge, decision, validation, and workflow architectures |
| Visual Art | [`v0.1.0`](Plugins/Visual%20Art/Visual_Art_v.0.1.0.zip) | [`VA.md`](Plugins/Visual%20Art/Prompts/VA.md) | Visual-art practice spanning perception, conception, research, design, making, critique, exhibition, preservation, professional practice, and learning |

The package directories pair versioned distribution artifacts with checked-in source prompts so the prompt architecture can be inspected independently of the ZIP.

## Construct

Construct is the repository's reusable core prompt architecture. It is organized as standalone Markdown specifications rather than executable software modules.

Each module frames a problem domain as a system: it defines key distinctions, entities and relationships, operating or evaluation models, uncertainty and evidence considerations, governance concerns, and workflows. The modules can be used independently from `Construct/Prompts/`, while the ZIP provides the versioned packaged distribution.

### Design intent

- **Reusable core:** the modules cover general reasoning and workflow primitives rather than a single task or persona.
- **Inspectable sources:** every checked-in core module is readable as Markdown.
- **Independent or combined use:** a module can be used directly, or the packaged Construct artifact can be used where supported.
- **Explicit boundaries:** the prompts repeatedly distinguish neighboring concepts instead of treating them as interchangeable.
- **Evidence and governance:** many modules include provenance, uncertainty, validation, monitoring, or governance as first-class concerns.

## Construct Modules

| Code | Module | Primary focus |
|---|---|---|
| C | [Construct](Construct/Prompts/C.md) | Archetypal personas, generative identity systems, and construct design |
| D | [Difference](Construct/Prompts/D.md) | Distinction, contrast, comparison, boundaries, and meaningful non-sameness |
| E | [Evaluation](Construct/Prompts/E.md) | Evidence, measurement, causal analysis, value judgments, and metaevaluation |
| F | [Format](Construct/Prompts/F.md) | Representation, encoding, schemas, interoperability, and transformation |
| G | [Gist](Construct/Prompts/G.md) | Minimum-sufficient meaning, compression, relevance, and faithful summarization |
| I | [Information](Construct/Prompts/I.md) | Information architecture, semantics, retrieval, provenance, and governance |
| J | [Judgement](Construct/Prompts/J.md) | Disciplined assessment, uncertainty, calibration, and decision support |
| K | [Knowledge](Construct/Prompts/K.md) | Knowledge frontiers, evidence, synthesis, exploration, and revision |
| L | [Learning](Construct/Prompts/L.md) | Learning science, memory, skill acquisition, transfer, and metacognition |
| M | [Model](Construct/Prompts/M.md) | Abstraction, formalization, simulation, validation, and model evolution |
| N | [Name](Construct/Prompts/N.md) | Naming, terminology, identifiers, namespaces, and nomenclature |
| O | [Openness](Construct/Prompts/O.md) | Access, transparency, interoperability, commons, licensing, and governance |
| P | [Priority](Construct/Prompts/P.md) | Prioritization, allocation, sequencing, triage, and portfolio decisions |
| Q | [Question](Construct/Prompts/Q.md) | Inquiry, information seeking, diagnosis, sequencing, and question quality |
| R | [Ranking](Construct/Prompts/R.md) | Comparative judgment, scoring, ordering, selection, and ranking governance |
| S | [Similarity](Construct/Prompts/S.md) | Resemblance, equivalence, correspondence, matching, and justified likeness |
| T | [Taxonomy](Construct/Prompts/T.md) | Classification, terminology, semantic structure, and knowledge organization |
| U | [Uniqueness](Construct/Prompts/U.md) | Identity, rarity, originality, discriminability, and provenance |
| V | [Validity](Construct/Prompts/V.md) | Verification, validation, evidence, assurance, and warranted reliance |
| W | [Workflow](Construct/Prompts/W.md) | Workflow discovery, orchestration, execution, observability, and optimization |

`H` is not a Construct source module; the repository's older `H` shorthand points to the Connotation utility under `Hack/`.

## Core Tools

The older shorthand is retained where it still maps cleanly to the current repository.

| Shorthand | Prompt | Function |
|---|---|---|
| A's | [Archetypes](https://github.com/1arry1iu/archetype/tree/main/GPTs) | Legacy specialist, creative-practice, workflow, and named-person archetypes |
| B | [Block](https://github.com/1arry1iu/archetype/blob/main/Block/B) | Generate ten relevance-ranked factors for a construct in compact bracket notation |
| C | [Construct](https://github.com/1arry1iu/archetype/tree/main/Construct) | Reusable core prompt architecture plus its packaged distribution |
| H | [Connotation](https://github.com/1arry1iu/archetype/blob/main/Hack/CONN.md) | Convert a construct into ten relevance-ranked verb/meaning entries |

## Categories

| Category | GPTs |
|---|---|
| [Construct core](#construct) | [Core modules](#construct-modules) |
| [Packaged systems](#packaged-systems) | [Construct and Visual Art](Plugins) |
| [Legacy archetypes](#legacy-archetypes) | [Specialists, creative practices, workflows, and named-person simulations](GPTs) |
| [Utilities](#core-tools) | [Block and Connotation](#core-tools) |

## Repository Layout

```text
archetype/
├── Construct/
│   ├── Construct_v.0.9.18.zip       # versioned Construct package
│   └── Prompts/                     # 20 source modules: C-G and I-W
├── Plugins/
│   └── Visual Art/
│       ├── Visual_Art_v.0.1.0.zip   # versioned Visual Art package
│       └── Prompts/
│           └── VA.md                # Visual Art source prompt
├── GPTs/                            # legacy standalone archetype library
├── Block/
│   └── B                            # ten-factor block generator
├── Hack/
│   └── CONN.md                      # construct-to-verbs Connotation utility
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
