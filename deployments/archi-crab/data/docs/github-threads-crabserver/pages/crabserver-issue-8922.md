# dmwm/CRABServer issue #8922: TW starting with v3.250204 breaks current CRABClient preparelocal

State: closed
Opened: 2025-02-15T17:22:41Z
Closed: 2025-02-15T17:58:50Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8922

## Opening post (belforte, 2025-02-15T17:22:41Z)

changes to CMSRunAnalysis.py introduced in a3457ab52f3020cf1bf6289090a3d086f1fdc520 are not compatible with current client v3.241218 or earlier ones.

There is some "confusion" in names of argument for CMSRunAnalysis.py

One  of the main goal of current cleanup is indeed to remove the need for the client to know and manipulate the names of those arguments !
