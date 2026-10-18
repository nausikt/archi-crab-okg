# dmwm/CRABServer pull request #9153: Reorganize tw tarballs

State: closed
Opened: 2025-08-18T16:36:49Z
Closed: 2025-08-25T10:26:18Z
Merged: 2025-08-25T10:26:18Z
URL: https://github.com/dmwm/CRABServer/pull/9153

## Opening post (belforte, 2025-08-18T16:36:49Z)

this PR reorganizes the handling of files used in the AP's (aka schedulers, i.e. the VM's where we run the Dagman's) an in the grid WorkerNodes (aka Job Wrapper).

It needs changes to CRABClient for `crab report` and `crab preparelocal` to work: 
- [x] https://github.com/dmwm/CRABClient/pull/5410

After this:
* scripts are not mixed anymore in same directory. New structure is
```text
scripts
├── dagman
│   └── task_process
└── job_wrapper
```
* everything needed "outside TaskWorker" is bundled in two tarballs (I am keeping old names, even if not fully descriptive, am open to changing)
   * `TaskManagerRun.tar.gz`   contains what is needed in the AP
   * `CMSRunAnalysis.tar.gz` contains what is needed in the JobWrapper
* they are initially created when we build the TW container (by `buildTWTarballs.sh`) but files are later added by DagmanCreator with information specific to this task like job arguments, runs and lumis, input files etc.
* those are structured so that a simple `tar xf` created the needed directory layout in either place
* those are combined in a single `InputFiles.tar.gz` which is stored in S3 and downloaded by AP's bootstrap script (`dagman_bootstrap_startup.sh`) and CRABClient for `preparelocal`
* all python code which contains the needed dependencies is in two "libraries", taking advantage of the fact that python's `import` can pull code from a zipped file
    * `WMCore.zip` which is used both in AP and JobWrapper
    * `CRAB3.zip` which is only used in the AP
       * note: we use `PYTHONPATH=$pwd:CRAB3.zip:WMCore.zip` so files can be unzipped and accessed/edited for debugging
* `buildTWTarballs.sh` which builds that tarballs only refers to directory names, no individual file is listed there anymore, not in `setup.py`
* some changes were of course needed to main drivers for AP and JobWrapper
   * `dag_bootstrap_startup.sh` , `dag_bootstrap.sh` and `gWMS-CMSRunAnalysis.sh`
* largish changes were needed in `DagmanCreator` since it needs to
   * when running in the TW: add files to the tarballs before submission to the AP
   * also be able to run in the AP during automatic splitting
 
While doing this I have also cleanup code a bit and added many comments.

## Comment (cmsdmwmbot, 2025-08-18T16:41:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 48 warnings and errors that must be fixed
   * 1 warnings
   * 571 comments to review
 * Pycodestyle check: succeeded
   * 800 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2566/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-18T19:35:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 48 warnings and errors that must be fixed
   * 1 warnings
   * 571 comments to review
 * Pycodestyle check: succeeded
   * 800 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2567/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-18T23:30:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 47 warnings and errors that must be fixed
   * 1 warnings
   * 569 comments to review
 * Pycodestyle check: succeeded
   * 799 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2570/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-18T23:38:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 1 warnings
   * 562 comments to review
 * Pycodestyle check: succeeded
   * 791 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2571/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-18T23:39:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 1 warnings
   * 562 comments to review
 * Pycodestyle check: succeeded
   * 791 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2572/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-18T23:56:16Z)

about remaining pylint errors:
* CMSRunAnalysys.py will be fixed by Vijay in #9157 
* CMSrucio.py is to be removed (obsolete, never really used)
* cmscp.py is "beyond fixing" and anyhow was not touched in this PR, only moved. Better not  to touch it until we have a real need.

## Comment (cmsdmwmbot, 2025-08-19T14:02:28Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 40 warnings and errors that must be fixed
   * 1 warnings
   * 563 comments to review
 * Pycodestyle check: succeeded
   * 793 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2575/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-08-22T18:38:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 40 warnings and errors that must be fixed
   * 1 warnings
   * 563 comments to review
 * Pycodestyle check: succeeded
   * 793 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2583/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-08-25T10:26:00Z)

* modified CRABClient now available in IB as `crab-dev`
* this PR now passed "standard pipeline" https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12733756

time to merge
