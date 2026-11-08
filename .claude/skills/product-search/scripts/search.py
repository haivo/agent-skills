"""Search the product catalog. Usage: python search.py "<keyword>" """

import os
import sys
from pathlib import Path


def _find_project_root() -> Path:
    """Locate the folder containing simple_agent.py.

    Walks up from this file (which may be reached through a junction from a
    parent workspace) and checks each ancestor and its SimpleAgent subfolder.
    """
    here = Path(__file__).resolve()
    for parent in here.parents:
        for candidate in (parent, parent / "SimpleAgent"):
            if (candidate / "simple_agent.py").is_file():
                return candidate
    sys.exit("Error: could not find simple_agent.py above " + str(here))


sys.path.insert(0, str(_find_project_root()))

# simple_agent constructs an Anthropic client at import time, which fails
# without an API key. The search itself never calls the API, so supply a
# placeholder when the key is absent.
os.environ.setdefault("ANTHROPIC_API_KEY", "not-needed-for-search")

# The local pg-simple-agent Docker container publishes PostgreSQL on host
# port 5433, while simple_agent.py defaults to 5432. Prefer 5433 unless the
# caller has already set POSTGRES_PORT.
os.environ.setdefault("POSTGRES_PORT", "5433")

from simple_agent import run_search_database  # noqa: E402

if len(sys.argv) != 2:
    print('Usage: python search.py "<keyword>"')
    sys.exit(2)

print(run_search_database(sys.argv[1]))
