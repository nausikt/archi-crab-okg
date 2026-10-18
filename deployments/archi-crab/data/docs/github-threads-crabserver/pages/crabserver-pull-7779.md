# dmwm/CRABServer pull request #7779: TW - set job classads to match arch in first and second matchmaking

State: closed
Opened: 2023-07-19T12:10:58Z
Closed: 2023-07-20T15:40:06Z
Merged: 2023-07-20T15:40:06Z
URL: https://github.com/dmwm/CRABServer/pull/7779

## Opening post (mapellidario, 2023-07-19T12:10:58Z)

Related to #7208 

### Status

tested, to the best of our knowledge so far

- when submitting from lxplus-arm (crab client scram_arch is aarch64), the TW generated jobs with the proper classads. so TW is ok
- however, no arm resource are available in the itb and global pool, so we could make sure that they actually work

### Details

Changes to TW, so that the resulting jobs have the proper classads to match the arch in first and second matchmaking.

## Comment (cmsdmwmbot, 2023-07-19T12:13:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 3 warnings
   * 124 comments to review
 * Pycodestyle check: succeeded
   * 127 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1623/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-19T12:39:27Z)

looks good. Please look into the comment above about odd syntax for `msg`
Please also remove at least "12 warnings and errors that must be fixed" from pylint.
The undefined variable is worrying. But I have not looked at what's happening there.

## Comment (mapellidario, 2023-07-19T18:34:14Z)

I added two commits. one fixes the bug related to "item" not been defined and added a comments about the regex, the second replaces `.format()` with and fstring and pleases pylint.

## Comment (cmsdmwmbot, 2023-07-19T18:37:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 3 warnings
   * 124 comments to review
 * Pycodestyle check: succeeded
   * 128 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1624/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-07-20T08:28:31Z)

Thanks stefano! It should be better now

(i eventually installed pylint on my system, not to miss bad errors again!)

## Comment (cmsdmwmbot, 2023-07-20T08:30:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 3 warnings
   * 124 comments to review
 * Pycodestyle check: succeeded
   * 128 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1627/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-20T08:39:10Z)

> (i eventually installed pylint on my system, not to miss bad errors again!)

+1
that helps for sure, even before committing to your branch
But maybe we can also find a a way to run Jenkins w/o a PR to master ?

## Comment (belforte, 2023-07-20T08:41:31Z)

can you kindly take care of this as well ?

 W0707, line 1195 in DagmanCreator.executeInternal: Consider explicitly re-raising using the 'from' keyword 

I like it better when there is no "warnings and errors that must be fixed"

## Comment (mapellidario, 2023-07-20T12:41:31Z)

> can you kindly take care of this as well ?

sure, i did not find it in the table at #7756 and thought you decided to ignore it. the is straightforward, i will edit the table myself

## Comment (cmsdmwmbot, 2023-07-20T12:47:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 124 comments to review
 * Pycodestyle check: succeeded
   * 128 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1628/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-20T13:28:01Z)

I only put in that table those which I had to fix now. Did not try to remember everything else. Please keep adding to the table

## Comment (mapellidario, 2023-07-20T15:37:28Z)

I see, thanks. 

can we merge this?
