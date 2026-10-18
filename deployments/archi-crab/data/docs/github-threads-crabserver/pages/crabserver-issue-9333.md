# dmwm/CRABServer issue #9333: move FailedMigrationAccounter from CSV file to SQLite

State: closed
Opened: 2026-06-26T10:12:52Z
Closed: 2026-08-24T10:17:50Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/9333

## Opening post (belforte, 2026-06-26T10:12:52Z)

current use of CVS file in this class is fragile in view of concurrent processes
https://github.com/dmwm/CRABServer/blob/e371f33876cf7a9fef1939a4763817a085507559/src/python/Publisher/PublisherUtils.py#L334

should replace the file with an SQLite DB, and evaluate if more parameters are worth storing (id of last failed migration for a block  ? History of all failures for that block ? )

Also provide some utility to visualize/explore the DB for non-SQL-savvy operators, e.g script(s) to list content (with time filtering) and to search by block (also dataset ?)

Think if we simply grow the DB "forever" or want a method to remove old things, certainly nobody will care to investigate things which failed 1 year ago.

Of course DB file must be (like the current CSV one) on a directory mounted from the host disk !

## Comment (belforte, 2026-07-22T15:06:27Z)

we will not need this if we stop publishing parentage and hence avoid migrations

## Comment (belforte, 2026-08-24T10:17:50Z)

we decided not to publish parents anymore
