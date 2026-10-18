# dmwm/CRABServer issue #8900: crab kill broken in v3.250109

State: closed
Opened: 2025-01-29T20:57:41Z
Closed: 2025-01-30T15:55:07Z
Labels: Type: Bug, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8900

## Opening post (belforte, 2025-01-29T20:57:41Z)

I only noticed while testing new (extensice) changes to DagmanCreator and DagmanSubmitter that `crab kill` fails. as indicated in https://github.com/dmwm/CRABServer/pull/8893#issuecomment-2617090507 (**BUG 5**).

The bug was independent and present already in v3.250109 which we have in preprod since then and luckily did not deploy in production yet.

We need to add `crab kill` to our validation.

The problem is this line2
https://github.com/dmwm/CRABServer/blob/5bdfcbfd35295520e171d6d5ca7796bb089b05ce/src/python/TaskWorker/Actions/DagmanKiller.py#L42-L44

introduced in https://github.com/dmwm/CRABServer/commit/8ed2195d78b2c47daa55f2738bd9d98469f9b8f7 to fix #8874 

The problem is that the `task` dictionary at this point in the code is what MasterWorker retrieved via a GET to `workflowdb` REST API in https://github.com/dmwm/CRABServer/blob/5bdfcbfd35295520e171d6d5ca7796bb089b05ce/src/python/TaskWorker/MasterWorker.py#L430
and that API as per
https://github.com/dmwm/CRABServer/blob/5bdfcbfd35295520e171d6d5ca7796bb089b05ce/src/python/CRABInterface/RESTWorkerWorkflow.py#L86-L89
uses the SQL from [Task.GetReadyTasks_sql](https://github.com/dmwm/CRABServer/blob/5bdfcbfd35295520e171d6d5ca7796bb089b05ce/src/python/Databases/TaskDB/Oracle/Task/Task.py#L84-L99) which retrieves in the `WHERE`  only a subset of the DB Task table columns. `clusterid` is not one of them !! In spite of what the comment in the API above states. 😠 

Of course this must be because initially the `tm_*` columns where "all the information", then developers added more columns and not all SQL's have been changed. I do not know if it is possible to have code which retrieves all colums and properly names them, to avoid the need to list column names in so many places... 

Anyhow, I do not feel like changing the REST code now. Will add a call in DagmanKiller to retrieve the full info about the task in order to check `clusterid`
