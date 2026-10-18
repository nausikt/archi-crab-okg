# dmwm/CRABServer issue #8578: enable FTS Reuse for FTS_ASO

State: closed
Opened: 2024-08-02T08:25:03Z
Closed: 2025-02-27T09:07:12Z
Labels: Status: Done, Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8578

## Opening post (belforte, 2024-08-02T08:25:03Z)

re-reading
https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC2776329

it looks like we want to set `reuse=True` in
https://github.com/dmwm/CRABServer/blob/e6227eed00e1e3a6e5bd9ec33d6db352173455d0/scripts/task_process/FTS_Transfers.py#L351

Somehow when reinstalling all schedd's via puppet the `/etc/use_fts_reuse` file got lost and I did not notice. We had waited too long to turn this from "experimental" to "permanent" and the file was there only as a consequence of explicit `touch` 3 years ago.

cleanup will be needed in
https://github.com/dmwm/CRABServer/blob/e6227eed00e1e3a6e5bd9ec33d6db352173455d0/scripts/task_process/FTS_Transfers.py#L86
https://github.com/dmwm/CRABServer/blob/e6227eed00e1e3a6e5bd9ec33d6db352173455d0/scripts/task_process/FTS_Transfers.py#L480
and
https://github.com/dmwm/CRABServer/blob/e6227eed00e1e3a6e5bd9ec33d6db352173455d0/scripts/dag_bootstrap_startup.sh#L173-L180

## Comment (belforte, 2024-08-02T08:26:18Z)

Of course we need to use current mechanism to enable Reuse on a couple of schedd's for a month or so before switching everything.

## Comment (belforte, 2024-08-02T08:30:25Z)

I have enabled FTS_REUSE on
* vocms059
* vocms0106
* vocms0107

```text

belforte@aiadm43/~> wassh -c vocmsglidein/crabsched ls /etc/use_fts_reuse
crab-preprod-scd03.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
crab-sched-901.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
crab-sched-903.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0106.cern.ch: /etc/use_fts_reuse
vocms0107.cern.ch: /etc/use_fts_reuse
vocms0119.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0120.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0121.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0122.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0137.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0144.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0155.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0194.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0195.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0196.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0197.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0198.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0199.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms059.cern.ch: /etc/use_fts_reuse
vocms068.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms069.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
belforte@aiadm43/~> 
```

## Comment (belforte, 2024-09-23T21:28:01Z)

no problems. Time to remove the Hold

## Comment (belforte, 2024-09-23T21:33:47Z)

as a start, create `/etc/use_fts_reuse` on 6 more schedulers
```console
belforte@aiadm81/~> wassh -c vocmsglidein/crabsched ls /etc/use_fts_reuse
crab-preprod-scd03.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
crab-sched-901.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
crab-sched-903.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0106.cern.ch: /etc/use_fts_reuse
vocms0107.cern.ch: /etc/use_fts_reuse
vocms0119.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0120.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0121.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0122.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0137.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0144.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0155.cern.ch: ls: cannot access '/etc/use_fts_reuse': No such file or directory
vocms0194.cern.ch: /etc/use_fts_reuse
vocms0195.cern.ch: /etc/use_fts_reuse
vocms0196.cern.ch: /etc/use_fts_reuse
vocms0197.cern.ch: /etc/use_fts_reuse
vocms0198.cern.ch: /etc/use_fts_reuse
vocms0199.cern.ch: /etc/use_fts_reuse
vocms059.cern.ch: /etc/use_fts_reuse
```

## Comment (belforte, 2025-02-27T09:03:40Z)

Just created on remaining schedulers, now is done everywhere
```console
belforte@aiadm99/~> wassh -c vocmsglidein/crabsched ls /etc/use_fts_reuse
crab-preprod-scd03.cern.ch: /etc/use_fts_reuse
crab-sched-901.cern.ch: /etc/use_fts_reuse
crab-sched-903.cern.ch: /etc/use_fts_reuse
vocms0106.cern.ch: /etc/use_fts_reuse
vocms0107.cern.ch: /etc/use_fts_reuse
vocms0119.cern.ch: /etc/use_fts_reuse
vocms0120.cern.ch: /etc/use_fts_reuse
vocms0121.cern.ch: /etc/use_fts_reuse
vocms0122.cern.ch: /etc/use_fts_reuse
vocms0137.cern.ch: /etc/use_fts_reuse
vocms0144.cern.ch: /etc/use_fts_reuse
vocms0155.cern.ch: /etc/use_fts_reuse
vocms0194.cern.ch: /etc/use_fts_reuse
vocms0195.cern.ch: /etc/use_fts_reuse
vocms0196.cern.ch: /etc/use_fts_reuse
vocms0197.cern.ch: /etc/use_fts_reuse
vocms0198.cern.ch: /etc/use_fts_reuse
vocms0199.cern.ch: /etc/use_fts_reuse
vocms059.cern.ch: /etc/use_fts_reuse
vocms068.cern.ch: /etc/use_fts_reuse
vocms069.cern.ch: /etc/use_fts_reuse
belforte@aiadm99/~> 
```

## Comment (belforte, 2025-02-27T09:07:02Z)

Next will be to remove the "if" from the code and simply do it #8952
