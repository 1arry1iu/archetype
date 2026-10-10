# Archetype (A-18)

**Archetype** is my evolving library of GPT prompt architectures and specialist plugin packages. It brings together general-purpose reasoning and knowledge-work modules, domain expertise, creative systems, and research workflows, with an emphasis on clarity, reusability, validation, and continuous improvement.

I maintain the **Markdown specifications as inspectable source material** and progressively package selected systems as GPT plugins. The conversion is ongoing: a source specification does not necessarily have a corresponding plugin, and an existing plugin ZIP is a versioned snapshot rather than an automatically synchronized build.

**Current inventory:** **35 Markdown specifications** (14 standalone specialists and 21 Construct modules) and **six versioned ZIP distributions** (five GPT plugin archives and one Grok skill archive). **A-18** identifies the Archetype knowledge architecture in [`Prompts/Construct/A.md`](Prompts/Construct/A.md); it is not a repository-wide release number. Each source architecture and plugin package has its own identifier or version.

[Get Started](#get-started) · [Architecture](#architecture) · [Packaged Distributions](#packaged-distributions) · [Construct Modules](#construct-modules) · [Standalone Specialists](#standalone-specialists) · [Validation](#validation-and-quality) · [Roadmap](#development-roadmap) · [Repository Layout](#repository-layout) · [License](#license)

## Get Started

### Use a prompt specification

1. Browse the [standalone specialists](Prompts) or the [21 Construct modules](Prompts/Construct).
2. Open the Markdown file for the subject or capability you need, such as [Archetype (A-18)](Prompts/Construct/A.md), [Analytical Psychology](Prompts/AP.md), [Citation](Prompts/CT.md), [Systematic Review](Prompts/SR.md), or [Visual Art](Prompts/VA.md).
3. Adapt the relevant instructions, knowledge structure, and operating procedures to your model, available tools, task, and context limits.

The specifications are extensive. They should not be assumed to fit in one model context window, nor should their conceptual breadth be confused with experimentally demonstrated model performance. For focused applications, select the relevant sections or create a smaller, tested skill from the source.

### Use a packaged plugin

Download a ZIP from [GPT Plugins/](GPT%20Plugins) or [Grok Skills/](Grok%20Skills) and follow the import process supported by your target environment. The archives include plugin metadata and skills, but compatibility depends on the target environment.

For exact contents, **inspect the ZIP itself**. The Markdown source may have changed since that release was packaged. The package inventory and compatibility caveats appear [below](#packaged-distributions).

### Check documentation links locally

```bash
python tests/test_readme.py
```

This is the repository's existing README-link check. It is **not** a complete plugin, prompt, or model-behavior test suite.

## Architecture

Archetype distinguishes three related layers:

| Layer | Location | Contents | Role |
|---|---|---|---|
| Reusable foundations | [Prompts/Construct/](Prompts/Construct) | 21 Markdown modules | Archetypal knowledge, generative identities, reasoning, judgment, representation, inquiry, modeling, and workflows |
| Specialized knowledge | [Prompts/](Prompts) | 14 standalone Markdown specifications | Domain-specific expertise, research methods, creative disciplines, and operating procedures |
| Packaged distributions | [GPT Plugins/](GPT%20Plugins), [Grok Skills/](Grok%20Skills) | 6 versioned ZIP archives | Platform-specific snapshots; verify compatibility per archive |

**Construct** is the modular foundation: **Archetype (A-18)** maps recurring patterns, symbolic structures, and their interpretations; **Construct (C-18)** models generative identities and personas; the remaining modules cover capabilities such as Difference, Evaluation, Knowledge, Taxonomy, Validity, and Workflow. The standalone specialists extend this foundation into disciplines such as Analytical Psychology, Jurisprudence, Legal Scholarship, Neurorights, Citation, Research, Aesthetics, and software engineering.

### Design principles

- **Readable sources:** preserve the underlying conceptual architectures as Markdown, independent of any one plugin runtime.
- **Separation of concerns:** distinguish general-purpose constructs from specialized knowledge systems.
- **Explicit concepts and boundaries:** define terminology, relationships, assumptions, and limits rather than treating neighboring concepts as interchangeable.
- **Evidence-conscious reasoning:** recognize that interpretation, theory, empirical evidence, and verification are different things.
- **Modular reuse:** let a construct or specialist inform a single task or become part of a broader packaged system.
- **Version awareness:** distinguish an evolving source document from the fixed contents of a released ZIP.

These are design intentions and characteristics of the specifications, not proof that every generated answer satisfies them.

## Packaged Distributions

The repository contains **five GPT plugin ZIPs** in [`GPT Plugins/`](GPT%20Plugins) and **one Grok skill ZIP** in [`Grok Skills/`](Grok%20Skills). These are checked-in release snapshots, not files that are automatically regenerated when a Markdown specification changes.

| Target | System | Current archive | Related Markdown sources |
|---|---|---|---|
| GPT | Analytical Psychology | [v0.1.2](GPT%20Plugins/Analytical_Psychology_v.0.1.2.zip) | [AP](Prompts/AP.md), [AAP](Prompts/AAP.md) (related specialty) |
| GPT | Citation | [v0.1.1](GPT%20Plugins/Citation_v.0.1.1.zip) | [CT](Prompts/CT.md), [RS](Prompts/RS.md) |
| GPT | Construct | [v0.9.21](GPT%20Plugins/Construct_v.0.9.21.zip) | [Construct modules](Prompts/Construct) |
| GPT | Systematic Review | [v0.1.7](GPT%20Plugins/Systematic_Review_v.0.1.7.zip) | [SR](Prompts/SR.md), [RS](Prompts/RS.md), [ST](Prompts/ST.md), [TR](Prompts/TR.md), [CT](Prompts/CT.md) |
| GPT | Visual Art | [v0.1.1](GPT%20Plugins/Visual_Art_v.0.1.1.zip) | [AT](Prompts/AT.md), [VA](Prompts/VA.md) |
| Grok | Construct | [v0.9.21](Grok%20Skills/Construct_Grok_v0.9.21.zip) | [Construct modules](Prompts/Construct) |

**Source-to-archive relationship:** The links above identify related source specifications, **not a claim that the ZIP contains every source document verbatim**. Architecture labels (such as `AP-18` and `C-18`) are distinct from distribution versions (such as `v0.9.21`). For exact skills, manifests, supported runtimes, and version metadata, inspect the relevant archive and confirm its import requirements with the target host. Do not assume GPT plugin and Grok skill archives are interchangeable.

### Release and compatibility notes

- There is **no automated reproducible packaging pipeline**, machine-readable source-commit mapping, or CI job checking whether ZIP contents match their corresponding Markdown source revisions.
- Archive filenames indicate distribution versions, but do **not** establish internal manifest versions, skill inventory, archive integrity, or importer compatibility. Verify these against each archive.
- The README and repository tree locate artifacts; the actual ZIP and target platform determine whether an archive imports successfully.
- Earlier manual inspection of a four-archive inventory does not establish that the six currently checked-in archives are valid. Historic observations about prior Construct versions should not be extrapolated to the current distributions.
- Recommended release hardening: deterministic builds, checksums, recorded source commits, manifest and ZIP hygiene validation, and host-specific import smoke tests.

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

I currently keep **14 standalone prompt specifications** at the top level of [`Prompts/`](Prompts):

| Code | Specialist | Primary focus |
|---|---|---|
| AAP | [Archetype: Analytical Psychology (AAP-18)](Prompts/AAP.md) | Focused archetypal configurations, theories, and psychological interpretation within analytical psychology |
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

**Currently checked:** README local paths and same-README heading anchors matched by the regex-based validator. It does **not** cover image links or reference-style links, and it does not validate fragments in other Markdown documents.

**Not yet automatically checked:** full Markdown link syntax, package manifest consistency, ZIP layout or integrity, source-to-package parity, factor-notation grammar, semantic distinctiveness, cross-document terminology, citations and evidence provenance, model behavior, or task performance. A link-check pass does not establish any of these properties.

A structurally extensive prompt is not, by itself, a validated expert system. In particular, frontier, legal, clinical, and scientific claims should be checked against relevant primary literature, current professional standards, and the context of use. The Markdown specifications are evolving knowledge architectures, not independently verified bibliographies.

## Development Roadmap

These are priorities for future work, **not implemented features**:

1. **Keep documentation synchronized.** Generate or verify source and package inventories, release links, and skill counts against the repository tree.
2. **Make releases reproducible and traceable.** Build skill ZIPs deterministically from explicitly identified source commits; record checksums, source-to-skill mappings, and release provenance.
3. **Validate packages in CI.** Check ZIP roots, manifests, version parity, skill metadata, required entries, and exclusion of editor or build artifacts, separately for GPT and Grok distributions.
4. **Formalize knowledge structures.** Define a parser and schema for nested-factor notation; lint hierarchy, numbering, uniqueness, and cross-document terminology.
5. **Improve semantic precision.** Audit repeated generic subfactor templates—particularly in A-18—and favor domain-specific relationships over expansion for its own sake.
6. **Track evidence and provenance.** Add source registries, citation verification, evidence status, and review dates to research-intensive specialists.
7. **Evaluate specialist behavior.** Add representative tasks, adversarial checks, domain-boundary tests, and regression benchmarks rather than inferring effectiveness from prompt length or coverage.
8. **Improve context efficiency.** Separate concise operating instructions from deep reference material where progressive disclosure is supported.
9. **Harden documentation and CI tooling.** Support image/reference-style links and cross-document anchors; modernize and pin GitHub Actions dependencies and run validator unit tests.

The goal is to retain the expressive scope of the original prompt library while developing more dependable, inspectable, and testable specialist systems.

## Repository Layout

```text
archetype/
├── Prompts/
│   ├── Construct/                     # 21 reusable Markdown modules: A, C, D, ... W
│   │   ├── A.md                       # Archetype (A-18)
│   │   ├── C.md                       # Construct (C-18)
│   │   └── ...                        # Other Construct modules
│   ├── AAP.md                         # Archetype: Analytical Psychology (AAP-18)
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
├── GPT Plugins/                       # 5 versioned GPT plugin ZIPs
│   ├── Analytical_Psychology_v.0.1.2.zip
│   ├── Citation_v.0.1.1.zip
│   ├── Construct_v.0.9.21.zip
│   ├── Systematic_Review_v.0.1.7.zip
│   └── Visual_Art_v.0.1.1.zip
├── Grok Skills/                       # 1 versioned Grok skill ZIP
│   └── Construct_Grok_v0.9.21.zip
├── tests/
│   └── test_readme.py                 # Lightweight README link and anchor check
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml          # Runs README validation on push and PR
├── A_Avatar.png
├── LICENSE                            # Apache License 2.0
└── README.md
```

## License

The repository is distributed under the [Apache License 2.0](LICENSE). Check the license terms and any applicable third-party material before redistribution.

![Archetype avatar](A_Avatar.png)
