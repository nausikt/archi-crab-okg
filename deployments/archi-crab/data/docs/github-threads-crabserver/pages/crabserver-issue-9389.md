# dmwm/CRABServer issue #9389: ensure that we can tell analysis from MC in monitoring

State: closed
Opened: 2026-08-19T22:01:10Z
Closed: 2026-08-24T21:45:15Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9389

## Opening post (belforte, 2026-08-19T22:01:10Z)

we currently rely on "no input dataset" (in details, classAd DESIRED_CMSDataset to be undefined, which is a bit tricky to select in Grafana). But this fails when e.g. users specfifies in the configuration `data.userInputFiles` which is a "data processing workflow" but has no `desired_cmsdataset`

That happens rather frequently now e.g. https://cmsweb.cern.ch/crabserver/ui/task/260815_181226:anstahll_crab_HIPhysicsRawPrime_PHOLEP_HIRun2024_PromptReco_MINIAOD_2026_08_07

In monitoring all of CRAB jobs have `JobType=analysis` and `JobType=Production/Processing` is reserved for WMA. Changing this is likely to break many existing monitoring dashboards and scripts, so it is not an option

some possibilities that come to mind

* clearly set `DESIRED_CMSDataset = "None"` to indicate MC
* set `DESIRED_CMSDataset = "UserFiles"` when  `data.userInputFiles`  is used
* check the CRABClient plugin type `config.JobType.pluginName = 'Analysis'` currently stored in `tm_job_type` and propagate it to OpenSearch "somehow"
* something else or combinations of the above
* adding a new classAd and a new field in OpenSearch
* ....

### Important notes

##### those will require changing the ad parsing in https://github.com/dmwm/cms-htcondor-es/blob/b1c8998e08702ca230831d10cf7910c9dd33cd8d/src/htcondor_es/convert_to_json.py#L764-L769

##### need to worry what happens to aggregated data in the job monitoring dashboard

## Comment (belforte, 2026-08-24T09:44:48Z)

I think that best option is to "extend" `CMS_JobType` which currently is always `Analysis` to be either `Analysis` or `PrivateMC`
That reflects the CRABClient plugin name and is consistent with WMA which uses `CMS_JobTyp` to differentiate Production from Processing.
