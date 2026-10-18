# dmwm/CRABServer issue #8700: deploy TW action timeout in production

State: closed
Opened: 2024-09-19T10:11:42Z
Closed: 2025-04-28T09:17:41Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8700

## Opening post (belforte, 2024-09-19T10:11:42Z)

see #8350 

maybe also rename config. param from "feature" ?

possible sequence

1. activate in prod, look at logs, wait O(1 day), turn off
2. put in canary TW, leave it there 2~3 weeks
3. enable for good

## Comment (belforte, 2025-04-24T14:30:10Z)

time for step 3. ?

## Comment (aspiringmind-code, 2025-04-28T09:17:41Z)

[Done](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/345)
