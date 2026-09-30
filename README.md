# Archetype (A-16)

**Archetype** is a repository of inspectable prompt architectures, packaged prompt systems, and legacy GPT archetypes.

The reusable core is **Construct**: 20 Markdown prompt specifications for construct design, comparison, evaluation, information and knowledge work, judgment, modeling, learning, prioritization, validation, workflow design, and related tasks. Its human-readable source is under [`Prompts/Construct/`](Prompts/Construct), and its current packaged distribution is [`Construct v0.9.18`](Construct/Construct_v.0.9.18.zip).

The repository also contains standalone domain prompt systems under [`Prompts/`](Prompts), versioned package artifacts under [`Plugins/`](Plugins), and a large legacy prompt library under [`GPTs/`](GPTs).

[Get Started](#get-started) · [Packaged Systems](#packaged-systems) · [Source Prompt Systems](#source-prompt-systems) · [Construct](#construct) · [Modules](#construct-modules) · [Legacy Archetypes](#legacy-archetypes) · [Validation](#validation-and-ci) · [Repository Layout](#repository-layout)

## Repository Model

This is primarily a **prompt-specification repository**, not an application codebase.

- There is no repository-wide runtime, package manager, dependency manifest, build command, or universal installer.
- Human-readable prompt sources are Markdown files.
- Versioned ZIP files are packaged distribution artifacts for hosts that support their package format.
- The only checked-in Python code is the README path validator under `tests/`.
- The GitHub Actions workflow runs that validator; it does not execute GPTs, call an LLM API, evaluate model responses, or verify that ZIP contents exactly match the Markdown sources.

## Get Started

### Use the source prompts directly

- For the reusable Construct core, choose a module from [`Prompts/Construct/`](Prompts/Construct).
- For Citation, Research, Systematic Review, Synthesis, Theory, and Visual Art, browse the standalone sources in [`Prompts/`](Prompts).
- For older standalone archetypes, browse [`GPTs/`](GPTs).

Supply the selected prompt to the LLM/GPT environment you use in the way that environment accepts system, custom-instruction, or prompt content.

### Use a packaged artifact

The repository currently contains four versioned ZIP artifacts:

- [`Construct_v.0.9.18.zip`](Construct/Construct_v.0.9.18.zip)
- [`Citation_v.0.1.1.zip`](Plugins/Citation_v.0.1.1.zip)
- [`Systematic_Review_v.0.1.7.zip`](Plugins/Systematic_Review_v.0.1.7.zip)
- [`Visual_Art_v.0.1.0.zip`](Plugins/Visual_Art_v.0.1.0.zip)

Import or load a ZIP only with a host that supports the package format you are using. The checked-in Markdown sources are the portable, inspectable reference; this repository does not define a universal package runtime.

## Packaged Systems

| System | Package | Human-readable source | Scope |
|---|---|---|---|
| Construct | [`v0.9.18`](Construct/Construct_v.0.9.18.zip) | [`Prompts/Construct/`](Prompts/Construct) | General-purpose reasoning, representation, knowledge, decision, validation, and workflow architectures |
| Citation | [`v0.1.1`](Plugins/Citation_v.0.1.1.zip) | [`CT.md`](Prompts/CT.md) | Citation, reference, provenance, evidence linkage, attribution, and bibliographic integrity |
| Systematic Review | [`v0.1.7`](Plugins/Systematic_Review_v.0.1.7.zip) | [`SR.md`](Prompts/SR.md) | Systematic-review and evidence-synthesis architecture |
| Visual Art | [`v0.1.0`](Plugins/Visual_Art_v.0.1.0.zip) | [`VA.md`](Prompts/VA.md) | Visual-art practice spanning perception, conception, research, design, making, critique, exhibition, preservation, professional practice, and learning |

Package artifacts and source prompts are stored separately: ZIP distributions live under `Construct/` or `Plugins/`, while inspectable Markdown sources live under `Prompts/`.

## Source Prompt Systems

In addition to the Construct modules, the repository contains these standalone source prompt systems:

| Code | System | Source | Package status |
|---|---|---|---|
| CT | Citation | [`Prompts/CT.md`](Prompts/CT.md) | Packaged as `Citation_v.0.1.1.zip` |
| RS | Research | [`Prompts/RS.md`](Prompts/RS.md) | Source only |
| SR | Systematic Review | [`Prompts/SR.md`](Prompts/SR.md) | Packaged as `Systematic_Review_v.0.1.7.zip` |
| ST | Synthesis | [`Prompts/ST.md`](Prompts/ST.md) | Source only |
| TR | Theory | [`Prompts/TR.md`](Prompts/TR.md) | Source only |
| VA | Visual Art | [`Prompts/VA.md`](Prompts/VA.md) | Packaged as `Visual_Art_v.0.1.0.zip` |

## Construct

Construct is the repository's reusable core prompt architecture. It is organized as standalone Markdown specifications under [`Prompts/Construct/`](Prompts/Construct), rather than executable software modules.

Each module frames a problem domain as a system: it defines key distinctions, entities and relationships, operating or evaluation models, uncertainty and evidence considerations, governance concerns, and workflows. Modules can be used independently, while the ZIP under `Construct/` provides the versioned packaged distribution.

### Design intent

- **Reusable core:** general reasoning and workflow primitives rather than a single task or persona.
- **Inspectable sources:** every checked-in core module is readable as Markdown.
- **Independent or combined use:** modules can be supplied directly or used through a supported package host.
- **Explicit boundaries:** prompts distinguish neighboring concepts instead of treating them as interchangeable.
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

## Legacy Archetypes

[`GPTs/`](GPTs) is the repository's library of standalone archetype prompts. It includes domain specialists, creative practices, specialized workflows, perspectives, and simulations of named people.

These prompts can be used independently from Construct and the packaged systems. They remain separate because they are primarily task-, perspective-, or persona-specific, while Construct is the reusable general-purpose prompt architecture.

Legacy prompts vary in age, scope, framing, and safety assumptions. Some use specialist or authoritative first-person language in medical, legal, political, technical, or other consequential domains. Treat that language as prompt design, not evidence of credentials, current factual accuracy, professional authorization, or suitability for high-stakes deployment. Review and adapt prompts for the model, host, domain, and safety requirements of the intended use.

Named-person prompts are simulations or perspective prompts, not the people represented. Inclusion in the repository is not an endorsement, and a prompt's subject label does not establish authority, factual accuracy, or evidentiary status.

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

## Validation and CI

The repository contains one Python validator: [`tests/test_readme.py`](tests/test_readme.py).

Run it locally with:

```bash
python tests/test_readme.py
```

The current validator checks repository paths referenced by the **Core Tools** table and local/repository paths referenced by the **Categories** table. It exits nonzero when one of those checked paths is missing.

The GitHub Actions workflow at [`.github/workflows/readme-check.yml`](.github/workflows/readme-check.yml) runs the validator for pushes and pull requests affecting `README.md`, `GPTs/**`, the validator itself, or the workflow file.

Current validation is intentionally narrow:

- it is a repository-path consistency check, not a GPT or LLM behavior test;
- it does not validate every Markdown link in this README;
- it does not evaluate the content, safety, factual accuracy, or quality of prompt files;
- it does not verify source-to-ZIP equivalence or package reproducibility;
- changes limited to `Prompts/**`, `Construct/**`, or `Plugins/**` do not currently trigger the workflow unless another watched path also changes.

## Repository Layout

```text
archetype/
├── .github/
│   ├── FUNDING.yml
│   └── workflows/
│       └── readme-check.yml         # runs the README path validator in CI
├── Construct/
│   └── Construct_v.0.9.18.zip       # versioned Construct package
├── GPTs/                            # legacy standalone archetype library
├── Plugins/
│   ├── Citation_v.0.1.1.zip         # versioned Citation package
│   ├── Systematic_Review_v.0.1.7.zip # versioned Systematic Review package
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
├── A_Avatar.png
├── LICENSE                          # Apache License 2.0
└── README.md
```

## License

Repository licensing is provided in [`LICENSE`](LICENSE) (Apache License 2.0).
