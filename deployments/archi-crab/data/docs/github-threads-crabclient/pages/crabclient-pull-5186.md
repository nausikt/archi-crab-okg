# dmwm/CRABClient pull request #5186: Fix getattr with config.Data.inputBlocks

State: closed
Opened: 2023-02-13T18:04:45Z
Closed: 2023-02-15T14:48:19Z
Merged: 2023-02-15T14:48:19Z
URL: https://github.com/dmwm/CRABClient/pull/5186

## Opening post (novicecpp, 2023-02-13T18:04:45Z)

Fix PR https://github.com/dmwm/CRABClient/pull/5185

I misunderstand [getattr()](https://docs.python.org/3/library/functions.html#getattr) with [dict.get()](https://docs.python.org/3/library/stdtypes.html#dict.get) by assuming `getattr()` will automatically return `None` if we do not provide a default value when calling the function.

## Comment (cmsdmwmbot, 2023-02-13T23:15:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 99 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/927/artifact/artifacts/PullRequestReport.html
