# Agent-authored knowledge

Use `submit_context_knowledge` for knowledge synthesized from inspected source.
Discover its live schema. Submit a JSON object, never a JSON string or Markdown.
If unavailable, keep artifacts pending and report the missing capability. Do not
fall back to `submit_context_ingestion`; that tool extracts knowledge from raw text.

## Canonical artifact

Author `.tracelix/kb/<topic>.knowledge.json`:

- `schema_version`: integer `1`; `title`: human-readable title.
- `ontology`: `revision_id` and `fingerprint` from the current live catalog.
- `repository`: `name`, `commit_sha` (null outside Git), `working_tree_dirty`.
- `sources`: local `id`, repository-relative POSIX `path`, file `sha256`, optional
  `symbol`, `start_line`, `end_line` anchors.
- `entities`: local `id`, active ontology `type_id`, `name`, meaningful authored
  `description`, nonempty `evidence` containing source IDs. Optional `owner`,
  `aliases`, `identifiers` (`namespace`/`value` records) describe this identity.
- `relations`: local `id`, active edge `type_id`, `source`/`target` entity IDs,
  meaningful authored `description`, nonempty source-ID `evidence`.

Use exact active catalog term IDs, semantic guidance and directed endpoint rules.
Relationships reference local IDs, preserving distinct same-named endpoints.
Descriptions explain inspected responsibilities and interactions; citations belong
in source anchors. Do not submit extraction-only `descriptionEvidence`, graph IDs,
relationship names, context selectors or arbitrary extra fields.

The server rejects the complete batch before queueing if invalid. Repair the
reported field paths/record IDs on definitive validation rejection. No records
from a rejected batch were admitted. Schema validation cannot verify local files
or truth; retain source inspection, semantic coverage and file-traceability checks.

Save the current `get_context_ontology` response in a temporary catalog file for
rendering. It is not an ontology fallback on subsequent invocations. Run:

```bash
python3 "$SKILL_DIR/scripts/render_knowledge.py" .tracelix/kb/topic.knowledge.json --ontology /tmp/current-ontology.json
```

Set `SKILL_DIR` to the absolute directory containing this installed skill's
`SKILL.md`. Run from the target repository so artifact paths resolve there. The
renderer is bundled in `scripts/` and this contract in `references/`. It canonicalizes
JSON (sorted object keys, preserved array order,
explicit defaults), writes paired `topic.md`, and prints the canonical payload
SHA-256. Never independently author/edit the rendered Markdown. Preserve unrelated
maintained Markdown; choose a new topic filename when needed. Submit the parsed
canonical object directly to `submit_context_knowledge`.

Refresh the live ontology before each batch. Revalidate/update JSON and Markdown
when context, revision or fingerprint changes. The server rejects revision
mismatch at admission and fails drift detected before application.

## Tracking

The tool returns document/run IDs, existing status fields and
`input_format: "knowledge"`. Track with existing run get/list tools. Check setup
with `get_context_readiness({})` before starting, and report its message when
`ready` is false. Handle actual submission/run errors as they occur. Queued status
confirms acceptance, not successful completion.

Preserve ledger history. Each artifact/attempt records `input_format`,
`schema_version`, canonical `payload_sha256`, paired paths, evidence hashes,
connection/context identity and ontology revision/fingerprint. Save run/document
IDs immediately. Keep semantic coverage, contract coverage and run outcomes
separate; successful ingestion does not establish graph completeness.

Every accepted submission creates a new document/run. Preserve `outcome_unknown`
on ambiguous transport failure; do not blindly retry. Reuse prior success only
after matching payload/evidence hashes, ontology/context identity and refreshing
its saved run through the current connection. Changed submissions do not replace
old assertions or retire stale evidence. Retain bounded tracking and retry rules.
