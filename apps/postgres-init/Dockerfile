FROM ghcr.io/chaijunkin/alpine:rolling@sha256:ab06f9be57d17f5c96711c7750529b9a45ce6f6b083938044b779254f97ba08e

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

#hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates postgresql16-client~"${VERSION}"

USER sauser

COPY ./apps/postgres-init/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/postgres/postgres"
