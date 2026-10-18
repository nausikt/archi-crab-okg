# dmwm/CRABServer issue #9099: add back ALWAYS-UPDATE to Dagmans

State: closed
Opened: 2025-05-29T15:27:38Z
Closed: 2025-05-29T15:44:09Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9099

## Opening post (belforte, 2025-05-29T15:27:38Z)

with ref to https://github.com/dmwm/CRABServer/issues/9098#issuecomment-2919689836

when Dagman exits with some failed nodes, it is not really guaranteed that `node_status` file is updated.

So we end up with a `node_status` (and crab status) that reports a running dagman and node in PRE status even if Dagman ha exited.

Need to revert part of the change discussed in https://github.com/dmwm/CRABServer/issues/9012 and implemented in https://github.com/belforte/CRABServer/commit/7606a362f98751b826841718b726f8be811ce7f1
with PR #9012 which is in TW since  [v3.250401](https://github.com/dmwm/CRABServer/releases/tag/v3.250401)

I think that we are not ready to deploy in production latest tag [v3.250509](https://github.com/dmwm/CRABServer/releases/tag/v3.250509). So will make an hot patch on top of v3.250424 which we run now.

## Comment (belforte, 2025-05-29T15:44:10Z)

fixed via #9100 (in v3.250424.patch branch) and #9101 (in master branch)
