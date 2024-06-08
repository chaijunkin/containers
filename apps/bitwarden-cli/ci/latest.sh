#!/usr/bin/env bash
version="$(curl -sX GET "https://api.github.com/repos/bitwarden/clients/releases" | jq --raw-output 'first(.[] |select(.tag_name | startswith("cli-"))) | .tag_name' 2>/dev/null)"
version="${version#*v}"
version="${version#*release-}"
version="${version#*cli-v}"
printf "%s" "${version}"
