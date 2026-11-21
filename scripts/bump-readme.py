"""Point the desktop and VS Code downloads of the releases README at a new version.

The CLI is released on its own, so `cli-v…` and `specforge-v…` are left alone.
"""

import re
import sys

VERSION = r"\d+\.\d+\.\d+"
PATTERNS = (
    rf"(vscode-v){VERSION}",
    rf"(spec-forge-[a-z0-9]+-[a-z0-9]+-){VERSION}(?=\.vsix)",
    rf"(Spec\.Forge\.Desktop_){VERSION}",
    rf"(/tag/v){VERSION}",
    rf"(/download/v){VERSION}",
    rf"(\[`v){VERSION}(?=`)",
)


def main() -> None:
    path, version = sys.argv[1], sys.argv[2]
    with open(path, encoding="utf-8") as readme:
        text = readme.read()
    for pattern in PATTERNS:
        text = re.sub(pattern, lambda found: found.group(1) + version, text)
    with open(path, "w", encoding="utf-8", newline="\n") as readme:
        readme.write(text)


if __name__ == "__main__":
    main()
