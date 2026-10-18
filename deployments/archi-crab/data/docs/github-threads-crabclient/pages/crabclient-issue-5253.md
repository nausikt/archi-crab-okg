# dmwm/CRABClient issue #5253: review --instance vs. --dbs-instance

State: closed
Opened: 2023-11-27T13:21:00Z
Closed: 2023-11-27T16:40:08Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5253

## Opening post (belforte, 2023-11-27T13:21:00Z)

we must consistently use `--instance` to indicate CRAB instance (`prod/preprod/test2/test11/...`) and `--dbs-instance` to indicate DBS instance (`prod/global`, `prod/phys03`, etc.)
See https://github.com/dmwm/CRABClient/pull/5252#discussion_r1404590312
