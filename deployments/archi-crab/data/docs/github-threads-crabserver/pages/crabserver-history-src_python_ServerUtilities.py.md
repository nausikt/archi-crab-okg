# dmwm/CRABServer: commit history of src/python/ServerUtilities.py (at 30286f7d5b21)

URL: https://github.com/dmwm/CRABServer/commits/master/src/python/ServerUtilities.py

c70345af 2026-09-04 13:13:11 +0200 Krittin Phornsiricharoenphant: clean-up test11. (#9413)
* clean-up test11.

* fix old typo in comment

* fix test11 was left in .gitlab-ci.yml

---------

Co-authored-by: Stefano Belforte <stefano.belforte@gmail.com>
eb8db5c5 2026-08-28 17:30:19 +0200 Krittin Phornsiricharoenphant: Refined and New ASO ExitCodes 60XXXs and their regexes. (#9400)
* refined new 60XXXs ASO ExitCodes, and their regexes.

* add missing TRANSFER SSL connection error, adjust err-mesg to preserve original mesg.

* revise to have scope-specific/generic ExitCodes, 60326,60327,60328.

* migrate legacy site-related issues 60321 to 60328 due to  numerical ordering reasons.

* fill missing curl error set, adjust ordering.

* add bare minimum isPermanent i.e. curl 3 (bad request), and http 404.

* revised 60325 error mesg.
ee725156 2026-06-15 11:58:49 +0200 Vijay Chakravarty: Use RRN and Exitcodes to overhaul resubmission and retry policy (#9319)
* use rrn

* json missing

* use job classad CRAB_RRN

* reuse_rrn

* coalesce new rrn with old exitcode policy

* 10 max retries

* satisfy pylint warnings

* correct comments
8b74e054 2025-12-13 17:28:19 +0700 Krittin Phornsiricharoenphant: make atomicReplaceAcrossFS a py2 compatible. (#9248)

5e84119c 2025-12-05 10:17:05 +0700 Krittin Phornsiricharoenphant: add safe lock on run_and_lumis, even in sequentially synchronized pla… (#9233)
* add safe lock on run_and_lumis, even in sequentially synchronized places like from PreDAG -> DagmanCreator.

* more specific lock, cover input_files locking.

* remove unnecessary lock.

* introduce atomic_move_to_spool.

* try to use atomic_move_to_spool on one of potential writer.

* PoC, on updating tarball at local first then atomic moving back to SPOOL.

* fix incorrect intermediate files naming, patch more clarity PoC.

* since it's more like upsert Tarballs, we have to explicitly check tarball existences in cases newly create tarball.

* wrap atomic update tarball as fn, rebuild_spool_tar_from_dir.

* preserve CRAB fn naming convention.

* remove no longer necessary Reader Locks.

* fix forgot to changed fn name in ServerUtilities.

* fix forgot to import tempfile.

* more CRAB's caMelCase naming convention for vars.

* fix typos.

* forgot to import tarfile

* remove path overloaded operator style, remove too compact low value fn.

* fix words and naming for more clarity.

* fix writter around tarballDir is already fine.

* remove unused import.

* formating, no new line.

* atomic copying input_files.tar.gz, CMSRunAnalysis.tar.gz as well.

* more clarity naming, docs.

* better be Cross than Across.

* clean-up localTempDir.

* fix final fn name to `AcrossFS`.
052d3992 2025-10-10 09:55:25 +0200 Stefano Belforte: only 3GB max mem for 1core at initial sub. Fix #9206 (#9207)
* only 3GB max mem for 1core at initial sub. Fix #9206

* add pointer to policy

* when asking too much in resubmt, allow to try again
18fdf540 2025-07-01 21:45:11 +0200 Stefano Belforte: remove unused service instances

a23e98a8 2025-04-08 18:05:36 +0200 Stefano Belforte: set default to 10 for MaxPost in Dagman. Fix #9034 (#9037)

c51853ef 2025-02-27 14:08:29 +0100 Stefano Belforte: reformat PreJob. Fix #8938 (#8949)

0445524d 2024-11-25 22:47:07 +0100 Stefano Belforte: use python2 compatible Popen. Fix #8811 (#8826)

76a4def7 2024-11-25 15:40:46 +0100 Stefano Belforte: use curl for http HEAD call. Fix #8811 (#8813)

256760aa 2024-10-18 02:33:11 +0200 Stefano Belforte: add checkS3Object and verify S3 upload with it (#8740)
* add checkS3Object and verify S3 upload with it

* pylint

* pass also taskname to checkS3Object
c5d4248f 2024-10-11 21:02:14 +0200 Stefano Belforte: correct use of rucio.get_local_account_usage. Fix #8738 (#8739)

88f83517 2024-09-30 15:02:30 +0200 Stefano Belforte: Remove extra files from TW tarballs (#8718)
* remove extra files from TaskManagerRun.tar.gz

* remove extra files from CMSRunAnalysis.tar.gz

* avoid using ServerUtilities in cmscp.py
9199c3a4 2024-09-04 16:22:33 +0200 Vijay Chakravarty: Task scheduling (#8676)
* adding task scheduling

* Initialising tw_name with 'any' to fix issue https://github.com/dmwm/CRABServer/issues/8618

* Changing any to crab-prod-tw01:testing

* Final changes: fixing key names

* Removing configreq reference

* fixing EOL

* Lazy logging

* Change selectwork comment and make use of return value

* Adding an Adhoc section in the configuration and using it to set the selection_limit

* Removing hardcoded tw_name value from Task.py and making use of SQL bindings

* Adding logging capability in task scheduling

* Adding a dry_run option under Adhoc to make user and task count logging conditional

* Making round robin task scheduling as an option for dry_run. All waiting tasks are returned if dry_run is false.

* Change Adhoc to TaskScheduling and logging a table of username waiting and selected tasks

* Default dry_run for taskscheduling set to True

---------

Co-authored-by: Vijay Chakravarty <vijay.chakravarty@cern.ch>
Co-authored-by: Vijay Chakravarty <vchakrav@cern.ch>
9660271e 2024-08-29 10:35:04 +0200 Thanayut Seethongchuen: add test14 (#8669)

414396a1 2024-08-10 01:14:11 +0200 Stefano Belforte: use TaskWorkerConfig to enable use of V2 bindings (#8595)
* use TaskWorkerConfig to enable use of V2 bindings

* pylint

* fix Main.py

* addres comments from Wa
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
839f10b4 2024-07-24 12:52:31 +0200 Thanayut Seethongchuen: add Vijay's dev env (#8555)

f8ab446e 2024-05-16 23:07:30 +0200 Stefano Belforte: Update ServerUtilities.py MaxTBtoRecal is 1, not 10PB
it was a typo. 1PB was meant as per https://github.com/dmwm/CRABServer/issues/7610
d4b13331 2024-05-16 00:33:33 +0300 Fredrik: Fix typos in output strings (#8408)

5f3ab24a 2024-03-25 23:37:01 +0100 Stefano Belforte: Correct fix for 8285 overrides 8296 (#8302)
* parseJobAd does not need classad.parse and add comments

* use parseOne not parseAds in place of parseOld. Fix #8285

* no need for parseJobAd in PreDAG. Use classad.parse

* no need for parseJobAd in PostJob. Use classad.parse

* remove unused code from TaskMagerBootstrap + pylint

* pylint in PreDAG

* remove unused code
4e2ba291 2024-03-18 19:43:53 +0100 Stefano Belforte: use classad.paraseAds - fix #8285 (#8296)

19adcac6 2023-11-30 11:54:52 +0100 Stefano Belforte: make it syntax-compatible with python2. Fix #8028 (#8030)
* make it syntax-compatible with python2. Fix #8028

* fix pylint at line 1133
6d3d7258 2023-11-07 20:53:27 +0100 Stefano Belforte: add FTS error status code 507 for WebDav. Fix #7863 (#7998)

34371ca2 2023-11-07 18:20:50 +0100 Stefano Belforte: move STAGEOUT_ERROR from WMCore to ServerUtilities (#7995)
* move STAGEOUT_ERROR from WMCore to ServerUtilities

* pylint and pep8
47875c8c 2023-11-03 16:08:26 +0100 Thanayut Seethongchuen: Move Rucio check write logic to ServerUtilities.py (#7987)

88c9de0b 2023-07-17 09:55:58 +0200 Stefano Belforte: move DataRecall and DataLock to separate file (#7750)
* move DataRecall and DataLock to separate file

* use a single class in Rucioactions

* fix pylint and pep-8

* move MAX_LUMIS to ServerUtilities with all constants

* complete pylint fixes
9a1f2b0c 2023-05-25 10:38:21 +0200 Stefano Belforte: refactor requestTapeRecall and accept dataset name. Fix #7603 (#7641)
* refactor requestTapeRecall and accept dataset name. For #7603
29619d6b 2023-05-03 14:09:01 +0200 Stefano Belforte: Refactor tape recall (#7620)
* introduce KILLRECALL status FIx #5608

* add TapeRecallManager fix #7406

15329d8e 2023-04-20 16:45:01 +0200 Stefano Belforte: wait 15d max for tape recalls (#7612)

6ade5a68 2023-04-14 00:18:00 +0200 Stefano Belforte: 30 days for recall and 30 days for processing. Fix #7590 (#7591)

9f6fd04c 2023-02-10 15:58:55 +0100 Thanayut Seethongchuen: new params inputblocks and support running on datablock (#7525)
remove redundancy on checking user inputdataset, and

verify if blocks belong to dataset

remove unused regex for pr, remove rucio alternative cert

allow USER dataset

remove unused import

Revert "remove unused import"

This reverts commit 7c43666a152339c8b0e9a2ee6838f7c4543dd275.

wrong file

remove unused import

Co-authored-by: Thanayut Seethongchuen <=>
64257a3a 2022-10-27 16:26:08 +0200 Thanayut Seethongchuen: Add new test12/devthree env (#7442)
* test12

* test12 in craserver ui

Co-authored-by: Thanayut Seethongchuen <=>
e765269e 2022-07-25 18:32:01 +0200 Thanayut Seethongchuen: Fix: forget to add modulename and label to log in measure_size function (#7351)
Co-authored-by: Thanayut Seethongchuen <=>
eab7b5d7 2022-07-25 16:41:51 +0200 Thanayut Seethongchuen: new measure_size function with log, change log format (#7345)
Co-authored-by: Thanayut Seethongchuen <=>
5c777704 2022-07-13 11:43:30 +0200 Thanayut Seethongchuen: Load data from db before streaming to client (#7255)
* load data to memory instead of streaming

* add toggle switch, return _FakeLOB instead of string,

* use MeasureTime in all function, MeasureTime accept None logger

Co-authored-by: Thanayut Seethongchuen <=>
76c59fa8 2022-05-23 18:37:05 +0200 Dario Mapelli: rest cache - measure s3 timeouts (#7256)

acfdfbf5 2022-05-19 23:34:13 +0200 Thanayut Seethongchuen: add devtwo (#7258)
Co-authored-by: Thanayut Seethongchuen <=>
48be5e17 2022-03-28 15:28:25 +0200 Dario Mapelli: remove b64encode/decode, use RX_ANYTHING_MULTILINE instead of RX_TEXT_FAIL. (#7106)

db170c62 2022-03-18 15:33:35 +0100 Stefano Belforte: temporary hack to avoid HTTP code strings in messages (#7147) (#7148)

77268992 2022-02-25 17:51:30 +0100 Stefano Belforte: point user feedback to CmsTalk. Fix #7100 (#7101)

2f365818 2021-11-30 22:56:35 +0100 Stefano Belforte: add comments

f47285bb 2021-10-30 13:59:52 +0200 Stefano Belforte: Remove couch db code (#6848)
* remove couchDb related code. Easy part for #6834

* remove CouchDB code from DagmanResubmitter. For #6845

* remove CouchDB code from PostJob. For #6845

* remove isCouchDBURL, now unused. For #6845

* one more cleanup in PostJob. For #6845

* one more cleanup in PostJob. For #6845

* restore code deleted by mistake
f161af09 2021-10-28 13:41:16 +0200 Stefano Belforte: Belforte patch 1 (#6825)
* use gocurl from CVMFS Fix #6822 (#6823)

* add comment about py2/3 compatibility needs
06cdc5be 2021-10-28 13:35:34 +0200 Stefano Belforte: use gocurl from CVMFS Fix #6822 (#6824)

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
6d339619 2021-09-30 17:03:47 +0200 Stefano Belforte: only print stderr from curl in case it fails (#6790)

1d7ae3ee 2021-07-16 11:48:39 +0200 Daina: Merge pull request #6698 from ddaina/testGoCurl
add option to use gocurl for s3 operations (fix #6685)
1f88e8de 2021-07-16 10:43:35 +0200 Daina: fix how CRAB_useGoCurl is used

4ba44ab6 2021-07-15 22:33:36 +0200 Stefano Belforte: remove references in the code to old k8s cluster (#6700)

f010be93 2021-07-15 11:16:01 +0200 Daina: add option to use gocurl for s3 operations (fix #6685)

a4ebe0b7 2021-06-21 14:51:30 +0200 Stefano Belforte: import fixed version of execute_command from Client. Fix #6646 (#6654)

0812a642 2021-06-15 14:10:34 +0200 Stefano Belforte: make curl work for CMSSW_7* fix #6649 (#6651)

c73cbc30 2021-06-15 14:10:17 +0200 Stefano Belforte: adapt to python2 in CMSSW_7 fix #6650 (#6652)

431edfb0 2021-06-11 18:41:58 +0200 Stefano Belforte: make ServerUtilities py3 compatible. Fix #6642 (#6643)
* make ServerUtilities py3 compatible. Fix #6642

* do not check py3 line with py2 pylint
72413a53 2021-06-10 09:34:32 +0200 Stefano Belforte: better messages. Fix #6636 (#6637)

2a5a0cb7 2021-06-08 22:01:41 +0200 Stefano Belforte: add execute_command from WMCore/Credential/Proxy (#6633)

5934e165 2021-05-14 10:33:41 +0200 Stefano Belforte: Make client py3 compat (#6594)
* import HTTPException from http.client

* from dict.iteritmes to dict.items

* import HTTPException from http.client

* from urllib.quote to urllibQuote
f1a73fdb 2021-04-22 10:50:39 +0200 Daina: fix wording (#6560)

82869143 2021-04-20 22:40:03 +0200 Stefano Belforte: update S3 utils descriptions to include runtimefiles (#6555)

2555e84a 2021-04-13 08:34:06 +0200 Stefano Belforte: typo in comments

463664e6 2021-04-12 16:46:00 +0200 Stefano Belforte: Properly deal with sandboxes (#6528)
* pass username to RESTCache when needed

* when accessing sandboxes, need a username
d4864ed0 2021-04-12 14:56:03 +0200 Stefano Belforte: Add download from s3 (#6527)
* add downloadFromS3 to ServerUtilities

* rearrange order of functions and improve comments

7b31ff06 2021-04-10 18:28:37 +0200 Stefano Belforte: RESTCache i/f changes (#6525)
* rename object to objecttype and cachename to tarballname. Fix #6522

* implement authz checking for RESTCache. Fix #6496
e3293af4 2021-04-09 23:43:20 +0200 Stefano Belforte: Download from s3via psu fix6520 (#6524)
* add download to RESTCache. Fix #6520

* add getDonwloadUrlFromS3 to ServerUtilities
320db815 2021-04-09 10:42:07 +0200 Stefano Belforte: Use CRABRest in ServerUtilities (#6518)
* use CRABRest class for S3 utils

* adapt getProxiedWebDir to CRABRest

* rename CRABRest arg and var to crabserver
8522b63c 2021-04-06 22:15:16 +0200 Stefano Belforte: Take s3bucket from rest config fix6494 (#6510)
* add external config to RESTCache and use it to get S3 endpoint and bucket. Fix #6494

* add -f to curl to prevent silent errors
730e8f45 2021-04-01 10:15:41 +0200 Stefano Belforte: improve message text

590951d7 2021-04-01 10:14:18 +0200 Stefano Belforte: Upload sandbox once fix6495 (#6498)
* Return url='' if sandbox exists

* skip uploading existing sandbox. Fix #6495
119254ff 2021-03-30 18:33:35 +0200 Stefano Belforte: Completes the planned CRABCache functionalities (#6488)
* implement list and used

d19050fc 2021-03-26 17:26:07 +0100 Stefano Belforte: Add RESTCache (#6485)
* add initial RESTCache.py

* add uploadToS3 and retrieveFromS3

17d8a0e5 2021-02-02 17:02:12 +0100 Daina: clean ServerUtilieties from cmsweb-k8s-prod host (fix #6376) (#6377)

921af0e3 2021-01-26 10:15:25 +0100 Stefano Belforte: getProxiedWebDir takes server as arg. Fix #6360 (#6361)

88b57650 2021-01-22 14:41:08 +0100 Stefano Belforte: add userAgent to HTTPRequest args and use it. Fix #6355 (#6358)
* add userAgent to HTTPRequest args and use it. Fix #6355

reduce the number of REST Server instantiations in TW

remove some old code (Dynamo e.g.)

use CRABClient as userAgent in getProxiedWebDir

* pylint fixes
9b4f5a5b 2021-01-12 19:14:06 +0100 Stefano Belforte: finalize TapeRecall. Fix #6336 (#6338)

aac31bb4 2020-12-11 13:45:56 +0100 ddaina: point prod instance to cmsweb-k8s-prod (fix #6291)

5257cc42 2020-10-29 06:31:17 -0500 Stefano Belforte: Use rucio for lfn2pfn in TaskWorker (#6221)
* move getPFN inside StageoutCheck since it is used only there
* implementation of StageoutCheck using Rucio for LFN2PFN
* modify DagmanCreator to use Rucio for LFN2PFN resolution
* fixes for pylint
32de647c 2020-10-25 09:29:06 -0500 Stefano Belforte: update K8s clusters in list of SERVICE_INSTANCES fix #6214 (#6215)
* update K8s clusters in list of SERVICE_INSTANCES fix #6214

* fix pylint
3dad9ce7 2020-08-28 11:56:47 +0200 dciangot: Disable direct stageout for Rucio + better exception management (#6140)
* disable direct stageout for rucio at dag creation
* some pylint fix
* fix most relevant pylink complaints in cmscp.py,  CMSRucio.py, MonitorTransfers.py

Co-authored-by: Diego Ciangottini <dciangot@crab-rucio-dev.cern.ch>
Co-authored-by: Stefano Belforte <stefano.belforte@cern.ch>
c208731d 2020-08-28 04:53:53 -0500 Stefano Belforte: fix on major pylint complain

a78ed1ce 2020-08-04 15:55:10 -0500 Stefano Belforte: another typo in definition of stefanovm(2) instance

3de29358 2020-06-17 23:05:08 -0500 Stefano Belforte: fix typo in SERVICE_INSTANCE defintion for stefanovm[2]

93e2513c 2020-05-23 19:00:11 -0500 Stefano Belforte: add predefined SERVICE_INSTANCES for stefanovm[2] (#6062)

5ad34970 2020-05-13 15:17:00 -0500 Stefano Belforte: use new configuration. fix #6050 (#6052)

e65c5e83 2020-02-18 04:27:11 +0100 Stefano Belforte: add args. description for getEpochFromDBTime

4dd075c3 2019-12-15 13:47:19 +0100 Leonardo Cristella: Define constants in ServerUtilities.py (#6002)
* Define constants in ServerUtilities.py
6e7ba9fb 2019-10-19 22:09:45 +0200 dciangot: Rucio demo: fix for integration tests  #5951 #5940 (#5954)  (#5956)
* fixes to Rucio from first integration tests
aaf64ff2 2019-10-15 06:19:42 +0200 dciangot: Rucio demo version #5951 #5940 (#5954)
* Rucio demo version

9e8efac5 2019-07-10 19:39:48 +0200 Leonardo Cristella: Do not perform the HTCondor query in the PreJob (#5914)
* Back to using file for webDir

* Replace deprecated parse methods

* Allow to tune maxIdle jobs
08189b11 2019-03-29 23:24:01 -0500 belforte: use lowercase to match error text in WMCore

5e94890b 2019-03-29 19:44:29 -0500 Stefano Belforte: Update ServerUtilities.py (#5857)

739caccb 2019-03-21 01:09:39 +0100 Leonardo Cristella: Increase sandbox limit to 120 MB (#5841)

a4aa634d 2019-02-22 17:58:05 +0100 Leonardo Cristella: Resolve #5727 (#5824)
* Resolve #5727

* Fail TAPERECALL tasks older than 30 days

* Replace warning with failure message
efec072c 2018-11-08 17:02:34 -0600 Stefano Belforte: use context handler to temporary change logLevel. Fix #5873 (#5788)
use context handler to temporary change logLevel. Fix #5783
dec08c91 2018-10-26 22:35:11 +0200 belforte: make newX509env idempotent. Fix #5764

35ff3bf0 2018-08-17 16:39:26 +0200 Stefano Belforte: use context manager to save/set/restore env for cmsweb. Fix #5715 (#5718)
* quick fix for #5715

* add context managers for save/clean/set/restore X509 env

* cleaner code

* proper indent, typos

* typo: extra -

* use context manager to save/set/restor X509 env

* __exit__ needs 4 args

* allow to use TestWorker also when there are exceptions thrown

* no point in waiting 1h on condor submit.Better sleep and retry

* let's wait 1min for submission

d1bf3879 2018-07-17 01:00:55 +0200 belforte: wrap calls to DBS and PhEDEx in save/clean/restore X509 env

cb3679b0 2017-08-14 10:59:28 +0200 Marco Mascheroni: Fix pylint warnings of some modules (#5559)

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

32d43b0b 2017-07-04 10:40:57 +0200 Marco Mascheroni: Add a step for aso to wmarchive metadata (#5536)
* Add meta_data.crab_id to WMArchive report

* More changes to WMArchive upload code

* Tagcollector is not a global variable

0a7c66bf 2017-06-01 10:16:43 +0200 Marco Mascheroni: Really fix encodeRequest (#5500)

35e93deb 2017-05-19 10:01:02 +0200 Marco Mascheroni: Fix recent change in encodeRequest (#5496)

525ec67a 2017-05-12 23:01:10 +0200 Marco Mascheroni: Bettern support unicode in encodeRequest (#5483)

15898ef5 2017-05-12 23:00:08 +0200 Marco Mascheroni: Change how we print memory in TestFilemetadataMemory (#5484)

fe501639 2017-03-17 13:45:52 +0100 Stefano Belforte: move UFC FILE_SIZE_LIMIT to ServerUtilities.py Fix #5438 (#5439)

402413c8 2017-02-15 11:49:54 +0100 Emilis Rupeika: Remove duplicate getLock definitions. Fix #5377 (#5378)

3154bcef 2016-11-21 11:38:07 +0100 Marco Mascheroni: Make sure to use the transfer cache in postjob even in case of failures

bae8ca74 2016-11-15 11:45:17 +0100 Marco Mascheroni: Merge with the master

5c6b9ef2 2016-09-06 10:30:28 +0200 Marco Mascheroni: Separate final states in ServerUtilities

502f281b 2016-10-25 16:49:04 +0200 Emilis Rupeika: resubmit rewriting using status2 (#5289)
* resubmit rewriting using status2

* remove unused variables from getfiles2/logs2/out2

27c009ca 2016-10-12 11:29:42 +0200 Emilis Rupeika: First implementation of backend report2 (#5286)
First implementation of report2

974ad6c5 2016-09-02 09:43:40 +0200 Marco Mascheroni: Merge branch 'master' of github.com:dmwm/CRABServer into automated_splitting
Conflicts:
	scripts/task_process/cache_status.py
	src/python/TaskWorker/Actions/DagmanCreator.py
	test/templates/CMSSW_VALIDATION/cmssw-validation.sh
	test/templates/client_validation.sh
	test/templates/validation.sh

49a3359f 2016-08-18 17:28:08 +0200 Marco Mascheroni: Truncate warning messages, and make sure only 10 blocks are returned in an error message (#5281)

fe3b3fc9 2016-07-20 09:41:14 +0200 Marco Mascheroni: Solve conflicts

47620f11 2016-06-28 16:11:38 +0200 Marco Mascheroni: First prototype of ASO&Oracle. Credits to @juztas and @dciangot
A more complete history of the commits can be found here https://github.com/dmwm/CRABServer/compare/master...mmascher:asoOracle?expand=1
In this PR I squashed the whole thing in a single commit (unfortunately
I was not able to keep the original authors, sorry Diego and Justas)

14791567 2016-06-14 10:34:56 +0200 Emilis Rupeika: Backward compatibility for debug tarball, comments, refactor

5461c0ed 2016-06-02 11:46:14 +0200 Emilis Rupeika: Separate Ops monitoring files into another tarball

968c382f 2016-05-26 11:01:15 +0200 Marco Mascheroni: Merge from master (3.3.1606.rc4)

e321205a 2016-05-19 12:09:50 +0200 Marco Mascheroni: Take care of review for #4681 (remove taska fter 30 days)

51da410a 2016-05-04 16:32:27 +0200 Marco Mascheroni: Variable renaming and code style changes

a03ad202 2016-05-03 12:13:25 +0200 Marco Mascheroni: Make sure a task is removed after 30 days. See #4681

319372ca 2016-04-22 11:06:02 +0200 Marco Mascheroni: Fix typo
https://github.com/dmwm/CRABServer/pull/5205#issuecomment-213334017
5608ed04 2016-04-21 15:47:08 +0200 Stefano Belforte: improve message when stage out destination fails . fix #5202

cad0c40a 2016-03-21 15:44:25 +0100 Marco Mascheroni: Merge pull request #5175 from mmascher/state-machine
State machine
cb1e5794 2016-02-22 13:24:58 +0100 Justas Balcas: Check disk usage from job.ad

6e7edb9e 2016-03-15 12:53:20 +0100 Marco Mascheroni: Refactor TASKDBSTATUSES in ServerUtilities: distinguish between final and temporary states

aaa10db2 2016-03-10 11:15:33 +0100 Matthias Wolf: Take care of the proper DAG creation for subjobs.

6dc34075 2016-03-08 15:51:28 +0100 Matthias Wolf: Fix number formatting strings.
Old-school formatting should not be used anymore...

47d31fba 2016-03-08 11:34:00 +0100 Marco Mascheroni: Take care of the 8 months merge

63ef2730 2016-02-17 16:20:25 +0100 Marco Mascheroni: Update list of states
Keeping in mind KILL and RESUBMIT have been included in the NEW state
now

a7588554 2016-02-09 09:00:01 +0100 Justas Balcas: Pylint fixes

72dd2f7c 2016-01-26 14:11:13 +0100 Justas Balcas: Use stageout errors from WMCore

9f272f54 2015-11-19 17:50:40 +0100 Marco Mascheroni: FUTURIZE: raise syntax is different

bd986272 2015-11-19 17:43:28 +0100 Marco Mascheroni: FUTURIZE: use absolute imports

00899f97 2015-11-19 17:41:37 +0100 Marco Mascheroni: FUTURIZE: remove extra whitespace

e5832ee6 2015-10-09 15:10:03 +0200 Andres Tanasijczuk: Add primarydataset parameter.

72224547 2015-10-05 23:05:16 +0200 Justas Balčas: Do not submit tasks for Connection refused error
[1]
TRANSFER globus_xio: Unable to connect to cms-0.mps.ohio-state.edu:2811 globus_xio: System error in connect: Connection refused globus_xio: A system call failed: Connection refused

[2]
$ uberftp  cms-0.mps.ohio-state.edu
Failed to read(): Connection refused
74b3ba42 2015-09-20 22:44:37 +0200 Marco Mascheroni: Merge pull request #5000 from mmascher/recycling_sandbox
Use calculateChecksum from WMCore intead of copy/paste the code. See …
0d4dcf23 2015-09-20 22:05:13 +0200 Marco Mascheroni: Add newchecksum parameter for backwar compatibility with old clients

0aa62733 2015-09-14 17:08:49 +0200 Marco Mascheroni: Merge pull request #4951 from juztas/pool_full
All pools are full means there is no space left
62de5f19 2015-09-14 16:59:15 +0200 Marco Mascheroni: Merge pull request #4993 from emaszs/iss4903v2
Helper function for creating dashboard reports (new PR after conflict fix). Fixes #4903
d5fe5710 2015-09-14 16:40:37 +0200 Emilis Rupeika: Helper function for creating dashboard reports. Fixes #4903

df5b4e23 2015-08-27 14:21:19 +0200 Andres Tanasijczuk: Introduce new task statuses: SUBMITFAILED, KILLFAILED and RESUBMITFAILED. Status get jobs status even if task in failed. Fixes #4806, #4849

6c3362e7 2015-08-20 10:55:01 +0200 Marco Mascheroni: Use calculateChecksum from WMCore intead of copy/paste the code. See #4948

bf13a6c2 2015-08-18 14:56:50 +0200 Andres Tanasijczuk: Make getProxiedWebDir compatible with old-style REST configuration.

9163b723 2015-08-17 13:11:47 +0200 Justas Balcas: All pools are full means there is no space left

bc87053f 2015-08-14 10:45:46 +0200 Marco Mascheroni: Move import inside getPFN so we don't need to update runtime archives

ba87e200 2015-08-13 18:17:23 +0200 Marco Mascheroni: Make cmd_exist really work

3c7ae73c 2015-08-13 14:15:06 +0200 Justas Balcas: Stageout check before submitting task.

ac2aad21 2015-08-12 17:43:45 +0200 Justas Balčas: Execute in shell command
if it is executed not with shell=True, we are getting OSError
1e7ed30d 2015-08-05 12:45:18 +0200 Andres Tanasijczuk: Add HOLDING to list of possible task statuses.

d60e8b4f 2015-08-04 13:26:32 +0200 Andres Tanasijczuk: Add list of possible task statuses.

076f28a7 2015-07-31 21:31:50 +0200 Marco Mascheroni: Some improvements after review of proxied webdir pull. #4883

a3f81a80 2015-07-31 16:33:08 +0200 Marco Mascheroni: Add RESTInteracions to runtime archives. #4883
Also rmove some trailing whitespaces

3aa8b746 2015-07-30 16:14:18 +0200 Marco Mascheroni: AdjustSites: fetch proxied webdir from REST. #4883
Main change is the addition of a function that calls getProxiedWebDir
from ServerUtilities and saves locally the webdir configured in the REST external
configuration file. getProxiedWebDir simply query the server to get this
URL.

Added some printouts, improved error messaged, and reorganized imports

afb6c948 2015-07-21 21:27:51 +0200 Marco Mascheroni: Better error message if schedd curl fails. Fixes #4878

7c0047e8 2015-07-17 16:34:45 +0200 Anna Elizabeth Woodard: This includes a merge which isn't fully resolved; need to add back in dealing with the site availability, then fix the issue passing ClassAds to subdags.

70aa6248 2015-06-25 11:13:39 +0200 Justas Balcas: Use gfal2 if possible, else lcg-cp. Fixes #4836

b01f67d0 2015-06-05 14:45:17 +0200 Mohd Nizam Yusli: json fjr file not send to dashboard. #4795

c2171913 2015-04-14 05:12:42 +0200 Marco Mascheroni: Fixes for dashboard logfiles
Fix dashboard logfiles not sent after
https://github.com/dmwm/CRABServer/commit/c498367605b79e6557ca7dea0b060eeb1d1aa5ee#diff-3fa1996a22a9c377b41882d6cf77ab1cL173
Also, uploads them at thebeginning of the jobwrapper.

9fc3273e 2015-02-16 17:06:40 +0100 Andres Tanasijczuk: Don't require USERNAME in /store/group output LFN.

89334cce 2015-01-13 20:20:21 +0100 Mohd Nizam Yusli: Added ServerUtilities with checkOutLFN function

