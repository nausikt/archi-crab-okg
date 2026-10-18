# dmwm/CRABClient issue #5239: allow users to force submit with python2

State: closed
Opened: 2023-10-23T08:37:09Z
Closed: 2024-01-10T09:37:38Z
Labels: HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5239

## Opening post (belforte, 2023-10-23T08:37:09Z)

for CMSSW_10 and 11 the default is now to use python3 to run crab, allowing fro Rucio client integration, But if some users have python2-only code in their configuration, they must be able to force usage of python2.

## Comment (belforte, 2023-11-09T22:23:31Z)

some ideas from discussion when this was opened, before I forget.

easiest seems to support something like
`crab py2 submit`
intercept the `py2` in the arg list inside `bin/crab`,  force `python_cmd=python2` and strip the `py2` from the list passed to `crab.py`
https://github.com/dmwm/CRABClient/blob/0edda22ce9af3ff76a41bc25fecb269762f54a6f/bin/crab#L1C8-L21

most difficult part is to agree on syntax for user ! 

Which commands would need python2 ? I.e. need to use crabConfig.py and/or PSet.py. Is that only `submit` ? If so maybe introduce `crab submitpy2` ?

## Comment (belforte, 2023-11-09T22:34:09Z)

I had a look and it seems that `--config` option is on only possible for `submit`
https://github.com/dmwm/CRABClient/blob/0edda22ce9af3ff76a41bc25fecb269762f54a6f/src/python/CRABClient/Commands/submit.py#L178
https://github.com/dmwm/CRABClient/blob/0edda22ce9af3ff76a41bc25fecb269762f54a6f/src/python/CRABClient/ClientUtilities.py#L597-L603
