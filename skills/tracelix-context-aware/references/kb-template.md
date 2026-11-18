# Development Knowledge Artifacts

Use the [shared structured contract](structured-knowledge.md) to author
canonical `.knowledge.json`, render paired Markdown, and submit typed records.
Choose live active ontology IDs and inspect implementation and use sites before
asserting descriptions or relationships. Descriptions explain responsibilities,
concrete interactions and conditions; citations/hashes belong in source evidence.

Include meaningful capabilities, constraints, interfaces and collaborators affected
by the change. File citations alone do not explain behavior or change impact. Keep
observed behavior separate from inferred intent and normative requirements.

## Implementation plan as a Requirement

Every post-implementation submission must include the implementation plan as an
entity using the live catalog's active Requirement type. Its description preserves
the plan's intended behavior, implementation approach, constraints and acceptance
criteria, including agreed revisions. Keep the plan used for the completed work in
`.tracelix/kb/<topic>.plan.md`; add that repository-relative path and its SHA-256 to
`sources` and reference its source ID in the Requirement's `evidence`. The plan is
authored evidence, separate from the deterministically rendered `<topic>.md`. Do
not replace the Requirement with a Document, Task or a prose-only mention.

Before submission, query published knowledge about the implemented feature. For
existing targets, confirm graph findings against inspected local evidence and
reuse verified types, names and available identifiers. Include those entities with
local IDs in the payload and reference those IDs in relationships; graph record
IDs are not submission endpoints or identity identifiers. Do not invent identifiers
or create renamed copies of published entities.

Use only relationships allowed by the current live ontology, with meaningful
descriptions and inspected evidence. For example, use Requirement → applies_to →
Functionality or Test Case → verifies → Requirement when their meanings and
endpoint rules fit. Do not assume implements → Requirement is permitted. The plan
supports intended conditions; implementation and test evidence support claims
about actual behavior and verification, not merely the plan's presence.

If no verified published target exists, record that coverage gap separately and
submit the Requirement with supported links to newly documented feature entities
where available; do not claim a link to published knowledge. If the ontology lacks
the Requirement type or cannot express a necessary relationship, leave affected
artifacts pending and report the blocker instead of substituting types or edges.

## Evidence and submission

Derive defining-file relationships from the catalog's meanings and endpoint rules.
Include both entity endpoints and each verified file relationship explicitly. Do
not infer definitions from imports, mentions, or test names. Inspect representative
test assertions as corroboration. Resolve unsupported records or omit them with
local reasons; never invent ontology terms or relationships. Preserve unrelated
maintained content and leave incompatible retained assertions pending.

Refresh the live catalog before submission, revalidate typed JSON on identity
changes, and rerender Markdown. The canonical artifact carries local IDs, typed
assertions, direct authored descriptions, source hashes, Git and ontology provenance.
Save operational status/attempt history separately; do not ingest tracking notes.
