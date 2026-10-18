# dmwm/CRABServer issue #8910: validate crab resubmit

State: closed
Opened: 2025-01-31T16:35:02Z
Closed: 2025-02-13T00:45:54Z
URL: https://github.com/dmwm/CRABServer/issues/8910

## Opening post (belforte, 2025-01-31T16:35:02Z)

(no text)

## Comment (belforte, 2025-02-03T13:50:33Z)

must make sure that parameter changing in resubmit (time, memory, sites) works

crab resubmit options (from `crab resubmit --help`)
- [x] --jobid=id
- [x] --sitewhitelist=SITEWHITELIST
- [x] --siteblacklist=SITEBLACKLIST
- [x]   --maxjobruntime=MAXJOBRUNTIME
- [x] --maxmemory=MAXMEMORY
- [x] --numcores=NUMCORES
    - looks like it alwasy failed to me ! DagmanResubmitter sets `CRAB_RequestedCpus`, but the PreJob will use `CRAB_RequestedCores` (which is set in DagmanSubmitter) to configure Job.submit.
    - OTOH: do we really want the user to be able to change NUMCORES ?? 
- [x] --priority=PRIORITY  priority of this task compared to other tasks you own; tasks default to 10
- [ ] --force   Force resubmission of successful jobs indicated i  --jobids option. Only works if task is not in  COMPLETED status

we have plan to deprecate the latter one though https://github.com/dmwm/CRABClient/issues/5273#issuecomment-1885195092

## Comment (belforte, 2025-02-12T16:24:28Z)

as a start, list of jobs to be resubmitted is correctly propagated, but sitewhitelist is not.
since I need to fix DagmanResubmitter will take care of this as well
- [x] https://github.com/dmwm/CRABServer/issues/8917

## Comment (belforte, 2025-02-12T20:27:52Z)

above I tested changing the values on individual jobs, i.e. always using `--jobid`.
Let's do again while acting on the whole task. And avoid numcores which I believe we should deprecate.

- [x] --sitewhitelist=SITEWHITELIST
- [x] --siteblacklist=SITEBLACKLIST
- [x]   --maxjobruntime=MAXJOBRUNTIME
- [x] --maxmemory=MAXMEMORY
- [x] --priority=PRIORITY

## Comment (belforte, 2025-02-13T00:45:54Z)

All OK !!!
