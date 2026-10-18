# dmwm/CRABServer pull request #8194: monit - run monit scripts inside docker containers

State: closed
Opened: 2024-01-26T14:57:19Z
Closed: 2024-04-22T13:29:33Z
Merged: 2024-04-22T13:29:33Z
URL: https://github.com/dmwm/CRABServer/pull/8194

## Opening post (mapellidario, 2024-01-26T14:57:19Z)

Related to #6493 

### status

Tested, ready to be reviewed

### Description

The purpose of this PR is to run the scripts GenerateMonit, CheckTapeRecall, aso_metrics_ora and ReportRecallQuota inside docker containers.

- GenerateMonit.py runs inside a crabtaskworker container.
- CheckTapeRecall.py, aso_metrics_ora and ReportRecallQuota runs inside a python:3.8 

design choices:

- run script inside a docker container. The script runs once per `docker run`
- script output:
    - every script has it's own application log, same as before
    - every script prints to stdout. if the script fails, then the stdout is saved in a file in `/tmp/monit-*.txt`
    - [ ] ? shall we get rid of the application log and send everything to stdout? 

next steps

- [x] merge this PR
- [ ] change puppet qa and master so that runcontainer.sh is taken from master branch (not from the branch of this PR)
- [ ] disable scripts on crab-preprod-tw02, enable script on crab-prod-tw02
- [x] disable recurring action [report recall quota](https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/Recurring/ReportRecallQuota.py)

All further information is available in our docs, at:

- https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-opensearch.html
- https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-crontabs.html

## Comment (cmsdmwmbot, 2024-01-26T15:00:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 27 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1805/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-29T11:29:25Z)

Very nice comments Dario. But I fear that they will get lost. Maybe this is something for https://cmscrab.docs.cern.ch/ ? Indeed the Monitoring section in there needs expanding and we lack a "How to develop" which is where advice on e.g. containers should better fit

## Comment (cmsdmwmbot, 2024-01-31T09:46:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 27 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1809/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-01-31T09:55:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1810/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-01-31T09:56:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1811/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-01-31T09:58:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1812/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-01-31T10:16:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1813/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-01T18:44:13Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1819/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-02-01T19:02:13Z)

GenerateMonit is properly running from the crontab inside a docker container [0] on `crab-dev-tw04` and the result looks good [1]

If nobody disagress, on monday I will merge this PR. 

I will make the required changes to run these scripts in "production" on another PR, which will need to be synchronized with changes in puppet.

---

[0] 

```plaintext
# Puppet Name: Send information to elasticsearch MONIT
*/5 * * * * test -f /home/crab3/monit_run-taskworker.sh && bash /home/crab3/monit_run-taskworker.sh >/dev/null 2>&1
```

[1] https://monit-opensearch.cern.ch/dashboards/goto/4e055aa73b4e128250e001d032243334

## Comment (belforte, 2024-02-01T21:05:23Z)

I do not understand why you need a new script instead of creating a new service in runContainer.sh
IIUC the "specialization of the container" is via the tag ( -v option to runContainer.sh)

## Comment (cmsdmwmbot, 2024-02-05T19:33:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 58 comments to review
 * Pycodestyle check: succeeded
   * 92 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1824/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-07T09:53:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 58 comments to review
 * Pycodestyle check: succeeded
   * 92 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1825/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T15:19:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1839/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T17:01:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1840/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T17:17:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1841/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T17:57:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1842/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T18:05:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1843/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-15T18:11:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1844/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T10:47:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1845/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T10:50:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 93 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1846/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T12:03:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 57 comments to review
 * Pycodestyle check: succeeded
   * 92 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1848/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T15:59:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 107 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1849/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T16:02:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 107 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1850/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T16:28:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 107 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1851/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T16:42:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 107 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1852/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T16:58:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1853/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T17:08:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1854/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T17:34:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1855/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-16T18:02:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1856/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T14:30:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1858/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T14:32:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1859/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T14:34:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1860/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T14:45:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1861/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T14:46:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 106 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1862/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:18:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1863/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:20:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1864/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:24:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 64 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1865/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:26:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 64 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1866/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:28:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 10 warnings and errors that must be fixed
   * 64 comments to review
 * Pycodestyle check: succeeded
   * 105 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1867/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T16:51:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1868/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T17:10:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1869/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T23:00:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1870/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-20T23:06:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1871/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-21T13:47:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1872/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-26T15:19:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1875/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-26T15:22:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1876/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-26T15:24:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1877/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-27T09:59:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1878/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-27T10:22:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1879/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-27T12:33:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1880/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-27T12:43:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 66 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1881/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-27T15:37:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1882/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-28T09:55:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1883/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-28T10:04:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 61 comments to review
 * Pycodestyle check: succeeded
   * 108 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1884/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-12T14:11:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1890/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-12T18:12:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1891/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-12T18:12:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1892/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-12T18:21:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1893/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T09:59:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1896/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T10:00:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1897/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T10:04:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1898/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T15:19:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 119 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1900/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:23:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1901/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:26:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1902/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:33:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1903/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:34:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1904/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:41:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1905/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:42:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1906/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-13T16:59:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1907/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-14T09:23:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1908/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-14T09:29:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1909/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-14T10:16:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1910/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-14T10:18:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1911/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T10:41:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1921/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T13:46:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1922/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T16:37:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 72 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1923/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T18:18:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1924/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T18:22:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1925/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-03-28T18:24:31Z)

This PR is ready to be reviewed, all additional information is in our mkdocs. Thanks to everybody for the patience!

## Comment (cmsdmwmbot, 2024-03-28T18:34:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1926/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-03-28T18:35:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1927/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-04-11T17:20:00Z)

I just noticed that this PR supersedes the recurring action defined in https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/Recurring/ReportRecallQuota.py

## Comment (belforte, 2024-04-18T13:28:00Z)

> Quick question: could you please remind me why we have 2 containers?

:open_mouth:  good question, I had not noticed. Hmm.. maybe I did not read carefully. Sorry, so many things.

## Comment (mapellidario, 2024-04-18T14:39:12Z)

@novicecpp

> Quick question: could you please remind me why we have 2 containers?

So, `GenerateMONIT.py` script requires `htcondor` to collect information from the schedulers, such as how many jobs are running or idle, how many task_proc, how many dagmans, etc... So I decided to just use the TW container for that script. 

Since I did not manage to install numpy on the TW container using the spec files, I decided that the other scripts can be run from a plain usual debian python docker container, where we can install what we want, for example numpy and pandas. I did not try to install and setup `htcondor` on this container. At this point I think we can stay with this for a bit, since when we will have the pypi containers, we can switch to those instead and drop these two containers.

## Comment (belforte, 2024-04-18T15:24:39Z)

> Since I did not manage to install numpy on the TW container using the spec files, I decided that the other scripts can be run from a plain usual debian python docker container

Ah.. I remember now. Sorry that I had forgotten.

## Comment (novicecpp, 2024-04-18T15:45:43Z)

Ah, numpy and the RPM....
Thanks. I remember we already had this discussion in Weekly meeting but cannot recall why.

## Comment (cmsdmwmbot, 2024-04-22T13:17:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1951/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-22T13:20:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 124 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1952/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-22T13:29:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 125 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1953/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-22T13:29:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 125 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1954/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-04-22T13:29:19Z)

I cleaned up a bit the dockerfiles and the build scripts. now it is ready to merge. thanks to everybody for the review and for the patience! :)

## Comment (cmsdmwmbot, 2024-04-22T13:29:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1955/artifact/artifacts/PullRequestReport.html
