FROM alpine:3.19

# Install base packages
RUN apk add --no-cache \
    bash zsh vim nano \
    curl wget bind-tools net-tools iputils nmap tcpdump socat netcat-openbsd \
    jq yq git \
    openssl ca-certificates unzip tar gzip htop strace file \
    postgresql-client mysql-client redis \
    busybox-extras \
    python3 py3-pip \
    go

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

# Install promtool (downloading prometheus and extracting promtool)
ARG PROMETHEUS_VERSION=2.51.0
RUN curl -LO https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz && \
    tar -xzf prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz && \
    mv prometheus-${PROMETHEUS_VERSION}.linux-amd64/promtool /usr/local/bin/ && \
    rm -rf prometheus-${PROMETHEUS_VERSION}.linux-amd64 prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz

# Install pint
ARG PINT_VERSION=0.52.0
RUN curl -LO https://github.com/cloudflare/pint/releases/download/v${PINT_VERSION}/pint-${PINT_VERSION}-linux-amd64.tar.gz && \
    tar -xzf pint-${PINT_VERSION}-linux-amd64.tar.gz && \
    mv pint-linux-amd64 /usr/local/bin/pint && \
    rm pint-${PINT_VERSION}-linux-amd64.tar.gz

# Install grafana-cli
# grafana-cli is typically bundled with Grafana. We can try to grab just the binary if possible, 
# but it often depends on other files. 
# A better approach for a utility container might be to install the grafana package if available or just the binary.
# Alpine has a grafana package, but it's the full server.
# Let's try downloading the tarball and extracting bin/grafana-cli.
ARG GRAFANA_VERSION=10.4.1
RUN curl -LO https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    tar -xzf grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    mv grafana-v${GRAFANA_VERSION}/bin/grafana-cli /usr/local/bin/ && \
    # grafana-cli might need some libs or paths, but let's try this minimal approach first.
    rm -rf grafana-v${GRAFANA_VERSION} grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz

# Set default shell to bash
CMD ["/bin/bash"]
