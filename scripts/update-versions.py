#!/usr/bin/env python3
import re
import os
import sys
import subprocess
import json
from urllib.request import urlopen, Request

# Mapping of ARG variable names to GitHub repositories
# Format: { "ARG_NAME": "owner/repo" }
TOOL_MAPPING = {
    "KUBECTX_VERSION": "ahmetb/kubectx",
    "K9S_VERSION": "derailed/k9s",
    "HELM_VERSION": "helm/helm",
    "STERN_VERSION": "stern/stern",
    "KUSTOMIZE_VERSION": "kubernetes-sigs/kustomize",
    "FLUX_VERSION": "fluxcd/flux2",
    "ARGOCD_VERSION": "argoproj/argo-cd",
    "TALOS_VERSION": "siderolabs/talos",
    "CILIUM_CLI_VERSION": "cilium/cilium-cli",
    "HUBBLE_VERSION": "cilium/hubble",
    "SOPS_VERSION": "getsops/sops",
    "AGE_VERSION": "FiloSottile/age",
    "CNPG_VERSION": "cloudnative-pg/cloudnative-pg",
    "KYVERNO_VERSION": "kyverno/kyverno",
    "TETRA_VERSION": "cilium/tetragon",
    "HELMFILE_VERSION": "helmfile/helmfile",
    "LOGCLI_VERSION": "grafana/loki",
    "TEMPO_CLI_VERSION": "grafana/tempo",
    "RESTIC_VERSION": "restic/restic",
    "RCLONE_VERSION": "rclone/rclone",
    "KOPIA_VERSION": "kopia/kopia",
    "TALHELPER_VERSION": "budimanjojo/talhelper",
    "MINIJINJA_VERSION": "mitsuhiko/minijinja",
    "CTOP_VERSION": "bcicen/ctop",
    "CALICOCTL_VERSION": "projectcalico/calico",
    "TERMSHARK_VERSION": "gcla/termshark",
    "GRPCURL_VERSION": "fullstorydev/grpcurl",
    "FORTIO_VERSION": "fortio/fortio",
    # linux-utility specific
    "PROMETHEUS_VERSION": "prometheus/prometheus",
    "PINT_VERSION": "cloudflare/pint",
    "GRAFANA_VERSION": "grafana/grafana",
    "TRIVY_VERSION": "aquasecurity/trivy",
    "COSIGN_VERSION": "sigstore/cosign",
    "TERRAFORM_VERSION": "hashicorp/terraform",
    "VAULT_VERSION": "hashicorp/vault",
    "CRANE_VERSION": "google/go-containerregistry",
    "VELERO_VERSION": "vmware-tanzu/velero",
    "TASK_VERSION": "go-task/task",
    "KUBECONFORM_VERSION": "yannh/kubeconform",
}

def get_latest_github_release(repo):
    """Fetch the latest release tag from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        req = Request(url)
        # Use GITHUB_TOKEN if available in environment
        token = os.environ.get('GITHUB_TOKEN')
        if token:
            req.add_header('Authorization', f'token {token}')
        # Adding a basic User-Agent to avoid issues with GitHub's API
        req.add_header('User-Agent', 'Update-Versions-Script')
        with urlopen(req) as response:
            data = json.loads(response.read().decode())
            tag = data['tag_name']
            # Remove 'v' prefix if present
            if tag.startswith('v'):
                tag = tag[1:]
            # Special case for kustomize (tags are often kustomize/vX.Y.Z)
            if 'kustomize' in repo and '/' in tag:
                tag = tag.split('/')[-1]
                if tag.startswith('v'): tag = tag[1:]
            return tag
    except Exception as e:
        print(f"Error fetching {repo}: {e}")
        return None

def update_dockerfile(file_path, dry_run=False):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Processing {file_path}...")
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    changes = 0
    for line in lines:
        match = re.match(r'ARG\s+([A-Z0-9_]+_VERSION)=([^\s]+)', line)
        if match:
            var_name, current_version = match.groups()
            if var_name in TOOL_MAPPING:
                repo = TOOL_MAPPING[var_name]
                latest_version = get_latest_github_release(repo)
                if latest_version and latest_version != current_version:
                    print(f"  Updating {var_name}: {current_version} -> {latest_version}")
                    new_lines.append(f"ARG {var_name}={latest_version}\n")
                    changes += 1
                    continue
        new_lines.append(line)

    if changes > 0 and not dry_run:
        with open(file_path, 'w') as f:
            f.writelines(new_lines)
        print(f"Successfully updated {changes} versions in {file_path}")
    elif dry_run:
        print(f"Dry run: {changes} changes would be made to {file_path}")
    else:
        print(f"No changes needed for {file_path}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Update tool versions in Dockerfiles')
    parser.add_argument('files', nargs='*', help='Dockerfiles to update (defaults to all in apps/)')
    parser.add_argument('--dry-run', action='store_true', help='Do not write changes to files')
    args = parser.parse_args()

    files = args.files
    if not files:
        # Scan apps/ for Dockerfiles
        for root, dirs, filenames in os.walk('apps'):
            for filename in filenames:
                if filename == 'Dockerfile':
                    files.append(os.path.join(root, filename))

    for file_path in files:
        update_dockerfile(file_path, dry_run=args.dry_run)

if __name__ == '__main__':
    main()
