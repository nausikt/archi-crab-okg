# dmwm/CRABServer issue #9438: edmProvDump spits O(1GB) on stdout

State: closed
Opened: 2026-10-11T16:10:00Z
Closed: 2026-10-12T11:04:12Z
Labels: Type: Bug, Type: Enhancement, Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/9438

## Opening post (belforte, 2026-10-11T16:10:00Z)

A couple AP WEB_DIRs filled up suddenly and excessively, one reaching 100%

<img width="626" height="189" alt="Image" src="https://github.com/user-attachments/assets/a3b8d7ff-447c-42a3-a81b-edd0ce052f39" />

Investigation (`du -sm`) showed that the increase was due to two tasks (one per AP)
`261009_135121:slehti_crab_TTto2L2Nu_Summer24` and `261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO` where job stdout `job_out.X.Y.txt` was several hundreds of MB, up to almost a GB e.g.
```console
[crabtw@vocms0122 261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO]$ ls -lh job_out.184.0.txt
-rw-r--r-- 1 crabtw zh 898M Oct  9 23:20 job_out.184.0.txt
[crabtw@vocms0122 261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO]$ 
```
The problem came from failed attempt to compute PSet hash from user output file, in which case out script adds `edmProvDump` output to log, but somehow here that output was amazingly long... 20M lines !!!

Here I captured beginning and end of the output prefixed with line number
```
[crabtw@vocms0122 261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO]$ grep -B2 -A10 -n edmProv job_out.184.0.txt 
2748-==== PSet Hash computation STARTING at Fri Oct  9 20:50:52 2026 UTC ====
2749-==== PSet Hash computation FINISHED at Fri Oct  9 20:51:30 2026 UTC ====
2750:ERROR: PSet Hash missing from edmProvDump output.  Full dump below.
2751----------Processing histories---------
2752-History: {
2753-  SIM [1]
2754-  HLT [1]
2755-  RECO [1]
2756-  PAT [1]
2757-  NANO [1]
2758-}
2759-History: {
2760-  SIM [1]
```
```
[crabtw@vocms0122 261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO]$ grep -B10 -A30 -n "Unable"  job_out.184.0.txt 
20431960-  applyAlignment: bool tracked  = false
20431961- }
20431962-ESModule: zdcTopologyEP NANO
20431963- parameters: {
20431964-  @module_edm_type: string tracked  = 'ESProducer'
20431965-  @module_label: string tracked  = 'zdcTopologyEP'
20431966-  @module_type: string tracked  = 'ZdcTopologyEP'
20431967-  appendToDataLabel: string tracked  = ''
20431968- }
20431969-
20431970:WARNING: Unable to parse WMCore's jobReport.json; FJR will not be useful.
20431971- Traceback (most recent call last):
20431972-  File "/srv/CMSRunAnalysis.py", line 221, in handleException
20431973-    report = json.load(fh)
20431974-  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/__init__.py", line 293, in load
20431975-    return loads(fp.read(),
20431976-  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/__init__.py", line 346, in loads
20431977-    return _default_decoder.decode(s)
20431978-  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/decoder.py", line 337, in decode
20431979-    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
20431980-  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/decoder.py", line 355, in raw_decode
20431981-    raise JSONDecodeError("Expecting value", s, err.value) from None
20431982-json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
20431983-
20431984:ERROR: Exceptional exit at Fri Oct  9 20:51:32 2026 UTC 80453: Unable to compute pset hash for job output. Got exception:
20431985-PSet hash missing from edmProvDump output.
20431986-
20431987-ERROR: Traceback follows:
20431988- Traceback (most recent call last):
20431989-  File "/srv/CMSRunAnalysis.py", line 505, in AddPsetHashFjr
20431990-    raise ValueError("Process element not found under FrameworkJobReport")
20431991-ValueError: Process element not found under FrameworkJobReport
20431992-
20431993-During handling of the above exception, another exception occurred:
20431994-
20431995-Traceback (most recent call last):
20431996-  File "/srv/CMSRunAnalysis.py", line 842, in <module>
20431997-    AddPsetHashFjr(report=rep, fjr_filename='FrameworkJobReport.xml')
20431998-  File "/srv/CMSRunAnalysis.py", line 519, in AddPsetHashFjr
20431999-    raise ValueError(f"Error processing XML file: {str(err)}")
20432000-ValueError: Error processing XML file: Process element not found under FrameworkJobReport
20432001-
20432002-During handling of the above exception, another exception occurred:
20432003-
20432004-Traceback (most recent call last):
20432005-  File "/srv/CMSRunAnalysis.py", line 847, in <module>
20432006-    AddPsetHashEdmProvDump(report=rep, scramTool=scram)
20432007-  File "/srv/CMSRunAnalysis.py", line 479, in AddPsetHashEdmProvDump
20432008-    raise Exception("PSet hash missing from edmProvDump output.")
20432009-Exception: PSet hash missing from edmProvDump output.
20432010-
20432011-== Execution site for failed job from site-local-config.xml: T2_CH_CERN
20432012-+ jobrc=69
20432013-+ set +x
20432014-== The job had an exit code of 69 
[crabtw@vocms0122 261009_135106:slehti_crab_DYto2Mu_4Jets_M_50_Summer24_LO]$ 
```

We clearly need to ensure that this output is "short".
I am also amazed that the script could digest it all parse it for the pset hash !

## Comment (belforte, 2026-10-12T07:36:39Z)

one possibility is that failing tasks declared `events.root` as EDM type (via PoolOutputModule in the PSet) while successful jobs did not.

The offending jobs were using NANOAODSIM as input and ran instances of `PostProcessor`
```python
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 
```

Here's the task PSET, which likely comes from NanoAODTools ...
```python
#this fake PSET is needed for local test and for crab to figure the output filename
#you do not need to edit it unless you want to do a local test using a different input file than
#the one marked below
import FWCore.ParameterSet.Config as cms
process = cms.Process('NANO')
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(),
#       lumisToProcess=cms.untracked.VLuminosityBlockRange("254231:1-254231:24")
)
process.source.fileNames = []
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('events.root')
)
process.out = cms.EndPath(process.output)

```

If CRAB had been told  that `events.root` was not EDM in the FJR, it would not have tried to compute the PSet hash !
https://github.com/dmwm/CRABServer/blob/2e332185308e37417ed85e4f8e50652c9793cda4/scripts/job_wrapper/CMSRunAnalysis.py#L440-L442

## Comment (belforte, 2026-10-12T07:38:12Z)

should we use this as a last resort protection? ?
https://htcondor.readthedocs.io/en/latest/admin-manual/configuration/schedd.html#MAX_TRANSFER_OUTPUT_MB
currently there is no limit
```
 -1
 # at: <Default>
 # raw: MAX_TRANSFER_OUTPUT_MB = -1
```

## Comment (belforte, 2026-10-12T09:38:03Z)

I believe that I have found the reason for the problem, and created an Issue in CMSSW GH.

But we need to protect CRAB no matter what.

So will cut edmProvDump output in any case and add the `MAX_TRANSFER_OUTPUT_MB` to the schedd
