FROM alpine:3.23

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
RUN (curl -fsSL "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o kubectl && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/) || echo "Failed to download kubectl"

# Install promtool (downloading prometheus and extracting promtool)
ARG PROMETHEUS_VERSION=2.51.0
RUN (curl -fsSLO https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz && \
    tar -xzf prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz && \
    mv prometheus-${PROMETHEUS_VERSION}.linux-amd64/promtool /usr/local/bin/ && \
    rm -rf prometheus-${PROMETHEUS_VERSION}.linux-amd64 prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz) || echo "Failed to download prometheus"

# Install pint
ARG PINT_VERSION=0.52.0
RUN (curl -fsSLO https://github.com/cloudflare/pint/releases/download/v${PINT_VERSION}/pint-${PINT_VERSION}-linux-amd64.tar.gz && \
    tar -xzf pint-${PINT_VERSION}-linux-amd64.tar.gz && \
    mv pint-linux-amd64 /usr/local/bin/pint && \
    rm pint-${PINT_VERSION}-linux-amd64.tar.gz) || echo "Failed to download pint"

# Install grafana-cli
ARG GRAFANA_VERSION=13.0.1
RUN (curl -fsSLO https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    tar -xzf grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz && \
    mv grafana-${GRAFANA_VERSION}/bin/grafana-cli /usr/local/bin/ && \
    rm -rf grafana-${GRAFANA_VERSION} grafana-${GRAFANA_VERSION}.linux-amd64.tar.gz) || echo "Failed to download grafana"

# Install Helm
ARG HELM_VERSION=3.14.3
RUN (curl -fsSLO https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    tar -xzf helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    rm -rf linux-amd64 helm-v${HELM_VERSION}-linux-amd64.tar.gz) || echo "Failed to download helm"

# Install k9s
ARG K9S_VERSION=0.32.4
RUN (curl -fsSLO https://github.com/derailed/k9s/releases/download/v${K9S_VERSION}/k9s_Linux_amd64.tar.gz && \
    tar -xzf k9s_Linux_amd64.tar.gz && \
    mv k9s /usr/local/bin/ && \
    rm k9s_Linux_amd64.tar.gz) || echo "Failed to download k9s"

# Install stern (multi-pod log tailing)
ARG STERN_VERSION=1.28.0
RUN (curl -fsSLO https://github.com/stern/stern/releases/download/v${STERN_VERSION}/stern_${STERN_VERSION}_linux_amd64.tar.gz && \
    tar -xzf stern_${STERN_VERSION}_linux_amd64.tar.gz && \
    mv stern /usr/local/bin/ && \
    rm stern_${STERN_VERSION}_linux_amd64.tar.gz) || echo "Failed to download stern"

# Install kustomize
ARG KUSTOMIZE_VERSION=5.3.0
RUN (curl -fsSLO https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz && \
    tar -xzf kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz && \
    mv kustomize /usr/local/bin/ && \
    rm kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz) || echo "Failed to download kustomize"

# Install ArgoCD CLI
ARG ARGOCD_VERSION=2.10.4
RUN (curl -fsSLO https://github.com/argoproj/argo-cd/releases/download/v${ARGOCD_VERSION}/argocd-linux-amd64 && \
    chmod +x argocd-linux-amd64 && \
    mv argocd-linux-amd64 /usr/local/bin/argocd) || echo "Failed to download argocd"

# Install Flux CLI
ARG FLUX_VERSION=2.2.3
RUN (curl -fsSLO https://github.com/fluxcd/flux2/releases/download/v${FLUX_VERSION}/flux_${FLUX_VERSION}_linux_amd64.tar.gz && \
    tar -xzf flux_${FLUX_VERSION}_linux_amd64.tar.gz && \
    mv flux /usr/local/bin/ && \
    rm flux_${FLUX_VERSION}_linux_amd64.tar.gz) || echo "Failed to download flux"

# Install Trivy (security scanner)
ARG TRIVY_VERSION=0.69.3
RUN (curl -fsSLO https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz && \
    tar -xzf trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz && \
    mv trivy /usr/local/bin/ && \
    rm trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz) || echo "Failed to download trivy"

# Install cosign (container signing)
ARG COSIGN_VERSION=2.2.3
RUN (curl -fsSLO https://github.com/sigstore/cosign/releases/download/v${COSIGN_VERSION}/cosign-linux-amd64 && \
    chmod +x cosign-linux-amd64 && \
    mv cosign-linux-amd64 /usr/local/bin/cosign) || echo "Failed to download cosign"

# Install Terraform
ARG TERRAFORM_VERSION=1.7.5
RUN (curl -fsSLO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip) || echo "Failed to download terraform"

# Install Vault CLI
ARG VAULT_VERSION=1.16.1
RUN (curl -fsSLO https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip && \
    unzip vault_${VAULT_VERSION}_linux_amd64.zip && \
    mv vault /usr/local/bin/ && \
    rm vault_${VAULT_VERSION}_linux_amd64.zip) || echo "Failed to download vault"

# Install crane (container registry tool)
ARG CRANE_VERSION=0.19.1
RUN (curl -fsSLO https://github.com/google/go-containerregistry/releases/download/v${CRANE_VERSION}/go-containerregistry_Linux_x86_64.tar.gz && \
    tar -xzf go-containerregistry_Linux_x86_64.tar.gz && \
    mv crane /usr/local/bin/ && \
    mv gcrane /usr/local/bin/ && \
    rm go-containerregistry_Linux_x86_64.tar.gz) || echo "Failed to download crane"

# Install kubectx and kubens
ARG KUBECTX_VERSION=0.9.5
RUN (curl -fsSLO https://github.com/ahmetb/kubectx/releases/download/v${KUBECTX_VERSION}/kubectx && \
    curl -fsSLO https://github.com/ahmetb/kubectx/releases/download/v${KUBECTX_VERSION}/kubens && \
    chmod +x kubectx kubens && \
    mv kubectx /usr/local/bin/ && \
    mv kubens /usr/local/bin/) || echo "Failed to download kubectx"

# Install velero
ARG VELERO_VERSION=1.13.1
RUN (curl -fsSLO https://github.com/vmware-tanzu/velero/releases/download/v${VELERO_VERSION}/velero-v${VELERO_VERSION}-linux-amd64.tar.gz && \
    tar -xzf velero-v${VELERO_VERSION}-linux-amd64.tar.gz && \
    mv velero-v${VELERO_VERSION}-linux-amd64/velero /usr/local/bin/ && \
    rm -rf velero-v${VELERO_VERSION}-linux-amd64 velero-v${VELERO_VERSION}-linux-amd64.tar.gz) || echo "Failed to download velero"

# Install SOPS (secret management)
ARG SOPS_VERSION=3.8.1
RUN (curl -fsSLO https://github.com/getsops/sops/releases/download/v${SOPS_VERSION}/sops-v${SOPS_VERSION}.linux.amd64 && \
    chmod +x sops-v${SOPS_VERSION}.linux.amd64 && \
    mv sops-v${SOPS_VERSION}.linux.amd64 /usr/local/bin/sops) || echo "Failed to download sops"

# Install age (encryption tool for SOPS)
ARG AGE_VERSION=1.1.1
RUN (curl -fsSLO https://github.com/FiloSottile/age/releases/download/v${AGE_VERSION}/age-v${AGE_VERSION}-linux-amd64.tar.gz && \
    tar -xzf age-v${AGE_VERSION}-linux-amd64.tar.gz && \
    mv age/age /usr/local/bin/ && \
    mv age/age-keygen /usr/local/bin/ && \
    rm -rf age age-v${AGE_VERSION}-linux-amd64.tar.gz) || echo "Failed to download age"

# Install task (taskfile/go-task)
ARG TASK_VERSION=3.35.1
RUN (curl -fsSLO https://github.com/go-task/task/releases/download/v${TASK_VERSION}/task_linux_amd64.tar.gz && \
    tar -xzf task_linux_amd64.tar.gz && \
    mv task /usr/local/bin/ && \
    rm task_linux_amd64.tar.gz) || echo "Failed to download task"

# Install kubeconform (Kubernetes manifest validation)
ARG KUBECONFORM_VERSION=0.6.4
RUN (curl -fsSLO https://github.com/yannh/kubeconform/releases/download/v${KUBECONFORM_VERSION}/kubeconform-linux-amd64.tar.gz && \
    tar -xzf kubeconform-linux-amd64.tar.gz && \
    mv kubeconform /usr/local/bin/ && \
    rm kubeconform-linux-amd64.tar.gz) || echo "Failed to download kubeconform"

# Install cilium CLI
ARG CILIUM_CLI_VERSION=0.19.2
RUN (curl -fsSLO https://github.com/cilium/cilium-cli/releases/download/v${CILIUM_CLI_VERSION}/cilium-linux-amd64.tar.gz && \
    tar -xzf cilium-linux-amd64.tar.gz && \
    mv cilium /usr/local/bin/ && \
    rm cilium-linux-amd64.tar.gz) || echo "Failed to download cilium"

# Install hubble CLI (for Cilium)
ARG HUBBLE_VERSION=0.13.2
RUN (curl -fsSLO https://github.com/cilium/hubble/releases/download/v${HUBBLE_VERSION}/hubble-linux-amd64.tar.gz && \
    tar -xzf hubble-linux-amd64.tar.gz && \
    mv hubble /usr/local/bin/ && \
    rm hubble-linux-amd64.tar.gz) || echo "Failed to download hubble"

# Install talosctl (Talos Linux CLI)
ARG TALOS_VERSION=1.6.7
RUN (curl -fsSLO https://github.com/siderolabs/talos/releases/download/v${TALOS_VERSION}/talosctl-linux-amd64 && \
    chmod +x talosctl-linux-amd64 && \
    mv talosctl-linux-amd64 /usr/local/bin/talosctl) || echo "Failed to download talosctl"

# Set default shell to bash
CMD ["/bin/bash"]
