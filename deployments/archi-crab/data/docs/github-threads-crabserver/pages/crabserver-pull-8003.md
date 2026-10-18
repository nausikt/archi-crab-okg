# dmwm/CRABServer pull request #8003: StageoutCheck use privilege Rucio account

State: closed
Opened: 2023-11-15T17:23:33Z
Closed: 2023-11-22T15:27:21Z
Merged: 2023-11-22T15:27:21Z
URL: https://github.com/dmwm/CRABServer/pull/8003

## Opening post (novicecpp, 2023-11-15T17:23:33Z)

Workaround on the [permission issue in CMSRucio](https://mattermost.web.cern.ch/cms-o-and-c/pl/ej7zwkr747rifezzcyyweisx9r) where `get_local_account_usage()` still need a privilege account.
It is pretty safe to pass `privilegedRucioClient` to the whole `StageoutCheck` class because it only uses read-only APIs.

## Comment (cmsdmwmbot, 2023-11-15T17:29:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 1 warnings
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1758/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-20T09:50:29Z)

very good, thanks

## Comment (belforte, 2023-11-20T09:52:05Z)

please fix the Pylint warnings in bold.

## Comment (cmsdmwmbot, 2023-11-22T15:24:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1767/artifact/artifacts/PullRequestReport.html
