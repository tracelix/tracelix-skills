# Semantic Knowledge Discovery and Coverage

Organize knowledge around what the product enables, the rules governing that
behavior, and functional or service dependencies that a local code change could
overlook. Connect capabilities to their realization and constraints; files and
symbols provide evidence and inspection anchors. The graph enriches current code
inspection; it is not a replacement for it or a comprehensive call graph. Retain exhaustive
contract accounting under [contract-mapping.md](contract-mapping.md) independently.
Use [test-coverage.md](test-coverage.md) to inspect representative regression
scenarios for each mapped capability and publish their verification links.
Tests missing or left uninspected remain explicit gaps, even for capabilities
with complete implementation and contract tracing.

## Establish Capabilities and Shared Rules

Start with observed abilities and goal-oriented scenarios, then identify the
components, interfaces, and UI that materially realize them. Keep capability names
consistent across overview and detailed articles; do not duplicate a capability
for every implementation file or manufacture one per endpoint. Product membership
alone does not explain realization. Operational interfaces may support an
operational capability rather than a user-facing feature; record a reason when
capability mapping is genuinely inapplicable, without excluding the contract.

Investigate independent configuration/initialization paths, operational and
evaluation tools, lifecycle conditions, service prerequisites, and producer/consumer
assumptions. Ask which separately implemented behaviors share a rule or meaning,
even if they never call each other. Existing maintained specifications or decisions
can establish explicit intent; inspect code separately to establish current behavior.

## Discover Applicable Surfaces

Inspect manifests and registration/composition roots across in-scope packages:

- UI: reconcile registered routes, navigation destinations, rendered pages, and
  significant user actions. Inspect nesting, shared shells/layouts, access gates,
  and feature conditions. Pages with no backend operation still belong in discovery.
- CLI: inspect command registrations, dispatch, and the capabilities they expose.
- Background behavior: inspect schedulers, worker startup, event handlers, and
  trigger bindings, including producers and consumers across package boundaries.
- Capabilities and domain concepts: derive responsibilities, actors, ownership,
  role scope, lifecycle states, and important constraints from inspected behavior.
  Documentation and UI labels can guide discovery but do not prove implementation.

Record the inspected roots and boundaries in `context_discovery`. Explain which
surfaces are absent or out of scope and why; do not equate an uninspected package
or unresolved dynamic registration with absence. Inspect applicable surfaces even
when every API operation has already been traced. A significant action changes
state, access, ownership, or workflow, or crosses a component boundary; ordinary
presentation controls need not become separate inventory items.

## Select and Establish Consequential Connections

Include a finding when it helps locate related behavior, recognize a constraint,
or identify another area requiring inspection during a change. Follow consumers
and providers only as far as necessary to establish its meaning and evidence.
Keep the implementation steps as anchors unless a step itself explains a
consequential dependency. Investigate these connections where applicable:

- Placement and reuse: which area owns a capability, how navigation exposes it,
  and which screens actually compose shared shells, components, or styles.
- Authorization and scope: which policies govern entry points and operations,
  and whether roles, ownership, or identity have platform, organization, or other
  scope. Distinguish human accounts, service identities, and memberships when
  the implementation gives them different responsibilities or lifecycles.
- Lifecycle coupling: behaviors that depend on the same state or invariant,
  such as account eligibility participating in both login and recovery. Inspect
  both uses before asserting a connection, even when there is no direct call.
- Data dependencies: authoritative sources and consequential joins, transformations,
  or contracts connecting displayed/consumed data to its meaning. Do not expand
  every response field or query into an entity.
- Downstream effects: changes to sessions, ownership, dependent data, asynchronous
  work, or external interactions caused by an action. Establish actual behavior;
  do not infer deletion cascades, delivery guarantees, or atomicity from names.

An import, similar name, shared table, or visual resemblance is a discovery lead,
not evidence of behavioral coupling or intended reuse. Inspect composition,
policy enforcement, predicates, foreign keys, calls, or configuration as relevant
to the claim. Test assertions can corroborate it. Separate observed semantics from
unverified implications; do not invent requirements or dependencies for a proposed
feature. Keep unresolved questions in the local ledger, not as graph assertions.

## Synthesize Logical Dependencies With Evidence

A direct call is not required. Establish a connection from inspected evidence for
each participant and the shared condition, rule, or behavioral assumption. Explain
why the connection warrants inspection during a change; do not reduce it to
co-occurring symbols or equal constants. Distinguish the basis of each finding:

- Observed behavior: what the implementations actually do, including inherited
  settings, explicit overrides, eligibility checks, or data interpretation.
- Enforced constraint: a condition demonstrably enforced by validation, schema,
  policy, or workflow. Describe its scope, not an imagined product requirement.
- Documented requirement: an explicit behavioral or alignment obligation from
  an authoritative specification or decision. Its existence does not prove that
  all implementations satisfy it.

Separate "review the related behavior" from "both implementations must change."
Only assert mandatory alignment when the evidence establishes that obligation.
For example, configuration initialization and evaluation setup may participate in
the same matching policy. Inspect how evaluation selects or overrides configuration:
inheriting a changed default may require no script edit, while an explicit override
requires review against the intended policy. Preserve that condition, not a blanket
claim that duplicated values must stay equal. A documented alignment obligation
can be relevant even when source inspection reveals the implementations diverge.

## Connect Realization, Ownership, and Behavioral Meaning

For supported findings, assert meaningful connections in addition to provenance:

- Capability realization: connect the components, interfaces, and UI that
  materially realize the capability. A product-to-capability link is insufficient.
- Interface ownership and purpose: establish the provider, any aggregate API
  contract containing the endpoint, and the capability the operation serves.
  Distinguish a backend service from its API interface with unambiguous names.
  Link a specification file to the aggregate contract it authoritatively defines;
  the file declaring an endpoint is not itself the endpoint's provider.
- Behavioral dependencies: connect participants through their shared configuration,
  domain data, requirement, or service condition, explaining the actual relationship.
  A connection may span several valid assertions rather than a single direct edge.
- Provenance: retain verified defining-file relationships where applicable. Neither
  provenance nor a path through a common source file substitutes for semantic links.

Use meaningful product/capability names grounded in observed behavior and labels,
with exact symbols as evidence. A discovery item need not become a separate graph
entity: it may be represented by relationships between existing entities. Select
all graph types, relationship meanings, directions, and endpoints from the live
MCP catalog, not from the discovery categories below. If the catalog cannot
express a supported finding under its guidance, record the limitation and omit
affected generated assertions or leave affected maintained articles pending under
the article rules. Never substitute a generic link to close a coverage gap.
Match realization, exposure, composition, and constraint meanings to the catalog's
actual allowed endpoints. Do not assume a dependency edge accepts functionality
endpoints, or a definition edge accepts requirements or capabilities. Use a mediated
path only when every assertion is independently supported and valid; do not invent
an intermediate entity or reclassify one just to obtain a permissible connection.

## Context Ledger and Reconciliation

Extend the existing manifest additively; preserve provenance and submission
history. `context_discovery` contains `inspected_roots` and `gaps`, documenting
surface coverage, availability conditions, and scope boundaries. An absent
section in an older manifest means discovery was not recorded, not completed.

`context_items` records significant findings, using:

- `key`: stable identity qualified by owner and finding, independent of line numbers.
- `category`: `entry_point`, `capability`, `domain_concept`, or `dependency`;
  these are local bookkeeping labels, not ontology terms.
- `name`, `source_anchors` (repository-relative path plus stable symbol or line),
  and `contextual_significance`: what the finding establishes and why related
  behavior or a constraint warrants inspection.
- For newly assessed items, `coverage_aspects`: applicable values from
  `capability_realization`, `interface_ownership_purpose`, and `behavioral_dependency`.
  These select local coverage checks, not ontology types or additional graph nodes.
- Once traced, `assertion_basis`: `observed_behavior`, `enforced_constraint`, or
  `documented_requirement`, with supporting anchors and conditions in the finding.
  Split findings when their evidence basis or conclusions differ materially.
- `related_contract_keys`: references to the existing inventory, empty when no
  communication contract is involved. Do not duplicate a contract's tracing record.
- `article_paths`, `entity_names`, and `relationships`: mappings to actual article
  assertions once documented. Each relationship mapping names its exact `source`,
  `relationship_type`, and `target`; use the article's catalog-selected terms.
- `status`: `discovered`, `traced`, `documented`, `blocked`, or `excluded`; include
  `reason` for blocked or excluded items. Exclusions cite the scope boundary or
  explain why a candidate fails the relevance rule, rather than silently dropping it.

`traced` means the connection/concept's meaning, consequential context, and source
evidence were inspected. `documented` additionally requires its supporting article
assertions, including relationships where the finding is a dependency. A list of
files or isolated endpoint nodes does not document a dependency. One assertion
may support several findings and contracts; reuse consistent identities instead
of multiplying entities or articles to satisfy ledger counts.

For applicable coverage aspects, reconcile capability realization, endpoint
ownership/purpose, and shared-rule participants with the actual relationship
mappings. Product-only functionality, file-only endpoints, or rules lacking a
supported participant remain gaps until inspected and documented or explicitly
disposed with a reason. An inapplicable semantic aspect does not exclude a contract
from exhaustive accounting. Missing aspect/basis fields in older items mean the
new semantic coverage has not been assessed; preserve earlier records and statuses
without treating their old `documented` status as proof of the added coverage.

Reconcile discovery roots with findings, then findings with article assertions.
Reconcile capability keys with test-discovery assessments and selected scenarios;
capabilities without communication contracts still need this assessment. Semantic
documentation status alone does not establish test inspection or publication.
Continue inspection when source is available; record concrete source, registration,
or ontology blockers otherwise. On repetition, refresh affected evidence, reconcile
removed findings, and preserve earlier provenance separately; new submissions do
not retire old graph records.

Report semantic knowledge coverage, including discovery/documentation, independently
of contract coverage and ingestion outcomes. Only describe coverage as complete within stated inspected
boundaries when discovery gaps are resolved and non-excluded findings are
documented. Explain absent/inapplicable surfaces using inspected roots. Missing
fields in older manifests remain unassessed until discovery is performed; an empty
array alone is not evidence of coverage. This accounting cannot prove that all
implicit dependencies were found, assertions extracted, or retrieval improved.
Report gaps by meaning and inspected scope, not just counts. Use no minimum node
degree or semantic/provenance edge ratio; a local structural check is not a graph
query or an acceptance claim about extraction, resolution, or retrieval quality.
