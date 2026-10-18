# dmwm/CRABServer issue #9012: reduce the update frequency of DAGMAN's node_status file

State: closed
Opened: 2025-03-20T10:30:54Z
Closed: 2025-05-28T16:08:57Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9012

## Opening post (belforte, 2025-03-20T10:30:54Z)

see discussion in MatterMost with Marco

![Image](https://github.com/user-attachments/assets/9c897836-dda7-4640-ac56-3272a20fb7de)

![Image](https://github.com/user-attachments/assets/b8b665a3-e5cf-42fb-bc0e-479af5df6c5e)

## Comment (belforte, 2025-03-31T10:02:47Z)

[documentation](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-information-files.html) says:
* `quote`

To have DAGMan write the node status file simply use the [NODE_STATUS_FILE](https://htcondor.readthedocs.io/en/latest/automated-workflows/dagman-reference.html#NODE_STATUS_FILE) commands syntax as follows:

NODE_STATUS_FILE filename [minimumUpdateTime] [ALWAYS-UPDATE]

The status file may be updated once per [DAGMAN_USER_LOG_SCAN_INTERVAL](https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#DAGMAN_USER_LOG_SCAN_INTERVAL) in combination with the optional minimumUpdateTime value which defaults to 60 seconds. The status file is also updated a final time when the DAG completes either successfully or not.

Normally the node status file is only updated if the status of some node has changed since the last file update. If provided the optional ALWAYS-UPDATE keyword then DAGMan will always update the status file even if no nodes have changed status.
* `end-quote`

our line is:
`NODE_STATUS_FILE node_state{nodestate} 30 ALWAYS-UPDATE`
 
I read that for our case as:
  dag status is checked every 30 seconds and a new file written all of the times.
If we simply remove `ALWAYS-UPDATE` it will be:
  dag status is checked every 30 seconds and a new file written if status has changes since last file update

So in addition to removing `ALWAYS-UPDATE` we may want to decrease the update frequency to e.g. a couple minute.
I am wary of making it 5 minutes, since when coupled with the 5 min period of `cache_status.py` it may lead to status information lagging up to almost 10 mins.
