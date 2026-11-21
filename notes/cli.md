The Spec Forge CLI, for the terminal and CI. The core is inside, nothing else to install.

## Download

| File | For |
| --- | --- |
| `specforge-v{{VERSION}}-windows-x86_64.zip` | **Windows x64** |
| `specforge-v{{VERSION}}-linux-x86_64.tar.xz` | **Linux x64** (Ubuntu 22.04+, Linux Mint 21+) |
| `specforge-v{{VERSION}}-macos-arm64.tar.xz` | **macOS**, Apple Silicon (M1 or later) |
| `specforge-v{{VERSION}}-macos-x86_64.tar.xz` | **macOS**, Intel |

`SHA256SUMS` lists the checksum of each.

## Install

- **Windows** (PowerShell): `powershell -c "irm https://raw.githubusercontent.com/Spec-Forge-Testing/specforge-releases/master/install.ps1 | iex"`
- **Linux and macOS:** `curl -fsSL https://raw.githubusercontent.com/Spec-Forge-Testing/specforge-releases/master/install.sh | sh`

Both install for the current user, without `sudo` or administrator rights, and pick this release's file on their own. Then run `specforge` inside your API's folder.

{{WHAT_IS_NEW}}
## Good to know

- `specforge update` updates an installed CLI in place; `specforge delete` removes it.
- The macOS builds are not signed. If you download the archive by hand instead of using the installer, run `xattr -dr com.apple.quarantine specforge/` once after extracting it.
- LLM provider keys are optional. Without them, runs use the schema only.
