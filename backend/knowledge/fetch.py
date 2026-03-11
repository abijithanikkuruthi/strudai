"""Fetch and clean Strudel MDX files into Markdown reference documents.

Usage:
    uv run python -m backend.knowledge.fetch              # fetch all sources
    uv run python -m backend.knowledge.fetch workshop      # fetch one source
    uv run python -m backend.knowledge.fetch workshop recipes  # fetch multiple
"""

import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path

BASE_RAW_URL = (
    "https://codeberg.org/uzu/strudel/raw/branch/main"
    "/website/src/pages"
)

KNOWLEDGE_DIR = Path(__file__).resolve().parent
RAW_DIR = KNOWLEDGE_DIR / "raw"


@dataclass
class Source:
    path: str
    pages: list[str]


SOURCES: dict[str, Source] = {
    "workshop": Source(
        path="workshop",
        pages=[
            "recap",
            "first-sounds",
            "first-notes",
            "first-effects",
            "pattern-effects",
            "getting-started",
        ],
    ),
    "understand": Source(
        path="understand",
        pages=["cycles", "pitch", "voicings"],
    ),
    "recipes": Source(
        path="recipes",
        pages=["arpeggios", "microrhythms", "recipes", "rhythms"],
    ),
    "learn": Source(
        path="learn",
        pages=[
            "mini-notation",
            "sounds",
            "notes",
            "effects",
            "signals",
            "samples",
            "synths",
            "tonal",
            "time-modifiers",
            "random-modifiers",
            "conditional-modifiers",
            "stepwise",
            "factories",
            "code",
            "visual-feedback",
            "colors",
            "input-output",
            "input-devices",
            "faq",
            "csound",
            "hydra",
            "accumulation",
            "getting-started",
            "strudel-vs-tidal",
            "mondo-notation",
            "xen",
            "pwa",
            "metadata",
            "devicemotion",
        ],
    ),
}


def clean_mdx(text: str) -> str:
    """Strip MDX artifacts from content, returning clean Markdown."""
    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n?", "", text, count=1, flags=re.DOTALL)

    # Remove import lines
    text = re.sub(r"^import\s+.*$\n?", "", text, flags=re.MULTILINE)

    # Handle <MiniRepl ... /> inside table cells FIRST
    # In tables, render as inline code to preserve table structure
    def _replace_table_minirepl(m: re.Match) -> str:
        prefix = m.group(1)  # everything before the MiniRepl in the cell
        tune = m.group(2)
        return f"{prefix}`{tune}`"

    text = re.sub(
        r"(\|[^|]*?)<MiniRepl\s[^>]*?tune=\{`([^`]*?)`\}[^/]*/\s*>",
        _replace_table_minirepl,
        text,
    )

    # Handle remaining <MiniRepl ... /> components (single or multiline)
    def _replace_minirepl(m: re.Match) -> str:
        tune = m.group(1)
        return f"\n```strudel\n{tune}\n```\n"

    text = re.sub(
        r"<MiniRepl\s[^>]*?tune=\{`(.*?)`\}[^/]*/\s*>",
        _replace_minirepl,
        text,
        flags=re.DOTALL,
    )

    # Handle MiniRepl with single-quote tune (e.g. tune={'...'})
    # Table context: inline code
    def _replace_table_minirepl_sq(m: re.Match) -> str:
        prefix = m.group(1)
        tune = m.group(2).replace("\\n", "\n")
        # For table cells, use inline code (collapse newlines to semicolons)
        inline = tune.replace("\n", "; ")
        return f"{prefix}`{inline}`"

    text = re.sub(
        r"(\|[^|]*?)<MiniRepl\s[^>]*?tune=\{'(.*?)'\}[^/]*/\s*>",
        _replace_table_minirepl_sq,
        text,
    )

    # Non-table single-quote tune
    def _replace_minirepl_sq(m: re.Match) -> str:
        tune = m.group(1).replace("\\n", "\n")
        return f"\n```strudel\n{tune}\n```\n"

    text = re.sub(
        r"<MiniRepl\s[^>]*?tune=\{'(.*?)'\}[^/]*/\s*>",
        _replace_minirepl_sq,
        text,
    )

    # Remove any remaining MiniRepl tags (e.g. tunes={...} variant)
    text = re.sub(r"<MiniRepl\s[^/]*/\s*>", "", text)

    # Strip <Box>, </Box>, <QA ...>, </QA> wrapper tags (keep inner content)
    text = re.sub(r"</?Box[^>]*>", "", text)
    text = re.sub(r"</?QA[^>]*>", "", text)

    # Strip <img ... /> tags
    text = re.sub(r"<img[^>]*/?\s*>", "", text)

    # Strip <a ...>...</a> tags (keep inner text)
    text = re.sub(r"<a[^>]*>(.*?)</a>", r"\1", text, flags=re.DOTALL)

    # Collapse 3+ consecutive blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


def fetch_source(name: str) -> None:
    """Fetch a single source's MDX files from Codeberg, clean them, and write {name}.md."""
    source = SOURCES.get(name)
    if source is None:
        raise KeyError(f"Unknown source: {name}. Available: {', '.join(SOURCES)}")

    sections: list[str] = []
    for page in source.pages:
        url = f"{BASE_RAW_URL}/{source.path}/{page}.mdx"
        print(f"Fetching {url} ...")
        with urllib.request.urlopen(url) as resp:
            raw = resp.read().decode()
        cleaned = clean_mdx(raw)
        sections.append(cleaned)

    combined = "\n\n---\n\n".join(sections)
    RAW_DIR.mkdir(exist_ok=True)
    output = RAW_DIR / f"{name}.md"
    output.write_text(combined)
    print(f"Wrote {output} ({len(combined)} chars)")


def fetch_all() -> None:
    """Fetch all sources."""
    for name in SOURCES:
        fetch_source(name)


if __name__ == "__main__":
    names = sys.argv[1:] if len(sys.argv) > 1 else list(SOURCES)
    for name in names:
        fetch_source(name)
