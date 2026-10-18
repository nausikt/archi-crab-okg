# dmwm/CRABClient: commit history of src/python/CRABClient/Commands/resubmit.py (at 970fabd75d68)

URL: https://github.com/dmwm/CRABClient/commits/master/src/python/CRABClient/Commands/resubmit.py

cfa2dee 2025-06-23 15:40:15 +0200 Stefano Belforte: deprecate resubmission of successful jobs. Fix #5285 (#5396)

bf347bd 2025-02-17 15:09:26 +0100 Vijay Chakravarty: deprecate numcores option (#5373)
* deprecate numcores option

* numcores only to be removed from resubmit, not completely
e5bc03c 2024-12-04 21:01:40 +0100 Stefano Belforte: Pass projdir to interall called commands 5337 (#5360)
* add projdir arg to getMutedStatusInfo. Fix #5337

* rename SubcommandExecution to SilenceLogging
c971c1d 2024-02-08 17:11:55 +0100 Stefano Belforte: improve help for resubmit.py

1c2f2de 2023-12-15 15:38:22 +0100 Stefano Belforte: Fix help for crab resubmit. fix #5273 (#5275)

da6d38f 2023-10-17 19:46:54 +0200 Stefano Belforte: make sure all commands return a dict. Fix #5224 (#5225)
* make sure all commands return a dict. Fix #5224

* fix two undefined vars

* use new CommandFailedException in crab.py

* add description of return dictionary

* checkusername must also return username, as before
3a27d49 2023-10-09 23:50:34 +0200 Stefano Belforte: Reduce curl verbosity (#5218)
* only print curl details on last failing iteration. Fix #5201

* Encoded request is already printed in CrabRestInterface
ef8a8d3 2021-06-15 16:34:02 +0200 Stefano Belforte: silence py2 pylint complain about urllib.parse fix #5035 (#5036)
* silence py2 pylint complain about urllib.parse fix #5035

* pylint
4f85696 2021-06-11 18:11:26 +0200 Stefano Belforte: a couple py3 compatibility fixes (#5024)
* a couple py3 compatibility fixes

* make LumiMask py3 compat

* make CMSSWConfig py3 compat

* make Analysis.py py3 compat

* sha* wants bytes, not string in py3

* make urrlib.quote/encode py3 compat

* open temp file for writing strings, not bytes

* open with "wb" to pickle a dictionary

* skip code dealing with config. parameter type validation
fdf6477 2021-04-09 09:52:26 +0200 Stefano Belforte: Use s3 for cache. partial solution for #4971 (#4983)
* allow to use S3 to upload sandboxes. for #4971
log upload still to be dealt with

heavy changes everywhere will need extensive validation

* remove wait option from resubmit

* stop using getUrl and remove it

5951982 2021-01-27 08:16:15 +0100 Stefano Belforte: Use new rest interaction (#4969)
* explicitely set userAgent to CRABClient

* adapt all commands to use a common RESTServer instance

* pylint fixes

0243ea0 2020-05-01 13:17:12 -0500 Stefano Belforte: make it easier to copy/paste suggested command

eec5357 2020-01-27 16:13:36 -0600 Stefano Belforte: deprecate --wait option. for #4730 (#4877)

c25551a 2019-09-09 17:35:20 -0500 Stefano Belforte: Resolve 4820 (#4821)
* add Kubernetes test server
* always use getUrl from ClientUtilities. Fix #4820
7bc742b 2019-01-11 00:58:05 +0100 Leonardo Cristella: Resolve #4774 (#4788)
* Resolve #4774

a837ef9 2018-02-09 12:53:20 +0100 Matthias Wolf: Make kill final for automatic splitting.

19cae61 2018-01-24 10:08:42 +0100 Matthias Wolf: Round out automatic splitting changes.
* Condense status display for the DAG
* Only list probe and split other job status for long display
  * Introduce "no output" as status for probes
  * Failed processing jobs turn "rescheduled"
* Better error message when resubmitting job ids that are "rescheduled"
* Add fractional dataset processing

a32e69e 2018-01-11 18:25:28 +0100 Marco Mascheroni: Standalone execution of jobs

7bfde7b 2017-08-14 11:10:02 +0200 Matthias Wolf: Fixes for automatic splitting (#4720)
* Exclude probe jobs from the publication status.

* Fix report.

* Be smarter about splitting jobId lists.

3a875f3 2017-06-14 10:15:57 +0200 Matthias Wolf: Make resubmission and status work with new automatic splitting conventions. (#4712)

b0250ea 2017-05-26 11:45:18 +0200 Emilis Rupeika: Further API fixes (#4708)

f4f2e24 2017-05-15 17:30:02 +0200 Emilis Rupeika: Resubmit command hotfix (#4705)

6f93a22 2017-05-08 12:12:53 +0200 Emilis Rupeika: Make new status calls return only one value (#4699)

9978ac2 2017-04-27 15:48:32 +0200 Emilis Rupeika: Make status2 return dict (mostly) backwards compatible (#4692)

ac180b1 2017-04-24 17:00:09 +0200 Emilis Rupeika: Rename commands (#4689)

6006b61 2016-05-25 17:43:16 +0200 Stefano Belforte: Clarify --priority option. Fix #4407

c6e2765 2016-01-19 13:48:27 +0100 Marco Mascheroni: FUTURIZE: fix few idiomatic things

5745323 2015-11-10 16:00:14 +0100 Andres Tanasijczuk: Pylint fixes

573ba4b 2015-11-10 15:57:52 +0100 Andres Tanasijczuk: Add --publication option to resubmit command.

2a067d0 2015-05-20 16:17:28 +0200 Marco Mascheroni: Merge pull request #4486 from AndresTanasijczuk/oldresubmitopts
Remove old options error messages in resubmit command.
e3373b6 2015-05-20 08:25:43 +0200 Andres Tanasijczuk: Remove old options error messages in resubmit command.

120594f 2015-04-27 17:48:23 +0200 Andres Tanasijczuk: Add --force option in resubmit command.

62b777c 2015-04-21 16:57:09 +0200 Mohd Nizam Yusli:  Add --wait option in crab resubmit. Fixes #4453

d8eac80 2015-04-13 17:40:23 +0200 Andres Tanasijczuk: Add message in crab resubmit.

a453522 2014-12-17 10:33:09 +0100 Andres Tanasijczuk: Change internal options in resubmit from strings to integers to align with taskdb. Don't harcode list-parameters in resubmit command. Interpret empty string in site white and black list options as an empty list.

1b61f9e 2015-03-24 19:01:48 +0100 Andres Tanasijczuk: Allow wildcards in site names in resubmit blacklist/whitelist options; in that case no regex check is done in the client.

410a1d1 2015-03-16 23:07:16 +0100 Anna Elizabeth Woodard: Client side of fix for dmwm/CRABServer#4462. Add a 'dryrun' option for crab submit, which:
1) Tells the server not to submit the job, but instead upload a dry run sandbox to the UserFileCache
2) Downloads the sandbox and runs a 10-event local test to measure time/event and memory used
3) Uses local test results to give rough job processing time and memory requirement estimates

Also: add a 'proceed' subcommand, which can be used to continue a job which was initialized with dryrun.
Also: in checkStatusLoop in submit.py, wait between server queries, even if the current result is the same as the previous one.

61cf43a 2015-01-14 17:01:00 +0100 Andres Tanasijczuk: Move client_utilities to ClientUtilities and client_exceptions to ClientExceptions. Create UserUtilities module with user exposed methods (move user exposed methods from ClientUtilities to UserUtilities). Still keep a client_utilities module with the user exposed methods from UserUtilities imported, and printing a module retirement message. Fixes #4358.

5683fb8 2014-11-11 14:32:56 +0100 Andres Tanasijczuk: Pass job options (maxmemory, maxjobruntime, numcores, priority) to server in resubmit command.

45cb3f3 2014-11-17 16:04:11 +0100 Andres Tanasijczuk: Change option -t/--task to -d/--dir.

0de6d11 2014-09-17 03:13:38 -0500 Andrew Melo: Further replace all REST calls with emulators

3266055 2014-07-14 16:31:05 +0200 qunox: Client library API, client changes. See #4091
alpha release of crabclient library api

Rebase of the client library

minor correction

Client Library: redo logging and create cmdexec

Add class Task for client API

Some pull requests you might look for history:
https://github.com/dmwm/CRABClient/pull/4213
https://github.com/dmwm/CRABClient/pull/4234

8d58479 2014-07-18 11:53:55 +0200 qunox: removing all short options and improve crab report

6421b46 2014-07-07 08:05:12 +0200 qunox: fix and improve cosmetic error

a9882cc 2014-01-05 21:11:30 -0600 Brian Bockelman: Fix optparse for resubmit.

8cb3f1b 2013-12-21 08:34:46 -0600 Brian Bockelman: Allow users to specify task runtime parameters at submit and resubmit time.

36f6255 2013-09-19 19:08:48 +0200 spiga: fix typo

bc22a08 2013-09-12 18:53:04 +0200 spiga: fix typo

2d0ee9d 2013-09-11 17:06:21 +0200 spiga: remove ServerInteraction switching to RESTInteraction

b2e9d36 2013-07-17 11:49:59 +0200 Marco Mascheroni: Implement kill and resubmit of defined jobids. CAF-120

5bc6fcb 2013-06-19 15:08:08 +0200 Marco Mascheroni: Fix a couple of printouts

46824a5 2013-05-31 11:04:23 +0200 cinquo: Cleaning import, most of them, removing deprecated dependencies CAF-162

8a1f7f7 2012-08-16 13:22:03 +0200 Marco Mascheroni: Reorganized status command.

847a1ff 2012-06-18 14:52:39 +0000 spiga: Added kill and resubmit commands. Fixes #3851
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@16016 4525493e-7705-40b1-a816-d608a930855b

e66567c 2012-04-27 14:16:29 +0000 spiga: From cab198a8cfd21933b15d68d231652a67183142eb Mon Sep 17 00:00:00 2001 Subject: [PATCH] Added requiresTaskOption to the mapping, deleted /data from the uri path with status -f, refactor. Fixes #3661
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15820 4525493e-7705-40b1-a816-d608a930855b

00f9544 2011-11-29 19:09:40 +0000 spiga: Better handling of user messaged. Fixes #2880, #2893, #2641
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14669 4525493e-7705-40b1-a816-d608a930855b

3d902fe 2011-11-03 09:14:02 +0000 spiga: From 1ef3a0756e7d2ce9bd0f517be6318d1adb245ea1 Mon Sep 17 00:00:00 2001 Subject: [PATCH 1/3] From mcinquil <mattia.cinquilli@cern.ch>; fixes #2694  #1780 #2145
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14431 4525493e-7705-40b1-a816-d608a930855b

