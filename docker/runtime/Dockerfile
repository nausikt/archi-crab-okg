# syntax=docker/dockerfile:1
# archi-crab runtime = upstream okg image + archi. Nothing else.
#
# This is the ONE build this repo admits. okg is already correct in the base
# (their provenance, their pins); we add the archi package and its checkout so
# the cern-team bundle generator, connectors and schema slices exist in-image.
#
# Base digest and ARCHI_REF come from versions.lock via build.yaml. The image
# is PRIVATE for as long as the base is (it contains upstream's private image).

ARG BASE_IMAGE=ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
FROM ${BASE_IMAGE}

ARG ARCHI_REF
ARG BASE_USER
USER root

# archi is PUBLIC: plain https clone, no secret. NEVER `pip install archi`
# (an unrelated PyPI package squats the name). Keep the checkout: the bundle
# generator reads /opt/archi/bundles and the schema slices live in
# /opt/archi/python/archi/schemas.
RUN set -eux; \
    test -n "$ARCHI_REF"; \
    command -v git >/dev/null || { apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*; }; \
    git clone https://github.com/archi-physics/archi /opt/archi; \
    git -C /opt/archi checkout "$ARCHI_REF"; \
    PY="$(command -v python)"; \
    if command -v uv >/dev/null; then uv pip install --python "$PY" --no-cache /opt/archi/python; \
    elif "$PY" -m pip --version >/dev/null 2>&1; then "$PY" -m pip install --no-cache-dir /opt/archi/python; \
    else "$PY" -m ensurepip --upgrade && "$PY" -m pip install --no-cache-dir /opt/archi/python; fi; \
    "$PY" -c "import archi, okg; print('archi+okg ok')"

ENV OKG_PROFILES_DIR=/opt/archi/bundles

# ---------------------------------------------------------------------------
# Framework release authority for an EXTERNAL deployment repo (repositorySync).
#
# okg's publish resolves its own ("framework") git revision by walking up from
# its module path (deployment_upgrade.py: discover_framework_repository). The
# upstream image drops .git (.dockerignore) and only works when the deployment
# lives INSIDE /opt/okg/deployments (kubernetes-smoke). Ours is an external
# checkout, so discovery fails and publish is refused.
#
# Fix: give /opt/okg its real .git at EXACTLY the baked revision, so
# `git rev-parse HEAD` == OKG_CODE_REVISION (the identity gate stays truthful).
# `reset --hard` makes the tree byte-identical to the commit (clean status).
# The PAT is a BuildKit secret: one RUN, no layer, no build-arg, no env.
# safe.directory: the runtime uid (10001 in-cluster, the runner uid in CI) never
# owns /opt/okg; without it git refuses ("dubious ownership") and discovery fails.
# ---------------------------------------------------------------------------
RUN --mount=type=secret,id=okg_pat set -eux; \
    test -n "$OKG_CODE_REVISION"; \
    git config --system safe.directory '*'; \
    cd /opt/okg; git init -q; \
    git remote add origin https://github.com/mitdbg/okg.git; \
    set +x; \
    printf 'https://x-access-token:%s@github.com\n' "$(cat /run/secrets/okg_pat)" > /tmp/.gitcred; \
    set -x; \
    git config --system credential.helper 'store --file=/tmp/.gitcred'; \
    git fetch -q --depth 1 origin "$OKG_CODE_REVISION" \
      || { git fetch -q --depth 50 origin main && git checkout -q "$OKG_CODE_REVISION"; }; \
    git config --system --unset credential.helper; rm -f /tmp/.gitcred; \
    git reset -q --hard FETCH_HEAD; \
    test "$(git rev-parse HEAD)" = "$OKG_CODE_REVISION"; \
    test -z "$(git status --porcelain)"; \
    python -c "import okg" ; \
    echo "framework authority: $(git rev-parse --short HEAD)"

LABEL org.opencontainers.image.source="https://github.com/nausikt/archi-crab-okg" \
      org.opencontainers.image.description="okg runtime + archi (cern-team bundle) for archi-crab" \
      io.archi-crab.archi.ref="${ARCHI_REF}"

# Restore the base image's user (read it with: podman inspect $BASE | jq -r '.[0].Config.User')
USER ${BASE_USER}
