# dmwm/CRABServer pull request #7572: jobwrapper - added cmscp.sh

State: closed
Opened: 2023-03-22T12:55:38Z
Closed: 2023-03-29T10:24:47Z
Merged: 2023-03-29T10:24:47Z
URL: https://github.com/dmwm/CRABServer/pull/7572

## Opening post (mapellidario, 2023-03-22T12:55:38Z)

### status

- [x] tested on test11: https://cmsweb-test11.cern.ch/crabserver/ui/task/230322_124355:dmapelli_crab_jobwr4_20230322_134354

ready to merge. no change on the crabclient is needed.

### description

I decided that I will open multiple PRs with the changes that I am making to the jowr, so that it will be easier to review and manage.

This is the first one and focuses on executing `cmscp.py` inside its own script, `cmscp.sh`, so that we always use only the gwms container environment in gWMS-CMSRunAnalysis.sh.

## Comment (cmsdmwmbot, 2023-03-22T12:58:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 3 warnings
   * 143 comments to review
 * Pycodestyle check: succeeded
   * 169 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1469/artifact/artifacts/PullRequestReport.html
