# Full-Stack Development Knowledge Atlas — 2026

**Scope:** web-centered full-stack engineering; transferable principles, not a mandated technology stack.
**Model:** 14 domains, 171 concepts, 287 typed edges (prerequisites plus lateral relationships).
**Knowledge maturity:** established = durable; evolving = usable but moving fast; emerging = promising yet context-dependent.

## Core architecture

User need → accessible browser interface → network / edge → trusted service / authorization → data / integrations → user feedback.

Security, testing, privacy, infrastructure, performance, observability, recovery, and governance cut across every step.

## Concept map

Each concept records its role, an independent proof of capability, and practical prerequisites.

### 01 · Computing foundations

Models of computation, the internet, and disciplined programming

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Systems thinking | P0 | established | Model actors, inputs, state, feedback, boundaries, and failure | Diagram a production request and its failure paths | — |
| Computational models | P0 | established | Explain CPU, memory, storage, bytes, encoding, and serialization | Trace a value from text input to bytes on disk | — |
| Operating systems & processes | P0 | established | Distinguish process, thread, file descriptor, signals, and permission | Debug a process and find a blocked port | Computational models |
| CLI & developer environment | P0 | established | Use shell, environment variables, editors, and local debugging | Reproduce a local environment from a README | Operating systems & processes |
| Git & version control | P0 | established | Explain commits, branches, merges, and history | Resolve a merge conflict and revert a bad commit | CLI & developer environment |
| Programming semantics | P0 | established | Use variables, types, control flow, functions, modules, and error handling | Build a CLI utility with robust input validation | Computational models |
| Data structures & algorithms | P0 | established | Choose representations and estimate time and space complexity | Explain why a query path is O(n) or O(log n) | Programming semantics |
| Asynchrony & concurrency | P1 | established | Understand event loops, promises, locking, races, and cancellation | Reproduce and fix a race condition | Programming semantics, Operating systems & processes |
| Networking & DNS | P0 | established | Understand IP, routing, DNS, TCP, UDP, and sockets | Diagnose a failed DNS lookup versus an unreachable server | Operating systems & processes |
| HTTP & TLS | P0 | established | Explain methods, headers, status codes, caching, cookies, and HTTPS | Trace a request through DNS, TLS, HTTP and response | Networking & DNS |
| JavaScript & TypeScript | P0 | established | Use modern JavaScript; TypeScript models contracts at compile time | Implement a typed module and runtime validation boundary | Programming semantics |
| Additional backend language | P2 | established | Learn one alternative ecosystem, e.g., Python, Go, Java, or C# | Expose equivalent HTTP handlers in two languages | Programming semantics |
| Dependency management | P1 | established | Use lockfiles, semver, reproducible installs, and advisories | Pin dependencies and identify a vulnerable transitive package | CLI & developer environment |
| Documentation literacy | P0 | established | Read specifications, source, advisories, and change logs | Justify a design choice with an official reference | Git & version control |

### 02 · Product & human needs

The people, problem, requirements, and experience

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Problem framing | P0 | established | Identify outcomes, constraints, actors, and non-goals | Write a one-page problem statement with success criteria | Systems thinking |
| User research & workflows | P1 | established | Map actual tasks, jobs-to-be-done, and failure journeys | Validate a flow with representative user scenarios | Problem framing |
| Domain modeling | P1 | established | Translate business language into entities, invariants, and policies | Document a domain rule and counterexample | Problem framing |
| Requirements & acceptance criteria | P0 | established | Distinguish functional, nonfunctional, and compliance requirements | Specify acceptance tests for a feature | Problem framing |
| Information architecture | P1 | established | Design navigation, findability, terminology, and content structure | Create a sitemap and navigation test | User research & workflows |
| Interaction design | P1 | established | Define states, focus, errors, feedback, and responsive transitions | Prototype loading, empty, error, and success states | Requirements & acceptance criteria |
| Accessible & inclusive UX | P1 | established | Account for keyboard, assistive technology, language, and varied devices | Conduct keyboard and screen-reader walkthroughs | Interaction design |
| Design systems | P2 | established | Define tokens, component contracts, patterns, and variants | Publish a reusable component with usage guidance | Interaction design |
| Internationalization | P2 | established | Separate messages, locales, formatting, directionality, and time zones | Localize a form with RTL and timezone handling | Interaction design |
| Product analytics & experiments | P2 | established | Design events, funnels, consent, and causal evaluation | Define a useful product metric without logging private data | Problem framing |
| Documentation & support UX | P1 | established | Treat help content, onboarding, and operations as part of product | Write a recovery path for a failed user task | Requirements & acceptance criteria |

### 03 · Web platform

The browser, standards, and network boundary

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Semantic HTML | P0 | established | Use native elements and document structure before custom roles | Build accessible forms and navigation without a framework | HTTP & TLS |
| CSS layout & responsive design | P0 | established | Understand cascade, box model, flex, grid, typography, and container queries | Ship a design that works at narrow and wide widths | Semantic HTML |
| DOM & browser events | P0 | established | Understand parsing, event propagation, focus, and DOM mutations | Debug an event capture or focus issue | JavaScript & TypeScript, Semantic HTML |
| Browser rendering pipeline | P1 | established | Model style, layout, paint, compositing, and main-thread work | Identify and eliminate layout thrashing | CSS layout & responsive design, DOM & browser events |
| Fetch & web requests | P1 | established | Work with headers, aborts, streaming, CORS, and request errors | Build a cancellable client with retry policy | HTTP & TLS, JavaScript & TypeScript |
| Browser security model | P1 | established | Understand origins, same-site context, CSP, cookies, and sandboxing | Explain why same-origin policy blocks a request | HTTP & TLS, DOM & browser events |
| Web storage & caching | P1 | established | Compare cookies, storage, Cache API, HTTP caches, and IndexedDB | Design offline storage without leaking secrets | Browser security model |
| Progressive enhancement | P1 | established | Start from accessible core behavior and add capabilities safely | Build a form that works without client JavaScript | Semantic HTML, Fetch & web requests |
| Browser compatibility / Baseline | P1 | established | Verify support across required devices and assistive tech | Replace an unsupported API or add a fallback | Documentation literacy, CSS layout & responsive design |
| Service workers & PWA | P2 | established | Explain offline strategies, update lifecycle, and installability | Build offline read-only support with versioned cache | Web storage & caching |
| Web Components | P3 | established | Understand custom elements, shadow DOM, and interop constraints | Package a framework-agnostic widget | DOM & browser events |

### 04 · Frontend engineering

Interactive, accessible, performant user interfaces

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Component architecture | P1 | established | Separate view, state, behavior, and reusable UI contracts | Build a composable accessible component | DOM & browser events, JavaScript & TypeScript |
| Frontend state ownership | P1 | established | Distinguish local UI, URL, server, and durable client state | Eliminate unnecessary duplicated state | Component architecture |
| Routing & navigation | P1 | established | Manage URL-driven state, nested layouts, history, and transitions | Make a deep link refresh and navigate correctly | Component architecture, HTTP & TLS |
| Forms & validation UX | P1 | established | Combine native constraints, server validation, errors, and a11y | Build a form that recovers from failed submission | Interaction design, Component architecture |
| Frontend API integration | P1 | established | Treat responses as untrusted, typed contracts with loading and retry states | Safely handle 401, 403, 429, and 5xx in UI | Fetch & web requests, Frontend state ownership |
| Rendering strategies | P2 | evolving | Choose client rendering, SSR, static generation, and hybrid routes | Explain SEO, latency, cache, and hydration tradeoffs | Browser rendering pipeline, Component architecture |
| Streaming & server components | P3 | evolving | Evaluate streaming HTML and server/client component boundaries | Reduce client bundle without leaking server secrets | Rendering strategies |
| Frontend accessibility engineering | P1 | established | Apply WCAG, keyboard navigation, focus, and semantic interaction | Pass keyboard testing and explain WCAG failures | Accessible & inclusive UX, Semantic HTML, Component architecture |
| UI performance | P2 | established | Optimize LCP, INP, CLS, code splitting, images, and rendering | Measure field metrics and improve a slow page | Browser rendering pipeline, Rendering strategies |
| Client-side resilience | P2 | established | Handle offline, backpressure, optimistic updates, and stale views | Recover an interrupted mutation without duplicate effects | Frontend API integration |
| Frontend testing | P2 | established | Test components, flows, a11y, browser behavior, and regressions | Write an end-to-end test from user intent | Component architecture, Requirements & acceptance criteria |
| SEO & metadata | P2 | established | Model crawlability, canonical URLs, structured data, and redirects | Validate indexing of a public page | Rendering strategies |

### 05 · Backend & API engineering

Trusted business logic, contracts, and workflows

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Request lifecycle | P1 | established | Trace middleware, parsing, routing, business logic, response, and error propagation | Follow one API request through each layer | HTTP & TLS, Programming semantics |
| Service & domain boundaries | P1 | established | Keep core business rules separate from transport and infrastructure | Refactor a controller with explicit domain rules | Domain modeling, Request lifecycle |
| HTTP API design | P1 | established | Design resources, methods, pagination, filtering, versions, and errors | Produce a consistent REST-style API contract | Request lifecycle |
| API contracts & schema | P1 | established | Use OpenAPI, JSON Schema, and compatibility rules | Validate provider and consumer against one schema | HTTP API design |
| GraphQL & RPC | P3 | established | Know selection-based and procedure-based protocols with tradeoffs | Explain when GraphQL or gRPC is warranted | HTTP API design |
| Input validation | P1 | established | Parse, constrain, normalize, and reject hostile or malformed inputs | Design tests for malformed and overlong inputs | Request lifecycle |
| Authentication integration | P1 | established | Verify identity via sessions, identity providers, or tokens | Implement a secure session lifecycle | Request lifecycle, Browser security model |
| Authorization enforcement | P1 | established | Enforce per-object, per-field, role and tenant boundaries server-side | Demonstrate blocked cross-user object access | Authentication integration, Domain modeling |
| Idempotency & retries | P2 | established | Make mutation retries safe and account for partial failure | Prevent duplicate order creation under retry | HTTP API design, Service & domain boundaries |
| Caching patterns | P2 | established | Use HTTP, CDN, application and cache-aside strategies with invalidation | Explain the source of truth and stale-data policy | HTTP API design |
| Queues & background jobs | P2 | established | Handle asynchronous tasks, retries, dead letters, and delivery semantics | Process a task safely after duplicate delivery | Idempotency & retries |
| Real-time systems | P3 | established | Compare WebSockets, SSE, polling, and backpressure | Stream progress with reconnection behavior | HTTP API design, Asynchrony & concurrency |
| File uploads & media | P2 | established | Use direct uploads, object storage, limits, and content validation | Upload a file without storing blobs in the app DB | Input validation |
| Webhooks & external integrations | P2 | established | Verify signatures, handle replay, retries, and provider outages | Consume a duplicate signed webhook once in effect | Idempotency & retries, Input validation |
| Rate limits & quotas | P2 | established | Bound abuse and resource consumption by principal and operation | Return predictable 429 behavior with quotas | Authentication integration, Request lifecycle |
| Schedulers & workflow state | P3 | established | Distinguish cron, durable work queues, and compensating flows | Implement recoverable multi-step background work | Queues & background jobs |

### 06 · Data & information systems

Durable state, retrieval, and consistency

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Relational data modeling | P1 | established | Define entities, keys, relationships, uniqueness, and constraints | Normalize a schema and enforce critical invariants | Domain modeling |
| SQL & query semantics | P1 | established | Write joins, aggregates, filters, CTEs, and parameterized statements | Answer product questions with correct SQL | Relational data modeling |
| Schema migrations | P2 | established | Evolve schema and data safely across rolling deployments | Apply backward-compatible migration and rollback plan | Relational data modeling, Git & version control |
| Transactions & isolation | P2 | established | Understand atomicity, isolation levels, deadlocks, and anomalies | Prevent a lost update or double spend | SQL & query semantics, Asynchrony & concurrency |
| Indexes & query planning | P2 | established | Evaluate selectivity, execution plans, and index costs | Optimize a slow query with EXPLAIN | SQL & query semantics |
| Data integrity & invariants | P2 | established | Decide which rules belong in schema, domain logic, or workflow | Enforce a uniqueness rule under concurrent requests | Relational data modeling, Transactions & isolation |
| Backups & restoration | P2 | established | Know RPO/RTO, snapshots, PITR, and restore tests | Restore a deleted dataset in a disposable environment | Schema migrations |
| NoSQL data models | P3 | established | Choose document, key-value, graph, or wide-column where appropriate | Explain why a model fits access patterns | Relational data modeling |
| Redis & ephemeral state | P2 | established | Use a cache/queue/store with TTL and consistency awareness | Implement safe caching with expiration | Caching patterns |
| Search & retrieval | P2 | established | Distinguish full-text, inverted indexes, facets, and semantic retrieval | Add search with relevance tests | SQL & query semantics |
| Object storage | P2 | established | Manage binary objects, URLs, permissions, and lifecycle | Implement private expiring download links | File uploads & media |
| Event-driven data integration | P3 | established | Compare transactional outbox, CDC, and event replay | Prevent lost domain events on DB commit | Transactions & isolation, Queues & background jobs |
| Data lifecycle & governance | P2 | established | Plan retention, deletion, provenance, access, and residency | Implement a deletion and retention policy | Relational data modeling |

### 07 · Security, identity & privacy

Risk management and enforceable trust boundaries

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Threat modeling | P1 | established | Identify assets, adversaries, entry points, trust boundaries, and mitigations | Threat-model a login and upload flow | Systems thinking, Request lifecycle |
| OWASP web/API risks | P1 | established | Understand common web and API failure classes | Detect an object authorization bug before release | Threat modeling, Authorization enforcement |
| Injection defenses | P1 | established | Use parameterization, contextual encoding, safe templating, and isolation | Demonstrate a prevented SQL injection | Input validation, SQL & query semantics |
| XSS, CSRF & browser defenses | P1 | established | Apply CSP, correct encoding, SameSite, anti-CSRF, and safe DOM APIs | Explain and test a cross-site request or script path | Browser security model, Authentication integration |
| CORS vs authorization | P1 | established | Know CORS is browser access policy, not API permission | Prove a CORS header cannot protect a private endpoint | Browser security model, Authorization enforcement |
| SSRF & egress protection | P2 | established | Validate outbound destinations and defend internal network access | Block metadata service access via URL fetch | Threat modeling, Webhooks & external integrations |
| OAuth 2.0 & OIDC | P2 | established | Distinguish authorization from authentication; implement PKCE and scopes | Draw a secure sign-in and token-flow sequence | Authentication integration |
| Session & credential security | P1 | established | Protect cookies, rotate credentials, mitigate fixation, revoke sessions | Implement secure logout and session invalidation | Authentication integration |
| Passkeys & WebAuthn | P3 | evolving | Understand challenge-response, relying-party scope, and recovery | Explain server verification and account recovery | Authentication integration, OAuth 2.0 & OIDC |
| Authorization models | P2 | established | Compare RBAC, ABAC, ReBAC, policy evaluation and deny defaults | Test tenancy across nested resources and actions | Authorization enforcement |
| Secrets & key management | P2 | established | Separate credentials from code, rotate, audit, and scope service identities | Rotate a leaked key without source changes | Dependency management, Threat modeling |
| Cryptography & transport | P2 | established | Use TLS and vetted primitives; manage keys and understand encryption limits | Explain why hashing differs from encryption | HTTP & TLS, Threat modeling |
| Supply-chain security | P2 | evolving | Use SBOM, provenance, pinned builds, review and vulnerability handling | Produce and verify a build attestation | Dependency management, Threat modeling |
| Privacy & data minimization | P2 | established | Limit collection, retention, logging, and access to personal data | Audit fields stored for a user journey | Data lifecycle & governance, Threat modeling |
| Security monitoring & response | P3 | established | Generate actionable audit trails; triage and contain incidents | Reconstruct a suspicious privileged operation | Threat modeling, Structured logs & correlation |

### 08 · Testing & quality

Evidence that the system behaves as intended

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Test strategy & pyramid | P1 | established | Choose tests by risk, speed, fidelity, and maintenance costs | Write a test plan with explicit critical scenarios | Requirements & acceptance criteria |
| Unit & property-based tests | P1 | established | Test pure logic, invariants, boundaries, and generated cases | Catch a subtle boundary-condition bug | Programming semantics, Test strategy & pyramid |
| Integration & database tests | P2 | established | Test real boundaries with isolated databases or services | Verify a transaction and constraint together | Test strategy & pyramid, Relational data modeling |
| End-to-end journey tests | P2 | established | Verify critical workflows in a real browser and environment | Cover registration-to-completion journey | Test strategy & pyramid, Frontend testing |
| Contract & compatibility tests | P2 | established | Detect breaking change between clients, services, and events | Prevent release of an incompatible API schema | API contracts & schema, Test strategy & pyramid |
| Static analysis & type checks | P1 | established | Catch defects with linters, types, dependency and code scanners | Enforce automated checks on pull requests | JavaScript & TypeScript, Git & version control |
| Accessibility QA | P2 | established | Combine automated rules with manual keyboard and AT testing | Record defects found in an assistive-technology test | Frontend accessibility engineering |
| Performance & load testing | P3 | established | Model realistic traffic, p95/p99 latencies, bottlenecks, and saturation | Find a throughput collapse before release | UI performance, Request lifecycle |
| Security verification | P2 | established | Combine dependency scans, DAST/SAST, tests, and manual review | Validate a broken-access-control fix | OWASP web/API risks, Test strategy & pyramid |
| Continuous integration quality gates | P2 | established | Keep build, test, lint, audit, and artifact checks deterministic | Fail a release candidate before it reaches production | Static analysis & type checks, Test strategy & pyramid |
| Release confidence & rollback | P2 | established | Define smoke tests, progressive rollout checks, and recovery | Revert a breaking deployment under controlled conditions | Continuous integration quality gates |

### 09 · Infrastructure & delivery

Reproducible production environments and releases

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Linux & process operations | P1 | established | Inspect files, permissions, services, networking, and resource use | Diagnose a production-like Linux host | Operating systems & processes |
| Cloud primitives | P1 | established | Distinguish compute, networking, managed DB, queues, storage, and IAM | Sketch a minimal cloud deployment with costs | Networking & DNS, Request lifecycle |
| Containers & immutable images | P2 | established | Build reproducible images and run isolated processes | Create a small multi-stage container build | Linux & process operations, Dependency management |
| Environment configuration | P2 | established | Separate build-time config, runtime secrets, and per-env identity | Move same artifact across staging and production | Containers & immutable images |
| CI/CD pipelines | P2 | established | Automate verification, artifact building, provenance, and deployment | Release from version control with review gates | Continuous integration quality gates |
| Deployment strategies | P2 | established | Compare rolling, blue-green, canary, and feature flag releases | Roll out and roll back with health checks | CI/CD pipelines |
| DNS, CDN & edge delivery | P2 | established | Use DNS, TLS termination, caching, assets, and geographic routing | Measure impact of CDN caching on user latency | Networking & DNS, Caching patterns |
| Infrastructure as code | P2 | established | Version declarative infrastructure with review and state controls | Provision repeatable environments in code | Cloud primitives, Git & version control |
| Serverless & managed platforms | P2 | evolving | Explain cold starts, limits, billing, and managed tradeoffs | Deploy an API with appropriate runtime limits | Cloud primitives |
| Container orchestration | P3 | established | Understand scheduling, scaling, probes, services, and operators | Operate a containerized service with health probes | Containers & immutable images |
| Networking & zero trust basics | P3 | established | Segment systems and authorize service-to-service access | Restrict DB access to the serving workload | Cloud primitives, Authorization models |
| Cost, efficiency & FinOps | P3 | established | Account for spend per request, egress, idle capacity, and storage | Find an avoidable recurring cloud cost | Cloud primitives, Performance & load testing |
| Regionality & disaster design | P3 | established | Consider latency, data residency, failover, and recovery objectives | Explain region selection and failure assumptions | Backups & restoration, Cloud primitives |

### 10 · Reliability & operations

Observability, resilience, and incident learning

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Structured logs & correlation | P2 | established | Emit safe, searchable events with request and trace IDs | Trace one failed request without exposing secrets | Request lifecycle |
| Metrics & tracing | P2 | established | Observe latency, traffic, error rate, saturation, and distributed spans | Find the slow dependency of an API request | Structured logs & correlation |
| SLI, SLO & error budgets | P3 | established | Connect reliability targets to user-visible outcomes and risk | Define one SLO with an actionable error budget | Metrics & tracing, Requirements & acceptance criteria |
| Alerting & on-call | P3 | established | Alert on actionable symptoms rather than noisy component events | Design a page-worthy alert with an owner | SLI, SLO & error budgets |
| Incident response | P3 | established | Detect, mitigate, communicate, and review failures without blame | Run an outage tabletop with timeline | Alerting & on-call |
| Runbooks & operational readiness | P2 | established | Document ownership, recovery, dependencies, and procedures | Restore a service using a runbook | Structured logs & correlation, Backups & restoration |
| Capacity & saturation | P3 | established | Understand queues, CPU, memory, connections, limits, and scaling | Diagnose tail latency under load | Performance & load testing, Metrics & tracing |
| Timeouts, retries & circuit breakers | P3 | established | Bound cascading failure with deadlines, backoff, and bulkheads | Prevent retry storms under dependency outage | Idempotency & retries, Metrics & tracing |
| Graceful degradation | P3 | established | Maintain safe core behavior when dependencies or features fail | Serve read-only fallback during outage | Timeouts, retries & circuit breakers |
| Disaster recovery & game days | P3 | established | Test backups, failover, RTO/RPO and incident coordination | Complete a rehearsed restore and record gaps | Backups & restoration, Incident response |
| Telemetry governance | P3 | established | Control cardinality, PII, sampling, storage, and instrumentation drift | Remove sensitive data from a trace pipeline | Metrics & tracing, Privacy & data minimization |

### 11 · Architecture & scale

Boundaries, tradeoffs, and distributed behavior

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Modular monolith | P2 | established | Build cohesive boundaries before distributing deployment units | Design modules with explicit dependency rules | Service & domain boundaries, Domain modeling |
| Architectural decision records | P2 | established | Record context, alternatives, forces, and consequences | Write a falsifiable architecture tradeoff decision | Documentation literacy, Requirements & acceptance criteria |
| Service decomposition | P3 | established | Partition domains by ownership and independent change needs | Explain whether splitting a service creates net value | Modular monolith |
| Distributed systems fundamentals | P3 | established | Understand partial failure, message delay, retries, clocks, and duplication | Diagnose a network timeout with unknown completion | Networking & DNS, Asynchrony & concurrency |
| Consistency & coordination | P3 | established | Distinguish linearizability, eventual consistency, isolation, and causality | Choose consistency for inventory versus activity feeds | Transactions & isolation, Distributed systems fundamentals |
| Messages & delivery semantics | P3 | established | Explain at-most-once, at-least-once, deduplication and ordering | Make a consumer safe under reordered duplicates | Queues & background jobs, Distributed systems fundamentals |
| Transactional outbox & sagas | P3 | established | Connect state changes to events and coordinate compensations | Design failure recovery for multi-service payment | Event-driven data integration, Messages & delivery semantics |
| CQRS & event sourcing | P3 | established | Separate read/write models or persist events only when justified | Compare ordinary CRUD with an event-sourced design | Domain modeling, Event-driven data integration |
| Microservices tradeoffs | P3 | established | Weigh deployment autonomy against latency, operations, and data coupling | Propose conditions under which a split is justified | Service decomposition, Distributed systems fundamentals |
| Scaling & load balancing | P3 | established | Understand horizontal scaling, statelessness, hotspots, and partitions | Identify a bottleneck and test a scaling hypothesis | Capacity & saturation, Distributed systems fundamentals |
| Design for maintainability | P2 | established | Manage coupling, cohesion, testability, dependency direction and evolution | Replace a dependency without rewriting business rules | Modular monolith, Test strategy & pyramid |
| Platform & internal developer experience | P3 | evolving | Standardize paved roads, templates, secrets, and observability | Measure onboarding and safe deployment time | Infrastructure as code, CI/CD pipelines |

### 12 · Team & lifecycle

Collaboration, ownership, governance, and decisions

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Git collaboration & review | P1 | established | Use trunk-compatible branching, small PRs, and constructive review | Review a change for correctness, operability, and risk | Git & version control |
| Iterative delivery & feedback | P1 | established | Deliver thin vertical slices and adjust from real outcomes | Ship a narrow feature, measure use, iterate | Requirements & acceptance criteria, Git collaboration & review |
| Technical writing & diagrams | P1 | established | Communicate architecture, assumptions, changes, and incidents | Produce a C4 context diagram and precise README | Documentation literacy, Systems thinking |
| Ownership & operational handoff | P3 | established | Define service ownership, on-call, support, and maintenance obligations | Transfer ownership with deploy and incident instructions | Runbooks & operational readiness |
| Prioritization & risk | P2 | established | Separate reversible decisions from high-impact risks and dependencies | Rank work by user value, urgency, uncertainty, and cost | Problem framing, Threat modeling |
| Technical debt management | P3 | established | Make tradeoffs explicit and repay debt with evidence | Create a refactor proposal tied to system outcomes | Design for maintainability |
| Ethical & responsible engineering | P3 | established | Balance accessibility, privacy, user agency, sustainability, and safety | Identify the people harmed by a design choice | Privacy & data minimization, Accessible & inclusive UX |
| Knowledge maintenance | P3 | established | Monitor changing standards, deprecations, vulnerabilities, and evidence | Replace an obsolete recommendation in a team playbook | Documentation literacy, Supply-chain security |

### 13 · AI-native applications

Building with models, tools, retrieval, and evaluation

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| AI-assisted development | P2 | evolving | Use model output as draft evidence, not proof of correctness | Review, test, and explain an AI-written code change | Git & version control, Test strategy & pyramid |
| Coding agents & delegated tasks | P3 | evolving | Scope repos, tools, permissions, tests, and review checkpoints | Delegate a bounded issue with verified patch | AI-assisted development, Continuous integration quality gates |
| LLM API fundamentals | P2 | evolving | Understand inference requests, tokens, latency, cost, and limits | Build a reliable request handler with timeout and budget | HTTP API design, Rate limits & quotas |
| Structured model outputs | P2 | evolving | Validate generated JSON against schemas and business constraints | Reject invalid or unsafe model responses deterministically | LLM API fundamentals, Input validation |
| Embeddings & semantic search | P3 | evolving | Explain vector similarity, indexing, reranking, and retrieval quality | Benchmark search with a human-labeled query set | Search & retrieval |
| Retrieval-augmented generation | P3 | evolving | Ground model responses in retrieved, permission-checked material | Answer with verifiable citations and access filtering | Embeddings & semantic search, LLM API fundamentals |
| LLM evaluation & observability | P3 | evolving | Test task success, grounding, safety, regressions, drift, cost | Maintain repeatable evaluation cases and traces | Structured model outputs, Metrics & tracing |
| Tool calling & orchestration | P3 | evolving | Validate tool schemas, manage state, idempotency, timeouts, and approvals | Safely retry a non-destructive tool workflow | Structured model outputs, Webhooks & external integrations |
| Model Context Protocol | P4 | evolving | Understand interoperable tools/resources/prompts and authorization | Serve a constrained tool and verify its permissions | Tool calling & orchestration, OAuth 2.0 & OIDC |
| Agent authority & human control | P3 | evolving | Separate proposed actions from permissions and approval gates | Stop an agent from invoking a privileged tool | Tool calling & orchestration, Authorization models |
| Prompt injection & data exfiltration | P3 | evolving | Treat retrieved documents and tool output as untrusted instructions | Demonstrate a blocked prompt-injection path | Agent authority & human control, Threat modeling |
| Conversation memory & privacy | P4 | evolving | Bound retention, consent, retrieval, and tenant segregation | Remove a user memory without affecting other tenants | Retrieval-augmented generation, Privacy & data minimization |
| AI cost & reliability | P3 | evolving | Account for token budgets, caching, fallback, and quality thresholds | Compare quality-adjusted cost across model options | LLM evaluation & observability |

### 14 · Emerging research frontier

Promising developments whose adoption is context-dependent

| Concept | Phase | Maturity | What it means | Demonstrate | Prerequisites |
|---|---|---|---|---|---|
| Local-first & CRDT sync | P4 | emerging | Explore offline-first replicas, conflicts, merges, and identity | Prototype concurrent offline edits and reconciliation | Service workers & PWA, Consistency & coordination |
| Edge execution & state placement | P4 | evolving | Evaluate workloads near users, cache, compute, and data location | Benchmark an edge versus centralized route | DNS, CDN & edge delivery, Distributed systems fundamentals |
| WebAssembly & WASI components | P4 | evolving | Study portable sandboxed execution and system interfaces | Run a sandboxed module and inspect capability limits | Programming semantics, Browser security model |
| WebGPU & on-device inference | P4 | emerging | Explore browser GPU compute, device availability, and privacy tradeoffs | Benchmark a GPU workload with safe fallback | Browser compatibility / Baseline, UI performance |
| Privacy-preserving computation | P4 | emerging | Explore confidential compute, federated analysis, and selective disclosure | Specify a privacy threat model for a data-sharing system | Cryptography & transport, Privacy & data minimization |
| Formal methods & software verification | P4 | evolving | Use state machines, contracts, property tests, and bounded models | Find an invariant violation with a model checker | Data structures & algorithms, Unit & property-based tests |
| Post-quantum migration readiness | P4 | evolving | Inventory cryptography and plan for algorithmic transitions | Map externally exposed crypto dependencies | Cryptography & transport |
| Agentic software delivery governance | P4 | emerging | Study autonomous workflows, auditability, review, and rollback | Define evidence required before an agent deploys | Coding agents & delegated tasks, Agent authority & human control |
| Multimodal & adaptive interfaces | P4 | emerging | Explore voice, vision, spatial, and model-driven UI with accessibility | Prototype one alternative modality and fallback | Accessible & inclusive UX, LLM API fundamentals |
| Sustainable systems engineering | P4 | evolving | Measure efficiency per successful task; weigh compute and data costs | Reduce workload energy/cost without worsening user outcomes | Cost, efficiency & FinOps, SLI, SLO & error budgets |
| Frontier evidence discipline | P4 | established | Distinguish standard, shipped API, benchmark, research, and speculation | Record source, date, confidence, and falsifying test | Knowledge maintenance, Architectural decision records |

## Five evidence milestones

### 01 · Foundations proof

Build an accessible, responsive, no-framework site and a CLI tool; deploy the site over HTTPS.

**Knowledge:** Semantic HTML, CSS layout & responsive design, JavaScript & TypeScript, HTTP & TLS, Git & version control

**Exit evidence:** Accessible forms, correct navigation, test output, clean Git history and deployment.

### 02 · A working vertical slice

Build a multi-user task/booking app: browser → API → relational DB, with auth and authorization.

**Knowledge:** Frontend API integration, HTTP API design, Authorization enforcement, SQL & query semantics, Test strategy & pyramid

**Exit evidence:** A complete workflow, validated requests, authorization tests, and database constraints.

### 03 · Production confidence

Make the product secure, maintainable, observable, reproducible and safe to release.

**Knowledge:** Schema migrations, OWASP web/API risks, CI/CD pipelines, Metrics & tracing, Backups & restoration

**Exit evidence:** CI quality gates, a threat model, migration/rollback, alerts, and a successful restore drill.

### 04 · Failure and scale

Introduce background work and external integrations, then simulate outages and load.

**Knowledge:** Queues & background jobs, Transactions & isolation, Timeouts, retries & circuit breakers, SLI, SLO & error budgets, Architectural decision records

**Exit evidence:** Duplicate-safe jobs, tested failure modes, service-level targets, and documented tradeoffs.

### 05 · Evidence-driven frontier

Add a permission-scoped AI assistant that retrieves approved data and uses controlled tools.

**Knowledge:** Retrieval-augmented generation, LLM evaluation & observability, Agent authority & human control, Prompt injection & data exfiltration, Frontier evidence discipline

**Exit evidence:** Human approval for consequential actions, an eval dataset, attack tests, budget, and audit trail.

## Decisions

| Area | Default | When to change it |
|---|---|---|
| Application shape | Modular monolith first | Split into microservices only when independent scaling, ownership, or release needs outweigh distributed failure costs. |
| Primary database | Relational database by default | Choose alternatives for a demonstrated data/access pattern; design constraints, migrations and recovery. |
| Frontend rendering | Choose per route | Static pages for durable content, SSR for dynamic first-load needs, CSR for highly interactive areas; weigh hydration and cache. |
| State placement | Each state has one clear owner | Use URL for navigation, component for ephemeral interaction, service/DB for authoritative state, cache for derived copies. |
| API boundary | HTTP/JSON plus explicit schema by default | GraphQL or RPC when clients and requirements justify their complexity. |
| Delivery | Managed platform before cluster operations | Adopt orchestration as an operational response, not a rite of passage. |
| AI integration | Start with deterministic workflow | Introduce LLM only where probabilistic generation/retrieval adds value; measure correctness and harm. |
| Optimization | Measure a bottleneck before optimizing | User-perceived latency, failure rate, developer time, security risk, and cost matter more than novelty. |

## Evidence and primary references

1. [WHATWG HTML Living Standard](https://html.spec.whatwg.org/dev/) — Canonical browser/document semantics.
2. [MDN Web Platform Baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) — Cross-browser availability, not a substitute for testing.
3. [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — Accessibility principles and success criteria.
4. [web.dev Web Vitals](https://web.dev/articles/vitals) — User-centric loading, responsiveness and stability metrics.
5. [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — Isolation and serialization anomalies.
6. [OWASP Top 10:2025](https://top10.owasp.org/2025/) — Common web application risks.
7. [OWASP API Security Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/) — API-specific authorization and business logic risks.
8. [IETF RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) — OAuth 2.0 security best current practice.
9. [SLSA v1.2](https://slsa.dev/spec/v1.2/) — Software supply-chain guarantees and provenance.
10. [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) — Shared telemetry vocabulary across signals.
11. [Google SRE Workbook & guidance](https://sre.google/sre-book/service-best-practices/) — SLOs, error budgets, production reliability.
12. [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — Secure development lifecycle practices (final edition).
13. [DORA State of AI-assisted Dev 2025](https://dora.dev/research/2025/dora-report/) — AI amplifies organizational strengths and weaknesses.
14. [OWASP GenAI LLM Top 10 2025](https://genai.owasp.org/llm-top-10/) — Prompt injection, unsafe output, sensitive-data risk.
15. [OWASP Agentic AI Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — Security risks and safeguards for autonomous workflows.
16. [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28) — Interoperability and authorization for agent tools.
17. [W3C WebGPU specification](https://www.w3.org/TR/webgpu/) — Candidate Recommendation Draft; browser GPU compute.
18. [CNCF 2026 Cloud Native Survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) — Production adoption context, not a beginner requirement.
19. [WebAuthn Level 3 W3C](https://www.w3.org/TR/webauthn-3/) — Strong public-key authentication and passkey primitives.
20. [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) — Developer ecosystem trend signal.

## Method & caveats

This is a curated knowledge graph and developmental scaffold, not a consensus standard or causal evaluation. All directed prerequisites were validated to form an acyclic graph. The mastery checklist in the HTML app is browser-local; no data is transmitted. Technologies evolve faster than fundamentals; refresh emerging claims and standards before committing to a project.
