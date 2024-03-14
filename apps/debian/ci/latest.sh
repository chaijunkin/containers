#!/usr/bin/env bash
channel=bookworm-slim
version=$(curl -s "https://registry.hub.docker.com/v2/repositories/library/debian/tags?ordering=name&name=$channel" | jq --raw-output --arg s "$channel" '.results[] | select(.name | contains($s)) | .name + "@" + .digest' 2>/dev/null | head -n1)
version="${version#*v}"
version="${version#*release-}"
version="${version%_*}"
printf "%s" "${version}"
