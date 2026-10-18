# dmwm/CRABServer issue #8917: remove hack for HTC v2 bug in Resubmitter

State: closed
Opened: 2025-02-12T16:22:19Z
Closed: 2025-02-13T00:42:45Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8917

## Opening post (belforte, 2025-02-12T16:22:19Z)

the bug in v2 binding described in #8604  is gone in the HTC release which we use now 24.0)

so we can simplify this code
https://github.com/dmwm/CRABServer/blob/a137724010dfd83d7db01cbaefb5ceadd15f670e/src/python/TaskWorker/Actions/DagmanResubmitter.py#L103-L105

I think I can simply remove `repr()` but of course will need to test
