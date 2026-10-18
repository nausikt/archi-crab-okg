# dmwm/CRABServer pull request #8643: monit - runcontainer improved

State: closed
Opened: 2024-08-23T07:45:11Z
Closed: 2024-08-23T07:45:21Z
Merged: 2024-08-23T07:45:21Z
URL: https://github.com/dmwm/CRABServer/pull/8643

## Opening post (mapellidario, 2024-08-23T07:45:11Z)

fixing a bug in #8640 that caused all the stdout of the monit container not to reach the email in case of problems. I tested this on crab-dev-tw02 and it works fine
