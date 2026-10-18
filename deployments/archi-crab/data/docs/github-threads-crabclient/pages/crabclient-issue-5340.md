# dmwm/CRABClient issue #5340: add support for tarballs in S3, not on webdir

State: closed
Opened: 2024-10-24T15:57:13Z
Closed: 2024-10-25T15:12:20Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5340

## Opening post (belforte, 2024-10-24T15:57:13Z)

needed to support the restructuring in https://github.com/dmwm/CRABServer/issues/6544#issuecomment-2380693510

should look in S3 first, an if things are not there fall back to old (current) way to pull from WEB_DIR.

This allows us to deploy new TW and be ready to change the day dryrun works as per 
https://github.com/dmwm/CRABClient/pull/5329
and https://github.com/dmwm/CRABServer/issues/6544
