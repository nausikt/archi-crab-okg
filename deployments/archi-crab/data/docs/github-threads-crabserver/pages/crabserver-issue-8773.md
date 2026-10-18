# dmwm/CRABServer issue #8773: declare suspicious file replicas to Rucio in RetryJob

State: open
Opened: 2024-11-07T12:25:51Z
Labels: Type: Enhancement, Type: Support, Status: In Progress, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/8773

## Opening post (belforte, 2024-11-07T12:25:51Z)

see https://its.cern.ch/jira/browse/CMSTRANSF-1024

should modify https://github.com/dmwm/CRABServer/blob/97f447747265684589ac1f5be773eed80de02239/src/python/TaskWorker/Actions/RetryJob.py#L407
so that suspicious file replicas are reported to Rucio

## Comment (belforte, 2024-11-11T09:52:23Z)

Need also to prepare  a knowledge base with strings to look-for/avoid in log, like
```
A list is accessing an object (0x154e2060ea40) already deleted (list name = TList)
```
which is not a corrupted file !

see https://github.com/cms-sw/cmssw/issues/46634

## Comment (belforte, 2024-11-18T15:43:22Z)

as a start, skip HammerCloud and limit to max 30 reports per task

## Comment (belforte, 2025-03-06T13:12:04Z)

I am not sure that we really want to do this. We seem not to have any good handle atm. See https://its.cern.ch/jira/browse/CMSTRANSF-1024?focusedId=6703745&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6703745

## Comment (belforte, 2025-07-10T09:01:26Z)

recap of current situation:
* RetryJob detects suspicious files [1] and writes in`/eos/cms/store/temp/user/BadInputFiles/`[2] 
* a crontab in Stefano's account on lxplus reads from there and writes in `/eos/project/c/cmsweb/www/CRAB/` [3], [4]

[1]
https://github.com/dmwm/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/src/python/TaskWorker/Actions/RetryJob.py#L411

[2]
https://github.com/dmwm/CRABServer/blob/646fbd7bcada83b0624ed05c16055340b4973f1e/src/python/TaskWorker/Actions/RetryJob.py#L483

[3]
```console

belforte@lxplus810/~> acrontab -l|grep -v '#'
30 02 * * * lxplus8.cern.ch /afs/cern.ch/user/b/belforte/utils/list-bad-input-files.sh
belforte@lxplus810/~> 
belforte@lxplus810/~> cat /afs/cern.ch/user/b/belforte/utils/list-bad-input-files.sh
#!/bin/bash
mkdir -p /tmp/belforte
cd /tmp/belforte

rm -rf ProcessBadFilesList.py

wget -q https://github.com/dmwm/CRABServer/raw/master/scripts/Utils/ProcessBadFilesList.py

python3 ProcessBadFilesList.py > PBF.log 2>&1
rc=$?

if ! [ $rc == "0" ] ; then
    echo "ProcessBadFilesListfailed: here's log"
    cat PBF.log
else
    cp BadInputFiles.html  /eos/project/c/cmsweb/www/CRAB/BadInputFiles.html
    cp TruncatedFiles.list /eos/project/c/cmsweb/www/CRAB/TruncatedFiles.list
    cp NotRootFiles.list /eos/project/c/cmsweb/www/CRAB/NotRootFiles.list
    cp SuspiciousFiles.list /eos/project/c/cmsweb/www/CRAB/SuspiciousFiles.list
fi
belforte@lxplus810/~> 
```

[4] https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/ProcessBadFilesList.py

## Comment (belforte, 2025-08-04T13:19:01Z)

current procedure and proposed improvement now documented in https://github.com/dmwm/CRABServer/wiki/reporting-corrupted-files  

How to proceed is not obvious, need handshake with Rucio/DM side: https://its.cern.ch/jira/browse/CMSTRANSF-1024?focusedId=7056974&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-7056974

## Comment (belforte, 2025-08-18T19:41:44Z)

need to increase reporting for truncated files #9154
