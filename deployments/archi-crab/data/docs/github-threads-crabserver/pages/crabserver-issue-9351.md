# dmwm/CRABServer issue #9351: make it clear when job stdout is missing

State: closed
Opened: 2026-07-17T09:34:28Z
Closed: 2026-07-17T11:50:53Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9351

## Opening post (belforte, 2026-07-17T09:34:28Z)

currently we have a "fake" job_out.X.Y.txt file with
```text
Job output has not been processed by post-job.
```
which is almost OK while waiting for job to run/end. But if output is missing it becomes confusing
