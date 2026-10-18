# dmwm/CRABClient: commit history of bin/crab (at 970fabd75d68)

URL: https://github.com/dmwm/CRABClient/commits/master/bin/crab

f754471 2024-02-16 12:16:50 +0100 Stefano Belforte: avoid python stuff in .local Fix #5290 (#5293)

64a0834 2024-01-10 10:37:35 +0100 Stefano Belforte: Use python2 for submit whenever cmsrun uses it fix #5279 (#5281)
* use py2 for crab submit on older CMSSW. Fix #5279. Fix #5239

* CMSSW uses py3 internally from CMSSW_12 onward
47e1531 2023-12-01 10:50:35 +0100 Stefano Belforte: proper way to use py3 from CMSSW_10_2 onward. Fix #5264 (#5266)

58a6504 2023-12-01 00:43:33 +0100 Stefano Belforte: typo in last commit

962726a 2023-11-30 23:21:57 +0100 Stefano Belforte: only use python3 for CMSSW_10_2 or later. Fix #5264 (#5265)

0edda22 2023-11-09 22:14:41 +0100 Stefano Belforte: remove obsolete comments

33cc58d 2023-10-20 16:35:28 +0200 Stefano Belforte: Use python3 and rucio client with cmssw 10 (#5238)
* use Python3 for CMSSW_10, add our LumiList, fix LumiList import, remove
pycurl from crab.py

* fix PSetCores check in CMSSWConfig.py

* remove unused, obsolete code from report.py

* add comments
a18cbd0 2023-10-13 14:00:29 +0200 Stefano Belforte: remove diagnostic trace in crab bash

ba525ea 2023-10-12 18:02:39 +0200 Stefano Belforte: Initialise Rucio client after we have proxy. Fix #5220 (#5222)

25c504f 2023-10-12 15:03:31 +0200 Stefano Belforte: remove debug statements from bin/crab

d3db807 2023-10-10 22:46:44 +0200 Stefano Belforte: diagnostics

24e54f7 2023-10-10 22:35:42 +0200 Stefano Belforte: add temp diagnostics

a6462a1 2023-10-10 22:26:25 +0200 Stefano Belforte: temporarely add diagnostics

c5ebc37 2023-10-10 00:58:14 +0200 Stefano Belforte: intial implementation of adding Rucio client. Fix #5213 (#5214)
* intial implementation of adding Rucio client. Fix #5213

* pylint
37171a3 2021-11-09 12:10:38 +0100 Daina: change how script dir is obtained (fix #5106) (#5109)

50df5fb 2021-11-03 14:56:12 +0100 Daina: remove reference to UserFileCache (#5103)

64d1326 2021-11-02 16:17:05 +0100 Daina: switch python versions based on CMSSW release (fix #5098) (#5102)

d1593c1 2021-10-26 12:10:36 +0200 Stefano Belforte: testing done. Move again to use python3

4673358 2021-10-26 11:53:19 +0200 Stefano Belforte: quick (and dirty?) fix for #5052 (#5095)

417e4c5 2021-10-19 11:12:48 +0200 Daina: revert to python for temp testing

9d64147 2021-08-31 14:11:51 +0200 Stefano Belforte: make crab commands use python3 (#5073)

5b9f650 2021-08-31 09:44:27 +0200 ddaina: take last HTTP response code (fix #5072)

a2fa639 2021-08-24 11:24:08 +0200 ddaina: remove HTTPException

bc5964d 2021-08-24 11:22:20 +0200 ddaina: rename exception

80688c5 2021-08-24 10:22:12 +0200 ddaina: fix curl error reporting (#5067)

961f5f5 2021-06-15 14:48:15 +0200 Stefano Belforte: import HTTPException in a way compatible with CMSSW7. Fix #5033 (#5034)
* import HTTPException in a way compatible with CMSSW7. Fix #5033

* pylint
b7da183 2021-06-09 22:39:36 +0200 Stefano Belforte: Py3 compat (#5018)
* make import of HTTPExceptions python3 compatible (#4924)

* fix import of HTTPException for python3 compatibility.  fixes #4923

* use pickle instead of cPickle

* iteritems -> items

* make import urlparse py3 compat

* change all occurrences of iteritems to items

* make import urlparse py3 compat

* import HTTPException from  http.client

* subprocess.check_output returns bytes, cast to string

* skip configuration validation

* add import sys

* introduce a local ProxyInteraction.py to deal with voms and myproxy. Fix #4973

* avoid un-necessary myproxy re-creations

* catch correct exceptions from ProxyInteractions

* fix indentations

* py3 compat syntax

* made checkwrite py3 compatible via execute_command
008b57c 2021-04-22 16:22:55 +0200 ddaina: fix pyling warnings

be87d37 2021-04-22 14:08:32 +0200 ddaina: remove automatic log upload (fix #4993)

e8c8837 2020-08-11 17:24:34 -0500 Stefano Belforte: revert HTTPException import. FIx #4936 (#4937)

cde999e 2020-06-25 15:27:52 -0500 Stefano Belforte: make import of HTTPExceptions python3 compatible (#4924)
* fix import of HTTPException for python3 compatibility.  fixes #4923
8614ae9 2020-05-09 00:48:51 -0500 Stefano Belforte: Fix 4907 (#4913)
* fix #4907
1f3c8dd 2020-03-11 23:12:29 -0500 Stefano Belforte: check pycurl version for SSL support. Fix #4892 (#4893)

92418a4 2020-02-19 23:31:02 -0600 Stefano Belforte: Improve exception handling fix 4884 (#4885)
* indicate which exception type is caught

* add logger to server_info. Fix #4884



4258b9d 2019-06-21 16:52:56 +0200 Leonardo Cristella: Add timezone in log (#4813)
* Resolve #4812

* Use always UTC time
6a03ba3 2019-03-13 14:47:56 +0100 Leonardo Cristella: Improve user message (#4802)
* Sort twiki table by most recent intervention
0f1bc75 2017-03-31 15:57:59 +0200 Emilis Rupeika: Minor bugfix when printing CRAB help message (#4687)

a91d0b9 2016-01-19 13:59:35 +0100 Marco Mascheroni: FUTURIZE: print need parenthesis in python3.0

72d8576 2016-01-19 13:45:18 +0100 Marco Mascheroni: FUTURIZE: remove has_key

f883863 2015-11-18 17:11:53 +0100 Marco Mascheroni: Merge pull request #4569 from AndresTanasijczuk/inputDSInPrivateMC
Remove check of no input dataset in PrivateMC.
dd8f86f 2015-10-20 19:31:58 +0200 Marco Mascheroni: Small error messa improvement

a154a8b 2015-10-14 21:13:56 +0200 Andres Tanasijczuk: Remove check of no input dataset in PrivateMC.

39973b1 2015-10-13 12:06:42 +0200 Andres Tanasijczuk: Change hasattr -> getattr for attributes that are now initialized to None.

e01cfe5 2015-10-08 12:37:38 +0200 Marco Mascheroni: pylint improvements

a075204 2015-10-05 21:10:36 +0200 Marco Mascheroni: Change error message when the server gives an error

867a461 2015-10-04 22:59:35 +0200 Marco Mascheroni: get(log|out) did not print error messages in the logfile (and on the screen)

3ebabb2 2015-10-04 11:17:49 +0200 Marco Mascheroni: Print error X-Error-Id when an unexpected exception occurs

778b152 2015-08-06 21:45:10 +0200 Andres Tanasijczuk: Fix double printing to crab.log file. Add filter to remove colors in filehandler. Fixes #4540

748fda1 2015-08-12 22:37:06 +0200 Marco Mascheroni: Merge pull request #4538 from nizamyusli/feedback
Take feedback mail from ServerUtils. Fixes #4521.
b3d6f05 2015-08-08 01:14:04 +0200 Andres Tanasijczuk: Improve error message for input sandbox size limit exceeded. Fixes #4527

38a0e20 2015-08-06 13:40:35 +0200 Mohd Nizam Yusli: Take feedback mail from ServerUtils. Fixes #4521.

797a5ef 2015-06-22 20:36:29 +0200 Andres Tanasijczuk: Flush memomy handler to crab.log file and remove handlers after executing commands via crabCommand.

caec397 2015-06-22 16:25:00 +0200 Andres Tanasijczuk: Add setConsoleLogLevel function to control console handler log level. Fixes #4418

096367d 2015-02-19 12:26:10 +0100 Marco Mascheroni: Separate COMP and CMSSW envs. Fixes #4300
Provides two new scripts:
  crab.sh: wrapper script that does scram unset env before running crab
commands. Also, if the command is a submit run the bootstrap script
  crab3bootstrap: executes all the operations that needs the CMSSW
environment saving the output to a tmp dir. Returns the tmp directory or
the error message in case of errors.

Backward compatibility is guaranteed since the bootstrapDone() function
is called to check if the clients needs to perform the CMSSW related
operations or the bootstrap script was run.

also refactored many parts of the client. We are providin now:
  flushMemoryLogger function that group the code used to save the output messages that
are stored in memory
  validateSubmitOptions to group the code that in the crab submit
command validate the command line options passed by the user
  setSubmitParserOptions to set the command line options of the client
submit command

5365c6d 2015-04-15 20:31:22 +0200 Andres Tanasijczuk: Remove SocketError exception.

ee563d0 2015-03-27 15:43:10 +0100 Marco Mascheroni: Refactor command line option parsing code

55c2f8f 2015-03-18 10:28:35 +0100 Andres Tanasijczuk: Keep track of where were the voGroup and voRole set (config, command line opts, request cache) to give more clear messages to users.

18a620d 2015-02-06 16:20:45 +0100 Andres Tanasijczuk: Include all config params in client mapping. Add reverted mapping and use it where possible. Fixes #4393

61cf43a 2015-01-14 17:01:00 +0100 Andres Tanasijczuk: Move client_utilities to ClientUtilities and client_exceptions to ClientExceptions. Create UserUtilities module with user exposed methods (move user exposed methods from ClientUtilities to UserUtilities). Still keep a client_utilities module with the user exposed methods from UserUtilities imported, and printing a module retirement message. Fixes #4358.

0a0b1c4 2014-12-11 12:07:02 +0100 Andres Tanasijczuk: Get username from SiteDB when uploading log file.

a105c11 2014-12-05 12:09:29 +0100 Andres Tanasijczuk: Add username to uploaded log file url. Convert retrieved username from SiteDB = 'null' to None (and give appropriate error msg in checkusername).

0442e76 2014-12-01 17:10:04 +0100 Andres Tanasijczuk: Fix check for -t/--task option. Remove -q and -d crab short options (allow only the long --quiet and --debug options).

c4ed5f0 2014-09-10 14:52:00 +0200 qunox: fetch the user enviroment when uploadlog

3266055 2014-07-14 16:31:05 +0200 qunox: Client library API, client changes. See #4091
alpha release of crabclient library api

Rebase of the client library

minor correction

Client Library: redo logging and create cmdexec

Add class Task for client API

Some pull requests you might look for history:
https://github.com/dmwm/CRABClient/pull/4213
https://github.com/dmwm/CRABClient/pull/4234

60107c3 2014-09-09 10:38:30 +0200 Marco Mascheroni: Remove exc handlers for NameError and Keyerror in bin/crab

da9457b 2014-08-26 17:55:57 +0200 qunox: fix #4136 upload automatically the log file for unhandled exception

814933a 2014-09-02 16:13:48 +0200 Marco Mascheroni: Merge pull request #4260 from qunox/capturekeyboard
fix #4236 capture keyboard interupt
97c38d8 2014-09-02 16:12:13 +0200 Marco Mascheroni: Server client param translation: parameter mapping is a list now

02c75c7 2014-09-01 10:25:25 +0200 qunox: fix #4236 capture keyboard interupt

7ec3e0f 2014-08-27 09:31:42 +0200 qunox: logging quick fix

63f6f9f 2014-08-23 16:56:00 +0200 Andres Tanasijczuk: Use Analysis as default job type. Put all possible config parameters in the client mapping. Better organize client mappings. Print unique task name on submit output.

ea40ab4 2014-08-20 18:17:21 +0200 qunox: improve logging

218622e 2014-08-19 11:28:45 +0200 Marco Mascheroni: Remove the comment to the exceptionhook

31d617f 2014-08-07 14:12:00 +0200 qunox: fixup #4179, improve logging system

c7351c8 2014-08-04 08:06:44 +0200 Marco Mascheroni: Add again PSet.pkl file

cec8de9 2014-07-03 14:08:27 +0200 Andres Tanasijczuk: Change twiki link from RunningCRAB3 to CRAB3Tutorial.

a749cb8 2014-07-01 12:29:30 +0200 Marco Mascheroni: Check the config name is there before converting from server's to client's naming

297c2d7 2014-06-24 15:24:54 +0200 Marco Mascheroni: Update hn for user's issues

5f6e631 2014-06-23 16:21:47 +0200 Marco Mascheroni: More error handling in case of CMSWEB interventions

2f39e65 2014-06-13 13:06:17 +0200 Andres Tanasijczuk: In case of a config parameter error, report the client parameter name instead of the server parameter name.

49011e7 2014-06-05 11:12:51 +0200 Marco Mascheroni: Print a link to the scheduled interventions. Fixes #4065

31bacc3 2014-04-29 16:38:20 +0200 qunox: implement client check write on a site #4048B

56bddcd 2014-03-24 02:11:12 +0100 Brian Bockelman: Change error information to refer to the crab feedback list.

5bc6fcb 2013-06-19 15:08:08 +0200 Marco Mascheroni: Fix a couple of printouts

2de072b 2012-11-01 12:33:48 +0100 cinquo: Make error handling more clear and in case of a bug ask to open an issue on github, not a bug on trac

02545b9 2012-06-06 16:43:51 +0000 spiga: From 97299784bd6fb6f10667d23c1ad536abf885a3fe Mon Sep 17 00:00:00 2001 Subject: [PATCH 1/2] Check and renew myproxy certificates at each client command. #Fixes #3810
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15983 4525493e-7705-40b1-a816-d608a930855b

6d86fa9 2012-06-05 16:28:14 +0000 spiga: From 9d5a981b343781e731d507614db5e266201e5020 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Passed the file logger to the Proxy library. Fixes #3658
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15974 4525493e-7705-40b1-a816-d608a930855b

42b5b74 2012-04-02 15:30:06 +0000 spiga: From 26ace87a6482451d4598974528a930419a63828e Mon Sep 17 00:00:00 2001 Subject: [PATCH 1/2] ISB url, encoding parameter during submit, output message if HTTPException. Fixes #3473
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15579 4525493e-7705-40b1-a816-d608a930855b

de4a7b1 2012-04-02 15:27:53 +0000 spiga: From f65368c51138f425e5cd18eef7001ee97479c543 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Polished error messages in case of HTTPException, computation of total number of jobs is done in the status and not server-side anymore, renabled default server url, UFC use server url if not specified in the config. Fixes #3425
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15576 4525493e-7705-40b1-a816-d608a930855b

01fba9f 2012-03-21 09:43:11 +0000 spiga: Client adapted to match the new rest. Fixes #3374
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15471 4525493e-7705-40b1-a816-d608a930855b

ecc8e6b 2011-12-05 16:48:20 +0000 spiga: From 74d5589c2db1b878d9fd4b51dd90abc9d6360583 Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch> - Move version in  CRABClient - fixes #2951
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14726 4525493e-7705-40b1-a816-d608a930855b

9688c49 2011-12-01 14:08:57 +0000 spiga: Added a missing piece of the patch. Fixes #2880
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14700 4525493e-7705-40b1-a816-d608a930855b

274b182 2011-11-22 17:09:22 +0000 spiga: update 306, fixes #2881
From: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14614 4525493e-7705-40b1-a816-d608a930855b

e228de9 2011-11-11 23:38:54 +0000 spiga: From a909de48bdbbdd4d236d9fa655d8c4907b798ce1 Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch>; fixes #2776
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14534 4525493e-7705-40b1-a816-d608a930855b

c5585c3 2011-10-27 12:56:05 +0000 spiga: Fixes #2681 patch-series-spiga/
From: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14359 4525493e-7705-40b1-a816-d608a930855b

02eb5a0 2011-10-12 08:52:09 +0000 spiga: update tag number
From: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14231 4525493e-7705-40b1-a816-d608a930855b

a6fbf5c 2011-09-30 12:19:35 +0000 spiga: Added the kill command and patched ServerInteractions. Fixes #2468
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14059 4525493e-7705-40b1-a816-d608a930855b

3c4bba4 2011-09-13 12:00:51 +0000 spiga: From c317a6e95fcc08a253ef6278df493abfe1e01ac6 Mon Sep 17 00:00:00 2001 Subject: [PATCH] From: mcinquil <mattia.cinquilli@cern.ch> - fixes #2318
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13829 4525493e-7705-40b1-a816-d608a930855b

b0fc9f1 2011-08-31 13:49:51 +0000 spiga: From 31fe9763799ecaa5c696f26f14b0c340bee6fcfa Mon Sep 17 00:00:00 2001 Subject: [PATCH] From: mcinquil <mattia.cinquilli@cern.ch> Better error  handling when 404, fixes #2240
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13720 4525493e-7705-40b1-a816-d608a930855b

c14b17f 2011-08-31 13:42:36 +0000 spiga: From a1c96afcc7cd2aefe65ea36d7fa19702e85a3bbc Mon Sep 17 00:00:00 2001 Subject: [PATCH] From: mcinquil <mattia.cinquilli@cern.ch> Adding consistent  help information for client commands. fixes #2231
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13719 4525493e-7705-40b1-a816-d608a930855b

7960b1e 2011-08-30 10:40:24 +0000 spiga: Added a more friendly error message when a task is not found. Fixes #2175
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13697 4525493e-7705-40b1-a816-d608a930855b

89bc1a9 2011-08-10 10:52:13 +0000 spiga: From f74eec7959d6aeb17e4178e49a25b78e4eeb52cc Mon Sep 17 00:00:00 2001 Subject: [PATCH] From: mcinquil <mattia.cinquilli@cern.ch> Changing command  name format. Now enabled long/short formats. Fixes #2015
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13471 4525493e-7705-40b1-a816-d608a930855b

1bb0da6 2011-07-15 14:42:49 +0000 spiga: fixes #208
patch-series-mcinquil/

From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@13322 4525493e-7705-40b1-a816-d608a930855b

99d455d 2011-05-19 12:33:16 +0000 spiga:  fixes #1619
patch-seres-mcinquil/

From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12747 4525493e-7705-40b1-a816-d608a930855b

2e6b6ab 2011-05-16 14:53:46 +0000 spiga: patch-series-mcinquil/
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12670 4525493e-7705-40b1-a816-d608a930855b

c19ab9c 2011-05-07 16:32:28 +0000 spiga: patch-series-mcinquil/
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12566 4525493e-7705-40b1-a816-d608a930855b

b902118 2011-04-11 11:37:42 +0000 spiga: patch-series-mcinquil/
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12245 4525493e-7705-40b1-a816-d608a930855b

afdbc87 2011-03-29 16:52:13 +0000 spiga: From db79bf532a2927c6994b97b7c80ec906357f1654 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Add a null handler to the traceback in case we throw errors before the crab.log is created
From: Eric Vaandering <ewv@fnal.gov>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12119 4525493e-7705-40b1-a816-d608a930855b

283334b 2011-03-28 16:52:23 +0000 spiga: patch-series-mcinquil/
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12099 4525493e-7705-40b1-a816-d608a930855b

c977b52 2011-03-21 15:20:47 +0000 spiga: From 2e3949c9900c76a57b1c376bacaaf75b9c35260d Mon Sep 17 00:00:00 2001 Subject: [PATCH] Don't exposer user to tracebacks. Updated for latest head.
Signed-off-by: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@12019 4525493e-7705-40b1-a816-d608a930855b

2c67c80 2011-03-18 13:53:26 +0000 spiga: First fixes
Signed-off-by: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@11999 4525493e-7705-40b1-a816-d608a930855b

27efe9f 2011-03-11 15:23:33 +0000 metson: First pass at a client for CRAB3 Fixes #207 #1173
From: Simon Metson <simonmetson@googlemail.com>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@11893 4525493e-7705-40b1-a816-d608a930855b

