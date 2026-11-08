---
name: explain-code
description: Explain a selected piece of code for a learner, in a fixed four-part layout: purpose, line by line, pitfalls, try it. Use when the user selects or pastes code and asks to explain it, walk through it, or asks what it does.
allowed-tools: Read, Grep
---

# Explain code

This skill has no script. It only shapes how the explanation is written.

## When to use
- The user has selected code in the editor, or pasted code, and asks what it
  does or how it works.
- Do not use for writing new code, fixing bugs, or reviewing for quality.

## How to run
1. Identify the code to explain. Prefer the editor selection if there is one,
   then pasted text. If neither exists, ask the user to select some lines.
2. Read the surrounding file with `Read` if the selection calls functions or
   variables defined elsewhere, so the explanation can say where they come from.
3. Read `references/layout.md` in this skill's folder and follow it exactly.
   It defines the four sections, their order, and the length limits.
4. Pitch the explanation at someone learning the language. Define any term a
   beginner might not know the first time it appears.
5. Do not suggest edits to the code unless the user asks. The job is to
   explain what is there.

## Notes
- The layout lives only in `references/layout.md`. Edit that file to change
  the structure of every explanation.
- A good test selection is `numeric_stats` in
  `.claude/skills/csv-profile/scripts/profile.py`.
