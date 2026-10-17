# Archetype (A-19)

**Archetype** is an evolving library of LLM prompt architectures, reusable reasoning modules, specialist knowledge systems, and versioned plugin and skill archives. It brings together domain expertise, research methods, creative work, and software engineering with an emphasis on conceptual precision, reuse, validation, and continuous improvement.

**Current repository inventory:** **42 Markdown specifications** (21 standalone specialists and 21 Construct modules) and **15 checked-in ZIP files** (seven topic archives in `blocks/`, seven GPT-named archives in `gpt/`, and one Grok archive in `grok/`). The previously documented five knowledge maps are **not present** on the current `main` branch.

**Contact:** [@1arry1iu on X](https://x.com/1arry1iu)

[Archetype Projects](#archetype-projects) · [Get Started](#get-started) · [Architecture](#architecture) · [Packaged Distributions](#packaged-distributions) · [Construct Modules](#construct-modules) · [Standalone Specialists](#standalone-specialists) · [Repository Layout](#repository-layout) · [Validation](#validation)

## Archetype Projects

Selected demo projects showcased alongside the Archetype knowledge architectures and prompt libraries.

- [Schoolside · Chiang Mai](https://schoolside-chiang-mai.greenlake32.chatgpt.site)
- [Thailand Fieldguide](https://thailand-fieldguide.greenlake32.chatgpt.site/)
- [远见 · Atlas](https://yuanjian-atlas.greenlake32.chatgpt.site/)
- [Little Days · Chiang Mai](https://little-days-chiang-mai.greenlake32.chatgpt.site/)
- [Pause · Chiang Mai](https://pause-chiang-mai.greenlake32.chatgpt.site/)

## Get Started

### Use a prompt specification

1. Browse the [standalone specialists](blocks) or [Construct modules](blocks/Construct).
2. Open a Markdown source such as [Archetype](blocks/Construct/A.md), [Analytical Psychology](blocks/AP.md), [Citation](blocks/CT.md), [Research](blocks/RS.md), or [Visual Art](blocks/VA.md).
3. Extract and adapt the relevant knowledge, instructions, and protocols to the target model, tools, task, and context window.

These specifications can be very long. Conceptual breadth **does not demonstrate model performance**. For focused applications, use a compact, task-specific subset and evaluate it on representative tasks.

### Use a packaged archive

The [`gpt/`](gpt), [`grok/`](grok), and [`blocks/`](blocks) directories contain checked-in ZIP archives. These are snapshots, not automatically regenerated when Markdown sources change. Check each archive's contents, integrity, and target-platform import requirements before installation. A file's presence or size alone does not establish ZIP integrity or target-platform compatibility.

## Architecture

| Layer | Location | Contents | Purpose |
|---|---|---|---|
| Reusable foundations | [`blocks/Construct/`](blocks/Construct) | 21 Markdown modules | Archetypes, knowledge, judgment, modeling, validation, and workflows |
| Standalone specialists | [`blocks/`](blocks) | 21 Markdown modules | Discipline-specific concepts, research methods, and operational approaches |
| Checked-in archives | [`blocks/`](blocks), [`gpt/`](gpt), [`grok/`](grok) | 15 ZIP files | Topic collections and distribution snapshots; compatibility varies |

Construct supplies shared conceptual foundations. **Archetype (A-18)** examines patterns and symbolic structures, while **Construct (C-18)** explores generative identities and personas. Specialists extend these foundations into fields such as psychology, anthropology, law, research, aesthetics, and software engineering.

## Packaged Distributions

Archive versions below are taken from filenames. Listing a file does **not** certify that it is importable, current, complete, or tested.

### GPT archives

| System | Tracked archive | Status |
|---|---|---|
| Analytical Psychology V.0.1.2.zip | [`analytical_psychology_v.0.1.2.zip`](gpt/analytical_psychology_v.0.1.2.zip) | Snapshot; contents and runtime compatibility not independently verified |
| Cinematic Creativity | [`Cinematic_Creativity_v.0.1.3.zip`](gpt/Cinematic_Creativity_v.0.1.3.zip) | Checked in (5,352,028 bytes); archive contents and runtime compatibility not independently verified |
| Citation V.0.1.1.zip | [`citation_v.0.1.1.zip`](gpt/citation_v.0.1.1.zip) | Snapshot; contents and runtime compatibility not independently verified |
| Construct V.0.9.23.zip | [`construct_v.0.9.23.zip`](gpt/construct_v.0.9.23.zip) | Snapshot; contents and runtime compatibility not independently verified |
| Systematic Review V.0.1.7.zip | [`systematic_review_v.0.1.7.zip`](gpt/systematic_review_v.0.1.7.zip) | Snapshot; contents and runtime compatibility not independently verified |
| Visual Art V.0.1.1.zip | [`visual_art_v.0.1.1.zip`](gpt/visual_art_v.0.1.1.zip) | Snapshot; contents and runtime compatibility not independently verified |
| Web Development V.1.0.20.zip | [`web_development_v.1.0.20.zip`](gpt/web_development_v.1.0.20.zip) | Snapshot; contents and runtime compatibility not independently verified |

### Grok archive

| System | Tracked archive | Status |
|---|---|---|
| Construct Grok | [`construct_grok_v0.9.21.zip`](grok/construct_grok_v0.9.21.zip) | Snapshot; contents and runtime compatibility not independently verified |

### Topic archives in blocks

| Subject | Tracked archive |
|---|---|
| Artificial Intelligence | [`artificial_intelligence.zip`](blocks/artificial_intelligence.zip) |
| Cinematic Creativity | [`cinematic_creativity.zip`](blocks/cinematic_creativity.zip) |
| Creativity | [`creativity.zip`](blocks/creativity.zip) |
| Digital Storytelling | [`digital_storytelling.zip`](blocks/digital_storytelling.zip) |
| Filmmaking | [`filmmaking.zip`](blocks/filmmaking.zip) |
| Research | [`research.zip`](blocks/research.zip) |
| Systematic Review | [`systematic_review.zip`](blocks/systematic_review.zip) |

**Archive integrity:** The [Cinematic Creativity GPT archive](gpt/Cinematic_Creativity_v.0.1.3.zip) replaces the former 2-byte placeholder and is now tracked at 5,352,028 bytes. The new archive's internal integrity and import compatibility have **not** been independently verified. Other archives are likewise inventoried by path and size rather than fully tested.

## Construct Modules

All 21 reusable source modules live in [`blocks/Construct/`](blocks/Construct). A Construct archive need not include every current source module.

| Code | Module | Primary focus |
|---|---|---|
| A | [Archetype (A-18)](blocks/Construct/A.md) | Archetypal patterns, symbolic morphologies, psychological and cultural interpretations, generative modeling, and evidence boundaries |
| C | [Construct (C-18)](blocks/Construct/C.md) | Archetypal personas, generative identity systems, and construct design |
| D | [Difference](blocks/Construct/D.md) | Distinction, contrast, comparison, boundaries, and meaningful non-sameness |
| E | [Evaluation](blocks/Construct/E.md) | Evidence, measurement, causal analysis, value judgments, and metaevaluation |
| F | [Format](blocks/Construct/F.md) | Representation, encoding, schemas, interoperability, and transformation |
| G | [Gist](blocks/Construct/G.md) | Minimum-sufficient meaning, compression, relevance, and faithful summarization |
| I | [Information (I-18)](blocks/Construct/I.md) | Information architecture, semantics, retrieval, provenance, and governance |
| J | [Judgement](blocks/Construct/J.md) | Disciplined assessment, uncertainty, calibration, and decision support |
| K | [Knowledge](blocks/Construct/K.md) | Knowledge frontiers, evidence, synthesis, exploration, and revision |
| L | [Learning](blocks/Construct/L.md) | Learning science, memory, skill acquisition, transfer, and metacognition |
| M | [Model](blocks/Construct/M.md) | Abstraction, formalization, simulation, validation, and model evolution |
| N | [Name](blocks/Construct/N.md) | Naming, terminology, identifiers, namespaces, and nomenclature |
| O | [Openness](blocks/Construct/O.md) | Access, transparency, interoperability, commons, licensing, and governance |
| P | [Priority](blocks/Construct/P.md) | Prioritization, allocation, sequencing, triage, and portfolio decisions |
| Q | [Question](blocks/Construct/Q.md) | Inquiry, information seeking, diagnosis, sequencing, and question quality |
| R | [Ranking](blocks/Construct/R.md) | Comparative judgment, scoring, ordering, selection, and ranking governance |
| S | [Similarity](blocks/Construct/S.md) | Resemblance, equivalence, correspondence, matching, and justified likeness |
| T | [Taxonomy](blocks/Construct/T.md) | Classification, terminology, semantic structure, and knowledge organization |
| U | [Uniqueness](blocks/Construct/U.md) | Identity, rarity, originality, discriminability, and provenance |
| V | [Validity](blocks/Construct/V.md) | Verification, validation, evidence, assurance, and warranted reliance |
| W | [Workflow](blocks/Construct/W.md) | Workflow discovery, orchestration, execution, observability, and optimization |

These modules may be used independently or combined when the task warrants it.

## Standalone Specialists

The 21 standalone source specifications live directly in [`blocks/`](blocks).

| Code | Specialist | Primary focus |
|---|---|---|
| AAP | [Archetype: Analytical Psychology (AAP-18)](blocks/AAP.md) | Focused archetypal configurations, theories, and psychological interpretation within analytical psychology |
| ANT | [Anthropology (ANT-18)](blocks/ANT.md) | Human evolution, cultures, archaeology, languages, and societies |
| AP | [Analytical Psychology (AP-18)](blocks/AP.md) | Jungian and post-Jungian psychology, psyche, symbolism, clinical theory, research, and critical validation |
| AT | [Aesthetics (AT-18)](blocks/AT.md) | Aesthetic experience, perception, interpretation, value, judgment, and creation |
| BED | [Back-End Development (BED-18)](blocks/BED.md) | Server systems, state transitions, security, distributed architecture, reliability, and operations |
| CN | [Chinese (CN-18)](blocks/CN.md) | Chinese languages, linguistic history, scripts, dialectology, and computational language research |
| CT | [Citation](blocks/CT.md) | Bibliographic identity, attribution, claim–evidence alignment, verification, and provenance |
| ETH | [Ethnography (ETH-18)](blocks/ETH.md) | Ethnographic methods, cultural interpretation, fieldwork, and research ethics |
| FED | [Front-End Development (FED-18)](blocks/FED.md) | Browser interfaces, interaction, accessibility, performance, and frontend engineering |
| FSD | [Full-Stack Development (FSD-18)](blocks/FSD.md) | Integrated frontend, backend, data, security, deployment, and AI-native engineering |
| JRP | [Jurisprudence](blocks/JRP.md) | Philosophy of law, legal concepts, authority, interpretation, and normative analysis |
| LS | [Legal Scholarship](blocks/LS.md) | Legal research, doctrinal and comparative analysis, empirical inquiry, and scholarly argument |
| NRR | [Neurorights](blocks/NRR.md) | Neurotechnology, mental autonomy, privacy, integrity, rights, and governance |
| OB | [Observation (OB-18)](blocks/OB.md) | Perception, observation, measurement, evidence, and validation |
| RS | [Research](blocks/RS.md) | Research questions, methods, evidence, analysis, validation, and reproducibility |
| ST | [Synthesis](blocks/ST.md) | Integration of heterogeneous evidence, findings, models, and perspectives |
| TH | [Thai (TH-18)](blocks/TH.md) | Thai language and linguistics, language variation, historical study, and computational modeling |
| TR | [Theory](blocks/TR.md) | Concepts, explanations, mechanisms, predictions, theory testing, and revision |
| VA | [Visual Art](blocks/VA.md) | Visual language, artistic inquiry, studio practice, critique, and artistic development |
| VC | [Vibe Coding (VC-18)](blocks/VC.md) | AI-assisted and agentic software engineering, specifications, verification, and governance |
| WD | [Web Development](blocks/WD.md) | Web architecture, frontend and backend systems, data, security, testing, and operations |

A source specialist does not necessarily have a corresponding installed or published plugin. The historical `SR.md` reference is not present on the current branch; systematic-review material is available as archived packages listed above.

## Repository Layout

```text
archetype/
├── blocks/
│   ├── Construct/                    # 21 reusable Markdown modules
│   ├── *.md                          # 21 standalone specialists
│   └── *.zip                         # 7 topic archives
├── gpt/                              # 7 checked-in GPT archives
├── grok/                             # 1 archive
├── tests/test_readme.py              # README path and anchor check
├── .github/workflows/readme-check.yml
├── .github/FUNDING.yml
├── A_Avatar.png
├── LICENSE                           # Apache License 2.0
└── README.md
```

The former `Prompts/`, `GPT Plugins/`, `Grok Skills/`, and `Knowledge Maps/` directories are not in the current repository tree.

## Validation

Run `python tests/test_readme.py` to check local links and anchors in this README. [GitHub Actions](.github/workflows/readme-check.yml) runs the same validator on pushes and pull requests. This documentation test **does not** verify archive integrity, packaged source completeness, plugin compatibility, or AI-model performance.

![Archetype avatar](A_Avatar.png)
