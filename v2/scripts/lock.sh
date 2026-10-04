#!/usr/bin/env bash
# v2/versions.lock helper: fingerprints of what each image is built from, and the writes the
# workflows make. Same idea as scripts/engine-lock.sh for the okg engine.
#
#   lock.sh base-inputs        sha256 of Dockerfile.base + the vendored base requirements + our extras
#   lock.sh base-stale         exit 0 when the base image must be rebuilt (inputs moved, or no digest)
#   lock.sh base-ref           ghcr.io/…/archi-v2-python-base@sha256:… (fails when unpinned)
#   lock.sh images-inputs      sha256 of Dockerfile(s) + v2/mcp + the scripts the image carries
#                              + archi.commit + base.digest + the baked embedding model
#   lock.sh images-stale       exit 0 when the three images must be rebuilt
#   lock.sh hf-model           the model to bake (from v2/deployments/archi-crab/config.yaml; empty = none)
#   lock.sh set-base DIGEST    write base.digest + base.inputs
#   lock.sh set-images DM MCP PG   write images.*.digest, images.inputs, images.built_from
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOCK="$REPO/v2/versions.lock"
cd "$REPO"

sha() { sha256sum | cut -c1-64; }

base_inputs() {
  cat v2/docker/Dockerfile.base v2/vendor/reference/dockerfiles/python-base-requirements.txt v2/docker/base-requirements.extra.txt | sha
}

hf_model() {
  # mikefarah yq v4 (the runner's): no if/then/else in its lexer -- select() prints nothing
  # when the embedding is not a HuggingFace one, which is the empty answer we want
  yq -r 'select(.data_manager.embedding_name == "HuggingFaceEmbeddings")
         | .data_manager.embedding_class_map.HuggingFaceEmbeddings.kwargs.model_name // ""' \
    v2/deployments/archi-crab/config.yaml
}

images_inputs() {
  {
    cat v2/docker/Dockerfile v2/docker/Dockerfile.postgres v2/mcp/requirements.txt v2/mcp/server.py \
        v2/scripts/contract-check.py v2/scripts/smoke.py
    yq -r '.archi.commit' "$LOCK"
    yq -r '.base.digest' "$LOCK"
    hf_model
  } | sha
}

case "${1:-}" in
  base-inputs)  base_inputs ;;
  images-inputs) images_inputs ;;
  hf-model)     hf_model ;;
  base-stale)
    d="$(yq -r '.base.digest' "$LOCK")"; i="$(yq -r '.base.inputs' "$LOCK")"
    [ -z "$d" ] || [ "$d" = null ] || [ "$i" != "$(base_inputs)" ] ;;
  images-stale)
    i="$(yq -r '.images.inputs' "$LOCK")"
    for k in data-manager mcp postgres; do
      d="$(yq -r ".images[\"$k\"].digest" "$LOCK")"; { [ -z "$d" ] || [ "$d" = null ]; } && exit 0
    done
    [ "$i" != "$(images_inputs)" ] ;;
  base-ref)
    d="$(yq -r '.base.digest' "$LOCK")"
    { [ -z "$d" ] || [ "$d" = null ]; } && { echo "v2/versions.lock: base.digest is empty -- build the base first (v2-build)" >&2; exit 1; }
    echo "$(yq -r '.base.ref' "$LOCK")@$d" ;;
  set-base)
    [[ "${2:-}" =~ ^sha256:[0-9a-f]{64}$ ]] || { echo "set-base: need sha256:…" >&2; exit 1; }
    D="$2" I="$(base_inputs)" yq -i '.base.digest = strenv(D) | .base.inputs = strenv(I)' "$LOCK" ;;
  set-images)
    for d in "${2:-}" "${3:-}" "${4:-}"; do [[ "$d" =~ ^sha256:[0-9a-f]{64}$ ]] || { echo "set-images: need three sha256:… digests" >&2; exit 1; }; done
    DM="$2" MCP="$3" PG="$4" I="$(images_inputs)" B="$(git rev-parse HEAD)" \
      yq -i '.images["data-manager"].digest = strenv(DM) | .images.mcp.digest = strenv(MCP) | .images.postgres.digest = strenv(PG)
             | .images.inputs = strenv(I) | .images.built_from = strenv(B)' "$LOCK" ;;
  *) sed -n '2,13p' "$0"; exit 2 ;;
esac
