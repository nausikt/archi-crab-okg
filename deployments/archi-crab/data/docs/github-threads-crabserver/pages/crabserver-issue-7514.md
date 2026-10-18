# dmwm/CRABServer issue #7514: add dset name to tarperecall rule metadata

State: closed
Opened: 2023-01-30T10:40:04Z
Closed: 2023-03-09T16:15:37Z
Labels: Status: Done, Priority: High, Area: zDATA RECALL, RUCIO
URL: https://github.com/dmwm/CRABServer/issues/7514

## Opening post (belforte, 2023-01-30T10:40:04Z)

currently rule info is like
```
belforte@lxplus8s15/~> rucio rule-info b24d483aab6a4da78905446e0e8fecca
Id:                         b24d483aab6a4da78905446e0e8fecca
Account:                    crab_tape_recall
Scope:                      user.crab_tape_recall
Name:                       /TapeRecall/230126_090925.dzuolo_crab_WJetsToLNu_4/USER
RSE Expression:             T1_FR_CCIN2P3_Disk|T2_BE_IIHE|T2_DE_RWTH|T2_EE_Estonia|T2_IN_TIFR|T2_US_Florida|T2_US_MIT|T2_IT_Legnaro|T2_US_Caltech|T2_FR_GRIF|T2_US_UCSD|T2_US_Vanderbilt|T2_IT_Pisa|T2_DE_DESY|T2_US_Purdue|T2_ES_CIEMAT|T1_IT_CNAF_Disk|T2_FR_IPHC|T2_UK_SGrid_RALPP|T2_US_Nebraska|T2_BR_SPRACE|T2_IT_Rome|T2_CH_CSCS|T1_DE_KIT_Disk|T2_HU_Budapest|T1_UK_RAL_Disk|T1_ES_PIC_Disk|T2_US_Wisconsin|T2_BE_UCL|T2_CH_CERN|T1_US_FNAL_Disk|T2_UK_London_IC|T2_IT_Bari|T2_FR_GRIF_IRFU|T2_FR_GRIF_LLR|T2_KR_KISTI
Copies:                     1
State:                      REPLICATING
Locks OK/REPLICATING/STUCK: 738/207/0
Grouping:                   ALL
Expires at:                 2023-02-09 09:10:09
Locked:                     False
Weight:                     ddm_quota
Created at:                 2023-01-26 09:10:09
Updated at:                 2023-01-30 03:10:00
Error:                      None
Subscription Id:            None
Source replica expression:  None
Activity:                   Analysis Input
Comment:                    Staged from tape for dzuolo
Ignore Quota:               False
Ignore Availability:        False
Purge replicas:             False
Notification:               NO
End of life:                None
Child Rule Id:              None
belforte@lxplus8s15/~> 
```

Since we recall full datasets (atm), it would be better to add the dataset name and size  (maybe in the comment)

## Comment (belforte, 2023-03-09T15:51:09Z)

OK. `rule-info` output is now like this, with the new comment in place
```
elforte@lxplus746/~> rucio rule-info 66728a69219b4f8d8e14559e448be057
Id:                         66728a69219b4f8d8e14559e448be057
Account:                    crab_tape_recall
Scope:                      user.crab_tape_recall
Name:                       /TapeRecall/230309_153209.belforte_crab_20230309_163202/USER
RSE Expression:             T2_IT_Rome|T2_ES_CIEMAT|T2_UK_SGrid_RALPP|T2_IT_Bari|T2_US_Caltech|T1_ES_PIC_Disk|T2_US_UCSD|T2_BE_IIHE|T2_US_Purdue|T2_CH_CSCS|T1_US_FNAL_Disk|T2_HU_Budapest|T1_IT_CNAF_Disk|T1_FR_CCIN2P3_Disk|T2_DE_RWTH|T2_IT_Legnaro|T1_UK_RAL_Disk|T2_DE_DESY|T2_US_Wisconsin|T2_IT_Pisa|T2_KR_KISTI|T2_FR_IPHC|T2_FR_GRIF_LLR|T2_EE_Estonia|T2_US_Nebraska|T2_US_Florida|T2_FR_GRIF|T2_UK_London_IC|T2_FR_GRIF_IRFU|T2_BR_SPRACE|T1_DE_KIT_Disk|T2_CH_CERN|T2_US_MIT|T2_IN_TIFR|T2_US_Vanderbilt|T2_BE_UCL
Copies:                     1
State:                      REPLICATING
Locks OK/REPLICATING/STUCK: 0/22/0
Grouping:                   ALL
Expires at:                 2023-03-23 15:47:20
Locked:                     False
Weight:                     ddm_quota
Created at:                 2023-03-09 15:47:20
Updated at:                 2023-03-09 15:48:19
Error:                      None
Subscription Id:            None
Source replica expression:  None
Activity:                   Analysis Input
Comment:                    Recall 17 GBytes for user: belforte dataset: /MuonEG/Run2016B-v1/RAW
Ignore Quota:               False
Ignore Availability:        False
Purge replicas:             False
Notification:               NO
End of life:                None
Child Rule Id:              None
belforte@lxplus746/~> 


```
