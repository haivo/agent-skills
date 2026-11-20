"""csv-reviewer as an MCP server: the same four tools, without the agent loop.

Compare with agent.py:
  agent.py       runs the loop itself and calls the Claude API (needs an API key).
  mcp_server.py  only offers the tools. The client (GitHub Copilot, Claude Code)
                 brings its own model and runs the loop, so there is no
                 `anthropic` import and no API key here.

Both files use the same registry in tools/__init__.py, so a tool added there
shows up in both places.

The client starts this file as a local process and talks to it over stdio.
You do not run it by hand, except to check that it starts:
    py -3.14 mcp_server.py
"""

import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from tools import FUNCTIONS, TOOLS

HERE = Path(__file__).parent
SYSTEM_PROMPT = (HERE / "prompts" / "system.md").read_text(encoding="utf-8")

# stdout carries the protocol, so keep the library quiet.
logging.getLogger("mcp").setLevel(logging.WARNING)

# `instructions` is the nearest thing to a system prompt that a server can
# offer. The client decides whether to show it to its model.
mcp = FastMCP("csv-reviewer", instructions=SYSTEM_PROMPT)

# Register every tool from the shared registry. FastMCP builds the input
# schema from each function's signature (path: str); the description comes
# from TOOLS so the model reads the same text in both versions.
# If a function raises (for example FileNotFoundError), FastMCP sends the
# message back to the client as an error result. That replaces the
# try/except in tools.execute_tool.
for tool in TOOLS:
    mcp.add_tool(
        FUNCTIONS[tool["name"]],
        name=tool["name"],
        description=tool["description"],
    )


@mcp.prompt()
def review_csv(path: str) -> str:
    """Review a CSV file and give a verdict, following the csv-reviewer instructions."""
    # A prompt is a ready-made message the user picks in the client. This is
    # how the standalone agent's system prompt travels to a client we do not
    # control.
    return f"{SYSTEM_PROMPT}\nReview this CSV file: {path}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
