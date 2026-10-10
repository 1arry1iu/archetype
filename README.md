# Archetype (A-18)

**Archetype** is my working library of GPT prompts and the place where I am progressively developing those prompts into GPT plugins.

I originally built this repository as a collection of standalone GPT prompt architectures: domain experts, creative practices, research systems, reasoning frameworks, personas, workflows, and other specialized archetypes. I am now updating selected prompts into more structured, inspectable, and reusable plugin packages while keeping the underlying prompt sources available in Markdown.

The current repository contains 32 Markdown prompt specifications and four versioned plugin packages:

- [`Prompts/`](Prompts) contains 12 standalone prompt specifications and the 20 modules in [`Prompts/Construct/`](Prompts/Construct).
- [`Plugins/`](Plugins) contains packaged GPT plugins that I have already started producing from selected prompts.
- [`Construct/`](Construct) contains my reusable Construct package and its underlying modules live in [`Prompts/Construct/`](Prompts/Construct).

I am treating this as an ongoing migration rather than a completed conversion. Not every GPT prompt has a plugin counterpart yet, and the prompt sources remain useful on their own.

[Get Started](#get-started) · [Repository Evolution](#repository-evolution) · [Packaged Systems](#packaged-systems) · [Construct](#construct) · [Construct Modules](#construct-modules) · [Standalone Prompts](#standalone-prompts) · [Repository Layout](#repository-layout) · [License](#license)

## Get Started

I keep the repository intentionally inspectable. Most of the source material is plain Markdown, while the plugin distributions are versioned ZIP artifacts.

### Use my GPT prompts directly

If you want to work with the prompt sources themselves:

- Browse the current prompt library in [`Prompts/`](Prompts).
- Use my Construct modules from [`Prompts/Construct/`](Prompts/Construct).
- Use Citation from [`Prompts/CT.md`](Prompts/CT.md).
- Use Systematic Review from [`Prompts/SR.md`](Prompts/SR.md).
- Use Visual Art from [`Prompts/VA.md`](Prompts/VA.md).
- Browse additional standalone prompt specifications under [`Prompts/`](Prompts).

I use these Markdown files as the human-readable source layer. They can be supplied directly to an LLM or GPT environment wherever system prompts, custom instructions, or equivalent prompt content are supported.

### Use a packaged GPT plugin

I currently maintain four versioned packaged systems:

- [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip)
- [`Citation_v.0.1.1.zip`](Plugins/Citation_v.0.1.1.zip)
- [`Systematic_Review_v.0.1.7.zip`](Plugins/Systematic_Review_v.0.1.7.zip)
- [`Visual_Art_v.0.1.0.zip`](Plugins/Visual_Art_v.0.1.0.zip)

I am using these packages as the next stage of the project: moving selected GPT prompts from standalone instructions into reusable GPT plugin form. Download the ZIP for the system you want and use the import or installation process supported by your plugin environment. To inspect a package, extract it and read its `plugin.json` manifest and `skills/` directory.

The Markdown sources describe the evolving prompt architectures. A versioned ZIP is a separate release snapshot, so inspect the files inside that archive when you need to know exactly what a package contains.

## Repository Evolution

Archetype began as a broader collection of GPT prompt architectures. The current tree focuses on two maintained forms:

1. **Prompt sources** — standalone specifications and reusable Construct modules under [`Prompts/`](Prompts).
2. **Packaged plugins** — versioned distributions under [`Plugins/`](Plugins) and [`Construct/`](Construct).

I do not expect these forms to move in lockstep. Some prompts may remain useful as standalone instructions, while others progress into packaged plugins. Earlier repository states remain available through Git history.

My aim is to preserve the strengths of the prompt library while making the systems I continue developing easier to inspect, version, reuse, test, and package.

## Packaged Systems

These are the systems I have packaged so far:

| System | Package | Related prompt sources | Scope |
|---|---|---|---|
| Construct | [`v0.9.18`](Construct/Construct_v.0.9.18.zip) | [`Prompts/Construct/`](Prompts/Construct) | General-purpose reasoning, representation, knowledge, decision, validation, and workflow architectures |
| Citation | [`v0.1.1`](Plugins/Citation_v.0.1.1.zip) | [`CT.md`](Prompts/CT.md), [`RS.md`](Prompts/RS.md) | Citation and research skills for scholarly reference, evidence linkage, attribution, provenance, verification, and research methods |
| Systematic Review | [`v0.1.7`](Plugins/Systematic_Review_v.0.1.7.zip) | [`SR.md`](Prompts/SR.md), [`RS.md`](Prompts/RS.md), [`ST.md`](Prompts/ST.md), [`TR.md`](Prompts/TR.md), [`CT.md`](Prompts/CT.md) | Systematic review, research, synthesis, theory, and citation skills for evidence workflows, appraisal, reporting, reproducibility, and updating |
| Visual Art | [`v0.1.0`](Plugins/Visual_Art_v.0.1.0.zip) | [`VA.md`](Prompts/VA.md) | Visual-art practice spanning perception, conception, research, design, making, critique, exhibition, preservation, professional practice, and learning |

I expect this section to grow as I convert more of the prompt library into plugin packages.

## Construct

**Construct** is my reusable core prompt architecture. I designed it as a set of general-purpose modules for reasoning, representation, knowledge work, judgment, modeling, learning, prioritization, validation, workflow design, and related tasks.

I keep the 20 source modules as standalone Markdown specifications under [`Prompts/Construct/`](Prompts/Construct), and I maintain a versioned packaged distribution at [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip).

I use Construct as a shared conceptual foundation rather than as a single persona or task prompt. Each module defines a problem domain through distinctions, entities, relationships, operating models, evidence, uncertainty, governance, and workflow considerations.

### Design intent

- **Reusable core:** I use the modules for general reasoning and workflow primitives rather than a single domain or persona.
- **Inspectable sources:** I keep every core module readable as Markdown.
- **Independent or combined use:** I can use a module directly or package the system for environments that support it.
- **Explicit boundaries:** I define neighboring concepts separately instead of treating them as interchangeable.
- **Evidence and governance:** I treat provenance, uncertainty, validation, monitoring, and governance as first-class concerns where they matter.

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

I keep 12 standalone prompt specifications at the top level of [`Prompts/`](Prompts):

| Code | Prompt | Primary focus |
|---|---|---|
| AT | [Aesthetics](Prompts/AT.md) | Aesthetic experience, perception, interpretation, value, judgment, and creation |
| CT | [Citation](Prompts/CT.md) | Bibliographic identity, attribution, claim–evidence alignment, verification, and provenance |
| FED | [Front-End Development](Prompts/FED.md) | Browser interfaces, interaction, accessibility, performance, and frontend engineering |
| JRP | [Jurisprudence](Prompts/JRP.md) | Philosophy of law, legal concepts, authority, interpretation, and normative analysis |
| LS | [Legal Scholarship](Prompts/LS.md) | Legal research, doctrinal and comparative analysis, empirical inquiry, and scholarly argument |
| NRR | [Neurorights](Prompts/NRR.md) | Neurotechnology, mental autonomy, privacy, integrity, rights, and governance |
| RS | [Research](Prompts/RS.md) | Research questions, methods, evidence, analysis, validation, and reproducibility |
| SR | [Systematic Review](Prompts/SR.md) | Protocols, searching, screening, extraction, appraisal, synthesis, and review reporting |
| ST | [Synthesis](Prompts/ST.md) | Integration of heterogeneous evidence, findings, models, and perspectives |
| TR | [Theory](Prompts/TR.md) | Concepts, explanations, mechanisms, predictions, theory testing, and revision |
| VA | [Visual Art](Prompts/VA.md) | Visual language, artistic inquiry, studio practice, critique, and artistic development |
| WD | [Web Development](Prompts/WD.md) | Web architecture, frontend and backend systems, data, security, testing, and operations |

Some of these are already connected to packaged plugins, while others are still part of the source-side development process.

## Repository Layout

```text
archetype/
├── Prompts/                         # source prompts I am organizing and evolving
│   ├── Construct/                   # 20 reusable Construct source modules
│   ├── AT.md                        # Aesthetics
│   ├── CT.md                        # Citation source
│   ├── FED.md                       # Front-End Development
│   ├── JRP.md                       # Jurisprudence
│   ├── LS.md                        # Legal Scholarship
│   ├── NRR.md                       # Neurorights
│   ├── RS.md                        # Research
│   ├── SR.md                        # Systematic Review source
│   ├── ST.md                        # Synthesis
│   ├── TR.md                        # Theory
│   ├── VA.md                        # Visual Art source
│   └── WD.md                        # Web Development
├── Plugins/                         # packaged GPT plugins
│   ├── Citation_v.0.1.1.zip
│   ├── Systematic_Review_v.0.1.7.zip
│   └── Visual_Art_v.0.1.0.zip
├── Construct/
│   └── Construct_v.0.9.18.zip        # packaged reusable core
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

## Direction

I am continuing to refine the prompt library and convert selected systems into GPT plugins. As I do that, I want the repository to preserve three things at once: the breadth of the original GPT prompts, the inspectability of their Markdown sources, and the versioned structure of the newer plugin packages.

The repository is an active development space for prompt sources and the plugin systems growing out of them.

## License

This repository is licensed under the [Apache License 2.0](LICENSE).

![Archetype avatar](A_Avatar.png)
