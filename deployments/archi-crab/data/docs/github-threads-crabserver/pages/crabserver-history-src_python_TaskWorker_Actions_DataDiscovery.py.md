# dmwm/CRABServer: commit history of src/python/TaskWorker/Actions/DataDiscovery.py (at 30286f7d5b21)

URL: https://github.com/dmwm/CRABServer/commits/master/src/python/TaskWorker/Actions/DataDiscovery.py

6dcdd788 2025-07-22 17:16:18 +0200 Krittin Phornsiricharoenphant: satisfy pylint, add some description/example.

d4761599 2025-07-11 11:16:03 +0200 Krittin Phornsiricharoenphant: squashed commit from longstanding PR#9082, w/o changes on REST.

73db7465 2023-11-09 21:26:35 +0100 Stefano Belforte: Better messages fix 7596 (#8000)
* use trimmed blacklist in msg

* trim skipped block list

* suggest use of crab checkdataset

* pylint

* remove last pylint warnings
16a275f0 2021-10-26 14:28:14 +0200 Stefano Belforte: parent 23707a194a1df38cd8cda928c21b6723001a95ea (#6818)
Initial changes for python3. Make it possible to run with python3 on sched.
1230090d 2021-06-30 13:56:56 +0200 Stefano Belforte: Recall dataset partially on tape fix 6666 (#6684)
* skip files w/o parents instead of failing task. Fix #6438

* recall dataset also if partially on tape. Fx #6666

* add a list of tiers to recall to TW config

* remove old code to protect during WMCore changes 6 years ago

* pylint
4cfe2b74 2020-06-10 15:27:24 -0500 Stefano Belforte: imporove message for blocks not on disk

9b27d117 2020-06-10 14:48:21 -0500 Stefano Belforte: better message. Fix #6077

d038b487 2020-04-03 23:58:10 -0500 Stefano Belforte: Improve stageout check (#6033)
* remove useless printout of task details

* reduce verbosity of call to PhEDEx

* avoid removin twice the tmp file for stageout check

* reduce verbosity of CRIC initialization
abc74de3 2018-11-08 21:40:31 -0600 Stefano Belforte: fix indentation

efec072c 2018-11-08 17:02:34 -0600 Stefano Belforte: use context handler to temporary change logLevel. Fix #5873 (#5788)
use context handler to temporary change logLevel. Fix #5783
33a05b3d 2018-10-28 23:48:04 +0100 Leonardo Cristella: Apply Pylint python3 compatibility patch

61f2c5a0 2018-10-28 23:27:32 +0100 Leonardo Cristella: Fix conflict

e8487079 2018-10-28 22:50:08 +0100 Leonardo Cristella: Resolve #5762

88cc70b2 2018-10-12 14:52:11 -0500 belforte: force CRIC to use pycurl, for #5752

8809a195 2018-10-02 18:21:10 +0200 todor-ivanov: Merge beanch 3.3.1810.rc4.patch (#5744)
* quick fix to 3.3.1810.rc4 config.envForCMSWEB -> config.TaskWorker.envForCMSWEB

* Typo

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

148e2598 2015-11-02 10:36:42 +0100 Andres Tanasijczuk: Fixes for report.

f5aeab71 2015-10-23 12:04:40 +0200 Andres Tanasijczuk: Fix pre-python 2.6 idioms. Some pylint fixes.

1dbdb21c 2015-10-22 19:37:53 +0200 Andres Tanasijczuk: Save input dataset lumis from DBS data discovery to file in schedd. Save also the duplicate lumis to file in schedd.

7a98f733 2015-11-19 17:49:50 +0100 Marco Mascheroni: FUTURIZE: print is a function in python3

e7bf1323 2015-11-19 16:59:44 +0100 Marco Mascheroni: FUTURIZE: Use isinstance and not type for type checking

da41124d 2015-05-06 20:40:49 +0200 Justas Balcas: Fix except to use what python2.6 recommends

1aca0140 2015-03-11 15:25:06 +0100 Marco Mascheroni: DataDiscovery: Backward WMCore compatibility

454b1c9b 2014-11-29 00:36:49 +0100 Matthias Wolf: Raise an exception when a file has no parents, but parent usage is requested.

7a747967 2014-11-28 17:06:45 +0100 Matthias Wolf: Add full support for `use_parent`.
If specified, the input files passed to the job are not a flat list of
input files anymore, but a list of hashes that the parameter set tweaking
of WMCore expects.  The latter then takes care of setting up CMSSW properly
for us.

Fixes #4514.

217ff8af 2014-09-16 15:45:51 +0200 Marco Mascheroni: Get the PNN instead of se names and convert them to PSN

9c67d25c 2014-07-30 14:58:28 +0200 Andres Tanasijczuk: Remove totalUnits usage from (DBS)DataDiscovery. Should put it in WMCore after lumi-mask is applied.

76d818f1 2014-07-23 17:21:42 +0200 Andres Tanasijczuk: Accept totalUnits for LumiBased and FileBased.

2bff8932 2014-06-12 18:03:32 +0200 Brian Bockelman: Improve debugging during data discovery.

4c3a0edf 2014-05-03 04:21:13 +0200 Brian Bockelman: Allow data discovery to work with older WMCore.

1a683e34 2014-04-29 22:47:30 +0200 Marco Mascheroni: Skip invalid files during discovery

b4dbdec3 2014-04-11 17:36:31 +0200 Marco Mascheroni: Skip blocks if they have no locations. Fixes #4270

00bbb535 2014-04-09 13:43:23 +0200 Marco Mascheroni: Implement fixes for using local DBS

6fe6380f 2013-11-26 16:32:11 +0100 Marco Mascheroni: Readd fix for using configuration cms certificates for sitedb

8786ca0d 2013-10-24 08:54:44 -0500 Brian Bockelman: Migrate CAFTaskWorker into CRABServer.

