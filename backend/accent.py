import re

# Light German accent transformation.
# Rules sourced from instructables.com/How-To-Type-and-Talk-With-a-German-Accent/
# Kept minimal to stay readable — only the most recognisable swaps.

_RULES: list[tuple[re.Pattern, str]] = [
    # "th" at word start → "z" (the → ze, that → zat, this → zis)
    (re.compile(r"\b[Tt]h", re.UNICODE), lambda m: "Z" if m.group()[0].isupper() else "z"),
    # "w" at word start → "v" (with → viz, was → vas, what → vat)
    (re.compile(r"\bW"), "V"),
    (re.compile(r"\bw"), "v"),
]


def germanise(text: str) -> str:
    """Apply a light German accent to plain text, skipping code blocks."""
    parts = re.split(r"(```[\s\S]*?```|`[^`]+`)", text)
    for i, part in enumerate(parts):
        if part.startswith("`"):
            continue
        for pattern, repl in _RULES:
            part = pattern.sub(repl, part)
        parts[i] = part
    return "".join(parts)
