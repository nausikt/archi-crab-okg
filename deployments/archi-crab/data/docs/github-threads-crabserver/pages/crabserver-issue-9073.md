# dmwm/CRABServer issue #9073: use task status information in scheduling

State: open
Opened: 2025-05-14T08:27:01Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9073

## Opening post (belforte, 2025-05-14T08:27:01Z)

Current code moves tasks from WAITING to NEW in round-robin fashion.

This can be improved:

1. do not move to NEW more tasks then TW can digest (i.e. look at number in NEW)
   * we have seen that when there is a submission burst tasks are moved in NEW very quickly, but once they are in NEW we loose scheduling and things become random (tasks are processed in the order in which they get fetched from DB with a `limit` option in SQL)
 2. get from DB the information  about dag status and number of jobs and reduce the share for users who are already using a lot of resources
   * this may require new API's to fetch data from task table with a "created since" constrain
   * be aware that tasks with failed jobs will appear s completed but can be re-activated by a `crab resubmit`. Can/should we do anything ?
