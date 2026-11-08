# Explanation layout

Produce exactly these four sections, in this order, with these bold labels.
No headers, no extra sections.

**Purpose.** One or two sentences. What this code achieves and where it sits
in the larger program. Name the caller if it is known.

**Line by line.** A bulleted list with one bullet per statement or logical
group of lines. Each bullet quotes the code in backticks, then explains it in
plain words. Keep each bullet to two sentences. If a line uses a library call,
say which module it comes from and what it returns.

**Pitfalls.** Two to four bullets. Things that commonly confuse learners about
this code, edge cases it handles, or edge cases it does not handle. If there
is nothing worth flagging, write a single bullet saying so.

**Try it.** One to three bullets suggesting a small experiment the reader can
do in the debugger or by running the script: a value to inspect, an input to
change, a line to comment out. Each should be doable in under a minute.

Rules:
- Use a table only when comparing three or more parallel items.
- Do not propose rewrites or improvements.
- Total length about 250 to 400 words.
