# dmwm/CRABServer issue #9147: Site_White/Black list left unexpanded, when we do CRAB resubmission.

State: closed
Opened: 2025-08-07T12:04:14Z
Closed: 2025-08-11T16:27:56Z
URL: https://github.com/dmwm/CRABServer/issues/9147

## Opening post (nausikt, 2025-08-07T12:04:14Z)

Thank you @belforte, for reporting these specific use-cases and pointed out shortcoming around #6917. 
```bash
Thu, 07 Aug 2025 11:22:49 CEST(+0200):INFO:PreJob Setting CRAB_Retry = 3
Thu, 07 Aug 2025 11:22:49 CEST(+0200):ERROR:PreJob Can not submit since DESIRED_Sites list is empty
```
it appears that in resubmission the white list was passed un-expanded to the AP (scheduler)
```bash
CRAB_SiteWhitelist = { "T1_*","T2_US_*","T2_IT_*","T2_DE_*","T2_ES_*","T2_FR_*","T2_UK_*" } 
```

## Comment (belforte, 2025-08-07T12:06:25Z)

thanks for opening this @sinonkt 
I will add here what I find

## Comment (nausikt, 2025-08-07T12:06:39Z)

As far as i investigated...

[1] `src/python/CRABInterface/RESTWorkerWorkflow.py` it was **Neither** expanded on **REST** here.
```python
143:    result['resubmit_site_whitelist'] = extraargs['site_whitelist'] if 'site_whitelist' in extraargs else None
144:    if result['resubmit_site_whitelist'] is None and 'siteWhiteList' in extraargs: ## For backward compatibility only.
145:        result['resubmit_site_whitelist'] = extraargs['siteWhiteList']
146:    result['resubmit_site_blacklist'] = extraargs['site_blacklist'] if 'site_blacklist' in extraargs else None
147:    if result['resubmit_site_blacklist'] is None and 'siteBlackList' in extraargs: ## For backward compatibility only.
148:        result['resubmit_site_blacklist'] = extraargs['siteBlackList']
```
[2] Nor on **TaskWorker**`src/python/TaskWorker/Actions/DagmanResubmitter.py`, when taskparam::`site_whitelist|site_blacklist` there.
```python
src/python/TaskWorker/Actions/DagmanResubmitter.py
80:        if ('resubmit_jobids' in task) and task['resubmit_jobids']:
87:                # files are in the directory resubmit_info in the schedd).
93:                    if task['resubmit_' + taskparam] is not None:
94:                        if isinstance(task['resubmit_'+taskparam], list):
95:                            newAdValue = pythonListToClassAdExprTree(task['resubmit_'+taskparam])
97:                            newAdValue = str(task['resubmit_'+taskparam])
```
____
We can **Either**
1. patch on TW at [1] _exapnding on REST. BUT it should be deprecated anyhow.
2. patch on TW at [2] add SiteResolverInfo TaskAction inside `handleResubmit` on TW, BUT we have to be cautious that SiteResolverInfo was not generic enough for DagmanResumitter which not use kwargs[`task`,`tm_site_whitelist`] but instead it use dedicated inkey `['resubmit_site_whitelist']` when come to task_param.
3. patch on TW at [2] try to just expanding sites there w/o resusing SiteResolverInfo, even we introduced some duplicated code here e.g. instantiate CRIC, exapanding...

**PreJob** should be fine when we patched upstream REST [1] or TaskAction [2].

Let me hear your thoughts...

## Comment (belforte, 2025-08-07T12:12:11Z)

you pointed out correclty to root cause: `task['resubmit_site_whitelist']` is not expanded by `SiteInfoResolver`

Maybe we can simply call that in the Handler also inside `handleResubmit` and inside it expand also the `resubmit_list*` if presents.

## Comment (nausikt, 2025-08-07T12:16:13Z)

> you pointed out correclty to root cause: `task['resubmit_site_whitelist']` is not expanded by `SiteInfoResolver`
> 
> Maybe we can simply call that in the Handler also inside `handleResubmit` and inside it expand also the `resubmit_list*` if presents.

Acknowledge Stefano, let me get back to you with PR and reproduced test results.

## Comment (belforte, 2025-08-07T12:17:14Z)

may want to restructure SiteInfoResolver a little bit to avoid duplicating code

## Comment (belforte, 2025-08-07T12:19:05Z)

Sorry, we did indeed talk about this "back then", but then I forgot. Simply that this time by chance the CI pipeline had two failed jobs in the 1K job task and I wanted to make it succeed.

I am trying to cook a quick test of the change now

## Comment (nausikt, 2025-08-07T12:32:52Z)

> Sorry, we did indeed talk about this "back then", but then I forgot. Simply that this time by chance the CI pipeline had two failed jobs in the 1K job task and I wanted to make it succeed.
> 
> I am trying to cook a quick test of the change now

No worries, Stefano. Thanks to you! kindly sparing your retirement time to thoroughly review and patiently mentor me, it easily been forgot when a lot of things going on on your side.

## Comment (belforte, 2025-08-07T13:04:38Z)

here's something that appears to almost work
https://github.com/belforte/CRABServer/blob/reorganize-tw-tarballs/src/python/TaskWorker/Actions/Handler.py
https://github.com/belforte/CRABServer/blob/reorganize-tw-tarballs/src/python/TaskWorker/Actions/SiteInfoResolver.py

I still get an error in preJob. But classAds in DagmanResubmitter appears OK.
Need to debug more.

## Comment (nausikt, 2025-08-07T13:10:03Z)

@belforte Thank you Stefano, I also come up with almost identical to you, https://github.com/dmwm/CRABServer/pull/9148/files but let me tested it more.

## Comment (nausikt, 2025-08-07T13:15:13Z)

> [@belforte](https://github.com/belforte) Thank you Stefano, I also come up with almost identical to you, https://github.com/dmwm/CRABServer/pull/9148/files but let me tested it more.

Ohh, yours is better, i made some mistake on mine, I'll converged to yours, since it's seems like `tm_site_*` also available in both **handleNewTask** and **handleResubmit** request, and `_expandSites` is idempotent.

## Comment (belforte, 2025-08-07T13:15:47Z)

it looks a problem in list to HTC classAd conversion. Originating from `set` vs. `list` "confusion". We should be more clear and more consistent on what variable is a set and what a list. Or otherwise use an explicit cast all of the times :-(

## Comment (nausikt, 2025-08-07T13:17:13Z)

> it looks a problem in list to HTC classAd conversion. Originating from `set` vs. `list` "confusion". We should be more clear and more consistent on what variable is a set and what a list. Or otherwise use an explicit cast all of the times :-(

Acknowledge Stefano.

## Comment (belforte, 2025-08-07T13:20:56Z)

at same link there's a fixed SiteInfoResolver.  The problem was this line in DagmanResubmitter
```python
if isinstance(task['resubmit_'+taskparam], list)
```
bad things happen when the argument is a `set` :-(

## Comment (nausikt, 2025-08-07T13:28:17Z)

I see. `set(...)` we need here is just for when we doing set manipulation like intersection checking, e.g. `global_black_list`, check/substract avaibliblesites...acceleratorssite, ...etc.. later. 

I will fixed other places where we really need set then.

## Comment (belforte, 2025-08-07T13:33:05Z)

I think the best way is: whatever variable we have which is called ...list should be a list. We can convert to a set to do the and/or manipulations, but then revert to a list.  We could surely extend `pythonListToClassAdExprTree()` to deal with set as well, but need to change all type checks before the call.

intermixing lists and sets is a bit in line with Python's "duck typing" standard. But that comes at cost of care in implementation, "strong typing" is a bit more annoying, but safer.

In this case we mostly need a clear policy, IMHO.

## Comment (nausikt, 2025-08-07T13:36:30Z)

Agree, Acknowledge, will converged to that in [PR](https://github.com/dmwm/CRABServer/pull/9148)

## Comment (belforte, 2025-08-07T13:37:40Z)

OK. The failed pipeline task was successfully resubmitted now.
Problem understood and no great urgency.
I will dedicate myself to my daughter now and will let you polish the fix.
Thanks for having jumped on it so quickly. The classAd conversion is alas something that I am the only one in the team who understands it.

## Comment (nausikt, 2025-08-07T13:39:37Z)

> OK. The failed pipeline task was successfully resubmitted now. Problem understood and no great urgency. I will dedicate myself to my daughter now and will let you polish the fix. Thanks for having jumped on it so quickly. The classAd conversion is alas something that I am the only one in the team who understands it.

Ack, Thanks Stefano.

## Comment (nausikt, 2025-08-11T12:50:24Z)

tests around resubmission on test14 looks OK as you can see [here](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=250811_120042%3Akphornsi_crab_testResubmissionExpectedFailed8&from=1754910042000&to=now)
and as I've inspected Job AD Site{White|Black} of retry jobs. They were expanded properly.

```
job_out.10.1.txt
63:== JOB AD: CRAB_SiteBlacklist = { "T2_ES_IFCA" }
64:== JOB AD: CRAB_SiteWhitelist = { "T2_US_Wisconsin","T1_IT_CNAF","T2_FR_GRIF","T2_US_Purdue","T2_US_Caltech","T2_IT_Legnaro","T1_RU_JINR","T1_US_FNAL","T2_ES_CIEMAT","T1_PL_NCBJ","T1_ES_PIC","T2_UK_SGrid_Bristol","T1_DE_KIT","T1_FR_CCIN2P3","T2_US_Vanderbilt","T2_IT_Bari","T2_US_MIT","T2_US_Florida","T1_UK_RAL","T2_UK_SGrid_RALPP","T2_ES_IFCA","T2_DE_DESY","T2_IT_Pisa","T2_UK_London_IC","T2_FR_IPHC","T2_DE_RWTH","T2_IT_Rome","T2_UK_London_Brunel","T2_US_UCSD","T2_US_Nebraska" }

job_out.8.1.txt
63:== JOB AD: CRAB_SiteBlacklist = { "T2_ES_IFCA" }
64:== JOB AD: CRAB_SiteWhitelist = { "T2_US_Wisconsin","T1_IT_CNAF","T2_FR_GRIF","T2_US_Purdue","T2_US_Caltech","T2_IT_Legnaro","T1_RU_JINR","T1_US_FNAL","T2_ES_CIEMAT","T1_PL_NCBJ","T1_ES_PIC","T2_UK_SGrid_Bristol","T1_DE_KIT","T1_FR_CCIN2P3","T2_US_Vanderbilt","T2_IT_Bari","T2_US_MIT","T2_US_Florida","T1_UK_RAL","T2_UK_SGrid_RALPP","T2_ES_IFCA","T2_DE_DESY","T2_IT_Pisa","T2_UK_London_IC","T2_FR_IPHC","T2_DE_RWTH","T2_IT_Rome","T2_UK_London_Brunel","T2_US_UCSD","T2_US_Nebraska" }
```

how do you feel about proceeding to merge and make release? @belforte

## Comment (belforte, 2025-08-11T15:02:30Z)

looks very good. Thanks !
Can you please address the small comments in the PR and then ask again for Review ? Thanks
