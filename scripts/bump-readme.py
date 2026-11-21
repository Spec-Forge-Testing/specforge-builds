"""Point the downloads of the releases README at a new version, for the components released."""

import re
import sys

VERSION = r"\d+\.\d+\.\d+"
PATTERNS = {
    "desktop": (
        rf"(vscode-v){VERSION}",
        rf"(spec-forge-[a-z0-9]+-[a-z0-9]+-){VERSION}(?=\.vsix)",
        rf"(Spec\.Forge\.Desktop_){VERSION}",
        rf"(/tag/v){VERSION}",
        rf"(/download/v){VERSION}",
        rf"(\[`v){VERSION}(?=`)",
    ),
    "cli": (rf"(cli-v){VERSION}",),
}


def main() -> None:
    path, version, components = sys.argv[1], sys.argv[2], sys.argv[3:]
    with open(path, encoding="utf-8") as readme:
        text = readme.read()
    for component in components:
        for pattern in PATTERNS[component]:
            text = re.sub(pattern, lambda found: found.group(1) + version, text)
    with open(path, "w", encoding="utf-8", newline="\n") as readme:
        readme.write(text)


if __name__ == "__main__":
    main()
