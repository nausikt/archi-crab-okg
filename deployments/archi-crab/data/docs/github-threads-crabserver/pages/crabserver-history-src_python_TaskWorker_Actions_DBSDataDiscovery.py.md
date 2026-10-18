# dmwm/CRABServer: commit history of src/python/TaskWorker/Actions/DBSDataDiscovery.py (at 30286f7d5b21)

URL: https://github.com/dmwm/CRABServer/commits/master/src/python/TaskWorker/Actions/DBSDataDiscovery.py

a6e5c44a 2025-06-30 10:24:44 +0200 Stefano Belforte: disable publication if non VALID input dataset. fix #9114 (#9115)

2283a7b9 2025-02-18 16:46:09 +0100 Vijay Chakravarty: replace service cert/key with robot cert/key (#8934)

99fe41a9 2024-11-21 15:00:39 +0100 Vijay Chakravarty: Adding all the rule states in getTapRecallUsage and a bug fix (#8741)
* Adding all the rule states in getTapRecallUsage and a bug fix in ReportRecallQuota

* Different handling of Analysis Input and Analysis TapeRecall within getTapeRecallUsage

* fix elif

* fix indentation

* logic fix

* fix getTapeRecallUsage

* change name of getTapeRecallUsage to getRucioUsage
01e1d7de 2024-08-16 16:46:49 +0200 Stefano Belforte: trim DBSDataDiscovery logging and add dataset name (#8629)

9589b463 2024-08-11 18:29:56 +0200 Stefano Belforte: improve message. Fix #7857 (#8608)

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
31592fa1 2024-07-16 18:25:47 +0200 Stefano Belforte: add per-user tape recall policy. Fix #8354 (#8544)
* add per-user tape recall policy. Fix #8354

* bump HTC bindings to 23.9.0a3 (#8547)

* fix message

* Update src/python/TaskWorker/Actions/DBSDataDiscovery.py

Co-authored-by: Thanayut Seethongchuen <thanayut.see@outlook.com>

* Update src/python/RucioUtils.py

thanks !!

Co-authored-by: Thanayut Seethongchuen <thanayut.see@outlook.com>

* activy is TapeRecall, not Tape Recall !

---------

Co-authored-by: Thanayut Seethongchuen <thanayut.see@outlook.com>
4a7ea9a5 2024-05-16 18:31:01 +0200 Stefano Belforte: Use user input files list as a filemask 8371 (#8410)
* use DBSDataDiscovery also when both inputData and inputUserFiles are present

* use userInputFiles param as file-mask Fix #8371
add validation of input files and input blocks list
616470a3 2024-04-26 00:28:31 +0200 David Lange: attempt to streamline parent file discovery (#8352)
* attempt to streamline parent file discovery
d6195e79 2024-04-25 23:52:14 +0200 Stefano Belforte: make test of DBSDataDiscovery work again and add printout of output (#8362)

eafa9ddb 2023-12-15 10:47:18 +0100 Thanayut Seethongchuen: fix possibly unbound in DBSDataDiscovery (#8101)

ea7bcd39 2023-11-09 17:40:51 +0100 Stefano Belforte: fix #7948 also restrict partialDataset to disk data (#8001)
* fix #7948 also restrict partialDataset to disk data

* list(), not list[] !!!
e7c14e31 2023-09-05 11:18:11 +0200 Thanayut Seethongchuen: Taperecall: allow to recall any data tier if size less than threshold (#7862)

9a4884ee 2023-08-21 15:21:19 +0200 Stefano Belforte: stop blacklisting KIPT datalocation. Fix #7846 (#7847)

fda4b6a2 2023-08-07 17:14:50 +0200 Stefano Belforte: Fix 7799 (#7800)
* pass correct config to RucioAction. Fix #7799

* add WorkerUtilities.py

* uploadWarning and deleteWarnings in WorkerUtilities

* correct uploadWarning in RucioAction, fix #7799

* pylint
88c9de0b 2023-07-17 09:55:58 +0200 Stefano Belforte: move DataRecall and DataLock to separate file (#7750)
* move DataRecall and DataLock to separate file

* use a single class in Rucioactions

* fix pylint and pep-8

* move MAX_LUMIS to ServerUtilities with all constants

* complete pylint fixes
dd72fb69 2023-07-12 15:10:46 +0200 Stefano Belforte: do not lock data when using partialDataset (#7744)

72f25833 2023-07-12 14:55:14 +0200 Stefano Belforte: beware rules created by other accounts. Fix #7742 (#7743)

2e36bc17 2023-07-11 09:03:52 +0200 Stefano Belforte: lock input data when submitting. Fix #7592 (#7732)
* lock input data when submitting. Fix #7592

* pylint

* pylint

* lock for TASKLIFETIME days

* use crab_input Rucio accont

* use correct scope
14116832 2023-07-05 11:13:02 +0200 Stefano Belforte: remove use of freeRSE. Fix #7714 (#7715)

e2dfd397 2023-06-12 11:48:25 +0200 Thanayut Seethongchuen: Hotfix taperecall exception in setTaskToTapeRecall (#7659)

9a1f2b0c 2023-05-25 10:38:21 +0200 Stefano Belforte: refactor requestTapeRecall and accept dataset name. Fix #7603 (#7641)
* refactor requestTapeRecall and accept dataset name. For #7603
2837eaca 2023-05-24 17:03:22 +0200 Stefano Belforte: ad hoc message for CERNBOX data. Fix #7640 (#7644)

55014249 2023-05-23 19:10:20 +0200 Stefano Belforte: beware shallow copies (#7639)

29619d6b 2023-05-03 14:09:01 +0200 Stefano Belforte: Refactor tape recall (#7620)
* introduce KILLRECALL status FIx #5608

* add TapeRecallManager fix #7406

f601c4b6 2023-04-28 19:11:58 +0200 Stefano Belforte: correct accounting of tape locations. Fix #7589 (#7619)
* correct accounting of tape locations. Fix #7589

* proper handling of set elements!
25e1fb95 2023-04-27 15:54:52 +0200 Stefano Belforte: always use grouping=all. Fix #7610

bf0a4651 2023-04-15 15:02:11 +0200 Stefano Belforte: improve message

c817fcce 2023-04-14 14:50:39 +0200 Stefano Belforte: do not recall across Atlantic. Fix #7589 (#7597)
* do not recall across Atlantic. Fix #7589

* fix example for test

* fix indentetion

* better comment
bbd2caba 2023-04-13 18:39:08 +0200 Stefano Belforte: tape recall rules expire in 30 days

44bb5a2a 2023-04-02 20:50:01 +0200 Stefano Belforte: when usePartialDataset use also partial blocks. Fix #7573 (#7576)

4b740536 2023-03-28 17:08:49 +0200 Stefano Belforte: remove hack based on runnumber=0 (#7574)
* remove hack based on runnumber=0

* restore runRange
2dde9fca 2023-03-09 17:15:34 +0100 Stefano Belforte: add dataset name, size to taperecall rule comment. Fix #7514 (#7562)

351ef94d 2023-02-17 17:19:10 +0100 Thanayut Seethongchuen: Allow blocks taperecall for any Tier if inputblocks provided (#7539)
* allow blocks taperecall for any Tier if inputblocks provided

---------

Co-authored-by: Thanayut Seethongchuen <=>
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
b941f538 2023-02-03 11:04:30 +0100 Stefano Belforte: Fix test for DBSDataDiscovery (#7522)

9df0542e 2023-01-12 09:38:17 +0100 Stefano Belforte: skip T2 UA as data location. Fix #7499 (#7501)
* skip T2 UA as data location. Fix #7499

* pylint
35ab935d 2022-11-09 16:38:48 +0100 Stefano Belforte: typo in DBSDataDiscovery test

65e3b434 2022-11-09 16:08:24 +0100 Stefano Belforte: skip RSE with empty usage detail list. Fix #7452 (#7453)

e65c4a3e 2022-09-21 22:09:52 +0200 Stefano Belforte: avoid to recall from tape to fragile sites. Fix #7400 (#7401)

1b60aba6 2022-07-05 15:57:16 +0200 Thanayut Seethongchuen: Proper use partialDataset instead of runRange=0 #7135 (#7296)

093d8ffb 2022-04-28 18:42:50 +0200 Stefano Belforte: further improve tape recall placing. Fix #7207 (#7224)
* further improve tape recall placing. Fix #7207

* further improve tape recall placing. Fix #7207
5d445711 2022-04-21 16:19:30 +0200 Stefano Belforte: properly spell rucioClient (#7221)

4a7f81d1 2022-04-21 14:20:56 +0200 Stefano Belforte: improve messages when issueing tape recall (#7220)

5c81cd78 2022-04-20 21:42:05 +0200 Stefano Belforte: Place tape-recalled data at few sites. fix #7207 (#7218)

6ae0db12 2022-04-20 15:36:27 +0200 Stefano Belforte: Hot fix for 7135 (#7217)
* introduce usePartialDataset via a temporary hack for #7135

* fixes to standalone test

* proper cleanup
8529c976 2022-03-30 17:59:00 +0200 Stefano Belforte: add pointer to Rucio WebUI to check taperacall. Fix #7189 (#7190)

5eeda573 2022-03-15 22:16:08 +0100 belforte: use py3 syntax for next(generator). Fix #7131

33bffcac 2022-03-14 18:30:41 +0100 Stefano Belforte: use dictionary copy when needed. Fix #7120 (#7121)

0485ab9c 2022-02-23 17:51:46 +0100 Dario Mapelli: adapt to new DBS serverinfo API (#7093)

16a275f0 2021-10-26 14:28:14 +0200 Stefano Belforte: parent 23707a194a1df38cd8cda928c21b6723001a95ea (#6818)
Initial changes for python3. Make it possible to run with python3 on sched.
2067016a 2021-08-17 15:09:09 +0200 ddaina: add deep flag (fix dmwm#6702)

1230090d 2021-06-30 13:56:56 +0200 Stefano Belforte: Recall dataset partially on tape fix 6666 (#6684)
* skip files w/o parents instead of failing task. Fix #6438

* recall dataset also if partially on tape. Fx #6666

* add a list of tiers to recall to TW config

* remove old code to protect during WMCore changes 6 years ago

* pylint
2883f766 2021-04-15 16:14:14 +0200 Stefano Belforte: Use crab rest in tw fix6530 (#6536)
* use CRABRest in MasterWorker Fix #6530

* complete adaptint to CRABRest class and remove code to switch cmsweb-k8s-prod to cmsweb

* use correct API in postJob

* pylint


88b57650 2021-01-22 14:41:08 +0100 Stefano Belforte: add userAgent to HTTPRequest args and use it. Fix #6355 (#6358)
* add userAgent to HTTPRequest args and use it. Fix #6355

reduce the number of REST Server instantiations in TW

remove some old code (Dynamo e.g.)

use CRABClient as userAgent in getProxiedWebDir

* pylint fixes
bccc8774 2021-01-15 11:52:15 +0100 Stefano Belforte: improve message to user for tape recall (#6344)

9b4f5a5b 2021-01-12 19:14:06 +0100 Stefano Belforte: finalize TapeRecall. Fix #6336 (#6338)

cc9aacd4 2021-01-12 15:58:41 +0100 Stefano Belforte: user dataset has datatier=USER . Fix #6272 (#6337)
* user dataset has datatier=USER . Fix #6272

* pylint fixes
a6b37e51 2021-01-10 21:44:17 +0100 Stefano Belforte: Use crab tape recall account for tape recall (#6333)
* use crab_tape_recall rucio account

* improve comments. Fix #6332
acdc0d83 2021-01-08 18:40:34 +0100 Stefano Belforte: use service account for requesting tape recall. Make it clear that it is temporary (#6330)

8309a206 2021-01-08 17:11:46 +0100 Stefano Belforte: Ddmreqid for rucio is 32 char fix #6325 (#6328)
* validate ddmreqid as a 32char string. Fix #6325

* improve messages to user and fix #6325
a75c7055 2021-01-08 11:15:16 +0100 Stefano Belforte: use native Rucio client and port TapeRecall to Rucio (#6322)
* * use native Rucio Client everywhere, not WMCore one
* use same instance of rucioClient for all actions on a Task
* introduce RucioUtils.py and move there getPFN
* use Rucio for placing tape recall requests (to be tested)

* py3 compatibility

* remove unused imports

* store Rucio ruleId even if SUBMITFAILED

* address last pylint warnings
8308bb56 2020-11-25 11:45:19 -0600 Stefano Belforte: use DBS location of USER secondary dataset. Fix #6267 (#6271)

76920b54 2020-11-05 16:05:20 -0600 Stefano Belforte: signature change for listFileBlockLocation DBS3Reader AP. as per https://github.com/dmwm/WMCore/pull/9927 Fix #6239I (#6241)

efb85398 2020-10-26 05:04:18 -0500 Stefano Belforte: remove all PhEDEx calls from DBSDataDiscovery Fix #6200 (#6212)
* remove all PhEDEx calls Fix #6200

* add one USER dataset to example for standalone test

* fix indentation for pylint

* fixes for pylint

* fixes for pylint
a01540d4 2020-10-16 23:54:44 +0200 belforte: this addresses first part of #6190

9fec6c46 2020-10-05 12:21:03 -0500 Stefano Belforte: Align withv3.200922 (#6180)
* make rucioClient a class member so can reuse in auxilliary methods

* print name of dataset not found with Rucio
43f63774 2020-09-24 17:14:41 -0500 Stefano Belforte: Use rucio client drop tape fix6165 (#6175)
* make rucioClient a class member so can reuse in auxilliary methods

* use rucioClient.dropTapeRSEs. fix #6165
c3424dc8 2020-09-21 19:29:49 -0500 Stefano Belforte: use dbs.listFileBlocks. Fix #6157 (#6164)

b6c5ece9 2020-09-21 18:53:44 -0500 Stefano Belforte: Add keep only disk for rucio (#6163)
* add keepOnlyDiskRSEs Fix #6160

* better messages

* fixes for pylint

* call block name "block" not "element" inside loops
fc7966c1 2020-09-18 10:22:33 -0500 Stefano Belforte: use Rucio for all dataset in CMS scope. Fix #6155 (#6156)

02085f81 2020-08-21 11:03:36 -0500 Stefano Belforte: Fix 6141 (#6142)
* make DBS host redirection via TW config really work. Fix #6141

* move lines around for clarity in test part

* check that DBSHostName is defined in config
5b06a68e 2020-08-15 15:29:43 -0500 Stefano Belforte: Fix 6116 (#6118)
* no fallback to PhEDEx for NANO. Fix #6116

* fixes for pylint

* revert bug in last commit

* fix messages
25902827 2020-06-09 22:07:47 -0500 Stefano Belforte: Cleanup and refactor a bit DBSDataDiscovery. Solve #6073. always use Rucio first for secondarDataset, fix #6075 (#6074)

b0e79f82 2020-05-30 00:14:54 -0500 Stefano Belforte: in DBSDataDiscovery use self.* for REST server and uri. FIx #6066 (#6067)

5ad34970 2020-05-13 15:17:00 -0500 Stefano Belforte: use new configuration. fix #6050 (#6052)

1768685e 2020-05-07 02:07:10 +0200 dciangot: Rucio client initialization only for nanoAod (#6044)

4eec0a36 2020-04-29 14:27:12 +0200 dciangot: RUCIO data location and user dataset name  (#6038)
* include rucio in taskworker DBS discovery

* rucio data location

* first working version

* Correct management of fallback in data location

* manage secondary blocks

* dbs only

* filter on NANOAOD on cms scope + debug enhancement
a4aa634d 2019-02-22 17:58:05 +0100 Leonardo Cristella: Resolve #5727 (#5824)
* Resolve #5727

* Fail TAPERECALL tasks older than 30 days

* Replace warning with failure message
d486503a 2018-12-12 01:59:44 +0100 Leonardo Cristella: Ignore T3_CH_CERN_OpenData (#5806)
* Ignore T3_CH_CERN_OpenData

58ecf87d 2018-11-30 08:45:31 +0100 Leonardo Cristella: Skip blocks without locations for secondary dataset (#5795)
* Resolve #5784

* Resolve #5794
3e1b6c43 2018-11-12 23:35:39 +0100 Leonardo Cristella: Resolve #5784 (#5790)
OK (also tested in my VM)
1f221147 2018-10-30 03:01:29 +0100 Leonardo Cristella: Refine TapeRecallStatus (#5767)
* Add reques_id in TapeRecallStatus log

* Resolve #5760

* Improve TapeRecallStatus log and user message

e8487079 2018-10-28 22:50:08 +0100 Leonardo Cristella: Resolve #5762

d23e345d 2018-10-16 00:54:06 +0200 Leonardo Cristella: Delete removeEmpty function

f1f0ffc3 2018-10-15 21:14:17 +0200 Leonardo Cristella: Resolve #5730

75e36c39 2018-10-15 19:56:56 +0200 Leonardo Cristella: Fix last Pylint warnings in DBSDataDiscovery

1dcdd77b 2018-10-10 00:43:00 +0200 Leonardo Cristella: Fake uploadWarning in standalone DBSDataDiscovery call

5646af56 2018-10-10 00:06:52 +0200 Leonardo Cristella: Fake uploadWarning in standalone DBSDataDiscovery call

bc099acf 2018-10-09 18:47:12 +0200 Leonardo Cristella: Resolve #5746 (#5747)

8569a4dd 2018-10-09 18:36:52 +0200 Leonardo Cristella: Resolve #5746

29f1d5e2 2018-09-26 15:08:37 +0200 Leonardo Cristella: Avoid TapreRecall recurring action spawning subProcesses and automatically create recurring action log file (#5728)
* Automatically create recurring action log file and fix ELOG/Analysis+Operations/2250

* Resolve #5731

* Resolve #5727
38db1ffc 2018-09-18 00:40:54 +0200 Stefano Belforte: Use CRIC in TW (#5738)
* make unit test work with new X509 env. context, requires Excluding type check in WMCore.Config

* use CRIC instead of SiteDB for PNN to PSN

* replace SiteDB with CRIC

* remove typo in previous commit

* getAllCMSNames is now getAllPSNs

* no need to indicate logger for CRIC

* suppress debug messages one-per-file. X509 env is now set OK also on schedd see #5711

* missing import

* instantiate CRIC after changing log leverl

* X509 env is now set OK also on schedd see #5711

* send CRIC messages to our logger, so we can control the log level

* send CRIC messages to our logger, so we can control the log level

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

0db5eb41 2018-08-16 18:39:19 +0200 Leonardo Cristella: Add TAPERECALL as possible output status of data discovery (#5685) solves #5607 #5609 #5606
* Move to crab-dev-tw01.cern.ch

* Resolve #5609

* Remove test printouts

* Resolve trivial Pylint warnings

* Remove test comment

* Use different variable name in the standalone execution

* Resolves #5607

* Resolves first part of 5606

* Move DDM lines to a separate file and catch servers exceptions

* Move TAPERECALL tasks handling in a recurring action

* Fix relevant Pylint warnings

* Move TAPERECALL status setting from workflow to task

* Add main function to recurring action

* Remove warnings from TAPERECALLED tasks

* Fix trivial Pylint warnings

* Remmove warnings after dataset tape recall

1243414e 2018-07-17 15:28:53 +0200 belforte: small cleanup

d1bf3879 2018-07-17 01:00:55 +0200 belforte: wrap calls to DBS and PhEDEx in save/clean/restore X509 env

884e1b7f 2018-05-15 21:47:55 +0200 belforte: make unit test in __main__ work again

d5731cce 2018-05-15 14:58:34 +0200 belforte: refer to FAQ in error message

2a1ffc76 2018-05-15 01:55:03 +0200 belforte: improve error message

3acc00c2 2018-05-13 14:27:58 +0200 belforte: adapt error message

cc073012 2018-05-13 02:37:05 +0200 belforte: remove extra )

0a306198 2018-05-13 02:24:27 +0200 belforte: cleanup

edd42024 2018-05-12 01:06:43 +0200 belforte: secondary -> secondaryDataset

75452429 2018-05-12 00:59:49 +0200 belforte: missing ]

108d17df 2018-05-12 00:51:24 +0200 belforte: firs try

35915b87 2018-03-13 10:27:49 +0100 Leonardo Cristella: Remove unused import urllib

1fff3637 2018-03-13 10:13:03 +0100 Leonardo Cristella: Switch to DDM production server

5fe6d379 2018-03-12 17:01:34 +0100 Leonardo Cristella: Move DMM server URL in TW config

d336230e 2018-03-09 15:42:14 +0100 Leonardo Cristella: Compact log message

a71b1150 2018-03-09 15:36:22 +0100 Leonardo Cristella: Fix last python3 compatibility issue

1fbb4b00 2018-03-09 15:29:06 +0100 Leonardo Cristella: Fix pylint warnings in this PR lines

b2e7de14 2018-03-09 15:21:27 +0100 Leonardo Cristella: Fix python3 compatibility

bc8a8eb7 2018-03-09 15:02:30 +0100 Leonardo Cristella: Switch to HTTPRequests

0df0f557 2018-03-02 19:05:55 +0100 Leonardo Cristella: Almost working in the TW env, throws pycurl.error

50b7d602 2018-02-28 21:26:37 +0100 Leonardo Cristella: Request a disk replica for tape-only blocks

c508cfe5 2017-08-18 19:21:53 +0200 Stefano Belforte: improve comments

f8e11d13 2017-05-22 10:21:39 +0200 Marco Mascheroni: Make sure big blocks are not processed. Fixes #5488 (#5491)

464f53b0 2017-03-21 11:15:40 +0100 Stefano Belforte: use DBSReader from WMCore.Services Fix #5443 (#5444)

55aceed7 2016-02-14 11:11:47 +0100 Marco Mascheroni: Merge pull request #5046 from AndresTanasijczuk/filesForReport
Save input dataset lumis from DBS data discovery to file in schedd.
e19f4880 2016-01-12 18:32:15 +0100 Marco Mascheroni: Make sure to unset X509_USER_* variables

148e2598 2015-11-02 10:36:42 +0100 Andres Tanasijczuk: Fixes for report.

f7338498 2015-12-16 13:56:33 +0100 Marco Mascheroni: pylint

31234041 2015-12-16 13:35:01 +0100 Marco Mascheroni: Adjust DBSDataDiscovery to new WMCore. Also makes https://github.com/dmwm/CRABServer/pull/5039 obsolete

f5aeab71 2015-10-23 12:04:40 +0200 Andres Tanasijczuk: Fix pre-python 2.6 idioms. Some pylint fixes.

1dbdb21c 2015-10-22 19:37:53 +0200 Andres Tanasijczuk: Save input dataset lumis from DBS data discovery to file in schedd. Save also the duplicate lumis to file in schedd.

1b03958e 2015-11-27 20:41:39 +0100 Andres Tanasijczuk: Fix intersection of LumiLists for secondary dataset.

c808ac93 2015-09-23 17:23:40 +0200 Andres Tanasijczuk: Don't abort submission if only some blocks have no locations.

48a0d4a5 2015-09-14 16:23:21 +0200 Marco Mascheroni: Merge pull request #4974 from AndresTanasijczuk/discovery
Discovery
a211118d 2015-08-27 18:12:28 +0200 Marco Mascheroni: Use DBSReader for standalone tests of DBSDataDiscovery

d7d0d344 2015-08-27 00:46:34 +0200 Andres Tanasijczuk: Finish warning messages with a dot.

86e31ae7 2015-08-19 18:00:39 +0200 Marco Mascheroni: Simple message change

8f54ec47 2015-08-19 17:40:21 +0200 Marco Mascheroni: Give proper error message when dataset contains only invalid files

301bf3ff 2015-08-14 15:12:46 +0200 Marco Mascheroni: Merge pull request #4934 from matz-e/use-secondary
Allow the usage of a secondary dataset.
a303f06a 2015-08-14 10:55:55 +0200 Matthias Wolf: Apply comments of code review.
* Make changes compatible with old REST interface.
* Only apply `use_parent` where needed.
* Log before and after matching computation.

d3fb5538 2015-08-14 10:58:09 +0200 Emilis Rupeika: Clearer error message when dataset is not found in DBS. Fixes #4932

f60b99b4 2015-08-10 15:33:18 +0200 Matthias Wolf: Allow the usage of a secondary dataset.
Simple n² algorithm to perform the matching based on file lumi sections.
Took about 30 seconds doing matching on 2012D data (USER + RAW) of a
dataset I found in DBS.

Resolves #4861.

a8a97777 2015-07-10 14:03:57 +0200 Andres Tanasijczuk: Improve and fix the DBSDataDiscovery tests.

bde8a731 2015-07-08 19:27:33 +0200 Andres Tanasijczuk: Change (improve) messages for non-VALID input datasets.

f6990e6c 2015-07-06 15:28:23 +0200 Andres Tanasijczuk: Get list of all dataset files from dbs, not only valid files.

9e54ea3d 2015-06-24 17:37:28 +0200 Andres Tanasijczuk: Don't run over non-VALID datasets unless user has set a corresponding configuration parameter. Fixes #4819

8e463ff1 2015-05-19 22:37:47 +0200 Marco Mascheroni: Merge pull request #4798 from belforte/master
if user think dataset status is wrong, tell him to contact physics group. fixes #4797
45b1cceb 2015-05-06 21:56:37 +0200 Stefano Belforte: if user think dataset status is wrong, tell him to contact physics group. fixes #4797

da41124d 2015-05-06 20:40:49 +0200 Justas Balcas: Fix except to use what python2.6 recommends

2a7316e4 2015-05-06 09:40:54 +0200 Marco Mascheroni: Improve error message where there is no valid file in the dataset

2a11da0e 2015-05-06 09:29:14 +0200 Marco Mascheroni: Remove duplicated code added by git during a merge. Fixes #4794

0a279820 2015-04-11 12:53:37 +0200 Marco Mascheroni: Improve error message as per @belforte suggesion.
See https://github.com/dmwm/CRABServer/issues/4459#issuecomment-91381034

10f54425 2015-04-09 22:28:01 +0200 Marco Mascheroni: Add warning for non-VALID datasets. Fixes #4739

770a3d42 2015-04-09 18:49:22 +0200 Marco Mascheroni: Better warning if a dataset is only on tape. See #4459

1a167d55 2015-04-11 12:53:37 +0200 Marco Mascheroni: Improve error message as per @belforte suggesion.
See https://github.com/dmwm/CRABServer/issues/4459#issuecomment-91381034

7a65c48f 2015-04-09 22:28:01 +0200 Marco Mascheroni: Add warning for non-VALID datasets. Fixes #4739

9d59811d 2015-04-09 18:49:22 +0200 Marco Mascheroni: Better warning if a dataset is only on tape. See #4459

6ce511bd 2015-04-11 12:53:37 +0200 Marco Mascheroni: Improve error message as per @belforte suggesion.
See https://github.com/dmwm/CRABServer/issues/4459#issuecomment-91381034

fc1fc4ef 2015-04-09 22:28:01 +0200 Marco Mascheroni: Add warning for non-VALID datasets. Fixes #4739

e4a3fd33 2015-04-09 18:49:22 +0200 Marco Mascheroni: Better warning if a dataset is only on tape. See #4459

dfc75b6b 2015-03-29 09:40:59 +0200 Andres Tanasijczuk: Fix typo in message.

390634b2 2015-01-16 22:15:25 +0100 Marco Mascheroni: Improve the error when phedex is unresponsive. Fixes #4581

c84f1a2a 2014-11-29 01:40:09 +0100 Marco Mascheroni: Naming conventions of UR* parameters in TW. #4544
Review the naming convention of parameters like resturl, resturi,
instance etc.

Take for example a REST URI (e.g.: '/crabserver/prod/workflowdb'). The
first field in the REST URI (e.g. 'crabserver') will be called the
server API. The second field (e.g. 'prod', 'preprod', 'dev') is the REST
database instance. The third field (e.g. 'workflowdb', 'info',
'filemetadata') is the REST API.

0ccf0299 2014-10-31 10:06:43 +0100 Mohd Nizam Yusli: Error message improve when if dataset is only on tape. Fixed #4459

9beef2ad 2014-10-22 13:31:47 +0200 Marco Mascheroni: Improve error messages in the TaskWorker. Fix #4471

1952eddf 2014-10-26 17:26:57 +0100 Marco Mascheroni: Simple changes in testing code of DBSDataDiscovery

39ab0c4e 2014-09-28 22:07:57 +0200 Marco Mascheroni: Check if a dataset is on tape when we look for locations. Fixes #4428

217ff8af 2014-09-16 15:45:51 +0200 Marco Mascheroni: Get the PNN instead of se names and convert them to PSN

fc2063fd 2014-08-19 18:39:38 +0200 Marco Mascheroni: Adjust printout in DBSDataDiscovery

9c67d25c 2014-07-30 14:58:28 +0200 Andres Tanasijczuk: Remove totalUnits usage from (DBS)DataDiscovery. Should put it in WMCore after lumi-mask is applied.

76d818f1 2014-07-23 17:21:42 +0200 Andres Tanasijczuk: Accept totalUnits for LumiBased and FileBased.

1a683e34 2014-04-29 22:47:30 +0200 Marco Mascheroni: Skip invalid files during discovery

b4dbdec3 2014-04-11 17:36:31 +0200 Marco Mascheroni: Skip blocks if they have no locations. Fixes #4270

00bbb535 2014-04-09 13:43:23 +0200 Marco Mascheroni: Implement fixes for using local DBS

96f28a72 2014-01-25 21:17:37 +0100 Brian: Switch all default URLs to DBS3.

846a511c 2014-01-25 14:26:25 +0100 Brian: Unset X509_USER_* as necessary.

0ad12b22 2014-01-23 17:27:14 +0100 Brian: Set / unset X509_USER_* for DBS3 querying.

12a09aff 2013-10-29 19:45:06 -0500 Andrew Melo: Remove faulty debug line

8786ca0d 2013-10-24 08:54:44 -0500 Brian Bockelman: Migrate CAFTaskWorker into CRABServer.

