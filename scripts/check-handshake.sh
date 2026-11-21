#!/usr/bin/env bash
# Starts the built core and checks it answers `hello` with the expected protocol version.
set -euo pipefail
core_dir="$1"
protocol="$2"

launcher=$(find "$core_dir" -maxdepth 1 -type f -name 'python-core-*' ! -name '*.d' | head -n 1)
hello='{"jsonrpc":"2.0","id":1,"method":"hello","params":{"protocol_version":"'"$protocol"'","client":{"name":"build-check","version":"0"}}}'
reply=$(printf '%s\n' "$hello" | SPECFORGE_DATA_DIR="${RUNNER_TEMP:-/tmp}/core-data" "$launcher" --serve 2> /dev/null | head -n 1)
echo "${reply:0:140}"
echo "$reply" | grep -q "\"protocol_version\":\"$protocol\""
