# dmwm/CRABServer issue #9325: ensure that core dumps are removed from WN before job ends

State: closed
Opened: 2026-06-22T09:33:22Z
Closed: 2026-06-22T17:20:56Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9325

## Opening post (belforte, 2026-06-22T09:33:22Z)

Although we set `coresize=0` in JDL, we have seen at least one case where core dumps are never the less spooled to the AP disk, which of course creates big problems with disk space since core dumps are multi-GB !!
Ref: #9324
