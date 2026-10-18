# dmwm/CRABServer issue #8794: StatusTracking should handle tail jobs in automatic splitting

State: closed
Opened: 2024-11-14T13:58:41Z
Closed: 2024-11-15T19:17:54Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8794

## Opening post (belforte, 2024-11-14T13:58:41Z)

if procssing step fails, but task completes via the tail jobs, the ST script does not notice but keeps seeing a failed job in the status summary and tries to resubmit. So test is stuck forever in "testResubmitted" even if task is OK.

## Comment (belforte, 2024-11-15T10:49:22Z)

this was triggered by https://cmsweb-testbed.cern.ch/crabserver/ui/task/241113_203248%3Acrabint1_crab_20241113_213248
even after I made it complete successfully, the CI pipeline test was failing

## Comment (belforte, 2024-11-15T11:04:45Z)

At first sigh one problem is here
https://github.com/dmwm/CRABServer/blob/6a3754dd8e4478e1dd10a8e9bd1c74918881248d/cicd/gitlab/st/statusTracking.py#L39-L42
that code removes also tail jobs, which is not what the comment says

## Comment (belforte, 2024-11-15T11:53:04Z)

But the real problem is that this script test is based on job counting. In this case there are 5 probes (one failing), 1 processing (failed), one tail (OK). Namely
```text
(Pdb) status_command_output['jobsPerStatus']
{'finished': 5, 'failed': 2}
(Pdb) status_command_output['jobList']
[['finished', '0-5'], ['finished', '0-3'], ['failed', '0-4'], ['finished', '0-1'], ['finished', '0-2'], ['failed', '1'], ['finished', '1-1']]
(Pdb) 
```

Need some smarter logic to tell that "yes, one job failed, but tail stage took care".  Of course we can't gliss over failed tails like done for probes, but if we sometimes run a larger task with automatic splitting will also face the problem that there can be multiple tail stages and number of jobs is not defined.

## Comment (belforte, 2024-11-15T12:01:22Z)

maybe "as simple as"
- if there's any jobid 0-x , call it automatic
- if automatic, check if all processing were OK, if not check that all tails are OK
