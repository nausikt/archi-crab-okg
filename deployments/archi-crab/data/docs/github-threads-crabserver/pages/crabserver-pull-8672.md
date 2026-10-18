# dmwm/CRABServer pull request #8672: spark monitoring cronjobs - a small refactor

State: closed
Opened: 2024-08-29T15:19:04Z
Closed: 2024-08-29T16:19:52Z
Merged: 2024-08-29T16:19:52Z
URL: https://github.com/dmwm/CRABServer/pull/8672

## Opening post (mapellidario, 2024-08-29T15:19:04Z)

This PR aims at refactoring a bit our spark cronjobs:

- we have a new docker image: registry.cern.ch/cmscrab/crabspark
- it is now possible to process more than one day calling a script only once [1]

I added all the data that comes from these jobs at [2] and i copied  couple of panels from there into "CRAB Overview"

[1]

it works with every script, i will use `crab_data_daily.py` as an example

```bash
docker run --rm --net=host -v /cvmfs:/cvmfs:shared \
  -v /data/certs/monit.d/monit_spark_crab.txt:/data/certs/monit.d/monit_spark_crab.txt \
  -v /data/certs/keytabs.d/cmscrab.keytab:/data/certs/keytabs.d/cmscrab.keytab \
  registry.cern.ch/cmscrab/crabspark:1723819475 \
  bash /data/srv/spark/run_spark.sh /data/srv/spark/crab_data_daily.py -s 2024-08-10 -e 2024-08-15
```

[2] https://monit-grafana.cern.ch/d/beac1005-c457-4423-8d24-714bab6c3a6a/user-dmapelli-crab-usage-spark?orgId=11

## Comment (cmsdmwmbot, 2024-08-29T15:23:04Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 81 warnings and errors that must be fixed
   * 172 comments to review
 * Pycodestyle check: succeeded
   * 203 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2133/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-08-29T16:19:46Z)

Had a chat with wa, he is ok with merging this PR and in taking care of this in the future :) thanks man! <3

## Comment (cmsdmwmbot, 2024-08-29T16:20:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2134/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-30T07:59:02Z)

thanks @mapellidario I like the new dashboard and have added two more to overview.
