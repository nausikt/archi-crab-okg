# dmwm/CRABServer pull request #8737: Various fix for process controller scripts (manage.sh/manage.py/etc.)

State: closed
Opened: 2024-10-11T11:32:58Z
Closed: 2024-10-17T00:23:06Z
Merged: 2024-10-17T00:23:06Z
URL: https://github.com/dmwm/CRABServer/pull/8737

## Opening post (novicecpp, 2024-10-11T11:32:58Z)

- Fix debug mode in crabserver image, check if var is set instead of boolean.
- Fix manage.sh for crabserver where `-g` does not work.
- Fix manage.py to execute manage.sh path in the same directory
- Fix manage.py `-s SERVICE` by moving to top-level, require by Publisher's manage.sh, and compatibility with other service.
- Print variables will be sourced in env.sh
- Add `./manage.py status` for all services, also print PYTHONPATH, partial fix https://github.com/dmwm/CRABServer/issues/8707
- Fix manage.sh waiting forever in Publisher https://github.com/dmwm/CRABServer/issues/8442

All tested except the last bullet.

## Comment (cmsdmwmbot, 2024-10-11T11:35:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2193/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-10-11T13:25:03Z)

thanks, superquick. Yet I do not understand the first commit, I was running from `/data` cwd

typing `/data/start.sh` with a cwd other than `/data` fails immediately with ` No such file or directory: './manage.sh'` which is all in all OK

i.e. this may be nice, but does not appear related to the problem that PYTHONPATH is not changed when using `-g`. Or is that due to the $DEBUG bug as well ?

## Comment (belforte, 2024-10-11T13:38:10Z)

hmm.. looks to me that `$MODE` is set in `manage.py` but never used

## Comment (novicecpp, 2024-10-11T14:42:41Z)

Yeah....I just discover while testing this script.
The new commits I pushed should fix many issues I found so far, including https://github.com/dmwm/CRABServer/issues/8707 and https://github.com/dmwm/CRABServer/issues/8707 (sorry for stealing Vijay task).

## Comment (cmsdmwmbot, 2024-10-11T14:43:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2194/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-10-11T15:25:00Z)

@belforte I have updated this PR description.  
I will leave this until Tuesday in case you have any question.

## Comment (cmsdmwmbot, 2024-10-11T15:26:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2195/artifact/artifacts/PullRequestReport.html
