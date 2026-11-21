Spec Forge inside VS Code: the same app as the desktop one in an editor panel, plus lenses and underlines on your handlers. The core is inside, nothing else to install.

## Download

| File | For |
| --- | --- |
| `spec-forge-win32-x64-{{VERSION}}.vsix` | **Windows x64** |
| `spec-forge-linux-x64-{{VERSION}}.vsix` | **Linux x64** (glibc 2.28 or later: Ubuntu 20.04+, Debian 10+) |
| `spec-forge-darwin-arm64-{{VERSION}}.vsix` | **macOS**, Apple Silicon |
| `spec-forge-darwin-x64-{{VERSION}}.vsix` | **macOS**, Intel |

## Install

1. In VS Code: `Extensions` → `⋯` → **Install from VSIX…** and pick the downloaded file.
2. Open your project folder (the one with `specforge.toml`) as the workspace and run `Spec Forge: Open`.

{{WHAT_IS_NEW}}
## Good to know

- Needs VS Code 1.90 or later and a trusted workspace.
- The core executable is not signed: Windows may show a SmartScreen or antivirus warning, and macOS blocks it until it is allowed in System Settings → Privacy & Security.
- Lenses, underlines and the tree follow the project of the folder open in the editor. Set the project's *Source repository* so handlers can be located.
- LLM provider keys are optional and go in `.env.local`. Without them, runs use the schema only.
