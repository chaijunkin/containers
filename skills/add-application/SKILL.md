Skill: add-application
Summary:
This workspace-scoped skill documents a repeatable process to add an application to the `containers` repo and produce a runnable image or build artifact.

When to use:
- You want to add a new application under `apps/` that can be built and packaged using the repo's conventions (Dockerfile + `metadata.yaml` + optional `ci/`).

Step-by-step process:
1. Identify application source and type
   - Inputs: git URL, local path, or tarball. Example: `https://github.com/we-promise/sure`.
   - Decision: If the app already contains a `Dockerfile` or conventional packaging (Makefile, Maven, npm, go.mod, setup.py), prefer using that. Otherwise, create a minimal `Dockerfile` using the language/runtime detected.

2. Create `apps/<name>/` layout
   - Required files: `Dockerfile`, `metadata.yaml` (carry repo metadata: name, summary, channels), and `ci/` (optional, add `goss.yaml` if healthchecks used elsewhere).
   - Example `metadata.yaml` keys: `name`, `summary`, `version` (optional), `maintainers`.

3. Add build/test helpers
   - Add a small `ci/` folder with `goss.yaml` if healthchecks are needed in CI.
   - Add `entrypoint.sh` if the application needs an entrypoint wrapper.

4. Add to repository automation (manual step)
   - If the repo uses a workflow to build/publish images, update its matrix or job definitions to include the new `apps/<name>` target. This repo uses a per-image build approach — add the image name to the build matrix where appropriate.

5. Verify locally
   - Clone the application into `apps/<name>` and run: `docker build -t <name> apps/<name>` (or the language-specific build command).
   - Run healthchecks or smoke tests defined in `ci/goss.yaml`.

Decision points and branching logic:
- If upstream repo already contains a Dockerfile: vendor it into `apps/<name>/Dockerfile` and adapt entrypoint/cmd as needed.
- If upstream repo is a library (not runnable): wrap it in a small service image that demonstrates the library usage (example app or tests) and document that this is a library packaging.

Quality criteria / completion checks:
- `apps/<name>/metadata.yaml` exists and contains `name` and `summary`.
- `apps/<name>/Dockerfile` builds locally without errors.
- If `ci/goss.yaml` is present, `goss` checks pass or are documented as TODOs.
- README in `apps/<name>/README.md` explains how to build and run locally.

Examples / example prompts to call this skill:
- "Add application from https://github.com/we-promise/sure as `sure` under `apps/` and create a metadata.yaml + Dockerfile if missing." 
- "Create `apps/my-app` from a local path and add CI skeleton with `goss.yaml`."

Related customizations you may want next:
- Automate adding the app to the repo build matrix (CI workflow edits).
- Add a small wrapper generator that scaffolds `metadata.yaml`, `Dockerfile`, and `ci/goss.yaml` from templates.

Notes and conventions for this repo:
- Apps live under `apps/` with each image's `Dockerfile` and `metadata.yaml` next to each other.
- Follow existing `apps/*` examples when choosing base images and channels.
