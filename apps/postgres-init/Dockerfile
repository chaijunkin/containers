FROM ghcr.io/chaijunkin/alpine:rolling@sha256:762afa2739ea8b4808788400b2a5e0f3320934f8c5e1caf4f38c614fd0f0dd09

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

#hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates postgresql16-client~"${VERSION}"

USER sauser

COPY ./apps/postgres-init/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/postgres/postgres"
