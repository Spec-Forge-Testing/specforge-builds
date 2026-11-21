#!/usr/bin/env bash
# Fails if any binary of the core needs a glibc newer than the given floor.
set -euo pipefail
core_dir="$1"
floor="$2"

needed=$(find "$core_dir" -type f \( -name '*.so*' -o -name 'python-core-*' \) -print0 |
    xargs -0 objdump -T 2> /dev/null | grep -oE 'GLIBC_[0-9]+\.[0-9]+' | sort -uV | tail -n 1)
needed="${needed#GLIBC_}"
echo "glibc needed: $needed (floor $floor)"
[ "$(printf '%s\n%s\n' "$needed" "$floor" | sort -V | tail -n 1)" = "$floor" ]
