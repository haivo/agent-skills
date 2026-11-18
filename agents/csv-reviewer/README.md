# csv-reviewer

A small standalone agent that decides whether a CSV file is clean enough to load.
It calls the Claude API in a loop, uses four plain Python tools to inspect the file,
and ends with a one-line verdict.

```
agent.py             the agent loop
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

## Test

```powershell
py -3.14 -m pytest tests -q
```
