# Regression-Test Discovery and Publication

Inspect representative regression scenarios for mapped capabilities and publish
what they check as connected knowledge. This is source inspection, not test
execution, an exhaustive test inventory, or a runtime coverage measurement.
Keep this accounting separate from [contract coverage](contract-mapping.md),
[semantic coverage](context-mapping.md), and ingestion outcomes.

## Discover and Inspect

Locate test roots using repository files, package manifests, test-runner
configuration, CI/build commands, and targeted searches for capability entry
points and collaborators. Inspect in-scope packages independently; tests may sit
beside implementation files or outside a conventional tests directory. Record
searched roots and scope boundaries. A filename search alone does not establish
that a capability has no tests.

For each mapped capability, inspect representative regression scenarios where
available. Select scenarios that establish its important behavior and shared
rules; include consequential success, failure, authorization, or lifecycle cases
as applicable rather than meeting a fixed scenario quota. Follow setup, fixtures,
helpers, mocks, exercised operations and actual assertions far enough to explain
the preconditions, action, expected result, and boundary being verified. Test
names, snapshots without their assertions, and helper declarations alone are
discovery leads, not inspected scenarios.

Inspect the target implementation or authoritative requirement separately.
Explain whether the test uses mocked collaborators or integration boundaries;
do not claim that a stubbed interaction proves the real collaborator's behavior.
Tests can document expectations and corroborate observed behavior, but do not
prove production compliance, business intent, or that any execution passed.

When relevant source is available, inspect it before closing the worklist. Record
remaining uninspected test areas explicitly. Distinguish tests not found within
the searched boundaries from tests known to exist but not inspected. Neither
condition excludes a capability or contract from its other coverage accounting.

## Publish Scenarios and Verification Links

Use the live ontology's active Test Case classification and verification
relationship meaning, directions and endpoint rules; labels and numeric IDs are
not fixed. A Test Case describes a reusable scenario, not a test run or result.
Give it a meaningful, owner-qualified name and a description of the setup/action
and asserted expectation. Cite inspected test symbols or line ranges with file
hashes; include relevant fixture/helper evidence when it establishes the claim.

Connect each scenario to the supported capability, requirement, interface,
component, or other permitted entity whose behavior its assertions check. Cite
the test assertions and inspected target evidence, and describe the particular
condition or result checked rather than merely saying "tests" or "verifies".
Reuse capability and target identities from the semantic mapping. One scenario
may verify several targets when each link is independently supported. Keep each
relation's endpoints in the same canonical payload and reuse scenario identities
across articles; do not create one Test Case per citation or execution.

Use only file relationships permitted by the live catalog. Test evidence is not
a definition of production behavior; do not assume a defining-file edge accepts
Test Case endpoints. If a required type or verification link cannot be expressed,
record an ontology gap and leave affected publication pending. Do not substitute
generic relationships, invent requirements or intermediate entities, or reclassify
targets merely to make an edge valid. Preserve unrelated maintained assertions.

## Local Ledger and Reconciliation

Extend `.tracelix/bootstrap/manifest.json` additively, preserving provenance and
attempt history. These are local accounting fields, not additions to the canonical
knowledge payload:

- `test_discovery`: `inspected_roots`, stated boundaries and `gaps`, plus
  `capability_assessments` keyed by the existing capability/context-item key.
  Each assessment records searched/inspected anchors, selected case keys and an
  explicit disposition: `inspected`, `tests_not_found`, `uninspected`, `blocked`,
  or `excluded`. Give missing, blocked, uninspected or excluded areas a reason;
  exclusions cite the agreed scope boundary. A search with no tests found needs
  its searched roots recorded, not an unsupported repository-wide absence claim.
  An `inspected` assessment requires at least one inspected representative case;
  it does not imply that publication succeeded.
- `test_cases`: stable `key` qualified by owner, test symbol and scenario;
  `name`, inspected `source_anchors`, setup/action/expected-result summary and
  mock/integration boundaries; `assertions_inspected` (true only after inspecting
  the scenario and assertions); related capability/context and contract keys;
  `article_paths` and exact canonical entity/relation IDs once documented.
  Use `discovered`, `traced`, `documented`, `blocked` or `excluded` status,
  with reasons for blocked or excluded cases. `traced` means the scenario and
  assertions were inspected. `documented` additionally requires a Test Case
  entity, at least one supported verification relation and inspected evidence
  in the named canonical artifacts. Retain `assertions_inspected` when a traced
  scenario becomes blocked from publication. Ingestion status remains independent.

Record known candidates not yet inspected as discovered cases or explicit
uninspected areas; do not present a partial filename list as an exhaustive count.
Count a reusable scenario once across articles and targets. Group parameterized
variants with the same expectation; retain materially different expectations as
distinct scenarios without counting every execution as a new case.

Before submission, reconcile mapped capabilities against their assessments, then
selected scenarios against their source evidence and canonical assertions. An
`inspected` capability assessment does not close a scenario publication gap.
On repetition, refresh changed evidence, reconcile removed tests separately from
current scenarios, and retain history. Missing fields in older manifests mean
test coverage is unassessed, even if old articles or ingestion runs succeeded.

## Completion and Report

Report these separately from semantic coverage, API/messaging counts and run
outcomes:

- Total mapped in-scope capabilities, assessments by disposition, and capabilities
  with documented verification links. Unassessed capabilities remain gaps.
- Unique candidate scenarios recorded, inspected (`assertions_inspected` is true,
  including publication-blocked cases), documented and remaining cases by status.
  Explain the representative selection
  boundaries; these counts are not an estimate of every test in the repository.
- Unique canonical Test Case entities and verification relationships, deduplicated
  across articles; distinguish authored assertions from ingestion outcomes.
- Uninspected areas, tests not found, exclusions, ontology limitations and pending
  publication, with reasons and source/scope boundaries.

Explain zero Test Case or verification counts explicitly. If relevant tests exist,
zero publication is incomplete work unless a concrete blocker is recorded.
Representative source/publication coverage is complete only within the stated
scope when every capability is assessed, selected scenarios are documented, and
unresolved discovery/publication gaps are absent. Explicit exclusions narrow the
scope; missing tests remain reported coverage gaps. Successful ingestion never
closes these gaps and does not prove tests passed or runtime coverage improved.
