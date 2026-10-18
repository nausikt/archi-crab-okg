# dmwm/CRABServer issue #9034: lower MAX_POST default value from 20 to 10

State: closed
Opened: 2025-04-07T16:50:31Z
Closed: 2025-04-08T16:05:37Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9034

## Opening post (belforte, 2025-04-07T16:50:31Z)

We recently hit some scale limitation in I/O and memory on schedulers. 
A source was in a high rate of job complete/start (or fail/restart !) resulting in a lot of PostJobs running at same time.

Lowering the number of concurrently running PostJobs for a task from 20 to 10 is expected to help by spreading that load over more time, while there should be no significant degradation on "performance". Delay resubmission of failed jobs can only help, and for successful jobs the only effect is a bit of delay in submisson to ASO which anyhow takes O(hours).

While this is controlled also in TaskWorker python configuration, a proper, documented, value in the code will help.
