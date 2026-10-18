# dmwm/CRABServer pull request #8143: use self.rucioClient inside internal method. Fix #8140

State: closed
Opened: 2024-01-10T20:20:19Z
Closed: 2024-01-11T15:31:39Z
Merged: 2024-01-11T15:31:39Z
URL: https://github.com/dmwm/CRABServer/pull/8143

## Opening post (belforte, 2024-01-10T20:20:19Z)

currently deployed on crab-preprod-tw01 and tested with the problem report use case
see https://github.com/dmwm/CRABServer/issues/8140#issuecomment-1885657627

## Comment (cmsdmwmbot, 2024-01-10T20:22:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1788/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-01-10T20:31:57Z)

also tested on a dataset on tape (instead of a list of blocks) and worked (using a dataset already being recalled)
https://cmsweb-testbed.cern.ch/crabserver/ui/task/240110_202807%3Abelforte_crab_20240110_212805
https://cms-rucio-webui.cern.ch/rule?rule_id=266ec34985f64a4cb8e75eca889bab5d

I think  its clear to go.

## Comment (belforte, 2024-01-10T20:32:03Z)

also tested on a dataset on tape (instead of a list of blocks) and worked (using a dataset already being recalled)
https://cmsweb-testbed.cern.ch/crabserver/ui/task/240110_202807%3Abelforte_crab_20240110_212805
https://cms-rucio-webui.cern.ch/rule?rule_id=266ec34985f64a4cb8e75eca889bab5d

I think  its clear to go.

## Comment (belforte, 2024-01-10T21:03:41Z)

@mapellidario it would be great if you can have a final look tomorrow morning so we can tag, build and deploy by the end of the week, ideally tomorrow.
