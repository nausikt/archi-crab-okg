# dmwm/CRABServer pull request #8414: Reduce bind mount to single path for apps data

State: closed
Opened: 2024-05-16T14:12:25Z
Closed: 2024-05-17T08:41:35Z
Merged: 2024-05-17T08:41:35Z
URL: https://github.com/dmwm/CRABServer/pull/8414

## Opening post (novicecpp, 2024-05-16T14:12:25Z)

Fix https://github.com/dmwm/CRABServer/issues/8402

This also requires a change in the [run.sh](https://github.com/dmwm/CRABServer/blob/5572f119fa4a76f20ef85628744cabc4bad02089/Docker/run.sh) of crabtaskworker's RPM image in order to use the new bindmount's scheme.

runContainer.sh from this PR is backward compatibility with old RPM images; it is capable of deploying old, new, or pypi images without updating the configuration. Revert the [04ad23a6673b333fd188f948ef88f353ce772c61](https://github.com/dmwm/CRABServer/commit/04ad23a6673b333fd188f948ef88f353ce772c61) change to clean up, later.

## Comment (cmsdmwmbot, 2024-05-16T14:14:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1990/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-16T16:04:52Z)

LGTM. Thanks @novicecpp
