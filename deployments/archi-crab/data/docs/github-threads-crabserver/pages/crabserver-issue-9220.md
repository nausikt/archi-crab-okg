# dmwm/CRABServer issue #9220: Clean up all externalconfig dependencies e.g. backend-urls, htcondor{Pool|Schedd}, ProxiedUrl on REST.

State: closed
Opened: 2025-10-16T11:33:40Z
Closed: 2025-12-03T16:18:48Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9220

## Opening post (nausikt, 2025-10-16T11:33:40Z)

A continuation from #9201. at first glance, I found that there is 5 places as following for cleaning-up.
### Straightforward places
- [x] **[1]** backendurls endpoint that just serves retrieved external config.
*P.S. where we use it as adhoc endpoint during this refactoring.*
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTServerInfo.py#L45-L54
- [x] **[2]** inside `getCentralConfig(extconfigurl)` utility function, we can safely remove `backend-urls` and no longer need to retrieve `htcondorScheddsLink`, htcondor{Pool|Schedds}` relevant, stuffs there.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/Utilities.py#L127-L131
- [x] **[3]**  `ProxiedUrl` that could be embed as a `static` pattern, thus no longer need to fetch from dynamically external config.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTTask.py#L236-L257

### Non-trivial places
- [x] **[4]** logic on REST that retreived backend-urls to just to doing some kind of setting default value to `collector` equal to `htcondorPool` from global external config. (wrote 10 yrs++ ago)
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/DataWorkflow.py#L151-L155
> This one might be trivial at first glance by just migrating this logic to TW, where backend-urls info was there.
> BUT AFAIU,  collector was expected to be dumped into database, `tm_collector` task information? by other mean expected to be resolved earlier in crab submit lifecycle given current design? do we have any TaskAction perfect with to write/send this resolved information of `finalized` solver, back to REST when we do submit?

- [x] **[5]** The last script that still call **[1]** *backendurls* endpoint, which i don't know whether it's still be used or we could safely deprecated them.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/scripts/Monitor/dashbgen.sh#L50-L68

## Comment (belforte, 2025-10-24T14:00:04Z)

about 4):  we need to still allow for a collector to be speciied in the submit command, so that we can submit to e.g. ITB. WHen we use collector from TW config, it may be nice to store in DB. But not a sgtrong necessity
about 5)  I have no idea what this script is meant for !!! Let's do some git -blame search. Result: not used !
