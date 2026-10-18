# dmwm/CRABServer issue #8855: add support for microarchitecture requirement

State: closed
Opened: 2024-12-03T08:42:23Z
Closed: 2024-12-11T17:30:27Z
URL: https://github.com/dmwm/CRABServer/issues/8855

## Opening post (belforte, 2024-12-03T08:42:23Z)

ref: https://github.com/dmwm/WMCore/issues/12168

will need changes to Client as well: https://github.com/dmwm/CRABClient/issues/5354

## Comment (belforte, 2024-12-06T11:45:48Z)

client will have a new `jobminuarch` parameter in submission PUT call
https://github.com/dmwm/CRABServer/blob/35d85e42c2e9f354885f28f9e9819e4d686a022e/src/python/CRABInterface/RESTUserWorkflow.py#L516

action list
- [x] create new column in DB `tm_job_min_microarch` (code)
- [x] modify all existing DB's to add that column
   - [x] dev
   - [x] devtwo
   - [x] devthree
   - [x] devfour
   - [x] preprod
   - [x] prod 
- [x] add `jobminuarch` in RESTUserWorkflow and store in DB in the `tm_job_min_microarch`  column
- [x] use it in DagmanCreator to put correct string in Job.submit file. Ref https://github.com/dmwm/WMCore/issues/12168#issuecomment-2522942038

## Comment (belforte, 2024-12-11T16:01:43Z)

tested on crab-dev-tw01 with a task submitted with `CMSSW_15_0_DEVEL_X_2024-12-05-0900`
https://cmsweb-test2.cern.ch/crabserver/ui/task/241211_155400%3Abelforte_crab_20241211_165356
job stdout correctly reports
```text
== JOB AD: REQUIRED_ARCH = "X86_64"
== JOB AD: REQUIRED_MINIMUM_MICROARCH = "x86-64-v3"
== JOB AD: REQUIRED_OS = "rhel8"
```
