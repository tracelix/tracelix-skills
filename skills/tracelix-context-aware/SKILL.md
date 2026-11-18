---
name: tracelix-context-aware
description: Use for software development requests that modify source code, tests, APIs, UI components, services, schemas, or shared logic. Before editing, query the MCP context graph with ask_context_graph to identify affected components. After implementation, submit concise .tracelix/kb/ knowledge and the implementation plan as a Requirement linked to published feature knowledge through submit_context_knowledge.
---

# Tracelix Context Awareness

Use this skill to connect code changes to the project knowledge graph without making Codex run a connector command for every request.

Assume the MCP server is already configured by the runtime and exposes native tools named `get_context_readiness`, `ask_context_graph`, `get_context_ontology`, and `submit_context_knowledge`. Do not create ad hoc clients or shell out to a connector unless the native MCP tools are unavailable and the user explicitly approves a fallback.

## Connection and Readiness

Call `get_context_readiness({})` before graph queries or knowledge submissions.
A successful response confirms the connection. If `ready` is false, report the
returned message and preserve local work until setup is complete. On a tool error
or missing tool, report the blocker; do not infer readiness or inspect backend
settings. This check does not call model providers or guarantee later execution.

## Workflow

1. Inspect the user's development request and relevant source code to identify the intended change, collaborators, methods, and evidence paths.
2. Before ontology-guided repository mapping or KB generation, call `get_context_ontology({})` through the same MCP connection used for ingestion. Use only its catalog to classify entities and relationships; never use local ontology documents, bundled copies, remembered catalogs, or graph-query answers as a fallback.
3. Before editing source files, call `ask_context_graph` with the intended change. Use `references/mcp-contract.md` for tool contracts.
4. Use the affected components to adjust implementation and verification. Retain the
   implementation plan in `.tracelix/kb/<topic>.plan.md`, preserving agreed revisions
   as the work proceeds, then implement using existing repository patterns. If no
   explicit plan exists, record a concise one before implementation; do not invent
   retrospective intent.
5. After verification, author or update a concise canonical `.knowledge.json` artifact
   under `.tracelix/kb/`. Read the [quality reference](references/kb-template.md) and
   [shared structured contract](references/structured-knowledge.md). Preserve unrelated
   maintained content. Include the plan used for the completed implementation as a
   Requirement entity whose description preserves intended behavior, implementation
   approach, constraints and acceptance criteria. Cite the saved plan as evidence.
   Before submission, query published feature knowledge with `ask_context_graph`
   and link the Requirement to verified existing entities using live ontology
   relationships and directed endpoint rules; follow the quality reference for
   identity reuse and missing targets. Omit unsupported assertions and record
   coverage gaps separately; do not omit the required plan entity.
6. Validate descriptions, active catalog IDs, directed endpoint references and
   inspected evidence; include verified implementation-file relationships where the
   catalog requires them. Hash evidence files, including `<topic>.plan.md`, and
   record Git provenance.
7. Refresh the live ontology before each batch. Revalidate/regenerate affected JSON
   on context/revision/fingerprint changes; failed refresh leaves artifacts pending.
8. Use the shared deterministic renderer to canonicalize JSON and create the paired
   Markdown. Submit the parsed object through `submit_context_knowledge`; do not
   independently author the generated Markdown review view or fall back to document
   extraction. The authored `.plan.md` is a separate evidence file.
9. Preserve a local `.tracelix/knowledge-submissions.json` ledger with paired paths,
   input format/schema version, canonical payload/evidence hashes, connection/context
   identity, ontology identity and attempt history. Save document/run IDs immediately.
   Track through existing get/list run tools; ambiguous outcomes remain outcome_unknown.
   Skip unchanged prior success only after checking its identity/hashes and refreshing
   the saved run. Changes do not replace old assertions. Report pending or failed work.

## Knowledge Base Artifacts

JSON carries authored descriptions and inspected evidence references directly into
shared graph application. Markdown is a deterministic review view. Retain live
ontology guidance, semantic coverage and implementation-file traceability; schema
validation cannot establish factual correctness. Use `get_context_readiness` to
check setup and track actual submission outcomes through the run tools.

## MCP Expectations

The skill depends on native MCP tools rather than a per-request connector script.

If `ask_context_graph` is unavailable, state that the impact query could not be performed and continue only if the user still wants the change.

If `submit_context_knowledge` is unavailable after the KB article is written, leave the paired artifacts in `.tracelix/kb/` pending and report the missing capability. Do not fall back to text ingestion.

If `get_context_ontology` is absent, fails, or cannot express the plan as a Requirement, its necessary relationships, or the requested implementation-file traceability for the affected article, stop affected KB generation/submission and report the blocker. Leave affected artifacts pending and keep existing articles intact. Local source inspection and already authorized development may continue. Do not invent an ontology or substitute relationships.
