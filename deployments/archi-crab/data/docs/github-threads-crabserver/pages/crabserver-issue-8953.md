# dmwm/CRABServer issue #8953: Adding PsetHash from Edmprovdump fails with CMSSW_15_1

State: closed
Opened: 2025-02-27T14:01:39Z
Closed: 2025-04-14T13:11:26Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8953

## Opening post (aspiringmind-code, 2025-02-27T14:01:39Z)

See [here](https://cms-talk.web.cern.ch/t/crab-job-failed-pset-hash-missing-from-edmprovdump/116834)
This [line](https://github.com/dmwm/CRABServer/blob/master/scripts/CMSRunAnalysis.py#L496) assumes that the hash value will be at the end of the line dumped by edmProvdump. Tests fail therefore. A robust way to get the hash value should be worked out.

## Comment (belforte, 2025-02-27T14:10:38Z)

see also discussion in https://github.com/cms-sw/cmssw/pull/47355#discussion_r1973412363

## Comment (makortel, 2025-02-27T14:36:35Z)

I want to have a better and more stable way to communicate what CRAB needs. To me the framework job report XML would sound a good way to convey the necessary information (rather than parsing output of any additional script). Would you agree?

I'd also want to understand better if it is really the PSet hash that is needed here, or e.g. reduced process history ID (which is what the framework internally uses for the segregation of different processing histories).

In particular I'd advise against making any quick patches, because I'll change the `edmProvDump` output (especially this part) more drastically, and then we'd be here again. I'm already restoring the `edmProvDump` output (temporarily) in https://github.com/cms-sw/cmssw/pull/47473 so that we'd have more time to make a proper fix.

## Comment (belforte, 2025-02-27T14:51:25Z)

Thanks Matti,

I agree that FJR is preferrable. Even if we may have to do the change in WMCore code https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/FwkJobReport/Report.py

As to "what is needed", I'd say that the use case is simple, even if possibly not technically defined: limit the possibilities to users to shoot their own feed and come complaining with use with obscure problems later. That said, we need guidance from FWK Core developers on what to check.

## Comment (aspiringmind-code, 2025-02-27T15:07:53Z)

@makortel and @belforte Thank you for your insight. Yes, we'd like to not rely on parsing like this. I'd refrain from doing the regex change as a quick fix. And wait for the final edmProvDump output format to make necessary changes on our end.

## Comment (makortel, 2025-02-27T16:15:02Z)

So if I understood the present situation correctly, CRAB uses the PSet hash as part the dataset name published in DBS as described in https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Output_dataset_names_in_DBS, but not for anything else.

I saw references to "PSet hash" in the WMCore repository as well, but it was unclear to me if WMCore uses the PSet hash only to fill the field in DBS or also for something else, and from where WMCore gets the values.

Listing the various options of "IDs"
1. The PSet hash is an ID for the configuration itself (including the process name).
2. The reduced ProcessConfiguration ID adds the major and minor numbers from CMSSW version into the hashing (i.e. cuts the version string to  `CMSSW_15_0`; e.g. `CMSSW_15_0_1` and `CMSSW_15_0_10` are considered the same, and `CMSSW_15_0_1` and `CMSSW_15_1_1` are considered different).
3. The reduced ProcessHistory ID effectively adds the ProcessConfiguration IDs of all the earlier processes in the chain. A single file may contain events with different reduced ProcessHistory IDs (and I think we have seen those).

The CMSSW framework uses the 3) to segregate data. But given that a single file can contain events with different ProcessHistory IDs (e.g. merged MiniAOD files that contain data taken with different HLT configurations), that doesn't seem like a good fit here.

Between 1 and 2 the question is then if CRAB should use the CMSSW major/minor version to segregate datasets.

For complex PSets there is a good chance that some component added a new (tracked) parameter or a value of some existing parameter between CMSSW major or minor versions (e.g. between `CMSSW_14_2` and `CMSSW_15_0`). But for simple PSets the PSet hash alone could have the same value between CMSSW versions, that could then result in a user publishing files produced with two CMSSW versions into the same DBS dataset. But I have no feeling how (im)probable such a case would be.

## Comment (belforte, 2025-02-27T16:59:46Z)

Thanks @makortel 
I stand corrected. The PSet hash is part of the dictionary needed to publish one block in DBS[1]. CRAB uses the one discussed here. And I do not know if /how that information is used later on.
So WMCore must be filling this field to, or DBS would complain. And I guess @amaltaro or @khurtado are the ones to know where they get it and tell if/how WMCore will be impacted by the change. Maybe this value in DBS is always dummy [2]  ? I can't list it with DAS(goclient) to check what's there.

Do I understand correctly that current edmProdDump prints out ID number `1.` above ?
If yes, I would stay with that and do not take chances with getting more strict. We have no evidence of problems.

OTOH, if you are going to put this in the FJR XML, which is already a very large file, maybe you can write all the three possibility and free yourself :-)

[1]
https://github.com/dmwm/dbs2go/blob/master/docs/apis.md
https://github.com/dmwm/dbs2go/blob/master/dbs/bulkblocks.go

[2]
have we reached the point where current DBS developers are remote enough from original developers that we do not know what the various metadata files mean ?

## Comment (makortel, 2025-02-27T17:14:53Z)

> Do I understand correctly that current edmProdDump prints out ID number `1.` above ?

Correct.

> If yes, I would stay with that and do not take chances with getting more strict. We have no evidence of problems.

Ok.

> OTOH, if you are going to put this in the FJR XML, which is already a very large file, maybe you can write all the three possibility and free yourself :-)

That would indeed a possibility (except maybe for 3, for which there may be multiple values).

## Comment (belforte, 2025-02-27T17:50:55Z)

Indeed it sounds like 3. is only useful for the framework.

One last point. I presume that we will keep using edmProvDump for up to CMSSW_14 (and maybe 15_0 ?) and switch to new way from 15_1 onward, right ?

## Comment (makortel, 2025-02-27T18:46:47Z)

> I presume that we will keep using edmProvDump for up to CMSSW_14 (and maybe 15_0 ?) and switch to new way from 15_1 onward, right ?

You can continue using `edmProvDump` for sure up to CMSSW_14_X_Y. I don't foresee any need to touch `edmProvDump` there. And the new way with FWJR will be part of 15_1_X.

Fate of 15_0_X is a good question. Until this issue I was planning to backport the (present and upcoming) `edmProvDump` changes there (although it's more of it being nice to be able to print the new provenance information we're adding in 15_0_X with a 15_0_X release, than being strictly necessary). I can backport the upcoming change in FWJR to 15_0_X, and I can delay the (possible) backport of `edmProvDump` changes until we have a new version of CRAB in production. But that would mean that CRAB would have to use `edmProvDump` until some X in 15_0_X, and FWJR from X+1 onwards. How feasible would that be?

## Comment (belforte, 2025-02-27T22:30:26Z)

> . But that would mean that CRAB would have to use edmProvDump until some X in 15_0_X, and FWJR from X+1 onwards. How feasible would that be?

it still seems a simple `if` to me. No problem. I am sure @aspiringmind-code will have no problem implementing it.
To ease the transition can we put in a small hack to use e.g. edmProvDump from CMSSW_14 in such cases, while a proper change to WMCore and CRAB production releases goes through the pipeline. Will it work on files produced by 15_x ?

So we can decouple our and your timelines.

## Comment (makortel, 2025-02-28T14:33:58Z)

I'd rather not use `edmProvDump` from an earlier release. It might work, but is not guaranteed (in this particular case I'd think it could work, but there are subtleties that I'd prefer not to think about).

One option for a transition would be that CRAB would first try to use the PSet hash from the framework job report, and if it isn't there, then use `edmProvDump`. That an explicit release checks could be avoided, and even backports to earlier CMSSW release cycles would work automatically (as long as the fwjr change is made before or at the same release as the `edmProvDump` change). There would still be some timeline coupling (framework needs to decide the XML schema change, then CRAB can do their change, and only after the deployment of new CRAB can framework deploy more changes to `edmProvDump`). I'd be fine with that though.

## Comment (belforte, 2025-03-04T16:14:06Z)

Sorry for late reply @makortel 
Sure. I am fine with going in the order which you describe
1. define how CRAB will get PSet has from FJR
2. implement this in CRAB+WMCore, with fallback to edmProvDump
3. deploy in production
4. update edmProvDump to new format 

@aspiringmind-code @sinonkt I think it is better if you decide who among you is going to do 2. and use the time until 1. is ready to understand where changes will have to be done.

## Comment (makortel, 2025-03-06T22:16:18Z)

We are planning to proceed with the following addition to the FJR XML file (under the `<FrameworkJobReport>` element)
```xml
<Process>
  <Name>PROD1</Name>
  <ReducedConfigurationID>783c5ab60bfe18ac97262801adef9de4</ReducedConfigurationID>
  <ParameterSetID>1f94f8e1ac0ae9d7dade1c99cc5862b3</ParameterSetID>
</Process>
```
The `ParameterSetID` is the element whose content is the "PSet hash". I'm working to open a CMSSW PR soon (I'll let you know here).

## Comment (makortel, 2025-03-10T16:41:25Z)

> I'm working to open a CMSSW PR soon (I'll let you know here).

The CMSSW PR is here https://github.com/cms-sw/cmssw/pull/47548. Can you make progress on CRAB side with CMSSW IBs, or would you need (or benefit) from a pre-release?

## Comment (belforte, 2025-03-10T16:46:24Z)

@aspiringmind-code FYI you can submit (and test) with IB releases, simply make sure that crabConfig has
```python
config.JobType.allowUndistributedCMSSW = True
```

## Comment (makortel, 2025-03-14T13:29:43Z)

> > I'm working to open a CMSSW PR soon (I'll let you know here).
> 
> The CMSSW PR is here [cms-sw/cmssw#47548](https://github.com/cms-sw/cmssw/pull/47548). Can you make progress on CRAB side with CMSSW IBs, or would you need (or benefit) from a pre-release?

The aforementioned PR was merged. So any IB after CMSSW_15_1_X_2025-03-14-1100 (whose build is in process) could be used to test the enhanced framework job report. CMSSW pre-release-wise the PR will be part of 15_1_0_pre2 (presently scheduled for April 15).

## Comment (nausikt, 2025-03-14T13:39:11Z)

Thank you! Matti @makortel for your neat refactoring and provided IB/pre-release details. we will let you know asap when it was adapted in our side!

## Comment (aspiringmind-code, 2025-04-03T07:44:00Z)

@makortel I tested with CMSSW IBs after 15_1_X and it is quite simple to use the FrameworkJobReport xml file on CRAB side. I will create a PR with the changes before 15 April. Thanks!

## Comment (makortel, 2025-04-03T13:58:00Z)

Thanks @aspiringmind-code !

## Comment (aspiringmind-code, 2025-04-14T12:32:49Z)

[PR](https://github.com/dmwm/CRABServer/pull/9044) created.

## Comment (makortel, 2025-04-16T17:51:03Z)

Do I still need to wait for https://github.com/dmwm/CRABServer/pull/9044 to be deployed before evolving the `edmProbDump` further in CMSSW? (I'd assume so, but I want to make sure)

## Comment (aspiringmind-code, 2025-04-16T18:06:47Z)

@makortel Hi Matti, currently we have deployed [#9044](https://github.com/dmwm/CRABServer/pull/9044) on canary VM which is handling 30% of the production load. We use the canary to catch errors in real time on a small workload before finally deploying on the primary prod VM. We like to leave things for a week or so before we do the full deployment for any change. Hence, I'd ask you to kindly wait till the week after Easter. I'd let you know on this thread when we have deployed fully. Thanks!

## Comment (makortel, 2025-04-16T20:09:26Z)

Thanks, that works. I just wanted to understand better where we are (given the merge of the PR closed this issue)

## Comment (aspiringmind-code, 2025-04-24T11:02:00Z)

Hi @makortel The change is deployed everywhere now. You can go ahead. Thanks!

## Comment (makortel, 2025-04-24T18:43:59Z)

Thanks @aspiringmind-code!
