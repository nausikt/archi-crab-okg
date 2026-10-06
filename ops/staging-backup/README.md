# ops/staging-backup — insurance before staging is wiped (RUN1-FREEZE step 4)

`docs/RUN1-FREEZE.md` rebuilds staging from scratch for okg v4. Wiping deletes staging's
volumes (reclaim policy Delete), and with them everything okg v3 accumulated there. This
directory takes one read-only dump first, into its own PVC. Nothing in the plan restores it.

```bash
kubectl apply -f ops/staging-backup/pvc.yaml
kubectl apply -f ops/staging-backup/dump-job.yaml
kubectl -n archi-crab-staging logs -f job/archi-crab-okg-staging-backup
```

`/backup/staging-v3/` then holds: `MANIFEST` (what staging ran, when, okg's fingerprint),
`SHA256SUMS`, `globals.sql` (roles WITH password hashes: treat the PVC as a secret),
`databases.txt`, and per database `<db>.dump` (custom format), `<db>.extensions.txt`,
`<db>.props.sql`; for okg also `okg.fingerprint.txt` and `okg.indexes.txt`, read in the
same snapshot as the dump.

**If it is ever needed**, into an EMPTY okg Postgres running the same okg-postgres image
(as `postgres`, per database, in this order):
1. `psql -d postgres -f globals.sql` (skip the `postgres` role lines; "already exists" is fine)
2. `CREATE DATABASE <db> TEMPLATE template0` with the encoding/collation of `databases.txt`
3. if `<db>.extensions.txt` lists timescaledb: `CREATE EXTENSION timescaledb VERSION '<that>'`,
   then `SELECT timescaledb_pre_restore();`
4. `pg_restore -d <db> -j 2 <db>.dump`
5. timescaledb: `UPDATE _timescaledb_config.bgw_job SET scheduled = false WHERE id >= 1000`
   if nothing may change the data, then `SELECT timescaledb_post_restore();`
6. `psql -d <db> -f <db>.props.sql`; `vacuumdb -d <db> --analyze-only`
7. okg: the two fingerprint queries and the `pg_indexes` list must equal the files.

A tested Job doing exactly this (with the checks as gates) is in the first run1 patch set
(2026-10-06, `envs/run1/freeze/restore-job.yaml`), set aside when run1 became a fresh build.
