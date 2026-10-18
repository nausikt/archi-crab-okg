# dmwm/CRABServer pull request #7519: use WMCore 2.1.6

State: closed
Opened: 2023-02-02T15:29:38Z
Closed: 2023-02-07T12:58:23Z
URL: https://github.com/dmwm/CRABServer/pull/7519

## Opening post (belforte, 2023-02-02T15:29:38Z)

(no text)

## Comment (cmsdmwmbot, 2023-02-02T15:33:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1408/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-02-02T15:38:14Z)

Could you bump to version `2.1.7rc3`? It contain the change I need for deprecating CephFS.
Issue: https://github.com/dmwm/WMCore/issues/11459, PR: https://github.com/dmwm/WMCore/pull/11463

## Comment (novicecpp, 2023-02-02T15:43:48Z)

Sorry, I can do it myself later with my on hold PR https://github.com/dmwm/CRABServer/pull/7496

## Comment (belforte, 2023-02-02T15:57:48Z)

sure, whatever comes easier

## Comment (novicecpp, 2023-02-07T10:59:13Z)

I have merged https://github.com/dmwm/CRABServer/pull/7496 to master.
Shall we close this?

## Comment (cmsdmwmbot, 2023-02-07T11:05:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1413/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-07T12:58:23Z)

yes, we can close.
