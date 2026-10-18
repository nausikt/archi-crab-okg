# dmwm/CRABServer issue #8852: Submission Deferral for HammerCloud does not work anymore

State: closed
Opened: 2024-11-29T18:03:07Z
Closed: 2024-12-02T21:38:39Z
URL: https://github.com/dmwm/CRABServer/issues/8852

## Opening post (belforte, 2024-11-29T18:03:07Z)

as reported by @stlammel [2]

see documentation of the deferral in [1](https://github.com/dmwm/CRABServer/wiki/CRAB-vs-HammerCloud#slow-job-release)

problem is that PreJob [looks](https://github.com/dmwm/CRABServer/blob/ddd6ce1ded4d1b49cf92406b39d9a47321bd6776/src/python/TaskWorker/Actions/PreJob.py#L477) for a non-zero value of `CRAB_JobReleaseTimeout` in the dag boostrap [classAds](https://github.com/dmwm/CRABServer/blob/ddd6ce1ded4d1b49cf92406b39d9a47321bd6776/src/python/TaskWorker/Actions/PreJob.py#L174).

The way for user to indicate that was implemented ([1]) via adding in crabConfig.
```
config.Debug.extraJDL=['+CRAB_JobReleaseTimeout=Nsec'] 
```
But `extraJDL` can also contain things which make DAG bootstrap fail , see #8784 

So I had to stop passing `extraJDL` ads to the dagman.jdl  and PreJob does not find the ad anymore.

Need a cleaner and explicit way to put `CRAB_JobReleaseTimeout` in `DAGJob.jdl`
https://github.com/dmwm/CRABServer/blob/ddd6ce1ded4d1b49cf92406b39d9a47321bd6776/src/python/TaskWorker/Actions/DagmanSubmitter.py#L459
[...]
https://github.com/dmwm/CRABServer/blob/ddd6ce1ded4d1b49cf92406b39d9a47321bd6776/src/python/TaskWorker/Actions/DagmanSubmitter.py#L528-L529

The best way would be an additional parameter in crabConfiguration, not an extrajdl classAd.

As a quick patch I can parse extraJdl from `info` in DagmanSubmitter and add `CRAB_JobReleaseTimeout`  if needed :-( Still ugly


[1]
```text
Subject: 	Re: no HammerCloud jobs at Tier-1s
Date: 	Fri, 29 Nov 2024 17:33:53 +0100
From: 	Stephan Lammel <stephan.lammel@cern.ch>
To: 	Stefano Belforte <Stefano.Belforte@cern.ch>, Andrea Sciaba <Andrea.Sciaba@cern.ch>, Jakrapop Akaranee <akaranee.jakrapop@cern.ch>, Malik Shahzad Muzaffar <shahzad.malik.muzaffar@cern.ch>
CC: 	Chan-Anun Rungphitakchai <rungphitakch@wisc.edu>, cms-service-crab3htcondor (Announcements from IT to CRAB3-HTCondor Project) <cms-service-crab3htcondor@cern.ch>


Many Thanks Stefano!

There is a remaining issue that started Wednesday when first jobs
run again: Jobs seem to be batched together and are not finishing
continuously. If you look at siteStatus, i.e.
https://cmssst.web.cern.ch/siteStatus/summary.html
you see an hour and a half of unknown status/no HC results and
then 30 minutes of ok status/many HC results. (Although Site
Readiness is shown, the pattern comes from HammerCloud. If you
click on a site, for instance
https://cmssst.web.cern.ch/siteStatus/detail.html?site=T1_FR_CCIN2P3
you see it's coming from HammerCloud.)

Was there any change made to the "release a job every 5 minute"
logic that could account for this?
(I can't exclude it's due to scheduling on SI/global pool side but the
"Submit" times on the Grafana dashboard, i.e.

https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=sciaba&var-task=241129_154348:sciaba_crab_HC-211-T1_FR_CCIN2P3-110047-20241129144101&from=1732895028000&to=now

suggests to me it's on CRAB side.)

```

## Comment (belforte, 2024-12-02T08:47:26Z)

three are more `extraJDL` used by HammerCloud, here's one config file from recent task:
```text
from WMCore.Configuration import Configuration
config = Configuration()
config.section_('Site')
config.Site.blacklist = ['T3*']
config.Site.ignoreGlobalBlacklist = True
config.Site.whitelist = ['T1_FR_CCIN2P3']
config.Site.storageSite = 'T2_CH_CERN'
config.section_('Data')
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 15
config.Data.publication = False
config.Data.ignoreLocality = True
config.Data.outputDatasetTag = '0ea12bcd230936c2556840cb8452714d'
config.Data.inputDataset = '/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM'
config.Data.allowNonValidInputDataset = True
config.Data.totalUnits = 3315
config.section_('JobType')
config.JobType.priority = 600000
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.maxJobRuntimeMin = 300
config.JobType.psetName = '/data/hc/apps/cms/inputfiles/usercode/miniaodsim_9xx.py'
config.section_('Debug')
config.Debug.extraJDL = ['+CRAB_NoWNStageout=1', '+CRAB_JobReleaseTimeout=300', '+CRAB_NoWNStageout=1', '+CRAB_HC=True', 'accounting_group=highprio', 'accounting_group_user=cmsdataops']
config.section_('User')
config.User.voRole = 'production'
config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'HC-211-T1_FR_CCIN2P3-110047-20241129144101'
config.General.transferOutputs = False
config.General.activity = 'hctest'
```

## Comment (belforte, 2024-12-02T09:46:03Z)

`config.Debug.extraJDL` are passed to job anyhow via Job.x.submit files.

`CRAB_NoWNStageout` is used in `cmscp.py` and PostJob. - OK , but ...could it be replaced with `config.General.transferOutputs=False` ?
`CRAB_HC` is only used in RenewRemoteProxies to skip HC tasks . Could replace with `if task['tm_activity'] and 'HC' in task['tm_activity'].upper():` as used already in DagmanCreator
`accounting_group` and `accounting_group_user`  are JDL [commands](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html#accounting_group) for the submitted jobs and are OK

## Comment (belforte, 2024-12-02T09:50:28Z)

so only `+CRAB_JobReleaseTimeout=300` needs to be passed to the DAG JDL, or replaced with a config. option, extending the JSON in `tm_user_config` like done for `input_blocks` or `require_accelerators`
