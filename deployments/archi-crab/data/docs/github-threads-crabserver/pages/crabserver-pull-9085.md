# dmwm/CRABServer pull request #9085: Remove backward compatibility code in response to new prepare local

State: closed
Opened: 2025-05-20T15:38:30Z
Closed: 2025-06-06T09:07:59Z
Merged: 2025-06-06T09:07:59Z
URL: https://github.com/dmwm/CRABServer/pull/9085

## Opening post (nausikt, 2025-05-20T15:38:30Z)

Resolve #8925

## Comment (cmsdmwmbot, 2025-05-20T15:41:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 63 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2464/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-03T12:31:05Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2487/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-05T09:30:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 80 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2489/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-05T09:47:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 63 comments to review
 * Pycodestyle check: succeeded
   * 81 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2490/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-05T10:23:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 60 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2492/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-06-06T09:05:23Z)

@belforte Thanks to your walkthrough yesterday, I've tested in test14 again both manual submission and via pipelines, as you can see [here](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12174934). Now, there is no bugs left and  i think we good for merging.

## Comment (belforte, 2025-06-06T10:39:37Z)

Generally speaking I think you should wait for the reviewer (me in this case) to do final review and approve before merging.
I do not like that you use `input_param` variable for the arguments passed to the scripts (which in the end is simply `jobId`)  it is confusing given that there is `input_params.json` file which have much more extended information. I can certainly agree that ``opts` was not ideal, but you can surely find a better name.
