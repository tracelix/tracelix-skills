# MCP Context Development Contract

Call `get_context_readiness({})` before starting graph queries or submission.
A successful response confirms the connection; `ready: false` means setup needs
attention. Report its message and preserve local work until resolved. Report tool
errors or a missing readiness tool without probing backend settings. The check
does not call model providers, so later operations may still return errors.

Use native get_context_ontology and ask_context_graph before ontology-guided
mapping/implementation. Graph answers identify impact leads; confirm concrete
methods and constraints against current code. Call `ask_context_graph` with the
intended question only; retrieval strategy is automatic and internal.

Ask about the intended change, likely components/collaborators, behavioral rules,
workflows, interfaces, tests, schemas and operational consequences. Keep graph
limitations visible without treating inferred implementation details as fact.

Before each post-implementation submission, use ask_context_graph to find published
knowledge about the implemented feature. Reuse verified entity types, names and
available identifiers as described in the quality reference. Include existing
targets as locally identified entities in the payload; never pass graph record IDs
as endpoints or identifiers. Ground their descriptions and links in inspected
evidence. Report missing published targets as coverage gaps.

After verification, follow the [shared structured contract](structured-knowledge.md)
and [quality reference](kb-template.md). The canonical payload must include the
implementation plan as a Requirement entity, its saved `.plan.md` as hashed source
evidence, and supported typed relationships to feature knowledge. Resolve type IDs
and relationship direction from the refreshed live ontology. If it cannot express
the Requirement or necessary links, leave affected artifacts pending and report
the blocker.

Submit the canonical JSON object through submit_context_knowledge, track through
existing run tools, and preserve attempt history. Keep the existing schema; no
context selector, raw Markdown, extraction-only evidence fields or JSON string
wrappers are accepted. Missing structured tools leave artifacts pending; never
fall back to submit_context_ingestion for these agent-authored records.
