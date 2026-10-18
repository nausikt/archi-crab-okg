# dmwm/CRABServer pull request #8531: Remove HTCondorUtils.py #8339

State: closed
Opened: 2024-06-27T08:36:49Z
Closed: 2024-07-05T10:36:18Z
Merged: 2024-07-05T10:36:18Z
URL: https://github.com/dmwm/CRABServer/pull/8531

## Opening post (aspiringmind-code, 2024-06-27T08:36:49Z)

See https://github.com/dmwm/CRABServer/issues/8339

## Comment (belforte, 2024-06-27T08:39:56Z)

did you test this ?

## Comment (cmsdmwmbot, 2024-06-27T08:40:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 1 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2036/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-06-28T12:12:59Z)

REST tested locally on K8s pod

crab3@crabserver-69b4975fc7-64ns9:/data/repos/CRABServer$ git checkout vchakrav27/06/24_Issue8339
Branch 'vchakrav27/06/24_Issue8339' set up to track remote branch 'vchakrav27/06/24_Issue8339' from 'vchakrav'.
Switched to a new branch 'vchakrav27/06/24_Issue8339'
crab3@crabserver-69b4975fc7-64ns9:/data/repos/CRABServer$ cd /data
crab3@crabserver-69b4975fc7-64ns9:/data$ ./start.sh -g -d
Stop crabserver service... 97 99 
Removing stale pid file /data/srv/state/crabserver/crabserver.pid
[28/Jun/2024:10:28:31]  INFO: final CherryPy configuration: {'engine.autoreload.on': False,
 'request.methods_with_bodies': ('POST', 'PUT', 'DELETE'),
 'request.show_tracebacks': False,
 'server.environment': 'production',
[...]
[28/Jun/2024:10:32:09]  RESTSQL:DlFSjowYUZIT ENTER cmsweb_crab_9r_dev@int2r CRABInterface.RESTBaseAPI.RESTBaseAPI (GET devtwo workflowdb) inuse=0 idle=1 - Podname=crabserver-69b4975fc7-64ns9 Type=cherrypylog
[28/Jun/2024:10:32:09]  RESTSQL:DlFSjowYUZIT (previously JLEyiCjFpzNh) connected, client: 21.5.0.0.0, server: 19.21.0.0.0, stmtcache: 50 - Podname=crabserver-69b4975fc7-64ns9 Type=cherrypylog
[28/Jun/2024:10:32:09]  RESTSQL:DlFSjowYUZIT ping - Podname=crabserver-69b4975fc7-64ns9 Type=cherrypylog
[28/Jun/2024:10:32:09]  RESTSQL:DlFSjowYUZIT check [select sysdate from dual] - Podname=crabserver-69b4975fc7-64ns9 Type=cherrypylog
[28/Jun/2024:10:32:09]  RESTSQL:DlFSjowYUZIT connection established - Podname=crabserver-69b4975fc7-64ns9 Type=cherrypylog
[...]

## Comment (belforte, 2024-06-28T13:17:07Z)

IIUC that means that crabserver is started. That's good, but you should also use it :-)
Changes in this PR only affect taskworker, by the way.

## Comment (novicecpp, 2024-06-28T13:32:56Z)

The `HTCondorUtils` is also inside `setup.py`. Please remove it too.

https://github.com/dmwm/CRABServer/blob/f37fd44274ed7fbb225036df55538bead2bb0e69/setup.py#L42

We use setup.py when run buildTWTarballs.sh here

https://github.com/dmwm/CRABServer/blob/f37fd44274ed7fbb225036df55538bead2bb0e69/cicd/crabtaskworker_pypi/buildTWTarballs.sh#L52

I am not sure why `buildTWTarballs.sh` did not break when I taught Vijay how to run `./start.sh -g`.

## Comment (aspiringmind-code, 2024-06-28T14:39:40Z)

References to HTCondorUtils in setup.py removed in PR https://github.com/aspiringmind-code/CRABServer/pull/1

## Comment (belforte, 2024-06-28T14:48:15Z)

Vijay, to modify `setup.py` you can simply add a commit to this branch in your local and do a `git push` no need to make a PR

## Comment (cmsdmwmbot, 2024-06-28T15:16:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 42 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2041/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2024-07-03T15:02:12Z)

TaskWorker tested on crab-dev-tw05

[vchakrav@lxplus9102 myfirstcrabtask]$ crab status -d ./crab_20240628_153254
Rucio client intialized for account vchakrav
CRAB project directory:		/afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20240628_153254
Task name:			240628_133258:vchakrav_crab_20240628_153254
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test11.cern.ch/crabserver/ui/task/240628_133258%3Avchakrav_crab_20240628_153254
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=240628_133258%3Avchakrav_crab_20240628_153254&from=1719577981000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol', 'T2_FR_GRIF']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (10/10)

Publication status of 1 dataset(s):	new          		100.0% (10/10)
(from CRAB internal bookkeeping in transferdb)

Output dataset:			/GenericTTbar/vchakrav-autotest-1719581574-94ba0e06145abd65ccb1d21786dc7e1d/USER
Output dataset DAS URL:		https://cmsweb.cern.ch/das/request?input=%2FGenericTTbar%2Fvchakrav-autotest-1719581574-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER&instance=prod%2Fphys03

Warning: the max jobs runtime is less than 30% of the task requested value (60 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 92MB min, 625MB max, 265MB ave
 * Runtime: 0:02:11 min, 0:04:32 max, 0:02:45 ave
 * CPU eff: 5% min, 12% max, 8% ave
 * Waste: 0:01:26 (5% of total)

Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20240628_153254/crab.log

## Comment (belforte, 2024-07-05T10:32:10Z)

@aspiringmind-code was that a new build of TW container which included this change ? The information which you put above indicates that a TW was working, but not which one !

## Comment (aspiringmind-code, 2024-07-05T10:35:17Z)

@belforte 
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED       STATUS       PORTS     NAMES
e2f097b1c73e   registry.cern.ch/cmscrab/crabtaskworker:v3.240618-stable   "tini -- /data/run.sh"   7 days ago    Up 7 days              TaskWorker
of crab-dev-tw05
