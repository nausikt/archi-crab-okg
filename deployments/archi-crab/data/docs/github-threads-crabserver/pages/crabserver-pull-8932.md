# dmwm/CRABServer pull request #8932: deprecate numcores option for resubmit on CRABServer side

State: closed
Opened: 2025-02-17T14:31:53Z
Closed: 2025-06-17T07:55:26Z
Merged: 2025-06-17T07:55:26Z
URL: https://github.com/dmwm/CRABServer/pull/8932

## Opening post (aspiringmind-code, 2025-02-17T14:31:53Z)

See https://github.com/dmwm/CRABClient/issues/5369

## Comment (cmsdmwmbot, 2025-02-17T14:34:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 77 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2377/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-02-17T14:41:28Z)

Now we need a proper timeline of when changes can be merged, tagged, deployed. Since we can't make this change in TW until the extra option is removed from Client. But may want to do other changes, so merging in master may not be ideal.

## Comment (belforte, 2025-02-17T14:42:10Z)

Also, I'd like to review code which has been tested, if possible.

## Comment (aspiringmind-code, 2025-02-17T15:00:45Z)

Put on hold for now.

## Comment (belforte, 2025-05-13T18:50:18Z)

the change in CRABClient is now in production. We can look forward to do final test and close.
Test is simply to try `crab resubmit` against a CRABServer REST with these modifications.
@aspiringmind-code please do that.

## Comment (cmsdmwmbot, 2025-05-19T08:24:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2453/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-19T13:06:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 18 comments to review
 * Pycodestyle check: succeeded
   * 79 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2455/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-19T13:22:23Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 47 comments to review
 * Pycodestyle check: succeeded
   * 375 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2456/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-22T14:34:45Z)

I think you can remove the "Draft" status. Was it set simply as a way to hold until client is ready ? Or do you still want to change things ?

## Comment (cmsdmwmbot, 2025-05-23T09:11:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 376 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2476/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-23T09:21:09Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 warnings
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 405 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2477/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-23T10:08:45Z)

thanks for catching that last instance of `numcores` :rocket:

## Comment (aspiringmind-code, 2025-05-23T10:11:54Z)

I think there's still somewhere that I am missing. Crab resubmit still gives this error.
```
[vchakrav@lxplus978 myfirstcrabtask]$ crab resubmit -d /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250523_113112/
Rucio client intialized for account vchakrav
Sending resubmit request to the server.
Fatal error trying to connect to https://cmsweb-test12.cern.ch:8443/crabserver/devthree/workflow using workflow=250523_093118%3Avchakrav_crab_20250523_113112&subresource=resubmit2&publication=0&jobids=5&jobids=3&jobids=2&jobids=1&jobids=4.
exit code from curl = 0
HTTP code/reason = 500/Internal Server Error .  stdout:
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
    <title>500 Internal Server Error</title>
    <style type="text/css">
    #powered_by {
        margin-top: 20px;
        border-top: 2px solid black;
        font-style: italic;
    }

    #traceback {
        color: red;
    }
    </style>
</head>
    <body>
        <h2>500 Internal Server Error</h2>
        <p>Execution error</p>
        <pre id="traceback"></pre>
    <div id="powered_by">
      <span>
        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.8.0</a>
      </span>
    </div>
    </body>
</html>

The server answered with an error.
Server answered with: Execution error
Error Id: c6c97cd1bd2de1f189d2dd27521e4db2
```

## Comment (aspiringmind-code, 2025-05-23T10:15:30Z)

I guess in Task.py

## Comment (belforte, 2025-05-23T10:24:41Z)

you can grep for  the ErrorId `c6c97cd1bd2de1f189d2dd27521e4db2` in the K8s log file and find the traceback

## Comment (belforte, 2025-06-06T10:25:55Z)

@aspiringmind-code did you/we forget to follow up on this ?

## Comment (aspiringmind-code, 2025-06-06T10:50:34Z)

Oh yes...thanks for reminding me.

## Comment (cmsdmwmbot, 2025-06-06T10:55:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 4 warnings
   * 47 comments to review
 * Pycodestyle check: succeeded
   * 405 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2495/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-06-06T11:55:18Z)

```
[vchakrav@lxplus910 ~]$ kubectl logs crabserver-5cb55d5c9b-drmm4 -n crab | grep '5ba530b78fb30cde10f76d6195680a7b'
[06/Jun/2025:13:43:00]  SERVER DATABASE ERROR 500/403 Execution error __builtins__.TypeError 5ba530b78fb30cde10f76d6195680a7b [instance: devthree] (resubmit2() got an unexpected keyword argument 'numcores'); last statement: None; binds: None, None; offset: None - Podname=crabserver-5cb55d5c9b-drmm4 Type=cherrypylog
```

## Comment (aspiringmind-code, 2025-06-06T11:57:29Z)

The first time the resubmit command worked
```
[vchakrav@lxplus910 myfirstcrabtask]$ crab resubmit -d /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250606_132924/ --jobids=1-5
Rucio client intialized for account vchakrav
Not possible to resubmit the following jobs:
['3']
Only jobs in status failed can be resubmitted. Jobs in status finished can also be resubmitted, but only if the jobid is specified and the force option is set. Successful jobs can only be resubmitted before the task is COMPLETED
```
but second time got the error.

## Comment (aspiringmind-code, 2025-06-06T12:07:40Z)

I think the problem is [here](https://github.com/aspiringmind-code/CRABServer/blob/09bcb36f3151530426ec58e63a6afe19a82a6fa1/src/python/CRABInterface/RESTUserWorkflow.py#L614)

## Comment (cmsdmwmbot, 2025-06-06T12:17:41Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 8 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 511 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2496/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-06-06T12:42:50Z)

> The first time the resubmit command worked

maybe the first time the client refused to post the resubmit comment to CRABServer because job was not in an allowed status ?

## Comment (belforte, 2025-06-06T12:48:55Z)

but I thought that client does not add numcores anymore when doing resubmit. Why an "unexpected argument" ? numcores argument is tested in the [validate step](https://github.com/aspiringmind-code/CRABServer/blob/09bcb36f3151530426ec58e63a6afe19a82a6fa1/src/python/CRABInterface/RESTUserWorkflow.py#L480C12-L480C65) so should be fully harmless.

## Comment (belforte, 2025-06-06T12:54:27Z)

btw, IIUC you still have `numores` in [resubmit2()](https://github.com/aspiringmind-code/CRABServer/blob/09bcb36f3151530426ec58e63a6afe19a82a6fa1/src/python/CRABInterface/DataWorkflow.py#L253) so are likely to get an undefined variable or missing argument exception now.

## Comment (belforte, 2025-06-06T12:56:24Z)

somehow it seems I was not looking at the correct branch. I better shut up

## Comment (aspiringmind-code, 2025-06-06T12:58:39Z)

> btw, IIUC you still have `numores` in [resubmit2()](https://github.com/aspiringmind-code/CRABServer/blob/09bcb36f3151530426ec58e63a6afe19a82a6fa1/src/python/CRABInterface/DataWorkflow.py#L253) so are likely to get an undefined variable or missing argument exception now.

I believe you're looking at the wrong branch. In deprecate_numcores branch [here](https://github.com/aspiringmind-code/CRABServer/blob/c40fedcdc75c734ff5865c8e20dea76ad31c10e3/src/python/CRABInterface/DataWorkflow.py#L252) numcores option isn't there.

## Comment (aspiringmind-code, 2025-06-06T13:00:04Z)

But yeah you're right that the problem persists even after the recent changes.
```
[vchakrav@lxplus910 ~]$ kubectl logs crabserver-598975954-mdhmn -n crab | grep 'e7646c8538c6cb5e6f8583e419eb38c4'
[06/Jun/2025:14:48:37]  SERVER DATABASE ERROR 500/403 Execution error __builtins__.TypeError e7646c8538c6cb5e6f8583e419eb38c4 [instance: devthree] (post() got an unexpected keyword argument 'numcores'); last statement: None; binds: None, None; offset: None - Podname=crabserver-598975954-mdhmn Type=cherrypylog
```

## Comment (aspiringmind-code, 2025-06-06T13:05:53Z)

Ok must be where this post is being called

## Comment (aspiringmind-code, 2025-06-06T14:38:38Z)

The problem is fixed now. I had to stop and start the crabserver to pick the latest change. 
Tested
```
[vchakrav@lxplus910 myfirstcrabtask]$ crab resubmit -d /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250606_132924/ --jobids=6-10
Rucio client intialized for account vchakrav
Sending resubmit request to the server.
Resubmit request sent to the server.
Please use ' crab status ' to check how the resubmission process proceeds.
Notice it may take a couple of minutes for the resubmission to get fully processed.
Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250606_132924/crab.log
[vchakrav@lxplus910 myfirstcrabtask]$ crab status
Rucio client intialized for account vchakrav
CRAB project directory:		/afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250606_132924/
Task name:			250606_112927:vchakrav_crab_20250606_132924
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw03
Status on the CRAB server:	NEW on command RESUBMIT
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/250606_112927%3Avchakrav_crab_20250606_132924
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=250606_112927%3Avchakrav_crab_20250606_132924&from=1749205768000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol', 'T2_IT_Bari']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	FAILED

Jobs status:                    failed       		100.0% (10/10)

No publication information available yet

Error Summary: (use crab status --verboseErrors for details about the errors)

 7 jobs failed with exit code 50664

 3 jobs failed in postprocessing step

Have a look at https://twiki.cern.ch/twiki/bin/viewauth/CMSPublic/JobExitCodes for a description of the exit codes.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 69MB min, 804MB max, 557MB ave
 * Runtime: 0:02:44 min, 0:04:51 max, 0:04:13 ave
 * CPU eff: 0% min, 4% max, 2% ave
 * Waste: 1:03:37 (60% of total)

Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250606_132924/crab.log
```

## Comment (cmsdmwmbot, 2025-06-16T09:32:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 8 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 511 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2499/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T09:34:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 8 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 511 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2500/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T10:20:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 10 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 534 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2501/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T11:10:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 10 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 534 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2502/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-16T14:13:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 10 warnings
   * 107 comments to review
 * Pycodestyle check: succeeded
   * 534 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2504/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-06-16T14:18:54Z)

Fixed now
```
[vchakrav@lxplus989 crab_20250616_131334]$ crab resubmit -d /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/ --jobids=6-8
Contacting voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u150799.

Your proxy is valid until Tue Jun 24 15:18:57 CEST 2025
Rucio client intialized for account vchakrav
Sending resubmit request to the server.
Resubmit request sent to the server.
Please use ' crab status ' to check how the resubmission process proceeds.
Notice it may take a couple of minutes for the resubmission to get fully processed.
Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/crab.log
[vchakrav@lxplus989 crab_20250616_131334]$ crab resubmit -d /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/ --jobids=6-8
Rucio client intialized for account vchakrav
Sending resubmit request to the server.
Resubmit request sent to the server.
Please use ' crab status ' to check how the resubmission process proceeds.
Notice it may take a couple of minutes for the resubmission to get fully processed.
Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/crab.log
[vchakrav@lxplus989 crab_20250616_131334]$ crab status
Rucio client intialized for account vchakrav
CRAB project directory:		/afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/
Task name:			250616_111338:vchakrav_crab_20250616_131334
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw03
Status on the CRAB server:	NEW on command RESUBMIT
Task URL to use for HELP:	https://cmsweb-test12.cern.ch/crabserver/ui/task/250616_111338%3Avchakrav_crab_20250616_131334
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=vchakrav&var-task=250616_111338%3Avchakrav_crab_20250616_131334&from=1750068818000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	FAILED

Jobs status:                    failed       		100.0% (10/10)

No publication information available yet

Error Summary: (use crab status --verboseErrors for details about the errors)

10 jobs failed with exit code 50664

Have a look at https://twiki.cern.ch/twiki/bin/viewauth/CMSPublic/JobExitCodes for a description of the exit codes.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 266MB min, 830MB max, 496MB ave
 * Runtime: 0:01:08 min, 0:01:11 max, 0:01:09 ave
 * CPU eff: 0% min, 16% max, 5% ave
 * Waste: 0:00:00 (0% of total)

Log file is /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250616_131334/crab.log
```

## Comment (aspiringmind-code, 2025-06-16T14:22:18Z)

Ready for your review @belforte Thanks!

## Comment (belforte, 2025-06-16T14:57:27Z)

Looks very good, thanks. Of course it also looked good when not-working, not all issues are apparent when simply reading the code !

## Comment (aspiringmind-code, 2025-06-17T07:55:14Z)

Thanks @sinonkt and @belforte For your help debugging this. Merging.
