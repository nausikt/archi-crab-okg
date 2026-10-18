# dmwm/CRABServer issue #9282: set XRD_LOGLEVEL=Debug in job wrapper

State: open
Opened: 2026-03-23T20:52:50Z
Labels: Type: Enhancement, Status: Done, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/9282

## Opening post (belforte, 2026-03-23T20:52:50Z)

@dynamic-entropy has asked that we enable more extensice xroot logging via
 `export  XRD_LOGLEVEL=Debug`
in the job wrapper before we execute `cmsRun`
That will enable him to better figure out the reason behind exit codes 802x and improce xroot client error reporting

This is hopefully something temporary which we can revert after a while.

## Comment (belforte, 2026-07-03T19:18:49Z)

PR was prepared, but looks like @dynamic-entropy does not need this ! On hold
