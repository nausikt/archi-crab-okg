# dmwm/CRABServer issue #9342: reduce lifetime of MINI* locking to 6 months

State: closed
Opened: 2026-07-06T13:06:00Z
Closed: 2026-07-22T14:25:11Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9342

## Opening post (belforte, 2026-07-06T13:06:00Z)

in https://github.com/dmwm/CRABServer/blob/7ae2e893a540c8044a108b0cd6a7f10b0e2cd690/src/python/TaskWorker/Actions/RucioActions.py#L292-L298

FYI @haozturk 

Let me know when to do, or wheter to close w/o doing, or change to a different lifetime

## Comment (belforte, 2026-07-06T13:07:22Z)

On Hold waiting for instructions from DM

## Comment (belforte, 2026-07-21T13:53:58Z)

DM decided to go ahead with this change https://its.cern.ch/jira/browse/CMSTRANSF-1379
I have asked them which exact `lifetime` value (in seconds) they'd like to use
[answer](https://its.cern.ch/jira/browse/CMSTRANSF-1379?focusedId=7401979&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-7401979) is `86400*30*6`
