FROM alpine:3.20 as bw-cli
ARG VERSION
RUN \
  apk add --no-cache \
    jq \
    curl \
    zip && \
  mkdir -p /tmp /out && \
  # # renovate: datasource=github-tags depName=bitwarden/clients type=calver
  # BW_RELEASE=cli-v2024.2.0 && \
  # BW_RELEASE=${BW_RELEASE#cli-v} && \
  curl -o \
    /tmp/bw.zip -L \
      "https://github.com/bitwarden/clients/releases/download/cli-v${VERSION}/bw-oss-linux-${VERSION}.zip" && \
  unzip -q /tmp/bw.zip -d /out

FROM ghcr.io/roxedus/debian:rolling
COPY --from=bw-cli /out /usr/sbin/

USER kubeguy
COPY ./apps/bw/entrypoint.sh /entrypoint.sh
COPY ./apps/bw/healthcheck.sh /healthcheck.sh

CMD ["/entrypoint.sh"]
