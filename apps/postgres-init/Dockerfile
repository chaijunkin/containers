FROM ghcr.io/chaijunkin/alpine:rolling@sha256:358e4ce4453fe54bb1dc3be8ec37fbd7b1be96c74fe37fa3c6e7224a816987be

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

#hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates postgresql16-client~"${VERSION}"

USER sauser

COPY ./apps/postgres-init/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/postgres/postgres"
