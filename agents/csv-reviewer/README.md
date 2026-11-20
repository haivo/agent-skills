# csv-reviewer

A small standalone agent that decides whether a CSV file is clean enough to load.
It calls the Claude API in a loop, uses four plain Python tools to inspect the file,
and ends with a one-line verdict.

```
agent.py             the agent loop
mcp_server.py        the same tools as an MCP server, for Copilot and other clients
tools/__init__.py    registry: tool name -> function + JSON schema
tools/csv_checks.py  the four inspection functions (no model code)
prompts/system.md    the instructions the model follows
tests/test_tools.py  tests for the tools, no API key needed
samples/             clean.csv and messy.csv to try
```

## Run

```powershell
cd agents\csv-reviewer
copy .env.example .env        # then put your key in .env, or set ANTHROPIC_API_KEY
py -3.14 agent.py samples\messy.csv
```

Tool calls are printed to stderr as they happen so you can watch the loop.

## Use from GitHub Copilot (MCP)

`mcp_server.py` offers the four tools to any MCP client. It has no agent loop and
needs no API key: the client's own model decides when to call the tools.

`.vscode/mcp.json` at the repository root registers it for VS Code. Open that file,
click **Start** above `csv-reviewer`, then in Copilot Chat (Agent mode) ask:

```
Review agents/csv-reviewer/samples/messy.csv
```

The `/mcp.csv-reviewer.review_csv` prompt sends the same instructions the
standalone agent uses in `prompts/system.md`.

## Test

```powershell
py -3.14 -m pytest tests -q
```
