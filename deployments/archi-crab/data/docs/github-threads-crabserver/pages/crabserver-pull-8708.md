# dmwm/CRABServer pull request #8708: fix #8703 and minor improv. to CI

State: closed
Opened: 2024-09-20T15:40:18Z
Closed: 2024-09-20T15:40:48Z
Merged: 2024-09-20T15:40:48Z
URL: https://github.com/dmwm/CRABServer/pull/8708

## Opening post (belforte, 2024-09-20T15:40:18Z)

in addition to fixing #8703 


* tag name is set as version for development pipeline buids
* a CR at the end of TaskWorker/__init__.py file so that it looks OK when doing `cat`

## Comment (belforte, 2024-09-20T15:40:44Z)

tested in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8175636
