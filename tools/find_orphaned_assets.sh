#!/usr/bin/env bash
set -uo pipefail

find static -type f | while read file; do
  grep --exclude-dir={tools,_site,.idea,.git} -rl ${file} . > /dev/null
  if [ ! $? -eq 0 ]; then
    echo "File ${file} is unused. Deleting";
    rm $file;
  fi
done
