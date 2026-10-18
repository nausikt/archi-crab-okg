# dmwm/CRABServer issue #9217: make MAX_MEMORY_SINGLE_CORE configurable via TaskWorkerConfig.py

State: closed
Opened: 2025-10-15T15:32:11Z
Closed: 2025-10-21T10:26:23Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9217

## Opening post (belforte, 2025-10-15T15:32:11Z)

as discussed in today's CRAB [meeting](https://indico.cern.ch/event/1601406/?note=352640) we want to have an "emergency" switch so that we can allow to go over the new 3GB max memory limit for single core jobs in case a user has a need.

Plan is to update TW config locally in TaskWorker so that the new limit is in effect until we restart TW again (puppet will reset to the default).

We do not see the need to have this as a hiera variable in puppet which would allow a persistent change on a per-TW base controlled via a Gitllab commit. But of course that can be done later if such a need arise. Chances are that we never need this !!

Of course could do via editing `/data/srv/current/lib/python/site-packages/ServerUtilities.py` and `start.sh -c`, but using the config. makes it a bit more clear and easy to do better in the future. It becomes like the canary fraction.

## Comment (belforte, 2025-10-15T19:31:49Z)

TW side of this is in https://github.com/dmwm/CRABServer/pull/9219

Now need to add the param to TaskWorkeConfig.py (even TW uses the constant from ServerUtilities as default if nothing is present in the configuration)

## Comment (belforte, 2025-10-21T16:39:19Z)

the changes to TW config in puppet are in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/376

In the end I made it a hiera variable so it can be configured in the YAML file of any specific TW machine
