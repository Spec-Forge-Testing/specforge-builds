#!/usr/bin/env bash
# Unpacks the CLI archive found in a folder and checks the unpacked CLI starts the core it carries.
set -euo pipefail
archive_dir="$1"
unpack_dir="$2"
UNZIP_WARNING=1 # unzip's exit code when it unpacked everything but had something to say

archive=$(find "$archive_dir" -maxdepth 1 -type f -name 'specforge-v*' -print -quit)
[ -n "$archive" ] || { echo "no CLI archive in $archive_dir" >&2; exit 1; }
rm -rf "$unpack_dir"
mkdir -p "$unpack_dir"
case "$archive" in
    *.zip) unzip -q "$archive" -d "$unpack_dir" || [ "$?" -eq "$UNZIP_WARNING" ] ;;
    *.tar.xz) tar -xJf "$archive" -C "$unpack_dir" ;;
    *) echo "unrecognized CLI archive: $archive" >&2; exit 1 ;;
esac

cli="$unpack_dir/specforge/specforge"
[ -f "$cli" ] || cli="$cli.exe"
[ -d "$unpack_dir/specforge/core/_internal" ] || { echo "the archive holds no core" >&2; exit 1; }
(cd "$unpack_dir" && "$cli" describe --json-output > /dev/null)
echo "$(basename "$archive"): the unpacked CLI started its core"
