#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/we-promise/sure"
DEST_DIR="apps/sure"

echo "Cloning $REPO_URL -> $DEST_DIR"
mkdir -p apps
if [ -d "$DEST_DIR" ]; then
  echo "Destination $DEST_DIR already exists; pulling latest"
  (cd "$DEST_DIR" && git pull --ff-only) || true
else
  git clone "$REPO_URL" "$DEST_DIR"
fi

cd "$DEST_DIR"
echo "Repository contents:"
ls -la

# detect common build systems and attempt a build
if [ -f package.json ]; then
  echo "Detected Node.js project (package.json). Installing and building if a build script exists."
  npm install --no-audit --no-fund
  if npm run | grep -q "build"; then
    npm run build
  else
    echo "No npm build script defined; skipping build step."
  fi
elif [ -f pom.xml ]; then
  echo "Detected Maven project (pom.xml). Building with maven."
  mvn -q -DskipTests package
elif [ -f go.mod ]; then
  echo "Detected Go project (go.mod). Building binaries."
  go build ./...
elif [ -f pyproject.toml ] || [ -f setup.py ]; then
  echo "Detected Python project. Installing requirements if present."
  if [ -f requirements.txt ]; then
    python3 -m pip install -r requirements.txt
  fi
  echo "No uniform Python build step defined; check project README."
elif [ -f Makefile ]; then
  echo "Detected Makefile. Running 'make build' if available."
  if make -n build >/dev/null 2>&1; then
    make build
  else
    echo "No 'build' target in Makefile; skipping."
  fi
elif [ -f Dockerfile ]; then
  echo "Detected Dockerfile. Building image 'sure:local'."
  docker build -t sure:local . || echo "Docker build failed or Docker not available."
else
  echo "No known build system detected. Inspect the repository and add a build step manually."
fi

echo "Done."
