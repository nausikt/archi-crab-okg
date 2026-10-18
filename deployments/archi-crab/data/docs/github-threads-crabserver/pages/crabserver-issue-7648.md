# dmwm/CRABServer issue #7648: The PSet tweaking sometimes breaks

State: closed
Opened: 2023-05-30T12:19:01Z
Closed: 2023-06-01T08:57:19Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7648

## Opening post (mapellidario, 2023-05-30T12:19:01Z)

As reported by a user [1], the pset tweaking sometimes breaks [2].

It seems that there is a mismatch between the variable type that we set (int) and the one that david scripts use (uint) [3].

It is not clear to me why this has not been noticed before, unfortunately i do not have time to look at it today, so i will not self-assign this issue to me. I can have a look tomorrow.

---

[1] https://cms-talk.web.cern.ch/t/crab-tasks-failing-with-error-code-10040/24805/2
[2] 

- https://cmsweb.cern.ch/crabserver/ui/task/230529_084643%3Afiorendi_crab_Staus_M_100_100mm_13p6TeV_Run3Winter23DR
- https://cmsweb.cern.ch/crabserver/ui/task/230530_113400%3Afiorendi_crab_Staus_M_100_1000mm_13p6TeV_Run3Winter23DR_trialEventsBased

[3]

<details>

see

```plaintext
Set attribute process.maxEvents.input to cms.untracked.int32(-1)
Set attribute process.maxSecondsUntilRampdown.input to cms.untracked.int32(-1)
will execute: cmssw_handle_random_seeds.py --input_pkl PSet.pkl --output_pkl PSet.pkl-seeds --seeding dummy
Populared random numbers of RandomNumberService
will execute: cmssw_handle_nEvents.py --input_pkl PSet.pkl --output_pkl PSet.pkl-nEvents
Traceback (most recent call last):
  File "/cvmfs/cms.cern.ch/share/overrides/bin/cmssw_handle_nEvents.py", line 41, in <module>
    main()
  File "/cvmfs/cms.cern.ch/share/overrides/bin/cmssw_handle_nEvents.py", line 39, in main
    do_loop(args, handle_nEvents)
  File "/cvmfs/cms.cern.ch/share/overrides/bin/../python/tweak_program_helpers.py", line 43, in do_loop
    process = func(process, args)
  File "/cvmfs/cms.cern.ch/share/overrides/bin/cmssw_handle_nEvents.py", line 28, in handle_nEvents
    getattr(process, producer).nEvents = process.maxEvents.input.value()
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_6_4/src/FWCore/ParameterSet/python/Mixins.py", line 282, in __setattr__
    self.__dict__[name].setValue(value)
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_6_4/src/FWCore/ParameterSet/python/Mixins.py", line 100, in setValue
    raise ValueError(str(value)+" is not a valid "+str(type(self)))
ValueError: -1 is not a valid <class 'FWCore.ParameterSet.Types.uint32'>
```

</details>

## Comment (belforte, 2023-05-30T15:02:13Z)

yeah, the error appears clear and trivial, but things should have been failing since 2 years !
Also CMSSW_12_6_4 is one of those which we test in Jenkins.

## Comment (belforte, 2023-05-31T08:15:07Z)

code on our side has not changed, the `int32` vs `uint32` bug has been there since we moved to new tweaking based on edm_pset_tweak
I am quite puzzled

## Comment (mapellidario, 2023-05-31T13:45:29Z)

I am running the job locally with preparelocal.

Using uint32 and maxEvents=0 at [1] and similar lines makes the PSet tweak be ok, but then the cmsRun execution fails [2].

Since I submitted a very similar task (filebased splitting, same cmssw version, same scram arch) [3] and evth seems ok, I start suspecting that something is wrong or unexpected with the user pset.

[1] https://github.com/dmwm/CRABServer/blob/a3467228257b94d7c5e21f40b7092758b022c8f4/scripts/TweakPSet.py#L185

[2]

```plaintext
==== Tweak PSet at Wed May 31 13:29:57 2023 ====
[...]
        Exit Status: 0
[...]
        Stderr: None
==== Tweak PSet Done at Wed May 31 13:30:02 2023 ====
[...]
======== CMSSW OUTPUT STARTING ========
NOTICE: lines longer than 3000 characters will be truncated
== CMSSW:
== CMSSW:         Scram Command Diagnostic:
== CMSSW:         Command : scramv1
== CMSSW:         Architecture: slc7_amd64_gcc10
== CMSSW:         Executed: cmsRun -p PSet.py -j FrameworkJobReport.xml
== CMSSW:         Exit Status: 5
== CMSSW:         Stdout: ----- Begin Fatal Exception 31-May-2023 15:30:03 CEST-----------------------
== CMSSW: An exception of category 'Configuration' occurred while
== CMSSW:    [0] Constructing the EventProcessor
== CMSSW:    [1] Validating top level 'maxEvents' ParameterSet for process 'SIM'
== CMSSW: Exception Message:
== CMSSW: Parameter "input" should be defined as an untracked int32.
== CMSSW: The type in the configuration is incorrect.
== CMSSW: ----- End Fatal Exception -------------------------------------------------
== CMSSW:
== CMSSW:         Stderr: None
======== CMSSW OUTPUT FINSHING ========
```

[3] https://cmsweb.cern.ch/crabserver/ui/task/230531_110409%3Admapelli_crab_pset_20230531_130408

## Comment (sarafiorendi, 2023-05-31T14:18:22Z)

hi, 
if I may comment, in my pSet I have
```
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
```
In this way the job runs locally. 
If I change it to uint32 as you did 
```
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.uint32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)
```
and run it I get the same error that you get in [2]
```
An exception of category 'Configuration' occurred while
   [0] Constructing the EventProcessor
   [1] Validating top level 'maxEvents' ParameterSet for process 'SIM'
Exception Message:
Parameter "input" should be defined as an untracked int32.
The type in the configuration is incorrect.
```

So it is "expected" that the job does not run with uint32.
I also checked how was the same parameter defined in CMSSW_12_4_11 (where the task could finish successfully) and it was int32 as well.
Sorry if I'm misunderstanding your comment above.

## Comment (mapellidario, 2023-05-31T14:57:59Z)

@sarafiorendi Could you please try change your pset in the following way?

```diff
process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('SMS-TStauStau-MM_mStau-100_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
-   nEvents = cms.untracked.uint32(100),
+   nEvents = cms.untracked.int32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
```

From a quick test [1], this makes the pset tweak happy (in my case the cmsRun execution fails because i did not copy entirely your sandbox, but i do not think this is relevant)

[1] https://cmsweb.cern.ch/crabserver/ui/task/230531_145044%3Admapelli_crab_pset_20230531_165042

## Comment (belforte, 2023-05-31T15:20:24Z)

something like "`edm_pset_tweak` could not change the value of nEvents because the input was the wrong type, not the new value" ? Dario, since you could reproduce with preparelocal, maybe you can go the extra mile and debug what's happening inside `/cvmfs/cms.cern.ch/share/overrides/bin/cmssw_handle_nEvents.py` ?

## Comment (sarafiorendi, 2023-06-01T08:36:03Z)

I understood the problem, and it's the wrong combination of the crab cfg and the pSet I wanted to run: using the appropriate pSet (which does not re-run process.externalLHEProducer or generator) everything works perfectly. 
I'm sorry for wasting your time.

## Comment (mapellidario, 2023-06-01T08:57:19Z)

Good! I am glad you found the solution, I am sorry we could not be of too much support. 

I am closing this issue, since I think that the mix of data types between our code and cmssw-wm-tools arises when only the user pset have something "unexpected". Maybe we can add some warnings in crab client, but that's something for another day.

Thank you Sara for you patience, thank you Stefano for having a look.

## Comment (belforte, 2023-06-01T10:00:20Z)

I believe that the problem orginates in running an Analysis task with a PSet which contains modules meant for MC production (GEN step)

I opened a new GH issue to follow up on a fix #7650
