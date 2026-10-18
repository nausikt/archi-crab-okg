# dmwm/CRABServer issue #7548: Parse cmsRun stdout/err to detect corrupted root files

State: closed
Opened: 2023-02-22T13:19:34Z
Closed: 2023-09-18T13:34:23Z
Labels: Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7548

## Opening post (belforte, 2023-02-22T13:19:34Z)

There are cases where cmsRun fails w/o creating a FJR with details, e.g. segmentation faults or corrupted input files. In the latter case the details are in the xroot exception which is printed to stdout/err but CMSSW framework only sees a generic failure.
It is also possible for CMSSW to exit with an alas generic 8021 whiel stderr has things like
```
Fatal Exception (Exit code: 8021)
An exception of category 'FileReadError' occurred while
[0] Rethrowing an exception that happened on a different thread.
[1] Reading branch patJets_slimmedJetsPuppi__RECO.
Additional Info:
[a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers
fNbytes = 2154, fKeylen = 121, fObjlen = 20636, noutot = 0, nout=0, nin=2033, nbuf=20636 
```
or
```
Fatal Exception (Exit code: 8021)
An exception of category 'FileReadError' occurred while
[0] Calling InputSource::readFile_
[1] Reading branch EventAuxiliary
Additional Info:
[a] Fatal Root Error: @SUB=TStorageFactoryFile::ReadBuffersSync
Storage::readv returned different size result=263352 expected=323232
```
The telling string is `Fatal Root Error` which makes this different from "object such and such is not present in this data file".

We should add a step in the wrapper where cmsRun stdout/err is parsed whenever the application fails w/o a FJR and set a proper exit code ourselves. This part could be common with WMA (e.g. part of existing FJR parsing).

May need to define a new exit code for corrupted files.

## Comment (belforte, 2023-07-17T10:41:28Z)

another example (this job exited with 8021 btw) Not clear to me if msg is from xroot or cmssw and if we manage `no such device` as a possible file corruption. Given also that this error appears  transient https://cms-talk.web.cern.ch/t/corrupted-files-mit-please-help/2690

```

== CMSSW: ----- Begin Fatal Exception 17-Jul-2023 06:15:16 EDT-----------------------
== CMSSW: An exception of category 'FileReadError' occurred while
== CMSSW:    [0] Rethrowing an exception that happened on a different thread.
== CMSSW:    [1] Reading branch GlobalAlgBlkBXVector_gtStage2Digis__RECO.
== CMSSW:    [2] Calling XrdFile::readv()
== CMSSW:    [3] XrdAdaptor::ClientRequest::HandleResponse() failure while running connection recovery
== CMSSW:    [4] In XrdAdaptor::RequestManager::requestFailure()
== CMSSW: Exception Message:
== CMSSW: XrdAdaptor::RequestManager::requestFailure Open(name='root://bost-cms-xcache01.lhcone.es.net//store/data/Run2017F/SingleMuon/MINIAOD/15Feb2022_UL2017-v1/40000/4F29BEB1-F606-3B44-9E56-68FACA2D2993.root', flags=0x10, permissions=0660, old source=bost-cms-xcache01.lhcone.es.net:1094 (site ESNET-BOST-CMS-XCACHE), new source=bost-cms-xcache01.lhcone.es.net:1094 (site ESNET-BOST-CMS-XCACHE)) => Xrootd server returned an excluded source
== CMSSW:    Additional Info:
== CMSSW:       [a] Original error: '[ERROR] Server responded with an error: [3005] Unable to readv /store/data/Run2017F/SingleMuon/MINIAOD/15Feb2022_UL2017-v1/40000/4F29BEB1-F606-3B44-9E56-68FACA2D2993.root; no such device
== CMSSW: ' (errno=3005, code=400, source=bost-cms-xcache01.lhcone.es.net:1094 (site ESNET-BOST-CMS-XCACHE)).
== CMSSW:       [b] Disabled source: bost-cms-xcache01.lhcone.es.net:1094
== CMSSW:       [c] Active source: bost-cms-xcache01.lhcone.es.net:1094 (site ESNET-BOST-CMS-XCACHE)
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```

## Comment (belforte, 2023-09-04T09:50:46Z)

Since the cmsRun stdout is brought back to the scheduler, even when jobs are killed on WN thanks to latest changes by Daro in https://github.com/dmwm/CRABServer/issues/7529 , I think this is better addressed inside the PostJob. Makes debugging and updating much easier.

## Comment (belforte, 2023-09-04T16:49:57Z)

a more classic example of corrupted file (job completed with 8028)
```

== CMSSW: ----- Begin Fatal Exception 04-Sep-2023 05:19:02 EDT-----------------------
== CMSSW: An exception of category 'FallbackFileOpenError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing input source of type PoolSource
== CMSSW:    [2] Calling RootFileSequenceBase::initTheFile()
== CMSSW:    Additional Info:
== CMSSW:       [a] Fatal Root Error: @SUB=TStorageFactoryFile::Init
== CMSSW: file ///cmsuf/data/store/data/Run2018D/DoubleMuon/MINIAOD/UL2018_MiniAODv2_GT36-v1/2430001/163AB5F4-6B5D-4141-A210-01AF7E72D967.root is truncated at 1740636160 bytes: should be 2459112823, trying to recover
== CMSSW:
== CMSSW:       [b] Input file file:///cmsuf/data/store/data/Run2018D/DoubleMuon/MINIAOD/UL2018_MiniAODv2_GT36-v1/2430001/163AB5F4-6B5D-4141-A210-01AF7E72D967.root could not be opened.
== CMSSW: Fallback Input file root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/MINIAOD/UL2018_MiniAODv2_GT36-v1/2430001/163AB5F4-6B5D-4141-A210-01AF7E72D967.root also could not be opened.
== CMSSW: Original exception info is above; fallback exception info is below.
== CMSSW:       [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init
== CMSSW: file root://cmsxrootd.fnal.gov//store/data/Run2018D/DoubleMuon/MINIAOD/UL2018_MiniAODv2_GT36-v1/2430001/163AB5F4-6B5D-4141-A210-01AF7E72D967.root is truncated at 1740636160 bytes: should be 2459112823, trying to recover
== CMSSW:
```

## Comment (belforte, 2023-09-04T17:10:07Z)

so far I have 3 examples of bad file
https://github.com/dmwm/CRABServer/issues/7548#issue-1595093112 (2 examples)
https://github.com/dmwm/CRABServer/issues/7548#issuecomment-1705533008

all have  `Fatal Root Error:`

So I will start looking for that.
Need a way to "report w/o alerting Rucio, simply to monitor".

this seems to work, as user `crabtw` using the job (i.e. user) proxy
```
gfal-copy gWMS-CMSRunAnalysis.sh gsiftp://eoscmsftp.cern.ch/eos/cms/store/temp/user/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f/gWMS-CMSRunAnalysis.sh
```
I can also cleanup
```
belforte@lxplus800/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f> ls -l
total 14
drwxrwxrwx. 2 belforte zh  4096 Aug 17 22:39 belforte/
-rw-r--r--. 1 zhenggan zh 10066 Sep  4 19:26 gWMS-CMSRunAnalysis.sh
belforte@lxplus800/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f> rm gWMS-CMSRunAnalysis.sh 
belforte@lxplus800/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f> ls -l
total 4
drwxrwxrwx. 2 belforte zh 4096 Aug 17 22:39 belforte/
belforte@lxplus800/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f> 
```

## Comment (belforte, 2023-09-06T09:17:16Z)

this will be cleaner
```
gfal-copy gWMS-CMSRunAnalysis.sh gsiftp://eoscmsftp.cern.ch/eos/cms/store/temp/user/corruped/example.txt
```
i.e. I will put a one-line file in `/store/temp/user/corrupted` at CERN
for easier maintenance I created `/store/temp/user/corrupted` there with my proxy:
```
belforte@lxplus806/~> ls -ld /eos/cms/store/temp/user/corrupted/
drwxrwxr-x. 2 belforte zh 4096 Sep  6 11:15 /eos/cms/store/temp/user/corrupted//
belforte@lxplus806/~> 
```

files there will be automatically cleaned by EOS after 30 days.

## Comment (belforte, 2023-09-07T14:33:57Z)

more examples in https://cms-talk.web.cern.ch/t/corrupted-missing-parkingbph-miniaod-files/29281/1

they all fit the pattern
* completed with 8021 or 8028
* job stdout contains `[a] Fatal Root Error`

## Comment (belforte, 2023-09-08T15:36:32Z)

initial implementation in https://github.com/dmwm/CRABServer/pull/7867
as indicated in there

this PR includes code to write a JSON file in `/eos/cms/store/temp/user/corrupted/` which we can use to check that things are OK before calling `rucioClient.declare_suspicious_file_replicas()` 

```
belforte@lxplus806/~> ls /eos/cms/store/temp/user/corrupted/
230908_074255:belforte_crab_20230908_094238.job.5.1.json
230908_074255:belforte_crab_20230908_094238.job.5.2.json
230908_074255:belforte_crab_20230908_094238.job.5.3.json
belforte@lxplus806/~> cat /eos/cms/store/temp/user/corrupted/230908_074255:belforte_crab_20230908_094238.job.5.3.json|jq
{
  "DID": "cms:/store/data/Run2018C/ParkingBPH5/MINIAOD/05May2019-v1/70000/4A628618-FB8A-804C-A905-A046244B6DF3.root",
  "RSE": "T2_US_Wisconsin",
  "exitCode": 8020,
  "message": [
    "== CMSSW:       [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init\n",
    "== CMSSW: file root://cmsxrootd.fnal.gov//store/data/Run2018C/ParkingBPH5/MINIAOD/05May2019-v1/70000/4A628618-FB8A-804C-A905-A046244B6DF3.root is truncated at 2183135232 bytes: should be 4128873606, trying to recover\n"
  ]
}
belforte@lxplus806/~> 
```

for each of those files one can obtain the PFN to be flagged (cfr https://rucio.cern.ch/documentation/client_api/replicaclient#declare_suspicious_file_replicas ) from  CLI `rucio list-file-replicas <did> rses RSE --pfns`

## Comment (belforte, 2023-09-08T19:34:50Z)

my code currently fails on this
```
== CMSSW: 08-Sep-2023 15:19:23 EDT  Closed file root://cmsxrootd.fnal.gov//store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/500
04/45F5AB3C-34F0-5949-A7AA-1B21643731DA.root
== CMSSW: ----- Begin Fatal Exception 08-Sep-2023 15:19:23 EDT-----------------------
== CMSSW: An exception of category 'FileReadError' occurred while
== CMSSW:    [0] Calling InputSource::readFile_
== CMSSW:    [1] Reading branch EventAuxiliary
== CMSSW:    Additional Info:
== CMSSW:       [a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers
== CMSSW: fNbytes = 33333, fKeylen = 83, fObjlen = 184213, noutot = 0, nout=0, nin=33250, nbuf=184213
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
```
since the line after `Fatal Root Error:` does not contain the file name like in the examples above.
OTOH this is special case described as "the last one" in https://its.cern.ch/jira/browse/CMSTRANSF-707?focusedId=4932194&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-4932194 where there is no bad checksum and Rucio can not fix this.

So I guess I will start by skipping errors where the line after `Fatal Root Error:`  does not have the format
```
== CMSSW: file root://cmsxrootd.fnal.gov//store/data/Run2018C/ParkingBPH5/MINIAOD/05May2019-v1/70000/4A628618-FB8A-804C-A905-A046244B6DF3.root is truncated at 2183135232 bytes: should be 4128873606, trying to recover
```

Maybe we should build some kind of updatable heuristic based on regexps ??? Sounds a bit far-fetched !

## Comment (belforte, 2023-09-08T19:37:57Z)

I also need some protection in `try...except` format, because in that case `RetryJob` raised an `IndexError: list index out of range` and PostJob went along replacing 8021 with 0 as exit code and declaring the job successful !!
```
Fri, 08 Sep 2023 21:19:38 CEST(+0200):INFO:PostJob ======== Starting execution on vocms0121.cern.ch. Task Worker Version development
Fri, 08 Sep 2023 21:19:38 CEST(+0200):DEBUG:PostJob Creating symbolic link in task web directory to post-job log file: /home/grid/belforte/230908_191251:belforte_crab_20230908_211238/postjob.7.0.txt -> postjob.7.0.txt
Fri, 08 Sep 2023 21:19:38 CEST(+0200):DEBUG:PostJob Copying job stdout from job_out.7 to /home/grid/belforte/230908_191251:belforte_crab_20230908_211238/job_out.7.0.txt.
Fri, 08 Sep 2023 21:19:38 CEST(+0200):DEBUG:PostJob Copying job report from jobReport.json.7 to job_fjr.7.0.json.
Fri, 08 Sep 2023 21:19:38 CEST(+0200):DEBUG:PostJob Creating symbolic link in task web directory to job report file: /home/grid/belforte/230908_191251:belforte_crab_20230908_211238/job_fjr.7.0.json -> job_fjr.7.0.json
Fri, 08 Sep 2023 21:19:38 CEST(+0200):INFO:PostJob This is job retry number 0. The maximum allowed number of retries is 2.
Fri, 08 Sep 2023 21:19:38 CEST(+0200):DEBUG:PostJob This post-job corresponds to job with Condor ID 94962737.
Fri, 08 Sep 2023 21:19:38 CEST(+0200):INFO:PostJob PER_JOB_HISTORY file /data/srv/glidecondor/condor_local/job_history/history.94962737.0 not found , look in ./finished_jobs
Fri, 08 Sep 2023 21:19:38 CEST(+0200):INFO:PostJob History file not found in ./finished_jobs. Create it by querying schedd
Fri, 08 Sep 2023 21:19:38 CEST(+0200):INFO:PostJob Executing condor_q -l 94962737.0 > ./finished_jobs/job.7.0
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob History file ./finished_jobs/job.7.0 created
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to parse job ad file ./finished_jobs/job.7.0.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        -----> Attempt # 0 of 1 -----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        -----> Succeeded to parse job ad file -----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished to parse job ad.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to analyze job exit status.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:RetryJob Job or stageout wrapper finished with exit code 8021. Trying to determine the meaning of the exit code and if it is a recoverable or fatal error.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:RetryJob exit code 8021, look for corrupted file in /home/grid/belforte/230908_191251:belforte_crab_20230908_211238/job_out.7.0.txt
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:RetryJob Corrupted input file found
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:RetryJob == CMSSW:       [a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers

Fri, 08 Sep 2023 21:19:41 CEST(+0200):ERROR:RetryJob list index out of range
Traceback (most recent call last):
  File "/data/srv/glidecondor/condor_local/spool/2729/0/cluster94962729.proc0.subproc0/TaskWorker/Actions/RetryJob.py", line 534, in execute
    job_status = self.execute_internal(*args, **kw)
  File "/data/srv/glidecondor/condor_local/spool/2729/0/cluster94962729.proc0.subproc0/TaskWorker/Actions/RetryJob.py", line 490, in execute_internal
    check_exit_code_retval = self.check_exit_code()
  File "/data/srv/glidecondor/condor_local/spool/2729/0/cluster94962729.proc0.subproc0/TaskWorker/Actions/RetryJob.py", line 314, in check_exit_code
    self.check_corrupted_file(exitCode)
  File "/data/srv/glidecondor/condor_local/spool/2729/0/cluster94962729.proc0.subproc0/TaskWorker/Actions/RetryJob.py", line 403, in check_corrupted_file
    fragment1 = line.split('/store/')[1]
IndexError: list index out of range
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to parse job report file jobReport.json.7.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Output file info for kk.root: {'input': ['/store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/50004/44C185C3-CF69-3E41-8877-3F70821771DB.root'], 'output_module_class': 'PoolOutputModule', 'runs': {'322179': {'1244': 15689, '1305': 15143, '1307': 14942}}, 'module_label': 'output', 'events': 45774, 'inputpfns': ['root://cmsxrootd.fnal.gov//store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/50004/44C185C3-CF69-3E41-8877-3F70821771DB.root'], 'guid': '91e90c7e-7aa5-4500-9027-51f7fc704ae4', 'pfn': 'kk.root', 'lfn': '', 'branch_hash': 'd41d8cd98f00b204e9800998ecf8427e', 'catalog': ''}
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished to parse job report.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting saving data for automatic splitting.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished saving data for automatic splitting.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob The user has not specified to transfer the log files. No log files stageout (nor log files metadata upload) will be performed.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob The user has specified to not transfer the output files. No output files stageout (nor output files metadata upload) will be performed.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob Uploading output_dataset /ParkingBPH1/belforte-Stefano-TestRucioP-2308-00000000000000000000000000000000/USER to task DB
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Uploading output dataset to https://cmsweb-test2.cern.ch:8443/crabserver/dev/task: [('subresource', 'addoutputdatasets'), ('workflow', '230908_191251:belforte_crab_20230908_211238'), ('outputdatasets', '/ParkingBPH1/belforte-Stefano-TestRucioP-2308-00000000000000000000000000000000/USER')]
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting upload of input files metadata.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Uploading input metadata for /store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/50004/44C185C3-CF69-3E41-8877-3F70821771DB.root_7 to https://cmsweb-test2.cern.ch:8443/crabserver/dev/filemetadata: [('taskname', '230908_191251:belforte_crab_20230908_211238'), ('globalTag', 'None'), ('jobid', '7'), ('outsize', '0'), ('publishdataname', 'Stefano-TestRucioP-2308-00000000000000000000000000000000'), ('appver', 'CMSSW_13_1_0'), ('outtype', 'POOLIN'), ('checksummd5', '0'), ('checksumcksum', '0'), ('checksumadler32', '0'), ('outlocation', 'T2_CH_CERN'), ('outtmplocation', 'T2_US_Florida'), ('acquisitionera', 'null'), ('outlfn', '/store/data/Run2018D/ParkingBPH1/MINIAOD/05May2019promptD-v1/50004/44C185C3-CF69-3E41-8877-3F70821771DB.root_7'), ('outtmplfn', '/store/temp/user/belforte.be1f4dc5be8664cbd145bf008f5399adf42b086f/belforte/testRucioPub/ParkingBPH1/Stefano-TestRucioP-2308/230908_191251/0000/failed'), ('events', 45774), ('outdatasetname', '/FakeDataset/fakefile-FakePublish-d01b6a75269baef20ced4c4418f068a5/USER'), ('directstageout', 0), ('outfileruns', '322179'), ('outfilelumis', '1244,1305,1307')]
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished upload of input files metadata.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to prepare/send report to dashboard.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Dashboard exit code already set on the worker node. Continuing normally.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to update job ClassAd.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Dashboard exit code already set on the worker node. Continuing normally.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob status: FINISHED. ClassAd attributes to set are: {'CRAB_PostJobStatus': '"FINISHED"'}
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        -----> Started attempt 1 out of 5 -----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob        -----> Finished attempt 1 out of 5 -----
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished to update job ClassAd.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to prepare error report.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Acquiring lock on error summary file.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Acquired lock on error summary file.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob Updating error summary for jobid 7 retry 0 with following information:
'exit code' = 8021
'exit message' = Error while running CMSSW:
Fatal Exception
An exception of category 'FileReadError' occurred while
   [0] Calling InputSource::readFile_
   [1] Reading branch EventAuxiliary
   Additional Info:
      [a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers
fNbytes = 33333, fKeylen = 83, fObjlen = 184213, noutot = 0, nout=0, nin=33250, nbuf=184213

'error message' = {'type': 'Fatal Exception', 'details': "An exception of category 'FileReadError' occurred while\n   [0] Calling InputSource::readFile_\n   [1] Reading branch EventAuxiliary\n   Additional Info:\n      [a] Fatal Root Error: @SUB=TBasket::ReadBasketBuffers\nfNbytes = 33333, fKeylen = 83, fObjlen = 184213, noutot = 0, nout=0, nin=33250, nbuf=184213", 'exitCode': 8021}
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Writing error summary file
Fri, 08 Sep 2023 21:19:41 CEST(+0200):DEBUG:PostJob Written error summary file
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished to prepare error report.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Starting to prepare WMArchive report.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob WMArchiveReport.7.0.json , /data/srv/WMArchiveWD/new/230908_191251:belforte_crab_20230908_211238_WMArchiveReport.7.0.json
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ====== Finished to prepare WMArchive report.
Fri, 08 Sep 2023 21:19:41 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 0  : SUCCESS
Ended TaskManagerBootstrap with code 0
belforte@vocms0121/SPOOL_DIR>
```

## Comment (belforte, 2023-09-08T19:41:24Z)

For sake of testing I have created a truncated file with bash `truncate` at `store/user/belforte/truncatedFile.root`, since all truncated files we knew about have been fixed by DM ops now !
It can be used with
```
config.section_("Data")
config.Data.userInputFiles = ['/store/user/belforte/truncatedFile.root']
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
```

## Comment (belforte, 2023-09-11T10:47:22Z)

I do not find a reliable way to tell if corrupted file is local, or was opened at a remote file via xrootd fallback.
E.e. this is when testing the above file from FNAL:
```
cmslpc112:~$ cmsRun tr.py -j fj
11-Sep-2023 05:14:59 CDT  Initiating request to open file root://cmsxrootd-site.fnal.gov//store/user/belforte/truncatedFile.root
%MSG-w XrdAdaptorInternal:  file_open 11-Sep-2023 05:15:02 CDT pre-events
Failed to open file at URL root://cmsxrootd-site.fnal.gov:1094//store/user/belforte/truncatedFile.root?xrdcl.requuid=5633b8fb-03e2-472e-83e3-fc9e7a66d9f2.
%MSG
%MSG-w XrdAdaptorInternal:  file_open 11-Sep-2023 05:15:02 CDT pre-events
Failed to open file at URL root://cmsxrootd-site.fnal.gov:1094//store/user/belforte/truncatedFile.root?tried=&xrdcl.requuid=fd91ffef-6a1d-462e-80df-1feee0a6f66f.
%MSG
11-Sep-2023 05:15:02 CDT  Initiating request to open file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root
----- Begin Fatal Exception 11-Sep-2023 05:15:45 CDT-----------------------
An exception of category 'FileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://cmsxrootd-site.fnal.gov//store/user/belforte/truncatedFile.root
      [b] Input file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root could not be opened.
      [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init
file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root is truncated at 52428800 bytes: should be 149732140, trying to recover

----- End Fatal Exception -------------------------------------------------
cmslpc112:~$ grep -i exit fj
<FrameworkError ExitStatus="8020" Type="Fatal Exception" >
cmslpc112:~$ 
```
pretty much same as at CERN
```
belforte@lxplus806/TC3> cmsRun trPS.py -j fj
grep11-Sep-2023 12:16:31 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/user/belforte/truncatedFile.root
 -i exit 11-Sep-2023 12:16:33 CEST  Initiating request to open file root://xrootd-cms.infn.it//store/user/belforte/truncatedFile.root
fj
----- Begin Fatal Exception 11-Sep-2023 12:16:35 CEST-----------------------
An exception of category 'FileOpenError' occurred while
   [0] Constructing the EventProcessor
   [1] Constructing input source of type PoolSource
   [2] Calling RootInputFileSequence::initTheFile()
   Additional Info:
      [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://eoscms.cern.ch//eos/cms/store/user/belforte/truncatedFile.root
      [b] Input file root://xrootd-cms.infn.it//store/user/belforte/truncatedFile.root could not be opened.
      [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init
file root://xrootd-cms.infn.it//store/user/belforte/truncatedFile.root is truncated at 52428800 bytes: should be 149732140, trying to recover

----- End Fatal Exception -------------------------------------------------
belforte@lxplus806/TC3> grep -i exit fj
<FrameworkError ExitStatus="8020" Type="Fatal Exception" >
belforte@lxplus806/TC3> 
```

## Comment (belforte, 2023-09-11T13:25:25Z)

I had a faint hope that the above was due to running interactively on LPC, where maybe the local storage.json has different fallback structure, but when e.g. running at Vanderbilt I still get a report which does not mention anywhere that the corruped file is at CERN !
```
======== CMSSW OUTPUT STARTING ========
NOTICE: lines longer than 3000 characters will be truncated
== CMSSW: 11-Sep-2023 08:20:40 CDT  Initiating request to open file file:/cms/store/user/belforte/truncatedFile.root
== CMSSW: 11-Sep-2023 08:20:41 CDT  Initiating request to open file root://xrootd-vanderbilt.sites.opensciencegrid.org:1094//store/user/belforte/truncatedFile.root
== CMSSW: %MSG-w XrdAdaptorInternal:  file_open 11-Sep-2023 08:20:42 CDT pre-events
== CMSSW: Failed to open file at URL root://xrootd-vanderbilt.sites.opensciencegrid.org:1094//store/user/belforte/truncatedFile.root?xrdcl.requuid=46bfc8c2-f128-48bb-b5b7-0776e3f16bb8.
== CMSSW: %MSG
== CMSSW: %MSG-w XrdAdaptorInternal:  file_open 11-Sep-2023 08:20:42 CDT pre-events
== CMSSW: Failed to open file at URL root://xrootd-vanderbilt.sites.opensciencegrid.org:1094//store/user/belforte/truncatedFile.root?tried=&xrdcl.requuid=bf05900d-5673-4640-9282-1289244f6468.
== CMSSW: %MSG
== CMSSW: 11-Sep-2023 08:20:42 CDT  Initiating request to open file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root
== CMSSW: ----- Begin Fatal Exception 11-Sep-2023 08:21:24 CDT-----------------------
== CMSSW: An exception of category 'FileOpenError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing input source of type PoolSource
== CMSSW:    [2] Calling RootInputFileSequence::initTheFile()
== CMSSW:    Additional Info:
== CMSSW:       [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://xrootd-vanderbilt.sites.opensciencegrid.org:1094//store/user/belforte/truncatedFile.root
== CMSSW:       [b] Calling RootInputFileSequence::initTheFile(): fail to open the file with name file:/cms/store/user/belforte/truncatedFile.root
== CMSSW:       [c] Input file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root could not be opened.
== CMSSW:       [d] Fatal Root Error: @SUB=TStorageFactoryFile::Init
== CMSSW: file root://cmsxrootd.fnal.gov//store/user/belforte/truncatedFile.root is truncated at 52428800 bytes: should be 149732140, trying to recover
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```

## Comment (belforte, 2023-09-11T13:42:42Z)

side note:
 are we chasing the right issue ?
 From grafana 8028 looks much more likely than 8020 and all my tests of corrupted files have 8020.
I guess we need to sample some jobs stdout

## Comment (belforte, 2023-09-11T15:59:22Z)

there seems to be no clear rule, I just found a truncated file resulting in 8028
```
== CMSSW: 11-Sep-2023 15:59:58 CEST  Closed file root://xrootd-cms.infn.it//store/user/prebello/QCD_pThat-30_EMEnrichedDijet_HS_TuneCP5_HydjetDrumMB_5p02TeV_pythia8/QCD_pThat-30_EMEnrichedDijet_HS_TuneCP5_HydjetDrumMB_5p02TeV_pythia8/230905_200327/0004/HIN-HINPbPbAutumn18GSHIMix-00057_4879.root
== CMSSW: ----- Begin Fatal Exception 11-Sep-2023 15:59:58 CEST-----------------------
== CMSSW: An exception of category 'FallbackFileOpenError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing module: class=MixingModule label='mix'
== CMSSW:    [2] Calling RootFileSequenceBase::initTheFile()
== CMSSW:    Additional Info:
== CMSSW:       [a] dc_open(name='dcap://storage01.lcg.cscs.ch/pnfs/lcg.cscs.ch/cms/trivcat/store/user/prebello/MinBias_Hydjet_Drum5F_2018_5p02TeV/MinBias_Hydjet_Drum5F_2018_5p02TeV/230901_161230/0004/HIN-HINPbPbAutumn18GS-00033_4473.root', flags=0x0, permissions=0666) => error '"No such file or directory"' (dc_errno=30)
== CMSSW:       [b] Input file dcap://storage01.lcg.cscs.ch/pnfs/lcg.cscs.ch/cms/trivcat/store/user/prebello/MinBias_Hydjet_Drum5F_2018_5p02TeV/MinBias_Hydjet_Drum5F_2018_5p02TeV/230901_161230/0004/HIN-HINPbPbAutumn18GS-00033_4473.root could not be opened.
== CMSSW: Fallback Input file root://xrootd-cms.infn.it//store/user/prebello/MinBias_Hydjet_Drum5F_2018_5p02TeV/MinBias_Hydjet_Drum5F_2018_5p02TeV/230901_161230/0004/HIN-HINPbPbAutumn18GS-00033_4473.root also could not be opened.
== CMSSW: Original exception info is above; fallback exception info is below.
== CMSSW:       [c] Fatal Root Error: @SUB=TStorageFactoryFile::Init
== CMSSW: file root://xrootd-cms.infn.it//store/user/prebello/MinBias_Hydjet_Drum5F_2018_5p02TeV/MinBias_Hydjet_Drum5F_2018_5p02TeV/230901_161230/0004/HIN-HINPbPbAutumn18GS-00033_4473.root is truncated at 18294 bytes: should be 1281516388, trying to recover
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: slc7_amd64_gcc700
== CMSSW:         Executed: stdbuf -oL -eL cmsRun -p PSet.py -j FrameworkJobReport.xml > cmsRun-stdout.log.tmp 2>&1
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINSHING ========
==== Report file creation STARTING at Mon Sep 11 13:59:58 2023 UTC ====
Sanitize FJR

Job Exit Code from FrameworkJobReport.xml: 8028 
==== Job Exit Code from FrameworkJobReport.xml and Application exit code: 8028 ====
```

## Comment (belforte, 2023-09-11T19:42:58Z)

the discussion about "what do do" goes on also in https://github.com/dmwm/CMSRucio/issues/403

## Comment (belforte, 2023-09-11T20:53:25Z)

an OpenSearch dashboard to look for stdout of jobs failed with 802x: https://monit-opensearch.cern.ch/dashboards/goto/128a23aeb90a87603a043cfeae9e1774?security_tenant=global

## Comment (belforte, 2023-09-11T20:57:04Z)

Next step is a script which checks reports in
`/eos/cms/store/temp/user/suspicious/new` and `/eos/cms/store/temp/user/corrupted/new` and possibly reports to Rucio
the script should
- [x] make list of files
- [x] read and process
- [x] move from `new` to `done`
- [x] create a growing log with counts (one line a day ?) - moved to #7883 
- [x] remove old files from `done` - moved to #7883

## Comment (belforte, 2023-09-13T16:44:09Z)

maybe I should rename
`/eos/cms/store/temp/user/corrupted/new` --> `/eos/cms/store/temp/user/filechecker/corrupted/new`
and same for `suspicious` so to have everything under same easy-to-find directory
Too bad that I can't delete directories form /eos/cms/store/temp/user even if I am the one who created them :-(

## Comment (belforte, 2023-09-15T09:39:44Z)

similar topic, now what we parse cmsRun stdout... can something be done about more mundane problems like this which was caused by a disk pool which got bad ? I.e. genuine "local site problems" which needs to be fixed by site admins !
(refs: [cms-talk](https://cms-talk.web.cern.ch/t/corrupted-unreadable-files-for-2017b-ul/29490/3) ,  [GGUS-163339](https://ggus.eu/?mode=ticket_info&ticket_id=163339) )
```
== CMSSW: %MSG-w XrdAdaptorInternal:  file_open 14-Sep-2023 22:35:56 BST pre-events
== CMSSW: Failed to open file at URL root://gfe02.grid.hep.ph.ic.ac.uk:1097//store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root?tried=&xrdcl.requuid=d8219edd-2fd0-41d2-a0c6-7daf1d2639a7.
== CMSSW: %MSG
== CMSSW: ----- Begin Fatal Exception 14-Sep-2023 22:35:56 BST-----------------------
== CMSSW: An exception of category 'FileOpenError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing input source of type PoolSource
== CMSSW:    [2] Calling RootInputFileSequence::initTheFile()
== CMSSW:    [3] Calling StorageFactory::open()
== CMSSW:    [4] Calling XrdFile::open()
== CMSSW: Exception Message:
== CMSSW: Failed to open the file 'root://xrootd-cms.infn.it//store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root'
== CMSSW:    Additional Info:
== CMSSW:       [a] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://xrootd.grid.hep.ph.ic.ac.uk/store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root?tried=gfe02.grid.hep.ph.ic.ac.uk
== CMSSW:       [b] Calling RootInputFileSequence::initTheFile(): fail to open the file with name root://gfe02.grid.hep.ph.ic.ac.uk:1094//pnfs/hep.ph.ic.ac.uk/data/cms/store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root
== CMSSW:       [c] Input file root://xrootd-cms.infn.it//store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root could not be opened.
== CMSSW:       [d] XrdCl::File::Open(name='root://xrootd-cms.infn.it//store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root', flags=0x10, permissions=0660) => error '[ERROR] Operation expired' (errno=0, code=206). No additional data servers were found.
== CMSSW:       [e] Last URL tried: root://gfe02.grid.hep.ph.ic.ac.uk:1097//store/data/Run2017B/SingleMuon/AOD/15Feb2022_UL2017-v1/2820000/D4D070D0-F00B-CC4E-9FCC-EB026D8E02DA.root?tried=&xrdcl.requuid=d8219edd-2fd0-41d2-a0c6-7daf1d2639a7
== CMSSW:       [f] Problematic data server: gfe02.grid.hep.ph.ic.ac.uk:1097
== CMSSW:       [g] Disabled source: gfe02.grid.hep.ph.ic.ac.uk:1097
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```

I think that the crucial point here is to identify that the first open failure was on a local file, not a remote one. I.g.
 * the file is listed to be present locally, but opening it fails
vs.
 * the file is not present on local disk
 
But the info does not  appear to be there.

## Comment (belforte, 2023-09-18T13:34:23Z)

Code which detects corrupted files and reports in `/cms/store/temp/user/corrupted/new/' or  `/store/temp/user/suspicious/new/` is not in master via above PR but will not be executed. It will be enabled by 
```
touch /etc/use_corruption_check`
```
on each condor scheduler. Once we are confident that it is OK, the check will be removed.

## Comment (belforte, 2023-09-18T13:37:50Z)

now need to finalize the script which parse summaries and reports to Rucio as per https://github.com/dmwm/CRABServer/issues/7548#issuecomment-1714567989

will track in a new GH issue
