# dmwm/CRABServer issue #8617: Remove TaskType backward compatibility

State: closed
Opened: 2024-08-13T12:59:00Z
Closed: 2025-04-29T14:34:58Z
Labels: Status: Done, Priority: High, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8617

## Opening post (belforte, 2024-08-13T12:59:00Z)

2 months after https://github.com/dmwm/CRABServer/pull/8616 has been put in production
* look for all places where there's a reference to CRAB_DAGType
* look for the cases where it is combinded (OR-ed typically) with old TaskType
* remove reference to old variant

## Comment (belforte, 2025-04-17T11:02:01Z)

enough time has passed. No reason to hold anymore.

## Comment (belforte, 2025-04-24T15:58:07Z)

note that in the code we also have `CMS_TaskType`, which must be kept, and `CRAB_DashboardTaskType`, which is very likely part of obsolete code.
