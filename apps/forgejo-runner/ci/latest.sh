#!/usr/bin/env bash
# forgejo-runner doesn't track a single upstream version
# Instead, we'll use a date-based versioning scheme
printf "%s" "$(date +%Y.%m.%d)"
