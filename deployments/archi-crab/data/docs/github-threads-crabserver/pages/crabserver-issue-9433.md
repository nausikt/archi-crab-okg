# dmwm/CRABServer issue #9433: wrong syntax for schedd.edit

State: closed
Opened: 2026-10-05T10:32:30Z
Closed: 2026-10-05T10:40:47Z
Labels: Type: Bug, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9433

## Opening post (belforte, 2026-10-05T10:32:30Z)

this line introduced in recent commit  https://github.com/dmwm/CRABServer/commit/3f81a5df4ea38a8cde1cf9cee609155ef5c5ee3c  is wrong
https://github.com/dmwm/CRABServer/blob/0808d5189d965d278afe676041da375783385fd3/src/python/TaskWorker/Actions/DagmanKiller.py#L91

the argument to classad.quote must be a string !

see https://cms-talk.web.cern.ch/t/crab-killfailed-blocks-exact-input-recovery-luobing-reco-task260930-003216/148896

## Comment (belforte, 2026-10-05T10:38:54Z)

anyhow there's no reason to call classad.quote() here, passing a string will do.
