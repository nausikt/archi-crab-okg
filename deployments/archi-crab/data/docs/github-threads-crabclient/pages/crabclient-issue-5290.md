# dmwm/CRABClient issue #5290: avoid interference from user local python environment

State: closed
Opened: 2024-02-06T16:37:48Z
Closed: 2024-02-16T11:16:52Z
Labels: enhancement, Support, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5290

## Opening post (belforte, 2024-02-06T16:37:48Z)

as per
https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE
add
```
export PYTHONNOUSERSITE=true
```
to `bin/crab`

ref: https://cms-talk.web.cern.ch/t/crab-status-fails/34034/7


thanks @novicecpp
