# Spec Forge builds

Build workflows for Spec Forge release artifacts. No product source lives here: the workflows
check out the source repositories at build time, build on GitHub's runners and leave the
finished binaries as workflow artifacts.

To install Spec Forge, go to
[specforge-releases](https://github.com/Spec-Forge-Testing/specforge-releases).

## Release

`.github/workflows/release.yml` builds, for Windows x64, Linux x64, macOS Apple Silicon and
macOS Intel:

- the core, from the commit you give;
- the desktop installer (`.exe` and `.msi`, `.deb`, `.dmg`);
- the VS Code package (`.vsix`) with the core inside.

Run it from the Actions tab (**Release** → **Run workflow**):

| Input | What it is |
| --- | --- |
| `version` | The version to release. The desktop app and the extension must already declare it. |
| `core_ref` | Commit of the core to build. |
| `desktop_ref` | Commit of the desktop app and the extension to build. |
| `protocol_version` | Protocol version the built core must answer the handshake with. |
| `highlights` | Optional "What is new" items, separated by `;`. |
| `publish` | Off: the files stay attached to the run for seven days. On: see below. |

With `publish` on, it creates `v<version>` (desktop) and `vscode-v<version>` (extension) in
specforge-releases, with the notes from `notes/`, and opens a pull request there that points
the README's download links at the new version. It refuses to overwrite a version that is
already published.

It needs two repository secrets:

- `SOURCE_READ_TOKEN`: reads the contents of the two source repositories and nothing else.
- `RELEASES_WRITE_TOKEN`: writes contents and pull requests in specforge-releases and nothing
  else.

The logs of this repository are public. Build output is written to files on the runner and
only the last lines of a failed step are printed.
