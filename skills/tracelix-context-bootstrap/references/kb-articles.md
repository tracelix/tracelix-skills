# Bootstrap Knowledge Artifacts

Read the [shared structured contract](structured-knowledge.md) for
JSON fields, deterministic Markdown rendering, ontology refresh and submission.
JSON is canonical. Markdown is for review and is never sent through extraction.
Use local assertion IDs and source evidence references. Retain meaningful role
and interaction descriptions, semantic coverage and verified file relationships.

## Author Roles and Interaction Meaning

Build descriptions while inspecting code, before writing the records:

1. For an entity, read its defining implementation or authoritative behavioral
   evidence and relevant use sites.
   Identify its responsibility, the domain object or data it handles, and its
   observable result or boundary. For a schema, describe what its records
   represent; for an interface, what exchange it exposes; for a source file,
   which behavior its declarations implement. Use ontology guidance to select
   the type separately from describing the instance.
2. For a relationship, inspect the call, query, binding, event handler, foreign
   key, or evidence establishing a shared behavioral rule. Capture the actual
   interaction or logical dependency and its conditions. A direct call is not
   required when inspected evidence for both participants establishes the link.
   Add a trigger, condition, cardinality, or lifecycle detail only when it changes the meaning
   and is established by the inspected implementation. For structural links,
   describe the actual ownership, composition, or definition; do not invent a
   runtime interaction. For runtime relationships, explain the concrete capability,
   data exchange, scope, or result connecting the endpoints. For implementation
   relationships, identify the declaration and its actual implementation
   responsibility; merely saying that a file contains a declaration does not
   explain that responsibility.
3. Write one short Description sentence, usually 15–35 words, starting with the
   exact entity name or naming both relationship endpoints. Prefer
   concrete verbs and domain objects. Include only details needed to distinguish
   this role or connection; do not pad simple facts to meet a word count.
4. Attach a source path plus a stable symbol or line anchor supporting the
   description, not merely the entity's existence. Follow code across a boundary
   when needed. For synthesized dependencies, cite each participant and the shared
   rule; distinguish observed behavior, enforced constraints, and documented
   requirements. Cite authoritative document sections for explicit obligations;
   document evidence does not prove implementation compliance. Use tests to
   corroborate behavior, not to supply assumed intent.
5. Keep each record understandable on its own, with its exact names and catalog
   types. State each description once per article; do not replace descriptions with
   "see above", an API-method list, source code, or an evidence path.

A description must add information beyond the name and type. Avoid "handles
processing", "service for documents", "depends on", or "calls the repository".
For example, **if verified in code**:

- Entity: "Document ingestion service validates incoming documents, creates queued ingestion runs, and
  returns run identifiers for clients to track processing."
- Runtime relationship: "Document ingestion service asks Document ingestion repository to persist a queued run with its document identifier before returning the run identifier."
- File relationship: "src/ingestion.py declares Document ingestion service and its submit method, implementing document validation and creation of queued runs."

These examples describe instances, not ontology terms or facts to assume about
the current repository. Preserve explicit type labels from the live catalog.
Do not copy catalog definitions into instance descriptions or infer business
goals from names. Qualify supported uncertainty in prose; leave unsupported
claims out and record inspection gaps in local omitted scope.

Before submission, read just the entity names/types/descriptions and relationship
endpoints/types/descriptions. They should explain what the system contains and
why its parts are connected, giving a future agent starting points for source
inspection. They do not replace checking current implementation behavior.
Reject blank, circular, generic, or evidence-only descriptions. Resolve them by
targeted inspection or omit unsupported assertions using the existing omission
rules. This is a local article-quality check, not a graph usefulness query.
Reject relationship descriptions that only restate their type and endpoints or
promise an unspecified result or error. A correct relationship classification or
code citation does not make such a description useful. Preserve the source-backed
entity role descriptions and explicit defining-file relationships while improving
the meaning of the individual connections.

## Semantic Knowledge Coverage Check

Apply [context-mapping.md](context-mapping.md) when selecting connected article
content. Group by coherent capability or shared rule, connecting its realization,
domain concepts, and constraints. Reuse capability identities across overview
and detailed articles rather than leaving functionality only in the overview.
Preserve each contract's exact identity and the distinction between an API
interface and its providing backend component.

For consequential relationships, ask whether the records explain why a related
area merits inspection during a potential change: shared implementation, access
policy, ownership/scope, lifecycle condition, data dependency, or downstream
effect. Record the inspected connection and its conditions, not speculative change
advice or a generic dependency label. A need to review related behavior does not
establish mandatory synchronized edits. Preserve inheritance, intentional overrides,
and the evidence basis of alignment obligations. Structural relationships and implementation-file
links retain their own purposes; do not force every edge into an impact claim.

Review the semantic assertions independently of file provenance. Check capability
realization by relevant components, interfaces, and UI; endpoint provider, aggregate
API membership where present, and purpose; and supported participants in shared
configuration, rules, or service dependencies. Product-only functionality,
file-only endpoints, and rules with missing participants expose gaps. Resolve
them through inspection and valid assertions or record an explicit disposition
under the context ledger's coverage aspects. Not every aspect is applicable;
explain genuine exceptions without dropping contracts from coverage.

Do not reconstruct complete execution paths, create a conceptual node per symbol,
or demand a minimum degree or edge ratio. Keep incidental symbols as evidence
anchors and select every type/direction from the live catalog. Do not assume
functionality-to-functionality dependency edges are permitted. Use supported
mediated relationships only when every entity and connection has evidence;
never invent a requirement or intermediate entity to make a path possible.

This is a local source-to-article quality check, not a graph query, completeness
guarantee, or usefulness acceptance test. Preserve the distinction between
missing source discovery/documentation, ontology limitations, and a documented
assertion missing from application, entity resolution, or retrieval. Improving
articles or skill instructions does not repair the existing graph automatically.

## Coverage and Names

- Overview: the product, observed capabilities, major components, and deployment
  boundaries. Connect capabilities to their realization in detailed articles;
  a product membership assertion alone is not realization coverage. Use a neutral
  purpose description when business intent is unknown.
- Components: responsibilities, direct collaborators, interfaces used or exposed,
  and important reads/writes.
- Flows: observed user or system behavior connected to UI, API, components,
  persistence, and representative test scenarios where evidence exists. Include
  non-contract entry points and consequential dependencies from context discovery.
- Interfaces: every in-scope API operation and messaging binding in the contract
  inventory, with purpose, workflow, implementation anchors, and explicit
  relationships. Include provider, aggregate API membership, and capability
  connections where supported; the source file is not the architectural owner.
  A general API description does not cover its individual methods.
  Group related operations into coherent articles and preserve each exact identity.
- Data and concepts: logical elements, actors, ownership, role scope, and lifecycle
  constraints needed to explain the traced contracts and capabilities;
  avoid expanding every payload field or internal helper into a graph entity.
- Shared rules: meaningful configuration, lifecycle, interpretation, and service
  constraints connecting separately implemented behavior. Do not turn descriptions
  of current behavior into normative requirements without supporting evidence.
- Regression scenarios: inspected Test Case entities and verification relationships
  under [test-coverage.md](test-coverage.md), describing the actual expectation,
  fixture/mock boundary and supported target. Test citations alone do not publish
  a scenario or verification link. Reconcile canonical IDs and evidence with the
  test ledger; missing entities, links or inspected assertions remain explicit gaps.

Use [contract-mapping.md](contract-mapping.md) and
[context-mapping.md](context-mapping.md) to reconcile both inventories with
these article assertions. The complete operational worklists belong in the local
ledger; do not duplicate them as ingested supplementary inventories.
Reconcile representative test publication separately; an API or semantic coverage
check cannot close its gaps. Missing live Test Case types or permitted verification
endpoints leave affected publication pending, without substituting generic links.

Use entity names consistently across documents without decorative quotes. Disambiguate generic names with
their owner or domain, such as "Document ingestion run" instead of "Run". Preserve
exact source symbols in evidence anchors. For multiple repositories
sharing a context, use meaningful repository/component qualifiers where needed.

## Ontology and Evidence Rules

Obtain the live catalog before mapping and refresh before each submission batch.
Classify with active term IDs and their usage guidance. Check edge direction and
sourceVertexTermIds/targetVertexTermIds. Do not assume a fixed ontology or invent
intermediate entities, fallback edges or requirements to make unsupported links.
Inspect definitions and actual use sites; imports/citations/test names alone do
not establish implementation ownership or behavioral coupling. For every entity
covered by the catalog's implementation-provenance rules, include its defining
file entity and an explicit supported relationship, not merely a source reference.
Keep capabilities outside those endpoint rules connected through supported realization
or constraint links; do not fabricate file links. Use consistent repository-qualified
file identities where multiple checkouts share a context. Each submission includes
its own relationship endpoints, even when identities also occur in other artifacts.

Review every submitted record, including code elements intentionally represented
as entities. Evidence symbols do not implicitly become entities. A file relationship
for a component does not assert a definition for its class. Resolve missing definitions
or omit unsupported assertions and record `omitted_scope`; preserve unrelated
maintained content and leave incompatible retained assertions pending.

Sources contain inspected relative paths, file SHA-256 hashes and symbols/line
anchors. Repository metadata records commit and dirty state; use null commit outside
Git. Refresh affected facts/hashes if the working tree changes. Test references
must correspond to inspected assertions. Hashes and anchors are client-supplied
provenance; neither server validation nor ingestion success proves their truth.
