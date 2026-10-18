# dmwm/CRABServer pull request #7604: Jobwrapper - fix elapsed time computation

State: closed
Opened: 2023-04-19T10:02:46Z
Closed: 2023-04-19T11:34:24Z
Merged: 2023-04-19T11:34:24Z
URL: https://github.com/dmwm/CRABServer/pull/7604

## Opening post (mapellidario, 2023-04-19T10:02:46Z)

Fixes #7602 
Fixes #7586 

### status

ready to merge, tested on test11:

- [x] https://cmsweb-test11.cern.ch/crabserver/ui/task/230419_094216%3Admapelli_crab_elapsed_20230419_114211

### description

Thank you both @belforte and @mmascher for having a look. I leaked a variable from WMCore indeed, there is no need for setting the start time in `submit_env.sh`.

For some obscure reason I have not been able to replicate the problem on my test environment, but since you found the culprit I will not give insist on it.

## Comment (cmsdmwmbot, 2023-04-19T10:07:29Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1496/artifact/artifacts/PullRequestReport.html
