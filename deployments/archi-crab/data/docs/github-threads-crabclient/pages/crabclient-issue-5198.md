# dmwm/CRABClient issue #5198: allow a user to add their own tarfile to the sandox

State: closed
Opened: 2023-05-15T15:19:00Z
Closed: 2023-06-12T11:35:07Z
Labels: HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5198

## Opening post (belforte, 2023-05-15T15:19:00Z)

i.e. make sure that such tar is expanded on the WN
e,g. look for files whose name contains `.tar.` or ends with `.tar` or `.tgz` or `.tbz`

see https://cms-talk.web.cern.ch/t/sandbox-questions/24063/2

## Comment (kpedro88, 2023-05-15T16:08:13Z)

A thought: some people name their tar files as `.tgz`, so probably check for that one, too.

## Comment (belforte, 2023-06-12T11:35:07Z)

there is nothing to change in Client, this is simply a matter of calling `tar` in the job wrapper. Will open issue in crabserver repo
