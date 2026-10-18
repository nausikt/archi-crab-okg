# dmwm/CRABServer pull request #8893: Cleanup after switch to input args

State: closed
Opened: 2025-01-27T21:13:52Z
Closed: 2025-01-30T16:24:30Z
Merged: 2025-01-30T16:24:30Z
URL: https://github.com/dmwm/CRABServer/pull/8893

## Opening post (belforte, 2025-01-27T21:13:52Z)

(no text)

## Comment (cmsdmwmbot, 2025-01-27T21:17:26Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2341/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-27T21:18:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2342/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-27T21:31:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 270 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2343/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-27T22:11:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2344/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-27T22:19:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2345/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-27T22:20:15Z)

now testing in `test2`: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10013422
**BUG 1** **fixed**
test used `crab-dev` and triggered a but in DagmanCreator. `requiredmicroarch` was not consistently set to a string.

## Comment (cmsdmwmbot, 2025-01-27T22:55:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2346/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-27T22:57:54Z)

new test pipeline after above fix: https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10013506
**BUG 2**  **fixed in 02b8699f**
**CV** fails because `crab preparelocal` fails with
```
  File "/cvmfs/cms.cern.ch/share/cms/crab-dev/v3.241218.00/lib/CRABClient/Commands/preparelocal.py", line 153, in prepareDir
    inputArgsForScript[key] = jobArgs[value]
KeyError: 'CRAB_Archive'
```
so pipeline does not submit CCV

* problem is that new TW code will work with [new `preparelocal`](https://github.com/dmwm/CRABClient/issues/5288) But current code still needs that the `input_args.json` file contains all args. listed in https://github.com/dmwm/CRABClient/blob/8b8da2a40b2ee3bd8a9df03613ff291608262b56/src/python/CRABClient/Commands/preparelocal.py#L136-L145
* I tried to rename ` -a archiveJob` to  `--userSandbox`, but it is too early for that. Let's keep both possibilities. Same for a few others

## Comment (belforte, 2025-01-27T23:08:54Z)

during automatic splitting, report for probe job on the WN i called e.g. `jobReport.json.5` while htcondor will want to transfer and PostJob will look for
`JOB AD: TransferOutput = "jobReport.json.0-5,WMArchiveReport.json.0-5"`
I need to keep renaming files in CMSRunAnalysis.py. and this means that I need to keep the confusing functionality overlap with `CRAB_Destination` until I understand this part well enough to do a proper cleanup.
**BUG 3** **fixed in 88de9c9a**

Jobs get help and retried and then fail with

<pre>[crabtw@vocms059 cluster10080353.proc0.subproc0]$ condor_q 10080374.0 -af holdreason
Transfer output files failure at the execution point while sending files to access point vocms059. Details: reading from file /storage/local/data1/condor/execute/dir_3383924/glide_3MGoC2/execute/dir_2079020/jobReport.json.0-1: (errno 2) No such file or directory
[crabtw@vocms059 cluster10080353.proc0.subproc0]$ 
</pre>
problem is still there after the jobNumber fix for BUG 6

damn.... the failing job has
`== JOB AD: CRAB_Id = 0 - 1`
it shuld be
`== JOB AD: CRAB_Id = "0-1"`
!!!!!


`crab kill` did nothing on that task. To be investigated.
**BUG 5**  **Fixed in #8901**
Task URL: https://cmsweb-test2.cern.ch/crabserver/ui/task/250127_223131%3Abelforte_crab_20250127_233124

problem is
```text
Failure message from server:	Problem handling 250127_223131:belforte_crab_20250127_233124 because of 'clusterid' failure, traceback follows
				Traceback (most recent call last):
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 98, in executeAction
				    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanKiller.py", line 109, in execute
				    self.executeInternal(*args, **kwargs)
				  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/DagmanKiller.py", line 42, in executeInternal
				    if not self.task['tw_name'] or not self.task['clusterid']:
				KeyError: 'clusterid'
```
**understood**: problem is [this](https://github.com/dmwm/CRABServer/blame/a6115c5b782bc9c0fe270f7f94c4ccf40df4a609/src/python/TaskWorker/Actions/DagmanKiller.py#L42) line introduced in https://github.com/dmwm/CRABServer/commit/8ed2195d78b2c47daa55f2738bd9d98469f9b8f7 . I did not notice at that time that the query used to retrieve tasks to process does not retrieve the full info from DB and in particular `clusterid` is always missing from the `task` dictionary at this point. Need to decide which is the best way ahead.

## Comment (belforte, 2025-01-27T23:49:09Z)

submitted **CCV** via Jenkins: https://github.com/dmwm/CRABServer/issues/8894 
mixed result: 8 tests failed, others OK
**BUG 6**  **fixed via 754ad1de 7ebdb5bf and 0c08e3c0**
```text
FAILED TESTS:
maxMemoryMB-check.sh 250127_234911:cmsbot_crab_maxMemoryMB - 1
maxJobRuntimeMin-check.sh 250127_234914:cmsbot_crab_maxJobRuntimeMin - 1
numCores-check.sh 250127_234919:cmsbot_crab_numCores - 1
scriptExe-check.sh 250127_234922:cmsbot_crab_scriptExe - 1
scriptArgs-check.sh 250127_234925:cmsbot_crab_scriptArgs - 1
lumiMaskFile-check.sh 250127_234946:cmsbot_crab_lumiMaskFile - 1
lumiMaskUrl-check.sh 250127_234949:cmsbot_crab_lumiMaskUrl - 1
runRange-check.sh 250127_234956:cmsbot_crab_runRange - 1
``` 

* `maxMemoryMB` , `maxJobRuntimeMin` , `numCores` were due to missing ads in Job.submit - **fixed**
* `lumiMaskFile` fails because ad format has changed to ` CRAB_AlgoArgs = "....'lumis': ['1,10` instead of `lumis": \["1,10'` I a not sure if it is worth to do anything but change our test when we merge the final PR - same for `lumiMaskUrl` where test looks for `grep -q '== JOB AD: CRAB_AlgoArgs.*"273158"' crab_lumiMaskUrl/results/job_out.1.0.txt` but file now has single quotes around Run Number `273158`, not double quotes
* `runRange` again single vs. double quotes in the ad value.
* the new format is "better" since it is the same as in the DataBase
![image](https://github.com/user-attachments/assets/b048298d-9b7a-4739-b153-39500535c761)

*  **Idea**: maybe I can remove the quotes from the `grep` in the text, it will not be "as strict" but should still do

* * *`scriptExe`** real bug. When the script runs in the WN it gets `None` as argument, instead of the job ID. Indeed job stdout has
   * `==== Will execute stdbuf -oL -eL /srv/SIMPLE-SCRIPT.sh  None  > cmsRun-stdout.log.tmp 2>&1`
   * and 
![image](https://github.com/user-attachments/assets/87a9e235-7338-4b4e-993a-007d340e2c38)
    * need to add `jobNumber` to `input_args.json` !! as usual it is not immediately clear what to use for automatic splitting (see also **BUG 3**), if the integer index (`$count`) of the dagman spec for that job or the crab ID with the 0-x, 1-x... etc. format
   
* same for `scriptArgs`, the arguments are passed finely but test looks also for the first arg (jobNumber)
![image](https://github.com/user-attachments/assets/1ea271ed-c6de-4dc7-9b73-226e76e6fc48)

## Comment (belforte, 2025-01-27T23:55:54Z)

`CRAB_Workflow` is missing in [OpenSearch](https://monit-opensearch.cern.ch/dashboards/goto/8ea4f9324a31c4b209185f07ef4e2f04) so jobs do not appear in Grafana 
 * odd because I find it in job classAds 
 
**BUG 4** **Fixed in 75fbb0ac**
ok. I was defining `CRAB_workflow` with lowercase `w`. Grafana is clearly case sensitive.

## Comment (cmsdmwmbot, 2025-01-28T11:06:20Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2347/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-28T18:43:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2348/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-28T21:15:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2349/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-28T22:22:16Z)

try again CCV test via Jenkins, now expect to see only ScriptExe and scriptArgs to fail.
This time submitted also CV which now should work since I fixed the problem with `preparelocal`  (**BUG 2**)
Jenkins test: https://github.com/dmwm/CRABServer/issues/8896
 * **CV** is OK
 * **CCV** `script*`failed as expected,  `runRange` appear still running which is odd since job completed 30min ago
    * looks like a new problem . [task Url](https://cmsweb-test2.cern.ch/crabserver/ui/task/250128_222145%3Acmsbot_crab_runRange)
    
![image](https://github.com/user-attachments/assets/a2c3631c-8cc4-48a3-ac74-c5a91cdae357)
* pff... typo in my fix to CCV test in #8895 
   * I pushed a fix in master, hopefully next iteration of CCV in #8896 will pick new code and be OK.

## Comment (cmsdmwmbot, 2025-01-28T23:47:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 269 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2351/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-29T09:31:33Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 175 comments to review
 * Pycodestyle check: succeeded
   * 311 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2354/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-01-29T21:35:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 283 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2356/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-29T21:43:18Z)

test again CV and CCV via Jenkins
- [x] PROD Client: https://github.com/dmwm/CRABServer/issues/8902
- [x] DEV Client: https://github.com/dmwm/CRABServer/issues/8903

All OK at last ! Only remaining problem is **BUG 3** about Automatic Splitting

## Comment (cmsdmwmbot, 2025-01-30T10:26:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 282 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2360/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-30T10:27:17Z)

Fixed all bugs found so far.
New automatic split task - processing stage jobs are running
- [x] https://cmsweb-test2.cern.ch/crabserver/ui/task/250130_095717%3Abelforte_crab_20250130_105713

New pipeline CV and CCV OK
- [x] https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10034118

## Comment (cmsdmwmbot, 2025-01-30T16:21:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 70 comments to review
 * Pycodestyle check: succeeded
   * 268 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2361/artifact/artifacts/PullRequestReport.html
