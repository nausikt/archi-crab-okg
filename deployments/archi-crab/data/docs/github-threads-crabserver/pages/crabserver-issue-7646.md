# dmwm/CRABServer issue #7646: add REST API to list tasks by tm_ddm_reqid

State: closed
Opened: 2023-05-25T08:42:43Z
Closed: 2023-06-14T17:36:40Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7646

## Opening post (belforte, 2023-05-25T08:42:43Z)

after the change in container name for tape recall requests in https://github.com/dmwm/CRABServer/pull/7641
we need a way to find which task is waiting on which rule, so that we can still build the table in https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/CheckTapeRecall.py

- [x] add new API to REST - #7655
- [x] need also new SQL query - #7655 
- [x] modify CheckTapeRecall to use it - #7662 #7663 #7665 #7664
