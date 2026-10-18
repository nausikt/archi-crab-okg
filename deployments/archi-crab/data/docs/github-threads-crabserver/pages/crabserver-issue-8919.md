# dmwm/CRABServer issue #8919: Consistently use My.<ad> everywhere

State: closed
Opened: 2025-02-13T08:12:38Z
Closed: 2025-02-13T20:37:16Z
URL: https://github.com/dmwm/CRABServer/issues/8919

## Opening post (belforte, 2025-02-13T08:12:38Z)

as done already in DagmanCreator and DagmanSubmitter, stop using the old `+` in front when we define classAd to be passed to a job

## Comment (belforte, 2025-02-13T20:31:28Z)

took this change to also fix log file naming for subdags. Maybe the way it was coded worked with ancient condor. But now subdags log was in `default.dagman.out` instead of `RunJobs0.subdag.dagman.out`

![Image](https://github.com/user-attachments/assets/0b23abd7-1bf7-430f-857c-ad7df46a4d49)
