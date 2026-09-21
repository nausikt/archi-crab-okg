#!/usr/bin/env bash
# gen-cern-team.sh — FIRST SCAFFOLD ONLY (once per instance lifetime, on your
# laptop, on the engine-bump PR branch). Archi/okg bumps afterwards flow through
# scripts/vendor-sync.sh, never through re-scaffolding.
#
# The installer materialises the bundle's schemas/, bridges/, skills/ and
# invariants itself (profile `schemas:` slot). This script then runs
# vendor-sync --apply to assert those files are byte-identical to VENDOR.yaml's
# sources and to add the okg codebase-index pieces the bundle does not carry.
#
# Usage:  IMG=ghcr.io/nausikt/archi-crab-okg@sha256:... OKG_DSN=postgresql://... scripts/gen-cern-team.sh
set -euo pipefail
: "${IMG:?set IMG to the derived image (ref@digest) from the engine-bump PR}"
: "${OKG_DSN:?set OKG_DSN to a SCRATCH database (the installer provisions+migrates it)}"
RT="${CONTAINER_RUNTIME:-podman}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"; DEP="$REPO/deployments/archi-crab"

if [ -d "$DEP" ]; then
  echo ">> $DEP exists -> $DEP.prev (cherry-pick source; delete when merged)"
  rm -rf "$DEP.prev"; mv "$DEP" "$DEP.prev"
fi
mkdir -p "$REPO/.okg-data/data" "$REPO/.okg-data/repos"

echo "== 1/3 scaffold with the cern-team bundle installer (--no-publish: stop before first load)"
"$RT" run --rm --network host -v "$REPO:$REPO" -w "$REPO" \
  -e OKG_DSN -e OKG_DEPLOYMENTS_DIR="$REPO/deployments" -e OKG_PROFILES_DIR=/opt/archi/bundles \
  -e ARCHI_DATA_ROOT="$REPO/.okg-data" -e OKG_ENVIRONMENT_DATA_ROOT="$REPO/.okg-data" \
  --entrypoint okg "$IMG" install --profile cern-team --deployment-name archi-crab \
  --postgres-dsn '${OKG_DSN}' --non-interactive --no-publish
test -f "$DEP/deployment.yaml" || { echo "scaffold produced no $DEP/deployment.yaml" >&2; exit 1; }
echo "   installer wrote:"; find "$DEP" -type f | sed "s|$DEP/|     |" | sort

echo "== 2/3 restore our manifest + invariants, then vendor-sync --apply"
cp "$DEP.prev/VENDOR.yaml" "$DEP/VENDOR.yaml"
cp "$DEP.prev/invariants.yaml" "$DEP/invariants.yaml"      # ours: overrides the bundle's floor
IMG="$IMG" CONTAINER_RUNTIME="$RT" "$REPO/scripts/vendor-sync.sh" --apply

echo "== 3/3 MANUAL EDITS (Runbook v0.7.1 B.2–B.4) — then claim -> load -> lint -> ingest -> smoke"
cat <<'TXT'
  B.2 registry: keep cmssw_releases; DROP connectors needing a cache file or SSO
      cookie (docsite, twiki*, jira, indico) and github_repo/gitlab_repo (superseded).
  B.3 code graph (from deployments/archi-crab.prev): code_repos{crabserver,crabclient} (NO
      git-history), the seven code modules appended to modules, consistency.dangling_edges: prune
  B.4 deployment.yaml: runtime.enabled true · chat.enabled false · search subtypes
      [document_chunk, source_file, code_symbol, cmssw_release] · nomos owner.contact
  Verify VENDOR.yaml's skills `dest` matches where the installer put skill-triggers.yaml.
TXT
