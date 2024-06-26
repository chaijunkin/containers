FROM ghcr.io/chaijunkin/alpine:rolling@sha256:358e4ce4453fe54bb1dc3be8ec37fbd7b1be96c74fe37fa3c6e7224a816987be

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_BREAK_SYSTEM_PACKAGES=1 \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN \
    curl -fsSL -o /tmp/app.zip "https://github.com/morpheus65535/bazarr/releases/download/v${VERSION}/bazarr.zip" \
    && unzip -q /tmp/app.zip -d /app \
    && chown -R root:root /app \
    && chmod -R 755 /app \
    && rm -rf /tmp/*

#hadolint ignore=DL3018,DL3013
RUN \
    apk add --no-cache ca-certificates ffmpeg mediainfo python3 py3-lxml py3-numpy py3-gevent py3-cryptography py3-setuptools py3-psycopg2 py3-pillow unzip \
    && \
    apk add --no-cache --virtual .build-deps py3-pip gcc python3-dev musl-dev \
    && \
    pip install --upgrade pip \
    && \
    pip install --upgrade \
      "webrtcvad-wheels>=2.0.10" \
    && apk del --purge .build-deps \
    && rm -rf \
        /root/.cache \
        /root/.cargo \
        /tmp/*

# Install unrar
COPY --from=ghcr.io/linuxserver/unrar:7.0.7 /usr/bin/unrar-alpine /usr/bin/unrar

USER sauser
COPY ./apps/bazarr/entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/morpheus65535/bazarr"
