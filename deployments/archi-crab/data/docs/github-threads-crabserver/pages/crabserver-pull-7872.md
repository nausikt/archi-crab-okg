# dmwm/CRABServer pull request #7872: Fix including ASO dir to RPM build

State: closed
Opened: 2023-09-12T16:26:35Z
Closed: 2023-09-13T16:00:17Z
Merged: 2023-09-13T16:00:17Z
URL: https://github.com/dmwm/CRABServer/pull/7872

## Opening post (novicecpp, 2023-09-12T16:26:35Z)

When building rpm, `htcondor_make_runtime.sh` zip files from `build/lib`, which is created by `setup.py` (at [crabtaskworker.spec#L39](https://github.com/cms-sw/cmsdist/blob/9633680c4b729ee34220398654bd5fe84038274f/crabtaskworker.spec#L39)). I never update setup.py, so there is no `ASO` directory in `build/lib`. 
Plus, the zip command always has exit 0 even if the file is not found and makes the build always pass.

~~This PR does not intend to fix the problem above but only to include `src/python/ASO` back to `CRAB3.zip` for RUCIO_Transfers.py script, plus remove unused CRABInterface (that we never put in `CRAB3.zip` in the first place) from zip arguments.~~

~~I plan to fix this issue in CRAB's PyPI later.~~

This PR is do the minimum fix, plus remove unused CRABInterface (that we never put in `CRAB3.zip` in the first place) from zip arguments. I plan to do improvement later in CRAB PyPI's task.

## Comment (cmsdmwmbot, 2023-09-12T16:31:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1700/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-13T15:05:56Z)

I am a bit lost. You wrote that you do not want to fix with problem with setup.py now, but there's a change in setup.py which appears to do that.
Anyhow.. as long as it works, and since it will need changing for pypi anyhow... sure !

## Comment (novicecpp, 2023-09-13T15:43:52Z)

My bad. 
This PR fixes the problem. I just do not like that you need to update both setup.py and htcondor_make_runtime.sh, which is easy to forget.

Anyway, thanks for review!

## Comment (belforte, 2023-09-13T15:47:15Z)

Yes. I don't like that either, but never realized. I also do not like that we send to the grid WN code which is only used by scripts running on the scheduler.
