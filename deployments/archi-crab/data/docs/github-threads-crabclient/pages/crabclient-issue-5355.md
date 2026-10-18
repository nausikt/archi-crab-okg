# dmwm/CRABClient issue #5355: crab recover should not fail if issued before task completed

State: closed
Opened: 2024-11-27T20:17:34Z
Closed: 2024-11-27T21:04:15Z
URL: https://github.com/dmwm/CRABClient/issues/5355

## Opening post (belforte, 2024-11-27T20:17:34Z)

avoid spurious errors in CI if task execution is delayed.
In this case `crab recover` issues a `kill` but does not wait for e.g. transfers to stop.
