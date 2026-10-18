# dmwm/CRABServer pull request #7868: Bump crabtaskworker baseimage to 20230427-stable

State: closed
Opened: 2023-09-12T08:42:34Z
Closed: 2023-09-12T09:13:15Z
Merged: 2023-09-12T09:13:15Z
URL: https://github.com/dmwm/CRABServer/pull/7868

## Opening post (novicecpp, 2023-09-12T08:42:34Z)

Current baseimage is failed to build because snapshot of epel repo is gone, thus make `yum` command fail.
 https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_BuildImage/107/console

Current oldest of snapshot is [2022-03-11](http://linuxsoft.cern.ch/internal/yumsnapshot/) but our image is pinned on 2022-03-01.

I also expose  `CI_CRABSERVER_REPO`, `CI_CRABSERVER_BRANCH` from jenkins_build_docker.sh script to test it locally.

## Comment (cmsdmwmbot, 2023-09-12T08:45:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1696/artifact/artifacts/PullRequestReport.html
