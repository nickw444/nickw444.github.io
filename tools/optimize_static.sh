#!/usr/bin/env bash

set -euo pipefail

find . -name '*.png' | xargs optipng -o7
find . -name '*.jpg' -o -name '*.jpeg' | xargs jpegoptim  --strip-all
