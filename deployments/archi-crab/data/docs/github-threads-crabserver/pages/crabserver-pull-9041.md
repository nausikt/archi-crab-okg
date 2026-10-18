# dmwm/CRABServer pull request #9041: avoid returning outputs to resolve pickling issues

State: closed
Opened: 2025-04-10T09:33:57Z
Closed: 2025-04-10T11:12:00Z
Merged: 2025-04-10T11:12:00Z
URL: https://github.com/dmwm/CRABServer/pull/9041

## Opening post (aspiringmind-code, 2025-04-10T09:33:57Z)

Fix #9040

## Comment (cmsdmwmbot, 2025-04-10T09:37:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2426/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-04-10T10:01:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2427/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-04-10T10:05:46Z)

did you test this ?

## Comment (aspiringmind-code, 2025-04-10T10:08:26Z)

Yes, on preprod. We don't get the pickling error anymore. However, since I was using CRABClient, we get the following which is resolved:
```
[vchakrav@lxplus972 myfirstcrabtask]$ crab submit --dryrun -c HC-1kj.py
Will use CRAB configuration file HC-1kj.py
Contacting voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u150799.

Your proxy is valid until Fri Apr 18 11:27:55 CEST 2025
Importing CMSSW configuration pset.py
Finished importing CMSSW configuration pset.py
Sending the request to the server at cmsweb-testbed.cern.ch
Success: Your task has been delivered to the preprod CRAB3 server.
Task name: 250410_092758:vchakrav_crab_20250410_112754
Project dir: ./crab_20250410_112754
Waiting for task to be processed
Checking task status
Task status: WAITING
Please wait...
Task status: UPLOADED

Dry run
Getting input files into tmp dir /tmp/vchakrav/tmp08qkua4w
Copying and preparing files for local execution in /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250410_112754/local
go to that directory IN A CLEAN SHELL and use  'sh run_job.sh NUMJOB' to execute the job
Execute rest run in local sub-directory of ./crab_20250410_112754
Executing test, please wait...
ERROR: FileNotFoundError: [Errno 2] No such file or directory: 'JobArgs-1.json'

	Please email cmstalk+computing-tools@dovecotmta.cern.ch for support with the crab.log file or crab.log URL.
	Client Version: v3.250318
	Please use 'crab uploadlog' to upload the log file /afs/cern.ch/user/v/vchakrav/crab/CMSSW_13_0_2/myfirstcrabtask/crab_20250410_112754/crab.log to the CRAB cache.
```

## Comment (cmsdmwmbot, 2025-04-10T10:52:51Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2428/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-04-10T11:01:11Z)

Ok to merge?

## Comment (belforte, 2025-04-10T11:08:29Z)

OK, but `outputs` in Line 54 will always be None.

## Comment (aspiringmind-code, 2025-04-10T11:11:46Z)

Thanks!
