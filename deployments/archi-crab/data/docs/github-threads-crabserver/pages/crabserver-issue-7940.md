# dmwm/CRABServer issue #7940: RUCIO_Transfers.py: change the Publish Container to  Publish Container to alway locks successfully transfer files

State: closed
Opened: 2023-10-12T08:41:09Z
Closed: 2023-10-16T16:09:17Z
Labels: Priority: High, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7940

## Opening post (novicecpp, 2023-10-12T08:41:09Z)

Stick to **Publish Container also used for keeping data on disk whenever users want to publish to DBS or not.**

Maybe just simply remove line 39 in 
https://github.com/dmwm/CRABServer/blob/50a9f8aa9d8ae6f55034cc62e3b6a27870b2c522/src/python/ASO/Rucio/Actions/MonitorLockStatus.py#L38-L45

Need to think/test to confirm.

## Comment (novicecpp, 2023-10-13T11:26:41Z)

This summary table show possible output of crab tasks with publish status, and the output dataset name.

| case | output edm | output tfile        | output misc   | publication | output dataset name | note  |
| ---- | ----- | --------- | ---- | ----------- | ------------------- | ----------------------------- |
| 1    | x     |           |      | T           | /GenericTTBar       |                               |
| 2    |       | x         | (x)  | T           |                     | Fail in crab submit           |
| 3    | x     |           | x    | T           | /GenericTTBar       | Success, but only publish edm |
| 4    | x     |           |      | F           | /FakeDataset        |                               |
| 5    |       | x         | (x)  | F           | /FakeDataset        |                               |
| 6    | x     |           | x    | F           | /FakeDataset        |                               |
| 7    | \>1   |           |      | T           |                     | Fail in crab submit           |
| 8    | \>1   |           |      | F           |    N/A                 | Not test yet     |

The weird case, like case 3, is working as I expected, thanks to the design (by Stefano) where the Publisher processes block level but publishes each file individually.
