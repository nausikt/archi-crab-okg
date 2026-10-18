# dmwm/CRABClient issue #5310: do not fail on spurious gfal-copy errors

State: closed
Opened: 2024-05-13T17:39:47Z
Closed: 2024-05-13T17:43:09Z
Labels: bug, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5310

## Opening post (belforte, 2024-05-13T17:39:47Z)

sometimes `gfal-copy` prints a message containing the `error` string to `stderr`, but the command succeeds. Currently this results (incorrectly) in client reporting failure.

Should check exit code first, and if that is 0, assume that copy was OK and parse stderr/stdout only to add information, no to take decisions. At least not on a generic string.

See https://github.com/dmwm/CRABServer/issues/8357
