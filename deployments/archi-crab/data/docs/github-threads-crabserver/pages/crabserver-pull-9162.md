# dmwm/CRABServer pull request #9162: Resubmit refactor

State: closed
Opened: 2025-08-26T11:49:44Z
Closed: 2025-11-17T14:33:42Z
URL: https://github.com/dmwm/CRABServer/pull/9162

## Opening post (aspiringmind-code, 2025-08-26T11:49:44Z)

#6270 
Preliminary draft changes to refactor resubmit. @belforte Please go through these changes and let me know if I am on the right track. Valuable comments and suggestions are welcome. At least I'd like to be sure that these are the only places we need to make changes.
Question: Why do we need to signal the jobs as "failed" and not held?
Automatic Splitting not figured out.

## Comment (cmsdmwmbot, 2025-08-26T11:55:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 479 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2584/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-26T11:56:53Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 477 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2585/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-26T13:10:07Z)

>  Question: Why do we need to signal the jobs as "failed" and not held?

That's for crab status. So not to confuse users who are used to see "failed". Jobs fail before becoming held. So in our code held is more proper.

## Comment (belforte, 2025-08-27T10:35:59Z)

Thanks @aspiringmind-code  looks very good to me so far !
You surely are on the right track !

## Comment (aspiringmind-code, 2025-08-28T09:06:06Z)

Thanks for the valuable insights. I will start incorporating the changes and then testing.

## Comment (cmsdmwmbot, 2025-09-01T08:04:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 477 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2588/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-01T13:10:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 477 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2589/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-02T09:52:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 477 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2593/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-02T13:48:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 544 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2594/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-02T14:24:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 543 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2595/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-05T09:32:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 113 comments to review
 * Pycodestyle check: succeeded
   * 543 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2605/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-05T11:33:41Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 589 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2606/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-05T15:18:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2607/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T08:32:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2608/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T09:33:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2611/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-08T10:24:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2612/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-09T08:53:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2620/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-09T11:33:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2621/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-15T11:50:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2627/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-15T11:52:12Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2628/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-15T13:44:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2629/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-16T21:55:17Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2630/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-23T09:41:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 579 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2632/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-28T03:23:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 575 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2638/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-28T04:00:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 575 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2639/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-29T03:45:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 580 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2640/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-29T06:08:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 582 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2641/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-29T07:39:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 119 comments to review
 * Pycodestyle check: succeeded
   * 583 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2642/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-09-29T09:00:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 582 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2643/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-10-06T06:09:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 118 comments to review
 * Pycodestyle check: succeeded
   * 582 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2649/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-11-17T14:20:20Z)

@aspiringmind-code I guess this can be closed, right ?

## Comment (aspiringmind-code, 2025-11-17T14:33:42Z)

Yes, closing. Thanks!
