# v0.7.0 delta — apply onto main@468d672

Files in this tarball REPLACE or ADD (nothing else in the repo changes in PR1):

    docker/runtime/Dockerfile                       ADD   upstream okg + archi
    .github/workflows/build.yaml                    ADD   build → engine-bump PR
    .github/workflows/ci.yaml                       REPL  + ARCHI_DATA_ROOT, guards for extractors/bridge files
    .github/workflows/main.yaml                     REPL  + ARCHI_DATA_ROOT; versions.lock removed from paths
    versions.lock                                   REPL  archi + runtime pins (fill 2 REPLACE_ME before merge)
    scripts/gen-cern-team.sh                        ADD   the generator ritual
    scripts/smoke.sh                                REPL  CMSSW query restored
    okg/archi-crab/invariants.yaml                  REPL  4-subtype floor (survives the generator)
    helm/okg/DELTA-5-archi-data-root.md             ADD   apply in Phase C, then delete
    docs/RUNBOOK-v0.7.0.md                          ADD

Do NOT touch envs/* in PR1 — they keep the upstream image so lint stays green;
build.yaml's engine-bump PR (PR2) is what switches them.

    tar xzf archi-crab-okg-v0.7.0-delta.tar.gz --strip-components=1 -C ~/archi-crab/archi-crab-okg
    cd ~/archi-crab/archi-crab-okg && git status
