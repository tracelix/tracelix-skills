# Bootstrap Structured Ingestion

Follow the [shared structured contract](structured-knowledge.md) for
the typed payload, canonical JSON, deterministic Markdown and readiness boundaries.
Discover `get_context_readiness`, `submit_context_knowledge`, `get_context_ontology`,
`get_context_ingestion_run` and `list_context_ingestion_runs` through the native
connection. No ad hoc clients or configuration changes are part of bootstrap.

## Readiness and Ontology

Call `get_context_readiness({})`. A successful response confirms the connection.
If `ready` is false, report its message and preserve local work until setup is
complete. If the tool is missing or fails, report the blocker. Do not probe backend
settings. Readiness does not execute model requests or guarantee later success;
handle actual submission and run errors when they occur.

Obtain the complete live catalog before mapping and refresh before each batch.
Use its active terms, semantic guidance and relationship endpoint rules. Capture
returned metadata automatically; do not ask the user to supply or compare numeric
identifiers. Never use a local or remembered catalog as fallback. If unavailable,
preserve work and leave affected generation/submission pending.

The tool receives parsed JSON data, not a filesystem path. Submit the canonical
object from the `.knowledge.json` artifact. No Markdown extraction step occurs.
On definitive validation rejection, repair bounded record/field diagnostics; no
document/run was admitted. The server also checks revision identity before application.

## Ledger and Repeated Invocations

Maintain `.tracelix/bootstrap/manifest.json`, preserving existing version-1 discovery
records, contracts, context items, test discovery/cases, gaps, article mappings
and attempt history.
Keep operational notes outside ingested knowledge. Add to each article entry:

```json
{
  "path": ".tracelix/kb/topic.md",
  "knowledge_path": ".tracelix/kb/topic.knowledge.json",
  "input_format": "knowledge",
  "schema_version": 1,
  "payload_sha256": "<canonical payload hash>",
  "content_sha256": "<rendered Markdown hash>",
  "source_hashes": {},
  "ontology_revision_id": "<live revision>",
  "ontology_fingerprint": "<live fingerprint>",
  "attempts": [],
  "submission_state": "not_submitted"
}
```

At ledger and attempt levels retain connection/context identity, commit SHA and
dirty state, ontology identity, input format/schema, canonical/evidence hashes,
document/run IDs, latest status/timestamps and errors. Historical entries without
these fields remain readable, but cannot establish a matching structured success.
Preserve semantic discovery, contract inventories and test assessments/scenarios
independently of run status; see [contract-mapping.md](contract-mapping.md),
[context-mapping.md](context-mapping.md) and [test-coverage.md](test-coverage.md)
for coverage reconciliation. Older manifests without test fields are unassessed.

Before submitting, record `submitting` and the intended canonical hash. Save every
returned document/run ID immediately. Skip an unchanged artifact only after its
payload/evidence and ontology/context identity match a saved succeeded run refreshed
through this connection. Track matching queued/running work rather than duplicate it.
Preserve unsuccessful attempts; do not automatically restart or simulate resume by
resubmitting. An ambiguous transport outcome is `outcome_unknown`: this API has no
admission idempotency key, and a title match cannot uniquely recover an attempt.
Changed submissions create new documents/runs without retiring old assertions.

## Submission Errors and Outcomes

On a reported size error, split knowledge coherently, keeping each relation's
endpoints in its submission. Handle reported capacity errors within the bounded
tracking window; stop further admissions on configuration/authentication errors.

Poll accepted runs about every 10 seconds, increasing to at most 30 seconds while
queued. Track a batch for five minutes unless instructed otherwise, reporting
progress at least once per minute. Preserve terminal outcomes separately and keep
pending IDs when tracking ends. Queued work continues on the server. Report paired
artifacts, semantic coverage, API/messaging coverage, representative test counts
and gaps, observed/unknown readiness, run counts and pending/errors separately.
Include test assessment dispositions, inspected/documented scenarios and unique
Test Case/verification assertion counts; explain zero counts and uninspected areas.
Authored verification links are not proof of graph application or test execution.
Do not query the graph or perform usefulness acceptance as part of bootstrap;
successful ingestion is not a completeness claim.
