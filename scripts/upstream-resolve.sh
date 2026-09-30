#!/usr/bin/env bash
# upstream-resolve.sh — move versions.lock to the newest upstream the two followed refs offer.
# It only resolves: nothing is built, nothing is pushed.
#
#   okg    the image tag  <upstream.image>:<upstream.track>  (okg publishes `dev` and
#          `sha-<commit>` for the tip of dev after every merge). The commit is READ FROM THE
#          IMAGE (label org.opencontainers.image.revision), and accepted only when BOTH the
#          runtime and the postgres image exist for it: the pair is what upstream tested.
#   archi  git ls-remote <archi.repository> refs/heads/<archi.branch>
#
# Usage  scripts/upstream-resolve.sh [--dry-run]
# Env    OKG_COMMIT / ARCHI_COMMIT   hold one side at a full 40-char sha instead of the newest
#        CONTAINER_RUNTIME           default docker; must be logged in to ghcr.io (read:packages)
# Out    versions.lock updated (not with --dry-run); key=value lines on stdout and, when set,
#        appended to $GITHUB_OUTPUT: changed, okg_from, okg_to, archi_from, archi_to
# Needs  yq v4 (mikefarah), jq, git, docker buildx.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LOCK="$REPO/versions.lock"
RT="${CONTAINER_RUNTIME:-docker}"
DRY=0; [[ "${1:-}" == --dry-run ]] && DRY=1
die() { echo "upstream-resolve: $*" >&2; exit 1; }
lock() { yq -r "$1" "$LOCK"; }
is_sha() { [[ "$1" =~ ^[0-9a-f]{40}$ ]]; }

okg_image="$(lock '.upstream.image')"
pg_image="$(lock '.upstream.postgres_image')"
track="$(lock '.upstream.track')"
archi_repo="$(lock '.archi.repository')"
archi_branch="$(lock '.archi.branch')"
old_okg="$(lock '.upstream.commit')"
old_archi="$(lock '.archi.commit')"
for v in okg_image pg_image track archi_repo archi_branch; do
  [[ -n "${!v}" && "${!v}" != null ]] || die "versions.lock is missing the key behind \$$v"
done

# The manifest of a reference: .digest is what a pull by that tag resolves to.
manifest() { "$RT" buildx imagetools inspect "$1" --format '{{json .Manifest}}' 2>/dev/null; }
index_digest() {
  local d; d="$(manifest "$1" | jq -r '.digest // empty')" || return 1
  [[ "$d" =~ ^sha256:[0-9a-f]{64}$ ]] || return 1
  echo "$d"
}
# The image config of the linux/amd64 member (the platform the cluster and CI run).
amd64_config() {
  local name="$1" tag="$2" m d
  m="$(manifest "$name:$tag")" || return 1
  d="$(jq -r '[.manifests[]? | select(.platform.os == "linux" and .platform.architecture == "amd64") | .digest][0] // empty' <<<"$m")"
  [[ -n "$d" ]] || d="$(jq -r '.digest // empty' <<<"$m")" # a single-platform image
  [[ -n "$d" ]] || return 1
  "$RT" buildx imagetools inspect "$name@$d" --format '{{json .Image}}' 2>/dev/null
}
revision_of() { amd64_config "$1" "$2" | jq -r '.config.Labels["org.opencontainers.image.revision"] // empty'; }

# ---- okg: candidate commits, newest first -------------------------------------------------
candidates=()
if [[ -n "${OKG_COMMIT:-}" ]]; then
  is_sha "$OKG_COMMIT" || die "OKG_COMMIT must be a full 40-char sha"
  candidates=("$OKG_COMMIT")
else
  c1="$(revision_of "$okg_image" "$track" || true)"
  [[ -n "$c1" ]] || die "cannot read $okg_image:$track — is $RT logged in to ghcr.io with read:packages, and does the tag exist?"
  candidates=("$c1")
  # Runtime and postgres are published by separate jobs; when one lags, its tag still
  # points at the previous commit. That commit is the newest COMPLETE pair.
  c2="$(revision_of "$pg_image" "$track" || true)"
  [[ -n "$c2" && "$c2" != "$c1" ]] && candidates+=("$c2")
fi

new_okg=""; okg_digest=""; pg_digest=""
for c in "${candidates[@]}"; do
  is_sha "$c" || { echo "skip: '$c' is not a commit sha" >&2; continue; }
  od="$(index_digest "$okg_image:sha-$c")" || { echo "skip $c: no $okg_image:sha-$c" >&2; continue; }
  pd="$(index_digest "$pg_image:sha-$c")" || { echo "skip $c: no $pg_image:sha-$c" >&2; continue; }
  new_okg="$c"; okg_digest="$od"; pg_digest="$pd"; break
done
[[ -n "$new_okg" ]] || die "no okg commit has both a runtime and a postgres image (tried: ${candidates[*]}). Upstream is mid-publish; the next run will pick it up."

base_user="$(amd64_config "$okg_image" "sha-$new_okg" | jq -r '.config.User // empty')"
[[ "$base_user" =~ ^[0-9]+(:[0-9]+)?$ ]] || base_user="$(lock '.runtime.base_user')"

# ---- archi ---------------------------------------------------------------------------------
if [[ -n "${ARCHI_COMMIT:-}" ]]; then
  new_archi="$ARCHI_COMMIT"
else
  new_archi="$(git ls-remote "$archi_repo" "refs/heads/$archi_branch" | cut -f1)"
fi
is_sha "$new_archi" || die "cannot resolve $archi_repo refs/heads/$archi_branch (got '${new_archi}')"

# ---- report, write -------------------------------------------------------------------------
changed=false
[[ "$new_okg" != "$old_okg" || "$new_archi" != "$old_archi" ]] && changed=true
[[ "$okg_image@$okg_digest" != "$(lock '.images.okg.ref')" ]] && changed=true
report() {
  echo "changed=$changed"
  echo "okg_from=$old_okg"
  echo "okg_to=$new_okg"
  echo "archi_from=$old_archi"
  echo "archi_to=$new_archi"
}
report
[[ -n "${GITHUB_OUTPUT:-}" ]] && report >>"$GITHUB_OUTPUT"
echo "okg    $old_okg -> $new_okg  ($okg_image@$okg_digest)" >&2
echo "pg     $pg_image@$pg_digest" >&2
echo "archi  $old_archi -> $new_archi  ($archi_repo $archi_branch)" >&2

if ((DRY)); then echo "dry run: versions.lock not written" >&2; exit 0; fi
NEW_OKG="$new_okg" OKG_REF="$okg_image@$okg_digest" PG_REF="$pg_image@$pg_digest" \
  NEW_ARCHI="$new_archi" BASE_USER="$base_user" yq -i '
    .upstream.commit = strenv(NEW_OKG)
  | .images.okg.ref = strenv(OKG_REF)
  | .images["okg-postgres"].ref = strenv(PG_REF)
  | .archi.commit = strenv(NEW_ARCHI)
  | .runtime.base_user = strenv(BASE_USER)' "$LOCK"
