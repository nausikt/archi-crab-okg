# dmwm/CRABServer issue #7988: REST - new api that exposes the crab Oracle DB tables and indexes size

State: closed
Opened: 2023-11-01T18:14:57Z
Closed: 2026-07-13T14:38:39Z
Labels: Type: Enhancement, Priority: Low, Status: Available, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/7988

## Opening post (mapellidario, 2023-11-01T18:14:57Z)

It would be nice to have a panel in grafana where we can monitor the size of the oracle tables and indexes that we use for prod and preprod.

We could imitate what DBS is doing. Use this query [1] to get a result similar to [2], which is a json document.
DBS code is here [3]. However, we use partitioned tables, so we may need to use slightly different queries, as described in our db admin docs [4].

After a quick discussion in a crab dev weekly meeting, instead of a json, we may prefer to expose the stats in a flat format compatible with prometheus, so it can easily be scraped by existing CMS Monit infrastructure. In order to flatten DBS schema, we can use an approach similar to what wmcore is using to flatten cherrypy metrics [5].

---

[1] curl -L --key $X509_USER_PROXY --cert $X509_USER_PROXY "https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader/dbstats" | jq

[2] https://dmapelli.web.cern.ch/dmapelli/crab/20231101-dbs-dbstats/dbstats.json

[3] 

function https://github.com/dmwm/dbs2go/blob/28e02bde209af797af7d59d4f7e3baba25a98605/dbs/stats.go#L50 calling queries

- full table query: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_db_size.sql
- full index query: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_db_indexes.sql
- table size, by schema: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_schemas_size.sql
- index size, by schema: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_schemas_indexes.sql
- table size, by table: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_tables_size.sql
- index size, by table: https://github.com/dmwm/dbs2go/blob/master/static/sql/stats_tables_indexes.sql

[4] https://cmscrab.docs.cern.ch/technical/crab-rest/database-admin.html#check-size-of-current-tables-and-indexes

[5]

- endpoint: https://github.com/dmwm/WMCore/blob/fbaabff7b705eafaf11c558bf1f04c95dece9f57/src/python/WMCore/REST/Server.py#L373
- using functions from https://github.com/dmwm/WMCore/blob/master/src/python/Utils/CPMetrics.py

## Comment (belforte, 2026-07-13T14:38:39Z)

we will not do this
