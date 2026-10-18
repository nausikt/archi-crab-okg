# dmwm/CRABServer pull request #9081: Fix8988

State: closed
Opened: 2025-05-19T08:12:59Z
Closed: 2025-05-23T08:12:59Z
Merged: 2025-05-23T08:12:59Z
URL: https://github.com/dmwm/CRABServer/pull/9081

## Opening post (aspiringmind-code, 2025-05-19T08:12:59Z)

Valentin has fixed on WMCore side. See[ here](https://github.com/dmwm/WMCore/issues/12358#event-17678769812). On our end, these changes are enough. Some light style clarity added.
We continue to use `data_files` within setup() even after the shift to `setuptools` on our end which works but can be replaced with `package_data` See [here](https://github.com/aspiringmind-code/CRABServer/blob/17dd4b21da3962d11b155243d2a44695e0304818/setup.py#L281) @belforte Let me know if you prefer to change or are fine with this.

## Comment (cmsdmwmbot, 2025-05-19T08:15:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2452/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-19T09:27:42Z)

IIUC `package_data` is "new way" while `data_files` is "old", so we should change to make it easier on future maintainers.

BTW these lines
```python
      data_files=['scripts/%s' % x for x in \
                        ['CMSRunAnalysis.sh', 'cmscp.py', 'cmscp.sh',
                         'gWMS-CMSRunAnalysis.sh', 'submit_env.sh',
                         'dag_bootstrap_startup.sh',
                         'dag_bootstrap.sh', 'AdjustSites.py']] + getWebDir(),
     )
```
are exactly what I'd like to simplify in #8727 by replacing the list of files with just one directory name

## Comment (cmsdmwmbot, 2025-05-22T11:18:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2469/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-22T11:19:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2470/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-22T11:21:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2471/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-22T11:54:55Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 26 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2472/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-22T12:06:56Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2473/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-22T12:14:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 41 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2474/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-05-22T12:15:54Z)

@belforte After trying to make package_data work with minimal changes, I believe it will involve deeper changes in buildDatafiles.sh script that makes use of data_files. We could go for an overhaul where we eliminate the script altogether or make it work with package_data in a separate issue. Since data_files is still compatible with setuptools, I suggest we stick to it here. Let me know what you think.

## Comment (belforte, 2025-05-22T12:30:53Z)

let's stick with `data_files` then, for the time being.
Getting rid of buildDataFiles.sh is certainly appealing, but I do not know if it is possible.

That said, if `data_files` vs. `package_data` is only a directory name change, it will be easy to accommodate and we can move to a more modern code. But if changes are deeper, I agree to be very careful and stick with "best is the enemy of good"

## Comment (belforte, 2025-05-22T12:31:11Z)

we can go through things in our next chat

## Comment (aspiringmind-code, 2025-05-23T08:13:38Z)

Thanks! Merged.
