# dmwm/CRABServer pull request #9258: rename submission classads CUDA* to new HTCondor vendor agnostic, DESIRED_GPU*, refactored acceleratedParams interface.

State: closed
Opened: 2026-01-15T20:16:15Z
Closed: 2026-01-22T10:01:02Z
Merged: 2026-01-22T10:01:02Z
URL: https://github.com/dmwm/CRABServer/pull/9258

## Opening post (nausikt, 2026-01-15T20:16:15Z)

Resolve #9215

I've tested GPU tasks submission via test14 as you can see [here](https://cmsweb-test14.cern.ch/crabserver/ui/task/260115_192827%3Akphornsi_crab_test_CMSSW_15_2026_new_GPUs_classads_2). 

All tasks was assigned to GPUs slot and met our requirements well [1], also the last mile ***Requirements expression & Attrs*** were set as expected [2]

The ***acceleratorParams*** interface will looks as follows: 
```python
config.Site.requireAccelerator = True
config.Site.acceleratorParams = {
        "GPUMemoryMB": "4000",
        "GPUMinimumCapability": "7.0",
        "GPUMaximumCapability": "8.0",
        "GPURuntime": "7.0",
}
```

[1] Example event logs show 2 jobs executed on `JOBGLIDEIN_CMSSite=T2_US_Purdue` and `T1_DE_KIT`, using distinct GPU models and CUDA capabilities: **Tesla T4 (capability 7.5)** and **NVIDIA A100-SXM4-40GB (capability 8.0)**, respectively. 
```
JOBGLIDEIN_CMSSite = "T2_US_Purdue"
SlotName: slot1_1@hammer-f000.rcac.purdue.edu
	AvailableGPUs = { GPUs_GPU_fd425f30 }
	CondorScratchDir = "/tmp/glide_WRNnlm/execute/dir_2387845"
	Cpus = 1
	Disk = 101679
	GPUs = 1
	GPUs_GPU_fd425f30 = [ Id = "GPU-fd425f30"; ClockMhz = 1590.0; Capability = 7.5; CoresPerCU = 64; DeviceName = "Tesla T4"; DeviceUuid = "fd425f30-3936-73ad-2528-bd8348d2f942"; ECCEnabled = true; ComputeUnits = 40; DriverVersion = 13.0; DevicePciBusId = "0000:E2:00.0"; GlobalMemoryMb = 14913; MaxSupportedVersion = 13000 ]
	Memory = 2048
....
JOBGLIDEIN_CMSSite = "T1_DE_KIT"
SlotName: slot1_1@hkn0728.localdomain
	AvailableGPUs = { GPUs_GPU_3a702310 }
	CondorScratchDir = "/srv/glide_jeGxkQ/execute/dir_30186"
	Cpus = 1
	Disk = 101376
	GPUs = 1
	GPUs_GPU_3a702310 = [ Id = "GPU-3a702310"; ClockMhz = 1410.0; Capability = 8.0; CoresPerCU = 64; DeviceName = "NVIDIA A100-SXM4-40GB"; DeviceUuid = "3a702310-f70f-9000-8f8f-845187178633"; ECCEnabled = true; ComputeUnits = 108; DriverVersion = 12.8; DevicePciBusId = "0000:CA:00.0"; GlobalMemoryMb = 40442; MaxSupportedVersion = 12080 ]
	Memory = 2048
```

[2] Full log, `condor_q --better-analyze 10329198.0`, Note that `GPUsMinRuntime` was set to 7000 which came from <major_version>*1000 + <minor_version>*10, in our case `7.0` fit 7000 well, See also [HTCondor condor_submit doc](https://htcondor.readthedocs.io/en/24.x/man-pages/condor_submit.html#gpus_minimum_runtime).
```
The Requirements expression for job 10329198.000 is

    (stringListMember(TARGET.Arch,REQUIRED_ARCH)) && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) &&
    (countMatches(MY.RequireGPUs,TARGET.AvailableGPUs) >= RequestGPUs) && (TARGET.HasFileTransfer)

    [0]    : stringListMember(TARGET.Arch,REQUIRED_ARCH)
    [1]    : TARGET.OpSys == "LINUX"
    [2]    : [0] && [1]
    [3]    : TARGET.Disk >= RequestDisk
    [4]    : [2] && [3]
    [5]    : TARGET.Memory >= RequestMemory
    [6]    : [4] && [5]
    [7]    : countMatches(MY.RequireGPUs,TARGET.AvailableGPUs) >= RequestGPUs
    [8]    : [6] && [7]
    [9]    : TARGET.HasFileTransfer
    [10]   : [8] && [9]

Job 10329198.000 defines the following attributes:

    GPUsMaxCapability = 8.0
    GPUsMinCapability = 7.0
    GPUsMinMemory = 4000
    GPUsMinRuntime = 7000
    RequestDisk = 100000 (kb)
    RequestGPUs = 1
    RequestMemory = 2000 (mb)
    REQUIRED_ARCH = "X86_64"
    RequireGPUs = Capability >= GPUsMinCapability && Capability <= GPUsMaxCapability && GlobalMemoryMb >= GPUsMinMemory && MaxSupportedVersion >= GPUsMinRuntime

The Requirements expression for job 10329198.000 reduces to these conditions:

         Slots      If
Step   Matched   Drained  Condition
----- --------- --------- ---------
[0]       53578        56  stringListMember(TARGET.Arch,REQUIRED_ARCH)
[1]       53578        56  TARGET.OpSys == "LINUX"
[3]       53577        56  TARGET.Disk >= RequestDisk
[5]       43795        56  TARGET.Memory >= RequestMemory
[7]           8        56  countMatches(MY.RequireGPUs,TARGET.AvailableGPUs) >= RequestGPUs


10329198.000:  Run analysis summary ignoring user priority.  Of 53578 slots on 6535 machines,
  53514 slots are rejected by your job's requirements
      0 slots reject your job because of their own requirements
      8 slots match and are willing to run your job
     56 slots would match if drained


10329198.000:  Job is completed.

Last successful match: Thu Jan 15 20:38:50 2026
Last successful match for this autocluster: Thu Jan 15 20:38:50 2026
This autocluster currently has 0 running and 1 completed jobs.
```

*P.S. twiki CRAB config params docs has not been updated yet, let me get it done asap after we settled on this interface.*

## Comment (cmsdmwmbot, 2026-01-15T20:20:42Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 164 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2715/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-01-21T17:56:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 164 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2723/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-01-21T18:01:55Z)

> looks good to me, with just one worry. Are you sure that it is OK to set one of those attributes as `classad.undefined` vs. simply avoid listing it in the JDL ? HTCondor documentation says nothing about this.

Thank you so much for careful review, Good catch!, indeed `classad.undefined` doesn't exist [1]. Originally i try to copying Kenyi's style for (IMO) more clarity in-line style setting, but its turn out he has [local `undefined` var in fn scope](https://github.com/khurtado/WMCore/blob/7d6e7d5f460d2e4eb34f99846d706a1da2e2aa8e/src/python/WMCore/BossAir/Plugins/SimpleCondorPlugin.py#L504) (i presume it belongs to classad somehow). Sorry about that, i've fixed it please review it once again.
[1]
```
>>> import classad2 as classad
>>> classad.undefined
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'classad2' has no attribute 'undefined'
```

## Comment (belforte, 2026-01-21T22:08:01Z)

Some background:
Kenyi uses dictionaries, even if they are called `ad` to eventually create an htcondor.Submit object. Indeed `'UNDEFINED'` (as a string) is a [special value](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-syntax) for classads. We use classad objects, but they can be defined using dictionary semantics, so we could similarly use `jobSubmit[...]="UNDEFINED"` , i.e. assign to the ad the `"UNDEFINED"` string. But in practice it is the same as not setting any value for this attribute which IMHO is more clear.  Currently we do not set a value (not even UNDEFINED) and it works, this means that all code which deals with this inside Condor and glideInWMS is properly written so not to crash on a missing optional ad, using e.g. the [Ternary operator](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-operators) and/or explicit testing for the ad being defined.
We could also use the python `None` value:  `jobSubmit[...]=None` or the "expert-smelling" `jobSubmit[...]=classad.Value.Undefined` as per https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/version2/classad2/classad.html#classad2.ClassAd

That said, whether to use one way or another, is mostly a matter of taste !
But you should have tested the new code also on a configuration that does not specify the new accelerator params !

## Comment (cmsdmwmbot, 2026-01-22T09:34:08Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 165 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2724/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-01-22T09:55:58Z)

> Some background: Kenyi uses dictionaries, even if they are called `ad` to eventually create an htcondor.Submit object. Indeed `'UNDEFINED'` (as a string) is a [special value](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-syntax) for classads. We use classad objects, but they can be defined using dictionary semantics, so we could similarly use `jobSubmit[...]="UNDEFINED"` , i.e. assign to the ad the `"UNDEFINED"` string. But in practice it is the same as not setting any value for this attribute which IMHO is more clear. Currently we do not set a value (not even UNDEFINED) and it works, this means that all code which deals with this inside Condor and glideInWMS is properly written so not to crash on a missing optional ad, using e.g. the [Ternary operator](https://htcondor.readthedocs.io/en/latest/classads/classad-mechanism.html#classad-operators) and/or explicit testing for the ad being defined. We could also use the python `None` value: `jobSubmit[...]=None` or the "expert-smelling" `jobSubmit[...]=classad.Value.Undefined` as per https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/version2/classad2/classad.html#classad2.ClassAd
> 

Thanks for the rationales! Especially `TernaryOperator`, demystifying the middleware. 

I've tested the happy path (all was specified) [1], some accelerateParams was specified path [2], non were specified path [3]. The `RequireGPUs` expression varied as we expected.

[1] All GPU* requirements were specified, [260122_093806:kphornsi_crab_test_CMSSW_15_2026_test14_GPU_all_listed_happy_path](https://cmsweb-test14.cern.ch/crabserver/ui/task/260122_093806%3Akphornsi_crab_test_CMSSW_15_2026_test14_GPU_all_listed_happy_path)
```bash
Job 101428872.000 defines the following attributes:

    GPUsMaxCapability = 8.0
    GPUsMinCapability = 7.0
    GPUsMinMemory = 4000
    GPUsMinRuntime = 7000
    ...
    RequireGPUs = Capability >= GPUsMinCapability && Capability <= GPUsMaxCapability && GlobalMemoryMb >= GPUsMinMemory && MaxSupportedVersion >= GPUsMinRuntime

The Requirements expression for job 101428872.000 reduces to these conditions:

        Slots
Step   Matched  Condition
----- --------- ---------
...
[7]          16  countMatches(MY.RequireGPUs,TARGET.AvailableGPUs) >= RequestGPUs

101428872.000:  Run analysis summary ignoring user priority.  Of 52812 slots on 6757 machines,
  52796 slots are rejected by your job's requirements
      0 slots reject your job because of their own requirements
     16 slots match and are willing to run your job
```

[2] Some were specified, `"GPUMinimumCapability": "7.0"` 
[260122_093856:kphornsi_crab_test_CMSSW_15_2026_test14_GPU_some_have_been_listed](https://cmsweb-test14.cern.ch/crabserver/ui/task/260122_093856%3Akphornsi_crab_test_CMSSW_15_2026_test14_GPU_some_have_been_listed)
```bash
Job 140326970.000 defines the following attributes:

    GPUsMinCapability = 7.0
    ...
    RequireGPUs = Capability >= GPUsMinCapability

The Requirements expression for job 140326970.000 reduces to these conditions:

        Slots
Step   Matched  Condition
----- --------- ---------
...
[7]           2  countMatches(MY.RequireGPUs,TARGET.AvailableGPUs) >= RequestGPUs


140326970.000:  Run analysis summary ignoring user priority.  Of 53852 slots on 6779 machines,
  53850 slots are rejected by your job's requirements
      0 slots reject your job because of their own requirements
      2 slots match and are willing to run your job

```

[3] Non GPU* specific requirements were listed, but `requireAccelerator=True`.
[260122_093835:kphornsi_crab_test_CMSSW_15_2026_test14_GPU_non_acceleratedParams_listed](https://cmsweb-test14.cern.ch/crabserver/ui/task/260122_093835%3Akphornsi_crab_test_CMSSW_15_2026_test14_GPU_non_acceleratedParams_listed)
```bash
Job 140977015.000 defines the following attributes:

    RequestDisk = 100000 (kb)
    RequestGPUs = 1
    RequestMemory = 2000 (mb)
    REQUIRED_ARCH = "X86_64"

The Requirements expression for job 140977015.000 reduces to these conditions:

         Slots      If
Step   Matched   Drained  Condition
----- --------- --------- ---------
[0]       53519         7  stringListMember(TARGET.Arch,REQUIRED_ARCH)
[1]       53519         7  TARGET.OpSys == "LINUX"
[3]       53514         7  TARGET.Disk >= RequestDisk
[5]       44019         7  TARGET.Memory >= RequestMemory
[7]          28         7  TARGET.GPUs >= RequestGPUs


140977015.000:  Run analysis summary ignoring user priority.  Of 53519 slots on 6782 machines,
  53484 slots are rejected by your job's requirements
      0 slots reject your job because of their own requirements
     28 slots match and are willing to run your job
      7 slots would match if drained
```

## Comment (nausikt, 2026-01-22T11:12:19Z)

I've added doc about `acceleratorParams` in [twiki:CRAB3ConfigurationFile](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile). Please, let me know if it's unclear and not comprehensive enough. Thanks!
