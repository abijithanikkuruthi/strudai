"""Compress knowledge markdown files into a brief reference for the agent.

Usage:
    uv run python -m backend.knowledge.compress
"""

import os

import anthropic
from dotenv import load_dotenv

from backend.knowledge import KNOWLEDGE_DIR, RAW_DIR

COMPRESS_PROMPT = """\
You are compressing Strudel live-coding documentation into a concise reference \
that an AI coding assistant will use at startup.

Rules:
- Output ONLY the compressed reference, no preamble or explanation.
- Target ~1500 tokens. Prefer tables and terse bullet points over prose.
- Prioritize: mini-notation syntax, common functions/methods, sound and note \
patterns, effects, modifiers, and short idiomatic code examples.
- Drop: tutorial prose, motivation, setup instructions, FAQ, niche topics \
(CSoound, Hydra, PWA, device motion, XEN).
- Group by topic. Use ```strudel``` fenced blocks for code examples.
"""

OUTPUT_FILE = KNOWLEDGE_DIR / "compressed.md"


def compress() -> str:
    """Read all knowledge .md files, send to Claude for compression, return result."""
    parts: list[str] = []
    for path in sorted(RAW_DIR.glob("*.md")):
        parts.append(f"# SOURCE: {path.name}\n\n{path.read_text()}")

    combined = "\n\n---\n\n".join(parts)

    client = anthropic.Anthropic(api_key=os.environ["CLAUDE_API_KEY"])
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=COMPRESS_PROMPT,
        messages=[{"role": "user", "content": combined}],
    )
    return response.content[0].text


def main() -> None:
    load_dotenv()
    print("Compressing knowledge files...")
    result = compress()
    OUTPUT_FILE.write_text(result)
    print(f"Wrote {OUTPUT_FILE} ({len(result)} chars)")


if __name__ == "__main__":
    main()
