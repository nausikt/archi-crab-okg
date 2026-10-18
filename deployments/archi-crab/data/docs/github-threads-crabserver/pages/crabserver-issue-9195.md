# dmwm/CRABServer issue #9195: stageout now fails when using tokens

State: closed
Opened: 2025-09-30T18:37:55Z
Closed: 2025-10-02T07:03:24Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9195

## Opening post (belforte, 2025-09-30T18:37:55Z)

something must have changed somewhere...
from e.g. https://cmsweb.cern.ch/scheddmon/crab-sched-901/belforte/250930_143930:belforte_crab_20250930_163928/job_out.1.0.txt
which was using TW from v3.250929
```text
Execution site: T2_DE_DESY
[...]
======== TOKEN SETUP START at Tue Sep 30 14:43:41 GMT 2025 ========
the file /srv/.condor_creds/cms_crab.use exists
the file /srv/.condor_creds/cms_crab.use is non-empty. TOKEN INFORMATION:
{
  "kid": "rsa2",
  "alg": "RS256"
}
{
  "wlcg.ver": "1.0",
  "sub": "58ba8516-2e94-4888-bce5-0187f7b4ebb9",
  "aud": "https://wlcg.cern.ch/jwt/v1/any",
  "nbf": "Tue Sep 30 06:50:44 CEST 2025",
  "scope": "condor:/WRITE openid storage.create:/store/temp/user offline_access profile storage.read:/ storage.modify:/store/temp/user email wlcg",
  "iss": "https://cms-auth.cern.ch/",
  "exp": "Sat Oct 4 18:50:44 CEST 2025",
  "iat": "Tue Sep 30 06:50:44 CEST 2025",
  "jti": "88b9aab7-8c47-4638-ad74-a5fc2a38c384",
  "client_id": "48620efa-e001-4c1d-84fc-4640d9498a11"
}
 Shall we use it as BEARER_TOKEN_FILE ?
CMSSW_13_3_0 is OK.
 T2_DE_DESY is token-ready.
Define BEARER_TOKEN_FILE and unset X509_USER_PROXY
======== TOKEN SETUP FINISH at Tue Sep 30 14:43:41 GMT 2025 ========
[...]
== ENV: BEARER_TOKEN_FILE=/srv/.condor_creds/cms_crab.use
```
**BUT** later on
```text

INFO:root:Command exited with status: 13
Output message: stdout: Tue Sep 30 17:02:50 CEST 2025
WARNING Could not load the user credentials: impossible to open :  : error:02001002:system library:fopen:No such file or directory
WARNING Could not load the user credentials: impossible to open :  : error:02001002:system library:fopen:No such file or directory
WARNING (SEToken) Could not retrieve any token for davs://dcache-cms-webdav.desy.de:2880/pnfs/desy.de/cms/tier2/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_143930/0000/kk_1.root
WARNING Could not load the user credentials: impossible to open :  : error:02001002:system library:fopen:No such file or directory
WARNING Could not load the user credentials: impossible to open :  : error:02001002:system library:fopen:No such file or directory
[...]

Debugging information on failing gfal-copy command

Current date and time: 2025-09-30 17:06:00
gfal-copy command which failed: env -i X509_USER_PROXY= JOBSTARTDIR= bash -c '. /startup_environment.sh; date; gfal-copy -t 2400 -T 2400 -p -v --abort-on-failure -K adler32  file:///srv/kk.root davs://dcache-cms-webdav.desy.de:2880/pnfs/desy.de/cms/tier2/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_143930/0000/kk_1.root'
Hostname:   batch1524.desy.de
OS:  Linux 5.14.0-570.44.1.el9_6.x86_64
[...]

Information for credentials in the environment
Bearer token content: 
Bearer token file: /srv/.condor_creds/cms_crab.use
httokendecode path: 
httokendecode: 

VOMS proxy info:
```

seems like  `/srv/.condor_creds/cms_crab.use` was removed ?????

same for jobs which ran e.g. at Vanderbilt https://cmsweb.cern.ch/scheddmon/crab-sched-901/belforte/250930_143930:belforte_crab_20250930_163928/job_out.5.1.txt 
I.e. not a site or dCache issue.

This used to work.

## Comment (belforte, 2025-09-30T18:39:10Z)

I think the only way forward is to keep X509 as backup and leave proper commissioning to SiteSupport

## Comment (belforte, 2025-09-30T19:08:40Z)

I modified TW in crab-dev-tw01 to not unser X509_USER_PROXY and now stageout worked using token
https://cmsweb.cern.ch/scheddmon/crab-sched-901/belforte/250930_184020:belforte_crab_20250930_204017/job_out.1.0.txt
```text

INFO:root:==>Working on file: /store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_184020/0000/kk_1.root
INFO:root:===> Attempting 2 Stage Outs
INFO:root:LFN to PFN match made:
LFN: /store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_184020/0000/kk_1.root
PFN: davs://cmsxrootd.hep.wisc.edu:1094/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_184020/0000/kk_1.root

INFO:root:Creating output directory...
INFO:root:Running the stage out with the available auth method (attempt 1)...
INFO:root:Command to run: #!/bin/bash
env -i BEARER_TOKEN_FILE=$BEARER_TOKEN_FILE BEARER_TOKEN=$(cat ${BEARER_TOKEN_FILE:-/dev/null}) JOBSTARTDIR=$JOBSTARTDIR bash -c '. $JOBSTARTDIR/startup_environment.sh;  date;  gfal-copy -t 2400 -T 2400 -p -v --abort-on-failure -K adler32  file:///srv/kk.root davs://cmsxrootd.hep.wisc.edu:1094/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_184020/0000/kk_1.root'
        EXIT_STATUS=$?
        echo "gfal-copy exit status: $EXIT_STATUS"
        if [[ $EXIT_STATUS != 0 ]]; then
            echo "ERROR: gfal-copy exited with $EXIT_STATUS"
            echo "Cleaning up failed file:"
            env -i BEARER_TOKEN_FILE=$BEARER_TOKEN_FILE BEARER_TOKEN=$(cat ${BEARER_TOKEN_FILE:-/dev/null}) JOBSTARTDIR=$JOBSTARTDIR bash -c '. $JOBSTARTDIR/startup_environment.sh;  date;  gfal-rm -t 600 davs://cmsxrootd.hep.wisc.edu:1094/store/temp/user/belforte.4bba3c2d14d54a938291c268ff4eba8b575b197f/GenericTTbar/Stefano-Test-250625/250930_184020/0000/kk_1.root'
        fi
        exit $EXIT_STATUS
        
INFO:root:Command exited with status: 0
Output message: stdout: Tue Sep 30 13:58:14 CDT 2025
```

What is going on ??????

## Comment (belforte, 2025-10-01T08:58:07Z)

I restarted TW container and submitted a new task
https://cmsweb-test2.cern.ch/crabserver/ui/task/250930_202056%3Abelforte_crab_20250930_222054
Thing worked this time.
Somehing with HTC token push to jobs ?

## Comment (belforte, 2025-10-01T09:45:40Z)

In CRAB meeting we agreed to keep the X509_USER_PROXY as fallback.
I will also add another call to httokendecode before calling cmscp, in case the problem si really that token gets deleted while the job was running.
