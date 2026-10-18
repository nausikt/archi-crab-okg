# dmwm/CRABClient issue #5248: crab report - raises exception when all the jobs failed

State: open
Opened: 2023-11-02T16:27:46Z
Labels: enhancement, MediumPrio
URL: https://github.com/dmwm/CRABClient/issues/5248

## Opening post (mapellidario, 2023-11-02T16:27:46Z)

While working on https://github.com/dmwm/CRABServer/issues/6540, I noticed that if all jobs of a task fail, then `crab report` refuses to compute `notFinishedLumis.json` and `notPublishedLumis.json`

#### example of a problem

consider `231026_133050:dmapelli_crab_20231026_153049` on test11. 4 jobs, all failed. (I killed the task after the jobs failed).

crab report fails with [1] because at

https://github.com/dmwm/CRABClient/blob/14c4ca79c704f1dea71088a3568cf937003597c9/src/python/CRABClient/Commands/report.py#L54

`reportData['runsAndLumis']` is empty, since

```plaintext
> curl -L --key $X509_USER_PROXY --cert $X509_USER_PROXY "https://cmsweb-test11.cern.ch/crabserver/devtwo/workflow?workflow=231026_133050:dmapelli_crab_20231026_153049&subresource=report2"
{"result": [
 {"taskDBInfo": {"userWebDirURL": "http://vocms059.cern.ch/mon/dmapelli/231026_133050:dmapelli_crab_20231026_153049", "inputDataset": "/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM", "outputDatasets": [], "publication": true}, "runsAndLumis": {}}
]}
```

#### expected result

If I remove the aforementioned check in crab report, then `notPublishedLumis.json` and `notFinishedLumis.json` are identical to `lumisToProcess.json` [2].

#### discussion

I know that it is very unlikely that a user will ever care running crab report on a task where all jobs failed. And also a crab recover will likely be not necessary, submitting the same task again will be a proper alternative. However, I do not like that our client returns an ambiguous result.

What shall we do? 

Keep in mind that `crab report` has this info [3], so it is not difficult to change the message to "sorry, all the jobs failed. You'd better submit a new task with the same config" if 

- `reportData["runsAndLumis"]` is empty, and
- all entries in `reportData["jobList"]`  are failed jobs

---

[1]

```plaintext
Singularity> crab report -d crab_20231026_153049 --recover notPublished --proxy=$X509_USER_PROXY
...
Error: Cannot get all the needed information for the report. Maybe no job has completed yet ?
 Notice, if your task has been submitted more than 30 days ago, then everything has been cleaned.
Will save lumi files into output directory /home/dario/crab/local/z-submitted/crab_20231026_153049/results
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
...
```

[2]


```plaintext
Singularity> crab report -d crab_20231026_153049 --recover notPublished --proxy=$X509_USER_PROXY
...
Will save lumi files into output directory /home/dario/crab/local/z-submitted/crab_20231026_153049/results
Summary from jobs in status 'finished':
  Number of files processed: 0
  Number of events read: 0
  Number of events written in EDM files: 0
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Warning: 'notPublished' lumis written to notPublishedLumis.json
           The 'notPublished' lumis were calculated as: the lumis to process minus the lumis published in the output dataset.
...
Singularity> diff -s crab_20231026_153049/results/notPublishedLumis.json crab_20231026_153049/results/lumisToProcess.json
Files crab_20231026_153049/results/notPublishedLumis.json and crab_20231026_153049/results/lumisToProcess.json are identical
Singularity> crab report -d crab_20231026_153049 --proxy=$X509_USER_PROXY
...
Will save lumi files into output directory /home/dario/crab/local/z-submitted/crab_20231026_153049/results
Summary from jobs in status 'finished':
  Number of files processed: 0
  Number of events read: 0
  Number of events written in EDM files: 0
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Warning: 'notFinished' lumis written to notFinishedLumis.json
           The 'notFinished' lumis were calculated as: the lumis to process minus the processed lumis.
...
Singularity> diff -s crab_20231026_153049/results/notFinishedLumis.json crab_20231026_153049/results/lumisToProcess.json
Files crab_20231026_153049/results/notFinishedLumis.json and crab_20231026_153049/results/lumisToProcess.json are identical
```

[3]

```plaintext
pprint.pprint(reportData)
{'inputDataset': '/GenericTTbar/HC-CMSSW_9_2_6_91X_mcRun1_realistic_v2-v2/AODSIM',
 'inputDatasetDuplicateLumis': {},
 'inputDatasetLumis': {'1': [[1, 49],
...
                             [3144, 3334]]},
 'jobList': [('failed', '2'),
             ('failed', '4'),
             ('failed', '1'),
             ('failed', '3')],
 'lumisToProcess': {'1': {'1': [[419, 419], [592, 592]]},
                    '2': {'1': [[652, 652], [1261, 1261]]},
                    '3': {'1': [[1849, 1849], [1858, 1858]]},
                    '4': {'1': [[2702, 2702], [2748, 2748]]}},
 'outputDatasets': [],
 'outputDatasetsInfo': {'outputDatasets': {}},
 'publication': True,
 'runsAndLumis': {}
}
```

## Comment (belforte, 2023-12-01T11:11:39Z)

I agree with:
* when all jobs failed, tell the user "no reporting is possible becasue all jobs failed"

I haven't gone through the logic, but I trust your judgement here that a fix is very simple. Please go ahead
