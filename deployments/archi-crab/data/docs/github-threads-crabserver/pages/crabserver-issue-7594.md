# dmwm/CRABServer issue #7594: implement `crab recall`

State: open
Opened: 2023-04-14T07:48:12Z
Labels: Type: Enhancement, Type: Question, Priority: Medium, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/7594

## Opening post (belforte, 2023-04-14T07:48:12Z)

develop a way for users to request recalls w/o submitting a task, also includes the possibility to simply request a replica (maybe not `crab recall`, but `crab getdata` ?
```
crab recall --dataset=.... --sites=... --days=...
```
Requires change also in CRABClient

Should use different Rucio account than for automatic tape recalls (`crab_tape_recall`) so that we can set different global/local quotas.
Will also need a different set of policies.

## Comment (belforte, 2023-09-14T15:54:35Z)

we have been discussing this for months now. It is technically straightforward especially after last refactoring of tape recall code in TaskWorker/RucioActions .
But  still not clear what exactly the need is.
 * We can surely provide a “crab recall” by which does the same as automatic recall but w/o submitting a task.
 * Is it worth ? useful ?
 * Doing more is easy technically, problem is which policies to enforce.
 * We nee DM Ops buying in and setting of proper policies.
 * Once we give such a tool to every user, the problem is when to say no.

There's also an evolution of DM policies about what to keep on disk anyhow, geared for Run3 in https://its.cern.ch/jira/browse/CMSTRANSF-687
Maybe we can simply wait for that to be finalized and listen to users.

## Comment (belforte, 2023-09-14T15:57:02Z)

technical detail: my current idea is to create an entry in CRAB's TaskDB like submit does, but with a different command (RECALL), when TW Handler finds, it will call a new "recall" action. I think about a solid week of work.
