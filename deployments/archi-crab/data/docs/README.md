# data/docs — records for `docs-files` sources

One directory per source id in `sources/archi-crab.yaml`, each holding the
`records.json` that archi's documentation reader ingests and the `build.json`
that says how it was made:

    data/docs/<source id>/records.json    built by scripts/docs-build.py, committed
    data/docs/<source id>/build.json

Never hand-edit `records.json`: rebuild it from the files (docs/SOURCES.md §3). It
is sorted with one page per line, so the rebuild's `git diff` shows exactly which
pages changed. A page's identity is its URL; changing a page's URL is a new page
plus a stale one that okg will not retract.
