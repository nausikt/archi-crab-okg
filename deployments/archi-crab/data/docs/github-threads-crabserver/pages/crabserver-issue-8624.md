# dmwm/CRABServer issue #8624: variable used before it is defined

State: closed
Opened: 2024-08-15T09:06:59Z
Closed: 2024-08-28T15:50:44Z
Labels: Type: Bug, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8624

## Opening post (belforte, 2024-08-15T09:06:59Z)

`Problem handling 240812_094541:avdas_crab_20240812_114528 because of local variable 'ruleId' referenced before assignment failure, traceback follows\nTraceback (most recent call last):\n  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/RucioActions.py", line 79, in createOrReuseRucioRule\n    ruleIds = self.rucioClient.add_replication_rule(  # N.B. returns a list\n  File "/usr/local/lib/python3.8/site-packages/rucio/client/ruleclient.py", line 71, in add_replication_rule\n    raise exc_cls(exc_msg)\nrucio.common.exception.DuplicateRule: A duplicate rule for this account, did, rse_expression, copies already exists.\nDetails: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 94, in executeAction\n    output = work.execute(nexti\n[... message truncated to the first 1000 chars ...]`

## Comment (belforte, 2024-08-16T14:21:46Z)

This test (which makes sure that we do not try to extend a rule created by e.g. WMA) needs to be modified
https://github.com/dmwm/CRABServer/blob/0486eebbc50c49e3bc30919bee06579a3ee57f28/src/python/TaskWorker/Actions/RucioActions.py#L92-L98

I thought this was due to the changes I did for introducing an individual quota for tale recall.
In this case a task from `avdas` was trying to recall same dataset as in an existing rule created for a task by `wkwon`.
Now recall rules have the user's account name as `account`, while it was always `crab_tape_recall`.

But Rucio should not raise "duplicate rule" if account is different  :-(

## Comment (belforte, 2024-08-16T14:54:12Z)

indeed the error came handling task 240812_094541:avdas_crab_20240812_114528
 A bit later task 240812_124249:avdas_crab_20240812_144239 was submitted with same dataset as input, and this time it worked. 
That dataset is `/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEDRPremix-124X_mcRun3_2022_realistic_postEE_v1-v4/AODSIM` and has only two rules
1. [6e937f42aad448c9b0829bff769188f5](https://cms-rucio-webui.cern.ch/rule?rule_id=6e937f42aad448c9b0829bff769188f5) from wmcore_output
2. [761856cd099f48fb8e532d37c5eda3cc](https://cms-rucio-webui.cern.ch/rule?rule_id=761856cd099f48fb8e532d37c5eda3cc) from that user `advas`

## Comment (belforte, 2024-08-16T15:04:36Z)

I do not understand how we could have got a duplicateException from Rucio before [761856cd099f48fb8e532d37c5eda3cc](https://cms-rucio-webui.cern.ch/rule?rule_id=761856cd099f48fb8e532d37c5eda3cc) was created.

So am trying to call this **Unreproducible** and move on

## Comment (belforte, 2024-08-16T15:05:10Z)

On Hold until it happens again. Maybe a glitch in Rucio ?

## Comment (belforte, 2024-08-17T10:27:06Z)

hmm problem is not that rare. It happens every few days and started on Aug 6 (we have logs back to July 12).
```text
twlog.txt.2024-08-06:Problem handling 240806_150852:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022B because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-06:Problem handling 240806_150916:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022C2 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-06:Problem handling 240806_152640:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022B because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-06:Problem handling 240806_152705:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022C2 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-07:Problem handling 240807_112221:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022C2 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-07:Problem handling 240807_153529:aguven_crab_20240807_173507 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-08:Problem handling 240808_073352:avdas_crab_20240808_093334 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-08:Problem handling 240808_093049:jbierken_crab_TnP_ntuplizer_muon_Z_Run2022_AOD_Run2022C2 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-09:Problem handling 240809_153536:pchou_crab_ppref_MC_ZB0_1400v172_HLT_20240808 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-09:Problem handling 240809_153640:pchou_crab_ppref_MC_ZB0_1400v172_noL1_HLT_20240808 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-12:Problem handling 240812_094541:avdas_crab_20240812_114528 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-12:Problem handling 240812_144322:sdansana_crab_HToSS_SmuonHadronFiltered_MH125_MS1p1_ctauS10_2017_20240812164310 because of local variable 'ruleId' referenced before assignment failure, traceback follows
twlog.txt.2024-08-16:Problem handling 240816_100136:aguven_crab_20240816_120109 because of local variable 'ruleId' referenced before assignment failure, traceback follows
```
Deserves more thought

## Comment (belforte, 2024-08-17T11:05:01Z)

a possibility is to check that the code finds the duplicate rule and if not, raise some more clear error

the other is to assume that Rucio does not check for "same account" and do that checking ourselves

I am still  puzzled.
I can start by printing all rules for that DID when we make the check for same account

https://github.com/dmwm/CRABServer/blob/0486eebbc50c49e3bc30919bee06579a3ee57f28/src/python/TaskWorker/Actions/RucioActions.py#L93-L96

## Comment (belforte, 2024-08-28T15:50:44Z)

fixed in #8632
