# dmwm/CRABClient issue #5385: add config param Data.lumisPerFile

State: closed
Opened: 2025-04-29T09:22:04Z
Closed: 2025-05-06T07:53:56Z
Labels: enhancement, HighPrio, In Progress
URL: https://github.com/dmwm/CRABClient/issues/5385

## Opening post (belforte, 2025-04-29T09:22:04Z)

to be used for PrivateMC, defaults to 1. Will override the default `eventsPerLumi=100`

Users may be able to specify either. But I am also considering deprecating eventsPerLumi.

To avoid changes in server side, we can keep using `evetnsperlumi` in the submission HTTP query, so the client code can do the transformation.

The aim is to avoid tasks with outlandish number of lumis per file/block which add load to DBS and Publisher w/o reason, https://github.com/dmwm/CRABServer/issues/9058

## Comment (belforte, 2025-04-29T14:59:55Z)

users polled in https://cms-talk.web.cern.ch/t/changes-to-craclient/124290

I have also e-mailed directly the 34 users who set a custom value for `eventsPerLumi` in their tasks during 2025

## Comment (belforte, 2025-04-29T16:42:10Z)

now 1 lumi per file is the default.
I am very tempted to remove the old eventsPerLumi.

## Comment (belforte, 2025-05-04T12:50:41Z)

we wait one week for user comments, than deprecate `eventsPerLumi` and introduce the new `lumisPerFile` with default=1
