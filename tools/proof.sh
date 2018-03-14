#!/usr/bin/env bash
set -euo pipefail

bundle exec jekyll build
bundle exec htmlproofer --empty-alt-ignore --disable-external ./_site
