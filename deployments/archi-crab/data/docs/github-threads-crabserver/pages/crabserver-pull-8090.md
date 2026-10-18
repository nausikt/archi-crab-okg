# dmwm/CRABServer pull request #8090: send diagnostic info to user when splitting fails. Fix #8002

State: closed
Opened: 2023-12-08T16:52:15Z
Closed: 2023-12-14T15:35:02Z
Merged: 2023-12-14T15:35:02Z
URL: https://github.com/dmwm/CRABServer/pull/8090

## Opening post (belforte, 2023-12-08T16:52:15Z)

with this PR, a task submission where "CRAB could not submit any job" results in a message like this
```
Failure message from server:	CRAB could not submit any job to the Grid scheduler:
				splitting task 231208_164915:belforte_crab_20231208_174911
				on dataset /SingleMuon/Run2018D-UL2018_MiniAODv2_GT36-v2/MINIAOD
				with FileBased method does not generate any job. See
				https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Splitting
				Some hopefully helpful information to help you figure out the reason:
				Run list from task configuration is inside the range: 0 - 0
				Run list from input dataset is inside the range: 320500 - 325175
				The intersection of the two lists is: []
```

I tried to print the full run lists instead of the range limits, but the message immediately goes over the 1K char limit.

## Comment (cmsdmwmbot, 2023-12-08T16:54:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1780/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-12-08T17:06:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 2 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1781/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-12-08T17:07:32Z)

Quick question. Would it make sense to put the full diagnosis in the tw logs? We would not be constrained by the 1k character limit, but in case a user ask we would have the answer at hand in the logs

## Comment (belforte, 2023-12-08T17:14:58Z)

I'd like to see first a use case where the simple test there is not enough.  So far we got along with "check your lumimask!!"

Printing very long lists is hardly useful in the end. Can't used "by eye" and we'd have to write code to do the parsing and matching.
