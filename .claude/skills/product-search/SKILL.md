---
name: product-search
description: Search the SimpleAgent product catalog in PostgreSQL by name or category keyword. Use when the user asks what products exist, what something costs, or what is in a category (Electronics, Furniture).
allowed-tools: Bash(py -3.14 .claude/skills/product-search/scripts/search.py:*), Bash(python .claude/skills/product-search/scripts/search.py:*), Read
---

# Product search

Look up products in the `products` table that `simple_agent.py` creates and seeds.

## When to use
- The user asks about products, prices, or categories in this project's catalog.
- Do not use for general shopping questions outside this catalog.

## How to run
1. Pick one keyword from the user's request. It matches against product name
   or category, case-insensitive, as a substring.
2. Run the search script from the project root (`SimpleAgent/`) and read its
   output. Use the `py -3.14` launcher: plain `python` is not on PATH on this
   machine, and the default `py` interpreter lacks `psycopg2`.

   ```bash
   py -3.14 .claude/skills/product-search/scripts/search.py "<keyword>"
   ```

   Output is a JSON list of `{name, category, price}` objects, or a
   "No products found" message, or a line starting with `Error:`.
3. If nothing matched, retry once with a broader keyword (for example the
   category instead of the product name), then tell the user nothing matched.
4. If the output starts with `Error:`, PostgreSQL is probably not reachable.
   Check that the `pg-simple-agent` Docker container is running (`docker ps`).
   Show the error and point the user at the connection variables below.
5. Report results as a short table: name, category, price.

## Notes
- Connection settings come from `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`,
  `POSTGRES_USER`, `POSTGRES_PASSWORD`. The app defaults to `localhost:5432`,
  but the local `pg-simple-agent` Docker container publishes PostgreSQL on host
  port **5433**, so `search.py` defaults `POSTGRES_PORT` to `5433` when it is
  not already set. Database `simple_agent`, user and password `postgres`.
- The table is created and seeded with six rows on first use.
- Column details and seed data are in `references/schema.md`.
