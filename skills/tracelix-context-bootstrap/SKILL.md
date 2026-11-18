---
name: tracelix-context-bootstrap
description: "Bootstrap connected product knowledge from a local checkout for coding-agent context and impact discovery. Map capabilities, behavioral rules, and functional/service dependencies with exhaustive API/messaging accounting and source evidence; generate KB articles and track native MCP ingestion. Use for repository onboarding or initial KB generation; ordinary code changes use the development workflow."
---

# Tracelix Context Bootstrap

Build initial repository and product knowledge without requiring articles from
earlier sessions. Execute only these four stages: readiness checks, repository
mapping, KB generation, and ingestion submission/tracking. Stop after reporting
ingestion outcomes. Do not call `ask_context_graph`, run usefulness acceptance
checks, declare the graph ready for development, or begin a development task.

Produce a source-grounded knowledge-graph description: named entities with exact
ontology types and concise descriptions of their actual roles, plus directed,
typed relationships with concise descriptions of what each connection does.
Names, types, and source anchors alone are not sufficient knowledge.

Organize knowledge around capabilities, behavioral rules, and functional or
service dependencies that a coding agent could otherwise overlook. Connect what
the product enables to its realization, architectural ownership, and governing
constraints. The graph enriches code inspection and impact discovery; it does not
replace reading current code. Code locations provide evidence and inspection
anchors, not substitutes for these semantic connections.

Discover capabilities first through application entry points, communication
contracts, configuration, and operational behavior. Enumerate API operations and
messaging bindings before tracing their implementations. Every discovered contract must have a recorded
disposition; article size or perceived importance must not silently remove
endpoints from coverage. Context discovery is also required, including behavior
not reachable from a contract. Exhaustive contract accounting and implementation
provenance support semantic knowledge coverage but do not establish it.

Use native Tracelix MCP tools. Read [references/ingestion.md](references/ingestion.md)
for tool contracts, readiness limitations, and submission tracking. Read
[references/kb-articles.md](references/kb-articles.md) and the shared
[structured knowledge contract](references/structured-knowledge.md) before authoring artifacts.

## 1. Check Readiness

- Resolve the repository and applicable AGENTS.md instructions. Use the current
  working tree; record commit and dirty state. Preserve existing local artifacts.
- Discover get_context_readiness, get_context_ontology, submit_context_knowledge,
  get_context_ingestion_run and list_context_ingestion_runs. Call
  `get_context_readiness({})`; a successful response confirms the connection.
  If `ready` is false, report its message and preserve local work until setup is
  complete. On a tool error or missing tool, report the blocker.
- Obtain the live ontology before mapping or generation. Its complete active term
  catalog is the only source for classification and endpoint rules. If retrieval
  fails, preserve work, stop affected generation/submission and report the blocker.
- Readiness does not call model providers or guarantee later execution. Handle
  actual submission/run errors as they occur; do not inspect backend settings,
  submit dummy data, or change configuration to test the connection.
- If the structured tool is absent, continue source inspection and artifact
  generation only when the ontology was retrieved. Leave artifacts pending;
  never fall back to text extraction or invent another connector.

## 2. Discover Context, Inventory Contracts, and Trace Dependencies

- Read [references/context-mapping.md](references/context-mapping.md) for entry-point
  discovery, knowledge synthesis, and semantic coverage. Inspect applicable
  UI routes/navigation and significant actions, CLI commands, jobs, and event
  triggers independently of API reachability. Record inspected roots, availability
  conditions, and unresolved boundaries; do not inventory every control or helper.
- Build a capability map from observed product behavior and investigate its
  realization, domain rules, and service prerequisites. Deliberately inspect
  independent configuration/initialization paths, operational tools, lifecycle
  conditions, and producer/consumer assumptions, not only direct callers.
- Read [references/contract-mapping.md](references/contract-mapping.md) for contract
  discovery, per-operation tracing, reconciliation, and the coverage ledger.
  Start with `rg --files`, manifests, entry points, contract definitions, router
  registrations, messaging bindings, and deployment configuration. Inventory all
  in-scope API operations and queue/topic producer and consumer bindings before
  tracing implementations. Documentation is optional input.
- Respect ignore rules. Exclude credentials, environment secrets, dependency
  directories, generated implementation bodies, build output, binary assets, and
  bootstrap output. Read generated contract declarations only when needed to
  reconcile the actual interface surface. Keep representative tests as evidence.
  Do not execute repository code or install an indexing service just to explore it.
- Reconcile declared APIs with mounted routes and message schemas with actual
  publishers, subscriptions, and worker configuration. Keep unmatched declarations,
  implementation-only operations, and unresolved dynamic registrations visible.
  Record discovery boundaries and gaps; do not call a partial scan complete.
- For every inventoried operation or messaging binding, establish its observed
  purpose, inputs/outputs, workflow, handler or producer, collaborators, state
  changes, and defining files. Follow imports and actual calls outward from each
  contract, expanding targeted reads instead of loading the whole repository.
  Record branches and error/lifecycle behavior that materially change its meaning.
- For each candidate entity, inspect its implementation or authoritative behavioral
  evidence and relevant use sites to explain what it does, what it acts on or
  produces, and its responsibility in the system.
  For each candidate relationship, establish its actual interaction or shared
  behavioral rule. Logical dependencies may be synthesized from evidence across
  implementations without a direct call. Inspect both sides and explain the
  connection, conditions, and consequences; an import or a generic dependency
  label does not explain a link.
- Connect observed capabilities to their entry points, relevant components, domain
  concepts, and constraints. Inspect consumers and providers as needed to establish
  shared UI infrastructure, authorization, ownership/scope, lifecycle coupling,
  data dependencies, and downstream effects. Imports, similar names, shared storage,
  and visual similarity alone do not establish behavioral coupling or intended reuse.
  Keep source symbols and locations as evidence; neither every discovery item nor
  every internal function needs its own graph entity.
- Connect functionality to its realizing components, interfaces, and UI where
  supported. Establish endpoint providers, aggregate API membership, and purpose
  independently of declaring files. Distinguish observed behavior, enforced
  constraints, and documented alignment requirements; a reason to review another
  area does not by itself mean both implementations must change.
- Classify candidate entities and relationships using the returned active terms
  and their usage guidance. Select implementation-provenance relationships by their meanings and endpoint
  rules to determine which entities need verified repository-file links and
  implementation anchors; do not assume vertex or edge names.
  Imports, mentions, documentation, and test coverage alone are not definitions.
- Record what was inspected and what was omitted. Separate observed behavior
  from inferred intent. Do not invent requirements or business purpose from
  filenames, test names, or naming conventions alone.

## 3. Generate Canonical Knowledge and Render the KB

- Author concise `.tracelix/kb/<topic>.knowledge.json` artifacts using the shared
  contract and article-quality reference. Generate paired Markdown with the shared
  renderer; do not independently write a second prose representation.
- Begin with a product overview, then coherent capabilities, behavioral rules and
  service dependencies. Preserve exhaustive contract accounting from stage 2.
  No article-count target may remove endpoints. Reuse identities across artifacts.
- Give each entity an active type ID, independently meaningful name, authored role
  description and inspected source references. Give each directed relationship its
  edge type ID, local endpoint IDs, interaction description and source references.
  Keep code citations separate from descriptions. Include verified implementation-file
  relationships where required by the catalog, not merely evidence paths.
- Resolve vague descriptions and missing participants through inspection. Omit
  unsupported assertions and record gaps; do not invent requirements or intermediate
  entities. Preserve unrelated maintained artifacts; leave incompatible retained
  assertions pending. Do not bulk-convert or overwrite maintained Markdown.
- Keep payloads below server limits; split by responsibility, retaining each link's
  endpoints in the same submission. Exclude generated KB and operational ledgers
  from source scans. Record hashes, ontology/context and Git provenance in the ledger.

## 4. Submit and Track Ingestion

- Reconcile semantic findings and every inventoried contract with the JSON assertion
  IDs and paired artifact paths. File provenance and endpoint counts do not establish
  semantic coverage. Complete missing tracing when possible; report real gaps.
- Check active classifications, directed endpoints, descriptions, source anchors and
  required implementation-file relationships. Apply the semantic coverage check in
  the article reference. Preserve omissions separately in `omitted_scope`.
- Refresh the live catalog before each batch. Revalidate affected JSON and rerender
  Markdown on context/revision/fingerprint changes; failed refresh leaves it pending.
- Submit overview first, then coherent artifacts sequentially in small batches using
  `submit_context_knowledge` with the parsed canonical object. Follow the ingestion
  reference's ledger/repetition rules and save returned document/run IDs immediately.
- Reject invalid records locally where possible; repair definitive server validation
  errors before a new admission. Stop admissions on configuration/auth errors. For
  oversize artifacts split coherently. Do not blindly retry ambiguous outcomes.
- Poll accepted runs at about 10 seconds, increasing to at most 30 seconds while
  queued. Track for five minutes per batch unless instructed otherwise; update the
  user at least once a minute. Capacity waits share this bounded window.
- Record succeeded, partially_succeeded, failed, terminated and any returned budget
  outcome separately. Preserve pending IDs when tracking ends; do not automatically
  restart failed runs or resubmit to simulate resume.
- Finish with paired artifact paths, inspected/omitted boundaries, semantic and
  contract coverage counts/gaps, readiness unknowns, run outcomes and pending work.
  Do not claim all implicit dependencies, retrieval usefulness or development readiness.
  Usefulness verification was not performed; successful ingestion is the endpoint.
