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
- the desktop installer (`.exe` and `.msi`, `.deb`, `.dmg`) and the VS Code package (`.vsix`),
  each with that core inside;
- the CLI archive (`.zip`, `.tar.xz`), with that core inside.

Run it from the Actions tab (**Release** → **Run workflow**):

| Input | What it is |
| --- | --- |
| `version` | The version to release. Every source given below must already declare it. |
| `core_ref` | Commit of the core to build. |
| `protocol_version` | Protocol version the built core must answer the handshake with. |
| `desktop_ref` | Commit of the desktop app and the extension. Empty: neither is built. |
| `cli_ref` | Commit of the CLI. Empty: it is not built. |
| `highlights` | Optional "What is new" items, separated by `;`. |
| `publish` | Off: the files stay attached to the run for seven days. On: see below. |

With `publish` on, it creates in specforge-releases `v<version>` (desktop), `vscode-v<version>`
(extension) and `cli-v<version>` (CLI, with its `SHA256SUMS`) for what was built, with the notes
from `notes/`, and opens a pull request there that points the README's download links at the
new version. It refuses to overwrite a version that is already published.

When a CLI is given it also builds the container image `specforge ci init` points a pipeline
at, `ghcr.io/spec-forge-testing/specforge:<version>`, from the same core commit, and checks it
starts. With `publish` on, the image is pushed before the releases are created, and never over a
tag that already exists. The package has to grant this repository write access (its settings →
Manage Actions access).

It needs two repository secrets:

- `SOURCE_READ_TOKEN`: reads the contents of the three source repositories and nothing else.
- `RELEASES_WRITE_TOKEN`: writes contents and pull requests in specforge-releases and nothing
  else.

The logs of this repository are public. Build output is written to files on the runner and
only the last lines of a failed step are printed.
