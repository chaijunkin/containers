FROM ghcr.io/chaijunkin/alpine:rolling@sha256:d00fa1676653cbf4a9cad55be6695a7db6416f8e81a6ceafe979aa15427fb0ea

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

#hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates postgresql16-client~"${VERSION}"

USER sauser

COPY ./apps/postgres-init/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/postgres/postgres"
