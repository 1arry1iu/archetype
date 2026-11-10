# Archetype

**Archetype** is a library of LLM prompt architectures, reusable reasoning modules, specialist knowledge systems, and packaged skills and plugins. It brings together research methods, conceptual frameworks, creative practices, and software engineering with an emphasis on reuse, evidence, and continuous improvement.

The **November 10, 2026 inventory** contains **89 ZIP archives** across four groups. It includes **21 Construct modules**, **57 topic and specialist packages**, **10 GPT packages**, and **1 Grok package**. `README.md` is the only Markdown file tracked outside the archives on `main`.

**Contact:** [@1arry1iu on X](https://x.com/1arry1iu)

[Projects](#archetype-projects) · [Get Started](#get-started) · [Architecture](#architecture) · [Package Inventory](#package-inventory) · [Package Notes](#package-notes) · [Historical Source](#historical-source) · [Verification](#verification-and-release-status) · [Repository Layout](#repository-layout)

## Archetype Projects

Selected demo projects showcased alongside the Archetype knowledge architectures and prompt libraries:

- [Schoolside · Chiang Mai](https://schoolside-chiang-mai.greenlake32.chatgpt.site)
- [Thailand Fieldguide](https://thailand-fieldguide.greenlake32.chatgpt.site/)
- [远见 · Atlas](https://yuanjian-atlas.greenlake32.chatgpt.site/)
- [Little Days · Chiang Mai](https://little-days-chiang-mai.greenlake32.chatgpt.site/)
- [Pause · Chiang Mai](https://pause-chiang-mai.greenlake32.chatgpt.site/)

## Get Started

1. **Choose a package family.** Browse [Construct foundations](blocks/Construct), [topic and specialist packages](blocks), [GPT packages](gpt), or the [Grok package](grok).
2. **Inspect the ZIP before importing.** Check its layout and metadata against the requirements of your target platform. The [package notes](#package-notes) list known issues in this snapshot.
3. **Select and adapt carefully.** Use only the instructions and supporting material relevant to your task, tools, permissions, and context window. A checked-in ZIP is not evidence of runtime compatibility or prompt quality.
4. **Need editable Markdown source?** The former source specifications are available in [Git history](#historical-source), not as standalone Markdown files on the current `main` branch.

The `blocks/` archives are not necessarily interchangeable with `gpt/` or `grok/` archives. No universal installer is provided.

## Architecture

| Layer | Current location | Tracked contents | Purpose |
|---|---|---|---|
| Reusable foundations | [`blocks/Construct/`](blocks/Construct) | 21 ZIP archives | General-purpose modules for reasoning, knowledge, judgment, models, validation, and workflows |
| Specialist and topic packages | [`blocks/`](blocks) | 57 ZIP archives, excluding `Construct/` | Discipline-specific skills, methods, and reference assets |
| GPT-oriented packages | [`gpt/`](gpt) | 10 ZIP archives | Packaged systems with platform-specific layouts and versioned filenames |
| Grok-oriented packages | [`grok/`](grok) | 1 ZIP archive | Construct-oriented distribution snapshot |

**Package identity is not source identity.** Module names, historical identifiers (such as `A-18`), and versioned ZIP filenames do not by themselves establish that a package corresponds to a specific source revision. Do not infer compatibility or feature parity from similar names.

## Package Inventory

The following is the complete tracked ZIP inventory for the snapshot above. Filenames are reproduced exactly, including punctuation and case. Links identify checked-in files, not verified releases.

### Construct modules — 21 archives

| Package | Tracked archive |
|---|---|
| Archetype | [`archetype.zip`](blocks/Construct/archetype.zip) |
| Construct | [`construct.zip`](blocks/Construct/construct.zip) |
| Difference | [`difference.zip`](blocks/Construct/difference.zip) |
| Evaluation | [`evaluation.zip`](blocks/Construct/evaluation.zip) |
| Format | [`format.zip`](blocks/Construct/format.zip) |
| Gist | [`gist.zip`](blocks/Construct/gist.zip) |
| Information | [`information.zip`](blocks/Construct/information.zip) |
| Judgement | [`judgement.zip`](blocks/Construct/judgement.zip) |
| Knowledge | [`knowledge.zip`](blocks/Construct/knowledge.zip) |
| Learning | [`learning.zip`](blocks/Construct/learning.zip) |
| Model | [`model.zip`](blocks/Construct/model.zip) |
| Name | [`name.zip`](blocks/Construct/name.zip) |
| Openness | [`openness.zip`](blocks/Construct/openness.zip) |
| Priority | [`priority.zip`](blocks/Construct/priority.zip) |
| Question | [`question.zip`](blocks/Construct/question.zip) |
| Ranking | [`ranking.zip`](blocks/Construct/ranking.zip) |
| Similarity | [`similarity.zip`](blocks/Construct/similarity.zip) |
| Taxonomy | [`taxonomy.zip`](blocks/Construct/taxonomy.zip) |
| Uniqueness | [`uniqueness.zip`](blocks/Construct/uniqueness.zip) |
| Validity | [`validity.zip`](blocks/Construct/validity.zip) |
| Workflow | [`workflow.zip`](blocks/Construct/workflow.zip) |

### Topic and specialist packages — 57 archives

| Package | Tracked archive |
|---|---|
| Academic and Creative Portfolios | [`academic-and-creative-portfolios.zip`](blocks/academic-and-creative-portfolios.zip) |
| Accounting | [`accounting.zip`](blocks/accounting.zip) |
| Admissions Interviews | [`admissions-interviews.zip`](blocks/admissions-interviews.zip) |
| Admissions Testing and Assessment | [`admissions-testing-and-assessment.zip`](blocks/admissions-testing-and-assessment.zip) |
| Application Essay Writing | [`application-essay-writing.zip`](blocks/application-essay-writing.zip) |
| Artificial Intelligence | [`artificial_intelligence.zip`](blocks/artificial_intelligence.zip) |
| Authenticity | [`authenticity.zip`](blocks/authenticity.zip) |
| Bible | [`bible.zip`](blocks/bible.zip) |
| Bible History | [`bible-history.zip`](blocks/bible-history.zip) |
| Biblical Corpus | [`biblical-corpus.zip`](blocks/biblical-corpus.zip) |
| Biblical Languages | [`biblical-languages.zip`](blocks/biblical-languages.zip) |
| Biblical Scholarship | [`biblical-scholarship.zip`](blocks/biblical-scholarship.zip) |
| Biblical World | [`biblical-world.zip`](blocks/biblical-world.zip) |
| Business Analytics | [`business-analytics.zip`](blocks/business-analytics.zip) |
| Career | [`career.zip`](blocks/career.zip) |
| Christianity | [`christianity.zip`](blocks/christianity.zip) |
| Cinematic Creativity | [`cinematic_creativity.zip`](blocks/cinematic_creativity.zip) |
| College Admissions | [`college-admissions.zip`](blocks/college-admissions.zip) |
| College Application | [`college-application.zip`](blocks/college-application.zip) |
| Creativity | [`creativity.zip`](blocks/creativity.zip) |
| Credential Recognition and Equivalency | [`credential-recognition-and-equivalency.zip`](blocks/credential-recognition-and-equivalency.zip) |
| Differentiation | [`differentiation.zip`](blocks/differentiation.zip) |
| Digital Storytelling | [`digital_storytelling.zip`](blocks/digital_storytelling.zip) |
| Economics | [`economics.zip`](blocks/economics.zip) |
| Educational Admissions And Application | [`educational-admissions-and-application.zip`](blocks/educational-admissions-and-application.zip) |
| Educational Admissions (reference atlas) | [`educational-admissions.zip`](blocks/educational-admissions.zip) |
| Evidence | [`evidence.zip`](blocks/evidence.zip) |
| Filmmaking | [`filmmaking.zip`](blocks/filmmaking.zip) |
| Finance | [`finance.zip`](blocks/finance.zip) |
| Fintech | [`fintech.zip`](blocks/fintech.zip) |
| Global and Comparative Education | [`global-and-comparative-education.zip`](blocks/global-and-comparative-education.zip) |
| Graduate Admissions | [`graduate-admissions.zip`](blocks/graduate-admissions.zip) |
| Graduate Application | [`graduate-application.zip`](blocks/graduate-application.zip) |
| Impact | [`impact.zip`](blocks/impact.zip) |
| International Student Mobility | [`international-student-mobility.zip`](blocks/international-student-mobility.zip) |
| Master's in Finance Application | [`masters-in-finance-application.zip`](blocks/masters-in-finance-application.zip) |
| Narration | [`narration.zip`](blocks/narration.zip) |
| Personality Psychology | [`personality-psychology.zip`](blocks/personality-psychology.zip) |
| Postgraduate Application Essay | [`postgraduate-application-essay.zip`](blocks/postgraduate-application-essay.zip) |
| Potential | [`potential.zip`](blocks/potential.zip) |
| Professional School Admissions | [`professional-school-admissions.zip`](blocks/professional-school-admissions.zip) |
| Professional School Application | [`professional-school-application.zip`](blocks/professional-school-application.zip) |
| Program Fit | [`program-fit.zip`](blocks/program-fit.zip) |
| Quantitative Analysis | [`quantitative-analysis.zip`](blocks/quantitative-analysis.zip) |
| Recommendations and References | [`recommendations-and-references.zip`](blocks/recommendations-and-references.zip) |
| Research Supervision and Doctoral Fit | [`research-supervision-and-doctoral-fit.zip`](blocks/research-supervision-and-doctoral-fit.zip) |
| Research | [`research.zip`](blocks/research.zip) |
| Scholarships and Financial Aid | [`scholarships-and-financial-aid.zip`](blocks/scholarships-and-financial-aid.zip) |
| Strategy | [`strategy.zip`](blocks/strategy.zip) |
| Systematic Review | [`systematic_review.zip`](blocks/systematic_review.zip) |
| Theology | [`theology.zip`](blocks/theology.zip) |
| Transfer and Alternative Pathways | [`transfer-and-alternative-pathways.zip`](blocks/transfer-and-alternative-pathways.zip) |
| UK Graduate Education | [`uk-graduate-education.zip`](blocks/uk-graduate-education.zip) |
| UK Undergraduate Education | [`uk-undergraduate-education.zip`](blocks/uk-undergraduate-education.zip) |
| University Rankings | [`university-rankings.zip`](blocks/university-rankings.zip) |
| US Graduate Education | [`us-graduate-education.zip`](blocks/us-graduate-education.zip) |
| US Undergraduate Education | [`us-undergraduate-education.zip`](blocks/us-undergraduate-education.zip) |

### GPT packages — 10 archives

| Package | Tracked archive |
|---|---|
| Cinematic Creativity V.0.1.3 | [`Cinematic_Creativity_v.0.1.3.zip`](gpt/Cinematic_Creativity_v.0.1.3.zip) |
| Analytical Psychology V.0.1.2 | [`analytical_psychology_v.0.1.2.zip`](gpt/analytical_psychology_v.0.1.2.zip) |
| Bible v1.1.1 | [`bible-v1.1.1.zip`](gpt/bible-v1.1.1.zip) |
| Citation V.0.1.1 | [`citation_v.0.1.1.zip`](gpt/citation_v.0.1.1.zip) |
| Construct v1.0.2 (Research only) | [`construct-v1.0.2.zip`](gpt/construct-v1.0.2.zip) |
| Educational Admissions And Application V0.0.8 | [`educational-admissions-and-application-v0.0.8.zip`](gpt/educational-admissions-and-application-v0.0.8.zip) |
| Post Graduate Application V.1.0.1 | [`post-graduate-application-v.1.0.1.zip`](gpt/post-graduate-application-v.1.0.1.zip) |
| Systematic Review V.0.1.7 | [`systematic_review_v.0.1.7.zip`](gpt/systematic_review_v.0.1.7.zip) |
| Visual Art V.0.1.1 | [`visual_art_v.0.1.1.zip`](gpt/visual_art_v.0.1.1.zip) |
| Web Development V.1.0.20 | [`web_development_v.1.0.20.zip`](gpt/web_development_v.1.0.20.zip) |

### Grok package — 1 archive

| Package | Tracked archive |
|---|---|
| Construct Grok V0.9.21 | [`construct_grok_v0.9.21.zip`](grok/construct_grok_v0.9.21.zip) |

## Package Notes

- **Construct v1.0.2.** The GPT archive contains only the Research skill. Its manifests describe a 22-skill suite, and the archive lacks the two reference ZIPs listed by the Research skill and the icon declared in the manifests.
- **Standalone skill format.** Of the 78 `blocks/` archives, 43 have a `SKILL.md` without YAML frontmatter, Digital Storytelling has a skill name that differs from its folder name, and Educational Admissions contains only a reference atlas. These 45 archives need packaging changes to meet the [Agent Skills format](https://agentskills.io/specification#skillmd-format).
- **GPT submission metadata.** Cinematic Creativity's primary workflow lacks YAML frontmatter. Systematic Review's main skill description exceeds the 1,024-character limit, and 14 skills in Educational Admissions and Application exceed the 64-character limit for the combined plugin and skill name. See the [OpenAI submission requirements](https://developers.openai.com/plugins/deploy/submission-errors#skill-errors).
- **Rebuild paths.** Some bundled rebuild scripts, including those for Admissions Interviews, Theology, Biblical World, and Taxonomy, use fixed `/mnt/data` paths. Review their input and output paths before running the rebuild commands.

## Historical Source

The repository previously tracked 21 standalone specialist Markdown files in `blocks/` and 21 Construct Markdown files in `blocks/Construct/`. These files **are absent from current `main`**.

- [Browse the earlier source-bearing `blocks/` snapshot](https://github.com/1arry1iu/archetype/tree/9660129dba9e9edcb40ac8b593aca3b25511074d/blocks).
- [Construct Markdown removal commit](https://github.com/1arry1iu/archetype/commit/6246ce4a7fefe6b9e3ac75118bb8625407dbd1a4) (October 26, 2026).
- [Standalone specialist Markdown removal commit](https://github.com/1arry1iu/archetype/commit/6cb53297f6a6a8dfe5a2be52253933733639c31c) (October 26, 2026).

Historical files can be useful for reading, comparison, and restoration decisions. **They are not a verified source map for the currently distributed ZIPs.** The previously documented knowledge-map files are also absent from this branch.

## Verification and Release Status

The [README link checker](tests/test_readme.py) runs in [GitHub Actions](.github/workflows/readme-check.yml) on pushes and pull requests. It checks local paths named in standard inline Markdown links and anchors that point into this README. Inventory completeness, historical Git revisions, image and reference-style links, and archive contents require separate checks.

A manual audit of the November 10 snapshot verified decompression and CRCs for all 89 tracked ZIPs and 301 nested ZIPs. All passed. Live platform imports and model behavior require separate verification.

The following checks are recommended before distribution:

1. **Archive integrity and safety:** test decompression and CRCs; reject absolute paths, traversal entries, unsafe symlinks, unexpected duplicates, and excessive expansion.
2. **Package contracts:** validate expected manifest paths and schemas, references, platform-specific layout, and required assets (including nested archives).
3. **Provenance:** record source commit, package version, target platform, and SHA-256 checksum for each artifact.
4. **Runtime smoke tests:** import the archive into the actual target platform and verify the intended skill or plugin can be invoked.
5. **Behavioral evaluation:** test representative use cases, regressions, groundedness, instruction adherence, security boundaries, and failures across target models.
6. **Release management:** publish tagged, traceable distributions only after the relevant gates pass; update this inventory when packages are added, renamed, or removed.

**Current limitation:** Checked-in archives are snapshots and are not demonstrably generated from a documented reproducible build pipeline. Presence in the repository is **not** a release certification.

## Repository Layout

```text
archetype/
├── blocks/
│   ├── Construct/                    # 21 Construct ZIP packages
│   └── *.zip                         # 57 topic and specialist ZIP packages
├── gpt/                              # 10 GPT ZIP packages
├── grok/                             # 1 Grok ZIP package
├── tests/test_readme.py              # README local-link validation
├── .github/workflows/readme-check.yml
├── .github/FUNDING.yml
├── A_Avatar.png
├── LICENSE                           # Apache License 2.0
└── README.md                         # Only tracked Markdown file
```

## License

See [LICENSE](LICENSE) for the Apache License 2.0.

![Archetype avatar](A_Avatar.png)
