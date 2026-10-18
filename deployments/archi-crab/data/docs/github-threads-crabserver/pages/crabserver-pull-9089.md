# dmwm/CRABServer pull request #9089: Handle kill in rucio aso 8429

State: closed
Opened: 2025-05-22T08:06:21Z
Closed: 2025-05-26T14:18:53Z
Merged: 2025-05-26T14:18:52Z
URL: https://github.com/dmwm/CRABServer/pull/9089

## Opening post (belforte, 2025-05-22T08:06:21Z)

Fixes #8429 via closing dataset if overallDagStatus is final  and a these connected sub-issues
-  do not timeout PostJob when using Rucio. Fix #9078
- Remove DAGs after TASKLIFETIME. Fix #9077

## Comment (cmsdmwmbot, 2025-05-22T08:09:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2466/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-23T10:50:21Z)

thanks for pointing out the redundant lines. I will do.

But I fail to understand the `bitwise OR` ! Do you refer to this line ?
`shouldClose |= (statusCache['overallDagStatus'] in ['COMPLETED', 'FAILED'])`
In my humble understanding that's an OR of booleans, and I am not really settled in my mind if a 
`shouldClose = shouldClose | ...` wouldn't be better

## Comment (aspiringmind-code, 2025-05-23T11:02:30Z)

Yes referring to those lines. I think it is called a bitwise OR assignment. I prefer the shorthand usage instead of writing shouldClose twice..

## Comment (cmsdmwmbot, 2025-05-23T12:20:29Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 167 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2481/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-26T13:45:39Z)

I have tested this as much as I could . Do you want to review more @aspiringmind-code ? Or may I merge ?

I am still willing to go through the code in a chat and explain what I did, if you would like to.

## Comment (aspiringmind-code, 2025-05-26T13:50:18Z)

Please feel free to merge. Looks good to me. Yes to the chat on Wednesday after meeting.
