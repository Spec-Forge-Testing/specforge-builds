"""Print a release notes template with its version and, when given, its highlights."""

import sys

VERSION_MARK = "{{VERSION}}"
HIGHLIGHTS_MARK = "{{WHAT_IS_NEW}}\n"
HIGHLIGHTS_HEADING = "## What is new\n\n"


def highlights_section(raw: str) -> str:
    items = [item.strip() for item in raw.split(";") if item.strip()]
    if not items:
        return ""
    return HIGHLIGHTS_HEADING + "".join(f"- {item}\n" for item in items) + "\n"


def main() -> None:
    template_path, version, raw_highlights = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(template_path, encoding="utf-8") as template:
        notes = template.read()
    notes = notes.replace(HIGHLIGHTS_MARK, highlights_section(raw_highlights))
    sys.stdout.write(notes.replace(VERSION_MARK, version))


if __name__ == "__main__":
    main()
