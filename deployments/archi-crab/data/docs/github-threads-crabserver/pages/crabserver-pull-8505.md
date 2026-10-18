# dmwm/CRABServer pull request #8505: monit - use taskworker pypi image as base docker image for monitoring scripts

State: closed
Opened: 2024-06-17T12:49:05Z
Closed: 2024-06-19T09:46:57Z
Merged: 2024-06-19T09:46:57Z
Labels: Type: Question, Status: Done
URL: https://github.com/dmwm/CRABServer/pull/8505

## Opening post (mapellidario, 2024-06-17T12:49:05Z)

Fixes #8504 

## status

tested:

- images have been built and tagged in this pipeline [1]
- I run the script on crab-dev-tw02 [2] and data arrived in opensearch [3]

## details

I removed the old docker images, based on pure python and rpm taskworker.

I migrated the same logic to a new docker image inside `monit_pypi` directory.

I added a stage in the pipeline that builds the new monit docker image every time we build taskworker and crabserver images. it takes only 2min, but if this annoys people than we can add some logic to skip this build for most cases.

Every time we build a new monit image, it is tagged with `registry.cern.ch/cmscrab/crabtaskworker:${IMAGE_TAG}.monit` and pushed.

I added a new tag retention policy in harbor [4] so that we keep the latest 5 images that match `v3.*.monit`.

when the image tag matches `v3.*.*` (or better,, when the pipeline satisfies the rule `.default_rules["release"]`), the new monit image is also tagged with `registry.cern.ch/cmscrab/crabtaskworker:v3.latest.monit` and pushed. 

## open questions

I propose to change the crontabs to always use `v3.latest.monit`, so that we can forget about deploying the new docker images for the monitoring scripts, and embrace "continuous delivery" at its fullest :)

If we do not like to do this for production monitoring, I sugggest to at least do it with test monitoring, the one that currently runs in `crab-dev-tw04`. This can be a nice exercise for Vijay.

---

[1]

- https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7583357/builds

[2]

```bash
bash -x runContainer.sh -v v3.latest.monit -s TaskWorker_monit_generatemonit -c "python3 /data/srv/monit/GenerateMONIT.py"
bash -x runContainer.sh -v v3.latest.monit -s TaskWorker_monit_checktaperecall -c "python3 /data/srv/monit/CheckTapeRecall.py"
bash -x runContainer.sh -v v3.latest.monit -s TaskWorker_monit_asometrics -c "python3 /data/srv/monit/aso_metrics_ora.py"
bash -x runContainer.sh -v v3.latest.monit -s TaskWorker_monit_reportrecallquota -c "python3 /data/srv/monit/ReportRecallQuota.py"
```

[3]

https://monit-opensearch.cern.ch/dashboards/goto/8ec71c78057c6ea3150334053ae136ee

[4] 

> For the repositories matching crabtaskworker, retain the most recently pushed 5 artifacts with tags matching v3.*.monit

## Comment (cmsdmwmbot, 2024-06-17T12:55:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2021/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-17T14:35:07Z)

Dario, I can't possibly review the details here. But it looks that it is orthogonal to other things, so you can merge fearlessly. But I still do not understand why we need a different container image. What's wrong with the TW one ? Does `pip install pandas` conflict with other things ?

## Comment (mapellidario, 2024-06-18T14:02:15Z)

> What's wrong with the TW one 

I had a chat with wa, and for the time being we prefer to keep the image for monitoring separate from the TW one

## Comment (cmsdmwmbot, 2024-06-18T14:08:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2022/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-06-18T14:38:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2023/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-06-18T15:09:35Z)

@novicecpp I implemented your suggestions, thanks for the review :)

## Comment (cmsdmwmbot, 2024-06-18T15:10:38Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 12 comments to review
 * Pycodestyle check: succeeded
   * 71 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2024/artifact/artifacts/PullRequestReport.html
