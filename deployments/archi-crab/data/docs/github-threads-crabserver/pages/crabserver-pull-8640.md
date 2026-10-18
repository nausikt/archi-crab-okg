# dmwm/CRABServer pull request #8640: monit - set CMD to bash

State: closed
Opened: 2024-08-21T14:14:20Z
Closed: 2024-08-22T14:39:01Z
Merged: 2024-08-22T14:39:01Z
URL: https://github.com/dmwm/CRABServer/pull/8640

## Opening post (mapellidario, 2024-08-21T14:14:20Z)

Quality of life for crab developers: whit this PR it is possible to run a monit container interactively with

```bash
./runContainer.sh -v v3.latest.monit -s TaskWorker_monit
```

and then connect to it with

```bash
docker exec -it TaskWorker_monit bash
```

## Comment (mapellidario, 2024-08-21T14:15:08Z)

this is currently set up in crab-dev-tw02 for you to try, I built and tagged this image with `v3.latest.monit`

## Comment (cmsdmwmbot, 2024-08-21T14:17:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2117/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-21T15:18:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2119/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-22T06:36:13Z)

thanks Dario

## Comment (cmsdmwmbot, 2024-08-22T14:43:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2120/artifact/artifacts/PullRequestReport.html
