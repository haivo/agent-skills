"""csv-reviewer: a small agent that checks whether a CSV is clean.

Usage:
    py -3.14 agent.py <path-to-csv>

The loop below is the whole idea of an agent:
  1. ask the model what to do,
  2. run any tool it asked for,
  3. append the result to the conversation,
  4. repeat until the model answers in plain text.
"""

import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv

from tools import TOOLS, execute_tool

HERE = Path(__file__).parent
MODEL = "claude-opus-5-5"


def load_system_prompt() -> str:
    return (HERE / "prompts" / "system.md").read_text(encoding="utf-8")


def run(csv_path: str) -> str:
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    system = load_system_prompt()
    messages = [{"role": "user", "content": f"Review this CSV file: {csv_path}"}]

    for _ in range(10):  # hard stop so a confused model cannot loop forever
        response = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if b.type == "text")

        if response.stop_reason == "refusal":
            return "The model declined to process this request."

        if response.stop_reason == "max_tokens":
            return "The response was cut off. Try a smaller file."

        if response.stop_reason != "tool_use":
            # pause_turn or anything new: send the turn back and continue
            messages.append({"role": "assistant", "content": response.content})
            continue

        # The model asked for one or more tools. Run them all, then reply
        # with every result in a single user message.
        messages.append({"role": "assistant", "content": response.content})
        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  -> {block.name}({block.input})", file=sys.stderr)
                text, is_error = execute_tool(block.name, block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": text,
                    "is_error": is_error,
                })
        messages.append({"role": "user", "content": results})

    return "Stopped after 10 turns without a final answer."


def main():
    load_dotenv(HERE / ".env")
    if len(sys.argv) != 2:
        print("Usage: py -3.14 agent.py <path-to-csv>")
        sys.exit(1)
    print(run(sys.argv[1]))


if __name__ == "__main__":
    main()
