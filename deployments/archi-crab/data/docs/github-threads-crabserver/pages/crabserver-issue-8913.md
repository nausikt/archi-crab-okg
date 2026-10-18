# dmwm/CRABServer issue #8913: StatusTracking test is failing to notice that  automatic splitting is completed

State: closed
Opened: 2025-02-04T08:09:46Z
Closed: 2025-02-12T13:31:50Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8913

## Opening post (belforte, 2025-02-04T08:09:46Z)

{'TN': '250203_234034:crabint1_crab_20250204_004032', 'testResult': 'TestRunning', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1, 'probe': 5, 'rescheduled': 0}, 'publication (fail/tdb/DBS)': '0/1/1'}

why is that classified as TestRunning ??

## Comment (belforte, 2025-02-04T11:34:27Z)

I executed [statusTracking.py](https://github.com/dmwm/CRABServer/blob/master/cicd/gitlab/st/statusTracking.py) interactively on lxplus8, and got
 
{'TN': '250203_234034:crabint1_crab_20250204_004032', 'testResult': 'TestPassed', 'dbStatus': 'SUBMITTED', 'combinedStatus': 'COMPLETED', 'jobsPerStatus': {'finished': 1, 'probe': 5, 'rescheduled': 0}, 'publication (fail/tdb/DBS)': '0/1/1'}

Puzzling.

## Comment (belforte, 2025-02-04T11:48:55Z)

I re-run the test in the pipeline, and it sitll says `TestRunning`. pfff....

## Comment (belforte, 2025-02-04T17:31:49Z)

I think problem is here, for automatic splitting total jobs and jobs to publish are 1 (the only processing job) but the code reduces by 1 for each of the 5 probe jobs, so after those lines `jobsToPublish` is `-4` !
https://github.com/dmwm/CRABServer/blob/d9bea5aefdd6dd288d6a288534ee3798069b6c74/cicd/gitlab/st/statusTracking.py#L72-L77

I suspect this was introduced  when I fixed https://github.com/dmwm/CRABServer/issues/8794 

a quick mitigation will be to disable check for publication in the YAML file, while code is changed/tested/built
https://github.com/dmwm/CRABServer/blob/d9bea5aefdd6dd288d6a288534ee3798069b6c74/.gitlab-ci.yml#L379

## Comment (belforte, 2025-02-04T17:36:36Z)

assigning to @aspiringmind-code as he expressed interest in fixing it.

When I did my initial test on lxplus I had publication check disabled :-(

Setting the correct env.var and putting the automatic splitting task name in `$WORK_DIR/ submitted_tasks_TS`  allows to reproduce this with `python3 statusTracking.py`

## Comment (aspiringmind-code, 2025-02-12T13:31:51Z)

The problem was probe jobs being subtracted twice. Fixed in [PR](https://github.com/dmwm/CRABServer/pull/8915)
