# dmwm/CRABClient issue #5354: CMSSW_15_0 and above: Support for CMSSW x86-64-v3 as default micro-arch 

State: closed
Opened: 2024-11-27T08:02:50Z
Closed: 2024-12-11T16:40:49Z
Labels: enhancement, Done, On Hold
URL: https://github.com/dmwm/CRABClient/issues/5354

## Opening post (smuzaffar, 2024-11-27T08:02:50Z)

Hi,

 We are planning to make `x86-64-v3` as default micro-arch for CMSSW_15_0_X ( see https://github.com/dmwm/WMCore/issues/12168 and [core sw meeting](https://indico.cern.ch/event/1482012/)). Though CMSSW_15_0 will support dual micro-arch stack (`x86-64-v3` and `x86-64-v2`) but `x86-64-v3` will be default. 

  In order to avoid increasing the build time (and also crab sandbox size) in cmssw developer area, scram will only build for default micro-arch ( i.e. `x86-64-v3` ). If someone wants to use a `x86-64-v2` resource (e.g. the dataset they need is only available on site with v2 resources) then they have to explicitly enable dual stack build in their developer area.

  We would suggest that, for CMSSW_15_0_X , crab sumbit jobs to `x86-64-v3` resources by default. SCRAM can set some env variable to expose the available micro-archs support e.g for CMSSW_15_0_X and above

- Normal user dev area: SCRAM can set `CMSSW_MICRO_ARCHS=x86-64-v3` i.e. job should run only on `x86-64-v3`
- Dev area multi-archs enabled:  SCRAM can set `CMSSW_MICRO_ARCHS=x86-64-v3,x86-64-v2` i.e job can use both `v2 and v3` resources
- Dev area with multi-archs enabled but user explicitly want to use `x86-64-v2`: SCRAM can set `CMSSW_MICRO_ARCHS=x86-64-v2`

If `CMSSW_MICRO_ARCHS` env sounds reasonable then we can enable this for 15.0.X IBs but if you have any better solutions which can help crab using the correct resources then please do let me know.

## Comment (belforte, 2024-11-27T09:24:56Z)

from a technical standpoint it will be easy to tune the requirements in grid jobs according to an env. variable.
Very little will have to change in CRABClient.

I rather worry about those datasets only available in v2 available sites. More discussion is needed. Not in this issue though.

## Comment (belforte, 2024-11-27T13:40:53Z)

On Hold waiting for discussion with SI / CMSSW to be finalized.

Need to decide if we want to create another column in DB for the microarchitecture list, or expand current `tm_job_arch` which now contains e.g. `el9_amd64_gcc12` (in case must change also RX_ARCH in Server's CRABInterface/Regexps.py )

## Comment (belforte, 2024-12-04T11:12:47Z)

link to changes needed on Server side: https://github.com/dmwm/CRABServer/issues/8855

## Comment (belforte, 2024-12-05T16:05:06Z)

CRAB Client will need to detect this env. variable ([ref.](https://github.com/dmwm/WMCore/issues/12168#issuecomment-2520351777))
`SCRAM_MIN_SUPPORTED_MICROARCH`
(value is e.g. `x86-64-v3` or `x86-64-v2` etc.)
and pass the information to the server

## Comment (belforte, 2024-12-05T17:30:21Z)

Can avoid creating a new DB column by leveraging the JSON in `tm_user_config`. But still need a new parameter in the submission from client. I do not like abusing SCRAM_ARCH by adding microver and then split it in the REST.

I have entertained the idea in the past to add a free-content JSON to the submission to avoid that the current horrendous list in the submission PUT CALL keeps growing. But it may require to change from params in the URL to a using a BODY and then changes on the REST side which go beyond my skills. And surely beyond current scope.

## Comment (belforte, 2024-12-05T17:36:27Z)

i need to breakdown in steps
- [x] add SCRAM_MIN_SUPPORTED_MICROARCH in [ScramEnvironment.py](https://github.com/dmwm/CRABClient/blob/v3.241125/src/python/CRABClient/JobType/ScramEnvironment.py)
- [x] add to parameters passed to submission in https://github.com/dmwm/CRABClient/blob/da79107c9f00eb1378c7da5ad57f46107f65c8d3/src/python/CRABClient/JobType/Analysis.py#L59-L61
- [x] new submission param will be called `jobminuarch` and defaults to "any" string

Then work is on server side.

## Comment (belforte, 2024-12-06T09:14:54Z)

wait for server changes and testing before closing

## Comment (smuzaffar, 2024-12-06T09:19:18Z)

We need bit more testing for using`v2` resources. I have opened https://github.com/cms-sw/cmsdist/pull/9555 hopeing that it might fix the issue.

Do we have 16 cores resources at T2_LB_HPC4L ? I can directly test the https://github.com/cms-sw/cmsdist/pull/9555 change by rebuilding full cmssw on a 16 core node @ T2_LB_HPC4L

## Comment (belforte, 2024-12-06T11:42:40Z)

@smuzaffar I do not know how to tell if there are 16-core machines with v2 arch which we can target. They do not need to be at T2_LB, you can always add extra requirements  in the submission (not as direct as site name, but possible).  Can you check with SubmissionInfrastructure ?

## Comment (belforte, 2024-12-06T17:37:01Z)

@smuzaffar this may help. YOu can find some 64-core at Nebraska and several 16-core at Vanderbilt

```console
belforte@vocms059/~> condor_status -con 'TotalSlotCPUs==64&&Microarch=="x86_64-v2"' -af GLIDEIN_CMSSite Microarch 
T1_US_FNAL x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
belforte@vocms059/~> condor_status -con 'TotalSlotCPUs==16&&Microarch=="x86_64-v2"' -af GLIDEIN_CMSSite Microarch 
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Nebraska x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
T2_US_Vanderbilt x86_64-v2
belforte@vocms059/~> 

```

## Comment (belforte, 2024-12-06T17:47:05Z)

hmm.. thinking more I do not believe that it is possible to change the current match making requirements, but if you ask for 16-cores at Vanderbilt, it could do, in this very moment those are all v2.
```console
belforte@vocms059/~> condor_status -con 'GLIDEIN_CMSSite=="T2_US_Vanderbilt"&&TotalSlotCPUs==16' -af GLIDEIN_CMSSite Microarch |sort|uniq -c
     51 T2_US_Vanderbilt x86_64-v2
belforte@vocms059/~> 
```
with the added advantage that if you need local help Andrew Melo should be able to give it !

## Comment (belforte, 2024-12-06T17:49:06Z)

Same for T2_US_Nebraska, but it looks they have fewer old machines.

At other sites we likely do not run whole-node pilots and I suspect maximum is 8-core.
