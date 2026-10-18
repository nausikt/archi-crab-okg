# dmwm/CRABServer issue #8509: automatic splitting fails in latest master after #8507

State: closed
Opened: 2024-06-18T16:11:23Z
Closed: 2024-06-18T22:00:48Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8509

## Opening post (belforte, 2024-06-18T16:11:23Z)

this task: https://cmsweb-test2.cern.ch/crabserver/ui/task/240618_133627%3Acmsbot_crab_20240618_153626
PreDag fails to start the processing DAG
https://cmsweb.cern.ch:8443/scheddmon/059/cmsbot/240618_133627:cmsbot_crab_20240618_153626/AutomaticSplitting/DagLog0.txt

relevant error line should be
```
ERROR: unable to read submit append file (subdag.ad)
```

## Comment (belforte, 2024-06-18T16:19:02Z)

this change had gone lost in merging of my modernize_HTC branch to master branch
```diff
@@ -333,7 +333,7 @@ class PreDAG():
         """ Submit a subdag
         """
         subprocess.check_call(['condor_submit_dag', '-DoRecov', '-AutoRescue', '0', '-MaxPre', '20', '-MaxIdle', str(maxidle),
-                               '-MaxPost', str(maxpost), '-insert_sub_file', 'subdag.ad',
+                               '-MaxPost', str(maxpost), '-insert_sub_file', 'subdag.jdl',
                                '-append', '+Environment = strcat(Environment," _CONDOR_DAGMAN_LOG={0}/{1}.dagman.out")'.format(os.getcwd(), subdag),
                                '-append', '+TaskType = "{0}"'.format(stage.upper()), subdag])
```

## Comment (belforte, 2024-06-18T21:18:15Z)

DAG submission is now OK. BUt the correct proxy is not passed to FTS_transfer script. The directory name is  inserted twice !
Things were OK for non-automatic splitting.
I must be missing some other change previously done in my development branch

```
2024-06-18 19:29:02,232: using user's proxy from /data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0//data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11
2024-06-18 19:29:02,232: error during main loop
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/task_process/FTS_Transfers.py", line 715, in <module>
    algorithm()
  File "/data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/task_process/FTS_Transfers.py", line 665, in algorithm
    ftsContext = fts3.Context(FTS_ENDPOINT, proxy, proxy, verify=True)
  File "/usr/lib/python3.9/site-packages/fts3/rest/client/context.py", line 182, in __init__
    self._set_x509(ucert, ukey)
  File "/usr/lib/python3.9/site-packages/fts3/rest/client/context.py", line 95, in _set_x509
    raise FileNotFoundError(name + " not found!")
FileNotFoundError: Certificate not found!
```

## Comment (belforte, 2024-06-18T21:23:32Z)

indeed 
```text
[crabtw@vocms059 task_process]$ cat RestInfoForFileTransfers.json |jq
{
  "host": "cmsweb-test2.cern.ch:8443",
  "dbInstance": "dev",
  "proxyfile": "/data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11"
}
[crabtw@vocms059 task_process]$ 
```
But code expect a file name w/o the path
https://github.com/dmwm/CRABServer/blob/3f893cf77152dc1bf9ad309bc1cad2411def88e7/scripts/task_process/FTS_Transfers.py#L73-L75

## Comment (belforte, 2024-06-18T21:56:44Z)

and here's what I am missing.  I do not understand how is it possible that other tests in #8508 were successful [1]

```diff
LapSB:CRABServer$ git diff modernize_HTC -- src/python/TaskWorker/Actions/PostJob.py
diff --git a/src/python/TaskWorker/Actions/PostJob.py b/src/python/TaskWorker/Actions/PostJob.py
index 5cc59b96..17c235ed 100644
--- a/src/python/TaskWorker/Actions/PostJob.py
+++ b/src/python/TaskWorker/Actions/PostJob.py
@@ -995,7 +995,7 @@ class ASOServerJob():
             #if not os.path.exists('task_process/rest_filetransfers.txt'):
                 restInfo = {'host':self.rest_host,
                             'dbInstance': self.db_instance,
-                            'proxyfile': os.path.basename(self.proxy)}
+                            'proxyfile': self.proxy}
                 with open('task_process/RestInfoForFileTransfers.json', 'w') as fp:
                     json.dump(restInfo, fp)
         else:
@@ -1014,7 +1014,7 @@ class ASOServerJob():
             #if not os.path.exists('task_process/rest_filetransfers.txt'):
                 restInfo = {'host':self.rest_host,
                             'dbInstance': self.db_instance,
-                            'proxyfile': os.path.basename(self.proxy)}
+                            'proxyfile': self.proxy}
                 with open('task_process/RestInfoForFileTransfers.json','w') as fp:
                     json.dump(restInfo, fp)
         return returnMsg
LapSB:CRABServer$ 
```

[1] I looked at one of those `240618_133632:cmsbot_crab_20240618_153631` and 
```text
[crabtw@vocms059 SPOOL_DIR]$ cat task_process/RestInfoForFileTransfers.json |jq
{
  "host": "cmsweb-test2.cern.ch:8443",
  "dbInstance": "dev",
  "proxyfile": "e080907cad69528d423bbe562e2f8f9873b2c933"
}
[crabtw@vocms059 SPOOL_DIR]$ 
```
but PostJob cose was missing the `os.path.basename`. I guess that normal jobs use proxy file name from the env. of `dag_bootstrap.sh`
```text
[crabtw@vocms059 SPOOL_DIR]$ grep  X509 dag_bootstrap.out
X509_USER_PROXY=e080907cad69528d423bbe562e2f8f9873b2c933
[crabtw@vocms059 SPOOL_DIR]$ 
```
while in case of automatic splitting I find
```text
[crabtw@vocms059 SPOOL_DIR]$ grep  X509 dag_bootstrap.out 
X509_USER_PROXY=/data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11
[crabtw@vocms059 SPOOL_DIR]$ 
```

I **think** that somehow PreDag takes the proxy from the ads of completed probe jobs
```text
finished_jobs/job.0-1.0:x509userproxy = "/data/srv/glidecondor/condor_local/spool/6222/0/cluster9636222.proc0.subproc0/c6ea75e904ebb26531217d954bd562c96db20c11"

```
But this is quite intricated. And of course the solution which I already found of removing any possible path in PostJob before writing it out in the file to pass to FTS_Transfer (or Rucio_Transfer) is just fine.
