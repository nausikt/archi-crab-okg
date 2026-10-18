# dmwm/CRABServer issue #8371: use userInputFiles list to select which files to process in a dataset

State: closed
Opened: 2024-05-02T16:01:14Z
Closed: 2024-05-16T16:31:03Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8371

## Opening post (belforte, 2024-05-02T16:01:14Z)

effectively turn it into a "file mask" by treating all files not listed in there as invalid.
To be used together with
https://github.com/dmwm/CRABClient/issues/5308

at first sight a small change here will do
https://github.com/dmwm/CRABServer/blob/b959b782d96fd7d0ca4e163475633c0492ce7c05/src/python/TaskWorker/Actions/DataDiscovery.py#L44-L47

the list should be available as `'task['tm_user_files']`
