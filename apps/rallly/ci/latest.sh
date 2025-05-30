#!/usr/bin/env bash
#version="$(curl -sX GET "https://api.github.com/repos/lukevella/rallly/releases/latest" | awk '/tag_name/{print $4;exit}' FS='[""]' | sed 's|^v||')"
version="3.11.2"
printf "%s" "${version}"
