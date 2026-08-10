FROM alpine:3.24

# Install essential debugging and networking tools
RUN apk add --no-cache \
    bash zsh vim nano \
    curl wget bind-tools net-tools iputils nmap tcpdump socat netcat-openbsd \
    jq yq git \
    openssl ca-certificates unzip tar gzip htop strace file \
    busybox-extras

# Set default shell to bash
CMD ["/bin/bash"]
