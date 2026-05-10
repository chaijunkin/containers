#!/usr/bin/env bash
# linux-utility doesn't track a single upstream version
# Instead, we'll use a date-based versioning scheme
printf "%s" "$(date +%Y.%m.%d)"
