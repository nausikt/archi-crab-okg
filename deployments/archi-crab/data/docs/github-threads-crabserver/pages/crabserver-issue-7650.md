# dmwm/CRABServer issue #7650: PSet tweaking on WN breaks if a MC PSet is used in Analysis task

State: closed
Opened: 2023-06-01T10:04:59Z
Closed: 2023-06-02T14:13:52Z
URL: https://github.com/dmwm/CRABServer/issues/7650

## Opening post (belforte, 2023-06-01T10:04:59Z)

as found after user problem report in #7648 

I believe that the problem orginates in running an Analysis task with a PSet which contains modules meant for MC production (GEN step). For analysis we need maxEvents=-1 to "dummyfy" it so to use runs/lumis instead to decide what to process. But for MC we set it to a positive integer to really mean maxEvents so there is no:
```
ValueError: -1 is not a valid <class 'FWCore.ParameterSet.Types.uint32'>
```

I am not sure how best to prevent this. Maybe CRABClient could refuse to submit if `config.JobType.pluginName = 'Analysis'` but ther PSet contains `process.source = cms.Source("EmptySource")`. 
We could avoid calling `cmssw_handle_nEvents.py` for CRAB tasks which use `Analysis` "plugin" , it looks like it could do [1]
I guess that I am confused because I do not know what a `producer` exactly is in the CMSSW process .

Maybe a quick chat with David Lange will solve all doubs i.e. confirm that we can safely restrict use of  `cmssw_handle_nEvents.py` to MC tasks. @mapellidario you can ask in person which may work better, but if you prefer that I do on MM, let me know

[1]
the PSet after CRAB's tweaking (i.e. before `cmssw_handle_nEvents.py` ) has this interesting piece
```
process.source = cms.Source("EmptySource",
    fileNames = cms.untracked.vstring('/store/group/lpcdisptau/Staus_M_100_100mm_13p6TeV_Run3Winter23/GENSIM/230526_095807/0000/TSG-Run3Winter23GS-LLStau_M100_ctau100mm_1.root'),
    numberEventsInLuminosityBlock = cms.untracked.uint32(100),
    skipEvents = cms.untracked.uint32(0)
)
```
and executing it leads to a reasonably clear error:
```
belforte@lxplus772/Ste> cmsRun tPS.py 
----- Begin Fatal Exception 01-Jun-2023 11:55:58 CEST-----------------------
An exception of category 'Configuration' occurred while
   [0] Constructing the EventProcessor
   [1] Validating configuration of input source of type EmptySource
Exception Message:
Illegal parameters found in configuration.  The parameters are named:
 'fileNames'
 'skipEvents'
You could be trying to use parameter names that are not
allowed for this plugin or they could be misspelled.
----- End Fatal Exception -------------------------------------------------
```

## Comment (davidlange6, 2023-06-01T10:33:12Z)

should not maxEvents be int32? does the traceback say more about which module? The "fun" of that specific  tweak is that to support generators forked by cmsrun - the tweak looks for any producer module with parameter maxEvents and changes its value. (but this is there since many years, its not new in the python2-3 changeover) I can see why that might be hard to support in an arbitrary user PSet. I'm also unsure of a robust fix.

As for input sources.. The tweaking could be changed to check that the input source is not emptySource  before adding parameters (again, this is not new code..) - however, what does "analysis" and "emptysource" together mean as a use case? Maybe that is worth understanding first.

## Comment (belforte, 2023-06-01T10:42:36Z)

@davidlange6 hey ! I did not tag you !! Some AI think notifies you of CRAB issues where your name appears ? I better be careful what I write !

The use case here is "mistake". A bad PSet was fed to a crab task and we got a cryptic (for us) error. The point is how to make it easier for us if it happens again in 1y when we have forgotten everything .

In the end, the problem is that the produces has an `uint32` for `nEvents` while your script tries to insert it a "-1" value from `maxEvents` which is `int32`.

Somehow, both here and in WMAgent, safest thing may be to remove `producer.nEvents`, rather than try to change it, and leave it to CRAB/WMA to set `maxEvents` for the full thing.
(sorry for not using proper terms)

## Comment (davidlange6, 2023-06-01T10:50:28Z)

I got pinged separately:) 

definitely defining analysis as having something other than emptySource would make sense to me (how else are mc and analysis differentiated in their set?)

I'm not sure I follow about nEvents? afaik, this tweak was in wma since a long time. The tweak could be adjusted to do the tweak only if the variable type is int32. That would make it more robust for example.

## Comment (belforte, 2023-06-01T10:50:58Z)

hmm.. I suspect I did not fully appreciate `forked by cmsRun`.
Better solution:
only use  `cmssw_handle_nEvents.py` if `process.maxEvents` is > 0

and leave it to user/developers to deal with improper use of `nEvents` in their producers

## Comment (davidlange6, 2023-06-01T10:52:19Z)

by forked I mean things like to generate events from a grid pack..

## Comment (davidlange6, 2023-06-01T10:52:52Z)

how does one get this pset with nEvents error?

## Comment (belforte, 2023-06-01T11:07:17Z)

> I'm not sure I follow about nEvents? afaik, this tweak was in wma since a long time. The tweak could be adjusted to do the tweak only if the variable type is int32. That would make it more robust for example.

We can't change the `process.maxEvents` to be `int32`, it needs to support `-1` value.
From CRAB side `process.maxEvents` is set to -1 when user declares to CRAB an "analysis" task which will use split by file/run/lumi vs. a "MC" task (i.e. no input) where split is done by events.

I guess that in the end we do NOT have a way to tell if a given producer is correct or not for this configuration. But EDM config. validation is a better place than CRAB job wrapper to figure out that !

## Comment (belforte, 2023-06-01T11:08:32Z)

> how does one get this pset with nEvents error?

https://cmsweb.cern.ch:8443/scheddmon/0144/fiorendi/230529_084643:fiorendi_crab_Staus_M_100_100mm_13p6TeV_Run3Winter23DR/debug/originalPSet.py

this is the part which "can't be tweaked"
```
process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('SMS-TStauStau-MM_mStau-100_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
```

## Comment (belforte, 2023-06-01T12:19:16Z)

if one submits an analysis CRAB task using a Pythia PSet, eventually gets the same configuration error as at the bottom of initial comment, so if we go for the simple fix[*], we simply restore that same behavior also in case the PSet contains a forked producer.

[*] 
```
only use cmssw_handle_nEvents.py in CRAB MC task.
```

Note that it is for user to specify if a task is MC or Analysis. Let's stick to that and not go into trying to decide in the code if the input PSet is one kind or another. A warning in CRABClient could make sense, but on such topic I'd rather let the user shoot himself in the foot and leave people freedom (e.g. if using a script around/instead of cmsRun)

## Comment (davidlange6, 2023-06-01T13:05:50Z)

```
this is the part which "can't be tweaked"

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('SMS-TStauStau-MM_mStau-100_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
```
Ok, so this is forking some generator process, and is one of the expected use cases of this tweak (as I understand it)

If you set nEvent =-1 here then the module will try to run ~forever. It doesn't make sense for this to be -1. I think the conclusion of set properly analysis vs mc is still valid.
