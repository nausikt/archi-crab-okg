# dmwm/CRABServer issue #9214: TW/Upload log content in CRABMonitor can be rendered right away

State: open
Opened: 2025-10-14T09:24:06Z
Labels: Type: Enhancement, Priority: Low
URL: https://github.com/dmwm/CRABServer/issues/9214

## Opening post (nausikt, 2025-10-14T09:24:06Z)

UX around TW/Upload log could be improved.

The content can be rendered right away in one-click instead of 3 clicks, downloading the intermediates every time we debugging. 

We can get it done by implementing tab click as chain-of-promises rendering and this js codebase could be simplified as well, See also #9204.
