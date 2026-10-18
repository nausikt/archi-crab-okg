# dmwm/CRABServer issue #7598: Refactoring RUCIO_Transfers.py

State: closed
Opened: 2023-04-14T17:53:41Z
Closed: 2023-07-19T08:56:39Z
Labels: Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7598

## Opening post (novicecpp, 2023-04-14T17:53:41Z)

Open this issue for discuss design and ask some questions.
The current goal is https://github.com/dmwm/CRABServer/issues/7524 .

## Comment (novicecpp, 2023-04-14T17:55:53Z)

**This proposal is now obsolete.** 

--------------------

I am propose change on [monitor\_locks\_status()](https://github.com/belforte/CRABServer/blob/0f37bb5ef61acb2127fdb97b97e77cbd33d96b85/scripts/task_process/RUCIO_Transfers.py#L591-L688).

This function get replicas info by drill down from container name to get replicas info (list dataset -> list rules -> list replicas).

I propose change it to:
- Add first bookkeeping of rule ID when the rule is created (For a new code, it is at [BuildTaskDataset.createDataset()](https://github.com/novicecpp/CRABServer/blob/0082a15ef8e8fedfe844ac8344697506350daf85/src/python/ASO/Rucio/Actions/BuildTaskDataset.py#L108))
  - In the map of `{ruleID: datasetName}`
  - If duplicaterule is raised, better to get ruleid and ensure it already in bookkeeping
- Then in new `monitor_locks_status`, loop over above list, and do usual stuff.
  - I want to ensure that replicas we track is only from the rules we created.
- Also, remove [id2lfn\_map](https://github.com/dmwm/CRABServer/blob/1f17608a8baa29ad042e229035794def865c23b3/scripts/task_process/RUCIO_Transfers.py#L634-L640) checking from this function because we agree to seperate container for track status and publish container.
- Second bookkeeping for "OK" replicas is done per dataset.
  - In format of `datasetName` per line.
  - skip the rule where dataset name match with this bookkeeping.
  - I don't want to write full replicas name to the file because we use too much IO in schedd machine.

@belforte what do you think?

## Comment (novicecpp, 2023-07-19T08:56:39Z)

Refactoring is done via  https://github.com/dmwm/CRABServer/pull/7587 https://github.com/dmwm/CRABServer/pull/7675 and https://github.com/dmwm/CRABServer/pull/7649.  The design has quite changes compare to original RUCIO_Transfers.py scripts.

Closing this issue and move to https://github.com/dmwm/CRABServer/issues/7632.
