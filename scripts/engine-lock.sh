#!/usr/bin/env bash
# engine-lock.sh — fingerprints of what the runtime image was built from.
#
#   engine-lock.sh pins         sha256 of the pins baked into the image
#                               (okg base digest, archi commit, base user)
#   engine-lock.sh dockerfile   sha256 of docker/runtime/Dockerfile
#   engine-lock.sh check        exit 1 unless versions.lock runtime.inputs == pins   (CI, every PR)
#   engine-lock.sh stale        exit 0 when the image must be rebuilt (pins or Dockerfile moved)
#   engine-lock.sh write        record both fingerprints in versions.lock            (engine.yaml)
#
# The archi REPOSITORY is deliberately not part of `pins`: a commit sha names the same
# content whichever remote serves it. Needs yq v4 (mikefarah).
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LOCK="$REPO/versions.lock"
DOCKERFILE="$REPO/docker/runtime/Dockerfile"

pins() {
  yq -r '[.images.okg.ref, .archi.commit, .runtime.base_user] | join("\n")' "$LOCK" | sha256sum | cut -d' ' -f1
}
dockerfile() { sha256sum "$DOCKERFILE" | cut -d' ' -f1; }

case "${1:-}" in
  pins) pins ;;
  dockerfile) dockerfile ;;
  check)
    want="$(pins)"; have="$(yq -r '.runtime.inputs' "$LOCK")"
    if [[ "$want" != "$have" ]]; then
      echo "versions.lock: the pins no longer match the image in runtime.digest." >&2
      echo "  runtime.inputs = $have" >&2
      echo "  pins now       = $want" >&2
      echo "Pins are moved by the 'engine' workflow only (Actions -> engine -> Run workflow)." >&2
      exit 1
    fi
    echo "versions.lock: runtime.digest was built from the pinned okg + archi ($want)"
    ;;
  stale)
    [[ "$(pins)" != "$(yq -r '.runtime.inputs' "$LOCK")" ]] && { echo "stale: pins moved"; exit 0; }
    [[ "$(dockerfile)" != "$(yq -r '.runtime.dockerfile' "$LOCK")" ]] && { echo "stale: Dockerfile changed"; exit 0; }
    echo "fresh: image matches pins and Dockerfile"; exit 1
    ;;
  write)
    PINS="$(pins)" DF="$(dockerfile)" yq -i '.runtime.inputs = strenv(PINS) | .runtime.dockerfile = strenv(DF)' "$LOCK"
    ;;
  *) echo "usage: engine-lock.sh pins|dockerfile|check|stale|write" >&2; exit 2 ;;
esac
