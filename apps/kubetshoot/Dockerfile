FROM debian:stable-slim AS fetcher

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    bzip2 \
    tar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

# Versions (May 2026)
ARG KUBECTL_VERSION=1.36.0
ARG KUBECTX_VERSION=0.10.0
ARG K9S_VERSION=0.40.0
ARG HELM_VERSION=4.1.4
ARG STERN_VERSION=1.32.0
ARG KUSTOMIZE_VERSION=5.6.0
ARG FLUX_VERSION=2.4.0
ARG ARGOCD_VERSION=3.4.1
ARG TALOS_VERSION=1.13.0
ARG CILIUM_CLI_VERSION=0.19.2
ARG HUBBLE_VERSION=1.19.3
ARG SOPS_VERSION=3.13.0
ARG AGE_VERSION=1.2.1
ARG CNPG_VERSION=1.29.0
ARG KYVERNO_VERSION=1.14.0
ARG TETRA_VERSION=0.2.0
ARG CLOUDFLARED_VERSION=2026.5.1
ARG HELMFILE_VERSION=0.165.0
ARG LOGCLI_VERSION=3.2.0
ARG TEMPO_CLI_VERSION=2.7.0
ARG RESTIC_VERSION=0.18.0
ARG RCLONE_VERSION=1.74.1
ARG KOPIA_VERSION=0.19.0
ARG TALHELPER_VERSION=3.2.0
ARG MINIJINJA_VERSION=2.5.0
ARG CTOP_VERSION=0.7.7
ARG CALICOCTL_VERSION=3.32.0
ARG TERMSHARK_VERSION=2.4.0
ARG GRPCURL_VERSION=1.9.3
ARG FORTIO_VERSION=1.75.1

# # # Fetch binaries
RUN (curl -fsSLO "https://dl.k8s.io/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl" && chmod +x kubectl) || touch kubectl
RUN (curl -fsSLO https://github.com/ahmetb/kubectx/releases/download/v${KUBECTX_VERSION}/kubectx && chmod +x kubectx) || touch kubectx
RUN (curl -fsSLO https://github.com/ahmetb/kubectx/releases/download/v${KUBECTX_VERSION}/kubens && chmod +x kubens) || touch kubens
RUN (curl -fsSLO https://github.com/derailed/k9s/releases/download/v${K9S_VERSION}/k9s_Linux_amd64.tar.gz && tar -xzf k9s_Linux_amd64.tar.gz) || touch k9s
RUN (curl -fsSLO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && tar -xzf helm-v${HELM_VERSION}-linux-amd64.tar.gz && mv linux-amd64/helm .) || touch helm
RUN (curl -fsSLO https://github.com/stern/stern/releases/download/v${STERN_VERSION}/stern_${STERN_VERSION}_linux_amd64.tar.gz && tar -xzf stern_${STERN_VERSION}_linux_amd64.tar.gz) || touch stern
RUN (curl -fsSLO https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz && tar -xzf kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz) || touch kustomize
RUN (curl -fsSLO https://github.com/fluxcd/flux2/releases/download/v${FLUX_VERSION}/flux_${FLUX_VERSION}_linux_amd64.tar.gz && tar -xzf flux_${FLUX_VERSION}_linux_amd64.tar.gz) || touch flux
RUN (curl -fsSLO https://github.com/argoproj/argo-cd/releases/download/v${ARGOCD_VERSION}/argocd-linux-amd64 && chmod +x argocd-linux-amd64 && mv argocd-linux-amd64 argocd) || touch argocd
RUN (curl -fsSLO https://github.com/siderolabs/talos/releases/download/v${TALOS_VERSION}/talosctl-linux-amd64 && chmod +x talosctl-linux-amd64 && mv talosctl-linux-amd64 talosctl) || touch talosctl
RUN (curl -fsSLO https://github.com/cilium/cilium-cli/releases/download/v${CILIUM_CLI_VERSION}/cilium-linux-amd64.tar.gz && tar -xzf cilium-linux-amd64.tar.gz) || touch cilium
RUN (curl -fsSLO https://github.com/cilium/hubble/releases/download/v${HUBBLE_VERSION}/hubble-linux-amd64.tar.gz && tar -xzf hubble-linux-amd64.tar.gz) || touch hubble
RUN (curl -fsSLO https://github.com/getsops/sops/releases/download/v${SOPS_VERSION}/sops-v${SOPS_VERSION}.linux.amd64 && chmod +x sops-v${SOPS_VERSION}.linux.amd64 && mv sops-v${SOPS_VERSION}.linux.amd64 sops) || touch sops
RUN (curl -fsSLO https://github.com/FiloSottile/age/releases/download/v${AGE_VERSION}/age-v${AGE_VERSION}-linux-amd64.tar.gz && tar -xzf age-v${AGE_VERSION}-linux-amd64.tar.gz --strip-components=1 && rm -f LICENSE) || touch age age-keygen
RUN (curl -fsSLO https://github.com/cloudnative-pg/cloudnative-pg/releases/download/v${CNPG_VERSION}/kubectl-cnpg_${CNPG_VERSION}_linux_x86_64.tar.gz && tar -xzf kubectl-cnpg_${CNPG_VERSION}_linux_x86_64.tar.gz) || touch kubectl-cnpg
RUN (curl -fsSLO https://github.com/kyverno/kyverno/releases/download/v${KYVERNO_VERSION}/kyverno-cli_v${KYVERNO_VERSION}_linux_x86_64.tar.gz && tar -xzf kyverno-cli_v${KYVERNO_VERSION}_linux_x86_64.tar.gz && mv kyverno .) || touch kyverno
RUN (curl -fsSLO https://github.com/cilium/tetragon/releases/download/v${TETRA_VERSION}/tetra-linux-amd64.tar.gz && tar -xzf tetra-linux-amd64.tar.gz) || touch tetra
RUN (curl -fsSLO https://github.com/cloudflare/cloudflared/releases/download/${CLOUDFLARED_VERSION}/cloudflared-linux-amd64 && chmod +x cloudflared-linux-amd64 && mv cloudflared-linux-amd64 cloudflared) || touch cloudflared
RUN (curl -fsSLO https://github.com/helmfile/helmfile/releases/download/v${HELMFILE_VERSION}/helmfile_${HELMFILE_VERSION}_linux_amd64.tar.gz && tar -xzf helmfile_${HELMFILE_VERSION}_linux_amd64.tar.gz) || touch helmfile
RUN (curl -fsSLO https://github.com/grafana/loki/releases/download/v${LOGCLI_VERSION}/logcli-linux-amd64.zip && unzip logcli-linux-amd64.zip && mv logcli-linux-amd64 logcli) || touch logcli
RUN (curl -fsSLO https://github.com/grafana/tempo/releases/download/v${TEMPO_CLI_VERSION}/tempo-cli_${TEMPO_CLI_VERSION}_linux_amd64.tar.gz && tar -xzf tempo-cli_${TEMPO_CLI_VERSION}_linux_amd64.tar.gz) || touch tempo-cli
RUN (curl -fsSLO https://github.com/restic/restic/releases/download/v${RESTIC_VERSION}/restic_${RESTIC_VERSION}_linux_amd64.bz2 && \
    bunzip2 restic_${RESTIC_VERSION}_linux_amd64.bz2 && chmod +x restic_${RESTIC_VERSION}_linux_amd64 && mv restic_${RESTIC_VERSION}_linux_amd64 restic) || touch restic
RUN (curl -fsSLO https://github.com/rclone/rclone/releases/download/v${RCLONE_VERSION}/rclone-v${RCLONE_VERSION}-linux-amd64.zip && \
    unzip rclone-v${RCLONE_VERSION}-linux-amd64.zip && mv rclone-v${RCLONE_VERSION}-linux-amd64/rclone .) || touch rclone
RUN (curl -fsSLO https://github.com/kopia/kopia/releases/download/v${KOPIA_VERSION}/kopia-${KOPIA_VERSION}-linux-x64.tar.gz && \
    tar -xzf kopia-${KOPIA_VERSION}-linux-x64.tar.gz && mv kopia-${KOPIA_VERSION}-linux-x64/kopia .) || touch kopia
RUN (curl -fsSLO https://github.com/budimanjojo/talhelper/releases/download/v${TALHELPER_VERSION}/talhelper_linux_amd64.tar.gz && tar -xzf talhelper_linux_amd64.tar.gz) || touch talhelper
RUN (curl -fsSLO https://github.com/mitsuhiko/minijinja/releases/download/${MINIJINJA_VERSION}/minijinja-cli-x86_64-unknown-linux-musl.tar.gz && \
    tar -xzf minijinja-cli-x86_64-unknown-linux-musl.tar.gz && mv minijinja-cli minijinja) || touch minijinja
RUN (curl -fsSLO https://github.com/bcicen/ctop/releases/download/v${CTOP_VERSION}/ctop-${CTOP_VERSION}-linux-amd64 && chmod +x ctop-${CTOP_VERSION}-linux-amd64 && mv ctop-${CTOP_VERSION}-linux-amd64 ctop) || touch ctop
RUN (curl -fsSLO https://github.com/projectcalico/calico/releases/download/v${CALICOCTL_VERSION}/calicoctl-linux-amd64 && chmod +x calicoctl-linux-amd64 && mv calicoctl-linux-amd64 calicoctl) || touch calicoctl
RUN (curl -fsSLO https://github.com/gcla/termshark/releases/download/v${TERMSHARK_VERSION}/termshark_${TERMSHARK_VERSION}_linux_amd64.tar.gz && tar -xzf termshark_${TERMSHARK_VERSION}_linux_amd64.tar.gz && mv termshark_${TERMSHARK_VERSION}_linux_amd64/termshark .) || touch termshark
RUN (curl -fsSLO https://github.com/fullstorydev/grpcurl/releases/download/v${GRPCURL_VERSION}/grpcurl_${GRPCURL_VERSION}_linux_x86_64.tar.gz && tar -xzf grpcurl_${GRPCURL_VERSION}_linux_x86_64.tar.gz) || touch grpcurl
RUN (curl -fsSLO https://github.com/fortio/fortio/releases/download/v${FORTIO_VERSION}/fortio-linux_amd64-${FORTIO_VERSION}.tgz && tar -xzf fortio-linux_amd64-${FORTIO_VERSION}.tgz && mv usr/bin/fortio .) || touch fortio

# --- Stage 2: Final ---
FROM alpine:3.23

# Install base packages and netshoot-style tools
RUN set -ex \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk upgrade \
    && apk add --no-cache \
    apache2-utils \
    bash \
    bind-tools \
    bird \
    bridge-utils \
    busybox-extras \
    conntrack-tools \
    curl \
    dhcping \
    drill \
    ethtool \
    file \
    fping \
    iftop \
    iperf \
    iperf3 \
    iproute2 \
    ipset \
    iptables \
    iptraf-ng \
    iputils \
    ipvsadm \
    httpie \
    jq \
    libc6-compat \
    liboping \
    ltrace \
    mtr \
    net-snmp-tools \
    netcat-openbsd \
    nftables \
    ngrep \
    nmap \
    nmap-nping \
    nmap-scripts \
    openssl \
    py3-pip \
    py3-setuptools \
    scapy \
    socat \
    speedtest-cli \
    openssh \
    strace \
    tcpdump \
    tcptraceroute \
    trippy \
    tshark \
    util-linux \
    vim \
    git \
    zsh \
    websocat \
    swaks \
    perl-crypt-ssleay \
    perl-net-ssleay \
    ca-certificates \
    unzip \
    tar \
    gzip

# Setting User and Home
USER root
WORKDIR /root
ENV HOSTNAME=kubetshoot

# Install Oh My Zsh and themes
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended \
    && git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions \
    && git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Copy binaries from fetcher
COPY --from=fetcher /tmp/kubectl /usr/local/bin/kubectl
COPY --from=fetcher /tmp/kubectx /usr/local/bin/kubectx
COPY --from=fetcher /tmp/kubens /usr/local/bin/kubens
COPY --from=fetcher /tmp/k9s /usr/local/bin/k9s
COPY --from=fetcher /tmp/helm /usr/local/bin/helm
COPY --from=fetcher /tmp/stern /usr/local/bin/stern
COPY --from=fetcher /tmp/kustomize /usr/local/bin/kustomize
COPY --from=fetcher /tmp/flux /usr/local/bin/flux
COPY --from=fetcher /tmp/argocd /usr/local/bin/argocd
COPY --from=fetcher /tmp/talosctl /usr/local/bin/talosctl
COPY --from=fetcher /tmp/cilium /usr/local/bin/cilium
COPY --from=fetcher /tmp/hubble /usr/local/bin/hubble
COPY --from=fetcher /tmp/sops /usr/local/bin/sops
COPY --from=fetcher /tmp/age /usr/local/bin/age
COPY --from=fetcher /tmp/age-keygen /usr/local/bin/age-keygen
COPY --from=fetcher /tmp/kubectl-cnpg /usr/local/bin/kubectl-cnpg
COPY --from=fetcher /tmp/kyverno /usr/local/bin/kyverno
COPY --from=fetcher /tmp/tetra /usr/local/bin/tetra
COPY --from=fetcher /tmp/cloudflared /usr/local/bin/cloudflared
COPY --from=fetcher /tmp/helmfile /usr/local/bin/helmfile
COPY --from=fetcher /tmp/logcli /usr/local/bin/logcli
COPY --from=fetcher /tmp/tempo-cli /usr/local/bin/tempo-cli
COPY --from=fetcher /tmp/restic /usr/local/bin/restic
COPY --from=fetcher /tmp/rclone /usr/local/bin/rclone
COPY --from=fetcher /tmp/kopia /usr/local/bin/kopia
COPY --from=fetcher /tmp/talhelper /usr/local/bin/talhelper
COPY --from=fetcher /tmp/minijinja /usr/local/bin/minijinja
COPY --from=fetcher /tmp/ctop /usr/local/bin/ctop
COPY --from=fetcher /tmp/calicoctl /usr/local/bin/calicoctl
COPY --from=fetcher /tmp/termshark /usr/local/bin/termshark
COPY --from=fetcher /tmp/grpcurl /usr/local/bin/grpcurl
COPY --from=fetcher /tmp/fortio /usr/local/bin/fortio

# Custom ZSHRC
RUN echo 'export ZSH=$HOME/.oh-my-zsh' > .zshrc \
    && echo 'ZSH_THEME="powerlevel10k/powerlevel10k"' >> .zshrc \
    && echo 'ZSH_DISABLE_COMPFIX="true"' >> .zshrc \
    && echo 'plugins=(git zsh-autosuggestions sudo docker kubectl)' >> .zshrc \
    && echo 'source $ZSH/oh-my-zsh.sh' >> .zshrc \
    && echo 'cat /etc/motd' >> .zshrc

# Custom MOTD
RUN echo "                     dP            dP                           dP   " > /etc/motd \
    && echo "                     88            88                           88   " >> /etc/motd \
    && echo " 88d888b. .d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. d8888P " >> /etc/motd \
    && echo " 88'  \`88 88ooood8   88   Y8ooooo. 88'  \`88 88'  \`88 88'  \`88   88   " >> /etc/motd \
    && echo " 88    88 88.  ...   88         88 88    88 88.  .88 88.  .88   88   " >> /etc/motd \
    && echo " dP    dP \`88888P'   dP   \`88888P' dP    dP \`88888P' \`88888P'   dP   " >> /etc/motd \
    && echo "" >> /etc/motd \
    && echo "Welcome to Kubetshoot! (Netshoot + Kubernetes)" >> /etc/motd \
    && echo "Version: 2026.05" >> /etc/motd

# Fix permissions for OpenShift and tshark
RUN chmod -R g=u /root \
    && chown root:root /usr/bin/dumpcap

# Ensure everything is executable
RUN chmod +x /usr/local/bin/*

# Set default shell to zsh
CMD ["zsh"]
