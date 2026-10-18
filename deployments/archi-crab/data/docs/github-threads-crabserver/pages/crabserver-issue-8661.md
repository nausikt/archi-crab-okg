# dmwm/CRABServer issue #8661: fix ReportRecallQuota for new usage of Rucio account

State: closed
Opened: 2024-08-28T11:57:54Z
Closed: 2024-09-17T11:07:03Z
URL: https://github.com/dmwm/CRABServer/issues/8661

## Opening post (belforte, 2024-08-28T11:57:54Z)

current code checks quota used by Rucio account `crab_tape_recall` but now we create rules with `account=username` in order to enforce a user quota.
This code needs to change
https://github.com/dmwm/CRABServer/blob/3f837baf0a67b1e90e2a7e98596bee5c9865ce3e/src/script/Monitor/ReportRecallQuota.py#L29-L46

to instead check total usage for `activity = "Analysys TapeRecall"`

## Comment (belforte, 2024-08-28T12:25:59Z)

A simple possibility is to re-use these functions 
https://github.com/dmwm/CRABServer/blob/3f837baf0a67b1e90e2a7e98596bee5c9865ce3e/src/python/RucioUtils.py#L106-L126
modifying the `getTapeRecallUsage` to be able to work w/o an account name, selecting simply by activity in that case.

@aspiringmind-code do not hesitate to ask me for help. One goal here is to make you understand how we track/enforce quotas of tape recall
