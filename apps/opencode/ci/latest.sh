#!/usr/bin/env bash
version=$(curl -s "https://registry.npmjs.org/@opencode/cli" | jq -r '."dist-tags".latest')
printf "%s" "${version}"
