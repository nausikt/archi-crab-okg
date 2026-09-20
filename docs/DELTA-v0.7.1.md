# v0.7.1 delta — apply on top of the v0.7.0 delta (before PR1 merges)

    okg/archi-crab/VENDOR.yaml            ADD   vendored-file manifest (verbatim entries + ours)
    scripts/vendor-sync.sh                ADD   --check (CI drift guard) / --apply (resync)
    scripts/gen-cern-team.sh              REPL  first-scaffold only; no manual schema copy (stale README step 2)
    .github/workflows/ci.yaml             REPL  + vendor-check job; guard for VENDOR.yaml
    .github/workflows/build.yaml          REPL  runs vendor-sync --apply from the new image before opening the engine-bump PR
    .github/workflows/main.yaml           REPL  identical to v0.7.0 (included for a clean overwrite)
    docs/RUNBOOK-v0.7.1.md                ADD   Phase B rewritten around vendoring

    tar xzf archi-crab-okg-v0.7.1-delta.tar.gz --strip-components=1 -C ~/archi-crab/archi-crab-okg
Requires yq v4 locally for the scripts.
