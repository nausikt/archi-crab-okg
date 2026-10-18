# dmwm/CRABServer issue #7550: make a proposal on how to automatically flag suspicious files

State: closed
Opened: 2023-02-22T13:39:22Z
Closed: 2024-06-26T21:13:29Z
Labels: Priority: High, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7550

## Opening post (belforte, 2023-02-22T13:39:22Z)

When a job fails with a file read error which hint at a corrupted or truncated  file, this should be automatically made known to Rucio for automatic recovery.

Refers to https://github.com/dmwm/CMSRucio/issues/403 and builds on top of #7548 and #7549

## Comment (belforte, 2024-06-26T21:13:30Z)

this is currently "somehow" handled automatically via parsing logs in PostJob and making LFN list which DM crontab consumes. DM is looking into a better solution. Tracked in https://its.cern.ch/jira/browse/CMSTRANSF-883
