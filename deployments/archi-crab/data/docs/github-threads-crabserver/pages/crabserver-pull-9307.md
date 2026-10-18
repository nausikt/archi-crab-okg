# dmwm/CRABServer pull request #9307: CRAB_Reqname, not ReqName. Anyhow use grep -i. Fix #9306

State: closed
Opened: 2026-04-27T17:08:48Z
Closed: 2026-04-28T09:27:07Z
Merged: 2026-04-28T09:27:06Z
URL: https://github.com/dmwm/CRABServer/pull/9307

## Opening post (belforte, 2026-04-27T17:08:48Z)

(no text)

## Comment (cmsdmwmbot, 2026-04-27T17:11:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2815/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-27T19:52:17Z)

passed minimal validation in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/14634699  I do not think more tests are needed.

With this change job wrapper output has
```
== ENV: FRONTIER_ID=CRAB-260427_172109:crabint1_crab_20260427_192106
```

from `https://cmsweb.cern.ch/scheddmon/059/crabint1/260427_172109:crabint1_crab_20260427_192106/job_out.1.0.txt`

## Comment (belforte, 2026-04-28T09:26:44Z)

thank you Vijay
