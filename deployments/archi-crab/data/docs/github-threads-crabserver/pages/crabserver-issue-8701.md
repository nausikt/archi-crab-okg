# dmwm/CRABServer issue #8701: Release pipeline broken without anybody notice

State: closed
Opened: 2024-09-19T21:43:48Z
Closed: 2024-12-12T10:08:49Z
Labels: Type: Bug, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8701

## Opening post (novicecpp, 2024-09-19T21:43:48Z)

The [release pipeline of v3.240904](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/8057298) is broken, all jobs complete except last job that tagging crabtwmonit image to release tag (which cause by a bug in CI config but that separate issue).
Nobody noticed it, including me, who received the mail, thought that it was my "usual broken" dev pipeline

This cause monitoring cron to fail because image not found.

This happened today after we merge puppet qa to master which contains bump cron image verison to `v3.240904-stable`.

## Comment (novicecpp, 2024-09-19T21:46:39Z)

~~Self-reminder: fix the pipeline before doing anything tomorrow.~~ 
DONE

## Comment (belforte, 2024-09-20T09:47:14Z)

we got "No Data" alert in MatterMost. NObody noticed :-(

## Comment (belforte, 2024-12-12T10:08:49Z)

I believe that this was fixed.
