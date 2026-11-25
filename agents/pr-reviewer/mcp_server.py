import os
import subprocess

from mcp.server.fastmcp import FastMCP

# The folder holding the Azure DevOps clone. Set in mcp.json (Step 2).
REPO_DIR = os.environ.get("REPO_DIR", ".")

mcp = FastMCP("pr-reviewer")


def run(args: list[str]) -> str:
    """Run a command in the repo folder and return what it printed."""
    result = subprocess.run(
        args, cwd=REPO_DIR, capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


@mcp.tool()
def list_active_prs() -> str:
    """List the active Azure DevOps pull requests as JSON. Call this first."""
    return run(["az.cmd", "repos", "pr", "list", "--status", "active", "--output", "json"])


@mcp.tool()
def get_pr_diff(source_branch: str, target_branch: str) -> str:
    """Return the code changes of a pull request.

    Pass branch names without the refs/heads/ prefix, e.g. "main".
    """
    run(["git", "fetch", "origin"])
    return run(["git", "diff", f"origin/{target_branch}...origin/{source_branch}"])


if __name__ == "__main__":
    mcp.run(transport="stdio")