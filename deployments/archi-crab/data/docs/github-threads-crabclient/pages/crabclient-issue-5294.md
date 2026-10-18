# dmwm/CRABClient issue #5294: Block publishing a new CRABClient until v3.240322

State: closed
Opened: 2024-03-05T15:22:33Z
Closed: 2024-04-27T14:22:35Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5294

## Opening post (novicecpp, 2024-03-05T15:22:33Z)

Subtask of https://github.com/dmwm/CRABClient/issues/5289.

This is due to a break change introduced in https://github.com/dmwm/CRABClient/pull/5287.
The change on the server side [was deployed on 2024-02-20](https://cms-talk.web.cern.ch/t/production-taskworker-updated/33636/2). We are waiting until the tasks submitted before 2024-02-20 expire. 

Deploy date: after 2024-03-22

## Comment (novicecpp, 2024-03-06T10:38:14Z)

Maybe we can update crabdev now (suggested by Stefano)?
I will do it after finish validation.

## Comment (belforte, 2024-03-29T11:09:06Z)

time to go.
- [x] update crab-dev in IB to v3.240216 https://github.com/cms-sw/cmsdist/pull/9104
- [x] validate crab-dev in IB  
   - [x] https://github.com/dmwm/CRABServer/issues/8317
   - [x]  https://github.com/dmwm/CRABServer/issues/8319
   - [x] added last minute fix so now have v3.240404 validate that:
        - [x] https://github.com/dmwm/CRABServer/issues/8320
       - [x] https://github.com/dmwm/CRABServer/issues/8321
       - [x] https://github.com/dmwm/CRABServer/issues/8322
- [x] move new v3.240216 to crab-prod in IB and current v3.240110 to crab-pre  https://github.com/cms-sw/cmsdist/pull/9120
- [x] wait for change to be built in production /cvmfs (or trigger this by ourselves)
      * hmmm... next CMSSW_14_1_0 build is [scheduled](https://twiki.cern.ch/twiki/bin/view/CMS/CMSSW_14_1_0) for Apr 23 let's not wait

## Comment (belforte, 2024-04-27T14:22:35Z)

CRABClient v3.240416 is now default
```
belforte@lxplus803/TC3> which crab
/cvmfs/cms.cern.ch/common/crab
belforte@lxplus803/TC3> crab-prod --version
CRAB client v3.240416
```
