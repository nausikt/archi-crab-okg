# syntax=docker/dockerfile:1
# archi-crab runtime = upstream okg image + archi. Nothing else.
#
# This is the ONE build this repo admits. okg is already correct in the base
# (their provenance, their pins); we add the archi package and its checkout so
# the cern-team bundle, connectors and schema slices exist in-image.
#
# Every ARG comes from versions.lock via .github/workflows/engine.yaml. The image
# is PRIVATE for as long as the base is (it contains upstream's private code).
#
# ORDER MATTERS FOR SECURITY. Step 1 is the only one that sees the okg token, and
# it runs BEFORE any archi code is installed: `pip install` executes archi's build
# backend as root, and a step that ran after it could be handed a tampered `git`.
# Step 1 runs git only; nothing from okg or archi is imported while the token exists.

ARG BASE_IMAGE=ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
FROM ${BASE_IMAGE}

ARG ARCHI_REPO=https://github.com/archi-physics/archi-okg
ARG ARCHI_REF
ARG OKG_REPO=https://github.com/mitdbg/okg
ARG OKG_BRANCH=dev
ARG BASE_USER
USER root

# ---------------------------------------------------------------------------
# 1. Framework release authority for an EXTERNAL deployment repo (repositorySync).
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
# The token is a BuildKit secret: one RUN, no layer, no build-arg, no env.
# safe.directory: the runtime uid (10001 in-cluster, the runner uid in CI) never
# owns /opt/okg; without it git refuses ("dubious ownership") and discovery fails.
# ---------------------------------------------------------------------------
RUN --mount=type=secret,id=okg_pat set -eux; \
    test -n "$OKG_CODE_REVISION"; \
    command -v git >/dev/null || { apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*; }; \
    git config --system safe.directory '*'; \
    cd /opt/okg; git init -q; \
    git remote add origin "${OKG_REPO}.git"; \
    set +x; \
    printf 'https://x-access-token:%s@github.com\n' "$(cat /run/secrets/okg_pat)" > /tmp/.gitcred; \
    set -x; \
    git config --system credential.helper 'store --file=/tmp/.gitcred'; \
    git fetch -q --depth 1 origin "$OKG_CODE_REVISION" \
      || git fetch -q --depth 500 origin "$OKG_BRANCH"; \
    git config --system --unset credential.helper; rm -f /tmp/.gitcred; \
    git reset -q --hard "$OKG_CODE_REVISION"; \
    test "$(git rev-parse HEAD)" = "$OKG_CODE_REVISION"; \
    test -z "$(git status --porcelain)"; \
    echo "framework authority: $(git rev-parse --short HEAD)"

# ---------------------------------------------------------------------------
# 1b. The venv's okg IS this checkout. Since okg dev 3d6cb3e8 the CLI refuses to start
# from inside a source checkout whose code is not what is installed ("bare okg is not
# running this checkout's code": the chart's containers start in /opt/okg, the image's
# working directory). An editable install of the checkout into the base image's venv
# makes the installed package the checkout itself: same commit, one copy of the code.
# --no-deps: the base image already resolved okg's dependencies; nothing else moves.
# ---------------------------------------------------------------------------
RUN set -eux; \
    PY=/opt/okg/.venv/bin/python; test -x "$PY"; \
    if command -v uv >/dev/null; then uv pip install --python "$PY" --no-cache --no-deps --editable /opt/okg; \
    else "$PY" -m pip install --no-cache-dir --no-deps --editable /opt/okg; fi; \
    "$PY" -c "import okg, pathlib; p = pathlib.Path(okg.__file__).resolve(); \
assert str(p).startswith('/opt/okg/') and '/.venv/' not in str(p), p; print('okg runs from', p)"; \
    cd /opt/okg && okg --help > /dev/null && echo "okg starts from its checkout"

# ---------------------------------------------------------------------------
# 2. archi, at one exact commit. PUBLIC: plain https, no secret. NEVER
# `pip install archi` (an unrelated PyPI package squats the name). Keep the
# checkout: the bundle lives in /opt/archi/bundles and vendor-sync.sh reads it.
# ---------------------------------------------------------------------------
RUN set -eux; \
    test -n "$ARCHI_REF"; \
    git init -q /opt/archi; \
    git -C /opt/archi remote add origin "$ARCHI_REPO"; \
    git -C /opt/archi fetch -q --depth 1 origin "$ARCHI_REF"; \
    git -C /opt/archi checkout -q FETCH_HEAD; \
    test "$(git -C /opt/archi rev-parse HEAD)" = "$ARCHI_REF"; \
    PY="$(command -v python)"; \
    if command -v uv >/dev/null; then uv pip install --python "$PY" --no-cache /opt/archi/python; \
    elif "$PY" -m pip --version >/dev/null 2>&1; then "$PY" -m pip install --no-cache-dir /opt/archi/python; \
    else "$PY" -m ensurepip --upgrade && "$PY" -m pip install --no-cache-dir /opt/archi/python; fi; \
    "$PY" -c "import archi, okg; print('archi+okg import ok')"

ENV OKG_PROFILES_DIR=/opt/archi/bundles \
    ARCHI_CODE_REVISION=${ARCHI_REF}

LABEL org.opencontainers.image.source="https://github.com/nausikt/archi-crab-okg" \
      org.opencontainers.image.description="okg runtime + archi (cern-team bundle) for archi-crab" \
      io.archi-crab.archi.repository="${ARCHI_REPO}" \
      io.archi-crab.archi.ref="${ARCHI_REF}"

# Restore the base image's user (versions.lock runtime.base_user, read from the base's config)
USER ${BASE_USER}
