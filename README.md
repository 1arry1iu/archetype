# Archetype (A-18)

**Archetype** is my evolving library of GPT prompt architectures and specialist plugin packages. It brings together general-purpose reasoning and knowledge-work modules, domain expertise, creative systems, and research workflows, with an emphasis on clarity, reusability, validation, and continuous improvement.

I maintain the **Markdown specifications as inspectable source material** and progressively package selected systems as GPT plugins. The conversion is ongoing: a source specification does not necessarily have a corresponding plugin, and an existing plugin ZIP is a versioned snapshot rather than an automatically synchronized build.

**Current inventory:** **33 Markdown specifications** (13 standalone specialists and 20 Construct modules) and **four versioned plugin ZIPs**. The label **A-18** identifies this repository's conceptual architecture; it is not the version number of every included prompt or plugin.

[Get Started](#get-started) · [Architecture](#architecture) · [Plugin Packages](#plugin-packages) · [Construct Modules](#construct-modules) · [Standalone Specialists](#standalone-specialists) · [Validation](#validation-and-quality) · [Roadmap](#development-roadmap) · [Repository Layout](#repository-layout) · [License](#license)

## Get Started

### Use a prompt specification

1. Browse the [standalone specialists](Prompts) or the [20 Construct modules](Prompts/Construct).
2. Open the Markdown file for the subject or capability you need, such as [Analytical Psychology](Prompts/AP.md), [Citation](Prompts/CT.md), [Systematic Review](Prompts/SR.md), or [Visual Art](Prompts/VA.md).
3. Adapt the relevant instructions, knowledge structure, and operating procedures to your model, available tools, task, and context limits.

The specifications are extensive. They should not be assumed to fit in one model context window, nor should their conceptual breadth be confused with experimentally demonstrated model performance. For focused applications, select the relevant sections or create a smaller, tested skill from the source.

### Use a packaged plugin

Download a ZIP from [Plugins/](Plugins) and follow the import process supported by your plugin environment. The archives include plugin metadata and skills, but compatibility depends on the target environment.

For exact contents, **inspect the ZIP itself**. The Markdown source may have changed since that release was packaged. The package inventory and compatibility caveats appear [below](#plugin-packages).

### Check documentation links locally

```bash
python tests/test_readme.py
```

This is the repository's existing README-link check. It is **not** a complete plugin, prompt, or model-behavior test suite.

## Architecture

Archetype distinguishes three related layers:

| Layer | Location | Contents | Role |
|---|---|---|---|
| Reusable foundations | [Prompts/Construct/](Prompts/Construct) | 20 Markdown modules | General reasoning, judgment, representation, inquiry, modeling, and workflow capabilities |
| Specialized knowledge | [Prompts/](Prompts) | 13 standalone Markdown specifications | Domain-specific expertise, research methods, creative disciplines, and operating procedures |
| Packaged distributions | [Plugins/](Plugins) | 4 versioned ZIP files | Reusable plugin snapshots with manifests and skill files |

**Construct** is the general-purpose foundation. Its modules cover concepts such as Difference, Evaluation, Knowledge, Taxonomy, Validity, and Workflow. The standalone specialists extend the library into disciplines such as Analytical Psychology, Jurisprudence, Legal Scholarship, Neurorights, Citation, Research, Aesthetics, and software engineering.

### Design principles

- **Readable sources:** preserve the underlying conceptual architectures as Markdown, independent of any one plugin runtime.
- **Separation of concerns:** distinguish general-purpose constructs from specialized knowledge systems.
- **Explicit concepts and boundaries:** define terminology, relationships, assumptions, and limits rather than treating neighboring concepts as interchangeable.
- **Evidence-conscious reasoning:** recognize that interpretation, theory, empirical evidence, and verification are different things.
- **Modular reuse:** let a construct or specialist inform a single task or become part of a broader packaged system.
- **Version awareness:** distinguish an evolving source document from the fixed contents of a released ZIP.

These are design intentions and characteristics of the specifications, not proof that every generated answer satisfies them.

## Plugin Packages

The following ZIPs are present in the repository:

| System | Current ZIP | Included skills | Related Markdown sources |
|---|---|---|---|
| Construct | [v0.9.20](Plugins/Construct_v.0.9.20.zip) | 20 | [Construct modules](Prompts/Construct) |
| Citation | [v0.1.1](Plugins/Citation_v.0.1.1.zip) | 2: citation, research | [CT](Prompts/CT.md), [RS](Prompts/RS.md) |
| Systematic Review | [v0.1.7](Plugins/Systematic_Review_v.0.1.7.zip) | 5: systematic-review, research, synthesis, theory, citation | [SR](Prompts/SR.md), [RS](Prompts/RS.md), [ST](Prompts/ST.md), [TR](Prompts/TR.md), [CT](Prompts/CT.md) |
| Visual Art | [v0.1.0](Plugins/Visual_Art_v.0.1.0.zip) | 1: visual-art | [VA](Prompts/VA.md) |

The source specifications in `Prompts/` remain useful independently of the packaged versions. A plugin's version number and a source architecture identifier (for example, `AP-18` or `C-17`) describe different things.

### Release and compatibility notes

The plugin packages are presently maintained as committed ZIP artifacts. There is **no automated, reproducible source-to-package build pipeline** in this repository, and there is no CI check demonstrating that packaged skills exactly match the latest Markdown sources.

The current archives also have packaging differences:

- **Construct, Citation, and Systematic Review** place `plugin.json` and their `skills/` directory at the ZIP root.
- **Visual Art** places those files inside a top-level `Visual_Art_v.0.1.0/` directory. Its two bundled manifests also disagree on the version: `plugin.json` records `0.1.0` while `.codex-plugin/plugin.json` records `1.0.0`. This inconsistency has **not** been corrected in the ZIP.

Importers may have different requirements; verify archive layout, manifests, and skills before relying on any given release. A standardized package format and release checks are on the [roadmap](#development-roadmap).

## Construct Modules

The 20 source modules of Construct live in [`Prompts/Construct/`](Prompts/Construct).

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

Construct is intended as a shared conceptual foundation, not a requirement that every specialist always invoke every module. I can use these sources separately or combine them according to the task.

## Standalone Specialists

I currently keep **13 standalone prompt specifications** at the top level of [`Prompts/`](Prompts):

| Code | Specialist | Primary focus |
|---|---|---|
| AP | [Analytical Psychology (AP-18)](Prompts/AP.md) | Jungian and post-Jungian psychology, psyche, symbolism, clinical theory, research, and critical validation |
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

Not every standalone specialist has a ZIP counterpart in this repository. A specialist's presence here also does not necessarily imply that a plugin with that name is currently installed or published elsewhere.

## Validation and Quality

The implemented automated check is [`tests/test_readme.py`](tests/test_readme.py), run by [`.github/workflows/readme-check.yml`](.github/workflows/readme-check.yml) on pushes and pull requests. It verifies local paths and README heading anchors referenced by Markdown links.

**Currently checked:** README local links and anchors.

**Not yet automatically checked:** plugin manifest consistency, ZIP layout or integrity, source-to-package parity, factor-notation grammar, cross-document terminology, citations and evidence provenance, model behavior, or task performance.

A structurally extensive prompt is not, by itself, a validated expert system. In particular, frontier, legal, clinical, and scientific claims should be checked against relevant primary literature, current professional standards, and the context of use. The Markdown specifications are evolving knowledge architectures, not independently verified bibliographies.

## Development Roadmap

These are priorities for future work, **not implemented features**:

1. **Restore and maintain repository integrity.** Keep source and package inventories, links, and release references synchronized.
2. **Standardize plugin packaging.** Normalize ZIP roots, manifests, version fields, and unwanted build artifacts.
3. **Make releases reproducible.** Add a deterministic source-to-skill build process, checksums, and package validation in CI.
4. **Validate knowledge structures.** Introduce a formal schema or parser for nested factors, structural linting, and semantic consistency checks.
5. **Track evidence and provenance.** Add source registries, citation verification, evidence status, and review dates to research-intensive specialists.
6. **Evaluate specialist behavior.** Develop task-based test cases, adversarial checks, and regression benchmarks rather than inferring effectiveness from prompt length or coverage.
7. **Improve context efficiency.** Separate concise operating instructions from deep reference material where progressive disclosure is supported.

The goal is to retain the expressive scope of the original prompt library while developing more dependable, inspectable, and testable specialist systems.

## Repository Layout

```text
archetype/
├── Prompts/
│   ├── Construct/                     # 20 reusable source modules: C, D, ... W
│   ├── AP.md                          # Analytical Psychology (AP-18)
│   ├── AT.md                          # Aesthetics
│   ├── CT.md                          # Citation
│   ├── FED.md                         # Front-End Development
│   ├── JRP.md                         # Jurisprudence
│   ├── LS.md                          # Legal Scholarship
│   ├── NRR.md                         # Neurorights
│   ├── RS.md                          # Research
│   ├── SR.md                          # Systematic Review
│   ├── ST.md                          # Synthesis
│   ├── TR.md                          # Theory
│   ├── VA.md                          # Visual Art
│   └── WD.md                          # Web Development
├── Plugins/
│   ├── Citation_v.0.1.1.zip
│   ├── Construct_v.0.9.20.zip
│   ├── Systematic_Review_v.0.1.7.zip
│   └── Visual_Art_v.0.1.0.zip
├── tests/
│   └── test_readme.py                 # README link and anchor validation
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml          # automated README link check
├── A_Avatar.png
├── LICENSE                            # Apache License 2.0
└── README.md
```

## License

The repository is distributed under the [Apache License 2.0](LICENSE). Check the license terms and any applicable third-party material before redistribution.

![Archetype avatar](A_Avatar.png)
