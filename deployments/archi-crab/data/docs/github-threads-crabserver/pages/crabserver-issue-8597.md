# dmwm/CRABServer issue #8597: stop using `schedd.transaction` in PostJob

State: closed
Opened: 2024-08-08T21:42:08Z
Closed: 2024-08-12T13:57:03Z
Labels: Type: Enhancement, Priority: High, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8597

## Opening post (belforte, 2024-08-08T21:42:08Z)

it has been [deprecated](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/htcondor.html#interacting-with-schedulers)
![image](https://github.com/user-attachments/assets/a6d18669-d786-4c72-9a63-8308e10c71bc)

need to change this code
https://github.com/dmwm/CRABServer/blob/7f4e9eed41081d9407a0c7b838a9438e0ba5bac0/src/python/TaskWorker/Actions/PostJob.py#L2912-L2920

## Comment (belforte, 2024-08-08T22:31:52Z)

`schedd.transaction` was introduced in https://github.com/dmwm/CRABServer/commit/48b3700c0f0feaf273f1ae766e53da61edcf0b6c
but there is no record of the reason for this choice. I suspect that we can simply remove it
