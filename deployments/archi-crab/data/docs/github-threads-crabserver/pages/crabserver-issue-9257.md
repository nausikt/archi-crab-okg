# dmwm/CRABServer issue #9257: HTCondor v2, refreshGSIProxy proxy renewal fails in delegation mode.

State: closed
Opened: 2026-01-14T19:23:43Z
Closed: 2026-07-13T13:12:57Z
Labels: Status: In Progress, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/9257

## Opening post (nausikt, 2026-01-14T19:23:43Z)

See also [[HTCondor-users] refreshGSIProxy stopped working](https://www-auth.cs.wisc.edu/lists/htcondor-users/2026-January/msg00023.shtml), the original discussion between Stefano and Jaime Frey.

## Summary
The problem is we migrated AP's from 24.7 to 25.0.3, to [fix submission failures happened](https://github.com/dmwm/CRABServer/issues/9245) in the old version after a reboot of the AP moved it to use more recent OpenSSL.

However, we didn't tested and unaware of ***renewRemoteProxies*** had been failing [1] for over a month during the Christmas break. (*Luckily, most of our users ran tasks that completed within 7-day proxy validity period.*)

[1] Our ***renewRemoteProxies*** encounters silent failures when call python binding fn, [*refreshGSIProxy*](https://github.com/dmwm/CRABServer/blob/0ac5f0097f4d11af2a97caadeb886bf9f6118ec6/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py#L136) (which quite buggy [2]), to call the underlying cpp ([_schedd_refresh_gsi_proxy](https://github.com/htcondor/htcondor/blob/main/src/python-bindings/htcondor2/schedd.cpp#L1543-L1582)) to send actual renewal command to Schedd (AP's) in **delegation** (default) mode where unfortunately is likely to have bugs as Jaime mentioned.

[2] [*refreshGSIProxy*](https://github.com/htcondor/htcondor/blob/2aa6c96a42465f469005de64e8dc7e59c765f603/bindings/python/htcondor2/_schedd.py#L914-L926) HTCondor v2 python binding also contain bugs (*e.g. missing of *self* as first positional arg in fn signature, typos proxy should be proc.*) waiting to be resolved by HTCondor Developers.

## Our workaround
*until the upcoming HTCondor 25.x patches are thoroughly tested*

On **TW** (especially in *canary*) 
1. We will remain with HTC 24.7 python binding, v1 interface, since it is guaranteed to work with newer HTC 25.X on APs.
2. We steer away from delegation mode by setting `DELEGATE_JOB_GSI_CREDENTIALS=False` in `/etc/condor/condor_config` . This will do a regular file copy of the proxy (encrypted) when sending to the AP, instead of a delegation as Jamie suggested. #9256

## Comment (belforte, 2026-02-02T13:00:02Z)

This can be closed IMHO. The workaround works and the "clean" solution will come once we build TW in Alma9 using recent OpenSSL and HTCondor

## Comment (belforte, 2026-04-07T14:22:21Z)

Now that we have an Alma9 build, time to get back to this and remove the workaround added in https://github.com/dmwm/CRABServer/pull/9256

## Comment (belforte, 2026-04-07T14:31:23Z)

@nausikt I am doing it

## Comment (belforte, 2026-04-07T16:10:15Z)

hmm... after I removed   `DELEGATE_JOB_GSI_CREDENTIALS=False`  from `/etc/condor/condor_config` in the AP
delegation still fails, and I get this in SchedLog on AP side
```
04/07/26 17:56:50 (cid:5457869) Command=DELEGATE_GSI_CRED_SCHEDD, peer=<137.138.159.63:33041>
04/07/26 17:56:50 (cid:5457869) AuthMethod=IDTOKENS, AuthId=(null), CondorId=crabtw@cms
04/07/26 17:56:50 ReliSock::get_x509_delegation_finish(): delegation failed to complete: Failed to open proxy file
04/07/26 17:56:50 Delegation error: C084A321237F0000:error:8000000D:system library:BIO_new_file:Permission denied:crypto/bio/bss_file.c:67:calling fopen(/etc/condor/condor_local/spool/8476/0/cluster10428476.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4, r)
C084A321237F0000:error:10080002:BIO routines:BIO_new_file:system lib:crypto/bio/bss_file.c:77:

04/07/26 17:56:50 updateGSICred(499): failed to read expiration time of updated proxy for job 10428476.0: unable to read proxy file
04/07/26 17:56:50 (cid:5457869) Refresh GSI cred for job 10428476.0 failed
```

Condor versions:
* TW (latest v3.260330 on Alma9): 25.0.8
* AP (vocms059 on Alma0): 25.0.2

The file in the error msg `/etc/condor/condor_local/spool/8476/0/cluster10428476.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4` exits and is readable by its onwer (`crabtw`). Why does the Schedd fail to open ? Could it be try to do this using a non-privileged account ?

But the TW authenticates via token and is matched to crabtw user, log says ` CondorId=crabtw@cms`  !

```
[crabtw@vocms059 log]$ ls -l /etc/condor/condor_local/spool/8476/0/cluster10428476.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4
-rw------- 1 crabtw zh 15245 Apr  1 12:04 /etc/condor/condor_local/spool/8476/0/cluster10428476.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4
[crabtw@vocms059 log]$ 
```

## Comment (belforte, 2026-04-07T16:32:39Z)

I will try after updating vocms059 to latest HTC 25.0.8, and then ask in condor support list. There is a relevant [bug fix](https://htcondor.readthedocs.io/en/latest/version-history/lts-versions-25-0.html#version-25-0-7) in 25.0.7, but on the TaskWorker side.

## Comment (belforte, 2026-04-07T16:49:45Z)

Indeed error did not change after updating vocms059
```
04/07/26 18:48:30 Remote entity presented valid token with payload {"iat":1642519166,"iss":"\"cmsgwms-global.cern.ch\"","jti":"01be75a9f9845eebe786f9a17d2461f7","sub":"crabtw@cms"}.
04/07/26 18:48:30 (cid:932) Command=DELEGATE_GSI_CRED_SCHEDD, peer=<137.138.159.63:33827>
04/07/26 18:48:30 (cid:932) AuthMethod=IDTOKENS, AuthId=(null), CondorId=crabtw@cms
04/07/26 18:48:30 ReliSock::get_x509_delegation_finish(): delegation failed to complete: Failed to open proxy file
04/07/26 18:48:30 Delegation error: C0241D0F5A7F0000:error:8000000D:system library:BIO_new_file:Permission denied:crypto/bio/bss_file.c:67:calling fopen(/etc/condor/condor_local/spool/8283/0/cluster10428283.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4, r)
C0241D0F5A7F0000:error:10080002:BIO routines:BIO_new_file:system lib:crypto/bio/bss_file.c:77:

04/07/26 18:48:30 updateGSICred(499): failed to read expiration time of updated proxy for job 10428283.0: unable to read proxy file
04/07/26 18:48:30 (cid:932) Refresh GSI cred for job 10428283.0 failed
^C
[root@vocms059 log]# condor_version
$CondorVersion: 25.0.8 2026-03-11 BuildID: 881761 PackageID: 25.0.8-1 GitSHA: 825683a2 $
$CondorPlatform: x86_64_AlmaLinux9 $
[root@vocms059 log]# 
```

## Comment (belforte, 2026-04-07T17:46:29Z)

Here's the thread on HTCondor support list
https://www-auth.cs.wisc.edu/lists/htcondor-users/2026-April/msg00005.shtml

## Comment (belforte, 2026-04-09T14:47:51Z)

I tried a couple of things, w/o success nor better understanding. We are stuck waiting for experts

https://www-auth.cs.wisc.edu/lists/htcondor-users/2026-April/msg00014.shtml

## Comment (belforte, 2026-04-09T17:02:51Z)

Condor experts acknowledged a [bug](https://opensciencegrid.atlassian.net/browse/HTCONDOR-3660)

Put this on hold until there's a release with the fix. No change to current TW until then.

## Comment (belforte, 2026-05-12T16:23:44Z)

But was fixed in HTCOndor 24.12.20. Not released yet (last is 24.12.19). Keep waiting

## Comment (belforte, 2026-05-15T08:23:10Z)

HTCondor [25.0.10](https://htcondor.readthedocs.io/en/25.0/version-history/lts-versions-25-0.html#version-25-0-10) is out and th refreshGSIProxy thing is the first one in the list of bug fixes.
Removing Hold.

## Comment (belforte, 2026-05-15T08:25:18Z)

We should update condor on a test AP and check.

## Comment (nausikt, 2026-05-15T09:14:45Z)

Roger that Stefano.

## Comment (belforte, 2026-05-15T09:26:59Z)

I can do once done with JobRouter

## Comment (nausikt, 2026-05-15T09:55:07Z)

vocms059 ready for test.

## Comment (belforte, 2026-05-15T12:59:08Z)

I removed this line from crab-dev-tw01
https://github.com/dmwm/CRABServer/blob/53ba4e7d7778d2776581e8f52f6f30644df942d9/cicd/crabtaskworker_pypi/condor_config#L4
restarted TW process and a test submission to 059 succeeded
But it also submits to vocms069 which is still running 25.0.3
Something is wrong

## Comment (belforte, 2026-05-15T13:06:28Z)

My bad. Submission was always OK. need to test a refresh... not now.

## Comment (belforte, 2026-05-18T13:34:19Z)

OK. it works
```text
05/18/26 15:32:53 Remote entity presented valid token with payload {"iat":1642519166,"iss":"\"cmsgwms-global.cern.ch\"","jti":"01be75a9f9845eebe786f9a17d2461f7","sub":"crabtw@cms"}.
05/18/26 15:32:53 (cid:629105) Command=DELEGATE_GSI_CRED_SCHEDD, peer=<137.138.159.63:40001>
05/18/26 15:32:53 (cid:629105) AuthMethod=IDTOKENS, AuthId=(null), CondorId=crabtw@cms
05/18/26 15:32:53 (cid:629105) Received proxy for job 10480491.0
05/18/26 15:32:53 (cid:629105) proxy path: /etc/condor/condor_local/spool/491/0/cluster10480491.proc0.subproc0/5267401399ee13b6837deacb824594bde73ab2b4
05/18/26 15:32:53 (cid:629105) proxy expiration: 1779197573
05/18/26 15:32:53 (cid:629105) proxy identity: /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1
05/18/26 15:32:53 (cid:629105) proxy subject: /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1/CN=1836853699/CN=674998665/CN=253624209/CN=168445796/CN=1975694979
05/18/26 15:32:53 (cid:629105) proxy email: cms.crab.integration1@cern.ch
05/18/26 15:32:53 (cid:629105) Refresh GSI cred for job 10480491.0 succeeded
```

to be compared with https://github.com/dmwm/CRABServer/issues/9257#issuecomment-4200750254

## Comment (belforte, 2026-05-20T13:38:20Z)

I have [reverted](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/459) the change to vocms059 to minimize differences from `qa` and `master` until we can reconcile changes to JobRouter table #9295

## Comment (belforte, 2026-05-20T13:40:41Z)

things to do:
- [x] update HTCondor on all AP's
- [x] remove https://github.com/dmwm/CRABServer/blob/53ba4e7d7778d2776581e8f52f6f30644df942d9/cicd/crabtaskworker_pypi/condor_config#L4
- [x] rebuild TW in a stable tag
- [x] verify one last time that proxy renewal works before deploy new tag in canary (we only renew proxies in canary)

## Comment (belforte, 2026-07-01T08:20:08Z)

@nausikt now that qa and master are sync'ed again in puppet, you can go ahead and update HTCondor version on all machines na. We need at least 25.0.10 but since 25.0.11 is out, you can go for that.

## Comment (nausikt, 2026-07-01T15:17:59Z)

Noted.

## Comment (nausikt, 2026-07-08T14:49:57Z)

@belforte Done in production. Schedd does robustly restart when binary changes.
```
07/08/26 16:22:39 /usr/sbin/condor_master was modified (1781106533 != 1761932000), restarting /usr/sbin/condor_master Gracefully.
```

## Comment (belforte, 2026-07-13T12:52:18Z)

@nausikt can we close this ? Did you check that latest tag is working ?

## Comment (nausikt, 2026-07-13T12:54:14Z)

No, didn't release to canary yet, let me doing it now.

## Comment (nausikt, 2026-07-13T13:12:57Z)

I saw successfully renewal been pushed to schedd + no Refresh GSI cred failed mesgs. (all w/o workaround, DELEGATE_JOB_GSI_CREDENTIALS flag in /etc/condor/condor_config)   
```
grep -nE -C 3   'Delegation error|Permission denied|updateGSICred|Refresh GSI cred|unable to read proxy file' twlog.txt
```

So, i considered this resolved.

## Comment (belforte, 2026-07-13T13:44:57Z)

I am not sure that errors from `RenewRemoteProxies` would show up in  `twlog.txt`
Anyhow the presence of log lines like this in the recurring action log is reassuring
```
2026-07-13 15:12:54,261:DEBUG:RenewRemoteProxies:Updated proxy pushed to schedd for task 260618_212745:srdas_crab_260618_PPRefPythiaPU_V0Skims
```
