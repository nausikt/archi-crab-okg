# dmwm/CRABServer pull request #9237: Clean up all externalconfig references, centralconfig and conn_handlers.

State: closed
Opened: 2025-12-02T10:01:59Z
Closed: 2025-12-03T15:48:35Z
Merged: 2025-12-03T15:48:35Z
URL: https://github.com/dmwm/CRABServer/pull/9237

## Opening post (nausikt, 2025-12-02T10:01:59Z)

This PR will take care the rest of [remove CRAB Server external_config](https://github.com/dmwm/CRABServer/issues/9167)
Resolves: #9167, #9220

## Tests:
- [x] Normal Task: [251202_090645:kphornsi_crab_test14-dryrun-20251202-final-test-deprecated-externalconfig](https://cmsweb-test14.cern.ch/crabserver/ui/task/251202_090645%3Akphornsi_crab_test14-dryrun-20251202-final-test-deprecated-externalconfig)
- [x] ITB Collector task: [251202_095223:kphornsi_crab_test14-itb-collector-vocms069-20251202-final-test-deprecated-externalconfig](https://cmsweb-test14.cern.ch/crabserver/ui/task/251202_095223%3Akphornsi_crab_test14-itb-collector-vocms069-20251202-final-test-deprecated-externalconfig) [[grafana](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=251202_095223%3Akphornsi_crab_test14-itb-collector-vocms069-20251202-final-test-deprecated-externalconfig&from=1764665543000&to=now)]
*P.S. task remain correctly scheduled/submitted to specific pool/collector as expected*
```python
config.section_("Debug")
config.Debug.scheddName = 'crab3@vocms069.cern.ch'
config.Debug.collector = 'cmsgwms-collector-itb.cern.ch'
# config.Debug.collector = 'cmsgwms-collector-itb.cern.ch,cmsgwms-collector-itb.fnal.gov"
```
- [x] AS Task: [251202_091550:kphornsi_crab_test14-automatic-splitting-deprecate-externalconfig](https://cmsweb-test14.cern.ch/crabserver/ui/task/251202_091550%3Akphornsi_crab_test14-automatic-splitting-deprecate-externalconfig)
*P.S. somehow, AS got **Status on the scheduler:	FAILED**?? stuck at running and not proceeding further, just intermittent?*
- [x] Regression tests via pipeline: [13496473](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13496473)
## ProxiedURL
tested, all works well as following. 
[1] CRAB REST Log
```
2025-12-02 10:35:32,192:bjmoHIqRFJXa:INFO:RESTTask:ProxiedUrl for task 251202_090645:kphornsi_crab_test14-dryrun-20251202-final-test-deprecated-externalconfig is: https://cmsweb.cern.ch/scheddmon/0155/kphornsi/251202_090645:kphornsi_crab_test14-dryrun-20251202-final-test-deprecated-externalconfig
```
[2] When we would like to retrieved JobLog/PostJob at Grafana
<img width="1492" height="568" alt="Screenshot 2025-12-02 at 16 41 49" src="https://github.com/user-attachments/assets/e97601a8-26ef-4058-9499-b8c46e01ab25" />

[3] Valid ProxiedURL extracted/reconstructed from `row.schedd` w/o having to consult externalconfig on REST side.
<img width="1419" height="904" alt="Screenshot 2025-12-02 at 16 41 58" src="https://github.com/user-attachments/assets/3331ff5e-8c10-40a7-8177-930c99b2ef6b" />

## Comment (cmsdmwmbot, 2025-12-02T10:07:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 9 warnings
   * 100 comments to review
 * Pycodestyle check: succeeded
   * 593 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2686/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-03T10:13:26Z)

Automatic Splitting failed for what looks like a bug in TW code https://cmsweb.cern.ch/scheddmon/0198/kphornsi/251202_091550:kphornsi_crab_test14-automatic-splitting-deprecate-externalconfig/AutomaticSplitting_Log0.txt

Please do not call things intermittent w/o proof that they are so. Did you run a successful AS task ?

Most likely the bug is not due to your changes. But when things fail, we need to investigate

## Comment (nausikt, 2025-12-03T10:34:09Z)

Acknowledge Stefano, this one is NOT, but i used to successfully run AS tasks.

## Comment (belforte, 2025-12-03T10:42:52Z)

I guess that the successes were before latest changes from Vijay :-(

## Comment (belforte, 2025-12-03T10:43:39Z)

thank for having tested those !

## Comment (nausikt, 2025-12-03T10:44:39Z)

Did vijay proposed last week changes? https://github.com/dmwm/CRABServer/commit/87cc42320ac3eee4c505e3f649b3d754c0c8517a

## Comment (belforte, 2025-12-03T10:46:38Z)

hmm... not. That was clearly me !!! Sorry for blaming him so carelessly. But I thought I looked at changes in master and missed my thing. Sorry. I clearly made a mistake.

## Comment (nausikt, 2025-12-03T10:50:05Z)

OK, I can patch & test it for you in this PR na.
if you ok with configFIleNaming in other stages e.g. processing, and else. to be
```
dagConfigFileName = "RunJobs.dag.config" # probe, conventional
dagConfigFileName = "RunJobs0.subdag.config" # processing 
dagConfigFileName = f"RunJobs{parentDag}.subdag.config" # else
```

## Comment (belforte, 2025-12-03T10:59:16Z)

I prefer that we roll back my change and I prepare e new, tested, PR

## Comment (nausikt, 2025-12-03T11:00:20Z)

Roger that, let me take care of rollback.

## Comment (belforte, 2025-12-03T11:01:22Z)

thanks for taking care of the rollback

## Comment (nausikt, 2025-12-03T11:16:09Z)

Man, @belforte  No worries, Nothing need to be rollback.

Both canary/primary still living with [v3.251015](https://github.com/dmwm/CRABServer/releases/tag/v3.251015) [[releases](https://github.com/dmwm/CRABServer/releases)]
```
[kphornsi@crab-prod-tw01 ~]$ docker ps
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED        STATUS        PORTS     NAMES
892f63b17793   registry.cern.ch/cmscrab/crabtaskworker:v3.251015-stable   "tini -- /data/run.sh"   6 weeks ago    Up 6 weeks              Publisher_rucio
c034fdb108f8   registry.cern.ch/cmscrab/crabtaskworker:v3.251015-stable   "tini -- /data/run.sh"   6 weeks ago    Up 6 weeks              Publisher_schedd
d5d4e97a688b   registry.cern.ch/cmscrab/crabtaskworker:v3.251015-stable   "tini -- /data/run.sh"   6 weeks ago    Up 13 days              TaskWorker
be0a42347940   registry.cern.ch/cmscrab/crabtwfilebeat:v3.latest          "tini -- /usr/share/…"   7 months ago   Up 7 months             crabtwfilebeat
[kphornsi@crab-prod-tw02 ~]$ docker ps
CONTAINER ID   IMAGE                                                      COMMAND                  CREATED         STATUS         PORTS     NAMES
752e8f7cb7e7   registry.cern.ch/cmscrab/crabtaskworker:v3.251015-stable   "tini -- /data/run.sh"   6 weeks ago     Up 13 days               TaskWorker
5f0f578ddf35   registry.cern.ch/cmscrab/crabtwfilebeat:v3.latest          "tini -- /usr/share/…"   16 months ago   Up 16 months             crabtwfilebeat
```

major Resubmission Refactoring [#9228](https://github.com/dmwm/CRABServer/pull/9228) was in [v3.251119](https://github.com/dmwm/CRABServer/releases/tag/v3.251119) (2 weeks ago...)

## Comment (belforte, 2025-12-03T13:27:33Z)

Yeah. I know we run a good version. Sorry, my bad, I meant "revert", not "roll back". So that we have a better working master (even if the resubmit refactoring in master is not really working on all cases).
Done in https://github.com/dmwm/CRABServer/pull/9239

## Comment (nausikt, 2025-12-03T14:39:51Z)

Forgive my blunt, i should realized that you meant reverted.

I've tested, its looks good but not completed yet...
AS Task: [251203_134539:kphornsi_crab_test14-automatic-splitting-deprecate-externalconfig-2](https://cmsweb-test14.cern.ch/crabserver/ui/task/251203_134539%3Akphornsi_crab_test14-automatic-splitting-deprecate-externalconfig-2) [[Grafana](https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=251203_134539%3Akphornsi_crab_test14-automatic-splitting-deprecate-externalconfig-2&from=1764765940000&to=now)]
Regression test via pipeline: [13507437](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/13507437)

## Comment (belforte, 2025-12-03T14:41:10Z)

Thanks, this looks good. Yet changes are in a lot of places and a bit hard to fully digest. We will have to rely on testing. I see a few places where we can simplify things, like there's no point in keeping the `backendurls` thing around, but better to leave for after this change has "settled".

## Comment (belforte, 2025-12-03T14:43:49Z)

Please fix the unused imports before merging. Even better if you can reach the pint where pylint does not report any error.

## Comment (cmsdmwmbot, 2025-12-03T15:02:07Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 3 warnings and errors that must be fixed
   * 9 warnings
   * 95 comments to review
 * Pycodestyle check: succeeded
   * 594 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2688/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-12-03T15:09:34Z)

The last 3 pylint errors, touch/affect underlining abstract/class structure. IMO better leave them like that for future major clean-up.

## Comment (belforte, 2025-12-03T15:40:13Z)

Yes, pylint situation is as godd as it can now. And at least not worse than before. We do not want to fix old code which works :-)
Feel free to merge
