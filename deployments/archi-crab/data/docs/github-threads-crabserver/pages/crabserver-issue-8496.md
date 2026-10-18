# dmwm/CRABServer issue #8496: capture MasterWorker/Publisher log

State: closed
Opened: 2024-06-14T20:11:06Z
Closed: 2024-09-03T11:34:27Z
Labels: Type: Question, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8496

## Opening post (belforte, 2024-06-14T20:11:06Z)

IIUC this lines
https://github.com/dmwm/CRABServer/blob/e6eb58703768825380e22efebd14889411d8c52a/cicd/crabtaskworker_pypi/TaskWorker/manage.sh#L44
https://github.com/dmwm/CRABServer/blob/e6eb58703768825380e22efebd14889411d8c52a/cicd/crabtaskworker_pypi/Publisher/manage.sh#L44
make the stdout/stderr of Master* get lost. While it previously was saved in the `nohup.out` file.

This makes it hard to debug crashes. Esp. if coming at the start.

Or am I simply unable to find the log ?

## Comment (novicecpp, 2024-06-18T16:40:51Z)

For now, it should printout to container's stdout/err. 
Run `docker logs TaskWorker` to see the logs. 

However it will not save to container's stdout properly when you re-start service by `./start.sh -c`  again.

## Comment (novicecpp, 2024-09-03T11:34:27Z)

This PR https://github.com/dmwm/CRABServer/pull/8658 also put the startup logs to `logs/nohup.out`.
