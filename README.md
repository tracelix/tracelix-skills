<p align="center">
   <a href="https://tracelix.ru">
      <img src="./images/logo.png" width="300">
   </a>
</p>

# Tracelix Skills

Coding-agent workflows for building and using connected repository knowledge in
[Tracelix](https://tracelix.ru). Use either skill independently or use both together.

| Skill | Purpose |
| --- | --- |
| [Tracelix Context Bootstrap](skills/tracelix-context-bootstrap/SKILL.md) | Discover repository capabilities, rules, and dependencies; generate and submit initial knowledge |
| [Tracelix Context Awareness](skills/tracelix-context-aware/SKILL.md) | Query impact before development and publish verified knowledge and the implementation plan afterward |

## Requirements

- A coding agent with skill support, local file access, command execution, and a
  native MCP client that supports Streamable HTTP and bearer-token authentication.
- Node.js 22.20+ and npm for installation with `npx skills`, or Git for the
  direct GitHub installation below.
- Python 3.9+ for the bundled renderer, which uses only the standard library.
- A Tracelix context with configured embedding and generation models.

## Install

Run from the target project and select your coding agent when prompted. Install
both skills:

```bash
npx skills add tracelix/tracelix-skills --skill '*'
```

Or install either skill independently:

```bash
npx skills add tracelix/tracelix-skills --skill tracelix-context-bootstrap
npx skills add tracelix/tracelix-skills --skill tracelix-context-aware
```

Add `-g` for user-wide installation or `--copy` to copy files instead of symlinking.
See the [installer reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
for agent selection and other options.

### Install directly from GitHub

If `npx` is unavailable or fails because of your project's Node requirements,
clone the repository and copy the complete skill folders. Run from your target
project's root on Linux, macOS, or WSL:

```bash
skills_source=$(mktemp -d)
git clone --depth 1 https://github.com/tracelix/tracelix-skills.git "$skills_source"
mkdir -p .agents/skills
cp -R "$skills_source/skills/tracelix-context-aware" \
      "$skills_source/skills/tracelix-context-bootstrap" \
      .agents/skills/
```

Replace `.agents/skills/` with your agent's project skill directory if it differs.
To install only one skill, include only that skill's source folder in the copy
command. Keep all bundled files and reload your agent's skills afterward.

This installation method uses Git and standard shell tools without invoking npm
or changing your project's Node version. Updates require copying newer skill
folders again.

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

| Tool | Used by |
| --- | --- |
| `get_context_readiness` | Both skills: validate the connection and configuration readiness |
| `get_context_ontology` | Both skills: read the active ontology |
| `submit_context_knowledge` | Both skills: submit structured knowledge |
| `get_context_ingestion_run` | Both skills: track a submitted run |
| `list_context_ingestion_runs` | Both skills: inspect ingestion history |
| `ask_context_graph` | Context Awareness: retrieve context before development and find published knowledge afterward |

The skills submit repository-derived descriptions, relationships, source paths,
hashes, and evidence anchors to that Tracelix context. Configure and authenticate
the MCP connection separately from the skills.

## Use

Open the target repository in your agent. Select a skill using the agent's skill
picker or invocation syntax, or request it by name. If needed, point the agent to
the installed skill's `SKILL.md`.

For initial repository knowledge:

```text
Use the tracelix-context-bootstrap skill to build initial knowledge for this repository.
```

For ongoing development:

```text
Use the tracelix-context-aware skill to implement this change using the connected context graph.
```

Knowledge artifacts and submission ledgers are saved under `.tracelix/` in the
target project. For tool requirements and ingestion behavior, see the
[bootstrap ingestion reference](skills/tracelix-context-bootstrap/references/ingestion.md)
and [development MCP contract](skills/tracelix-context-aware/references/mcp-contract.md).

Licensed under [MIT](LICENSE).
