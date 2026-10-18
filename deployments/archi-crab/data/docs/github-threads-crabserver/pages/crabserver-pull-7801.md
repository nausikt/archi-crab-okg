# dmwm/CRABServer pull request #7801: Fix WebUI to display Rucio URL to the rule

State: closed
Opened: 2023-08-08T13:33:50Z
Closed: 2023-08-08T14:11:32Z
Merged: 2023-08-08T14:11:32Z
URL: https://github.com/dmwm/CRABServer/pull/7801

## Opening post (novicecpp, 2023-08-08T13:33:50Z)

Subtask of https://github.com/dmwm/CRABServer/issues/7797

Now you can click link in "Transfer Info" tab -> "ASO job" column, to go to Rucio Web UI to see the rule status.

![Screenshot from 2023-08-08 15-29-22](https://github.com/dmwm/CRABServer/assets/2346664/ac59f30e-0fc4-4dac-8786-8abfea39c029)

## Comment (cmsdmwmbot, 2023-08-08T13:36:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1645/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-08T13:40:58Z)

Very nice. Thanks !
Only one suggestion:  change column header `ASO Job` to `FTS Job / Rucio Rule`

## Comment (belforte, 2023-08-08T13:43:05Z)

this should also fix https://github.com/dmwm/CRABServer/issues/7421

## Comment (novicecpp, 2023-08-08T13:44:14Z)

> Very nice. Thanks ! Only one suggestion: change column header `ASO Job` to `FTS Job / Rucio Rule`

Actually, I changed it to "ASO job" instead because it is a bit hard to change header of the table dynamically.

## Comment (belforte, 2023-08-08T13:48:32Z)

> Actually, I changed it to "ASO job" instead because it is a bit hard to change header of the table dynamically.

yes, I understand that. I was suggesting to put the both names to mean "it can be either or or the other".  Which one is used will be evident after clicking, unless one has the minimum experience to tell from "job" id format

## Comment (novicecpp, 2023-08-08T13:49:39Z)

Ah. I see. Will fix.

## Comment (cmsdmwmbot, 2023-08-08T13:52:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1646/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-08T13:56:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1647/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-08-08T13:57:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1648/artifact/artifacts/PullRequestReport.html
