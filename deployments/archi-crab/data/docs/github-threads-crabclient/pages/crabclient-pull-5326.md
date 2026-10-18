# dmwm/CRABClient pull request #5326: report - fix bug in --recovery=failed

State: closed
Opened: 2024-07-12T15:03:32Z
Closed: 2024-07-15T07:57:05Z
Merged: 2024-07-15T07:57:05Z
URL: https://github.com/dmwm/CRABClient/pull/5326

## Opening post (mapellidario, 2024-07-12T15:03:32Z)

fix #5325

### status

tested, the `failedLumis.json` file is produced [1]

---

[1]:

<details>

```plaintext
Singularity> crab report -d crab_EGammaEXO_Run2018A_20240704_231147 --proxy=$X509_USER_PROXY --recovery=failed
Running crab status first to fetch necessary information.
Rucio client intialized for account dmapelli
Will save lumi files into output directory /home/dario/crab/local/z-submitted/crab_EGammaEXO_Run2018A_20240704_231147/results
Summary from jobs in status 'finished':
  Number of files processed: 2860
  Number of events read: 3848368
  Number of events written in EDM files: 0
  Number of events written in TFileService files: 0
  Number of events written in other type of files: 0
  Processed lumis written to processedLumis.json
  Warning: 'failed' lumis written to failedLumis.json
           The 'failed' lumis were calculated as: the lumis to process by jobs in status 'failed'.
Additional report lumi files:
  Input dataset lumis (from DBS, at task submission time) written to inputDatasetLumis.json
  Lumis to process written to lumisToProcess.json
Log file is /home/dario/crab/local/z-submitted/crab_EGammaEXO_Run2018A_20240704_231147/crab.log

Singularity> wc crab_EGammaEXO_Run2018A_20240704_231147/results/failedLumis.json
    1  4151 25317 crab_EGammaEXO_Run2018A_20240704_231147/results/failedLumis.json
```

</details>

## Comment (cmsdmwmbot, 2024-07-12T15:07:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 11 warnings and errors that must be fixed
   * 41 comments to review
 * Pycodestyle check: succeeded
   * 45 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1065/artifact/artifacts/PullRequestReport.html
