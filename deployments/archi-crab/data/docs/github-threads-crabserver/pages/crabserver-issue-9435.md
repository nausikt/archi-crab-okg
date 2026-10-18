# dmwm/CRABServer issue #9435: Job runs with a 24h proxy and fails to read data after ~1.3 day with permission error

State: closed
Opened: 2026-10-07T17:44:24Z
Closed: 2026-10-11T14:40:45Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9435

## Opening post (belforte, 2026-10-07T17:44:24Z)

currently we do not refresh proxy on AP if it is valid for 24h
https://github.com/dmwm/CRABServer/blob/74fbcb387c1ea7875d1c51d737c3cb45e34b5666/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py#L27

But such proxy is not good enough for jobs which need to run longer (we allow up to 2 days).
E.g. in this job stdout
https://cmsweb.cern.ch/scheddmon/0196/bputra/260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1/job_out.289.5.txt
we have

```text
======== PROXY INFORMATION START at Sun Oct  4 05:37:39 GMT 2026 ========
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bputra/CN=870523/CN=Bayu Adi Nugraha Putra/CN=1914544483/CN=639522693/CN=1215315622/CN=1013941152/CN=1920060926/CN=1924565322
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bputra/CN=870523/CN=Bayu Adi Nugraha Putra/CN=1914544483/CN=639522693/CN=1215315622/CN=1013941152/CN=1920060926
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bputra/CN=870523/CN=Bayu Adi Nugraha Putra/CN=1914544483/CN=639522693/CN=1215315622/CN=1013941152/CN=1920060926
type      : RFC compliant proxy
strength  : 2048 bits
path      : /srv/30af5d882a666f50700cc05c99a615df256faa0e
timeleft  : 23:59:52
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=bputra/CN=870523/CN=Bayu Adi Nugraha Putra
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
timeleft  : 83:13:31
uri       : voms-cms-auth.cern.ch:15000
```
So proxy is valid until Oct 5 05:37 GMT
and later in the log the local storage server eventually noticed and failed about 8h later

```
==== CMSSW JOB Execution started at Sun Oct  4 05:38:28 2026 UTC ====
==== Will execute stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
Error executing application in CMSSW environment.
	See stdout log
==== Execution FAILED at Mon Oct  5 13:08:47 2026 UTC ====
```
 the exception details are
```
== CMSSW: ----- Begin Fatal Exception 05-Oct-2026 08:08:43 CDT-----------------------
== CMSSW: An exception of category 'FileReadError' occurred while
== CMSSW:    [0] Processing  Event run: 375448 lumi: 45 event: 44098710 stream: 0
== CMSSW:    [1] Running path 'dStarAna_step'
== CMSSW:    [2] Prefetching for module TrackAndVertexUnpacker/'unpackedTracksAndVertices'
== CMSSW:    [3] While reading from source std::vector<pat::PackedCandidate> packedPFCandidates '' RECO
== CMSSW:    [4] Rethrowing an exception that happened on a different read request.
== CMSSW:    [5] Processing  Event run: 375448 lumi: 45 event: 44098710 stream: 0
== CMSSW:    [6] Running path 'pevt'
== CMSSW:    [7] Prefetching for module EventInfoTreeProducer/'eventinfoana'
== CMSSW:    [8] While reading from source reco::BeamSpot offlineBeamSpot '' RECO
== CMSSW:    [9] Reading branch recoBeamSpot_offlineBeamSpot__RECO.
== CMSSW:    [10] Calling File::read()
== CMSSW: Exception Message:
== CMSSW: read() failed with system error 'Permission denied' (error code 13)
== CMSSW: ----- End Fatal Exception -------------------------------------------------
```


But from the RenewProxy logs tw02, the proxy still had 70h when job was submitted on Oct 4 at
```
== JOB AD: QDate = 1791091954
LapSB:CRAB$ date -d @1791091954
Sun Oct  4 07:32:34 CEST 2026
```

```
[crab3@crab-prod-tw02 recurring]$ grep "260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1" RenewRemoveProxies_26100*
RenewRemoveProxies_261001-0603.log:2026-10-01 07:08:43,139:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 155 hours.
RenewRemoveProxies_261001-1804.log:2026-10-01 18:48:12,440:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 144 hours.
RenewRemoveProxies_261002-0604.log:2026-10-02 06:29:29,317:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 132 hours.
RenewRemoveProxies_261002-1804.log:2026-10-02 18:20:43,593:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 120 hours.
RenewRemoveProxies_261003-0604.log:2026-10-03 07:00:56,554:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 107 hours.
RenewRemoveProxies_261003-1805.log:2026-10-03 20:47:16,263:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 94 hours.
RenewRemoveProxies_261004-0605.log:2026-10-04 06:48:01,514:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 84 hours.
RenewRemoveProxies_261004-1805.log:2026-10-04 19:12:38,086:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 71 hours.
RenewRemoveProxies_261005-0605.log:2026-10-05 06:20:29,844:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 60 hours.
RenewRemoveProxies_261005-1235.log:2026-10-05 13:13:33,430:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 53 hours.
RenewRemoveProxies_261005-1614.log:2026-10-05 16:22:15,763:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 50 hours.
RenewRemoveProxies_261006-0415.log:2026-10-06 04:45:06,445:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 38 hours.
RenewRemoveProxies_261006-1615.log:2026-10-06 16:55:21,334:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 25 hours.
RenewRemoveProxies_261007-0415.log:2026-10-07 04:51:22,253:DEBUG:RenewRemoteProxies:Updated proxy pushed to schedd for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1
RenewRemoveProxies_261007-1615.log:2026-10-07 16:46:04,957:INFO:RenewRemoteProxies:Skipping refresh of proxy for task 260930_165938:bputra_crab_DStarAna_Data_RawPrime24_31_MVA0p8_DIAG_NoD0Tuple_CMSSW13211_01Oct26_v1 because it still has a lifetime of 155 hours.
[crab3@crab-prod-tw02 recurring]$ 
```

I am very puzzled that the proxy in the job was valid for exactly 24h. Very suspicious !!!
```
timeleft  : 23:59:52
```
Note that the VOMS proxy extension was longer
```
timeleft  : 83:13:31
```
and appears consistent with what should have been based on RenewRemotProxies log (and which should have sufficed !!)

Since Sept 8 crab-prod-tw02 was running v3.260907 which pushes to the AP a proxy valid for as long as possible, not 24h  as per #9393 
Therefore it is really odd that the job had a proxy valid for exactly 24h.

Do we have something wrong in how the proxy is delegated from AP to running job ?

## Comment (belforte, 2026-10-08T16:01:53Z)

While I not satisfied with understanding yet, it looks much safer not to wait for proxy on SPOOL_DIR to have <24h to live before refreshing.
So let's change
https://github.com/dmwm/CRABServer/blob/74fbcb387c1ea7875d1c51d737c3cb45e34b5666/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py#L27

## Comment (belforte, 2026-10-11T14:29:59Z)

I tested proxy renewal in our job.
Ran this script
```
printProxy() {
  ls -l $X509_USER_PROXY
  tlSec=`voms-proxy-info -timeleft`
  vlSec=`voms-proxy-info -actimeleft`
  tlHour=`echo "scale=1; $tlSec/3600" |bc`
  vlHour=`echo "scale=1; $vlSec/3600" |bc`

  echo "bare proxy time left = $tlSec sec = $tlHour hours"
  echo "voms Exten time left = $vlSec sec = $vlHour hours"
}

echo "============ SB testProxy  =================" 

for iter in `seq 47`; do
  printProxy
  sleep 1h
done

echo "============ SB ALL DONE  =======================" 
```
and here's the result (job timeout after 46 hours)
```
===== PRINT CONTENT OF FILE cmsRun-stdout.log.tmp ==== 
=== NOTICE: lines longer than 1000 characters will be truncated
============ SB testProxy  =================
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 604003 sec = 167.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 600403 sec = 166.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79187 sec = 21.9 hours
voms Exten time left = 596803 sec = 165.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75587 sec = 20.9 hours
voms Exten time left = 593203 sec = 164.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71986 sec = 19.9 hours
voms Exten time left = 589602 sec = 163.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 09:27 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68386 sec = 18.9 hours
voms Exten time left = 586002 sec = 162.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 582402 sec = 161.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 578802 sec = 160.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79187 sec = 21.9 hours
voms Exten time left = 575202 sec = 159.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75587 sec = 20.9 hours
voms Exten time left = 571602 sec = 158.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71987 sec = 19.9 hours
voms Exten time left = 568002 sec = 157.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68386 sec = 18.9 hours
voms Exten time left = 564401 sec = 156.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 560801 sec = 155.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 557201 sec = 154.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79187 sec = 21.9 hours
voms Exten time left = 553601 sec = 153.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75587 sec = 20.9 hours
voms Exten time left = 550001 sec = 152.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71987 sec = 19.9 hours
voms Exten time left = 546401 sec = 151.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct  9 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68387 sec = 18.9 hours
voms Exten time left = 542801 sec = 150.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 539200 sec = 149.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 535600 sec = 148.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79187 sec = 21.9 hours
voms Exten time left = 532000 sec = 147.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75587 sec = 20.9 hours
voms Exten time left = 528400 sec = 146.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71987 sec = 19.9 hours
voms Exten time left = 524800 sec = 145.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68387 sec = 18.9 hours
voms Exten time left = 521200 sec = 144.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86388 sec = 23.9 hours
voms Exten time left = 517599 sec = 143.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82788 sec = 22.9 hours
voms Exten time left = 513999 sec = 142.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79188 sec = 21.9 hours
voms Exten time left = 510399 sec = 141.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75588 sec = 20.9 hours
voms Exten time left = 506799 sec = 140.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71988 sec = 19.9 hours
voms Exten time left = 503199 sec = 139.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 09:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68388 sec = 18.9 hours
voms Exten time left = 499599 sec = 138.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86388 sec = 23.9 hours
voms Exten time left = 495998 sec = 137.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 492398 sec = 136.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79187 sec = 21.9 hours
voms Exten time left = 488798 sec = 135.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75587 sec = 20.9 hours
voms Exten time left = 485198 sec = 134.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71987 sec = 19.9 hours
voms Exten time left = 481598 sec = 133.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 15:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68387 sec = 18.9 hours
voms Exten time left = 477998 sec = 132.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 474398 sec = 131.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 470797 sec = 130.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79186 sec = 21.9 hours
voms Exten time left = 467197 sec = 129.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 75586 sec = 20.9 hours
voms Exten time left = 463597 sec = 128.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 71986 sec = 19.9 hours
voms Exten time left = 459997 sec = 127.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 10 21:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 68386 sec = 18.9 hours
voms Exten time left = 456397 sec = 126.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 11 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 86387 sec = 23.9 hours
voms Exten time left = 452797 sec = 125.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 11 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 82787 sec = 22.9 hours
voms Exten time left = 449197 sec = 124.7 hours
-rw------- 1 cmsgli us_cms 18883 Oct 11 03:28 /srv/c6ea75e904ebb26531217d954bd562c96db20c11
bare proxy time left = 79186 sec = 21.9 hours
voms Exten time left = 445596 sec = 123.7 hours

===== END OF FILE ==== 
```

Conclusion:
* **GOOD:** HTCondor delegates initially a 24h proxy and then keeps renewing whenever lifetime gets ~18h creating a new 24h proxy
* **BAD:** VOMS extension is not touched and remains what it was at the time the job was submitted
* **I.E.:** HTCondor proxy renewal works finely, but it is not sufficient for us
* **THEREFORE:** we must make sure that VOMS extension isnever <48h on the SPOOL_DIR, to make sure that jobs will have a valid VOMS extension even if they run the max. time

## Comment (belforte, 2026-10-11T14:32:54Z)

given the above and the fact that ProxyRenewal runs every 6h, I will increase the minimum guaranteed validity in the SPOOL_DIR to 3 days = 72 hours so that we are OK even if ProxyRenewal skips a few runs for some reason
