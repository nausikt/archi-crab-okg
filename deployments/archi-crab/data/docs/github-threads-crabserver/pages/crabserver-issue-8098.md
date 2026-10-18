# dmwm/CRABServer issue #8098: add support for `SCRAM_ARCH=el9...`

State: closed
Opened: 2023-12-14T13:39:10Z
Closed: 2024-02-14T07:48:52Z
Labels: Type: Enhancement, Type: Support, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8098

## Opening post (belforte, 2023-12-14T13:39:10Z)

With reference to
https://cms-talk.web.cern.ch/t/jobs-failing-with-exit-code-10040/32699
and
https://cms-talk.web.cern.ch/t/crab-announcement/32724

currenly submission with `SCRAM_ARCH=el9...`  is broken.

It seems natural that some users may want to use el9 builds, it is not validated for Physics, but I understand from Matti that all recent releases are built for that as well, and with CERN now having `el9` as default for `lxplus` and `lxbatch` people may prefer to build their private executable for that OS.

Currently jobs submitted with `el9` SCRAM_ARCH have in their JDL `+REQUIRED_OS=Any` which makes them run in the default glideInWMS container which is `rhel7`.

The best solution looks to me to add the correct ARCH to OS mapping in WMCore, in:
https://github.com/dmwm/WMCore/blob/87ea437f508308b5e1d544a234a80e2a9911d5c1/src/python/WMCore/WMRuntime/Tools/Scram.py#L43-L46

which is used by CRAB in
https://github.com/dmwm/CRABServer/blob/94a11eb7bf795a1f344efb64fe0cea7c960386ff/src/python/TaskWorker/Actions/DagmanCreator.py#L524-L526

What do yoy think @amaltaro @mmascher @smuzaffar ?

FYI @mapellidario

## Comment (belforte, 2023-12-14T15:18:48Z)

I think that maybe there was a good reason in the past, pre-singularity era, for falling back to `"any"` in case `ARCH_TO_OS` returns nothing. But I suspect that now we should better raise a NotSupported exception ! What's the view from SI/CMSSW side ? Can we expect that for every scram arch there is a well defined container to be use

That will at least give clear and immediate feedback to users in this and possibly future cases.

## Comment (mapellidario, 2023-12-14T15:18:53Z)

I had a chat with @mmascher during the latest O&C week. Apart from changing WMCore arch to os mapping, the only missing piece that I could find was in the frontend configuration. Even if we specify the proper classads, the frontend is not equipped yet to spawn an el9 container on the WN. Marco said it should not be a big change, just a simple change in the config, but the priority felt low and I forgot to follow up.

## Comment (belforte, 2023-12-14T15:19:39Z)

I am happy to say that we do no support `el9` until `SI` does !

## Comment (belforte, 2023-12-14T15:20:18Z)

let's add the exception then

## Comment (smuzaffar, 2023-12-15T16:29:55Z)

@belforte 
> It seems natural that some users may want to use el9 builds, it is not validated for Physics, but I understand from Matti that all recent releases are built for that as well, and with CERN now having el9 as default for lxplus and lxbatch people may prefer to build their private executable for that OS.

I do not think that user ( who mostly have complained about this issue)  want to build/test for el9. They just follow the instructions which starts with `login to lxplus`. This had worked till 7th of Dec as lxplus was `CentOS7`  which is one of our production/validation arch. Now `lxplus` is `el9` and though we are building for `el9` but it is not validation yet.

> Can we expect that for every scram arch there is a well defined container to be use

Yes, for all enterprise linux based archs we have well defined container. For every SCRAM_ARCH there is `cmssw/rhelN` container ( available under /cvmfs/singularity.opensciencegrid.org/cmssw).

## Comment (belforte, 2023-12-18T13:34:31Z)

Thanks @smuzaffar , yes. I understand that. CMSSW users should stick with validated releases.
I am not advocating for that. But some users may find it useful to have el9 custom applications so that they can run on lxplus, lxbatch and grid too. All I am saying is that it would be good to add an entry to
ARCH_TO_OS mapping

## Comment (belforte, 2024-02-01T15:50:55Z)

@mmascher reported that EL9 container is now available from the factory.
We should test this and then update ARCH_TO_OS  mapping.

## Comment (belforte, 2024-02-12T21:37:39Z)

no change to CRAB code is required. In order to test we only need to edit https://github.com/dmwm/WMCore/blob/87ea437f508308b5e1d544a234a80e2a9911d5c1/src/python/WMCore/WMRuntime/Tools/Scram.py#L43-L46 in the TW container

## Comment (belforte, 2024-02-12T22:13:26Z)

testing on crab-dev-tw01
so far so good. Submitted from `SCRAM_ARCH=el9_amd64_gcc11`
job is running with new required OS
```
[crabtw@vocms059 SPOOL_DIR]$ condor_q 9507614


-- Schedd: crab3@vocms059.cern.ch : <188.184.103.189:4080?... @ 02/12/24 23:11:59
 ID         OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD
9507614.0   crabtw          2/12 23:07   0+00:01:52 R  10   0.0 gWMS-CMSRunAnalysis.sh -a sandbox.tar.gz --sourceUR

Total for query: 1 jobs; 0 completed, 0 removed, 0 idle, 1 running, 0 held, 0 suspended 
Total for all users: 38 jobs; 1 completed, 0 removed, 0 idle, 36 running, 1 held, 0 suspended

[crabtw@vocms059 SPOOL_DIR]$ condor_q 9507614 -af required_os
rhel9
[crabtw@vocms059 SPOOL_DIR]$ 

```

and in the job stdout
```
== ENV: GWMS_SINGULARITY_IMAGE_HUMAN=/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel9-x86_64
== ENV: SCRAM_ARCH=el9_amd64_gcc11
```

In other words, it works.

## Comment (belforte, 2024-02-12T22:22:55Z)

I will make a PR for WMCore

## Comment (belforte, 2024-02-13T09:38:39Z)

moved to https://github.com/dmwm/WMCore/issues/11895

## Comment (belforte, 2024-02-13T17:36:32Z)

Here's the PR in WMCore: https://github.com/dmwm/WMCore/issues/11895
keep this open in Hold until that's merged, so we remember to ping if it does not happen

## Comment (belforte, 2024-02-14T07:48:45Z)

WMCore PR was merged. Closing
