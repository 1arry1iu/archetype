# Archetype — Construct

**Archetype** is now centered on **Construct**, a versioned GPT plugin that consolidates the repository's general-purpose reasoning and workflow prompts into one modular system.

The repository still includes the legacy `GPTs/` library of specialist, creative, and named-person archetypes, but **Construct is the primary maintained entry point for the reusable core prompt architecture**.

**Current packaged release:** [`Construct v0.9.18`](https://github.com/1arry1iu/archetype/blob/main/Construct/Construct_v.0.9.18.zip)

[Get Started](#get-started) · [Construct](#construct) · [Modules](#construct-modules) · [Repository Layout](#repository-layout) · [Legacy Archetypes](#legacy-archetypes) · [Development](#development)

## Get Started

### Use Construct as a plugin

1. Download [`Construct_v.0.9.18.zip`](https://github.com/1arry1iu/archetype/blob/main/Construct/Construct_v.0.9.18.zip).
2. Load the archive using the plugin/import workflow supported by your GPT environment.
3. Give Construct the task, context, constraints, evidence, and output requirements relevant to your work.

The ZIP archive is the packaged distribution. Human-readable prompt sources are kept in [`Construct/Prompts/`](https://github.com/1arry1iu/archetype/tree/main/Construct/Prompts) so the system can be inspected, reviewed, reused, and developed without treating the package as a black box.

If your environment does not support package import, the source modules can also be used directly as prompts.

## Construct

Construct is a **modular prompt system** rather than a single persona prompt. It brings together a family of reusable reasoning architectures for creating constructs, distinguishing alternatives, evaluating evidence, organizing information, making judgments, modeling systems, asking questions, ranking options, validating claims, designing workflows, and related tasks.

The consolidation has three practical goals:

- **One entry point:** the packaged Construct plugin replaces a collection of separate top-level core-prompt directories.
- **Inspectable sources:** each major capability remains available as a standalone Markdown module under `Construct/Prompts/`.
- **Versioned distribution:** packaged releases can evolve as a coherent system while source prompts remain easy to review and compare.

The modules are deliberately broader than short prompt templates. Their source files specify distinctions, operating models, evaluation criteria, uncertainty handling, governance considerations, and workflows intended to make behavior more systematic across unfamiliar contexts.

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

## Core Tools

The older shorthand is retained where it still maps cleanly to the current repository.

| Shorthand | Prompt | Function |
|---|---|---|
| A's | [Archetypes](https://github.com/1arry1iu/archetype/tree/main/GPTs) | Legacy specialist, creative, and persona prompt library |
| B | [Block](https://github.com/1arry1iu/archetype/blob/main/Block/B) | Generate structured ten-factor blocks for a construct |
| C | [Construct](https://github.com/1arry1iu/archetype/tree/main/Construct) | Packaged plugin and modular core prompt system |
| H | [Connotation](https://github.com/1arry1iu/archetype/blob/main/Hack/CONN.md) | Construct-to-verbs formatting helper |

## Categories

| Category | GPTs |
|---|---|
| [Construct plugin](#construct) | [Core modules](#construct-modules) |
| [Legacy archetypes](#legacy-archetypes) | [Specialists, creative practices, and personas](#legacy-archetypes) |
| [Utilities](#core-tools) | [Block and Connotation](#core-tools) |

## Repository Layout

```text
archetype/
├── Construct/
│   ├── Construct_v.0.9.18.zip   # packaged Construct release
│   └── Prompts/                 # source modules: C–G and I–W
├── GPTs/                        # legacy standalone archetype library
├── Block/
│   └── B                        # block generator
├── Hack/
│   └── CONN.md                  # connotation/formatting helper
├── tests/
│   └── test_readme.py           # README path/table checks
├── .github/workflows/
│   └── readme-check.yml         # CI for README consistency
├── A_Avatar.png
├── LICENSE
└── README.md
```

## Legacy Archetypes

[`GPTs/`](https://github.com/1arry1iu/archetype/tree/main/GPTs) remains the archive/library of standalone archetypes: domain experts, creative practices, specialized workflows, perspectives, and simulations of named people.

These files can still be used directly with an LLM. They are kept separate from Construct because they represent **task- or persona-specific archetypes**, whereas Construct now carries the reusable general-purpose reasoning architecture.

A named-person prompt is a simulation or perspective prompt, not the person represented. Inclusion in the repository is not an endorsement. Geographic or subject labels indicate intended scope, not authority or evidentiary status.

## Design Notes

Construct's source modules repeatedly separate concepts that are easy to collapse in ordinary prompting — for example data from evidence, identity from role, similarity from equivalence, measurement from evaluation, and validation from mere checking. The aim is to make those distinctions explicit enough that a model can reason with them rather than rely only on surface wording.

That architecture is useful when a task needs one or more of the following:

- explicit definitions and boundaries;
- structured comparison or evaluation;
- uncertainty-aware judgment;
- information, taxonomy, or naming design;
- model or workflow design;
- prioritization, ranking, or selection;
- validation and assurance;
- reusable persona or construct architecture.

Construct is still prompt-driven software: behavior depends on the host model, available tools, context, and the user's instructions. Important factual, legal, medical, financial, scientific, or safety-critical outputs should be checked against appropriate primary sources and qualified expertise.

## Development

The repository includes a README consistency check at [`tests/test_readme.py`](tests/test_readme.py), run by [`.github/workflows/readme-check.yml`](.github/workflows/readme-check.yml). When changing paths or the compatibility tables above, keep those checks in sync.

For Construct development:

1. Edit or review source modules under `Construct/Prompts/`.
2. Keep module names and shorthand stable where possible so links and references remain durable.
3. Version packaged plugin releases explicitly.
4. Update this README when the packaged version or module inventory changes.

## License

This repository is licensed under the [Apache License 2.0](LICENSE).
