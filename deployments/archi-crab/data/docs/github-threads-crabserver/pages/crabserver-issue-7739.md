# dmwm/CRABServer issue #7739: in RUcioDataDiscovery allow for multiple scopes

State: closed
Opened: 2023-07-10T21:56:49Z
Closed: 2024-01-18T12:47:32Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7739

## Opening post (belforte, 2023-07-10T21:56:49Z)

scope of the top container may be different form scope of the datasets.
Need to pick scope from Rucio's `list_content`, not assume it is static.

FYI @dciangot

## Comment (belforte, 2024-01-17T16:43:23Z)

original report
```
rucio list-dataset-replicas  user.dciangot:/datasets/dataset_cc/USER --deep   

DATASET: user.mascioti:/datasets/dataset_cc/USER#1
+-----------------+---------+---------+
| RSE             |   FOUND |   TOTAL |
|-----------------+---------+---------|
| T2_IT_Rome_Temp |     500 |     500 |
| T2_IT_Rome      |     500 |     500 |
+-----------------+---------+---------+
```
