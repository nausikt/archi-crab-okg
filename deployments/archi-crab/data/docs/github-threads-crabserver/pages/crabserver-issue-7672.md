# dmwm/CRABServer issue #7672: avoid deleting rules used by other tasks

State: closed
Opened: 2023-06-15T19:35:05Z
Closed: 2023-06-16T13:25:56Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7672

## Opening post (belforte, 2023-06-15T19:35:05Z)

the new code which recycle Rucio tape recall rules across multiple tasks
failed to deal with the following scenario:
* task A creates rule R
* later task B comes for same dataset and rule R is reused
* user kills task A - task is put in KILLRECALL
* TapeRecallManager deletes rule R and put task A in killed
* at this point task B points to a rule which does not exist in Rucio and will of course never succeed

<details><summary>Details from today's example</summary>
this resulted in messages like this in TaskRecallManager.log

```
2023-06-15 18:41:48,778:INFO:TapeRecallManager:Working on task 230615_062905:santocch_crab_singlemu-2016b
2023-06-15 18:41:48,778:INFO:TapeRecallManager:Task points to Rucio RuleId:  60350d44cf2a49d29de6e9688993903a 
2023-06-15 18:41:48,832:ERROR:TapeRecallManager:Rucio rule id 60350d44cf2a49d29de6e9688993903a not found. Please report to experts
```

one can tell what's happened by listing rule history for the input dataset of that task:

```
belforte@lxplus814/cmsweb> rucio list-rules-history cms:/SingleMuon/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/MINIAOD
----------------------------------------
Rule insertion
Account : transfer_ops
RSE expression : ddm_quota>0&rse_type=DISK&country=US
Time : 2020-12-13 00:10:56
----------------------------------------
Rule deletion
Account : transfer_ops
RSE expression : ddm_quota>0&rse_type=DISK&country=US
Time : 2023-03-21 08:30:57
----------------------------------------
Rule insertion
Account : crab_tape_recall
RSE expression : T1_US_FNAL_Disk|T2_BR_SPRACE|T2_US_Caltech|T2_US_Florida|T2_US_MIT|T2_US_Nebraska|T2_US_Purdue|T2_US_UCSD|T2_US_Vanderbilt|T2_US_Wisconsin
Time : 2023-06-15 03:29:14
----------------------------------------
Rule deletion
Account : crab_tape_recall
RSE expression : T1_US_FNAL_Disk|T2_BR_SPRACE|T2_US_Caltech|T2_US_Florida|T2_US_MIT|T2_US_Nebraska|T2_US_Purdue|T2_US_UCSD|T2_US_Vanderbilt|T2_US_Wisconsin
Time : 2023-06-15 09:11:53
belforte@lxplus814/cmsweb> 
```

and indeed

```
 belforte@lxplus814/cmsweb> rucio rule-info 60350d44cf2a49d29de6e9688993903a
2023-06-15 20:50:53,794	ERROR	No replication rule found.
Details: No rule with the id 60350d44cf2a49d29de6e9688993903a found
belforte@lxplus814/cmsweb>
```

and rule deletion was duly logged

```
2023-06-15 10:30:27,417:INFO:TapeRecallManager:Retrieving KILLRECALL tasks
2023-06-15 10:30:34,550:INFO:TapeRecallManager:Retrieved a total of 6 KILLRECALL tasks
2023-06-15 10:30:34,550:INFO:TapeRecallManager:Working on task 230615_032814:santocch_crab_singlemu-2016b
2023-06-15 10:30:34,551:INFO:TapeRecallManager:Task points to Rucio RuleId:  60350d44cf2a49d29de6e9688993903a 
2023-06-15 10:30:34,551:INFO:TapeRecallManager:Will delete rule 60350d44cf2a49d29de6e9688993903a
2023-06-15 10:30:34,576:INFO:TapeRecallManager:Will set to KILLED task 230615_032814:santocch_crab_singlemu-2016b
2023-06-15 10:30:34,658:INFO:TapeRecallManager:Done on this task
```

</detail>

## Comment (belforte, 2023-06-15T19:37:39Z)

this problem is what made TapeRecallManager go for the first time through
https://github.com/dmwm/CRABServer/blob/b0e87839e79743850e292d35f012efc42344cb01/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L93-L97
which triggered the bugs in #7667 and #7669

## Comment (belforte, 2023-06-15T19:44:35Z)

the solution will be to use new `taskbyddmreqid` API
https://github.com/dmwm/CRABServer/blob/b0e87839e79743850e292d35f012efc42344cb01/src/python/CRABInterface/RESTTask.py#L108-L112
to list all tasks which refer to same rule as the task in KILLRECALL and only delete the rule if that task is the only one.

This is not 100% foolproof, there can be race conditions as TW thread does a DBSDataDiscovery and reuses a rule while another thread processes KILLRECALL and remove the rule. But changes of this are very small, and in the end, the result will be one task stuck in TAPERECALL which user will likely kill and submit again.
We can live with that, and avoid making code more complex.
- [ ] put comments in the (new) code explaining this
