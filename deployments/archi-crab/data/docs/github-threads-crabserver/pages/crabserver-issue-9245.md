# dmwm/CRABServer issue #9245: TW fails to submit to vocms0137

State: closed
Opened: 2025-12-09T16:56:35Z
Closed: 2025-12-18T14:03:14Z
Labels: Priority: Critical, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9245

## Opening post (belforte, 2025-12-09T16:56:35Z)

all of a sudden submissions to vocms0137 always fail.
All other schedd's work.
Restarting and even rebooting vocms0137 did not help.

Here's logs

* TW side:
```
2025-12-09 17:52:57,993:ERROR:DagmanSubmitter,294:Failed to submit task to: crab3@vocms0137.cern.ch . Task: 251209_165102:belforte_crab_20251209_175054;
Submission failed with:
DCSchedd::spoolJobFiles:7002:File transfer failed for target job 136855724.0: TOOL at 137.138.159.63 failed to send file(s) to <188.185.51.8:4080>: |Error: sending file /data/certs/creds/c6ea75e904ebb26531217d954bd562c96db20c11; SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/5724/0/cluster136855724.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11
```

* Schedd side (/var/log/condor/ScheddLog)
```
12/09/25 17:52:57 (pid:1014112) Not entering transfer queue because sandbox (1750380) is too small (<= 104857600).
12/09/25 17:52:57 (pid:1014112) ReliSock::get_x509_delegation(): delegation failed: X509Credential::Request() failed
12/09/25 17:52:57 (pid:1014112) DoDownload: SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/5724/0/cluster136855724.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11
12/09/25 17:52:57 (pid:1014112) DoDownload: exiting at 3355
12/09/25 17:52:57 (pid:1014112) (cid:187944) generalJobFilesWorkerThread(): failed to transfer files for job 136855724.0 
12/09/25 17:52:57 (pid:1014112) Scheduler::spoolJobFilesWorkerThread(void *arg, Stream* s) NAP TIME
12/09/25 17:52:58 (pid:4269) ERROR - Staging of job files failed!
```

## Comment (belforte, 2025-12-09T16:57:36Z)

FYI @nausikt

## Comment (belforte, 2025-12-09T17:07:21Z)

Try again with `SCHEDD_DEBUG = D_FULLDEBUG` in `/etc/condor/config.d/99_local_tweaks.config` and a `condor_restart`

* TW log
```
2025-12-09 18:01:39,089:ERROR:DagmanSubmitter,294:Failed to submit task to: crab3@vocms0137.cern.ch . Task: 251209_170036:belforte_crab_20251209_180034;
Submission failed with:
DCSchedd::spoolJobFiles:7002:File transfer failed for target job 136855743.0: TOOL at 137.138.159.63 failed to send file(s) to <188.185.51.8:4080>: |Error: sending file /data/certs/creds/c6ea75e904ebb26531217d954bd562c96db20c11; SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/5743/0/cluster136855743.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11
```


* SchedLog
```
12/09/25 18:01:39 generalJobFilesWorkerThread(): transfer files for job 136855743.0
12/09/25 18:01:39 entering FileTransfer::SimpleInit
12/09/25 18:01:39 entering FileTransfer::DownloadFiles
12/09/25 18:01:39 entering FileTransfer::Download
12/09/25 18:01:39 entering FileTransfer::DoDownload sync=0
12/09/25 18:01:39 FILETRANSFER: incoming file_command is 4
12/09/25 18:01:39 Not entering transfer queue because sandbox (1750415) is too small (<= 104857600).
12/09/25 18:01:39 Sending GoAhead for 137.138.159.63 to send /etc/condor/condor_local/spool/5743/0/cluster136855743.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11 and all further files.
12/09/25 18:01:39 Received GoAhead from peer to receive /etc/condor/condor_local/spool/5743/0/cluster136855743.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11 and all further files.
12/09/25 18:01:39 ReliSock::get_x509_delegation(): delegation failed: X509Credential::Request() failed
12/09/25 18:01:39 DoDownload: get_x509_delegation() returned -1
12/09/25 18:01:39 DoDownload: SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/5743/0/cluster136855743.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11
12/09/25 18:01:39 DoDownload: exiting at 3355
12/09/25 18:01:39 (cid:253) generalJobFilesWorkerThread(): failed to transfer files for job 136855743.0
12/09/25 18:01:39 Scheduler::spoolJobFilesWorkerThread(void *arg, Stream* s) NAP TIME
12/09/25 18:01:39 Added data to SelfDrainingQueue act_on_job_myself_queue, now has 1 element(s)
12/09/25 18:01:39 Registered timer for SelfDrainingQueue act_on_job_myself_queue, period: 0 (id: 49)
12/09/25 18:01:39 Expedited call to StartJobs()
12/09/25 18:01:39 -------- Begin starting jobs --------
12/09/25 18:01:39 -------- Done starting jobs --------
12/09/25 18:01:39 Inside SelfDrainingQueue::timerHandler() for act_on_job_myself_queue
12/09/25 18:01:39 abort_job_myself: 136855743.0 action:Remove log_hold:true
12/09/25 18:01:39 Cleared dirty attributes for job 136855743.0
```

## Comment (belforte, 2025-12-09T17:11:25Z)

The only hint is `:get_x509_delegation(): delegation failed: X509Credential::Request() failed`

But it is not the "OpenSSL" problem typical in these days because:
1)  things work with the other identically configured AP's
2) TW is using old `OpenSSL 1.1.1n  15 Mar 2022 (Library: OpenSSL 1.1.1w  11 Sep 2023)`

I am out of ideas.

## Comment (belforte, 2025-12-10T11:09:11Z)

First time the error happened:
```
12/04/25 02:29:47 (pid:2385742) ReliSock::get_x509_delegation(): delegation failed: X509Credential::Request() failed
12/04/25 02:29:47 (pid:2385742) DoDownload: SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/9595/0/cluster136599595.proc0.subproc0.tmp/db85de4154ab6954b8b313bee9b26408357e57f4
12/04/25 02:29:47 (pid:2385742) DoDownload: exiting at 3355
12/04/25 02:29:47 (pid:2385742) (cid:880882) generalJobFilesWorkerThread(): failed to transfer files for job 136599595.0 
```
in `/var/log/condor/SchedLog.20251204T041331`

## Comment (belforte, 2025-12-10T13:44:13Z)

something very strange, duplicated directory entries !
```
belforte@vocms0137/condor> ls -l  /etc/condor/condor_local/spool/5743/0
total 32
drwxr-xr-x 10 crabtw zh 20480 Dec  3 05:20 cluster135965743.proc0.subproc0/
drwxr-xr-x  2 crabtw zh  4096 Nov 25 18:11 cluster135965743.proc0.subproc0.tmp/
drwxr-xr-x  2 crabtw zh  4096 Dec  9 18:01 cluster136855743.proc0.subproc0/
drwxr-xr-x  2 crabtw zh  4096 Dec  9 18:01 cluster136855743.proc0.subproc0.tmp/
belforte@vocms0137/condor> 
```

## Comment (belforte, 2025-12-10T16:04:38Z)

I have updated vocms0137 to HTC 25.0.3 (latest LTS), but error persists
```
12/10/25 15:16:46 Not entering transfer queue because sandbox (1750422) is too small (<= 104857600).
12/10/25 15:16:46 Sending GoAhead for 137.138.159.63 to send /etc/condor/condor_local/spool/5792/0/cluster136855792.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11 and all further files.
12/10/25 15:16:46 Received GoAhead from peer to receive /etc/condor/condor_local/spool/5792/0/cluster136855792.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11 and all further files.
12/10/25 15:16:46 ReliSock::get_x509_delegation(): delegation failed: X509Credential::Request() failed
12/10/25 15:16:46 DoDownload: get_x509_delegation() returned -1
12/10/25 15:16:46 DoDownload: SCHEDD at 188.185.51.8 - |Error: receiving file /etc/condor/condor_local/spool/5792/0/cluster136855792.proc0.subproc0.tmp/c6ea75e904ebb26531217d954bd562c96db20c11
12/10/25 15:16:46 DoDownload: exiting at 3355
12/10/25 15:16:46 (cid:49369) generalJobFilesWorkerThread(): failed to transfer files for job 136855792.0 
```
and again the odd double entries in the spool directory, with a mysterious date from Dec 4 
```
[root@vocms0137 log]# ls -l /etc/condor/condor_local/spool/5792/0/
total 16
drwxr-xr-x 2 crabtw zh 4096 Dec  4 23:58 cluster136655792.proc0.subproc0
drwxr-xr-x 2 crabtw zh 4096 Dec  4 23:58 cluster136655792.proc0.subproc0.tmp
drwxr-xr-x 2 crabtw zh 4096 Dec 10 15:16 cluster136855792.proc0.subproc0
drwxr-xr-x 2 crabtw zh 4096 Dec 10 15:16 cluster136855792.proc0.subproc0.tmp
[root@vocms0137 log]# 
```
even if there's no trace of cluster `136855792` in ScheddLog before today:
```
[root@vocms0137 log]# grep -l 136855792 /var/log/condor/SchedLog*
/var/log/condor/SchedLog
[root@vocms0137 log]# 
```
FWIW those 4 directories are all empty.

## Comment (belforte, 2025-12-18T14:03:14Z)

solved by updating AP to HTC 25.0.3. The previous comment about error persisting after that was due to a mistake on my side.
