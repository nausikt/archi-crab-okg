# dmwm/CRABServer pull request #7867: Detect and report corrupted files

State: closed
Opened: 2023-09-08T15:08:48Z
Closed: 2023-09-18T13:27:40Z
Merged: 2023-09-18T13:27:40Z
URL: https://github.com/dmwm/CRABServer/pull/7867

## Opening post (belforte, 2023-09-08T15:08:48Z)

a first step toward fixing  #7548
this PR includes code to write a JSON file in `/eos/cms/store/temp/user/corrupted/` which we can use to check that things are OK before calling `rucioClient.declare_suspicious_file_replicas()` 

```
belforte@lxplus806/~> ls /eos/cms/store/temp/user/corrupted/
230908_074255:belforte_crab_20230908_094238.job.5.1.json
230908_074255:belforte_crab_20230908_094238.job.5.2.json
230908_074255:belforte_crab_20230908_094238.job.5.3.json
belforte@lxplus806/~> cat /eos/cms/store/temp/user/corrupted/230908_074255:belforte_crab_20230908_094238.job.5.3.json|jq
{
  "DID": "cms:/store/data/Run2018C/ParkingBPH5/MINIAOD/05May2019-v1/70000/4A628618-FB8A-804C-A905-A046244B6DF3.root",
  "RSE": "T2_US_Wisconsin",
  "exitCode": 8020,
  "message": [
    "== CMSSW:       [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init\n",
    "== CMSSW: file root://cmsxrootd.fnal.gov//store/data/Run2018C/ParkingBPH5/MINIAOD/05May2019-v1/70000/4A628618-FB8A-804C-A905-A046244B6DF3.root is truncated at 2183135232 bytes: should be 4128873606, trying to recover\n"
  ]
}
belforte@lxplus806/~> 

```

There are also a few simple pylint fixes

## Comment (belforte, 2023-09-08T15:09:18Z)

I need to rebase

## Comment (cmsdmwmbot, 2023-09-08T15:10:31Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 warnings
   * 100 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1689/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-08T15:24:33Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 warnings
   * 100 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1690/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-08T15:34:31Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 7 warnings
   * 100 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1691/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-08T17:30:59Z)

I tested this locally on crab-dev-tw01
It should be reasonably safe, pylint aside the change is the addition of the new `check_corrupted_file()` method which is called when exit code is 8020/8021/8028

But surely a look by a second  couple of eyes will be good.

## Comment (belforte, 2023-09-11T11:39:07Z)

good points.  I have more fundamental issues now, see #7548 , but will get to these as well.
A first step is indeed to see how many open errors are reported as corrupted files.
Timeout is needed "immediately", yes !

## Comment (cmsdmwmbot, 2023-09-11T13:46:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1692/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-11T19:23:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1693/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-11T20:01:16Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1694/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-09-11T20:29:06Z)

I did some changes and after the gfal timeout and this https://github.com/belforte/CRABServer/blob/7be608a0a25fb4149b0ed3ff7a8a68312450d2d1/src/python/TaskWorker/Actions/RetryJob.py#L313-L321
I hope that it is robust enough to be put in production and see what happens.

@novicecpp maybe you can consider using this you your copy-cat tests, to give it a first shake ?

## Comment (cmsdmwmbot, 2023-09-11T20:53:14Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1695/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-09-13T09:23:29Z)

> @novicecpp maybe you can consider using this you your copy-cat tests, to give it a first shake ?

Sure. I will deploy it tomorrow, in test12.

## Comment (cmsdmwmbot, 2023-09-18T12:01:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 8 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 75 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1702/artifact/artifacts/PullRequestReport.html
