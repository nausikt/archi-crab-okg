#!/usr/bin/env bash
# vendor-sync.sh — keep deployments/archi-crab's vendored vocabulary in step with the
# pinned runtime image, per deployments/archi-crab/VENDOR.yaml.
#
#   IMG=<ref@digest> scripts/vendor-sync.sh --check    # exit 1 + diff on drift (CI)
#   IMG=<ref@digest> scripts/vendor-sync.sh --apply    # overwrite verbatim entries
#
# IMG defaults to versions.lock runtime.ref@runtime.digest. CONTAINER_RUNTIME
# defaults to podman (docker on GitHub runners). Needs yq v4.
set -euo pipefail
MODE="${1:?usage: vendor-sync.sh --check|--apply}"
RT="${CONTAINER_RUNTIME:-podman}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEP="$REPO/deployments/archi-crab"; MAN="$DEP/VENDOR.yaml"
IMG="${IMG:-$(yq -r '.runtime.ref + "@" + .runtime.digest' "$REPO/versions.lock")}"
[[ "$IMG" == *null* || -z "$IMG" ]] && { echo "no runtime digest in versions.lock; pass IMG=" >&2; exit 2; }

SCRATCH="$(mktemp -d)"; CID=""
cleanup() { rm -rf "$SCRATCH"; [[ -n "$CID" ]] && "$RT" rm -f "$CID" >/dev/null 2>&1 || true; }
trap cleanup EXIT
CID="$("$RT" create --entrypoint true "$IMG")"

# Bootstrap window: until the engine-bump PR lands, envs/staging still pins the
# upstream okg image, which has no /opt/archi. Archi-sourced entries are then
# SKIPPED LOUDLY (never silently); okg-sourced entries are still checked.
# --apply refuses to run in this state (it would half-sync the vocabulary).
HAS_ARCHI=1
"$RT" cp "$CID:/opt/archi/bundles" "$SCRATCH/.probe" >/dev/null 2>&1 || HAS_ARCHI=0
rm -rf "$SCRATCH/.probe"
if (( ! HAS_ARCHI )); then
  [[ "$MODE" == --apply ]] && { echo "refusing --apply: $IMG has no /opt/archi (use the derived image)" >&2; exit 2; }
  echo "::warning::$IMG has no /opt/archi (pre engine-bump). Archi entries skipped; okg entries checked."
fi

n="$(yq '.entries | length' "$MAN")"; drift=0; skipped=0
for ((i=0; i<n; i++)); do
  dest="$(yq -r ".entries[$i].dest" "$MAN")"
  src="$(yq -r ".entries[$i].src" "$MAN")"
  type="$(yq -r ".entries[$i].type" "$MAN")"
  # root: repo -> dest is relative to the repo root (reference copies under vendor/),
  # default -> relative to deployments/archi-crab. optional: true -> --check only
  # warns while the dest does not exist yet (the first --apply creates it).
  base="$DEP"; [[ "$(yq -r ".entries[$i].root // \"deployment\"" "$MAN")" == repo ]] && base="$REPO"
  # --apply rm -rf's "$base/$dest": refuse anything that could reach outside it,
  # and keep repo-rooted entries inside vendor/.
  case "$dest" in ""|.|./*|/*|*..*) echo "VENDOR.yaml entry $i: refusing dest '$dest'" >&2; exit 2 ;; esac
  [[ "$base" == "$REPO" && "$dest" != vendor/?* ]] && { echo "VENDOR.yaml entry $i: root: repo dest must be under vendor/ (got '$dest')" >&2; exit 2; }
  if (( ! HAS_ARCHI )) && [[ "$src" == /opt/archi/* ]]; then
    echo "skip   $dest  (archi entry; no archi in pinned engine)"; skipped=$((skipped+1)); continue
  fi
  if [[ "$MODE" == --check && "$(yq -r ".entries[$i].optional // false" "$MAN")" == true && ! -e "$base/$dest" ]]; then
    echo "::warning::new    $dest  (optional, not vendored yet: run --apply to create it)"; continue
  fi
  out="$SCRATCH/e$i"
  if [[ "$type" == dir ]]; then
    # -h dereferences: the cern-team bundle ships skills/ as symlinks into the
    # archi repo, and `cp` from a container refuses to copy a dangling link.
    mkdir -p "$out"
    "$RT" run --rm --entrypoint tar "$IMG" -ch -C "$src" . | tar -x -C "$out"
  else "$RT" cp "$CID:$src" "$out"; fi
  if ! diff -ruN --exclude='.gitkeep' "$base/$dest" "$out" >"$SCRATCH/.diff.$i" 2>&1; then
    drift=1; echo "DRIFT  $dest  <-  $src"
    [[ "$MODE" == --check ]] && sed 's/^/    /' "$SCRATCH/.diff.$i" | head -200
  else echo "ok     $dest"; fi
done

case "$MODE" in
  --check) (( drift )) && { echo "vendored files drift from $IMG — run: IMG=$IMG scripts/vendor-sync.sh --apply" >&2; exit 1; }
           echo "vendor in sync with $IMG$( (( skipped )) && echo " ($skipped archi entries skipped)")" ;;
  --apply) for ((i=0; i<n; i++)); do
             dest="$(yq -r ".entries[$i].dest" "$MAN")"
             base="$DEP"; [[ "$(yq -r ".entries[$i].root // \"deployment\"" "$MAN")" == repo ]] && base="$REPO"
             rm -rf "$base/$dest"; mkdir -p "$(dirname "$base/$dest")"; cp -R "$SCRATCH/e$i" "$base/$dest"
           done
           echo "applied from $IMG. untouched (ours): $(yq -r '.ours[]' "$MAN" | tr '\n' ' ')" ;;
  *) echo "unknown mode $MODE" >&2; exit 2 ;;
esac
