# dmwm/CRABServer pull request #8348: Fix deployTW.sh script, fix CI job tags to crab3 and crab3-shell

State: closed
Opened: 2024-04-22T17:00:42Z
Closed: 2024-04-23T11:59:25Z
Merged: 2024-04-23T11:59:25Z
URL: https://github.com/dmwm/CRABServer/pull/8348

## Opening post (novicecpp, 2024-04-22T17:00:42Z)

`deployTW.sh`  need to provide command to `runContainer.sh` to start application in container.
(and thank Dario for make a change to support custom command). 

Also fix CI job tag. Default tag is now `crab3` to run job in docker, and use `crab3-shell` to run job where apptainer is required.

## Comment (cmsdmwmbot, 2024-04-22T17:03:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1956/artifact/artifacts/PullRequestReport.html
