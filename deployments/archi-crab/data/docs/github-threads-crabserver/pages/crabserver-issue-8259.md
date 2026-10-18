# dmwm/CRABServer issue #8259: extra () in FTS_Transfers.py

State: closed
Opened: 2024-02-23T09:43:04Z
Closed: 2024-02-27T19:53:52Z
URL: https://github.com/dmwm/CRABServer/issues/8259

## Opening post (belforte, 2024-02-23T09:43:04Z)

accidental discovery. It is not fatal, but annoying
```
TypeError: not enough arguments for format string
Call stack:
  File "task_process/FTS_Transfers.py", line 653, in <module>
    algorithm()
  File "task_process/FTS_Transfers.py", line 643, in algorithm
    jobs_ongoing = state_manager(ftsContext, crabserver)
  File "task_process/FTS_Transfers.py", line 520, in state_manager
    check_FTSJob(logging, ftsContext, jobid, jobsEnded, jobs_ongoing, done_id, failed_id, failed_reasons)
  File "task_process/FTS_Transfers.py", line 169, in check_FTSJob
    logger.info("State of job %s: %s", (jobid, status["job_state"]))
Message: 'State of job %s: %s'
Arguments: (('e096ddd0-d22b-11ee-aa63-fa163e172462', 'FINISHED'),)
```
