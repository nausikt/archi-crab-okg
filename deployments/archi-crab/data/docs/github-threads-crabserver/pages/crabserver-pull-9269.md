# dmwm/CRABServer pull request #9269: remove LDAP dependency

State: closed
Opened: 2026-01-30T11:13:13Z
Closed: 2026-01-30T13:05:32Z
Merged: 2026-01-30T13:05:32Z
URL: https://github.com/dmwm/CRABServer/pull/9269

## Opening post (belforte, 2026-01-30T11:13:13Z)

(no text)

## Comment (cmsdmwmbot, 2026-01-30T11:18:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2734/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-01-30T11:27:00Z)

test pipeline: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13917614

## Comment (belforte, 2026-01-30T13:05:14Z)

thanks @nausikt for super-fast review ! Pylint complaints about CMSGroupMapper will likely go away when addressing #9270 
Indeed CRIC API is extra-stable at this point.
