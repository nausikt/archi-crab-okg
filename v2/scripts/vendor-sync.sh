#!/usr/bin/env bash
# Re-copy the upstream files v2/ mirrors from an archi checkout (at v2/versions.lock
# archi.commit). v2-engine runs it on every bump; v2-ci fails when the copies drift.
#
#   v2/scripts/vendor-sync.sh <archi checkout>
#
# What is copied (verbatim):
#   src/cli/templates/dockerfiles/base-helm-images/Dockerfile-{data-manager,postgres}-universal
#   src/cli/templates/dockerfiles/base-python-image/{Dockerfile,requirements.txt}   <- the base image's inputs
#   src/cli/templates/helm/                                                            <- archi's own chart, for diffing
# Read the diff of v2/vendor/reference after a bump: it is the upstream change, next to what
# v2/docker/Dockerfile* reproduce. Dockerfile.postgres is a verbatim copy and is refreshed too.
set -euo pipefail
A="${1:?archi checkout}"; R="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
D="$R/v2/vendor/reference"
cp "$A/src/cli/templates/dockerfiles/base-helm-images/Dockerfile-data-manager-universal" "$D/dockerfiles/"
cp "$A/src/cli/templates/dockerfiles/base-helm-images/Dockerfile-postgres-universal" "$D/dockerfiles/"
cp "$A/src/cli/templates/dockerfiles/base-python-image/Dockerfile" "$D/dockerfiles/Dockerfile-python-base"
cp "$A/src/cli/templates/dockerfiles/base-python-image/requirements.txt" "$D/dockerfiles/python-base-requirements.txt"
rm -rf "$D/helm" && mkdir -p "$D/helm" && cp -r "$A/src/cli/templates/helm/." "$D/helm/"
# Dockerfile.postgres = upstream's, with our 3-line header kept
{ sed -n '1,4p' "$R/v2/docker/Dockerfile.postgres"; sed -n '2,$p' "$A/src/cli/templates/dockerfiles/base-helm-images/Dockerfile-postgres-universal"; } > "$R/v2/docker/Dockerfile.postgres.new"
mv "$R/v2/docker/Dockerfile.postgres.new" "$R/v2/docker/Dockerfile.postgres"
git -C "$R" status --short v2/vendor v2/docker/Dockerfile.postgres
