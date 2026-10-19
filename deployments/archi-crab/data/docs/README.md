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

## Sources harvested from public URLs (corpus/v0.2.0-rc1 and later)

`code-snapshots`, `public-web-docs` and the `github-threads-*` sources are not built
from a folder someone keeps elsewhere: their input is a list of public URLs, and the
bytes are fetched once with `scripts/harvest-fetch.py` (or `scripts/harvest-gh-threads.py`).
Each of those directories keeps what a rebuild needs, and not the fetched bytes:

    data/docs/<id>/snapshots.tsv | pages.tsv   the list: <file name><TAB><url><TAB><title>
    data/docs/<id>/pages/urls.tsv              the rows that were fetched (docs-build --urls input)
    data/docs/<id>/pages/manifest.json         fetched_at, status and sha256 per file
    data/docs/<id>/pages/.gitignore            ignores the fetched files themselves

Rebuild (the manifest's sha256 says whether the bytes changed):

    python3 scripts/harvest-fetch.py --list data/docs/<id>/<list>.tsv --out data/docs/<id>/pages
    python3 scripts/docs-build.py --src data/docs/<id>/pages --out data/docs/<id> \
        --urls data/docs/<id>/pages/urls.tsv --site-name <host> --strict --report /tmp/<id>.csv
    python3 scripts/leakage-audit.py --gold <gold checkout>      # must print 0 hit(s)

Pinned raw GitHub URLs (`raw.githubusercontent.com/<org>/<repo>/<sha or tag>/<path>`) give
every engine the same bytes; a live page gives same-day-identical bytes, so build v2 and
the okg instances of one corpus on the same day (docs/RELEASES.md).

Dropped pages are recorded under `dropped` in `build.json` with the date and reason; remove
the same files from the source folder so a rebuild does not bring them back.
