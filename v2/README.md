# v2/ — archi v2 as a benchmark fixture

The LangChain-era retrieval stack (archi-physics/archi `main`, pinned in `versions.lock`),
headless: Postgres (pgvector + pg_textsearch), the data-manager that ingests the SAME source
list as the okg instances, and two MCP servers that expose its retrieval tools unchanged --
as two sidecars of the data-manager pod -- the same chart in CI and on the cluster. Exposure is
the CMSKubernetes mcp-gateway (ToolHive MCPRemoteProxy, CERN SSO) at
archi-crab-v2.cern.ch/grep/mcp and /vectorstore/mcp:

    grep     search_local_files, search_metadata_index, list_metadata_schema, fetch_catalog_document
    vector   search_vectorstore_hybrid, fetch_catalog_document

Decisions and runbook: docs/V2-BENCH.md.

    deployments/archi-crab/config.yaml   our choices (embedding, chunking, which collectors)
    helm/archi-v2/                        the chart (Argo CD); files/ is GENERATED:
      files/config.yaml, files/init.sql     <- v2/scripts/render-config.py (archi's own templates)
      files/weblists/archi-crab.list        <- scripts/sources.py render (from sources/archi-crab.yaml)
    envs/bench/values.yaml                the one environment (image digests pinned by v2-main after a green smoke)
    envs/ci/values.yaml                   image tags `ci`, for helm template in CI
    docker/Dockerfile.base                OUR base image (python:3.10 + archi's base requirements)
    docker/Dockerfile                     targets data-manager (model baked in), mcp; Dockerfile.postgres
    mcp/server.py                         the thin MCP layer (archi's tools, by introspection)
    scripts/                              render-config, contract-check, smoke, lock (fingerprints), vendor-sync
    versions.lock                         archi commit, our base image digest, our image digests (+ fingerprints)
    vendor/reference/                     upstream's Dockerfiles and chart, verbatim, for diffing
    argocd/                               an Application example for the IaC repository

Regenerate after any change to config.yaml or sources/:

    python3 v2/scripts/render-config.py --write --archi <archi checkout>   # or inside the image
    python3 scripts/sources.py render --write
    python3 scripts/sources.py lint --base published && python3 v2/scripts/render-config.py --check --archi <archi checkout>
