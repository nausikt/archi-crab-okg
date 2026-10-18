# dmwm/CRABServer: commit history of src/python/TaskWorker/Actions/DagmanSubmitter.py (at 30286f7d5b21)

URL: https://github.com/dmwm/CRABServer/commits/master/src/python/TaskWorker/Actions/DagmanSubmitter.py

737d961c 2026-09-28 15:23:43 +0200 Krittin Phornsiricharoenphant: attached CRAB_UserEmail which retrieved via CRIC. (#9431)

61ea0187 2025-10-21 12:26:22 +0200 Stefano Belforte: allow config.TaskWorker.maxMemorySingleCore to override default in (#9219)
ServerUtilitie
9812df1e 2025-10-20 15:13:28 +0200 Stefano Belforte: point to CRAB_DAGType doc. Fix #9222 (#9223)

052d3992 2025-10-10 09:55:25 +0200 Stefano Belforte: only 3GB max mem for 1core at initial sub. Fix #9206 (#9207)
* only 3GB max mem for 1core at initial sub. Fix #9206

* add pointer to policy

* when asking too much in resubmt, allow to try again
640deb33 2025-07-14 11:55:53 +0200 Vijay Chakravarty: use tm_numcores (#9133)

d1deba38 2025-05-26 16:18:52 +0200 Stefano Belforte: Handle kill in rucio aso 8429 (#9089)
* close dataset if overallDagStatus is final Fix #8429

* close dataset at 100 files or 4 hours

* Remove DAGs after TASKLIFETIME. Fix #9077

* do not timeout PostJob when using Rucio. Fix #9078
accd4c8a 2025-05-20 16:49:08 +0200 Stefano Belforte: remove last usage of leading `+` for classAds
consistently use `My.` everywhere
0888a37b 2025-05-20 16:43:32 +0200 Stefano Belforte: remove last usage of +CRAB in classAds
Consistently use My.CRAB everywhere
8863cdcd 2025-02-20 13:05:48 +0100 Stefano Belforte: remove "if useHtcV2". Always use V2. Fix #8935 (#8936)
* remove "if useHtcV2". Always use V2. Fix #8935

* some pylint

* a bit more pylint
a5203b23 2025-02-13 21:37:14 +0100 Stefano Belforte: always use My. to add ads to JDL. Fix #8919 (#8920)

3f18b998 2025-01-31 17:29:42 +0100 Stefano Belforte: ensure CRAB_TaskSubmitTime becomes a classAd. Fix #8908 (#8909)

367e5692 2025-01-30 17:24:29 +0100 Stefano Belforte: refactor DAG creation and submission. Fix #8892 (#8893)

987523ca 2024-12-02 22:38:37 +0100 Stefano Belforte: add back CRAB_JobReleaseTimeout in DAG JDL. Fix #8852 (#8854)

443d91f7 2024-11-15 11:02:48 +0100 Stefano Belforte: do not put extraJdl nor require accelerator in dagman submission (#8796)

48420232 2024-08-19 18:44:11 +0200 Stefano Belforte: rename classad TaskType to CRAB_DAGType. Fix #8488 (#8616)
* rename classad TaskType to CRAB_DAGType. Fix #8488

* rename DAGType ROOT to BASE

* add backward compatibility
414396a1 2024-08-10 01:14:11 +0200 Stefano Belforte: use TaskWorkerConfig to enable use of V2 bindings (#8595)
* use TaskWorkerConfig to enable use of V2 bindings

* pylint

* fix Main.py

* addres comments from Wa
6cacb768 2024-08-03 23:28:17 +0200 Stefano Belforte: fix #8585 (#8586)

e6227eed 2024-07-30 11:11:39 +0200 Stefano Belforte: Add submitrefused 7989 (#8564)
* add SubmissionRefusedException in StageoutCheck

* move upload msg to common location in Handler

* use SubmissionRefusedException in DBSDataDiscovery

* use SubmissionRefusedException in Splitter

* use SubmissionRefusedException also for Rucio StageoutCheck

* use SubmissionRefusedException in Rucio and User DataDiscovery

* use SubmissionRefusedException in Dagman* actions

* use SubmissionRefusedException in Rucio actions

* pylint

* raise SubmissionRefused also when error is catched in Handler
f7000452 2024-06-17 14:44:41 +0200 Stefano Belforte: Merge modernize htc (#8503)
* custom attributs in JDL need classad.quote. Fix #8471 (#8476)

* first version which works using JDL to submit dag (#8486)

* use HTC bindings 23.9.0a2 (#8487)

* Modernize htc (#8493)

* htcondor.Submit() object must be filled with strings !

* pylint

* Modernize htc (#8495)

* bump htc bindings to 23.0 for crabserver

* stupid typo

* we want HTC ~= 23.0.12  see PR #8492
7bac1b78 2024-06-05 14:06:26 +0200 Stefano Belforte: Revert to v3.240530 (#8478)
* Revert "Revert "Run test jobs on crab sched 903 (#8472)" (#8474)"

This reverts commit 066545445ef330a43f1aa0ec9363bc5bbf48056c.

* Revert "Run test jobs on crab sched 903 (#8472)"

This reverts commit c5ec3efc9701b5924ac2ca61d1225b67cfa5db5d.

* Revert "ensure proxyfile in RestInfoForFileTransfers.json is a filename w/o path. Fix #8464 (#8467)"

This reverts commit 9ced4fd15edaffd72d4af51647dde15d2cba8e6e.

* Revert "workaround for #8456 (#8466)"

This reverts commit 602f8d6b043e79ee9e4f627ed0e272f055b3b5f5.

* Revert "Update makeTests.py: collector param does not allow port #. Simply put FNAL first"

This reverts commit 7ac2b90193632df3757bcf3bf7750ff27bf736a3.

* Revert "Update makeTests.py: add collector port for ITB"

This reverts commit f6c01ebafddb56ea7f15cbcf8f8563baae20114a.

* Revert "do not set RequestCpus in task submission JDL. Fix #8456 (#8457)"

This reverts commit 198e2d370a6b1a73f82a1c12b6dc88486dc4b2f1.

* Revert "pass string, not bytes, to htcondor.param Fix #8450 (#8452)"

This reverts commit 856d1efed8cba1f6c65d9b263ab8ffc20db9cd4d.

* Revert "schedd.xquery is deprecated. Use schedd.query. Fix #8447 (#8449)"

This reverts commit b12964501c116f758375c61389c6498c4baedb47.

* Revert "new format of schedd.submit)/spool() fix #8336 fix #8333 (#8448)"

This reverts commit 806226a154f55968c7d3007f513ab12fe9586088.

* Revert "do not indicate unused args in FTS calls. Fix #8460 (#8475)"

This reverts commit 20d4f900471dd3eb11b318455ae4a50e9b764d0f.
602f8d6b 2024-06-03 23:28:58 +0200 Stefano Belforte: workaround for #8456 (#8466)

198e2d37 2024-06-02 17:01:49 +0200 Stefano Belforte: do not set RequestCpus in task submission JDL. Fix #8456 (#8457)

b1296450 2024-05-31 16:54:15 +0200 Stefano Belforte: schedd.xquery is deprecated. Use schedd.query. Fix #8447 (#8449)

806226a1 2024-05-31 16:36:52 +0200 Stefano Belforte: new format of schedd.submit)/spool() fix #8336 fix #8333 (#8448)
* new format of schedd.submit)/spool() fix #8336 fix #8333

* pylint
793490e6 2024-05-27 10:25:33 +0200 Stefano Belforte: beware extra spaces in accelerator_jdl too (#8431)

40a796ff 2024-05-22 12:04:07 +0200 Stefano Belforte: sanitize extraJDL. See #8420 (#8423)

b603077c 2024-04-19 17:41:08 +0200 Stefano Belforte: use classad.quote, not HTCondorUtils. Fix #8332 (#8346)
* use classad.quote, not HTCondorUtils. Fix #8332

* pylint in HTCondorLocator
6f65ad6a 2024-04-12 13:00:42 +0200 Stefano Belforte: stop using AuthenticatedSubprocess. Fix #8277 (#8331)
* stop using AuthenticatedSubprocess. Fix #8277

* add explanation of why AuthenticatedSuprocess is still in HTCondorUtils

* pylint in DagmanSubmitter

* pylint in HTCondorUtils

* pylint in Handler
452dc411 2022-12-05 16:18:50 +0100 Thanayut Seethongchuen: New Site.acceleratorParams as json-like dictionary (#7470)
* accelerator params

* fix keyerror and change request gpu back to request_GPUs

Co-authored-by: Thanayut Seethongchuen <=>
8c51e4a5 2022-11-14 10:42:20 +0100 Stefano Belforte: stop using publishgroupname in REST. For #7359 (#7411)
* stop using publishgroupname in REST. For #7359

* do not write tm_publish_groupname in DB when inserting
26c17f3c 2022-01-18 23:06:17 +0100 Stefano Belforte: enable TaskWorker to use IDTOKENS. Fix #6903 (#6975)

e29ca43b 2022-01-17 12:07:19 +0100 Stefano Belforte: remove useless encode. fix #6972 (#6973)

c3262918 2021-12-22 11:10:56 +0100 Stefano Belforte: remove references to asourl/asodb in TW (#6929)

6965fcbd 2021-12-13 14:59:00 +0100 Stefano Belforte: Make tw work in py3 for #6899 (#6901)
* Queue is now lowercase, xrange -> range

* use python3 to start TW

* start TW from python3.8 dir

* workaround ldap currently missing in py3 build

* basestring --> str

* use binary files for pickle

* make sure to hande classAd defined as bytes as well
16a275f0 2021-10-26 14:28:14 +0200 Stefano Belforte: parent 23707a194a1df38cd8cda928c21b6723001a95ea (#6818)
Initial changes for python3. Make it possible to run with python3 on sched.
23707a19 2021-10-25 19:05:31 +0200 Stefano Belforte: Remove old dashboard (#6816)
* remove old dashboard code

* remove setDashboardLogs from ServerUtilities

* remove calls to setDashboardLogs

* remove calls to ApmonIf

* remove calls to ApmonIf

* remove calls to DashboardAPI

* remove last calls to old Dashboard code

* remove calls to Dashboard from sh scripts as well

* remove calls to Apmon from sh scripts as well

* syntax error in previous commits
c97deffb 2021-04-29 20:43:40 +0200 Stefano Belforte: Use CRABRest class in place of HTTPRequest everywhere and cleanup code (#6571)
* use CRABRest in Utils/TestRest.py

* use CRABRest in GenerateMONIT.py

* use CRABRest in aso_metrics_ora.py

* use CRABRest in TaskPublish.py

* pylint

* use CRABRest in PublisherMaster.py

* pylint

* remove old, commented, reference to HTTPRequest

* pylint

* fix #6576
2883f766 2021-04-15 16:14:14 +0200 Stefano Belforte: Use crab rest in tw fix6530 (#6536)
* use CRABRest in MasterWorker Fix #6530

* complete adaptint to CRABRest class and remove code to switch cmsweb-k8s-prod to cmsweb

* use correct API in postJob

* pylint


dc194f27 2021-02-17 21:54:29 +0100 Stefano Belforte: No cmsweb k8s prod fix 6407 (#6408)
* do not force REST host to cmsweb-k8s-prod

* stop manipulating resthost. Fix #6407

* stop manipulating resthost. Fix #6407
88b57650 2021-01-22 14:41:08 +0100 Stefano Belforte: add userAgent to HTTPRequest args and use it. Fix #6355 (#6358)
* add userAgent to HTTPRequest args and use it. Fix #6355

reduce the number of REST Server instantiations in TW

remove some old code (Dynamo e.g.)

use CRABClient as userAgent in getProxiedWebDir

* pylint fixes
e0a86e12 2020-10-27 10:04:23 -0500 Stefano Belforte: add some explanatory comments (#6220)

c470815b 2020-10-24 17:17:41 -0500 Stefano Belforte: do not pass K8s restHost to submitted jobs. Solve #6188 (#6213)

e99d084b 2020-09-22 15:06:26 +0200 belforte: improve return status from Actions

0ad8ced1 2020-09-14 11:13:41 +0200 Daina: Fix indentation

0a592f9e 2020-09-09 07:48:15 -0500 Stefano Belforte: When task submission has a problem do condor_rm before retry Fix #6145 (#6148)
* When task submission reports a problem, issue a condor_rm before retry. Fix #6145

* pylint complains
98cc1043 2020-09-08 12:53:22 -0500 Stefano Belforte: do not dump submission env. fix #6149 (#6150)

06a6a8fe 2020-07-31 08:38:11 -0500 Stefano Belforte: make sure user_groups is defined. Fix #6106 (#6107)
* make sure user_groups is defined. Fix #6106

* fix pylint complains

* fix more pylint complains
5ad34970 2020-05-13 15:17:00 -0500 Stefano Belforte: use new configuration. fix #6050 (#6052)

30eb6779 2019-12-24 11:25:32 +0100 Leonardo Cristella: Generalize message to 1 core jobs (#6004)
* Generalize message to 1 core jobs
4dd075c3 2019-12-15 13:47:19 +0100 Leonardo Cristella: Define constants in ServerUtilities.py (#6002)
* Define constants in ServerUtilities.py
279a24d6 2019-12-05 20:47:43 -0600 Stefano Belforte: sliding cut on maxReqMem. Fix #5995 (#5996)

e49db012 2019-11-06 22:54:48 -0600 Stefano Belforte: do not allow to request more than 10GB of RAM. Fix #5965 (#5981)

62ed8381 2019-11-06 20:32:05 -0600 Stefano Belforte: Fix 5966 (#5979)
* print failing schedd name in twlog next to time stamp

* print failing schedd name in twlog. fix #5966

67c45b2b 2019-07-11 23:47:26 +0200 Stefano Belforte: Fix 5913 (#5916)
avoid double quoting in classAds. Fix #5913
9e8efac5 2019-07-10 19:39:48 +0200 Leonardo Cristella: Do not perform the HTCondor query in the PreJob (#5914)
* Back to using file for webDir

* Replace deprecated parse methods

* Allow to tune maxIdle jobs
7e919f54 2019-05-13 21:35:21 -0500 Stefano Belforte:  fill monitoring classAds for jobs in universes 7 and 12 (#5892)
* fill monitoring classAds also for dagman and task_wrapper jobs. Fix #5890

8d2fedfd 2019-04-11 16:07:15 -0500 Stefano Belforte: improve message

1f49dd43 2019-03-14 01:57:47 +0100 Leonardo Cristella: Resolve #5827 (#5840)
* Resolve #5827

* Filter warning for numCores

* Add FAQ pointer to user message
83529bd3 2019-01-24 21:32:09 +0100 Stefano Belforte: set various classAds for MONIT (#5818)
* set CMS_TaskType andCMS_WMTool ads. Fix #5666

* add missing string terminator

* fix more stupid syntax errors

* report CMS_JobType not CRAB_JobType. Fix #5813

* fix pylint complains in older code

* fix again pylint complains in older code

* pylint is hard to please

* pylint is really hard to please

* typo in task['..']

* new classAds to be set need to be defined also in transform_strings()

* missing comma

* add CMS_Type and CMS_SubmissionTool. Fix #5820

* pylint says: line 440 in DagmanCreator.setCMS_Type: Redefining built-in type

* CMS_JobType is Analysis with capital A. See https://its.cern.ch/jira/browse/CMSMONIT-41?focusedCommentId=2423154&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-2423154

* string classAds need to be quoted

7d607c98 2018-08-23 12:20:43 +0200 Stefano Belforte: duplicateCheck should preserve clusterId in Task DataBase. Fix #5720 (#5721)

a0550be0 2018-06-01 18:05:36 +0200 Stefano Belforte: introduce MaxWallTimeMinsRun. Fix #5683

e93d3ca7 2018-01-16 18:04:24 +0100 Matthias Wolf: Fix probes transferring logs to the local SE.
Move the deactivation of log transfer and output stage-out from the
post-job to the pre-job. This required moving the transfer flags from the
generic Job.submit to the task class-ad and setting them correctly in the
pre-job.

bd0b6fe7 2017-08-31 15:37:53 +0200 Matthias Wolf: Fix resubmission with automatic splitting (#5568)
* Fix resubmission with automatic splitting

When using the external SubDAG line of DAGMan, HTCondor actively removes
remaining jobs in the queue when aborting a DAG due to failed nodes. This
includes tail SubDAGs and makes resubmission impossible. Make the DAGs
independent by submitting them when we previously created a submission file
only, and switch the DAG nodes to NOOP.

* Pacify jenkins.

5e692278 2017-08-03 15:14:50 +0200 Marco Mascheroni: Automatic refactoring (#5557)
* First prototype of PreDAG.py

* Refactor DAG creation.

* Clean up some crap.

* More fixes.

* Fix PostJob and PreDAG.

* More fixes.

* More fixes.

* Start coding tail jobs preparation both in PJ and PreDAG

* Fix even more stuff.

* More fixes to get the tail DAGs worked out.

* Fix logic error.

* Fix typo.

* More logic fixes.

* Fix typo.

* Style changes (and pylint)

* PreDAGs should be executed inside a lock

* We should run PreDags in parallel to include failed jobs

* Set splitting algorithm separately from DAG creation when running the PreDAG.

* Put failed job inputs into tails.

* Make sure execute is locked if called by TaskManagerBootstrap

* Don't attempt to grab throughput for failed jobs.

* Lock locally.

* Be more verbose.

* Have tails be 20% of the processing runtime, but at least 45m.

* Fix copy-paste mistake.

* Fix integer handling.

* Set conditions of subdag to dag ones.

* Fix JobIds checking for resubmission.

* Use recovery mode.

* Modify TaskType to match stage.

* Set tasktype better.

* Missing link for httplib2

* Automatic splitting resubmit implementation

* Only hold tail dags when resubmitting.

* Change leave job in queue.

* Few changes to make sure all the dags ends when the task is completed

* Documentation and style refactoring

* Add a first implementation fo unit tests for PreDAG (automatic splitting)

* Add files for automatic splitting unit tests

* Make job_id strings in filetransfersdb

* Reduce retries for automatic splitting.

Currently, all jobs are run/retried 3 times. That means that for automatic
splitting, every lumi is run/retried 3 + 3 (from tails) times. Reducing retries
for processing to 0 will reduce this to 1 + 3 possible processing attempts.

fccc08c0 2017-07-04 16:56:28 +0200 Marco Mascheroni: Improve task lifetime management (#5534)
* add CRAB_TaskLifetimeDays and CRAB_TaskEndTime classAds. Fixes #5505

* remove grid jobs at CRAB_TaskEndTime. Fixes #5507

* use new classAds CRAB_TaskLifetimeDays and CRAB_TaskEndTime forTask control. Fixes #5506

f8770011 2017-05-12 23:07:41 +0200 Matthias Wolf: Adjust probe walltime to fit better into pilots. (#5480)
Also add some stubs to take care of tail jobs.
1ad3fd62 2017-04-24 10:40:11 +0200 Marco Mascheroni: Fix list treatment for DAG settings. (#5468)

3398854c 2017-03-31 13:10:51 +0200 Marco Mascheroni: Make ldap optional for devs, fix x509 bug (#5456)

dcfdaf16 2017-03-28 17:51:36 +0200 Marco Mascheroni: Use user x509 proxy for collector queries in DagmanSubmitter (#5452)

a22ae643 2017-02-23 14:04:09 +0100 Emilis Rupeika: Set walltime correctly if it exceeds 47h. Fix #5215 (#5401)
* Set walltime correctly if it exceeds 47h. Fix #5215

* Some refactoring for DagmanSubmitter

14f97eb2 2017-02-21 16:33:55 +0100 todor-ivanov: Increasing the time for keeping the dagman into the queue. (#5394)

80b9a791 2017-02-16 11:12:04 +0100 Emilis Rupeika: Fix uninitialized logger bug in new schedd picker function (#5375)
* Fix uninitialized logger bug in new schedd picker function

* Pass logger correctly to picker func

18d89afa 2017-01-23 11:01:15 +0100 Marco Mascheroni: Make sure TW subprocesses do not hang indefinetly if condor commands do not respond (#5350)

bae8ca74 2016-11-15 11:45:17 +0100 Marco Mascheroni: Merge with the master

8e6ec960 2016-10-25 12:00:12 +0200 Emilis Rupeika: Minor fixes for WMCore 1.0.21 (#5303)

974ad6c5 2016-09-02 09:43:40 +0200 Marco Mascheroni: Merge branch 'master' of github.com:dmwm/CRABServer into automated_splitting
Conflicts:
	scripts/task_process/cache_status.py
	src/python/TaskWorker/Actions/DagmanCreator.py
	test/templates/CMSSW_VALIDATION/cmssw-validation.sh
	test/templates/client_validation.sh
	test/templates/validation.sh

c1cd30c9 2016-08-15 16:01:01 +0200 Marco Mascheroni: Fix error when schedd list is empty after retries (#5275)

0323c312 2016-08-15 15:51:33 +0200 Stefano Belforte: allow = sign in the extraJDL classad (#5272)

fe3b3fc9 2016-07-20 09:41:14 +0200 Marco Mascheroni: Solve conflicts

812ef5d4 2016-06-09 17:11:29 +0200 Marco Mascheroni: Pick up a new schedd only after retries for current one are exhausted
This also make sure statistics are reported correctly. Plus some other minor log printout changes

968c382f 2016-05-26 11:01:15 +0200 Marco Mascheroni: Merge from master (3.3.1606.rc4)

ca4c7bdb 2016-05-25 11:56:56 +0200 Marco Mascheroni: Make sure we do not retry a schedd after max_retry failures

e9bb1c95 2016-05-24 05:47:38 +0200 Marco Mascheroni: Validate configuration and pass scheddPickerFunction function

1b37fea3 2016-05-24 03:48:35 +0200 Marco Mascheroni: Finish changes for duplicate check in DagmanSubmitter

3e2cb7fd 2016-04-22 16:42:39 +0200 Marco Mascheroni: Retry failure that may succeds

a7ab7b4d 2016-03-22 21:24:01 +0100 Marco Mascheroni: Retry the duplicate check if the dag status is 5

052dc459 2016-03-22 13:14:40 +0100 Marco Mascheroni: Refactoring: create a method to check user's memory and walltime values

0cef8ba5 2016-03-22 12:37:10 +0100 Marco Mascheroni: Refactoring: create a method to get the list of schedds

0c644bb4 2016-03-22 12:23:33 +0100 Marco Mascheroni: Replace kwargs['task'] with task in DagmanSubmitter

e7291748 2016-03-22 12:15:19 +0100 Marco Mascheroni: Remove useless try/except

92cad545 2016-03-22 12:14:29 +0100 Marco Mascheroni: Let the TW retry the duplicatecheck

df477635 2016-02-17 15:16:34 +0100 Justas Balcas: Check if task is really correctly submitted.

e321205a 2016-05-19 12:09:50 +0200 Marco Mascheroni: Take care of review for #4681 (remove taska fter 30 days)

a03ad202 2016-05-03 12:13:25 +0200 Marco Mascheroni: Make sure a task is removed after 30 days. See #4681

f24e47f2 2016-04-05 17:44:23 +0200 Marco Mascheroni: Adding clusterid to the database, minor status code refactoring.

a84ac498 2016-03-24 09:59:44 +0100 Matthias Wolf: Get everything nearly working.
Currently fails trying to upload the file metadata (panda job id is
supposed to be integer).

3c586eab 2016-03-23 16:57:57 +0100 Matthias Wolf: Inch towards a working subdag.

0e12283d 2016-03-23 16:32:34 +0100 Marco Mascheroni: Print dashboard information only for the last job

3aafbcae 2016-03-23 16:24:37 +0100 Marco Mascheroni: Print clusterid and schedd of the task just submitted. Fixes #5184

a044c80d 2016-03-22 22:53:46 +0100 Marco Mascheroni: Print cluster id of the condor job in the TW log

cad0c40a 2016-03-21 15:44:25 +0100 Marco Mascheroni: Merge pull request #5175 from mmascher/state-machine
State machine
bfcdabb0 2016-03-16 12:57:38 +0100 Marco Mascheroni: Some code cleanup in RESTWorkerWorkflow: remove unused runs, lumis and jobset params

34ef7c51 2016-03-15 12:58:05 +0100 Marco Mascheroni: Retrying Task DB updates: add missing retry and fix log

78d51c41 2016-03-14 15:55:50 +0100 Marco Mascheroni: Be more aggressive with retrying Task DB updates

f075ceda 2016-03-14 12:07:21 +0100 Marco Mascheroni: Schedd stats are wrong in TW

55aceed7 2016-02-14 11:11:47 +0100 Marco Mascheroni: Merge pull request #5046 from AndresTanasijczuk/filesForReport
Save input dataset lumis from DBS data discovery to file in schedd.
73652654 2016-01-30 10:24:03 +0100 Marco Mascheroni: Changes to taskworker, postjob and cmscp for configurable aso database

a4bc07f9 2016-01-14 14:32:33 +0100 Marco Mascheroni: Print the environment used for task submission when there is a failure

fb65e525 2016-01-13 12:06:14 +0100 Marco Mascheroni: Print schedd stats in slave processes

148e2598 2015-11-02 10:36:42 +0100 Andres Tanasijczuk: Fixes for report.

f5aeab71 2015-10-23 12:04:40 +0200 Andres Tanasijczuk: Fix pre-python 2.6 idioms. Some pylint fixes.

1dbdb21c 2015-10-22 19:37:53 +0200 Andres Tanasijczuk: Save input dataset lumis from DBS data discovery to file in schedd. Save also the duplicate lumis to file in schedd.

307cec85 2015-12-03 16:29:07 +0100 Marco Mascheroni: Allow using VOMS group for using local pilot in gWms. Fixes #5090

656bcf96 2015-11-18 10:42:42 +0100 Andres Tanasijczuk: Fix bytes -> MB in messages

540e0a33 2015-10-20 19:10:20 +0200 Marco Mascheroni: Merge pull request #5037 from AndresTanasijczuk/primds
Add primarydataset parameter. Fixes #5031
e5832ee6 2015-10-09 15:10:03 +0200 Andres Tanasijczuk: Add primarydataset parameter.

c66a1042 2015-10-16 08:15:45 +0200 Andres Tanasijczuk: Remove leftovers used only by submitRaw.

711b39af 2015-10-05 18:11:51 +0200 Marco Mascheroni: Change stdmaxjobruntime to 2750

a6568804 2015-10-01 09:40:04 +0200 Justas Balcas: Pylint improvements of whitespace, invalid-name, logging-not-lazy

32a5339f 2015-10-01 08:54:45 +0200 Justas Balcas: Remove gsissh from TW

dfc5155f 2015-09-17 11:35:50 +0200 Marco Mascheroni: Harmonize classad names with WMAgent. See #4856

a2e2fdf7 2015-09-16 15:07:56 +0200 Marco Mascheroni: Reorganize import in DagmanSubmitter

68ad9a35 2015-08-27 01:32:06 +0200 Andres Tanasijczuk: Add FEEDBACKMAIL and minor modifications to error messages.

586ec7dc 2015-08-27 01:25:22 +0200 Andres Tanasijczuk: Bug fix: self.workflow -> workflow

bbb3e75a 2015-08-27 01:20:25 +0200 Andres Tanasijczuk: Remove unneccessary variables.

ae8a3daa 2015-08-27 01:17:54 +0200 Andres Tanasijczuk: Fix retryIssues: don't accumulate all issues for all schedds.

81af6463 2015-08-27 00:59:20 +0200 Andres Tanasijczuk: Make list of good schedulers a set.

f52aa471 2015-08-27 00:57:46 +0200 Andres Tanasijczuk: Use variables for the standard maxmemory and maxjobruntime.

febf83b5 2015-08-27 00:55:35 +0200 Andres Tanasijczuk: Rename keyword arguments variable from kw to the more standard kwargs.

49f66eff 2015-08-19 14:27:45 +0200 Marco Mascheroni: Remove unused classad CRAB_BlacklistT1. See #4950

bb1a234a 2015-08-06 10:53:28 +0200 Marco Mascheroni: Fix commit about retry of cmsweb updates

2421d8c3 2015-08-05 17:44:26 +0200 Marco Mascheroni: Retry task updates to cmsweb more than one time and print failures. See #4926

ca31d004 2015-08-03 17:11:57 +0200 Marco Mascheroni: Add a missing commit for proxied webdir (#4883)
Converting the dictionary to a list to take only the keys. Allows
backward compatibility for old external configurations.

bc7eb58d 2015-07-17 20:31:46 -0500 Brian Bockelman: Fix the RemoteCondorScript idea.
This allows us to have a per-schedd environment setup script (in case
we want different condor configs depending on which schedd is used).

1fb39e5d 2015-07-15 19:27:40 +0200 Marco Mascheroni: Manically add debug printout to DagmanSubmitter

b4086e4e 2015-06-24 18:18:21 +0200 Marco Mascheroni: Merge pull request #4828 from juztas/patch-23
timeout gsissh connection after 60s. Fixes #4827
66e78900 2015-06-12 16:36:11 +0200 Andres Tanasijczuk: Use groupname for output dataset name when outLFN is in /store/group. Fixes #4825

8486e239 2015-06-10 12:59:43 +0200 Justas Balčas: timeout gsissh connection after 60s. Fixes #4827

da41124d 2015-05-06 20:40:49 +0200 Justas Balcas: Fix except to use what python2.6 recommends

92aa0ecb 2015-04-28 22:33:09 +0200 Marco Mascheroni: Merge pull request #4777 from bbockelm/map_user_to_groups
Map user to groups
2e617c35 2015-04-20 05:04:01 +0200 Marco Mascheroni: Merge pull request #4758 from juztas/reasonableMemory
Memory and walltime warnings
be695ad6 2015-04-14 21:11:54 -0500 Brian Bockelman: Allow CVMFS-based group mapping to be done on either the TW or the schedd.
Fixes a few bugs from the prior commit.

145bb20b 2015-04-13 11:21:43 +0200 Justas Balcas: Memory and walltime warnings This pull request will not allow to submit/resubmit with walltime bigger then 2800, CRAB3 will change to 2800 Gives warning for submit/resubmit of memory bigger then 2500 and walltime bigger then 2800 It is one line add for shuffling good schedulers list and not using it static

8ea5a939 2015-04-13 15:21:48 +0200 Justas Balčas: fix typo setDefault

1c6d7f58 2015-04-07 16:34:40 +0200 Justas Balčas: Allow to submit to any scheduler for testing on different pool
I have introduced this bug in current pre-prod version. We were not able to submit to ITB, because CRABServer shows to global pool rest configuration. In case schedd is not in the list of good schedulers, use only one schedd.

c812d1c1 2014-12-03 12:43:34 +0100 Andres Tanasijczuk: Fix resubmit options (can resubmit specified jobs; can overwrite site black/white list, maxmemory, maxwalltime, numcores and/or priority for the resubmitted jobs without affecting other jobs). Allow resubmission of successful jobs if jobids option is given. To achive controled resubmission of single jobs, run condor_dagman in recovery mode (and not in rescue mode). Remove unnecessary attrs CRAB_SiteResubmitWhitelist and CRAB_SiteResubmitBlacklist. Don't do the copy of Job.sumit to Job.jobid.submit in AdjustSites.py. Finally, some code clean-up, small reorderings, variables renaming and addition of many comments.

2eca62d5 2015-03-18 22:46:09 +0100 Marco Mascheroni: Fixes in DagmanSubmitter
Need to account for max_retries=0.
Bad spelling of retry (was retries)

2be175de 2015-03-18 17:16:05 +0100 Andres Tanasijczuk: Don't hard-code the number of automatic job retries. Instead read it from the TW config and add it to the job ad. If not specified in the TW config, use default of 2. Rename function adjustPost --> adjustPostScriptExitStatus in AdjustSites.py. Rename function resubmitDag --> adjustMaxRetries n AdjustSites.py.

b1f2c66b 2015-03-16 23:46:29 +0100 Justas Balcas: updateschedd API needed for late binding of schedd. Needed for CMSWEB

36aa8c4c 2015-03-16 22:41:41 +0100 Anna Elizabeth Woodard: 1. Add a 'dryrun' flag entry in the DB 2. Create a 'splitting summary' 3. If the 'dryrun' flag is set: do not report to dashboard or submit job; instead, upload DagmanCreator materials in a tarball to the UserFileCache and set task status to 'UPLOADED' 4. Implement a 'proceed' API the client can use to ask for a task in the 'UPLOADED' state to be reset to 'NEW'
Fixes #4462.

befed0db 2015-03-03 14:54:53 +0100 Justas Balčas: Bug found after production TW upgrade (workflow unknown)

1a720374 2015-02-16 16:29:52 +0100 Marco Mascheroni: Merge pull request #4669 from dmwm/fixes
Fixes for 1) warning messages and 2)phedex unresponsive
bbd6b885 2015-02-13 14:10:38 +0100 Marco Mascheroni: Merge pull request #4638 from juztas/late_binding
Late binding of schedd. Fixes #4629
61726848 2015-02-11 16:58:48 +0100 Justas Balčas: Remove reschedule as it is not needed anymore
After discussion with @bbockelm : Turns out, it already calls reschedule() in the 8.3.x series
390634b2 2015-01-16 22:15:25 +0100 Marco Mascheroni: Improve the error when phedex is unresponsive. Fixes #4581

4de0861c 2015-02-03 16:00:09 +0100 Justas Balčas: Move schedd.reschedule to be used with user_proxy
reschedule requires authentication, so moving this after schedd.edit and to be used with HTCondorUtils.AuthenticatedSubprocess. reschedule is just an optimization - otherwise if we don`t have this, it may take up to 5 minutes about new jobs
1ce9b167 2015-01-20 11:28:55 +0100 Justas Balcas: Late binding of schedd. Fixes #4629 This pull request also have backward compatability for tasks submitted before. After some time(2months) need to clean up. Schedd choose is done in CRABServer and will create a new issue for TaskWorker to allow change scheduler and update it in CRABServer database. Also this pull request allows to name crab3 shedds `vocms095.cern.ch` and it is not required anymore to have `crab3test-1`. If we will change schedd names from `crab3test-2@vocms095.cern.ch` to `vocms095.cern.ch`, we have to update all collumn in database which points to old name.
P.S. This pull request is not for February release.

9864d199 2015-01-08 21:38:11 +0100 Justas Balcas: Possibility to specify collector. Fixes #4565

c84f1a2a 2014-11-29 01:40:09 +0100 Marco Mascheroni: Naming conventions of UR* parameters in TW. #4544
Review the naming convention of parameters like resturl, resturi,
instance etc.

Take for example a REST URI (e.g.: '/crabserver/prod/workflowdb'). The
first field in the REST URI (e.g. 'crabserver') will be called the
server API. The second field (e.g. 'prod', 'preprod', 'dev') is the REST
database instance. The third field (e.g. 'workflowdb', 'info',
'filemetadata') is the REST API.

6e26cc94 2014-10-23 14:52:31 +0200 Andres Tanasijczuk: In cmscp: 1) inject to ASO after all local transfers are successfull; 2) do same stagoeut policy for all files; 3) clean storage if stageout failes; 4) upload log file metadata from WN; 5) add cmscp exit code to job report; 6) and more... Add rest_host, rest_uri, source_lfn and destination_lfn to ASO docs.

8390c7e2 2014-11-20 00:41:02 +0100 Justas Balčas: Raise TaskWorkerException. Fixes #4494

b639a4b3 2014-11-18 16:47:25 +0100 Marco Mascheroni: Merge pull request #4493 from juztas/lumi_to_file
Save lumis in file and all in tarball. Fixes #4476
4e84bc4b 2014-11-03 15:50:45 +0100 Justas Balcas: ASOURL not known. Fixes #4486

d02768f9 2014-11-02 21:19:13 +0100 Justas Balcas: Save lumis in file and all in tarball

1c2f7b96 2014-10-31 00:07:45 +0100 Marco Mascheroni: Use non-blocking schedd.xquery instead of blocking query

9beef2ad 2014-10-22 13:31:47 +0200 Marco Mascheroni: Improve error messages in the TaskWorker. Fix #4471

ed4a6a37 2014-10-13 17:55:01 +0200 Marco Mascheroni: Do not upload filemetadata if CRAB_NoWNStageout is used

229bd2e3 2014-10-13 16:48:12 +0200 Marco Mascheroni: Simple typo in a message

fe873816 2014-09-15 08:46:37 +0200 Justas Balcas: Save webdirurl in database.
Signed-off-by: Justas Balcas <juztas@gmail.com>

b28a75f4 2014-08-31 17:06:11 +0200 Justas Balcas: Missing check for uisource. Fixes #4398

5a99ff10 2014-08-19 16:16:48 +0200 Justas Balcas: small fixes, don`t encode failures twice. Validation script fixes
Signed-off-by: Justas Balcas <juztas@gmail.com>

5c9e86e2 2014-07-18 12:12:42 +0200 Marco Mascheroni: Improve error messaging in the MasterWorker

c12ddf14 2014-07-10 19:56:33 +0200 Andres Tanasijczuk: Remove CRAB_SkipASO from dagAd, since it is not used anymore.

da3ec4a8 2014-07-07 17:04:44 +0200 Justas Balcas: Retry policy in TW

f5966b0a 2014-06-20 17:30:38 +0200 Andres Tanasijczuk: Propagate transferOutput, saveLogs and publication flags from client up to ASO. Don't publish files that are not EDM.

f667cc6f 2014-05-07 15:58:25 +0200 Brian Bockelman: Fix LeaveJobInQueue logic.

3a6f278d 2014-05-07 15:55:28 +0200 Brian Bockelman: Auto expire tasks after 30 days.

cfdf23c5 2014-03-12 15:20:58 +0100 Marco Mascheroni: Add the possibility to remove and configure the ASO timeout on the postjobs, add the possibility of disabling transfer retries

3115d525 2014-03-11 03:04:26 +0100 Brian Bockelman: Bugfixes for bulk ASO poll.

75b85ca9 2014-03-10 16:44:49 +0100 Brian Bockelman: Switch to a JSON-based format for the site ad to reduce prejob usage.

7e0beeb0 2014-03-04 09:38:34 -0600 Brian Bockelman: Merge pull request #4210 from mmascher/master
Do local stageout no matter what if saveLogs=False. #4206
94bc44dc 2014-03-04 15:33:10 +0100 Brian Bockelman: Record task worker name in task and job ads.

b25abc60 2014-03-03 18:47:47 +0100 Marco Mascheroni: Do a gsissh before submitting a task. Fixes #4223

2460f846 2014-02-24 22:54:49 +0100 Brian Bockelman: Make post-job count and dashboard task type operator-configurable.

a982093c 2014-02-22 16:55:12 +0100 Brian Bockelman: DashboardFailure script should go in runtime tarball, not to schedd environment.

50a1f525 2014-02-22 09:32:38 -0600 Brian Bockelman: Report to dashboard using system python if the CMS python is unusable.

639db720 2014-02-03 17:01:27 +0100 Brian: Allow the DAG to be aborted after a number of node failures.

1fbb8cc4 2014-01-27 17:23:47 +0100 Brian: Fix syntax error with ASO URL.

99c7c8bb 2014-01-26 15:46:22 +0100 Brian Bockelman: Implement minor feature requests.
This includes:
 - Pass ASO URL to the backend and use ASO by default if configured
   to do so.
 - Allow user to request we ignore file locality.
 - Allow user to request we skip ASO.

96dab6ea 2013-12-21 03:03:26 +0100 Brian: Rewrite how site list calculations are done.
Site lists are now calculated in the PreJob instead of at submit
time.  This allows us to be more dynamic in automatically blacklisting
sites and makes changing the available sites less dynamic.

The list of available sites for a given job as an output from data
discovery is transferred as a separate file.

f9f8e55f 2013-12-20 22:31:02 +0100 Brian: Add initial support for runtime attributes and automatic blacklisting.

8f4b0906 2013-12-05 16:59:39 +0100 Marco Mascheroni: Move HTCondor* modules up one level and include them in setup.py

380bd661 2013-12-04 22:28:16 +0100 Brian: Record the user's VO / role / group in the task classad.

4f78311c 2013-11-27 23:18:14 +0100 Brian: First attempt at using TaskWorker-local runtime tarballs.

64f21908 2013-11-19 16:20:00 +0100 Marco Mascheroni: Move htcondorSchedds and htcondorPool parameters to the external configuration file on the REST

79ca3044 2013-11-19 05:10:05 +0100 Brian: Start TaskWorker side of schedd-load-balance.

1d11cf45 2013-11-19 04:14:55 +0100 Brian: Add preliminary support for the UFC.

686937a6 2013-11-18 16:59:43 +0100 Brian: Remove ASO submit file from list of input.

8f7aa9a1 2013-11-12 03:49:28 +0100 Brian: Switch to scheduler universe so we can propagate the correct hold signal.

60f2af86 2013-11-05 22:45:01 +0100 Brian: Beginning of Dashboard integration.  UDP packets are sent, but dont show up in Dashboard - will follow up with that team.

84d903e8 2013-11-05 17:25:00 +0100 Brian: Rewrite the DAG on the fly after resubmits so we can update the black/white lists.

2a0f2a4b 2013-11-04 03:11:22 +0100 Brian: Record the number of jobs in the DAG job ad.

693d25c1 2013-10-30 19:59:39 +0100 Brian: Fix runtime environment for PostJob.

8786ca0d 2013-10-24 08:54:44 -0500 Brian Bockelman: Migrate CAFTaskWorker into CRABServer.

