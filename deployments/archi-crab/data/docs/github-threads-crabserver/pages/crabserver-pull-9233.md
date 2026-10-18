# dmwm/CRABServer pull request #9233: add safe lock on run_and_lumis, even in sequentially synchronized pla…

State: closed
Opened: 2025-11-17T13:00:07Z
Closed: 2025-12-05T03:17:06Z
Merged: 2025-12-05T03:17:06Z
URL: https://github.com/dmwm/CRABServer/pull/9233

## Opening post (nausikt, 2025-11-17T13:00:07Z)

Resolve #9226

## Comment (cmsdmwmbot, 2025-11-17T13:03:18Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 374 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2669/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-11-17T14:40:55Z)

I've tested Automatic Splitting on *test14* as you can see [here](https://cmsweb-test14.cern.ch/crabserver/ui/task/251117_134000%3Akphornsi_crab_test14-automatic-splitting-have-race/dbver/devfour), 

Everything looks good, Task've been through both Lock in PreDAG twice for each stage (0-X, 1-X, even there is no tails stage) [1], also PostJob [2].

[1] 251117_134000:kphornsi_crab_test14-automatic-splitting-have-race
```
https://cmsweb.cern.ch/scheddmon/0197/kphornsi/251117_134000:kphornsi_crab_test14-automatic-splitting-have-race/AutomaticSplitting/

Probe Jobs status:              finished     		100.0% (5/5)
Estimated application throughput from probe jobs :
  found 5 completed jobs
  average throughput for 5 jobs: 1175.0878 evt/s
  average eventsize for 5 jobs: 179.0 bytes

Jobs status:                    transferring 		100.0% (1/1)
```

[2] PostJob 1-0 log
```
[kphornsi@vocms0197 251117_134000:kphornsi_crab_test14-automatic-splitting-have-race]$ cat postjob.1.0.txt  | grep "automatic splitting"
Mon, 17 Nov 2025 15:20:21 CET(+0100):INFO:PostJob ====== Starting saving data for automatic splitting.
Mon, 17 Nov 2025 15:20:21 CET(+0100):INFO:PostJob ====== Finished saving data for automatic splitting.
```

## Comment (cmsdmwmbot, 2025-11-17T15:57:11Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 381 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2670/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-11-17T16:11:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 362 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2671/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-11-18T09:35:46Z)

note that there are other files in `CMSRunAnalysis.tar.gz` which are modified by PreDag, like `input_args.json`. The actions are safe locally to the AP, since PreDag adds information needed to new jobs in tail subdags before those are submitted, but it is possible for PreDag to run and create subdags before the current stage is completed (e.g. when main processing stage is at 80%). Of course if stage is 80% completed, chances are that all jobs have started already, but we can not guarantee it, and since you are putting your hands in this part now, it is good to do it properly.

Further note: when a job is submitted, it is not "safe" yet. It may stay in the queue for a a while, only when it is matched to an available pilot and starts running on the remove WN, condor will copy the tarball there.

## Comment (nausikt, 2025-11-18T09:44:33Z)

I've slept on this with ChatGPT as well for ideas coverage, Chat suggested quite elegant pattern that completely kill this kind of races **w/o using lock** that i totally intriguing with. (same pattern that HTCondor used for writing some log in schedds)

Every time we ***write***, create it as `temp`.
```python
tmp_name = 'run_and_lumis.tar.gz.tmp'

with tarfile.open(tmp_name, 'w:gz') as tf:
    tf.add(runAndLumisDir, arcname='')
```
Then do atomic replace later
```
os.replace(tmp_name, 'run_and_lumis.tar.gz')  # atomic on POSIX
```
Such that it safe for ***read*** at any moment, `run_and_lumis.tar.gz` is either the ***old valid*** tar, the ***new valid tar***. May i hear your opinions on this too, please?

## Comment (nausikt, 2025-11-18T09:47:49Z)

this way we simplify the code by eliminated **all** **Read Lock**, and worries just about **Write Lock** which have much less potential clash places.

P.S. **Read Lock** may required when that piece of code better wait for **new valid tar**, very sensitive to content inside tar. 
P.S. In other words if **new valid tar** doesn't naturally arrived on time, they can live with **old valid tar**, in naturally never clashes manner. 
P.S. Suite scenarios where there's very few writers at overlap time window, like in our cases here?

## Comment (belforte, 2025-11-18T09:59:33Z)

well.. sure. `os.rename` is the same as the good old `mv`, you do not need ChatGPT for this ! Indeed there are many places in the code where we do that (create .tmp, then mv). It should be OK here. At least I can't think right away of a reason to wait before reading.
Instead, where PostJob is using the lock atm, there can be a benefit by avoiding many processes doing same work at ~same time, but doing it in one and sharing updated result.
But we can't ask original developers for their reasons where they did not document in the comments.

## Comment (belforte, 2025-11-18T10:01:15Z)

I guess it was my bad here, to have suggested a lock instead of a `mv`. I was wary of `mv` across file systems (SPOOL_DIR is on CEPH, tmpdir is on /tmp i.e. local hypervisor disk). But we can copy to SPOOL_DIR/tarball.tmp and then do an atomic move there. That should be safe

## Comment (belforte, 2025-11-18T10:08:18Z)

Thinking about it, only mv inside the same  file system can be atomic, i.e. the pointer from file name to disk location is changed in "one go". Across file systems there's no alternative to copying bytes around.
If you ask why I did not create tmpdir in /data, it was to limit I/O since tar operations are I/O intensive and we already struggle with IOops on /data = /vdc = SPOOL_DIR

## Comment (belforte, 2025-11-18T10:11:09Z)

thanks for having pointed out my "overkill".

## Comment (nausikt, 2025-11-18T10:11:44Z)

> Thinking about it, only mv inside the same file system can be atomic, i.e. the pointer from file name to disk location is changed in "one go". Across file systems there's no alternative to copying bytes around. If you ask why I did not create tmpdir in /data, it was to limit I/O since tar operations are I/O intensive and we already struggle with IOops on /data = /vdc = SPOOL_DIR

Ahhh, that resonated with me both heterogenous file system, I/O ops, so having lock this way sound more convincing to me.

## Comment (nausikt, 2025-11-18T10:14:33Z)

if I/O heavy atomic mv happened on TW, IMO is tolerable but otherwise on AP/WN not sound good to me.

## Comment (belforte, 2025-11-18T10:15:00Z)

recap:
1. create new `tarball` in `/tmp`
2. copy to `SPOOL_DIR/tarball.tmp`
3. `mv SPOOL_DIR/tarball.tmp SPOOL_DIR/tarbal`

what do you think ?

## Comment (nausikt, 2025-11-18T10:17:17Z)

Sound good to me, let me converging to that.

## Comment (belforte, 2025-11-18T10:19:08Z)

> if I/O heavy atomic mv happened on TW, IMO is tolerable but otherwise on AP/WN not sound good to me.

?? I think `mv` does not shuffle disk bytes around, it is not I/O heavy.

## Comment (nausikt, 2025-11-18T10:22:42Z)

> recap:
> 
> 1. create new `tarball` in `/tmp`
> 2. copy to `SPOOL_DIR/tarball.tmp`
> 3. `mv SPOOL_DIR/tarball.tmp SPOOL_DIR/tarbal`
> 
> what do you think ?

For clarity, May i have your clarifications/confirmation? around where 1,2,3 has happened.
From my understanding.
1. local AP disk, `/tmp`
2. [Non-atomic transferring] from local AP disk -> HTCondor shared/parallel NFS `SPOOL_DIR/tarball.tmp`
3. [expected Atomic] among shared/parallel NFS `SPOOL_DIR/tarball.tmp SPOOL_DIR/tarbal`

So, so it's something like 2-steps copy with atomic guarantee on destination site?

> if I/O heavy atomic mv happened on TW, IMO is tolerable but otherwise on AP/WN not sound good to me.

Apologize, I means write/add/update tar gz as temp that original developer try to lock.

## Comment (belforte, 2025-11-18T10:31:23Z)

Yes.

## Comment (belforte, 2025-11-18T10:32:33Z)

> Apologize, I means write/add/update tar gz as temp that original developer try to lock.

The existing lock acts on files created and read by PostJob. Nothing happens in TW

## Comment (cmsdmwmbot, 2025-12-01T14:54:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 376 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2674/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T15:10:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 376 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2675/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T15:33:08Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2676/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T15:46:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2677/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T16:28:06Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 379 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2678/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:05:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 40 comments to review
 * Pycodestyle check: succeeded
   * 377 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2679/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-01T17:05:09Z)

@nausikt please remember to use caMelCase for CRAB code

## Comment (cmsdmwmbot, 2025-12-01T17:08:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2680/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:12:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2681/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:24:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2682/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:28:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2683/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:37:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2684/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-01T17:49:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2685/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-01T19:25:16Z)

Thank you for the idea! @belforte, I've converged to your 2-steps atomic copy and tested them via Automatic Splitting task on test14, as following [1]. 

Could you please kindly review and let me know what you think at your most convenience please, e.g. Do we need more verifications? whether its truly resolved race condition OR we good to putting it on test in canary/prod right away. 
P.S. IIUC, it's quite hard to reproduce such a race condition in non-prod envs?

[1] Task: [251201_175003:kphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7](https://cmsweb-test14.cern.ch/crabserver/ui/task/251201_175003%3Akphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7/dbver/devfour)
```bash
[kphornsi@lxplus942 automatic-splitting]$ crab status
Rucio client intialized for account kphornsi
CRAB project directory:		/tmp/crabStatusTracking/crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7
Task name:			251201_175003:kphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7
Grid scheduler - Task Worker:	crab3@vocms0121.cern.ch - crab-dev-tw05
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test14.cern.ch/crabserver/ui/task/251201_175003%3Akphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=251201_175003%3Akphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7&from=1764607803000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_FR_IPHC', 'T2_UK_SGrid_Bristol', 'T2_IT_Legnaro', 'T2_IT_Pisa']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	SUBMITTED

The job splitting of this task is 'Automatic', please refer to this FAQ for a description of the jobs status summary:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
More details of Automatic Splitting process for this task (including possible failures) are in the Dagman Log files in:
https://cmsweb.cern.ch/scheddmon/0121/kphornsi/251201_175003:kphornsi_crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7/AutomaticSplitting/

Probe Jobs status:              finished     		100.0% (5/5)
Estimated application throughput from probe jobs :
  found 5 completed jobs
  average throughput for 5 jobs: 785.5183800000001 evt/s
  average eventsize for 5 jobs: 193.2 bytes

Jobs status:                    transferring 		100.0% (1/1)

Output dataset:			/GenericTTbar/kphornsi-autotest-1764611395-94ba0e06145abd65ccb1d21786dc7e1d/USER

No publication information available yet

Summary of run jobs:
 * Memory: 703MB min, 1112MB max, 1113MB ave
 * Runtime: 0:03:29 min, 0:14:14 max, 0:14:14 ave
 * CPU eff: 70% min, 70% max, 70% ave
 * Waste: 0:02:28 (15% of total)

Log file is /tmp/crabStatusTracking/crab_test14-automatic-splitting-fix-by-atomic-move-to-spool-7/crab.log
```

## Comment (cmsdmwmbot, 2025-12-04T08:16:47Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2689/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-04T08:23:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 32 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2690/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-04T08:36:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2691/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-04T08:45:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2692/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-04T11:05:10Z)

AS Task went well on test14, [251204_084559:kphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-1](https://cmsweb-test14.cern.ch/crabserver/ui/task/251204_084559%3Akphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-1) [[Grafana](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=251204_084559%3Akphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-1&from=1764834360000&to=now)]

## Comment (belforte, 2025-12-04T14:36:23Z)

@nausikt if you want another review, you should click on the ad-hoc button (with circular arrows) at top right. I'll do it now, but for you to know in the future.

## Comment (nausikt, 2025-12-04T14:51:36Z)

> THanks, much neater now ! But IIUC you forgot to make it atomic the copy of `input_files.tar.gz` and `'CMSRunAnalysis.tar.g`. I still suggest to rename ` atomicMoveToSpool` as `atomicReplaceFileOnOtherFileSystem` and remove `Spool` word in there.

Acknowledged, Man. i totally forgot to click re-review, normally i did aware and clicked it.
Roger that on `atomicReplaceFileOnOtherFileSystem`.
Okk for `input_files.tar.gz`, `CMSRunAnalysis.tar.gz`, let me find out potential cross filesystem copying. and back to you asap.

## Comment (cmsdmwmbot, 2025-12-04T16:32:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2693/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-12-04T16:45:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2694/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-04T17:56:18Z)

AS Task Tested! [251204_172101:kphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-2](https://cmsweb-test14.cern.ch/crabserver/ui/task/251204_172101%3Akphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-2) [[Grafana](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=251204_172101%3Akphornsi_crab_test14-automatic-splitting-test-atomic-move-to-spool-2&from=1764865263000&to=now)]

IIUC, There's no other potential writers elsewhere for all tarballs. other than that please let me know whether all vars, fns naming now is good enough? Thanks in advance man!

## Comment (cmsdmwmbot, 2025-12-04T18:04:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2695/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-05T03:14:23Z)

Done! Thanks Man.

## Comment (cmsdmwmbot, 2025-12-05T03:15:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 31 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2696/artifact/artifacts/PullRequestReport.html
