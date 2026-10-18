# dmwm/CRABClient pull request #5241: Add change dbs dataset file status fix #5204

State: closed
Opened: 2023-10-25T16:36:53Z
Closed: 2023-10-27T19:54:18Z
Merged: 2023-10-27T19:54:18Z
URL: https://github.com/dmwm/CRABClient/pull/5241

## Opening post (belforte, 2023-10-25T16:36:53Z)

I think this is OK now. Aside from
* setfilestatus does not work with a list of files. Valentin acknowledged a bug but it is for others to fix. We can live w/o it for quite some time
* tune/polish help (remove single char commands ? now that we have autocompletion...)
* whatever @novicecpp and @mapellidario suggest

## Comment (belforte, 2023-10-25T16:38:30Z)

I did a quick test on CMSSW_9 on lxplus7 (python2) and it is OK. Once have test in Jenkins will run all archs
and of  course I need to  make sure I did not break anything !

## Comment (cmsdmwmbot, 2023-10-25T16:41:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 407 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/968/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T18:11:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 396 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/969/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-25T20:49:08Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 42 comments to review
 * Pycodestyle check: succeeded
   * 395 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/970/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-26T12:42:41Z)

thanks a lot @novicecpp 
I have a question for you now: would it then be better to also move HTTPRequests to ClientUtilities ? Since it is not used by CRABRest only.

## Comment (belforte, 2023-10-26T12:45:50Z)

I merged [my branch](https://github.com/belforte/CRABClient/tree/add-change-DBS-dataset-file-status-fix-5204) with master dmwm repo  in [test-setdatasetfilesstatus branch](https://github.com/dmwm/CRABClient/tree/test-setdatasetfilesstatus) tagged as [testSetDsetFilesStatus.1](https://github.com/dmwm/CRABClient/releases/tag/testSetDsetFilesStatus.1) and ran Jenkins CV to check for regression
* https://github.com/dmwm/CRABServer/issues/7977
* https://github.com/dmwm/CRABServer/issues/7978
* https://github.com/dmwm/CRABServer/issues/7979
* https://github.com/dmwm/CRABServer/issues/7980
* https://github.com/dmwm/CRABServer/issues/7981

All OK !

## Comment (belforte, 2023-10-26T12:52:22Z)

@novicecpp I captured your comments before in [this](https://github.com/dmwm/CRABClient/issues/5204#issuecomment-1781051917) list of actions. I will add more as needed once you answer my questions. Feel free to check and comment in there. Thanks

## Comment (novicecpp, 2023-10-26T13:39:55Z)

> I have a question for you now: would it then be better to also move HTTPRequests to ClientUtilities ? Since it is not used by CRABRest only.

Maybe move HTTPRequests to utils and move DBSREST to new file same level as CrabRestInterface.py?

## Comment (cmsdmwmbot, 2023-10-26T20:35:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 10 warnings
   * 259 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/972/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-26T20:43:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/973/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-26T20:44:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/974/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-26T21:15:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/975/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-26T21:37:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/976/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-26T21:38:36Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/977/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-26T21:48:01Z)

Hope I addressed all coments (only the `uri` vs. `api` confusion is left, but I think it is too much work). Will run Jenkins again.
New code tagged as  [testSetDsetFilesStatus.2](https://github.com/dmwm/CRABClient/releases/tag/testSetDsetFilesStatus.2)
Jenkinks OK
 * https://github.com/dmwm/CRABServer/issues/7982
 * https://github.com/dmwm/CRABServer/issues/7983
 * https://github.com/dmwm/CRABServer/issues/7984
 * https://github.com/dmwm/CRABServer/issues/7985

## Comment (cmsdmwmbot, 2023-10-26T21:49:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 10 warnings
   * 260 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/978/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-26T22:32:40Z)

code with last changes is now tagged as [testSetDsetFilesStatus.2](https://github.com/dmwm/CRABClient/releases/tag/testSetDsetFilesStatus.2) in the ad-hoc test branch

## Comment (cmsdmwmbot, 2023-10-26T23:04:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 23 warnings and errors that must be fixed
   * 9 warnings
   * 246 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/982/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-26T23:27:11Z)

ooopppss. I had added content-type in the wrong place. But of course CRAB Server REST happily ignores it and everything kept working, but better not confuse the reader.

## Comment (belforte, 2023-10-26T23:28:00Z)

If there are no more objection I will do a BIG SQUASH and merge.

## Comment (cmsdmwmbot, 2023-10-27T12:58:16Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 23 warnings and errors that must be fixed
   * 9 warnings
   * 246 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/983/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-27T13:54:57Z)

thanks @mapellidario and @novicecpp for review and advice. I will merge. And we can discuss separately if/how to add --recursive. Maybe wait for someone to ask for it :grin: ?

We still have time to decide if to keep old semantic (Invalidating a dataset will automatically invalidate all the files in the dataset) or leave it to user with two actions as I indicated above. It seems a soft decisions, with arguments in pro/con either choice.

## Comment (belforte, 2023-10-27T13:55:46Z)

Since in current implementation `crab setdatasetstatus` does not change status of individual files, I will print a note about this when the command is executed !

## Comment (mapellidario, 2023-10-27T14:19:38Z)

Thanks Stefano for the detailed description of dataset and file validity in DBS. Sorry for the dumb questions! 

Do we already have an entry in the FAQs about DBS dataset and file status? Since we are allowing users to change it, we should also provide clear instructions about what those are and what the commands we provide do (or plan to do).

## Comment (belforte, 2023-10-27T14:35:21Z)

Dario,your questions were not dumb. The problem is that there is no real rule on how to use those status flags,
DBS allows to set, then everybody can do as they see fit. I think Production changed their practice over time.

As user documentation  this is what we have:
  https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Can_I_delete_a_dataset_I_publish
it clearly needs a rewriting ! That is my next step.

## Comment (cmsdmwmbot, 2023-10-27T19:34:11Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 23 warnings and errors that must be fixed
   * 9 warnings
   * 246 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/984/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-27T19:37:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 23 warnings and errors that must be fixed
   * 9 warnings
   * 246 comments to review
 * Pycodestyle check: succeeded
   * 666 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/985/artifact/artifacts/PullRequestReport.html
