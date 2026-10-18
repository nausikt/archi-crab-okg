# dmwm/CRABServer issue #9370: odd-named task_statistics files in SPOOL_DIR

State: closed
Opened: 2026-07-28T17:29:16Z
Closed: 2026-07-29T07:28:26Z
URL: https://github.com/dmwm/CRABServer/issues/9370

## Opening post (belforte, 2026-07-28T17:29:16Z)

currently SPOOL_DIR almost always contains files like
```text
'task_statistics.$$([ifThenElse(GLIDEIN_CMSSite is undefined, "Unknown", GLIDEIN_CMSSite)]).FATAL_ERROR'
'task_statistics.$$([ifThenElse(GLIDEIN_CMSSite is undefined, "Unknown", GLIDEIN_CMSSite)]).RECOVERABLE_ERROR'
```
this is confusing, and annoying since makes `ls` to fall back to one file per line.

This is due to 
https://github.com/dmwm/CRABServer/blob/0a4d004e1d6d686e3496b62d62ca96061dd9c2cb/src/python/TaskWorker/Actions/RetryJob.py#L662-L663
which try to pick from the `finished_jobs/job.N.R` file a classAd which is defined via an expression.

Simple solution is to use a classAd which has the site name string, like
`
MATCH_GLIDEIN_CMSSite = "T2_CH_CERN"
`

## Comment (belforte, 2026-07-28T17:34:58Z)

take this chance to also improve comments and method name to make it easier to read
