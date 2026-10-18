# dmwm/CRABServer pull request #8214: report ReadBranches to crab-test index in MONIT. Fix #7932

State: closed
Opened: 2024-02-01T16:24:27Z
Closed: 2024-02-03T18:21:38Z
Merged: 2024-02-03T18:21:38Z
URL: https://github.com/dmwm/CRABServer/pull/8214

## Opening post (belforte, 2024-02-01T16:24:27Z)

this is for intial testing.
 List of Braches is reported to `crab-test` index via this secret file
```
[crabtw@vocms059 ~]$ pwd
/home/grid/crabtw
[crabtw@vocms059 ~]$ cat MONIT-CRAB.json|jq
{
  "username": "crab-test",
  "password": "PutRealPasswordHere"
}
[crabtw@vocms059 ~]$ 
```

We may want to tune additional metadata sent to OpenSearch (currently username, taskname, inputdataset, datatier) and possibly change where data are sent, so that it can be aggregated with  data from `monit-prod-condor-raw-metric*` to e.g. add CPU usage

## Comment (cmsdmwmbot, 2024-02-01T16:26:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 2 warnings
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 619 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1817/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-01T16:32:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 2 warnings
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 619 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1818/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-01T19:21:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 616 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1820/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-01T19:41:27Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 304 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1821/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-02-02T09:43:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 303 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1822/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-02-02T11:02:43Z)

Jenkins validation:
- [x] #8218
- [x] #8225 
- [x] #8227 
- [x] #8228 
- [x] #8229
