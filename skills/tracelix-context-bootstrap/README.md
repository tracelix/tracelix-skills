# Tracelix Context Bootstrap

Discover repository capabilities, rules, and dependencies; generate and submit
initial connected knowledge. See [SKILL.md](SKILL.md) for the workflow and
[ingestion reference](references/ingestion.md) for tool requirements. This package
works independently of the context-aware skill.

## Requirements

- A coding agent with skill support, local file access, command execution, and a
  native MCP client that supports Streamable HTTP and bearer-token authentication.
- Node.js 22.20+ and npm for installation with `npx skills`.
- Python 3.9+ for the bundled renderer, which uses only the standard library.
- A Tracelix context with a published ontology and configured embedding and
  generation models.

## Install

Run from the target project and select your coding agent when prompted:

```bash
npx skills add tracelix/tracelix-skills --skill tracelix-context-bootstrap
```

Add `-g` for user-wide installation or `--copy` to copy files instead of symlinking.
See the [installer reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for other options.

## Connect Tracelix

1. Create a service user in the intended context's **Service users** settings and
   securely save the token shown on creation.
2. Obtain the Streamable HTTP `/mcp` endpoint from your Tracelix operator.
3. Register the server in your agent's MCP settings using the connection details
   below. Configuration syntax and secret storage depend on the agent; use its
   supported secret or environment-variable mechanism for the token.
4. Connect or reload the server, then ask the agent to call
   `get_context_readiness({})`. A successful response confirms the connection. If
   `ready` is `false`, follow the returned message to complete setup in Tracelix
   and run the check again. The check does not call model providers, so provider
   availability is established when you use the workflows.

| Setting | Value |
| --- | --- |
| Transport | Streamable HTTP |
| Server URL | Your operator's endpoint, for example `https://YOUR_TRACELIX_HOST/mcp` |
| Authentication | Service-user token sent as `Authorization: Bearer <SERVICE_USER_TOKEN>` |

Confirm that the agent can access these tools through the connection:

| Tool | Purpose |
| --- | --- |
| `get_context_readiness` | validate the connection and configuration readiness |
| `get_context_ontology` | read the active ontology |
| `submit_context_knowledge` | submit structured knowledge |
| `get_context_ingestion_run` | track a submitted run |
| `list_context_ingestion_runs` | inspect ingestion history |

This skill submits repository-derived descriptions, relationships, source paths,
hashes, and evidence anchors to that Tracelix context. Configure and authenticate
the MCP connection separately from the skill.

## Use

Open the target repository in your agent. Select a skill using the agent's skill
picker or invocation syntax, or request it by name. If needed, point the agent to
the installed skill's `SKILL.md`.

```text
Use the tracelix-context-bootstrap skill to build initial knowledge for this repository.
```

Artifacts and submission history are written under the target project's `.tracelix/`.

Successful ingestion is the endpoint; bootstrap does not query the graph or
verify retrieval usefulness.

The [knowledge contract](references/structured-knowledge.md) and
[renderer](scripts/render_knowledge.py) are bundled locally.

Licensed under [MIT](LICENSE).
