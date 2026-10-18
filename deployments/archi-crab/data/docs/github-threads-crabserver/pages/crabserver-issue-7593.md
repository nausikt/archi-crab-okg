# dmwm/CRABServer issue #7593: report progress of tape recall in crab status

State: closed
Opened: 2023-04-14T07:41:29Z
Closed: 2023-08-28T15:08:52Z
Labels: Type: Enhancement, Priority: High, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/7593

## Opening post (belforte, 2023-04-14T07:41:29Z)

help users figure out how things are going.
Also report expiration date of rule
This can be done tuning message uploaded to DB. No need to change CRABClient
Also current printout is a bit too long and obscure.
```
Warning: Task could not be submitted because not all blocks of dataset /DoubleElectron_Pt-1To300-gun/RunIISummer20UL18RECO-FlatPU0to70EdalIdealGT_EdalIdealGT_106X_upgrade2018_realistic_v11_L1v1_EcalIdealIC-v2/AODSIM are on DISK
Will try to request a full disk copy for you. See
 https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_submit_fails_with_Task_coul
A disk replica has been requested to Rucio (rule ID: 3264ca6fb2954d189f08144500962b23 )
you can check progress via either of the following two commands:
 rucio rule-info 3264ca6fb2954d189f08144500962b23
 rucio list-rules user.crab_tape_recall:/TapeRecall/230411_192809.bjoshi_crab_DoubleElectron_Pt-1To300-gun_RunIISummer20UL18RECO-FlatPU0to70EdalIdealGT_EdalIdealGT_106X_upgrade/USER
or simply check 'state' line in this page: https://cms-rucio-webui.cern.ch/rule?rule_id=3264ca6fb2954d189f08144500962b23
This task will be automatically submitted as soon as the stage-out is completed.
```

## Comment (novicecpp, 2023-04-14T13:00:09Z)

Is better to improve message in client? Maybe somehow reuse interface from `crab recall`.

## Comment (belforte, 2023-04-14T13:05:30Z)

matter of taste I think. in periodic action to check status there are already calls to rucio for this rule, so it may be where it is done with less work. Updating message in Oracle makes it possible to see message in server UI... yeah.. all soft arguments. The difficult part is always to write a good message. Current one is horrible !

## Comment (belforte, 2023-08-17T10:35:37Z)

Maybe when TapeRecallManager process a task it could:
1. delete warnings
2. upload a new short warning:
   `data recall from tape in progress: ok/all = xxx/yyy = zz%.\n Rucio rule <link_to_rule_page>\n more info in <ptr-to-twiki>`

I will give this a try

## Comment (belforte, 2023-08-28T15:04:08Z)

example output from new code
```
belforte@lxplus802/castells> crab status -d crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017/
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/castells/crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017
Task name:			230828_095504:castells_crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017
Grid scheduler - Task Worker:	N/A yet - crab-prod-tw01
Status on the CRAB server:	TAPERECALL on command SUBMIT
Task URL to use for HELP:	https://cmsweb.cern.ch/crabserver/ui/task/230828_095504%3Acastells_crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=castells&var-task=230828_095504%3Acastells_crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017&from=1693212904000&to=now
Warning:			Data recall from tape in progress: ok/all = 0/30 = 0.0%
				Rucio rule details at https://cms-rucio-webui.cern.ch/rule?rule_id=ee1777ea2ffa4da4b38fae60b2609678
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/castells/crab_MNConversion_HAHMHToAA_AToGG_MA-35GeV_TuneCP5_PSweights_13TeV-madgraph_pythia8_2017/crab.log
belforte@lxplus802/castells> 
```
