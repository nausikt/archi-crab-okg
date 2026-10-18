# dmwm/CRABClient pull request #5322: Fix autocompletion

State: closed
Opened: 2024-07-04T09:05:47Z
Closed: 2024-07-14T15:49:42Z
Merged: 2024-07-14T15:49:42Z
URL: https://github.com/dmwm/CRABClient/pull/5322

## Opening post (belforte, 2024-07-04T09:05:47Z)

fixes #5321 
fixes #5319

## Comment (cmsdmwmbot, 2024-07-04T09:08:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 23 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1061/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-07-04T09:10:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1062/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-07-11T16:16:58Z)

Stefano, can I ask you to run the `generate_completions` script and commit the new ` etc/crab-bash-completion.sh` as well? [1]

maybe we should add this command to the specifile as well https://github.com/cms-sw/cmsdist/blob/IB/CMSSW_14_1_X/master/crab-build.file, but if the changes are not frequent enough it may not be worth it.

---

[1]

```bash
> cd CRABClient
> python3 scripts/generate_completions.py
```

mentioned at https://github.com/dmwm/CRABClient/blob/d17ff66a143d33d99d31c8f767c3cc75fdbceef8/scripts/generate_completion.py#L13

## Comment (belforte, 2024-07-11T20:53:00Z)

I had tried that, but can't do it on my laptop since
```text
LapSB:CRABClient$ python3 scripts/generate_completion.py
INFO:root:etc/crab-bash-completion.sh

Error: $CMSSW_VERSION is not defined. Make sure you do cmsenv first. Exiting...
LapSB:CRABClient$ 
```
As you were away, I forgot to ask for help and/or mention this.

I can fix this with a commit from lxplus, But...
1) it means that there's no hope to do it in `crab_build`
2) even including it in a future automatic pipeline for CRABClient (which Wa has in his plans) may be complicated

## Comment (belforte, 2024-07-11T21:03:56Z)

Done. Thanks @mapellidario for reminding me !

## Comment (cmsdmwmbot, 2024-07-11T21:04:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1064/artifact/artifacts/PullRequestReport.html
