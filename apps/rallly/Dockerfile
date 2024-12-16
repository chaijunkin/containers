FROM ghcr.io/roxedus/debian:rolling AS base

ARG VERSION

RUN \
  echo "**** install runtime dependencies ****" && \
  apt-get update && \
  apt-get install -y \
    git \
    curl \
    gpg && \
  echo "**** install node dependencies ****" && \
  curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor | tee /usr/share/keyrings/nodesource.gpg >/dev/null && \
  echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" > /etc/apt/sources.list.d/nodesource.list && \
  curl -fsSL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /usr/share/keyrings/yarnsource.gpg >/dev/null && \
  echo 'deb [signed-by=/usr/share/keyrings/yarnsource.gpg] https://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install -y \
    nodejs \
    yarn

FROM base AS builder
RUN \
  if [ -z ${RALLLY_RELEASE+x} ]; then \
    RALLLY_RELEASE=$(curl -sX GET https://api.github.com/repos/lukevella/rallly/releases/latest \
      | awk '/tag_name/{print $4;exit}' FS='[""]' | sed 's|^v||'); \
  fi && \
  mkdir -p \
    /app/rallly && \
  curl -o \
    /tmp/rallly.tar.gz -L \
    "https://github.com/lukevella/rallly/archive/refs/tags/v${RALLLY_RELEASE}.tar.gz" && \
  tar xf /tmp/rallly.tar.gz -C \
    /app/rallly --strip-components=1 && \
  cd /app/rallly && \
  yarn global add turbo && \
  turbo prune --scope=@rallly/web --docker && \
  cd /app/rallly/out && \
  yarn --network-timeout 1000000 && \
  mv /app/rallly/out/full /app/rallly && \
  yarn db:generate && \
  export NEXT_PUBLIC_APP_VERSION=$RALLLY_RELEASE && \
  export NEXT_PUBLIC_SELF_HOSTED=true && \
  SKIP_ENV_VALIDATION=1 yarn build

FROM base

RUN \
  apt-get install -y --no-install-recommends \
    openssl \
    zlib1g \
    libgcc-s1 && \
  mkdir -p /app/rallly && \
  yarn global add prisma && \
  rm -rf \
    /tmp/* \
    $HOME/.cache \
    /var/lib/apt/lists/* \
    /var/tmp/*

USER kubeguy

COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/packages/database/prisma /app/rallly/prisma

COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/apps/web/next.config.js /app/rallly
COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/apps/web/package.json /app/rallly

COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/apps/web/.next/standalone /app/rallly
COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/apps/web/.next/static /app/rallly/apps/web/.next/static
COPY --from=builder --chown=kubeguy:kubeguy /app/rallly/apps/web/public /app/rallly/apps/web/public

COPY ./apps/rallly/entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
