# dmwm/CRABServer pull request #9297: Allow sites to force ASO via Rucio. Fix #9294

State: closed
Opened: 2026-04-12T16:12:11Z
Closed: 2026-04-14T23:20:47Z
Merged: 2026-04-14T23:20:47Z
URL: https://github.com/dmwm/CRABServer/pull/9297

## Opening post (belforte, 2026-04-12T16:12:11Z)

took this chance to make code a bit more readable by introducing
```python
 asoSite = self.task['tm_asyncdest']
 asoLfn = self.task['tm_output_lfn']
```

## Comment (cmsdmwmbot, 2026-04-12T16:17:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2787/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-12T19:58:11Z)

i expect that it user's specified ASO site is not correct submission will be refused.
If that's not the case, there's a mistake in the code logic to fix :-)

Or do you worry about a missing storage destination in the crab configuration file ?

## Comment (belforte, 2026-04-12T20:08:54Z)

`config.site.storageSite` is a mandatory configuration parameter in CRAB configuration file.

## Comment (nausikt, 2026-04-12T20:30:02Z)

Roger that, understood.

## Comment (cmsdmwmbot, 2026-04-13T09:23:08Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2789/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-14T17:22:07Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2791/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-14T17:22:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2792/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-04-14T17:23:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 6 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2793/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-04-14T17:25:21Z)

@dciangot after latest commit
```console
belforte@lxplus802/TC3> crab status 
Rucio client intialized for account belforte
CRAB project directory:		/afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20260414_192224
Task name:			260414_172226:belforte_crab_20260414_192224
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw01
Status on the CRAB server:	SUBMITREFUSED
Task URL to use for HELP:	https://cmsweb-test2.cern.ch/crabserver/ui/task/260414_172226%3Abelforte_crab_20260414_192224
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=belforte&var-task=260414_172226%3Abelforte_crab_20260414_192224&from=1776183746000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_CH_CERN_P5', 'T2_CH_CERN_HLT', 'T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			You are using T2_IT_Rome as output destination
				but that site only accepts output to be sent via Rucio
				You must change your crab configuration python file to make sure that
				config.Data.outLFNDirBase starts with /store/user/rucio/ or /store/group/rucio
				More info in https://twiki.cern.ch/twiki/bin/view/CMSPublic/CrabASOwithRucio
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab_20260414_192224/crab.log
belforte@lxplus802/TC3> 
```

## Comment (dciangot, 2026-04-14T21:42:19Z)

LGTM!

## Comment (belforte, 2026-04-14T23:20:42Z)

thanks Diego. Merging. We'll tag an deploy. Let us know when some site is ready for the switch.
