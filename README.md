# Archetype (A-18)

**Archetype** is my evolving library of LLM prompt architectures, knowledge maps, and versioned plugin and skill packages. It brings together general-purpose reasoning and knowledge-work modules, domain expertise, creative systems, and research workflows, with an emphasis on clarity, reusability, validation, and continuous improvement.

**Current inventory:** **40 Markdown prompt specifications** (19 standalone specialists and 21 Construct modules), **five knowledge maps**, and **seven versioned ZIP distributions** (six GPT plugin archives and one Grok skill archive). **A-18** identifies the Archetype knowledge architecture in [`Prompts/Construct/A.md`](Prompts/Construct/A.md); it is not a repository-wide release number. Each source architecture and plugin package has its own identifier or version.

**Contact:** [@1arry1iu on X](https://x.com/1arry1iu)

[Archetype Projects](#archetype-projects) · [Get Started](#get-started) · [Architecture](#architecture) · [Packaged Distributions](#packaged-distributions) · [Construct Modules](#construct-modules) · [Standalone Specialists](#standalone-specialists) · [Knowledge Maps](#knowledge-maps) · [Repository Layout](#repository-layout)

## Archetype Projects

Selected demo projects showcased alongside the Archetype knowledge architectures and prompt libraries.

### [Schoolside · Chiang Mai](https://schoolside-chiang-mai.greenlake32.chatgpt.site)

## Get Started

### Use a prompt specification

1. Browse the [19 standalone specialists](Prompts) or the [21 Construct modules](Prompts/Construct).
2. Open the Markdown file for the subject or capability you need, such as [Archetype (A-18)](Prompts/Construct/A.md), [Analytical Psychology](Prompts/AP.md), [Citation](Prompts/CT.md), [Systematic Review](Prompts/SR.md), or [Visual Art](Prompts/VA.md).
3. Adapt the relevant instructions, knowledge structure, and operating procedures to your model, available tools, task, and context limits.

The specifications are extensive. They should not be assumed to fit in one model context window, nor should their conceptual breadth be confused with experimentally demonstrated model performance. For focused applications, select the relevant sections or create a smaller, tested skill from the source.

### Explore a knowledge map

Read the [knowledge maps](Knowledge%20Maps) for structured learning paths and conceptual relationships across front-end, back-end, full-stack, web development, and AI-assisted coding. These educational atlases complement the specialist prompts; they are not executable software or validated proficiency assessments.

### Use a packaged plugin

Download a ZIP from [GPT Plugins/](GPT%20Plugins) or [Grok Skills/](Grok%20Skills) and follow the import process supported by your target environment. The archives include plugin metadata and skills, but compatibility depends on the target environment.

For exact contents, **inspect the ZIP itself**. The Markdown source may have changed since that release was packaged. The package inventory and compatibility caveats appear [below](#packaged-distributions).

## Architecture

Archetype distinguishes four related layers:

| Layer | Location | Contents | Role |
|---|---|---|---|
| Reusable foundations | [Prompts/Construct/](Prompts/Construct) | 21 Markdown modules | Archetypal knowledge, generative identities, reasoning, judgment, representation, inquiry, modeling, and workflows |
| Specialized knowledge | [Prompts/](Prompts) | 19 standalone Markdown specifications | Domain-specific expertise, research methods, creative disciplines, and operating procedures |
| Knowledge maps | [Knowledge Maps/](Knowledge%20Maps) | 5 Markdown atlases | Learning pathways and connections among technical concepts |
| Packaged distributions | [GPT Plugins/](GPT%20Plugins), [Grok Skills/](Grok%20Skills) | 7 versioned ZIP archives | Platform-specific snapshots; verify compatibility per archive |

**Construct** is the modular foundation: **Archetype (A-18)** maps recurring patterns, symbolic structures, and their interpretations; **Construct (C-18)** models generative identities and personas; the remaining modules cover capabilities such as Difference, Evaluation, Knowledge, Taxonomy, Validity, and Workflow. The standalone specialists extend this foundation into disciplines such as Analytical Psychology, Jurisprudence, Legal Scholarship, Neurorights, Citation, Research, Aesthetics, and software engineering.

## Packaged Distributions

The repository contains **six GPT plugin ZIPs** in [`GPT Plugins/`](GPT%20Plugins) and **one Grok skill ZIP** in [`Grok Skills/`](Grok%20Skills). These are checked-in release snapshots, not files that are automatically regenerated when a Markdown specification changes.

| Target | System | Current archive | Related Markdown sources |
|---|---|---|---|
| GPT | Analytical Psychology | [v0.1.2](GPT%20Plugins/Analytical_Psychology_v.0.1.2.zip) | [AP](Prompts/AP.md), [AAP](Prompts/AAP.md) (related specialty) |
| GPT | Citation | [v0.1.1](GPT%20Plugins/Citation_v.0.1.1.zip) | [CT](Prompts/CT.md), [RS](Prompts/RS.md) |
| GPT | Construct | [v0.9.22](GPT%20Plugins/Construct_v.0.9.22.zip) | [Construct modules](Prompts/Construct) |
| GPT | Systematic Review | [v0.1.7](GPT%20Plugins/Systematic_Review_v.0.1.7.zip) | [SR](Prompts/SR.md), [RS](Prompts/RS.md), [ST](Prompts/ST.md), [TR](Prompts/TR.md), [CT](Prompts/CT.md) |
| GPT | Visual Art | [v0.1.1](GPT%20Plugins/Visual_Art_v.0.1.1.zip) | [AT](Prompts/AT.md), [VA](Prompts/VA.md) |
| GPT | Web Development | [v1.0.17](GPT%20Plugins/Web-Development-v.1.0.17.zip) | [WD](Prompts/WD.md), [FED](Prompts/FED.md), [BED](Prompts/BED.md), [FSD](Prompts/FSD.md), [VC](Prompts/VC.md) (related specialties) |
| Grok | Construct | [v0.9.21](Grok%20Skills/Construct_Grok_v0.9.21.zip) | [Construct modules](Prompts/Construct) |

## Construct Modules

The 21 source modules of Construct live in [`Prompts/Construct/`](Prompts/Construct). Not every source module is included in the existing Construct plugin ZIP.

| Code | Module | Primary focus |
|---|---|---|
| A | [Archetype (A-18)](Prompts/Construct/A.md) | Archetypal patterns, symbolic morphologies, psychological and cultural interpretations, generative modeling, and evidence boundaries |
| C | [Construct (C-18)](Prompts/Construct/C.md) | Archetypal personas, generative identity systems, and construct design |
| D | [Difference](Prompts/Construct/D.md) | Distinction, contrast, comparison, boundaries, and meaningful non-sameness |
| E | [Evaluation](Prompts/Construct/E.md) | Evidence, measurement, causal analysis, value judgments, and metaevaluation |
| F | [Format](Prompts/Construct/F.md) | Representation, encoding, schemas, interoperability, and transformation |
| G | [Gist](Prompts/Construct/G.md) | Minimum-sufficient meaning, compression, relevance, and faithful summarization |
| I | [Information (I-18)](Prompts/Construct/I.md) | Information architecture, semantics, retrieval, provenance, and governance |
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

Construct is intended as a shared conceptual foundation, not a requirement that every specialist always invoke every module. I can use these sources separately or combine them according to the task.

## Standalone Specialists

I currently keep **19 standalone prompt specifications** at the top level of [`Prompts/`](Prompts):

| Code | Specialist | Primary focus |
|---|---|---|
| AAP | [Archetype: Analytical Psychology (AAP-18)](Prompts/AAP.md) | Focused archetypal configurations, theories, and psychological interpretation within analytical psychology |
| AP | [Analytical Psychology (AP-18)](Prompts/AP.md) | Jungian and post-Jungian psychology, psyche, symbolism, clinical theory, research, and critical validation |
| AT | [Aesthetics (AT-18)](Prompts/AT.md) | Aesthetic experience, perception, interpretation, value, judgment, and creation |
| BED | [Back-End Development (BED-18)](Prompts/BED.md) | Server systems, state transitions, security, distributed architecture, reliability, and operations |
| CN | [Chinese (CN-18)](Prompts/CN.md) | Chinese languages, linguistic history, scripts, dialectology, and computational language research |
| CT | [Citation](Prompts/CT.md) | Bibliographic identity, attribution, claim–evidence alignment, verification, and provenance |
| FED | [Front-End Development (FED-18)](Prompts/FED.md) | Browser interfaces, interaction, accessibility, performance, and frontend engineering |
| FSD | [Full-Stack Development (FSD-18)](Prompts/FSD.md) | Integrated frontend, backend, data, security, deployment, and AI-native engineering |
| JRP | [Jurisprudence](Prompts/JRP.md) | Philosophy of law, legal concepts, authority, interpretation, and normative analysis |
| LS | [Legal Scholarship](Prompts/LS.md) | Legal research, doctrinal and comparative analysis, empirical inquiry, and scholarly argument |
| NRR | [Neurorights](Prompts/NRR.md) | Neurotechnology, mental autonomy, privacy, integrity, rights, and governance |
| RS | [Research](Prompts/RS.md) | Research questions, methods, evidence, analysis, validation, and reproducibility |
| SR | [Systematic Review](Prompts/SR.md) | Protocols, searching, screening, extraction, appraisal, synthesis, and review reporting |
| ST | [Synthesis](Prompts/ST.md) | Integration of heterogeneous evidence, findings, models, and perspectives |
| TH | [Thai (TH-18)](Prompts/TH.md) | Thai language and linguistics, language variation, historical study, and computational modeling |
| TR | [Theory](Prompts/TR.md) | Concepts, explanations, mechanisms, predictions, theory testing, and revision |
| VA | [Visual Art](Prompts/VA.md) | Visual language, artistic inquiry, studio practice, critique, and artistic development |
| VC | [Vibe Coding (VC-18)](Prompts/VC.md) | AI-assisted and agentic software engineering, specifications, verification, and governance |
| WD | [Web Development](Prompts/WD.md) | Web architecture, frontend and backend systems, data, security, testing, and operations |

Not every standalone specialist has a ZIP counterpart in this repository. A specialist's presence here also does not necessarily imply that a plugin with that name is currently installed or published elsewhere.

## Knowledge Maps

Five educational knowledge maps are available in [`Knowledge Maps/`](Knowledge%20Maps). They are complementary reference atlases, not additional prompt specifications.

| Map | Focus |
|---|---|
| [Back-End Development](Knowledge%20Maps/backend-development-knowledge-map.md) | APIs, state, persistence, distributed systems, security, and reliability |
| [Front-End Development](Knowledge%20Maps/front-end-development-knowledge-map.md) | Browser fundamentals, interface architecture, accessibility, quality, and delivery |
| [Full-Stack Development](Knowledge%20Maps/full-stack-development-knowledge-map.md) | End-to-end web systems, architectural dependencies, and engineering capability |
| [Vibe Coding](Knowledge%20Maps/vibe-coding-knowledge-map.md) | AI-assisted coding, agentic workflows, verification, and operational responsibility |
| [Web Development](Knowledge%20Maps/web-development-knowledge-map.md) | Web platform concepts, cross-domain connections, and learning journeys |

## Repository Layout

```text
archetype/
├── Prompts/
│   ├── Construct/                     # 21 reusable Markdown modules: A, C, D, ... W
│   │   ├── A.md                       # Archetype (A-18)
│   │   ├── C.md                       # Construct (C-18)
│   │   └── ...                        # Other Construct modules
│   ├── AAP.md                         # Archetype: Analytical Psychology
│   ├── AP.md                          # Analytical Psychology
│   ├── AT.md                          # Aesthetics
│   ├── BED.md                         # Back-End Development
│   ├── CN.md                          # Chinese
│   ├── CT.md                          # Citation
│   ├── FED.md                         # Front-End Development
│   ├── FSD.md                         # Full-Stack Development
│   ├── JRP.md                         # Jurisprudence
│   ├── LS.md                          # Legal Scholarship
│   ├── NRR.md                         # Neurorights
│   ├── RS.md                          # Research
│   ├── SR.md                          # Systematic Review
│   ├── ST.md                          # Synthesis
│   ├── TH.md                          # Thai
│   ├── TR.md                          # Theory
│   ├── VA.md                          # Visual Art
│   ├── VC.md                          # Vibe Coding
│   └── WD.md                          # Web Development
├── Knowledge Maps/                    # 5 technical learning atlases
│   ├── backend-development-knowledge-map.md
│   ├── front-end-development-knowledge-map.md
│   ├── full-stack-development-knowledge-map.md
│   ├── vibe-coding-knowledge-map.md
│   └── web-development-knowledge-map.md
├── GPT Plugins/                       # 6 versioned GPT plugin ZIPs
│   ├── Analytical_Psychology_v.0.1.2.zip
│   ├── Citation_v.0.1.1.zip
│   ├── Construct_v.0.9.22.zip
│   ├── Systematic_Review_v.0.1.7.zip
│   ├── Visual_Art_v.0.1.1.zip
│   └── Web-Development-v.1.0.17.zip
├── Grok Skills/                       # 1 versioned Grok skill ZIP
│   └── Construct_Grok_v0.9.21.zip
├── tests/
│   └── test_readme.py                 # README local-link and anchor check
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml          # Runs README validation on push and PR
├── A_Avatar.png
├── LICENSE                            # Apache License 2.0
└── README.md
```

Run `python tests/test_readme.py` locally to check README paths and anchors. GitHub Actions runs the same check on pushes and pull requests. This is a documentation check, not a verification of plugin ZIP contents or runtime compatibility.

![Archetype avatar](A_Avatar.png)
