ARG VERSION

FROM docker.io/library/debian:${VERSION}

ARG DEBIAN_FRONTEND="noninteractive"
ENV \
  LANG en_US.UTF-8 \
  DEBCONF_NONINTERACTIVE_SEEN=true \
  UMASK="0002" \
  TZ="Etc/UTC"

# https://github.com/linuxserver/docker-baseimage-debian/blob/b53571add9f420b356330035d8ab1539d8ab0187/Dockerfile#L70-L101
RUN \
  echo "**** Ripped from Ubuntu Docker Logic ****" && \
  echo '#!/bin/sh' \
    > /usr/sbin/policy-rc.d && \
  echo 'exit 101' \
    >> /usr/sbin/policy-rc.d && \
  chmod +x \
    /usr/sbin/policy-rc.d && \
  dpkg-divert --local --rename --add /sbin/initctl && \
  cp -a \
    /usr/sbin/policy-rc.d \
    /sbin/initctl && \
  sed -i \
    's/^exit.*/exit 0/' \
    /sbin/initctl && \
  echo 'force-unsafe-io' \
    > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup && \
  echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' \
    > /etc/apt/apt.conf.d/docker-clean && \
  echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' \
    >> /etc/apt/apt.conf.d/docker-clean && \
  echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' \
    >> /etc/apt/apt.conf.d/docker-clean && \
  echo 'Acquire::Languages "none";' \
    > /etc/apt/apt.conf.d/docker-no-languages && \
  echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' \
    > /etc/apt/apt.conf.d/docker-gzip-indexes && \
  echo 'Apt::AutoRemove::SuggestsImportant "false";' \
    > /etc/apt/apt.conf.d/docker-autoremove-suggests && \
  mkdir -p /run/systemd && \
  echo 'docker' \
    > /run/systemd/container

WORKDIR /app

RUN \
  adduser kubeguy \
    --uid 769 \
    --group \
    --system \
    --disabled-password \
    --no-create-home && \
  mkdir -p /config && \
  chown -R kubeguy:kubeguy /config /app && \
  chmod -R 775 /config

RUN \
  echo "**** install apt-utils and locales ****" && \
  apt-get update && \
  apt-get install -y \
    apt-utils \
    locales && \
  echo "**** install packages ****" && \
  apt-get install -y \
    bash \
    ca-certificates \
    catatonit \
    curl \
    iputils-ping \
    jq \
    netcat-traditional \
    tzdata


ENTRYPOINT [ "/usr/bin/catatonit", "--" ]
