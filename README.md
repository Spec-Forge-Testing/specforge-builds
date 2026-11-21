# Spec Forge builds

Build workflows for Spec Forge release artifacts. No product source lives here: the workflows
check out the source repositories at build time, build on GitHub's runners and leave the
finished binaries as workflow artifacts.

To install Spec Forge, go to
[specforge-releases](https://github.com/Spec-Forge-Testing/specforge-releases).

## macOS builds

`.github/workflows/macos.yml` builds, for Apple Silicon and for Intel:

- the desktop installer (`.dmg`);
- the VS Code package (`.vsix`) with the core inside.

Run it from the Actions tab (**macOS builds** → **Run workflow**), giving the commit of the
core and the commit of the desktop app to build. The results are attached to the run as
artifacts for seven days; publishing them to a release is a separate, manual step.

It needs one repository secret, `SOURCE_READ_TOKEN`: a token that can read the contents of
the two source repositories and nothing else.

The logs of this repository are public. Build output is written to files on the runner and
only the last lines of a failed step are printed.
