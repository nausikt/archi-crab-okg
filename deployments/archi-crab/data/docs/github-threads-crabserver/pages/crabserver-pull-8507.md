# dmwm/CRABServer pull request #8507: Fix pre job

State: closed
Opened: 2024-06-17T19:00:19Z
Closed: 2024-06-17T19:00:28Z
Merged: 2024-06-17T19:00:28Z
URL: https://github.com/dmwm/CRABServer/pull/8507

## Opening post (belforte, 2024-06-17T19:00:19Z)

this fixes a bug in previous commit f700045273ff40d510dea30441fd2eccde053af3 which I introduced after testing, when I fixed `pylint` warnings in PreJob.py in line https://github.com/dmwm/CRABServer/blob/e6eb58703768825380e22efebd14889411d8c52a/src/python/TaskWorker/Actions/PreJob.py#L516a
```python
fd_prejob_log = os.open(prejob_log_file_name, os.O_RDWR | os.O_CREAT | os.O_TRUNC, 0o644)
```
and replaced it with
https://github.com/dmwm/CRABServer/blob/f700045273ff40d510dea30441fd2eccde053af3/src/python/TaskWorker/Actions/PreJob.py#L516
which could not possibly work.

In the end I decided to replace the obscure use of `os.open()` and `os.dup2` with plain calls to `logging.logger`.

## Comment (novicecpp, 2024-06-18T08:39:14Z)

Stefano, could you please provide the information why you need this PR?
Usually, you have issue number in the PR but not this one.

## Comment (belforte, 2024-06-18T09:27:28Z)

I have added a description at the top.

## Comment (novicecpp, 2024-06-18T09:29:45Z)

Thanks! :+1:
