# dmwm/CRABServer issue #8904: processing of LHE input files is broken

State: closed
Opened: 2025-01-29T22:26:12Z
Closed: 2025-02-04T08:32:57Z
Labels: Type: Bug, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8904

## Opening post (belforte, 2025-01-29T22:26:12Z)

As reported by two users
1. https://cms-talk.web.cern.ch/t/every-crab-job-runs-with-the-same-input-event/2489
2. private communication by Annalisa Feliziani (in Italian)

when running PrivateMC with LHE input, every job processes the same events form the input file.

Link to a task which exhibits the problem: https://cmsweb.cern.ch/crabserver/ui/task/250124_151436%3Aafelizia_crab_crab_afelizia_2025-01-24_UTC16-14-24

Annalisa digged in already with `crab preparelocal` and found the following (translating in English):

PSet used by first job
```text
process = cms.Process("LHE")

process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://eosuser.cern.ch////eos/user/a/afelizia/CMSPhysicsAnalysis/Output/LHE_FIN/toy_mc_pps_HX_massS900_massX735_GeV.lhe'),
    firstEvent = cms.untracked.uint32(1),
    firstLuminosityBlock = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(1),
    numberEventsInLuminosityBlock = cms.untracked.uint32(100),
    skipEvents = cms.untracked.uint32(0)
)
```
PSet used by second job
```text
process = cms.Process("LHE")

process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://eosuser.cern.ch////eos/user/a/afelizia/CMSPhysicsAnalysis/Output/LHE_FIN/toy_mc_pps_HX_massS900_massX735_GeV.lhe'),
    firstEvent = cms.untracked.uint32(21),
    firstLuminosityBlock = cms.untracked.uint32(2),
    firstRun = cms.untracked.uint32(1),
    numberEventsInLuminosityBlock = cms.untracked.uint32(100),
    skipEvents = cms.untracked.uint32(0)
)
```
So while `firstEvent` changes from1 to 21, `skipEvents` stays at 0.

Changing `skipEvents = cms.untracked.uint32(0)`  to  `skipEvents = cms.untracked.uint32(21)` the processed events become different as expected.

This behavior of `cmsRun` is consistend with [CRAB3AdvancedTopic#job_splitting_on_LHE_files](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3AdvancedTopic#job_splitting_on_LHE_files) twiki page, but apparently something changed inside CRAB since that was written (in 2015) and the tool behavior is no longer consistent.

I thought of blaming #7349, but the first problem report is from one year before we made that change ! And in any case that only applies for `Analysis` job type, this is `PrivateMC`.

I have to wonder if this goes back to when I rewrote PSet tweaking for python3 compatibility using `edm_pset_tweak.py` but at first sight older code saved in https://github.com/dmwm/CRABServer/blob/master/scripts/TweakPSetOLD.py does not manipulate `skipEvents` either

## Comment (belforte, 2025-01-29T22:38:06Z)

so far I have no clue how this could have ever worked, other then using one different input file in each job. I looked at "ancient" versions of TweakPSet and there's no sign of manipulation of skipEvents

## Comment (belforte, 2025-02-03T22:31:24Z)

I suspect that even if TweadPSetOld did not touch skipEvents, it was handing all tweaking via WMCore RunTime where skipEvents is set based on firstEvent
https://github.com/dmwm/WMCore/blob/d48389c0793abbf376b99a8a1e147e576948452c/src/python/PSetTweaks/WMTweak.py#L465-L469
i.e.
```python
    firstEvent = mask['FirstEvent']
    if firstEvent != None and firstEvent >= 0 and (len(primaryFiles) > 0 or lheInput):
        if lheInput:
            logging.info("Setting 'skipEvents' attr to: %s", firstEvent - 1)
            result.addParameter("process.source.skipEvents", "customTypeCms.untracked.uint32(%s)" % (firstEvent - 1))
```

If I am correct, the bug was indeed introduced with the rewrite for decoupling from WMCore and python3 compatibility in 3f63696b6d33f4110a8225540204c8d22515389f i.e. Summer 2021
Which is alas consistent with the first user problem report in November 2021 (link to cms-talk in initial comment)

Well.. should be easy to fix !
