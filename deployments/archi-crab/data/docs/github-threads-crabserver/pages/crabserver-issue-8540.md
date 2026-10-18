# dmwm/CRABServer issue #8540: Change entrypoint of TW process to simple binary script

State: closed
Opened: 2024-07-04T10:30:24Z
Closed: 2024-07-09T10:43:31Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8540

## Opening post (novicecpp, 2024-07-04T10:30:24Z)

Currently we execute `MasterWorker.py` directly to start TW process.
https://github.com/dmwm/CRABServer/blob/c56db97db0f6ca6e885ff11f95c680201c649971/cicd/crabtaskworker_pypi/TaskWorker/manage.sh#L43-L50

To test change of `MasterWorker.py` itself, you need to copy-paste new version of this file to installation path every time, it does not work with `./start.sh -g` because script always point to installation path.

To fix this, create simple entrypoint script and import the `__main__` section from `MasterWorker.py` instead.
The same way we do with Rucio ASO, 

https://github.com/dmwm/CRABServer/blob/c56db97db0f6ca6e885ff11f95c680201c649971/scripts/task_process/RUCIO_Transfers.py#L7-L10
