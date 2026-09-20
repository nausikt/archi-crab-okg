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

LABEL org.opencontainers.image.source="https://github.com/nausikt/archi-crab-okg" \
      org.opencontainers.image.description="okg runtime + archi (cern-team bundle) for archi-crab" \
      io.archi-crab.archi.ref="${ARCHI_REF}"

# Restore the base image's user (read it with: podman inspect $BASE | jq -r '.[0].Config.User')
USER ${BASE_USER}
