---
name: pr-review
description: List active Azure DevOps pull requests and review their code changes.  Use when the user asks to check, list, or review Azure DevOps PRs.
---

#Review Azure DevOps pull requests

1. List active PRs:

   `az repos pr list --status active --output json`
   If there are none, say so and stop

2. For each PR, note: id, title, author, sourceRefName, targetRefName.

3. Get the diff:

   `git fetch origin`
   `git diff origin/<target>...origin/<source>`

4. Review the diff for: bugs, missing error handling, hardcoded secrets, unclear naming.

5. Report one section per PR:

   -PR id and title
   -Verdict: LOOKS GOOD or NEEDS CHANGES
   -Findings, each with file and line

Do NOT approve, vote on, or merge any PR.

