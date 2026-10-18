# dmwm/CRABServer issue #7883: collect file corruption report from jobs and act on the info

State: closed
Opened: 2023-09-18T13:49:52Z
Closed: 2023-11-17T16:07:13Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7883

## Opening post (belforte, 2023-09-18T13:49:52Z)

after #7867 CRAB PostJob will create one line on CERN EOS everytime a corrupted file is found.
As indicated in https://github.com/dmwm/CRABServer/issues/7548#issuecomment-1714567989 we need a script to run periodically to create daily (?) tallies, and possibly report to Rucio.

Breakdown:
- [x] have a parsers + summary-make script
- [x] deploy in production
- [x] collect some experience
- [x] decide how to integrate calls to Rucio (mark suspicious ? mark bad ? need privileged account ?
- [x] finalize the script and make it run automatically e.g. in TW

## Comment (belforte, 2023-09-18T21:28:12Z)

Waiting to get experience before deciding if/how to progress

## Comment (belforte, 2023-10-03T16:18:29Z)

keep this open

## Comment (belforte, 2023-10-09T19:43:45Z)

the version "which reports" is now deployed in production with v3.231006 I will enable reporting by
```
sudo touch /etc/use_corruption_check
```
on all schedulers.
This way we can quickly roll back if the change to PostJob result in some problems.

## Comment (belforte, 2023-10-13T23:04:18Z)

Chek enabled on Oct 9. Stil no corruption reported. DId I do something wrong ?

## Comment (belforte, 2023-10-17T21:22:19Z)

first "non from me" event !
An HammerCloud job reported a suspicious file
```
belforte@lxplus810/BadInputFiles> cat suspicious/new/231017_080559:sciaba_crab_HC-208-T2_AT_Vienna-105008-20231017100501.job.76.0.json|jq
{
  "DID": "cms:/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/E238F708-2176-E711-B5DF-FA163EAD7847.root",
  "RSE": "T2_AT_Vienna",
  "exitCode": 8021,
  "message": [
    "== CMSSW:       [a] Fatal Root Error: @SUB=TBasket::Streamer",
    "== CMSSW: The value of fNbytes is incorrect (-322747004) ; trying to recover by setting it to zero",
    "NOT CLEARLY CORRUPTED, OTHER ROOT ERROR ?",
    "DID Identification may not be corrrect",
    "stdout: https://cmsweb.cern.ch:8443/scheddmon/0144/sciaba/231017_080559:sciaba_crab_HC-208-T2_AT_Vienna-105008-20231017100501/job_out.76.0.txt",
    "postjob: https://cmsweb.cern.ch:8443/scheddmon/0144/sciaba/231017_080559:sciaba_crab_HC-208-T2_AT_Vienna-105008-20231017100501/postjob.76.0.txt"
  ]
}
belforte@lxplus810/BadInputFiles> 

```

But after `rucio get --rses T2_AT_Vienna cms:/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/E238F708-2176-E711-B5DF-FA163EAD7847.root` the file appears OK and indeed CRAB resubmitted that jobs
and `76.1` completed OK

This proves that tools is working and that so far it looks good to have SUSPICIOUS as separated from CORRUPTED.

## Comment (belforte, 2023-10-20T10:22:29Z)

today another bunch of fatal errors from HammerCloud, of the kind, all at T2_US_MIT
```
== CMSSW: ----- Begin Fatal Exception 18-Oct-2023 14:40:04 EDT-----------------------
== CMSSW: An exception of category 'FileReadError' occurred while
== CMSSW:    [0] Rethrowing an exception that happened on a different thread.
== CMSSW:    [1] Reading branch HcalNoiseSummary_hcalnoise__RECO.
== CMSSW:    Additional Info:
== CMSSW:       [a] Fatal Root Error: @SUB=TBranchElement::GetBasket
== CMSSW: File: ///mnt/hadoop/cms/store/mc/HC/GenericTTbar/AODSIM/CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/00000/0A11E55B-0876-E711-9647-FA163EB8F562.root at byte:153972288, branch:HcalNoiseSummary_hcalnoise__RECO.present, entry:1485, badread=1, nerrors=1, basketnumber=9
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```

All of them went away in following, automatic, job resubmissions.
Only [one job](https://cmsweb.cern.ch:8443/scheddmon/0155/sciaba/231018_120358:sciaba_crab_HC-205-T2_US_MIT-105024-20231018140301/job_out.56.2.txt)  kept failing 3 times, but direct inspection (rucio get plus gfal-sum) adler32 checksum is fine.

We already knew that MIT is not top-of-the-class as robustness, but other than that... have not learn anything yet.

## Comment (belforte, 2023-10-31T14:22:39Z)

Still the only corruption reports are the read errors at MIT `badread=1, nerrors=1, basketnumber=...` also one case with `badread=0, nerrors=1..`
and the only suspicion are again at MIT with the very cryptic
```
    "== CMSSW:       [a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers",
    "== CMSSW: fNbytes = 581760, fKeylen = 119, fObjlen = 600644, noutot = 0, nout=0, nin=581641, nbuf=600644",
```

I will
- [ ] change the "detection" code to move the former from `corrupted` to `suspicious`.
- [ ] review the conditions under which I now set exit code to 8022

## Comment (belforte, 2023-11-07T21:11:15Z)

More than a month into this. Only recorded problems are form HammerCloud transient read errors (usually fixed in next automatic retry). All such errors have exit code 8021 (means file open is OK and there was a read error).
Plain corruption like truncated file onlly happened in my test and has exit code 8020 (error in open).

I think I have spent too much time on this already.
Will try to keep checking summaries once a month, but that's all.
I have added this to my acrontab
```
`# every week make a summary of CRAB corrupted file reports
30 05 */7 * * lxplus8.cern.ch /afs/cern.ch/user/b/belforte/utils/MakeCorruptedFileReportsSummary.sh
```
that script `MakeCorruptedFileReportsSummary.sh` is:
```bash
#!/bin/bash
mkdir -p /tmp/belforte
cd /tmp/belforte
rm -rf ProcessBadFilesList.py
wget -q https://github.com/dmwm/CRABServer/raw/master/scripts/Utils/ProcessBadFilesList.py
python3 ProcessBadFilesList.py > /dev/null
```

## Comment (belforte, 2023-11-13T09:46:09Z)

**DAMN** I was fooled by the fact that HC jobs could write reports, but directory tree `/eos/cms/temp/user/BadInputFiles` lacked the needed permission for users to write. I guess Sciaba identity has special privileges on EOS.
I had tested that user jobs could write initially, but forgot about the needed config. when moving to a better-named directory.

I have now done `chmod g+w -R` and `chmod o+w -R` and tested again with a user job.
Need to reset the "wait and see".

## Comment (belforte, 2023-11-13T11:14:40Z)

corrupted file reports are now coming in like rain... oh well.

## Comment (belforte, 2023-11-17T16:06:07Z)

I have now setup automatic daily reporting of bad input files, check of disk replicas size and Adler, and suggestion of which replica can be marked as BAD after making sure that there is a tape replica and handed this over to CMSRucio and CMS DM folks.
References:
https://its.cern.ch/jira/browse/CMSTRANSF-766
https://github.com/dmwm/CMSRucio/issues/403

Daily reports are available at links in https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&refresh=1h&from=1700063958182&to=1700236758182&viewPanel=116
