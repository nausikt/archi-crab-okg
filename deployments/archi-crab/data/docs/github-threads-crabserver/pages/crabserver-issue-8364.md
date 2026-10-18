# dmwm/CRABServer issue #8364: WEB_DIRs in schedd are not cleaned timely

State: closed
Opened: 2024-04-26T16:38:21Z
Closed: 2024-04-26T16:57:09Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8364

## Opening post (belforte, 2024-04-26T16:38:21Z)

in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/files/crabschedd/JobCleanup.py?ref_type=heads#L56
```python
    homeDir="/home/grid/%s/%s"%(crabDag.task["Owner"], crabDag.task["Crab_ReqName"])
```

But now all tasks run with `Owner = crabtw` !! So that variable always points to non-existing directory names and all WEB_DIRs are only catched by the fall-back `cleanup_home_dir.sh` after 60 days.

Need to change to

```python
    homeDir="/home/grid/%s/%s"%(crabDag.task["CRAB_UserHN"], crabDag.task["Crab_ReqName"])
```

## Comment (belforte, 2024-04-26T16:57:09Z)

fixed via https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/176
