# schemas/bridges — TODO before first lint (Runbook Phase 2, step 4)

Copy from the archi checkout INSIDE the pinned runtime image, then prune:

    IMG=ghcr.io/mitdbg/okg@sha256:5a825f73c8929d2153859d95bfaf4c6f4ae01f02d08477583a7af05131826705
    # locate: docker run --rm --entrypoint sh $IMG -c 'find / -path "*archi*/schemas/bridges/*.yaml" 2>/dev/null'
    docker run --rm --entrypoint cat $IMG <path>/schemas/bridges/operations.yaml > operations.yaml
    docker run --rm --entrypoint cat $IMG <path>/schemas/bridges/sources.yaml   > sources.yaml

Then in operations.yaml keep ONLY `cmssw_release_supersedes_release`. Every
other bridge names a connector this registry does not run -> lint blocker
(`bridge_subtype_unknown` / unknown-connector). In sources.yaml remove any
bridge referencing jira / docsite / twiki / monit connectors.

Rules that bite:
- Narrowings live ONLY in this directory. Placed anywhere else they are
  silently ignored, then explode at ingest as ProducerPolicyViolation.
- Ownership claim happens AFTER this directory is final. Any later edit ->
  re-run claim -> load -> lint (CI does exactly that every run).

Delete this README once both files exist.
