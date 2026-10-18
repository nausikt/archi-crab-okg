# dmwm/CRABServer issue #9357: investigate exit code 50115

State: closed
Opened: 2026-07-20T14:40:35Z
Closed: 2026-09-28T17:02:31Z
URL: https://github.com/dmwm/CRABServer/issues/9357

## Opening post (belforte, 2026-07-20T14:40:35Z)

it is too much generic. Sometimes a simple grep of cmsRun log may give better hints (a segfault e.g.)

## Comment (nausikt, 2026-08-20T12:47:54Z)

As i skimming through 87 of 50115 tasks by distinct user [3], let me laid out some incomplete thoughts na.

# Seemingly Classic Transient
They got segmentation fault CoreDump with one follow-up retry then fine [?]. 
Typically ended with `BadFWJRXML`, 50115.
Examples:
- [260813_154347:joshin_crab_muRPCTnPFlatTableProducer_cfg_Muon0_Run2024I-PromptReco-v1](http://vocms0137.cern.ch/mon/joshin/260813_154347:joshin_crab_muRPCTnPFlatTableProducer_cfg_Muon0_Run2024I-PromptReco-v1/job_out.729.0.txt)
- [260725_131513:tdey_crab_MonoHToGG_ZpBaryonic_MZp1500_MChi400_TuneCP5_13TeV_madgraph-pythia8](http://vocms0137.cern.ch/mon/tdey/260725_131513:tdey_crab_MonoHToGG_ZpBaryonic_MZp1500_MChi400_TuneCP5_13TeV_madgraph-pythia8/job_out.30.0.txt)
```
== CMSSW: #13 0x0000000000000000 in ?? ()
== CMSSW:
== CMSSW: Current Modules:
== CMSSW:
== CMSSW: Module: none (crashed)
== CMSSW:
== CMSSW: A fatal system signal has occurred: segmentation violation
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: slc7_amd64_gcc700
== CMSSW:         Executed: stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout: /bin/bash: line 165:   529 Segmentation fault      (core dumped) stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINISHING ========
==== Report file creation STARTING at Sat Jul 25 14:47:34 2026 UTC ====
Sanitize FJR

WARNING: Unable to parse WMCore's jobReport.json; FJR will not be useful.
 Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 221, in handleException
    report = json.load(fh)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/__init__.py", line 357, in loads
    return _default_decoder.decode(s)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

ERROR: Exceptional exit at Sat Jul 25 14:47:34 2026 UTC 50115: BadFWJRXML
```

# Classic Terminally failures?
Maybe compilation errors — or any other hundreds of possibilities, let me gathered more coverage logs of these kind. 
Typically end with: `Exception while handling the job report.`, 50115.
Examples:
- [260731_232715:sqian_crab_ParkingDoubleMuonLowMass5_Run2025D_PromptReco_v1_mmphi_2026Jul31b](http://vocms0199.cern.ch/mon/sqian/260731_232715:sqian_crab_ParkingDoubleMuonLowMass5_Run2025D_PromptReco_v1_mmphi_2026Jul31b/job_out.92.0.txt)

```
== CMSSW:
== CMSSW: #undef  _BACKWARD_BACKWARD_WARNING_H
== CMSSW:
== CMSSW: Error in <TClass::LoadClassInfo>: no interpreter information for class TStorageFactoryFile is available even though it has a TClass initialization routine.
== CMSSW: input_line_27:2:2: error: unknown type name 'line'
== CMSSW: #line 1 "DataFormatsStdDictionaries_xr dictionary forward declarations' payload"
== CMSSW:  ^
== CMSSW: DataFormatsStdDictionaries_xr dictionary forward declarations' payload:1:8: error: expected ';' after top level declarator
== CMSSW: #pragma clang diagnostic ignored "-Wkeyword-compat"
== CMSSW:        ^
== CMSSW:        ;
== CMSSW: ----- Begin Fatal Exception 05-Aug-2026 02:24:57 EDT-----------------------
== CMSSW: An exception of category 'FatalRootError' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Constructing service of type InitRootHandlers
== CMSSW:    [2] Calling edm::TypeWithDict::byName()
== CMSSW:    Additional Info:
== CMSSW:       [a] Getting TClass for std::vector<std::vector<unsigned int> >
== CMSSW:       [b] Fatal Root Error: @SUB=TInterpreter::TCling::RegisterModule
== CMSSW: Problems in compiling forward declarations for module DataFormatsStdDictionaries_xr: '
== CMSSW: #line 1 "DataFormatsStdDictionaries_xr dictionary forward declarations' payload"
== CMSSW: #pragma clang diagnostic ignored "-Wkeyword-compat"
== CMSSW: #pragma clang diagnostic ignored "-Wignored-attributes"
== CMSSW: #pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
== CMSSW: extern int __Cling_AutoLoading_Map;
== CMSSW: namespace std{template <typename _T1, typename _T2> struct __attribute__((annotate("$clingAutoload$bits/stl_pair.h")))  __attribute__((annotate("$clingAutoload$string")))  pair;
== CMSSW: }
== CMSSW: namespace std{template <typename _CharT> struct __attribute__((annotate("$clingAutoload$bits/char_traits.h")))  __attribute__((annotate("$clingAutoload$string")))  char_traits;
== CMSSW: }
== CMSSW: namespace std{template <typename > class __attribute__((annotate("$clingAutoload$bits/memoryfwd.h")))  __attribute__((annotate("$clingAutoload$string")))  allocator;
== CMSSW: }
== CMSSW: namespace std{template <typename _Tp = void> struct __attribute__((annotate("$clingAutoload$bits/stl_function.h")))  __attribute__((annotate("$clingAutoload$string")))  less;
== CMSSW: }
== CMSSW: '
== CMSSW:
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW: Failed to load module RooFitMore
== CMSSW: Failed to load module ROOTGpadv7
== CMSSW: Failed to load module Recorder
== CMSSW: Failed to load module ROOTHistDraw
== CMSSW: Failed to load module ASImage
== CMSSW: Failed to load module ASImageGui
== CMSSW: Failed to load module ROOTTreeViewer
== CMSSW: Failed to load module ROOTGraphicsPrimitives
== CMSSW: Failed to load module ROOTFitPanelv7
== CMSSW: Failed to load module ROOTGpadv7
== CMSSW: Failed to load module ROOTTreeViewer
== CMSSW: Failed to load module ROOTGraphicsPrimitives
== CMSSW: Failed to load module ROOTFitPanelv7
== CMSSW: Failed to load module ROOTHistDraw
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: el9_amd64_gcc12
== CMSSW:         Executed: stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINISHING ========
==== Report file creation STARTING at Wed Aug  5 06:24:57 2026 UTC ====
Sanitize FJR

WARNING: Unable to parse WMCore's jobReport.json; FJR will not be useful.
 Traceback (most recent call last):
  File "/srv/CMSRunAnalysis.py", line 221, in handleException
    report = json.load(fh)
  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/cvmfs/cms.cern.ch/cs9_amd64_gcc11/external/python3/3.9.6-2c93591d796451daeaf67dc8130bfa35/lib/python3.9/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

ERROR: Exceptional exit at Wed Aug  5 06:24:57 2026 UTC 50115: Exception while handling the job report.
```

# Next
I will gather all these expected, tolerable, distinct behaviours and skim through them in detail with an LLM to classify the failure modes. Alternatively, we could go back up to one month in the logs to cover the most recent mountains for flooding submissions.
________

P.S. In order to see the pattern comprehensively, I grasped 87 x 50115 jobs by distinct user, queried via OS DevTool [1] then parse/transform/reconstruct as url via `jq` cmd for the ease of investigating, fetching problematic postjob/jobout log. [2]
P.S. vocms0195, vocms0199 sometimes they are accessible sometimes they aren't.

- [1] OS filter, query
```
GET monit_prod_condor_raw_metric*/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        { "range": { "metadata.timestamp": { "gte": "now-1M", "lte": "now" } } },
        { "term":  { "data.ExitCode": 50115 } },
        { "term":  { "data.CMS_Type": "Analysis" } },
        { "term":  { "data.CMS_SubmissionTool": "CRAB" } },
        { "term":  { "data.CMS_TaskType": "cmsRun" } }
      ]
    }
  },
  "aggs": {
    "by_group": {
      "terms": {
        "field": "data.AccountingGroup",
        "size": 1000,
        "order": { "_count": "desc" }
      },
      "aggs": {
        "example_task": {
          "top_hits": {
            "size": 5,
            "_source": [
              "data.CRAB_Reqname",
              "data.AccountingGroup",
              "data.ScheddName",
              "data.FormattedCrabId",
              "data.ExitCode"
            ]
          }
        }
      }
    }
  }
}
```
- [2] parsing via JQ as following
```bash
jq -r '
  def job_id:
    split(".")
    | if length == 1
      then (.[0] | tonumber | tostring)
      else (.[0] | tonumber | tostring) + "-" + (.[-1] | tonumber | tostring)
      end;

  def crab_urls:
    (.ScheddName      | split("@")[1])              as $host
    | (.AccountingGroup | split(".")[1:] | join(".")) as $user
    | (.FormattedCrabId | job_id)                    as $jid
    | "http://\($host)/mon/\($user)/\(.CRAB_Reqname)" as $base
    | { postjob_url: "\($base)/postjob.\($jid).0.txt",
        job_out_url: "\($base)/job_out.\($jid).0.txt" };

  [ .aggregations.by_group.buckets[]
    | .example_task.hits.hits[0]._source.data as $d
    | { group: $d.AccountingGroup,
        FormattedCrabId: $d.FormattedCrabId,
        ScheddName: $d.ScheddName,
        ExitCode:  $d.ExitCode,
        task:  $d.CRAB_Reqname }
      + ($d | crab_urls)
  ]
' 50115.CRAB.cmsRun.distinct.user.raw.json > 50115.CRAB.cmsRun.distinct.user.json
```
- [3] [50115.CRAB.cmsRun.distinct.user.json](https://cms-docs.web.cern.ch/CRAB/investigations/50115.CRAB.cmsRun.distinct.user.json)
```json
{
    "group": "analysis.tdey",
    "FormattedCrabId": "000030",
    "ScheddName": "crab3@vocms0137.cern.ch",
    "ExitCode": 50115,
    "task": "260725_131513:tdey_crab_MonoHToGG_ZpBaryonic_MZp1500_MChi400_TuneCP5_13TeV_madgraph-pythia8",
    "postjob_url": "http://vocms0137.cern.ch/mon/tdey/260725_131513:tdey_crab_MonoHToGG_ZpBaryonic_MZp1500_MChi400_TuneCP5_13TeV_madgraph-pythia8/postjob.30.0.txt",
    "job_out_url": "http://vocms0137.cern.ch/mon/tdey/260725_131513:tdey_crab_MonoHToGG_ZpBaryonic_MZp1500_MChi400_TuneCP5_13TeV_madgraph-pythia8/job_out.30.0.txt"
  }
```

## Comment (nausikt, 2026-08-20T13:01:17Z)

### Next
- [x] Gather `cmsRun-stdout.log` (`job_out.X.0.log`) from all problematic 50115 tasks locally.
- [x] Feed them to an LLM for quick hints on classification patterns.
- [x] Gather up to a month, while the logs still exist. [More Samplings]

## Comment (belforte, 2026-08-20T13:10:38Z)

we already know that segmentation faults are part of the culprits, simply our wrapper is not very good at catching this condition. Most likely worth to do some small change in job wrapper to detect this in the log and set a more telling exit code.

P.S. you link [3] gives error 
P.P.S. which OS index do you query ? usual one has only 30 days, how can we go back longer ? (I am interested for the other errors too)

## Comment (nausikt, 2026-08-20T13:22:34Z)

Thanks Stefano! Link [3] was fixed.

It's a usual condor_raw_metric os idx. One possibility to go back further is digging into HDFS for job records up-to 6 months.
Though SPOOL_DIR periodically wiped out are the actual hard limit to go back in time.

## Comment (nausikt, 2026-08-20T13:33:03Z)

Apologize i meant right now we have 87 jobs since last week, we will grasp more up-to a month if possible to have better coverage.

## Comment (nausikt, 2026-08-24T09:41:30Z)

I had sampled 5 x 50115 jobs for each distinct user over a month, approximately 301 cases in total. [1,2]
- [1] [50115.CRAB.cmsRun.distinct.user.raw.1M.5samples.json](https://cms-docs.web.cern.ch/CRAB/investigations//50115.CRAB.cmsRun.distinct.user.1M.5samples.json) **got 277 more cases, somehow many failed with 404, either fall into inconsistent webdir issue or SPOOL_DIR been wiped out  
- [2] [All jobout_logs](https://cms-docs.web.cern.ch/CRAB/investigations/jobout_logs/)

## Comment (nausikt, 2026-08-24T12:32:56Z)

After dump a few errors to Claude and some discussions.

Let's briefly classified into 4 mains category.

1. **BadCode** — fails identically on every file, every node, every replica.
The defect is in the release or configuration. Input is irrelevant.
P.S. Can/Should we breakdown BadCode? or no points. IMO, no points leave them alone in 50115. 

2. **BadData** — fails on specific events or specific files; other files in the same dataset succeed.
The input is intact but content triggers an unhandled path.

3. **BadFileReplica** (Transient) — fails on one physical copy; the same LFN read from a different site succeeds.
Bytes on disk are wrong. Logical dataset is fine.

4. **FlakySite** (Transient) — fails on one node or during one time window; succeeds elsewhere on the same input.
Nothing wrong with code or data.

## Example of Bad Code 
[1] [**Bad Code**] Data/Code-dependent framework exceptions followed by a crash, like **InvalidReference** at event 1785
[260718_200303_llorente_crab_20260718_220225.job_out.3-2684.0](https://cms-docs.web.cern.ch/CRAB/investigations/jobout_logs/260718_200303_llorente_crab_20260718_220225.job_out.3-2684.0.txt)
```
== CMSSW: Begin processing the 1785th record. Run 1, Event 120150783, LumiSection 120151 on stream 0 at 21-Jul-2026 23:40:39.342 EDT
== CMSSW: ----- Begin Fatal Exception 21-Jul-2026 23:40:40 EDT-----------------------
== CMSSW: An exception of category 'InvalidReference' occurred while
== CMSSW:    [0] Processing  Event run: 1 lumi: 120151 event: 120150783 stream: 0
== CMSSW:    [1] Running path 'MINIAODSIMoutput_step'
== CMSSW:    [2] Prefetching for module PoolOutputModule/'MINIAODSIMoutput'
== CMSSW:    [3] Prefetching for module L1ECALPrefiringWeightProducer/'prefiringweight'
== CMSSW:    [4] Prefetching for module PATJetSelector/'slimmedJets'
== CMSSW:    [5] Prefetching for module PATJetUpdater/'updatedPatJetsTransientCorrectedSlimmedDeepFlavour'
== CMSSW:    [6] Prefetching for module PATJetUpdater/'updatedPatJetsSlimmedDeepFlavour'
== CMSSW:    [7] Prefetching for module PATJetSlimmer/'slimmedJetsNoDeepFlavour'
== CMSSW:    [8] Prefetching for module PATJetSelector/'selectedPatJets'
== CMSSW:    [9] Calling method for module PATJetProducer/'patJets'
== CMSSW: Exception Message:
== CMSSW: AssociationVector: trying to use [] operator passing a reference
== CMSSW:  with the wrong product id (i.e.: pointing to the wrong collection)
== CMSSW:  keyRef.id = 5:1266, ref.id = 0:0
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW: 21-Jul-2026 23:40:40 EDT  Closed file root://cmsxrootd.fnal.gov//store/mc/RunIISummer20UL17RECO/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/AODSIM/106X_mc2017_realistic_v6-v2/270002/E7E7D83C-FC64-BA48-8F5F-70361F9E13EC.root
```

[2] [BadCode] The G4 message names the cause outright: Likely geometry overlap, between eehier:EEBackDee_1 and eehier:EEBackQuad_1. That's a defect in the ECAL endcap geometry description, not in any input. 
[260720_130703_kakang_crab_MC_ggHtoDsstW_phipi_2022_20260717.job_out.858.0.txt](https://cms-docs.web.cern.ch/CRAB/investigations/jobout_logs/260720_130703_kakang_crab_MC_ggHtoDsstW_phipi_2022_20260717.job_out.858.0.txt)
```
== CMSSW: Begin processing the 329th record. Run 1, Event 2571329, LumiSection 858 on stream 0 at 20-Jul-2026 20:07:22.721 CEST
== CMSSW: Begin processing the 330th record. Run 1, Event 2571330, LumiSection 858 on stream 0 at 20-Jul-2026 20:07:31.930 CEST
== CMSSW: %MSG-w SimG4CoreApplication:  (NoModuleName) 20-Jul-2026 20:07:54 CEST  pre-events
== CMSSW:
== CMSSW: -------- EEEE ------- G4Exception-START -------- EEEE -------
== CMSSW: *** G4Exception : GeomNav0003
== CMSSW:       issued by : G4Navigator::ComputeStep()
== CMSSW: Stuck Track: potential geometry or navigation problem.
== CMSSW:   Track stuck, not moving for 25 steps.
== CMSSW:   Current  phys volume: 'eehier:EEBackQuad_1'
== CMSSW:    - at position : (350.3423721583744,-149.3578232336829,-3649.000001174346)
== CMSSW:      in direction: (0.4025486379684495,0.4743687710571217,-0.7828977347747932)
== CMSSW:     (local position: (350.3423721583731,149.3578232336825,3665.000001174346))
== CMSSW:     (local direction: (0.4025486379684491,-0.4743687710571217,0.7828977347747932)).
== CMSSW:   Previous phys volume: 'eehier:EEBackDee_1'
== CMSSW:
== CMSSW:   Likely geometry overlap - else navigation problem !
== CMSSW:  Track *abandoned* due to excessive number of Zero steps. Event aborted.
== CMSSW:
== CMSSW:
== CMSSW:  CMS info: TrackID=427018 ParentID=425261  neutron; Ekin(MeV)=178.91; time(ns)=13.5186; status=0
== CMSSW:    position(mm): (350.342,-149.358,-3649); direction: (0.402549,0.474369,-0.782898)
== CMSSW:    PhysicalVolume: eehier:EEBackQuad_1; material: materials:E_Air
== CMSSW:    stepNumber=38; stepLength(mm)=1e-07; weight=1; creatorProcess: pi-Inelastic; modelID=-1
== CMSSW:
== CMSSW: -------- EEEE -------- G4Exception-END --------- EEEE -------
== CMSSW:
== CMSSW: %MSG
== CMSSW: ----- Begin Fatal Exception 20-Jul-2026 20:07:54 CEST-----------------------
== CMSSW: An exception of category 'Geant4 fatal exception' occurred while
== CMSSW:    [0] Processing  Event run: 1 lumi: 858 event: 2571330 stream: 0
== CMSSW:    [1] Running path 'RAWSIMoutput_step'
== CMSSW:    [2] Prefetching for module PoolOutputModule/'RAWSIMoutput'
== CMSSW:    [3] Calling method for module OscarMTProducer/'g4SimHits'
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW: Another exception was caught while trying to clean up runs after the primary fatal exception.
== CMSSW: Another exception was caught while trying to clean up files after the primary fatal exception.
== CMSSW:
== CMSSW: ------------------------------------
== CMSSW: GenXsecAnalyzer:
== CMSSW: ------------------------------------
```
Clearly user customized simulation-specific code error
Geant4 fatal exception is not an EDMException.h category — it's a custom string thrown by OscarMTProducer. Unrecognized categories collapse to the generic CMSSW "other" code, so even with a valid FJR you'd learn nothing more specific than "something in CMSSW threw."
Noted:
Any Exit-code mapping gap? need to be reconsidered?
50122 — Geant4 geometry/navigation failure (stuck track, zero-step, overlap). Distinguishable by the GeomNav#### tag plus the volume names, both of which are always printed.

________

### To nail down transients (BadFileReplica, FlakySite) errors log patterns. 

Claude suggest the same approach that Stefano and Vijay had used last year.

Which is to take a few months of 50115 jobs, group by workflow and by whether the retry succeeded, and check whether success correlates with landing on a different node versus a different input replica.

This way we may have 2 more transients class separate from terminal failed BadCode?

## Next
- [ ] Query jobs 50115 with retry succeed to see transient pattern cleanly.
- [ ] Go through more Error patterns among 300 logs we've now, try to critically analyze.

## Comment (belforte, 2026-08-24T13:17:51Z)

Both examples [1] and [2] contains the telling line
`== CMSSW: A fatal system signal has occurred: segmentation violation`

I think that we should grep for that in the CMSSW log in the wrapper and make sure that we get an FJR with the correct error, so that PostJob does not fall back to 50115. We should be able to catch also segmentation violation in user code.

All in all our twiki already says
"50115 - cmsRun did not produce a valid job report at runtime (often means cmsRun segfaulted) "

I suspect that we need to define a new exit code in the 50xxx range. Or just use the simple `11` which is unix  `SIGSEGV` signal.

Please note that currently we only care to have a "named"  reason for the failure and "user code segfaulted" is a good reason.
We are not in the business of fixing code which fails all of the times or only when input data or random number sequence causes an unusual situation.

If we know for sure that all 50115 are due to segmentation violation, we may simply rename it !!

So next step is to check what was the reason for [3]. Maybe [3] is a fatal error inside Root ?

About [4] I'd be interested in knowing if we can have a transient segmentation violation, or whether it was a different error in those cases.

## Comment (nausikt, 2026-08-24T13:22:25Z)

Got it, Thanks for the clues! they all resonated with me.

## Comment (nausikt, 2026-09-01T09:15:44Z)

Here's high signal task that have 1000 jobs succeed after thousands of retries in total. (this task is 3~4k jobs scale and majority of succeed retries were 50115, though tasks not finished yet.).

Also worth noting that the task executed at one site which hold possibilities of being site-related issues.

Task: `260811_221520:snandaku_crab_SMEFT_CuH12_HplusU_QUAD_HToZZTo4l_Step3_RECO_2022postEE_v1`
Task Grafana: [260811_221520:snandaku_crab_SMEFT_CuH12_HplusU_QUAD_HToZZTo4l_Step3_RECO_2022postEE_v1](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=trmishra&var-task=260811_221520:snandaku_crab_SMEFT_CuH12_HplusU_QUAD_HToZZTo4l_Step3_RECO_2022postEE_v1&from=now-90d&to=now&timezone=utc&var-site=$__all&var-schedd=0122&var-cmsUserId=&var-task_str=snandaku_crab_SMEFT_CuH12_HplusU_QUAD_HToZZTo4l_Step3_RECO_2022postEE_v1&var-status=$__all&var-crabid=$__all&var-Filters=&var-rest_host=https:%2F%2Fcmsweb.cern.ch)

## Comment (belforte, 2026-09-01T09:31:48Z)

that's surely a peculiar stdout ! 
```text

======== CMSSW OUTPUT STARTING ========
NOTICE: lines longer than 3000 characters will be truncated
== CMSSW: %MSG-i ThreadStreamSetup:  (NoModuleName) 14-Aug-2026 06:23:15 CEST pre-events
== CMSSW: setting # threads 4
== CMSSW: setting # streams 4
== CMSSW: %MSG
== CMSSW:
== CMSSW:  *** Break *** segmentation violation
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: el8_amd64_gcc10
== CMSSW:         Executed: stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout: /bin/bash: line 149:   750 Segmentation fault      (core dumped) stdbuf -oL -eL cmsRun -j FrameworkJobReport.xml PSet.py > cmsRun-stdout.log.tmp 2>&1
== CMSSW:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINISHING ========
```

## Comment (nausikt, 2026-09-01T10:11:11Z)

Here is a Hopeless 50115 where no succeed after retries. (permanent, clearly user code errors, no signs of transient with-in)

15,000 jobs (including retries all wasted!)

Task: `260808_210941:wgong_crab_B2jpsiPhiK_PHSP_2016pre_fullchain_n100x5000`
Task Grafana: [260808_210941:wgong_crab_B2jpsiPhiK_PHSP_2016pre_fullchain_n100x5000](https://monit-grafana.cern.ch/goto/dfwxjoa0kmmm8e?orgId=11)

## Comment (nausikt, 2026-09-01T10:17:39Z)

And to add cherry on top of the cake.

There's 8 tasks of these kind of 15k completely failed jobs from a single user!

- 260808_210941:wgong_crab_B2jpsiPhiK_PHSP_2016pre_fullchain_n100x5000
- 260808_205713:wgong_crab_B2jpsiPhiK_PHSP_2022_fullchain_n100x5000
- 260808_205731:wgong_crab_B2jpsiPhiK_PHSP_2022postEE_fullchain_n100x5000
- 260808_205829:wgong_crab_B2jpsiPhiK_PHSP_2023BPix_fullchain_n100x5000
- 260808_210907:wgong_crab_B2jpsiPhiK_PHSP_2018_fullchain_n100x5000
- 260808_210922:wgong_crab_B2jpsiPhiK_PHSP_2017_fullchain_n100x5000
- 260808_211004:wgong_crab_B2jpsiPhiK_PHSP_2016post_fullchain_n100x5000
- 260808_205815:wgong_crab_B2jpsiPhiK_PHSP_2023_fullchain_n100x5000

## Comment (nausikt, 2026-09-01T10:34:43Z)

Please, allow me to note more of 50115 transients cases.
 
Here's 10k-scale-jobs task `260824_133216:ekoenig_crab_ggZH_HToBB_ZToBB_M-125_2024_v1` which even they got 50115 failures over 20k jobs (retries) scattered on **multiple sites** but it eventually succeed their retries and completed well. 

```json
{
  "key": "260824_133216:ekoenig_crab_ggZH_HToBB_ZToBB_M-125_2024_v1",
  "50115_job_count": 21463,
  "succeed_job_after_retry": 7041,
  "total_retry_before_succeed": 21994,
  "grafana": "https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=ekoenig&var-task=260824_133216:ekoenig_crab_ggZH_HToBB_ZToBB_M-125_2024_v1&from=1787578336000&to=now",
  "task_info": "https://cmsweb.cern.ch/crabserver/ui/task/260824_133216%3Aekoenig_crab_ggZH_HToBB_ZToBB_M-125_2024_v1"
}
```

## Comment (nausikt, 2026-09-01T12:11:05Z)

## Overview
* We queried 1,000 of 50115 tasks over a month. [1]
*That experienced 50115 at least a job, since **04-08-2026** till **30-08-2026***

## [BadCode/Data, 26.2%, 50AAA, new Permanent]
**262** tasks falls into user code error and were permanent, since they have **NO SUCCEED** after retries. 
*Exhaustively retried 3 times.* 
```json
{ "succeed_job_after_retry": null, "total_retry_before_succeed": null }
```
**Regexes**: Just capture `segmentation violation` and let this be default route for all user code error
*P.S. Neither we're in business of finding generic error log patterns/regexes nor retry these failure modes anyhow.*

**Actions**:  
- Either Introduce new ExitCode (50AAA) OR let them stay with `50115`
- AND *IMHO*, we can let this default route ***Fail Fast*** (**NO Retry**) 
*P.S. This way not only we no longer waste resources, but also let users having a faster feedback loop for their code failures.*

## [BadFileReplica/Site-related, at least 56.5%, 50BBB...50XXX, new Transients]
There's **565** tasks that have at least 80% of their job failures came from 50115 and all of 50115 failures eventually succeeded on retry
Thus, we can dive deeper and potentially do log regexes/pattern recognition and classification here. 

**Regexes**: **TBD**

**Actions**:  
- Introduce new **Recoverable** ExitCode (50BBB...50XXX) give them clear transient definitions.

[1] [All 1000 of 50115 workflows, summarized data](https://cms-docs.web.cern.ch/CRAB/investigations/50115.workflows.with.succeed.and.retry.infos.and.help.urls.joined.json)

```json
{
    "key": "260820_134310:ekoenig_crab_ZZTo4B01j_5f_NLO_FXFX_2024_v5",
    "50115_job_count": 47336,
    "succeed_job_after_retry": 10026,
    "total_retry_before_succeed": 65502,
    "grafana": "https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=ekoenig&var-task=260820_134310:ekoenig_crab_ZZTo4B01j_5f_NLO_FXFX_2024_v5&from=1787233390000&to=now",
    "task_info": "https://cmsweb.cern.ch/crabserver/ui/task/260820_134310%3Aekoenig_crab_ZZTo4B01j_5f_NLO_FXFX_2024_v5"
}
```
[2] [Overview stats](https://cms-docs.web.cern.ch/CRAB/investigations/50115.workflows.overview.json)
```json
{
  "total": 1000,
  "50115_permanent": 262,
  "50115_p80": 565,
  "50115_p50": 79,
  "below_50115_p50": 94
}
```

## Comment (nausikt, 2026-09-01T12:21:04Z)

## [The rest, 50115 <p80, 17.3%, Mixtures of 50115 and other ExitCodes failures]
These 173 tasks, we better discard them since half or just minority ExitCodes are 50115. it just mixed with other thus it were very hard to tell whether these 50115s were actually the one who succeed retry. 

Not worth it to digging-into/classifying these fractions of queried workflows here.

## Comment (nausikt, 2026-09-01T16:33:36Z)

## Next, dive into BadFileReplica/Site-related
- [ ] Randomly samples 5 ~ 10 jobs from only in 50115_p80 task pool and fetch their job_out logs.
- [ ] Dump to LLM and let it briefly categorize them in potential transient failure modes.
- [ ] Nail down regexes the same way we did in FTS-based ASO ExitCodes.
- [ ] Integrate catching & regexes into current mechanism.

## Comment (belforte, 2026-09-01T17:08:59Z)

about
>  Here's 10k-scale-jobs task 260824_133216:ekoenig_crab_ggZH_HToBB_ZToBB_M-125_2024_v1 which even they got 50115 failures over 20k jobs (retries) scattered on multiple sites but it eventually succeed their retries and completed well.

It is very "interesting", failures were due to error in intializing apptainer
(user sends a script which does `cmssw-el8 ... some commands` which is IMHO totally stupid since jobs already start in an EL8 apptainer).

So it seems something like apptainer was being updated in CVMFS and things were failing, no matter where. Then build was completed, and things started to work.

Yet I'd rather not parse app. stdout to look for apptainer error, nor would flag this as site problem.

## Comment (belforte, 2026-09-01T17:13:04Z)

I suggest to check if the recverable 50115 have some clear pattern, like very short wall time. If they fail in <30 sec it could indeed be bad worker node ( https://github.com/dmwm/CRABServer/issues/9357#issuecomment-5491725323 ) or CVMFS problem ( https://github.com/dmwm/CRABServer/issues/9357#issuecomment-5491725323 )

Hopefully users fixed already bugs which made their code segfault right away. And also there's no big damage in retrying a jobs which used little CPU. But when segfault happen after application has been running for a while, let's report it as such.

## Comment (belforte, 2026-09-01T17:15:11Z)

labelling the error  as recoverable when it succeeds after 6 retries does not help us to decide how to call it at retry #3, nor to decide a specific action.

## Comment (nausikt, 2026-09-02T07:03:48Z)

Thanks Stefano for illuminating comments and pointing out the pitfalls, let me converge to that.
