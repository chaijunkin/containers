FROM ghcr.io/chaijunkin/alpine:rolling@sha256:9503c97d0c8851e28e451973387a544f849c3d3b4a18d9822f64a02d19a598c8

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

#hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates postgresql16-client~"${VERSION}"

USER sauser

COPY ./apps/postgres-init/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/postgres/postgres"
