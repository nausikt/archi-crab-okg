# dmwm/CRABServer pull request #8536: fix rucio.cfg . Fixes #8535

State: closed
Opened: 2024-06-28T11:13:03Z
Closed: 2024-06-28T11:18:29Z
Merged: 2024-06-28T11:18:29Z
URL: https://github.com/dmwm/CRABServer/pull/8536

## Opening post (belforte, 2024-06-28T11:13:03Z)

(no text)

## Comment (belforte, 2024-06-28T11:13:20Z)

@novicecpp let me know if you see any reason not to do this !

## Comment (novicecpp, 2024-06-28T11:15:10Z)

No no. At the time I started dev pypi container, my cvmfs local setup was not stable and needed to restart one or two times A DAY! 
It was so frustrating.

## Comment (belforte, 2024-06-28T11:18:22Z)

indeed we do not use cvmfs anymore for this now ! with updating puppet manifests for alma9 we got automatic maintenance of things in local /etc/grid-security in the VM

## Comment (cmsdmwmbot, 2024-06-28T11:18:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2040/artifact/artifacts/PullRequestReport.html
