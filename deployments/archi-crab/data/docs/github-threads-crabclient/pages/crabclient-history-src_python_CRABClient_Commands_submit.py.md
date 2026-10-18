# dmwm/CRABClient: commit history of src/python/CRABClient/Commands/submit.py (at 970fabd75d68)

URL: https://github.com/dmwm/CRABClient/commits/master/src/python/CRABClient/Commands/submit.py

1fc14cb 2025-10-20 11:33:10 +0200 Stefano Belforte: use --jobId as arg for CMSRunAnalysis. Fix #5241 (#5422)
* use --jobId as arg for CMSRunAnalysis. Fix #5241

* pylint (a cleanup missed in #5419)

* typos in comments
cf12e74 2025-10-06 10:23:34 +0200 Stefano Belforte: remove filecacheurl. Fix #5411 (#5419)

e986360 2025-07-02 08:33:22 +0200 Stefano Belforte: enforce sitewhitelist when using userInputFiles. Fix #5400 (#5401)
* enforce sitewhitelist when using userInputFiles. Fix #5400

* pylint
6d396a3 2025-05-06 09:53:54 +0200 Stefano Belforte: add Data.lumisPerFile  fix #5385 (#5386)

6ce332b 2025-04-09 17:26:51 +0200 Stefano Belforte: make submit dryrun work with TW v3.250401 Fix #5383 (#5384)

653bafe 2024-11-07 09:31:35 +0100 Stefano Belforte: make --dryrun work again with TW v3.2411xx (#5347)

f372163 2023-12-01 14:14:14 +0100 Dario Mapelli: crab recover - new command (#5250)
* crab recover - first implementation using crab report

This commit provide a new crab command: crab recover.
run with:

crab recover --task=taskname

It aims at recovering tasks such that

- jobtype: analysis
- splitting: lumibased, eventawarelumibased, automatic
- publication: both on or off

What does not cover

- lumibased splitting

* crab recover - defaults to --strategy=notPublished

* crab recover - suppress debug messages

* crab recover - wa's review

* crab recover - silence log in all subcommand, apart from report

* crab recover - submit.py need to be aware of copycat and recover jobtypes

* crab recover - crab report prints proper message if the task does not need to be recovered

* crab recover - replace assert with exceptions

* crab recover - final touches to log messages

* crab recover - jobtype Recover manipulates only a single task configuration

* recover - if task can not be recovered, return exitcode 0 and commandStatus FAILED

* crab recover - adapt to both --dir and --task
da6d38f 2023-10-17 19:46:54 +0200 Stefano Belforte: make sure all commands return a dict. Fix #5224 (#5225)
* make sure all commands return a dict. Fix #5224

* fix two undefined vars

* use new CommandFailedException in crab.py

* add description of return dictionary

* checkusername must also return username, as before
3a27d49 2023-10-09 23:50:34 +0200 Stefano Belforte: Reduce curl verbosity (#5218)
* only print curl details on last failing iteration. Fix #5201

* Encoded request is already printed in CrabRestInterface
ecd2936 2023-02-10 15:59:37 +0100 Thanayut Seethongchuen: new Data.inputBlocks parameter (#5185)
* inputBlocks

* fix list args

* append dataset to block uuid

---------

Co-authored-by: Thanayut Seethongchuen <thanayut.seethongchuen@cern>
6637f80 2023-01-24 14:29:44 +0100 Dario Mapelli: submit --dryrun. print info about last trial (#5184)
submit --dryrun needs to run for at least 25s in order not
to make its estimates based on very few small events.
If the first dryrun attempt is too short, the same cmsRun
comman is called again, with an increasing number of events.
with this commit, every trial reports how long it took and
how many events the next trial will process.
e87a05d 2022-12-05 16:13:05 +0100 Thanayut Seethongchuen: new Site.acceleratorParams (#5179)
* new Site.acceleratorParams

* fix KeyError

Co-authored-by: Thanayut Seethongchuen <thanayut.seethongchuen@cern>
0e4c5cf 2022-12-05 15:35:10 +0100 Dario Mapelli: adapt CRABClient to new jobwrapper (#5180)
* adapt CRABClient to new jobwrapper

* submit, preparelocal: compatible with both old and new jobwrapper
8b8f2a2 2022-10-14 11:21:22 +0200 Thanayut Seethongchuen: Site.requireAccelerator (#5174)
* add requireAccelerator

* indent

Co-authored-by: Thanayut Seethongchuen <thanayut.seethongchuen@cern>
7248a05 2022-10-03 19:00:59 +0200 Stefano Belforte: deprecate publishWithGroupName (#5173)
* deprecate publishWithGroupName as per https://github.com/dmwm/CRABServer/issues/7359

* pylint

* pylint
353922e 2022-07-14 11:25:50 +0200 Thanayut Seethongchuen: Add Data.partialDataset option #5164 (#5168)
* WIP: add option in configmap

* fix: convert partialdataset

37caaf2 2022-02-25 17:19:28 +0100 Stefano Belforte: always use FEEDBACKMAIL. Solve #5155 (#5157)

b79c77b 2021-11-30 13:52:37 +0100 Stefano Belforte: execute dryrun test in a clean env. Fix #5121 (#5122)

25502cb 2021-11-19 10:21:51 +0100 Stefano Belforte: Remove old crab cache code (#5115)
* remove code which referenced to old CrabCache. Fix #5113 and fix #5114

* remove unneeded import
c3d0714 2021-08-12 12:18:51 +0200 Stefano Belforte: print task name and projdir also for --dryrun and use same API as Commands/status in checkStatusLoop. Fix #5060 (#5062)

2967546 2021-08-11 18:50:28 +0200 Stefano Belforte: no need to pass an env to the dryrun subprocess. Fix #5057 (#5058)

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
c7027f4 2021-06-11 15:29:58 +0200 Stefano Belforte: Wrap suprocesses calls with execute command fix 5017 (#5023)
* replace direct calls to suprocess with execute_command. fix #5017

* do not change cwd in execute_command

* fixes to first commit
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
e1ff736 2021-05-05 14:52:13 +0200 Stefano Belforte: add parasitic upload of tarablls to S3. Fix #4996 (#4997)
* add parasitic upload of tarablls to S3. Fix #4996

* stupid bug

* pylint

* no retries for parasitic S3 upload

* silence parasitic call to S3 upload

* fix hash calculation in testS3upload

* silence parasitic call to S3 upload and add some logging

* silence parasitic call to S3 upload and add some logging

* improve logging
a5c9b45 2021-04-20 23:22:23 +0200 Stefano Belforte: submit --dryrun can use S3. Fix #4991 (#4992)
* make submit capable to use S3 for dryrun sandbox. Fix #4991

* pass taskname (uniquerequestname) to executeTestRun

* small fix
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

521212f 2020-05-01 13:16:16 -0500 Stefano Belforte: make it easier to copy/paste suggested command

92418a4 2020-02-19 23:31:02 -0600 Stefano Belforte: Improve exception handling fix 4884 (#4885)
* indicate which exception type is caught

* add logger to server_info. Fix #4884



38235ad 2019-12-20 16:45:14 +0100 Leonardo Cristella: Resolve #4853 (#4862)

a1b100a 2019-10-22 04:08:08 -0500 Stefano Belforte: Use current value for server instance. Fix #4838 (#4839)

f17c209 2019-09-13 14:46:27 -0500 Stefano Belforte: when submitting, print where to (#4829)

a5775c3 2019-03-08 12:26:55 +0100 Leonardo Cristella: Resolve #4797 (#4801)
* 'minAutomaticRuntimeMins' is not a server parameter so can't be added in [`parametersMapping`](https://github.com/dmwm/CRABClient/pull/4801/files#diff-f0af4d07f2c1efc7257bf6d93fafcd9aR16)

3fd5972 2019-03-07 20:45:07 +0100 Leonardo Cristella: Revert #4799 (#4800)
This reverts commit ae58c6ee1bdd3c3905d8b4a8810fa44cec2a0652
because of:
https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/4664.html
ae58c6e 2019-03-07 12:37:31 +0100 Leonardo Cristella: No max job runtime min with automatic splitt (#4799)
Resolve #4797
71ec156 2019-02-28 15:24:04 +0100 Leonardo Cristella: Add project dir in 'crab submit' output (#4798)
* Decouple logpath validation from validateOptions()

* Add project dir to crab submit output

* Additional protection for remake command

461e187 2019-02-11 15:44:05 +0100 Leonardo Cristella: Align comments to code (#4792)
Polish code

052bc23 2019-02-11 11:29:52 +0100 Leonardo Cristella: Restore original behaviour of 'crab submit' (#4791)
Decouple option.config validation from SubCommand validateOptions()
ff5f0ab 2018-06-20 18:00:31 +0200 Leonardo Cristella: Avoid usage of 'maxJobRuntimeMin' with Automatic splitting (#4772)

407a8ab 2018-06-08 20:18:51 +0200 Leonardo Cristella: Avoid usage of '--dryrun' with Automatic splitting (#4769)
* Avoid usage of '--dryrun' with Automatic splitting
19cae61 2018-01-24 10:08:42 +0100 Matthias Wolf: Round out automatic splitting changes.
* Condense status display for the DAG
* Only list probe and split other job status for long display
  * Introduce "no output" as status for probes
  * Failed processing jobs turn "rescheduled"
* Better error message when resubmitting job ids that are "rescheduled"
* Add fractional dataset processing

ab8b516 2018-01-24 13:15:39 +0100 Stefano Belforte: Merge pull request #4731 from mmascher/standalone
Standalone execution of jobs
a32e69e 2018-01-11 18:25:28 +0100 Marco Mascheroni: Standalone execution of jobs

ecadec1 2017-10-31 00:31:32 +0100 belforte: make sure that configuration.Data.unitsPerJob is strictly >0. Fix #4727

962c169 2017-09-25 18:03:39 +0200 Stefano Belforte: warn users who try to set . Fix #4719 (#4723)

a890889 2017-09-25 18:01:07 +0200 Stefano Belforte: require a sitewhitelist with ignoreLocality. Fix #4646 (#4725)
Require a sitewhitelist with ignoreLocality. Fix #4646
ffd64af 2017-04-24 17:34:49 +0200 Matthias Wolf: Provide a default time for Automatic splitting. (#4690)
Move the error message to the configuration validation for all other
splitting modes.
7502a55 2017-03-02 13:50:56 +0100 Emilis Rupeika: Don't send additional input files list to server (#4679)

2dcc46e 2016-10-21 16:25:33 +0200 Emilis Rupeika: Put ignoreGlobalBlacklist flag in the DB

5bb5563 2016-09-02 10:06:29 +0200 Marco Mascheroni: Restoring master files

c1988b0 2016-08-19 17:02:23 +0200 Marco Mascheroni: Allow to ignore global blacklist (#4641)

0a5dcd6 2016-04-06 19:48:45 +0200 Marco Mascheroni: Add init-light script for lightweight client; fixed few bugs; updated .gitignore

772963b 2016-04-11 16:18:33 +0200 Matthias Wolf: Add automatic splitting to the client.

be0733a 2016-04-06 19:48:45 +0200 Marco Mascheroni: Add init-light script for lightweight client; fixed few bugs; updated .gitignore

afc3407 2016-03-24 00:59:39 +0100 Marco Mascheroni: Merge pull request #4598 from matz-e/fix-dryrun-scriptargs
Dry-run: Parse Condor DAG and JOB_AD files better.
770af91 2016-03-18 08:53:17 +0100 Marco Mascheroni: Have status ready for new state machine

d38fc49 2016-02-17 21:25:06 +0100 Matthias Wolf: Parse Condor DAG and JOB_AD files better.
Use a regular expression to parse the Condor settings and shlex to split
setting values.

Fixes dmwm/CRABServer#5125

9cf21e3 2015-11-24 11:35:33 +0100 Andres Tanasijczuk: Some pylint warning fixes.

085afd5 2015-11-19 11:27:02 +0100 Marco Mascheroni: Change maximum projdir len

1e7f796 2015-11-18 13:27:10 +0100 Andres Tanasijczuk: Don't accept request names longer than 80 characters.

18ec0c8 2015-09-30 10:47:38 +0200 Andres Tanasijczuk: Implement some of the DMWMBot pylint suggestions.

a3377d8 2015-09-30 10:29:50 +0200 Andres Tanasijczuk: Change pre-python 2.6 idioms to what DMWMBot suggests.

a554983 2015-09-21 15:28:49 +0200 Andres Tanasijczuk: Add user function getLumiListInValidFiles

91f1ef8 2015-08-17 22:28:41 +0200 Marco Mascheroni: Remove isbchecksum and useless calculateChecsum function in UserTarball. See https://github.com/dmwm/CRABServer/issues/4947

c231c6b 2015-08-13 13:03:45 +0200 Marco Mascheroni: Make dryrun ready for https://github.com/dmwm/CRABClient/pull/4519

ad378e8 2015-08-13 12:18:34 +0200 Marco Mascheroni: submit refactor: make configreq a class member

bb3c4b3 2015-07-21 10:43:36 +0200 Anna Elizabeth Woodard: A few whitespace changes ot make pylint happier.

9ad18a2 2015-07-21 10:29:34 +0200 Anna Elizabeth Woodard: Improvements for dryrun option. Fixes #4406.
Includes: suggestion for 'correct' splitting, warnings in case
memory exceeds normal envelope, and adding a CL option to skip
timing and memory estimates.

b3e8b66 2015-06-24 16:57:23 +0200 Andres Tanasijczuk: Add parameter Data.allowNonValidInputDataset to CRAB configuration.

ca2c242 2015-06-16 10:38:49 +0200 Andres Tanasijczuk: Add Data.publishWithGroupName parameter to CRAB config.

7773884 2015-05-27 16:42:11 +0200 Marco Mascheroni: Make sure firstEvent is not negative in dryrun

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

62b777c 2015-04-21 16:57:09 +0200 Mohd Nizam Yusli:  Add --wait option in crab resubmit. Fixes #4453

bb00d68 2015-04-17 14:58:18 +0200 Andres Tanasijczuk: Fix in check status loop for dryrun case.

4c72ea3 2015-03-26 19:25:06 +0100 Andres Tanasijczuk: Make clear which configuration are we talking about. Fixes #4354

a453522 2014-12-17 10:33:09 +0100 Andres Tanasijczuk: Change internal options in resubmit from strings to integers to align with taskdb. Don't harcode list-parameters in resubmit command. Interpret empty string in site white and black list options as an empty list.

7b29efe 2015-03-19 20:35:26 +0100 Andres Tanasijczuk: Give error if arguments are given but command doesn't take arguments. Try to unify validateOptions from uploadlog and SubCommand. Give default value None to logpath in uploadlog.

648c964 2015-03-20 15:46:48 +0100 Andres Tanasijczuk: snake_case -> camelCase changes.

9db5380 2015-03-19 09:59:45 +0100 Marco Mascheroni: Small client fix for --dryrun

04b5f13 2015-03-19 09:33:42 +0100 Marco Mascheroni: Improve completion message for task submitted with --wait

410a1d1 2015-03-16 23:07:16 +0100 Anna Elizabeth Woodard: Client side of fix for dmwm/CRABServer#4462. Add a 'dryrun' option for crab submit, which:
1) Tells the server not to submit the job, but instead upload a dry run sandbox to the UserFileCache
2) Downloads the sandbox and runs a 10-event local test to measure time/event and memory used
3) Uses local test results to give rough job processing time and memory requirement estimates

Also: add a 'proceed' subcommand, which can be used to continue a job which was initialized with dryrun.
Also: in checkStatusLoop in submit.py, wait between server queries, even if the current result is the same as the previous one.

e1b7e3f 2015-03-03 17:15:39 +0100 Marco Mascheroni: Fix logging error
In one particular case (crab submit --wait and failure) we were printing
None to the screen and the logfilter did not have a protection against
that. Protection added and printing of None removed (it was a stupid
mistake: `selfo.logger.info(self.logger.info("message"))` was used)

fdc1321 2015-02-18 14:28:30 +0100 Andres Tanasijczuk: Accept only one of Data.inputDataset and Data.userInputFiles. When running over user input files accept only FileBased splitting.

9035612 2015-02-13 12:15:33 +0100 Marco Mascheroni: Generate audio bell with submit --wait

18a620d 2015-02-06 16:20:45 +0100 Andres Tanasijczuk: Include all config params in client mapping. Add reverted mapping and use it where possible. Fixes #4393

0e45071 2015-01-23 08:17:17 +0100 Andres Tanasijczuk: Move check of renamed parameters from submit to SubCommand.

0966780 2015-01-18 18:50:11 +0100 Marco Mascheroni:     Changes for multicrab
    In CRABAPI: Use getLoggers from client_utilities, add a cmdexec
command
    that allows to better use commands.

    In the client: fix how we pass parameters to the Analysis/PrivateMC
    plugins, delete unused params, check if the tblogger has already an
    handler before adding a new one

61cf43a 2015-01-14 17:01:00 +0100 Andres Tanasijczuk: Move client_utilities to ClientUtilities and client_exceptions to ClientExceptions. Create UserUtilities module with user exposed methods (move user exposed methods from ClientUtilities to UserUtilities). Still keep a client_utilities module with the user exposed methods from UserUtilities imported, and printing a module retirement message. Fixes #4358.

fcfb812 2014-11-19 22:53:59 +0100 Andres Tanasijczuk: Add protection to avoid PrivateMC with inputDataset, and force specifying primaryDataset which is validated with WMCore.Lexicon. Move spellchecking from submit::__call__ to SubCommand::validateConfig.

bf70926 2014-12-18 12:24:53 +0100 Marco Mascheroni: Change errore message for config problems

2c8bb25 2014-12-16 20:05:55 +0100 Marco Mascheroni: Avoid using PrivateMC if an inputDataset is set. Fixes https://github.com/dmwm/CRABServer/issues/4597

5683fb8 2014-11-11 14:32:56 +0100 Andres Tanasijczuk: Pass job options (maxmemory, maxjobruntime, numcores, priority) to server in resubmit command.

d6e945f 2014-12-02 22:38:47 +0100 Andres Tanasijczuk: Replace s.lstrip('file:') by re.sub(r'^file:', '', s).

ee632fd 2014-12-01 14:48:50 +0100 Mohd Nizam Yusli: Improve msg and point to a twiki for unknown parameter in submit.py.Fixes #4314

f76929b 2014-11-29 03:35:18 +0100 Marco Mascheroni: Merge pull request #4322 from AndresTanasijczuk/dir_option
Change option -t/--task to -d/--dir.
45cb3f3 2014-11-17 16:04:11 +0100 Andres Tanasijczuk: Change option -t/--task to -d/--dir.

b8f6a27 2014-11-27 11:23:33 +0100 Matthias Wolf: Add option to use the parent dataset.

a070828 2014-10-20 19:58:34 +0200 Andres Tanasijczuk: Change option --skip-proxy to --proxy. Rename getHyperNewsName to getUsernameFromSiteDB. New wrapper functions for getUsernameFromSiteDB and getUserDN; new function getUserDNandUsernameFromSiteDB. Use getUserDNandUsernameFromSiteDB in checkusername; and in checkwrite (when retrieving username) instead of CredentialInteractions.

223400d 2014-10-03 11:26:33 +0200 Andres Tanasijczuk: Rename some configuration parameters.

5a09fa2 2014-09-28 23:06:54 +0200 Marco Mascheroni: Add extraJDL parameter

25ff937 2014-09-19 15:30:58 +0200 Marco Mascheroni: Add parameters needed for scriptexe

3266055 2014-07-14 16:31:05 +0200 qunox: Client library API, client changes. See #4091
alpha release of crabclient library api

Rebase of the client library

minor correction

Client Library: redo logging and create cmdexec

Add class Task for client API

Some pull requests you might look for history:
https://github.com/dmwm/CRABClient/pull/4213
https://github.com/dmwm/CRABClient/pull/4234

80135ad 2014-08-22 13:04:07 -0500 Andrew Melo: Code needed to inject dependencies into CRABClient
Ideally, testing involves both unittesting (doesn't touch external
services) and fuller testing (sometimes called integration testing).
This is a first step to allow testing with external services by
injecting "fake" classes that look and feel like external services

da9457b 2014-08-26 17:55:57 +0200 qunox: fix #4136 upload automatically the log file for unhandled exception

63f6f9f 2014-08-23 16:56:00 +0200 Andres Tanasijczuk: Use Analysis as default job type. Put all possible config parameters in the client mapping. Better organize client mappings. Print unique task name on submit output.

9d7a8dc 2014-08-21 12:41:45 +0200 Andres Tanasijczuk: Allow USER input datasets to be read from global DBS. Allow phys0x DBS only for USER input dataset. Move the validation of DBS URLs (and aliases) to validateConfig.

2054881 2014-07-30 11:28:45 +0200 Marco Mascheroni: Merge pull request #4196 from AndresTanasijczuk/dbs
Check dbsUrl is a local DBS instance if inputDataset tier is USER
11030d9 2014-07-22 16:52:40 +0200 Marco Mascheroni: Merge pull request #4193 from AndresTanasijczuk/warning_msg_publ
Add warning message that non-EDM files will not be published
20afbd8 2014-07-21 16:52:35 +0200 Andres Tanasijczuk: Check that config param dbsUrl is a local DBS instance if inputDataset tier is USER.

cd0457c 2014-07-18 16:58:40 +0200 Andres Tanasijczuk: Add warning message that non-EDM files will not be published

8d58479 2014-07-18 11:53:55 +0200 qunox: removing all short options and improve crab report

a3d7d21 2014-07-08 14:01:57 +0200 Marco Mascheroni: Merge pull request #4170 from qunox/enforcestr
enforce str to encoded_rquest return
cbacfea 2014-07-08 13:24:30 +0200 qunox: enforce str to encoded_rquest return

6421b46 2014-07-07 08:05:12 +0200 qunox: fix and improve cosmetic error

aa6ab84 2014-07-02 15:42:58 +0200 Andres Tanasijczuk: Improve options parsing and passing config params from command line in submit command.

c085def 2014-07-01 17:35:54 +0200 Marco Mascheroni: Merge pull request #4153 from AndresTanasijczuk/optparser_config
Fix config argument recognition.
a7fdecd 2014-07-01 11:26:35 +0200 Marco Mascheroni: Merge pull request #4134 from qunox/colorfix
better cosmetic 
67340ff 2014-07-01 01:40:33 +0200 Andres Tanasijczuk: Fix config argument recognition.

b6620f1 2014-06-20 10:25:48 +0200 qunox: better cosmetic

4e27564 2014-06-19 11:06:15 +0200 Andres Tanasijczuk: Allow section User to not be specified in the config file.

68183c3 2014-06-05 17:11:30 +0200 Andres Tanasijczuk: Allow aliases for DBS URLs.

28a06f5 2014-06-11 15:29:27 +0200 Marco Mascheroni: Merge pull request #4106 from AndresTanasijczuk/booleans
Correctly propagate boolean parameters.
d967fe4 2014-06-05 17:44:40 +0200 Andres Tanasijczuk: Correctly propagate boolean parameters.

9e03678 2014-06-05 13:24:27 +0200 Andres Tanasijczuk: Set default for Data.publishDbsUrl.

20b6cc6 2014-06-04 14:08:41 +0200 Marco Mascheroni: Merge pull request #4093 from AndresTanasijczuk/storage
Change validateConfig so that storageSite does not need to be provided i...
81220bc 2014-06-04 14:01:58 +0200 Andres Tanasijczuk: Change validateConfig so that storageSite does not need to be provided if saveLogs and transferOutput are both False.

9497ef5 2014-06-04 13:37:46 +0200 Andres Tanasijczuk: Give General.transferOutput a default of True.

973b1fb 2014-06-03 13:28:33 +0200 Andres Tanasijczuk: Make Site.storageSite not a required parameter unless General.saveLogs or General.transferOutput are True. Make Data.splitting a required parameter. Make General.saveLogs and Data.publishDataName not required parameters (they default to False and an empty string respectively).

1dc23fd 2014-05-08 12:33:09 +0200 Marco Mascheroni: Green color in submit message + status simple fix

17d75f7 2014-05-12 10:49:07 +0200 qunox: quick fix on the output message when option wait is use

5c76e5c 2014-05-06 16:03:44 +0200 Marco Mascheroni: Update submit.py

7c5e9f9 2014-05-05 22:16:23 +0200 Marco Mascheroni: Convert ignoreLocality flag to integer

887bada 2014-04-30 10:19:36 +0200 qunox: no asnyc submision by default

ab2a669 2014-04-22 14:44:20 +0200 Marco Mascheroni: Fix UFC: was not considering the urls from the external conf

578fca1 2014-04-10 16:11:13 +0200 Marco Mascheroni: Consider the 'UNKNOWN' task state as successful in crab submit

0b14b3b 2014-03-17 14:40:51 +0100 qunox: submit only show message if job status change

bf10227 2014-02-26 10:50:28 +0100 Marco Mascheroni: Merge pull request #4016 from qunox/newSubmit
some changes and feutures in submit.py
e087b59 2014-02-18 11:54:52 +0100 qunox: some changes and feutures in submit.py

6d82203 2014-02-11 15:07:48 +0100 Brian: Allow users to specify a list of files to process as the primary input.

43abd1d 2014-01-08 12:11:43 +0100 Marco Mascheroni: Add the flag to allow non production releases of CMSSW

649e216 2013-12-28 14:25:51 +0100 Marco Mascheroni: Adjust error message in submit check status loop

05287f6 2013-12-27 03:11:09 -0800 Marco Mascheroni: Merge pull request #4003 from qunox/stuff
Implement syncronous submit by checking the status of the task after sub...
bc5fe86 2013-11-28 11:32:13 +0100 qunox: Implement syncronous submit by checking the status of the task after submission. Fix for issue #4078 and #4081

089826e 2013-12-16 18:58:39 +0100 Marco Mascheroni: Delete automatic blacklisting of T1s

ef72917 2013-11-18 11:31:33 +0100 Marco Mascheroni: Fix oneEventMode parameter setting when no configuration is passed

1b4ce20 2013-11-11 23:00:59 -0600 Andrew Melo: adding oneEventMode to client

2d0ee9d 2013-09-11 17:06:21 +0200 spiga: remove ServerInteraction switching to RESTInteraction

05f3436 2013-09-10 09:59:19 +0200 Marco Mascheroni: Pass baseurl to PandaServerInterface so that we can figure out which panda cache to use. CAF-297

be6d7ea 2013-08-14 12:30:57 +0200 spiga: remove integer args to ConfigurationException

8ceb361 2013-06-27 15:08:59 +0200 Marco Mascheroni: Ask the server the URLs to use for PandaServerInterface. CAF-278

ab61185 2013-06-20 19:53:58 +0200 spiga: Fixing MC plugin. Adapt to the PanDA related changes. New input parameter Improve Validation CAF-309 and CAF-211

4fe1a70 2013-06-13 15:06:35 +0200 mcinquil: client now handles prod/preprod/dev/private. clientmapping, submit and subcommand have been refactored. More refactoring work would be needed to make things nicer. CAF-275
Signed-off-by: cinquo <m.cinquilli@gmail.com>

f936e8e 2013-06-13 10:50:23 +0200 cinquo: Handling server url by instance type

7c2901f 2013-06-11 11:58:41 +0200 cinquo: Removing old deprecated cache parameters - CAF-288

ba7d2ea 2013-06-05 16:13:27 +0200 spiga: remove obsolete import

b4e2561 2013-06-05 11:06:43 +0200 Valentina Mancinelli: adding flag for publication from config

164f252 2013-06-04 18:13:42 +0200 spiga: resolve bug on the config handling

46824a5 2013-05-31 11:04:23 +0200 cinquo: Cleaning import, most of them, removing deprecated dependencies CAF-162

b3cd795 2013-04-19 18:52:32 +0200 mcinquil: Adding isb hash to publish data name fixes CAF-159
Signed-off-by: cinquo <m.cinquilli@gmail.com>

3ac28d2 2013-03-13 08:36:44 +0100 Marco Mascheroni: Create initial commit for Common Analysis Framework project. CAF-59

c365a30 2012-09-28 16:30:44 +0200 Marco Mascheroni: Change the default database name of configcache

03818fa 2012-07-31 16:21:37 +0200 Marco Mascheroni: Do not use anymore acdc for lumi mask. Fixes #3936

62a44c0 2012-06-19 16:09:34 +0000 spiga: Reactivated skip-proxy parameter. Fixes #3835
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@16018 4525493e-7705-40b1-a816-d608a930855b

12be7df 2012-06-08 14:27:55 +0000 spiga: Remove unused import in submit. Fixes #3831
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15991 4525493e-7705-40b1-a816-d608a930855b

02545b9 2012-06-06 16:43:51 +0000 spiga: From 97299784bd6fb6f10667d23c1ad536abf885a3fe Mon Sep 17 00:00:00 2001 Subject: [PATCH 1/2] Check and renew myproxy certificates at each client command. #Fixes #3810
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15983 4525493e-7705-40b1-a816-d608a930855b

7e73c57 2012-05-10 12:45:52 +0000 spiga: From a3c6fc0fa1d1bfdecc0fcba51e3d7f07158a0159 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Adding the server delegation parameter to the configuration. Fixes #3448
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15885 4525493e-7705-40b1-a816-d608a930855b

60a69c2 2012-05-10 07:16:27 +0000 spiga: From ad26ad4b2c692b164f27357d85f93f9121cedea7 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Added default value for configcache parameters. Fixes #3652
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15882 4525493e-7705-40b1-a816-d608a930855b

e66567c 2012-04-27 14:16:29 +0000 spiga: From cab198a8cfd21933b15d68d231652a67183142eb Mon Sep 17 00:00:00 2001 Subject: [PATCH] Added requiresTaskOption to the mapping, deleted /data from the uri path with status -f, refactor. Fixes #3661
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15820 4525493e-7705-40b1-a816-d608a930855b

42b5b74 2012-04-02 15:30:06 +0000 spiga: From 26ace87a6482451d4598974528a930419a63828e Mon Sep 17 00:00:00 2001 Subject: [PATCH 1/2] ISB url, encoding parameter during submit, output message if HTTPException. Fixes #3473
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15579 4525493e-7705-40b1-a816-d608a930855b

de4a7b1 2012-04-02 15:27:53 +0000 spiga: From f65368c51138f425e5cd18eef7001ee97479c543 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Polished error messages in case of HTTPException, computation of total number of jobs is done in the status and not server-side anymore, renabled default server url, UFC use server url if not specified in the config. Fixes #3425
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15576 4525493e-7705-40b1-a816-d608a930855b

01fba9f 2012-03-21 09:43:11 +0000 spiga: Client adapted to match the new rest. Fixes #3374
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@15471 4525493e-7705-40b1-a816-d608a930855b

00bd8e9 2012-01-24 11:19:45 +0000 spiga: From 799f5a57f90c0775260d5449f9d099340b87ad91 Mon Sep 17 00:00:00 2001 Subject: [PATCH] Fixes #3075
From: Eric Vaandering <ewv@fnal.gov>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14983 4525493e-7705-40b1-a816-d608a930855b

71d08d5 2012-01-17 16:32:37 +0000 spiga: Added the removeT1blacklisting parameter, Fixes #3110
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14950 4525493e-7705-40b1-a816-d608a930855b

f216c29 2012-01-16 16:00:49 +0000 spiga: differentiate-import-notfound, fixes #3103
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14945 4525493e-7705-40b1-a816-d608a930855b

bf074aa 2011-12-16 10:45:32 +0000 spiga: Implemented modifications to use pycurl. Fixes #2869
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14795 4525493e-7705-40b1-a816-d608a930855b

04e3a46 2011-12-09 12:42:23 +0000 spiga: From 8600dca40ad72144bbcbfbde99ce62382b8ce1bc Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch> - Replacing  fixes #2974
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14755 4525493e-7705-40b1-a816-d608a930855b

37ee6c1 2011-12-01 13:43:11 +0000 spiga: From 4404c1f3bf783cc77ade30341e557ba3e4fb64cb Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch> - Missing argument  to get CLI paramters - fixes #2934
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14697 4525493e-7705-40b1-a816-d608a930855b

00f9544 2011-11-29 19:09:40 +0000 spiga: Better handling of user messaged. Fixes #2880, #2893, #2641
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14669 4525493e-7705-40b1-a816-d608a930855b

12b355c 2011-11-18 08:32:19 +0000 spiga: Takes parameters from the ClientMapping and check if user config params are there. Fixes #2678
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14577 4525493e-7705-40b1-a816-d608a930855b

af3c205 2011-11-12 00:03:01 +0000 spiga: Automatically set team and group as Analysis. Fixes #2832
From: Marco Mascheroni <marco.mascheroni@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14542 4525493e-7705-40b1-a816-d608a930855b

7c28168 2011-11-11 23:47:09 +0000 spiga: From 154cc59c0aaa94589e7bd1c2d39073bdb598743a Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch>; fixes #2180
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14536 4525493e-7705-40b1-a816-d608a930855b

e228de9 2011-11-11 23:38:54 +0000 spiga: From a909de48bdbbdd4d236d9fa655d8c4907b798ce1 Mon Sep 17 00:00:00 2001 Subject: [PATCH] From mcinquil <mattia.cinquilli@cern.ch>; fixes #2776
From: mcinquil <mcinquil@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14534 4525493e-7705-40b1-a816-d608a930855b

c5585c3 2011-10-27 12:56:05 +0000 spiga: Fixes #2681 patch-series-spiga/
From: spiga <spiga@cern.ch>


git-svn-id: svn+ssh://svn.cern.ch/reps/CMSDMWM/CRABClient/trunk@14359 4525493e-7705-40b1-a816-d608a930855b

