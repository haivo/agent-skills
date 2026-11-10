# agent-skills

Practice skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), built while
learning how agent skills work. A skill is a folder with a `SKILL.md` file: YAML frontmatter that
controls when it triggers and which tools it may use, followed by instructions the agent follows.

## Skills

| Skill | What it does | Where the output is produced |
|-------|--------------|------------------------------|
| `csv-summary` | Row/column counts and a min/max/mean table for a CSV | Python script prints the finished table |
| `csv-profile` | Same stats as JSON and as a table | Python script prints both |
| `explain-code` | Explains a code selection in a fixed four-part layout | Agent writes prose, guided by `references/layout.md` |
| `product-search` | Searches a PostgreSQL product catalog by keyword | Python script queries the DB, agent formats a table |

## How a skill is triggered

- **Explicit:** type the slash command, e.g. `/csv-summary path/to/file.csv`.
- **Implicit:** the agent matches the request against each skill's `description` and loads the
  one that fits, e.g. "what's in sales.csv?" loads `csv-summary` without naming it.

## Design note: who produces the output

Early versions of the CSV skills had the script emit raw JSON and the agent write the table from a
one-line instruction. The current versions move formatting into the script. Both are valid skills;
the trade-off is:

- **Agent-formatted:** flexible, layout can be changed by editing markdown, but may vary between runs.
- **Script-formatted:** identical every run, but layout changes mean editing code.

Rule of thumb: give the script anything that must be exact, give the agent anything that needs
judgment or language. `explain-code` is all judgment, so it has no script at all.

## Running locally

Scripts use the standard library only. On this machine Python is launched with `py -3.14`.

```powershell
py -3.14 .claude\skills\csv-profile\scripts\profile.py .claude\skills\csv-profile\samples\sales.csv
```

`.vscode/launch.json` has debug configurations for `profile.py`. `product-search` needs the
`pg-simple-agent` Docker container from the SimpleAgent project.
