# dmwm/CRABClient issue #5332: reorganize sandbox structure

State: closed
Opened: 2024-09-20T10:49:19Z
Closed: 2024-09-20T16:18:33Z
Labels: enhancement, Done
URL: https://github.com/dmwm/CRABClient/issues/5332

## Opening post (belforte, 2024-09-20T10:49:19Z)

currently it has flatly at same level
- files from $CMSSW_BASE which need to be restored in there in the WN
- PSet* files which need to go in the cwd directory of the running job (`/srv`)
- user's `jobType.inputFiles` which need to go in `/srv`as well

Should change to a structure which allows a single `tar` command to put everything in its place in the WN
```
.
|-- CMSSW_13_3
|   |-- biglib
|   |-- bin
|   |-- cfipython
|   |-- config
|   |-- external
|   |-- lib
|   |-- python
|   |-- src
|   `-- venv
|-- PSet.pkl
|-- PSet.py
|-- PSetDump.py
|-- userInputFile-1
|-- userInputFile-2
`-- userInputTar

```

## Comment (belforte, 2024-09-20T10:50:09Z)

reference: https://github.com/dmwm/CRABServer/issues/7705
