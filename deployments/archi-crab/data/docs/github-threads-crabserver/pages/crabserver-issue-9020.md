# dmwm/CRABServer issue #9020: all tasks get 7-days ASO timeout in v3.250310

State: closed
Opened: 2025-03-28T16:56:18Z
Closed: 2025-03-29T16:16:04Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9020

## Opening post (belforte, 2025-03-28T16:56:18Z)

in current master
https://github.com/dmwm/CRABServer/blob/becd9e6008d69afef8bd9151e489d023f9738d95/src/python/TaskWorker/Actions/DagmanCreator.py#L365

which is obviously wrong since CRAB_ASORucioTimeout (7 days) should only be used for tasks which send output via Rucio

Previous code was
https://github.com/dmwm/CRABServer/blob/a6115c5b782bc9c0fe270f7f94c4ccf40df4a609/src/python/TaskWorker/Actions/DagmanCreator.py#L506-L510

## Comment (belforte, 2025-03-28T17:07:04Z)

FYI @aspiringmind-code @sinonkt
