# dmwm/CRABServer issue #7208: Support jobs on non-x86 architectures

State: closed
Opened: 2022-04-08T15:03:22Z
Closed: 2023-09-12T16:10:13Z
Labels: Type: Enhancement, Priority: High, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7208

## Opening post (mapellidario, 2022-04-08T15:03:22Z)

We want CRAB to support jobs running on non-x86 architecture, i.e. PPC or ARM.

At the moment there is not any non-x86 machine in the global pool [1], but they may be added in the future and we want to be prepared, with a solid understanding on how the arch is selected.

#### step 1: run jobs on arm64 when the user request it

If I understood correctly, the desired process needs to be

1. the user sets `$SCRAM_ARCH` in his env. crab client passes it to the crabserver when the user run `crab submit`.
2. TW uses the value of `$SCRAM_ARCH` to set "+DESIRED_Archs" in the JDL.
3. during the matchmaking, condor uses "+DESIRED_Archs" to match the "arch" classad advertised by the pilot.

Maybe we also need to set `+TARGET_Arch` in the JDL, but we do not think it will be necessary.

We should already have 1. and 3. in place. From a quick look at the code, it seems that we can achieve 2. simply improving [2], maybe with a mapping in common with WMCore, with an approach similar to https://github.com/dmwm/CRABServer/pull/7191, but I may be wrong.

#### step 2: allow to run a job on multiple architecture

We are still not sure if this will ever be required.

This would be similar in spirit to https://github.com/dmwm/WMCore/pull/11228.

However, CRAB does things a bit differently that WMCore and we still have some open questions.

For example, we currently take the scram_arch from the environment that the user submitted the task from. Under what circumstances we can widen it? For example, a user submits a simple task from x86 lxplus. When is the code that the user need to run allowed to run on arm as well?
Should we detect it somehow (hard) or should the user explicitly allow his code to run on arm as well with a new crab  client option?

Any comment, improvement, further explanation is very welcomed! :)

#### further references:

- https://github.com/dmwm/WMCore/issues/11401

---

[1]. The pilots publish the architecture of the site in which they landed with the "arch" classad. at the moment only `X86_64` is present

```plaintext
# 2022-04-08, ~16.00 cern time
> condor_status -pool vocms0814.cern.ch -af arch | sort | uniq -c
 154675 X86_64
```

[2]


https://github.com/dmwm/CRABServer/blob/01c1bdd55853164a55a669cfa581212d17cf5682/src/python/TaskWorker/Actions/DagmanCreator.py#L364-L372

## Comment (belforte, 2022-08-13T11:10:26Z)

will be a byproduct of https://github.com/dmwm/CRABServer/issues/7084

## Comment (mapellidario, 2022-12-13T11:03:16Z)

From a [discussion](https://mattermost.web.cern.ch/cms-o-and-c/pl/gqrckwuo53y7dfk8jpk4x64jza) on cern mattermost 

> REQUIRED_ARCH is something CRAB should set. Can be a comma separated list of architectures (including "any" if the job can run on any architecture)

I must admit that I am a bit confused. We have `REQUIRED_ARCH`, `TARGET.ARCH`, [desired_arch](https://github.com/dmwm/CRABServer/blob/452dc411e5c279a72d8129ca5692d00d331b0a7e/src/python/TaskWorker/Actions/DagmanCreator.py#L369) and [DESIRED_Archs](https://github.com/dmwm/CRABServer/blob/452dc411e5c279a72d8129ca5692d00d331b0a7e/src/python/TaskWorker/Actions/DagmanCreator.py#L116) and it is not clear to me which variable is used for what and if we can deprecate some of them. For example, I only find "old" references to `DESIRED_Archs` in WMCore, maybe we can stop using it in CRAB as well.

@mmascher Would you have any suggestion and up-to-date reference?

## Comment (mapellidario, 2022-12-13T11:09:20Z)

Moreover, Marco gave us some instructions on how to submit jobs on arm arch (same discussion on mattermost linked above): 

- crab config:

    ```plaintext
    config.Debug.scheddName = 'crab3@vocms069.cern.ch'
    config.Debug.collector = 'cmsgwms-collector-itb.cern.ch'
    config.Debug.extraJDL = ['+REQUIRED_ARCH="aarch64"', '+requirements=TARGET.ARCH=="aarch64"']
    ```

- For submission he used an ARM node at lxplus, by ssh-ing to lxplus8-arm.cern.ch 
- He used `CMSSW_12_5_2` for `el8_aarch64_gcc10`. ("I picked a recent CMSSW version and one of the aarch64 scram arch")

## Comment (mmascher, 2022-12-15T14:33:39Z)

> From a [discussion](https://mattermost.web.cern.ch/cms-o-and-c/pl/gqrckwuo53y7dfk8jpk4x64jza) on cern mattermost
> 
> > REQUIRED_ARCH is something CRAB should set. Can be a comma separated list of architectures (including "any" if the job can run on any architecture)
> 
> I must admit that I am a bit confused. We have `REQUIRED_ARCH`, `TARGET.ARCH`, [desired_arch](https://github.com/dmwm/CRABServer/blob/452dc411e5c279a72d8129ca5692d00d331b0a7e/src/python/TaskWorker/Actions/DagmanCreator.py#L369) and [DESIRED_Archs](https://github.com/dmwm/CRABServer/blob/452dc411e5c279a72d8129ca5692d00d331b0a7e/src/python/TaskWorker/Actions/DagmanCreator.py#L116) and it is not clear to me which variable is used for what and if we can deprecate some of them. For example, I only find "old" references to `DESIRED_Archs` in WMCore, maybe we can stop using it in CRAB as well.
> 
> @mmascher Would you have any suggestion and up-to-date reference?

@mapellidario I was not actually aware of [this](https://github.com/dmwm/CRABServer/blob/452dc411e5c279a72d8129ca5692d00d331b0a7e/src/python/TaskWorker/Actions/DagmanCreator.py#L115) twiki. I think it is something Brian put initially in, but then it was forgotten. [Here](https://docs.google.com/document/d/1d2fLLmMs09pv0zveVu97tieD3FTYXaWcDqGcnBhYu7k/edit#) is a google doc we used to collect thoughs in SI. I picked REQUIRED_ARCH because we already have REQUIRED_OS.

Do you guys know if DESIRED_Arch is used anywhere in the monitoring?

## Comment (mapellidario, 2023-06-02T16:10:01Z)

As Stefano suggested, I exported a different SCRAM_ARCH after `cmsenv`. This does not break `crab submit` and I was able to submit a task [0] :)

Using the code from [1] on `test11`, I was able to set what I think are the required classads [2] to run the jobs on ppc.

Now we need to make sure that the pilots at cineca are started. If the jobs are not started during the weekend, then on monday I will seek guidance from Daniele Spiga and Marco Mascheroni.

---

[0] https://cmsweb-test11.cern.ch/crabserver/ui/task/230602_151033%3Admapelli_crab_test_20230602_171032
[1] https://github.com/dmwm/CRABServer/compare/master...mapellidario:20221206_jobwrarch_0
[2]

From lxplus8, I run `cmsenv` to source

```
SCRAM_ARCH : el8_amd64_gcc10
CMSSW_VERSION : CMSSW_12_6_0
```

then i changed scram_arch with `export SCRAM_ARCH=el8_ppc64le_gcc10`, then I run `crab submit` of a simple HC analysis task. The resulting jobs have the following classads:

```plaintext
CRAB_JobSW = "CMSSW_12_6_0"
CRAB_JobArch = "el8_ppc64le_gcc10"
REQUIRED_ARCH = "ppc64le"
REQUIRED_OS = "rhel8"
Requirements = (stringListMember(TARGET.Arch,REQUIRED_ARCH)) && (TARGET.OpSys == "LINUX") && (TARGET.Disk >= RequestDisk) && (TARGET.Memory >= RequestMemory) && (TARGET.HasFileTransfer)
```

## Comment (mapellidario, 2023-06-02T16:34:35Z)

There is an alternative, which is using the `qemu` emulator, it looks promising, but I have not managed to solve all the quirks yet.

Open a shell on lxplus, make sure you use bash. Clone this repo https://github.com/cms-sw/cms-bot and cd into it.

```plaintext
[dmapelli@lxplus901 cms-bot]$ export SCRAM_ARCH=el9_aarch64_gcc11
[dmapelli@lxplus901 cms-bot]$ source ./dockerrun.sh
[dmapelli@lxplus901 cms-bot]$ dockerrun bash
[..., ignoring some errors...]
[I have no name!@lxplus901 cms-bot]$ 
```

then make sure that you can read from cvmfs with `ls /cvmfs/cms.cern.ch`, then you can

```
scram list CMSSW
cmsrel CMSSW_13_1_0
cd CMSSW_13_1_0
cmsenv
crab submit --proxy=$X509_USER_PROXY -c ppc-crab.py
```

at the moment crab submit fails because it can not read the certificate directory

```plaintext
ERROR: Exception: The X509_CERT_DIR variable is not set and the /etc/grid-security/certificates/ directory cannot be found.
Cannot find the CA certificate path to authenticate the server.
```

I can not see that directory indeed from inside qemu, despite I see it from a plain lxplus shell. 

```
[I have no name!@lxplus901 0-dev]$ ls /etc/grid-security/
qemu: Unsupported syscall: 293
qemu: Unsupported syscall: 291
gsi.conf  vomsdir
```

I guess that there is a way around it, I will have a look in the next days.

## Comment (belforte, 2023-06-02T18:46:11Z)

you may need to bind mount /etc/grid-security from the host into the container.

## Comment (belforte, 2023-06-02T18:52:26Z)

this may actually be enough:
```
export X509_CERT_DIR=/cvmfs/grid.cern.ch/etc/grid-security/certificates
```
of course it is easier to use `voms-proxy-info` instead of `crab submit` to verify correct env. for X509 stuff

## Comment (belforte, 2023-08-17T10:39:34Z)

@mapellidario where are we on this? I think it was completed waiting for some ARM grid node where to test. If that's the case we could close and open new ones according to which problems (if any) appears

## Comment (mapellidario, 2023-09-12T16:10:13Z)

yes, we did all we could so far, now we need some non-x86 resources to test the TW and the job wrapper. I agree about closing this issue
