The Spec Forge desktop app: contract, runs, findings and comparisons in a window of its own. The core is inside, nothing else to install.

## Download

| File | For |
| --- | --- |
| `Spec.Forge.Desktop_{{VERSION}}_x64-setup.exe` | **Windows x64** (the `.msi` installs the same app) |
| `Spec.Forge.Desktop_{{VERSION}}_amd64.deb` | **Linux x64** (Ubuntu 22.04+, Linux Mint 21+, Debian 12+) |
| `Spec.Forge.Desktop_{{VERSION}}_aarch64.dmg` | **macOS**, Apple Silicon |
| `Spec.Forge.Desktop_{{VERSION}}_x64.dmg` | **macOS**, Intel |

## Install

- **Windows:** run the installer.
- **Linux:** `sudo apt install ./Spec.Forge.Desktop_{{VERSION}}_amd64.deb`
- **macOS:** open the `.dmg`, drag the app to Applications and run `xattr -cr "/Applications/Spec Forge Desktop.app"` once.

{{WHAT_IS_NEW}}
## Good to know

- The installers are not signed: Windows may show a SmartScreen or antivirus warning, and macOS needs the `xattr` step above.
- LLM provider keys are optional. Without them, runs use the schema only.
