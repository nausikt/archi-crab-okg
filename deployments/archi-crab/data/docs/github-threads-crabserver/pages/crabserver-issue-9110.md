# dmwm/CRABServer issue #9110: update CRABClient

State: closed
Opened: 2025-06-06T11:11:46Z
Closed: 2025-06-10T19:42:38Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9110

## Opening post (belforte, 2025-06-06T11:11:46Z)

current situation
#### PRODUCTION  (`/cvmfs/cms.cern.ch/common/crab`)


pre | prod | dev
| - | - | - |
v3.241125 | v3.250409 | v3.250505


#### IB (`/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-xxxxx/common/crab`)


pre | prod | dev
| - | - | - |
v3.241125 | v3.250409 | v3.250522


### TODO

- [x] move v3.250522 to prod in IB (and update pre)
- [x] check when this will be deployed in production to define timeline
- [x] judge if it is useful/important to ask Shahzad to deploy CRAB in production earlier

See documentation in https://cmscrab.docs.cern.ch/crab-components/crab-client.html

## Comment (nausikt, 2025-06-06T12:51:35Z)

Hi, Thank you Stefano for opening the issue. (Forgive me, I forgot that it could be urgent.)

[1] PR was made here [#9916](https://github.com/cms-sw/cmsdist/pull/9916).

[2] AFAIU, crab-prod will be depoyed on **24/6/2025**. (Not sure whether Tentative schedule for pre-release deadlines mentioned in [Twiki](https://twiki.cern.ch/twiki/bin/view/CMS/CMSSW_15_1_0) are the right & up-to-date place to looking for this kind of information)

[3] Given latest [CMS-talks issues, that user report, regarding corrupted files](https://cms-talk.web.cern.ch/t/3-files-are-damaged-in-this-dataset-doublemuon-run2016g-ul2016-miniaodv2-v1-miniaod/125539/4). it's gave me a little sense of urgent patch for our CRAB bug (that you already fixed). But on the other hand this issue occurs when dataset files were corrupted which seems rarely happens and was fixed by Data Transfer Team, So it's still unclear to me whether we need to rush Shahzad for the patch or we could wait 18 days following regular release cycles.

## Comment (belforte, 2025-06-06T13:03:00Z)

thanks Krittin, I was afraid that you would totally forget with all things you are doing.
as to your questions:
[1] it is not relevant now, but for the future it is better to also "port" crabserver version from `prod` to `pre` etc. in those `spec` files. There are a few dependency inside CRABClient from code in CRABServer and if we chage, it is important to be in sync. It is a long time since such changes happened, but it is better to take the good habit.
[2] yes, that's the best there is. Of course things happens and at  times those build are delayes, but it never happens that they do it before the scheduled date !
[3] those changes that you mention are on server side. You can check client changes in https://github.com/dmwm/CRABClient/releases

## Comment (belforte, 2025-06-06T13:03:16Z)

do not hesitate to ask questions, here on in MM

## Comment (nausikt, 2025-06-10T19:42:38Z)

Thanks Stefano for pointed out my clumsy regarding SUFFIX version conflicts.

Now, I can confirm that new version have been released in IB.
```
[kphornsi@lxplus953 CMSSW_13_0_2]$ /cvmfs/cms-ib.cern.ch/latest/common/crab --version
CRAB client v3.250522
[kphornsi@lxplus953 CMSSW_13_0_2]$ /cvmfs/cms-ib.cern.ch/latest/common/crab-pre --version
CRAB client v3.250217
[kphornsi@lxplus953 CMSSW_13_0_2]$ /cvmfs/cms-ib.cern.ch/latest/common/crab-dev --version
CRAB client v3.250522
```

For Production, i thought its on their way to production earlier as we requested. (can be few days or tomorrow). 

As we can saw [here](https://github.com/cms-sw/cmssw/pull/48256#event-18075657362) today that it was merged to master. Thanks to Shazad and cmssw team!, they have such a productive automated githubbot/workflow to keep tracking of extremely intricate things!
