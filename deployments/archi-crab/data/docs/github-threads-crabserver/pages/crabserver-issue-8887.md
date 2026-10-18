# dmwm/CRABServer issue #8887: periodically clean Rucio quota usage by test accounts

State: closed
Opened: 2025-01-21T08:35:54Z
Closed: 2025-03-11T14:52:16Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8887

## Opening post (belforte, 2025-01-21T08:35:54Z)

pipeline submission failed because
```
elforte@lxplus805/github> rucio list-account-usage crabint1
+------------+------------+------------+--------------+
| RSE        | USAGE      | LIMIT      | QUOTA LEFT   |
|------------+------------+------------+--------------|
| T2_CH_CERN | 100.000 GB | 100.000 GB | 424.496 kB   |
| T2_IT_Rome | 0.000 B    | 100.000 GB | 100.000 GB   |
+------------+------------+------------+--------------+
+------------------+---------+---------+--------------+
| RSE EXPRESSION   | USAGE   | LIMIT   | QUOTA LEFT   |
|------------------+---------+---------+--------------|
+------------------+---------+---------+--------------+
belforte@lxplus805/github> 
```

something needs to be setup to avoid this from happening. Also do for `cmscrab`.

We have tools to cleanup in https://github.com/dmwm/CRABServer/tree/v3.250120/cicd/rucio
Need to have something which uses them automatically.

While we still have use for Jenkins tests, should also do for `cmsbot`

## Comment (belforte, 2025-01-21T13:51:17Z)

Same thing for `/eos/cms/store/user/crabint1` We need a periodic cleanup ! Even if atm it is only 20% full it is 200TB of useless stuff which keeps growing
