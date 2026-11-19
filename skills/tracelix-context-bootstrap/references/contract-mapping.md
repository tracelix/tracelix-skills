# Contract Inventory and Tracing

Build the contract worklist from the repository's current communication contracts
before tracing their implementations. Trace each API operation and messaging
binding to its purpose, workflow, and implementation. Contract coverage is measured
against this worklist, not a sample of important flows or article counts. Use it
to support [semantic knowledge discovery](context-mapping.md), not as the organizing
model of the product. Complete contract accounting does not establish capability
realization, architectural ownership, or consequential dependency coverage.

## Discover and Reconcile the Surface

Use `rg --files` and targeted searches to locate contract declarations and their
registration roots across all in-scope services/packages. Inspect manifests,
startup/assembly code, router mounts, workers, and deployment configuration to
find each surface. Existing docs help discovery but do not define completeness.
Where an existing parser can enumerate a structured contract without starting
the application, use it to obtain the full operation list. Record counts per
surface and reconcile them with inventory keys; targeted search results alone
are not evidence that every router or subscription was inspected.

- APIs: enumerate each HTTP method and fully mounted path, RPC service/method,
  GraphQL query/mutation/subscription field, MCP tool, or equivalent operation
  present in the checkout. Include versions, router prefixes, and conditional
  registrations. Inspect both machine-readable schemas and actual registrations;
  reconcile schema-only and implementation-only operations explicitly. Read
  generated interface declarations when authoritative; skip generated handler
  boilerplate when locating handwritten implementations.
- Messaging: enumerate declared queues/topics, publishers, consumer subscriptions,
  and their handler bindings. Match message schemas to actual send and receive
  sites and configuration. Record broker/vhost or namespace, topic/routing key,
  direction, and subscription/group where these distinguish operations. A topic
  with several consumers needs each binding traced. Include retry/dead-letter
  bindings when present, and record dynamic name patterns without inventing
  runtime instances.
- Distinguish provided contracts from outbound API/message dependencies. Trace
  outbound calls through their local adapters and intended use; do not claim
  knowledge of external implementation unavailable in this checkout. Record
  direction and ownership so an imported schema is not mistaken for a local API.

Do not omit admin, authentication, health, internal, deprecated, or conditional
operations merely because they look unimportant. Record whether a declaration is
mounted, unmounted, conditional, or unresolved. Stale or unsupported declarations
remain visible discrepancies rather than disappearing from the denominator.
Only exclude operations under an explicit scope boundary, with a reason.

Track inspected discovery roots and unresolved registrations. Static inspection
cannot establish a full live surface when routing or subscriptions depend on
unavailable runtime configuration, plugins, external schemas, or generated output.
State those discovery gaps; do not turn an unresolved surface into a zero count.
If no communication contracts exist, record which roots were checked. Context
discovery is required whether or not communication contracts exist.

## Trace Every Inventory Item

For each operation or binding, inspect and record:

1. Its exact identity, declaration/registration anchors, availability condition,
   and provider/consumer ownership.
2. Its observed purpose and input/output or message contract. Describe what the
   operation achieves without inventing business intent from its name.
3. Its handler, resolver, consumer, or producer and defining file. Follow the
   workflow through actual collaborators, queries/writes, emitted messages, and
   response/acknowledgement behavior. Include authorization, validation, failure,
   retry, and idempotency branches when they materially affect the workflow.
4. The files and stable symbols supporting those facts, plus representative
   inspected test assertions when available. Follow [test-coverage.md](test-coverage.md)
   to record and publish those scenarios, reusing contract/capability keys.
   Missing tests do not erase an otherwise traceable contract; record the test
   gap independently rather than silently omitting it.
5. Its article path and exact entity/relationship records once documented. Select
   ontology terms from MCP; do not invent types or links to close a coverage gap.

Reconcile the provider, aggregate API membership where present, and capability
purpose through semantic context findings. The specification's declaration link
does not establish these relationships. Distinguish the backend service from its
API contract and connect the aggregate declaration where the source supports it.
Keep exact operation identities even when several implement one capability.

Shared workflows can be described together, but preserve each operation's exact
identity and distinct behavior. An API-wide paragraph or one traced sibling does
not cover the remaining methods. Reuse shared component records consistently;
do not expand every internal helper into a graph entity.

When tracing reveals local consumers, domain constraints, shared policies, or
downstream effects relevant to impact discovery, reconcile them with the context
inventory. Inspect both ends as needed to establish their meaning, without
reproducing every call or payload field. Link context items to contract keys;
reuse the same article assertions rather than duplicating inventories in the KB.
Shared policy or interpretation can establish a logical dependency without a
direct call; follow the context reference's evidence and obligation rules. A
semantic coverage gap does not erase a traced contract, and a fully documented
contract does not close the semantic gap.

## Coverage Ledger and Completion

Extend `.tracelix/bootstrap/manifest.json` without replacing existing provenance or
attempt history. Keep the operational inventory local instead of submitting it as
a second endpoint/fact list. Record discovery roots/gaps under
`contract_discovery`, and inventory items under `contracts`. Each item needs:

- A stable `key` reflecting protocol, owner, direction, and exact operation or
  messaging binding; retain versions/prefixes and distinct subscriptions.
- `kind`, `direction`, `availability`, declaration/registration source anchors,
  and implementation anchors when located.
- Observed `purpose`, a concise `workflow`, and inspected `source_files`.
- `article_paths` and exact `entity_names` once represented in article assertions.
- `status`: `discovered`, `traced`, `documented`, `blocked`, or `excluded`, plus
  a `reason` for blocked or excluded items.

`traced` means purpose, workflow, and implementation have been inspected;
`documented` additionally requires matching assertions and evidence in the named
articles. `blocked` records the missing source, unresolved binding, ontology
limitation, or other concrete gap. Exclusions must cite the scope boundary.
These statuses are independent of article ingestion status.

Before reporting source coverage, compare the union of declarations and actual
registrations/bindings with the inventory, then the inventory with the articles.
New contracts found during tracing must be added and traced before closing the
worklist. On repeated invocation, reconcile changes against the current checkout;
do not carry forward a removed operation as current merely because an old article
or successful ingestion run exists. Preserve its earlier provenance separately;
document submission does not retire old graph records.

Report total unique inventory items and counts by status, with API operations and
messaging bindings distinguishable. Contract source coverage is complete only
within the stated scope when discovery has no unresolved gaps and every non-excluded item
is documented. Otherwise report partial coverage and identify the remaining
items. This is a local contract-to-source/article reconciliation, not a graph
query or a guarantee about runtime-only endpoints or extraction completeness.
Report semantic knowledge coverage under its own discovery boundaries and statuses; complete
contract coverage must not be reported as complete repository-context coverage.
