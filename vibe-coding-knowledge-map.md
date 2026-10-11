# Vibe Coding — Frontier Knowledge Atlas

**As of: 11 October 2026** · Construct-inspired conceptual synthesis · 16 domains · 129 concepts · 27 directed typed relationships · 17 primary/technical references.

> Core thesis: Natural-language generation lowers the cost of producing software; correctness, user value, safety, permissions, context, and long-term operations determine whether generated software is trustworthy.

## Definitions and boundaries

- **Vibe coding** (narrow historical sense): prompt-based software creation with minimal review of generated code, suitable especially for disposable prototypes.
- **AI-assisted programming**: AI helps but the human retains implementation-level oversight.
- **Agentic coding**: a tool-using agent makes and checks code changes toward a task.
- **Spec-driven engineering**: explicit intent, requirements, constraints, and tests guide agents.
- **Agentic engineering**: engineers design agents’ environments, constraints, feedback, and approval systems while delegating much implementation.

## Core system model

**Intent → specification → context → agent/harness + tools → implementation → independent tests + security controls → release → observation → evidence → revised intent.**

Human ownership and scoped permissions run across every stage.

## Epistemic key

- **Established**: operational practice or demonstrated phenomenon (not automatically sufficient for all contexts).
- **Emerging**: developing practice, active research, or empirically unsettled frontier question.
- **Hypothesis**: proposed future or approach whose utility and reliability remain to be validated.

The labels are editorial maturity assessments, not scientific confidence scores.

## Complete taxonomy

### Why and who (FRAME)

#### D01 — Definitions & Paradigms

**Purpose.** Separate a casual interaction style from a reliable engineering operating model.

**Diagnostic question.** How much implementation knowledge and operational responsibility remains with the human?

**Failure mode.** Mistaking a generated demo for a validated product.

- **D01.01 · Vibe coding** [established] — Describe desired behavior, accept model-written code, and iterate using output, often without detailed code inspection.
- **D01.02 · AI-assisted coding** [established] — Human retains direct implementation oversight while AI contributes explanations, completions, and edits.
- **D01.03 · Agentic coding** [established] — Tool-using agents inspect repositories, edit files, execute commands, and iterate toward an assigned objective.
- **D01.04 · Spec-driven engineering** [established] — Build from explicit requirements, acceptance checks, architecture decisions, and trackable implementation tasks.
- **D01.05 · Agentic engineering** [emerging] — Humans shape intent and guardrails while software agents perform larger portions of engineering work.
- **D01.06 · Autonomy continuum** [established] — Range from suggestion and supervised edits to bounded delegation and long-running agent execution.
- **D01.07 · Prototype vs production** [established] — Different assurance obligations: disposable experiments can tolerate risks that public deployments cannot.
- **D01.08 · Control vs delegation** [established] — Distinguish writing code from being accountable for code, data, behavior, and outcomes.

#### D02 — Product Intent & Value

**Purpose.** Translate fuzzy desire into an explicit, bounded problem worth solving.

**Diagnostic question.** What measurable user outcome defines success, and what must not happen?

**Failure mode.** Feature quantity substitutes for product value.

- **D02.01 · Problem discovery** [established] — Identify the user, job-to-be-done, constraints, unmet need, and alternatives.
- **D02.02 · Outcome hypothesis** [established] — Articulate who benefits, what changes, and how the change will be observed.
- **D02.03 · Requirements and non-goals** [established] — Define capabilities, scope boundaries, limitations, and explicit exclusions.
- **D02.04 · Acceptance criteria** [established] — Specify observable examples and thresholds that constitute done.
- **D02.05 · User research** [established] — Use interviews, behavioral data, or real workflow observation to test assumptions.
- **D02.06 · Prototype experiment** [established] — Build the smallest artifact able to invalidate a meaningful product assumption.
- **D02.07 · Risk tiering** [established] — Match review effort to consequence, data sensitivity, reversibility, and external exposure.
- **D02.08 · Prioritization** [established] — Choose high-learning-value, bounded, testable slices rather than a sprawling backlog.

#### D03 — Humans, Roles & Agency

**Purpose.** Specify who judges, who builds, who approves, and who is responsible.

**Diagnostic question.** Which decisions can an agent make; which remain legitimately human?

**Failure mode.** Autonomy expands faster than understanding or accountability.

- **D03.01 · Human as product owner** [established] — Owns user goals, trade-offs, and acceptance of outcomes.
- **D03.02 · Human as system architect** [established] — Owns boundaries, invariants, data flows, and integration decisions.
- **D03.03 · Human as verifier** [established] — Challenges evidence and checks whether tests match the original intent.
- **D03.04 · Agent as implementer** [established] — Executes scoped changes to code, tests, docs, and supporting assets.
- **D03.05 · Agent as reviewer** [emerging] — A second agent checks diffs, threats, tests, and failure cases; not a replacement for independent evidence.
- **D03.06 · Agent as investigator** [emerging] — Explores logs, traces, failures, and possible fixes under explicit permissions.
- **D03.07 · Authority matrix** [established] — Assign read/write/execute/deploy capabilities, escalation points, and human veto.
- **D03.08 · Multi-agent organization** [emerging] — Use specialized subagents and delegation selectively when coordination overhead is justified.

### How software is generated (BUILD)

#### D04 — Interaction & Prompt Design

**Purpose.** Make natural-language instructions executable, verifiable, and appropriately scoped.

**Diagnostic question.** Can another engineer—or agent—tell what success looks like?

**Failure mode.** Ambiguity is converted into confident but incorrect code.

- **D04.01 · Intent statements** [established] — State desired behavior, actors, examples, limits, and user impact.
- **D04.02 · Constraints and invariants** [established] — Prescribe what must stay true, including interfaces, budgets, and security requirements.
- **D04.03 · Context-rich requests** [established] — Provide relevant paths, existing interfaces, failing tests, and expected behavior.
- **D04.04 · Plan-before-edit** [established] — Request a diagnosis and proposed changes before making large or risky edits.
- **D04.05 · Diff-focused iteration** [established] — Inspect and constrain the minimal change; avoid rewriting unrelated modules.
- **D04.06 · Examples and counterexamples** [established] — Use concrete inputs, outputs, and edge cases to disambiguate intent.
- **D04.07 · Structured outputs** [established] — Ask for plans, checklists, data schemas, and machine-checkable acceptance evidence.
- **D04.08 · Uncertainty and stop conditions** [emerging] — Require explicit unknowns, assumptions, escalation triggers, and refusal to guess silently.

#### D05 — Context & Knowledge Architecture

**Purpose.** Give agents the right information at the right moment with traceable provenance.

**Diagnostic question.** What context is authoritative, current, relevant, and safe to load?

**Failure mode.** Context bloat, stale docs, and untrusted content distort behavior.

- **D05.01 · Repository instructions** [established] — Use concise project guidance (for example AGENTS.md or CLAUDE.md) with commands and conventions.
- **D05.02 · Source-of-truth documents** [established] — Maintain compact specs, architecture decisions, interface contracts, and non-goals.
- **D05.03 · Context selection** [established] — Retrieve necessary files, relevant history, examples, and failing cases instead of everything.
- **D05.04 · Session continuity** [emerging] — Use progress artifacts, task state, commits, and handoff summaries across context windows.
- **D05.05 · Memory and provenance** [emerging] — Track decisions, their dates, source, confidence, and reasons for later revision.
- **D05.06 · Retrieval design** [established] — Combine repository search, file navigation, symbol tools, docs, and curated references.
- **D05.07 · Context hygiene** [established] — Remove stale instructions, summarize histories, and prevent redundant or contradictory context.
- **D05.08 · Trusted/untrusted separation** [established] — Treat webpages, repository content, messages, and tool output as data, not higher-authority instructions.

#### D06 — Agent Runtime & Harness

**Purpose.** Treat the coding system as model + execution environment + feedback + policy.

**Diagnostic question.** Can the agent make progress, detect failure, recover, and stop safely?

**Failure mode.** A stronger model does not compensate for a broken execution loop.

- **D06.01 · Agent control loop** [established] — Observe repository state, plan, call tools, inspect feedback, and revise.
- **D06.02 · Tool execution substrate** [established] — Provide terminal, editor, repo tools, browser, and test runners with scoped access.
- **D06.03 · Sandbox and isolation** [established] — Constrain workspace, filesystem, network, credentials, and risky side effects.
- **D06.04 · Harness policy** [emerging] — Encode commands, invariants, approvals, and quality rules in enforceable runtime checks.
- **D06.05 · Long-horizon checkpoints** [emerging] — Use structured feature status, clean commits, reproducible setup, and handoff notes.
- **D06.06 · Recovery and retries** [emerging] — Classify failures, retry boundedly, revert bad steps, and surface unrecoverable issues.
- **D06.07 · Parallel work orchestration** [emerging] — Allocate isolated worktrees to independent tasks; manage integration and conflicts.
- **D06.08 · Observability and traces** [emerging] — Capture tool calls, actions, outcomes, costs, failures, and decisions.

#### D07 — Tools, Surfaces & Protocols

**Purpose.** Understand tools by capability and trust boundary rather than winner lists.

**Diagnostic question.** Which integration grants the minimum power needed to perform a task?

**Failure mode.** Convenient connectors expand attack surface and authority unnoticed.

- **D07.01 · Chat and app builders** [established] — Prompt-first interfaces for quick prototypes, UI generation, and small applications.
- **D07.02 · IDE agents** [established] — Work within editor context, changes, diffs, and local tests.
- **D07.03 · CLI and terminal agents** [established] — Operate through shells, files, commands, and development tooling.
- **D07.04 · Cloud coding agents** [emerging] — Execute delegated tasks in managed workspaces with asynchronous task/report interfaces.
- **D07.05 · Model Context Protocol** [established] — Standardizes exposure of external resources and tools; does not grant authorization by itself.
- **D07.06 · Agent Skills and conventions** [emerging] — Package reusable procedures and expertise in versioned, discoverable files.
- **D07.07 · Repository automation** [established] — Git, CI, PRs, issue trackers, and automated checks structure collaboration.
- **D07.08 · Browser and computer use** [emerging] — Enable visual interaction and end-to-end checks, subject to sandbox and approval controls.

#### D08 — Architecture, Data & Code

**Purpose.** Make generated software coherent across files, interfaces, state, and time.

**Diagnostic question.** Will a change preserve system invariants and remain maintainable?

**Failure mode.** Local prompt success causes global architectural drift.

- **D08.01 · System decomposition** [established] — Identify domains, modules, boundaries, dependencies, and ownership.
- **D08.02 · Interface contracts** [established] — Define API shapes, typed schemas, errors, compatibility, and versioning.
- **D08.03 · Data modeling** [established] — Design entities, invariants, relationships, migrations, and retention.
- **D08.04 · Authentication and authorization** [established] — Separate identity from permission, enforce decisions on the server, and test privilege boundaries.
- **D08.05 · Dependency hygiene** [established] — Audit packages, pin or constrain versions, check licenses and vulnerability advisories.
- **D08.06 · Maintainability** [established] — Keep changes small, typed, readable, documented, and consistent with local conventions.
- **D08.07 · Technical-debt controls** [established] — Detect unnecessary abstractions, duplicate logic, brittle generated patterns, and excessive complexity.
- **D08.08 · Architecture decisions** [established] — Record important trade-offs, alternatives, assumptions, and reversal costs.

#### D09 — Experience & Multimodality

**Purpose.** Connect conversational intent to observable interfaces and user experience.

**Diagnostic question.** Can actual users complete their jobs across devices, input modes, and abilities?

**Failure mode.** Beautiful screenshots conceal broken task flows.

- **D09.01 · UI generation** [established] — Generate page structure, components, forms, layouts, and styles from intent.
- **D09.02 · Visual feedback loops** [established] — Inspect screenshots or browser output, specify changes, and compare states.
- **D09.03 · Design systems** [established] — Reuse tokens, components, interaction patterns, and responsive conventions.
- **D09.04 · Accessibility** [established] — Evaluate semantics, keyboard use, focus states, labels, contrast, and assistive technology.
- **D09.05 · Responsive behavior** [established] — Verify flows on mobile, desktop, variable content, and constrained screens.
- **D09.06 · Interaction states** [established] — Handle loading, errors, empty states, confirmation, undo, and retries.
- **D09.07 · End-to-end journeys** [established] — Test meaningful user tasks rather than isolated components.
- **D09.08 · Multimodal agents** [emerging] — Combine text, images, screenshots, voice, and interface exploration with task specifications.

### How results earn trust (PROVE)

#### D10 — Verification & Evaluation

**Purpose.** Distinguish apparent success, test success, intended behavior, and safe operation.

**Diagnostic question.** What independent evidence would falsify the claim that this works?

**Failure mode.** Agents overfit visible tests, self-report success, or miss security flaws.

- **D10.01 · Unit and integration tests** [established] — Check local rules, contracts, database effects, and component interactions.
- **D10.02 · End-to-end tests** [established] — Exercise real user workflows in representative environments.
- **D10.03 · Static analysis** [established] — Apply type checking, linting, dependency and secret scans, and security rules.
- **D10.04 · Property and metamorphic tests** [established] — Test invariants over generated inputs, transformations, and edge cases.
- **D10.05 · Adversarial and mutation tests** [established] — Challenge hidden assumptions; mutate code or inputs to assess test sensitivity.
- **D10.06 · Independent code review** [established] — Review changes, requirements, attack surfaces, maintenance costs, and evidence.
- **D10.07 · Agent system evals** [emerging] — Measure full model + tools + context + harness + environment across repeated tasks.
- **D10.08 · Production feedback** [established] — Use telemetry, incident learning, regression checks, and user outcomes as ongoing evidence.

#### D11 — Security, Privacy & Governance

**Purpose.** Limit the blast radius of agent errors and attacks while retaining auditability.

**Diagnostic question.** What can this agent read, execute, change, publish, or exfiltrate?

**Failure mode.** Passing functional tests is not sufficient evidence of security.

- **D11.01 · Prompt injection defense** [established] — Do not treat untrusted retrieved content as instructions; constrain tool effects.
- **D11.02 · Least privilege** [established] — Use scoped credentials, temporary permissions, and restricted external services.
- **D11.03 · Secrets and data handling** [established] — Prevent sensitive content in prompts, logs, commits, tool outputs, and generated artifacts.
- **D11.04 · Supply chain assurance** [established] — Review packages, lockfiles, downloads, MCP servers, actions, and installation scripts.
- **D11.05 · Destructive action controls** [established] — Require explicit approval for deployment, payment, deletion, credential, or production changes.
- **D11.06 · Threat modeling** [established] — Analyze actors, assets, trust boundaries, abuse cases, and layered defenses.
- **D11.07 · Audit and attribution** [emerging] — Record what agent ran, with which instructions, permissions, tools, and approvals.
- **D11.08 · Governed autonomy** [emerging] — Set risk thresholds, rollback authority, alerting, kill switches, and human responsibility.

#### D12 — Delivery & Operations

**Purpose.** Turn a local result into a maintained service with controlled release and recovery.

**Diagnostic question.** Can we reproduce, deploy, monitor, and undo the change safely?

**Failure mode.** Shipping speed outpaces operational capability.

- **D12.01 · Version control** [established] — Use small atomic commits, branches, code reviews, history, and recoverable changes.
- **D12.02 · CI quality gates** [established] — Run reproducible lint, types, tests, scans, builds, and policy checks.
- **D12.03 · Environment parity** [established] — Make setup scripts, dependencies, configuration, and seed data reproducible.
- **D12.04 · Release strategies** [established] — Use previews, canaries, feature flags, staged rollout, and documented approvals.
- **D12.05 · Observability** [established] — Track logs, traces, metrics, meaningful service-level objectives, and diagnostic context.
- **D12.06 · Rollback and incident response** [established] — Have tested recovery, ownership, escalation, and post-incident learning.
- **D12.07 · Maintenance and upgrades** [established] — Budget for dependency updates, migrations, breaking APIs, and operational costs.
- **D12.08 · Continuous agent tasks** [emerging] — Automate scoped issue-to-PR or maintenance loops with human-approved merge/release boundaries.

### How the system learns and improves (ADAPT)

#### D13 — Economics & Measurement

**Purpose.** Measure realized product value, quality, and rework—not raw generation volume.

**Diagnostic question.** Is this approach actually improving delivery outcomes after review and rework?

**Failure mode.** Code output and subjective speed disguise downstream costs.

- **D13.01 · End-to-end cycle time** [established] — Measure discovery-to-validated-deployment time, including review and bug fixing.
- **D13.02 · Quality-adjusted throughput** [emerging] — Combine accepted useful work with regressions, incidents, and rework.
- **D13.03 · Token and compute cost** [established] — Track model spend, tool time, environment costs, and marginal returns.
- **D13.04 · Review load** [emerging] — Quantify human attention, agent supervision, queueing, and context switching.
- **D13.05 · Lead time and change failure** [established] — Measure delivery outcomes rather than lines of code or prompt counts.
- **D13.06 · Experiment design** [established] — Compare matched tasks with and without AI, account for task selection and confounders.
- **D13.07 · Bottleneck migration** [emerging] — Observe shifts from coding to specification, evaluation, integration, or operations.
- **D13.08 · Portfolio fit** [established] — Choose automation by expected value, reversibility, task clarity, and risk.

#### D14 — Learning & Expertise

**Purpose.** Preserve human understanding while using AI to amplify exploration and skill.

**Diagnostic question.** Can the creator diagnose, change, and own the system without blind dependence?

**Failure mode.** Immediate output quality is mistaken for lasting expertise.

- **D14.01 · Foundational mental models** [established] — Understand files, processes, state, APIs, databases, testing, security, and deployment.
- **D14.02 · Reading generated code** [established] — Explain critical paths, dependencies, state transitions, and failure modes.
- **D14.03 · Debugging practice** [established] — Form hypotheses, isolate cases, inspect evidence, and verify fixes.
- **D14.04 · Test literacy** [established] — Write acceptance criteria and meaningful tests that catch incorrect behavior.
- **D14.05 · AI as tutor** [established] — Ask for explanations, counterexamples, alternatives, and independent exercises.
- **D14.06 · Calibration** [emerging] — Learn when to trust, verify, delegate, escalate, or refuse a generated suggestion.
- **D14.07 · Cognitive offloading** [emerging] — Monitor both freed attention and loss of situation awareness or skill retention.
- **D14.08 · Team knowledge retention** [emerging] — Codify durable lessons in docs, skills, decisions, and reusable evaluations.

### Moving research frontier (FRONTIER)

#### D15 — Emergent Architectures

**Purpose.** Track high-leverage patterns moving from experiments to wider engineering practice.

**Diagnostic question.** What changes when work is organized around tasks, agents, and evidence instead of sessions?

**Failure mode.** Scaling agent count can scale coordination failures instead of useful work.

- **D15.01 · Harness-first design** [emerging] — Invest in executable constraints and feedback architecture rather than prompt wording alone.
- **D15.02 · Issue-tracker orchestration** [emerging] — Map scoped backlog items to isolated agent workspaces with reviewable completion artifacts.
- **D15.03 · Agent-friendly repositories** [emerging] — Write repo instructions, setup automation, tests, schemas, and review gates for agents.
- **D15.04 · Long-running work memory** [emerging] — Use durable progress files, commits, feature inventories, and reproducible sessions.
- **D15.05 · Multi-agent specialization** [emerging] — Separate implementation, security review, test generation, and integration where beneficial.
- **D15.06 · Computer-use development** [emerging] — Combine visual testing, browser actions, and software changes in one controlled loop.
- **D15.07 · Self-improving harnesses** [hypothesis] — Let agents propose harness/policy refinements, but require independent evaluation and human approval.
- **D15.08 · Executable specifications** [emerging] — Connect human intent, formal acceptance checks, fixtures, and tests in a traceable chain.

#### D16 — Knowledge Frontier & Unknowns

**Purpose.** Maintain distinctions between established practice, evidence-limited claims, and testable futures.

**Diagnostic question.** What is still unknown—and what observation would change our mind?

**Failure mode.** Vendor demonstrations and benchmark scores become unearned generalizations.

- **D16.01 · Benchmark contamination** [established] — Public solved-task benchmarks can leak into training and inflate apparent capability.
- **D16.02 · True productivity effect** [emerging] — Measure human-agent performance by task type and organization with credible controls.
- **D16.03 · Security correctness gap** [emerging] — Assess why functionally correct agent implementations remain vulnerable in real tasks.
- **D16.04 · Autonomy reliability frontier** [emerging] — Study how task horizon, complexity, dependency depth, and environment affect failure rates.
- **D16.05 · Trust calibration** [emerging] — Explore evidence formats that improve human judgment without overwhelming attention.
- **D16.06 · Formal verification integration** [hypothesis] — Test whether selected proof obligations can provide scalable guarantees for agent-produced code.
- **D16.07 · Agentic maintenance ecology** [hypothesis] — Study durable systems of agents that maintain software under policy with limited intervention.
- **D16.08 · Causal harness evaluation** [emerging] — Use ablations and randomized comparisons to learn which harness changes cause improvements.
- **D16.09 · Unknown unknowns** [hypothesis] — Design methods to surface failure classes absent from specifications, tests, and benchmarks.

## Typed dependencies (not just a category tree)

- D01 Definitions & Paradigms — **sets accountability frame** → D03 Humans, Roles & Agency
- D02 Product Intent & Value — **specifies intent for** → D04 Interaction & Prompt Design
- D02 Product Intent & Value — **defines expected behavior for** → D10 Verification & Evaluation
- D02 Product Intent & Value — **defines value criteria for** → D13 Economics & Measurement
- D03 Humans, Roles & Agency — **governs authority of** → D06 Agent Runtime & Harness
- D04 Interaction & Prompt Design — **requires context from** → D05 Context & Knowledge Architecture
- D05 Context & Knowledge Architecture — **feeds** → D06 Agent Runtime & Harness
- D07 Tools, Surfaces & Protocols — **exposes tools to** → D06 Agent Runtime & Harness
- D06 Agent Runtime & Harness — **executes changes in** → D08 Architecture, Data & Code
- D08 Architecture, Data & Code — **implements experience for** → D09 Experience & Multimodality
- D08 Architecture, Data & Code — **must be verified by** → D10 Verification & Evaluation
- D09 Experience & Multimodality — **requires journey validation** → D10 Verification & Evaluation
- D10 Verification & Evaluation — **does not replace** → D11 Security, Privacy & Governance
- D11 Security, Privacy & Governance — **constrains** → D06 Agent Runtime & Harness
- D10 Verification & Evaluation — **gates release in** → D12 Delivery & Operations
- D12 Delivery & Operations — **generates outcome metrics for** → D13 Economics & Measurement
- D13 Economics & Measurement — **feeds product decisions** → D02 Product Intent & Value
- D14 Learning & Expertise — **strengthens oversight** → D03 Humans, Roles & Agency
- D15 Emergent Architectures — **extends architectures of** → D06 Agent Runtime & Harness
- D16 Knowledge Frontier & Unknowns — **assesses evidence for** → D15 Emergent Architectures
- D16 Knowledge Frontier & Unknowns — **improves evaluation** → D10 Verification & Evaluation
- D11 Security, Privacy & Governance — **scopes access to** → D07 Tools, Surfaces & Protocols
- D12 Delivery & Operations — **updates operational knowledge** → D05 Context & Knowledge Architecture
- D13 Economics & Measurement — **tests value of** → D15 Emergent Architectures
- D14 Learning & Expertise — **improves instructions** → D04 Interaction & Prompt Design
- D10 Verification & Evaluation — **provides feedback to** → D06 Agent Runtime & Harness
- D16 Knowledge Frontier & Unknowns — **qualifies causal claims** → D13 Economics & Measurement

## Archetypal operating roles (inspired by Construct)

| Archetype | Owns | Failure to watch |
|---|---|---|
| Visionary | problem, value, user outcome | scope inflation |
| Architect | system boundaries and invariants | overcomplication |
| Builder | implementation within scope | unverified shortcuts |
| Skeptic | tests and falsification | test tunnel vision |
| Guardian | permissions, safety, blast radius | policy without enforcement |
| Steward | release, maintenance, learning | orphaned software |

These are role metaphors, not claims that an AI agent has independent moral or legal authority. One person may perform several roles.

## Risk-scaled assurance ladder

| Level | Example | Reasonable minimum control |
|---|---|---|
| A: Throwaway | Private, local visual prototype | Manual exploratory checks; no sensitive data; discard freely |
| B: Personal utility | Local scripts on non-sensitive files | Version control, unit tests, previews, rollback |
| C: Public-facing | A site or small SaaS feature | Auth review, input validation, E2E tests, logging, CI, deployment checks |
| D: Sensitive workflows | Personal data, permissions, payments | Threat model, least privilege, strong test evidence, independent review, human deployment approval |
| E: High consequence | Healthcare, critical infrastructure, safety/regulated processes | Domain experts, formal assurance where warranted, governance, incident readiness; do not rely on unreviewed agent-generated code |

## Practice loop with artifacts

1. Write a one-page intent brief: audience, problem, non-goals, important user journeys, acceptance criteria, risk tier.
2. Ask the agent to inspect the repository and return a scoped plan with unknowns, affected files, test strategy, and security implications.
3. Supply only relevant source-of-truth context; grant tools the least privilege needed.
4. Implement a reversible vertical slice; commit a small diff and update progress notes.
5. Test with unit/integration/E2E cases, adversarial inputs, accessibility checks, and security gates proportional to risk.
6. Require evidence, not self-reported success: command output, passing tests, reviewed diff, reproducible demo, and unresolved limitations.
7. Deploy via preview/staged release; monitor outcomes, incidents, cost, and user value.
8. Preserve learning in specs, tests, repository instructions, and harness improvements; retest after changes.


## Frontier research agenda: questions and discriminating tests

1. **What is the causal productivity effect of agents on different task classes?**  
   *Proposed discriminating test:* Randomized cross-over on representative tasks measuring shipped correctness and total human time.

2. **How far can coding agents operate reliably without oversight?**  
   *Proposed discriminating test:* Fresh, private tasks at varying complexity and time horizons with verified success and incident metrics.

3. **Can security assurance scale as fast as code generation?**  
   *Proposed discriminating test:* Threat-model-led hidden tests, exploit validation, and independent review on fresh tasks.

4. **Which harness components drive gains?**  
   *Proposed discriminating test:* Controlled ablation of context, tool access, tests, permissions, and checkpoints.

5. **When does multi-agent coordination outperform a strong single agent?**  
   *Proposed discriminating test:* Matched total budget comparison controlling for integration overhead and reviewer time.

6. **How can humans stay calibrated as they stop writing most code?**  
   *Proposed discriminating test:* Measure detection of seeded faults, architectural comprehension, and long-term learning.

7. **Could specifications become independently executable contracts?**  
   *Proposed discriminating test:* Compare natural-language criteria, formal constraints, and generated property tests on mutation suites.


## Evidence-based cautions

- A 2026 ICML benchmark reported a large gap between functionally correct and secure implementations in tested coding-agent configurations. This is evidence about those settings and tasks, not a universal security rate. [S8]

- METR reported a 19% completion-time slowdown in an early-2025 experiment on experienced open-source contributors; its Feb 2026 update found later data too selection-biased to support a reliable general speedup estimate. [S9]

- OpenAI concluded in Feb 2026 that SWE-bench Verified was contaminated enough that frontier results are misleading; prefer fresh, representative, task-specific evaluations. [S13]

- OWASP 2026 guidance treats goal hijacking, tool misuse, identity abuse, supply chain, and unexpected code execution as distinct agentic security concerns. [S10]


## Source register

- **[S1]** [Origin of term / Karpathy (2025)](https://simonwillison.net/2025/feb/6/andrej-karpathy/)
- **[S2]** [GitHub Spec Kit: specification-driven development](https://github.github.com/spec-kit/)
- **[S3]** [OpenAI: harness engineering (Feb 2026)](https://openai.com/index/harness-engineering/)
- **[S4]** [OpenAI: Symphony orchestration (Apr 2026)](https://openai.com/index/open-source-codex-orchestration-symphony/)
- **[S5]** [Anthropic: effective long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **[S6]** [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **[S7]** [Anthropic: demystifying agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- **[S8]** [ICML 2026: SUSVIBES security benchmark](https://proceedings.mlr.press/v306/zhao26ax.html)
- **[S9]** [METR: developer productivity experiment update (Feb 2026)](https://metr.org/blog/2026-02-24-uplift-update/)
- **[S10]** [OWASP: Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- **[S11]** [MCP specification: tools, security](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx)
- **[S12]** [Agent Skills standard](https://github.com/agentskills/agentskills)
- **[S13]** [OpenAI: limits of SWE-bench Verified (Feb 2026)](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- **[S14]** [DORA 2025: AI and software delivery](https://dora.dev/research/2025/dora-report/)
- **[S15]** [OpenAI: running Codex safely (May 2026)](https://openai.com/index/running-codex-safely/)
- **[S16]** [Anthropic: long-running app harnesses (Mar 2026)](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- **[S17]** [MCP specification (Jul 2026)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

## Maintenance protocol for this map

For each future change: record publication/event dates; identify the exact claim; trace the primary source; tag established/emerging/hypothesis; add an observable falsification or adoption criterion; recheck benchmark leakage and task distribution; update related nodes and edges; preserve superseded claims instead of silently rewriting history.

**Boundary:** This is a structured map of a changing field, not a claim to have exhaustively surveyed all 2026 products, tools, studies, or unpublished work.

