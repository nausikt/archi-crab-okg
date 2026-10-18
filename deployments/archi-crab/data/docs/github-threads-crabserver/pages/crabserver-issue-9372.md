# dmwm/CRABServer issue #9372: "fake" submission failed with : Could not get a proxy valid for at least 5-days from myproxy

State: closed
Opened: 2026-07-29T14:28:19Z
Closed: 2026-08-03T07:35:35Z
URL: https://github.com/dmwm/CRABServer/issues/9372

## Opening post (belforte, 2026-07-29T14:28:19Z)

CICD submission of one task failed
```console
 crab status --instance preprod --task 260728_173034:crabint1_crab_disableAutomaticOutputCollection
crab status requires a projdir. Since you passed a taskname, we will run crab remake
Remaking crab_disableAutomaticOutputCollection folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_disableAutomaticOutputCollection
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/crabint1/crab_disableAutomaticOutputCollection
Task name:			260728_173034:crabint1_crab_disableAutomaticOutputCollection
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-preprod-tw01
Status on the CRAB server:	SUBMITFAILED
Task URL to use for HELP:	https://cmsweb-testbed.cern.ch/crabserver/ui/task/260728_173034%3Acrabint1_crab_disableAutomaticOutputCollection
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=crabint1&var-task=260728_173034%3Acrabint1_crab_disableAutomaticOutputCollection&from=1785256234000&to=now
Failure message from server:	Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1.
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/crabint1/crab_disableAutomaticOutputCollection/crab.log
belforte@lxplus808/crabint1> 
```

I checked tw log for that task and in there every command returns with 0 and final lifetime is 7 days (Juy 28 to Aug 4), not <5 (would be July 28-29-30-31-1-2)

Something seems wrong and may be the reason why we keep seeing submissions failed with that error (occasionally)

```text
2026-07-28 19:46:16,275:ERROR:MyProxyLogon:Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1.
2026-07-28 19:46:16,275:ERROR:MyProxyLogon:Will try again in verbose mode
2026-07-28 19:46:16,275:ERROR:MyProxyLogon:===========PROXY ERROR START ==========================
2026-07-28 19:46:16,781:DEBUG:Proxy:Executing : 
 command : env -i sh -c 'env X509_USER_PROXY=/data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4 voms-proxy-info -fqan'
 output : 
 error: No VOMS attributes found!

 retcode : 1
2026-07-28 19:46:16,781:DEBUG:Proxy:Calculating hash of /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1 for credential name
2026-07-28 19:46:16,987:DEBUG:Proxy:Executing : 
 command : env -i sh -c 'unset X509_USER_CERT X509_USER_KEY && env X509_USER_CERT=/data/certs/robotcert.pem X509_USER_KEY=/data/certs/robotkey.pem myproxy-logon -d -n -s myproxy.cern.ch -o /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097 -l "fc8da30b0c45665baadb7dd2e2b252177bdff657" -t 168:00'
 output : A credential has been received for user fc8da30b0c45665baadb7dd2e2b252177bdff657 in /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097.

 error: 
 retcode : 0
2026-07-28 19:46:17,494:DEBUG:Proxy:Executing : 
 command : env -i sh -c 'voms-proxy-info -type -file /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097'
 output : RFC3820 compliant impersonation proxy

 error: 
 retcode : 0
2026-07-28 19:46:17,600:DEBUG:Proxy:Executing : 
 command : env -i sh -c 'grid-proxy-info -file /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097 -timeleft'
 output : 604799

 error: 
 retcode : 0
2026-07-28 19:46:17,601:DEBUG:Proxy:Requested voms validity: 167:49
2026-07-28 19:46:18,909:DEBUG:Proxy:Executing : 
 command : env -i sh -c 'env X509_USER_PROXY=/data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097 voms-proxy-init -noregen -voms cms:/cms -out /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097 -bits 2048 -valid 167:49 -rfc'
 output : Contacting voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /data/certs/creds/5267401399ee13b6837deacb824594bde73ab2b4.47097.

Your proxy is valid until Tue Aug 04 19:35:18 CEST 2026

 error: 
 retcode : 0
2026-07-28 19:46:18,909:ERROR:MyProxyLogon:===========PROXY ERROR END   ==========================
2026-07-28 19:46:18,910:ERROR:MyProxyLogon:proxy retrieval from myproxy.cern.ch failed with DN hash as credential name.
2026-07-28 19:46:18,910:DEBUG:Handler:Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/MyProxyLogon.py", line 84, in execute
    (userproxy, usergroups) = self.tryProxyLogon(proxycfg=proxycfg)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/MyProxyLogon.py", line 58, in tryProxyLogon
    raise TaskWorkerException(errmsg)
TaskWorker.WorkerExceptions.TaskWorkerException: Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 97, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/MyProxyLogon.py", line 88, in execute
    raise TaskWorkerException(str(ex)) from ex
TaskWorker.WorkerExceptions.TaskWorkerException: Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1.

2026-07-28 19:46:18,916:INFO:Worker:Uploading failure message to the REST:
```

## Comment (belforte, 2026-07-29T14:58:13Z)

maybe when "retry in verbose mode" succeeds the proxy is still not considered valid ?

## Comment (belforte, 2026-08-02T16:06:32Z)

Indeed current code raises exception after calling `proxy.logonRenewMyProxy()` in verbose mode, likely under the assumption that failure was reproducible. But it may be that doing the 2n time works !
