# dmwm/CRABServer issue #7543: fix chirping of exit code at job wrapper termination

State: closed
Opened: 2023-02-20T14:51:34Z
Closed: 2024-08-23T11:01:51Z
Labels: Priority: Medium, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7543

## Opening post (belforte, 2023-02-20T14:51:34Z)

job wrapper use condor_chirp when wrapper terminates to communicate exit code as a classAd. This proved to be a fragile operation. We should:
- [ ] execute it in the startup environment of the task
- [ ] avoid to call python in there to parse FJR but rather create a file with the exit code at same time we put it into FJR
- [ ] report to glideInWMS team situations where condor_chirp fails in the startup (pilot_ environment so that they can address those

## Comment (belforte, 2024-08-23T11:01:51Z)

Need to be reviewed, most likely we need nothing. All in all case where we do no have proper exit code are extremely rare. Better have specific examples to work on.
