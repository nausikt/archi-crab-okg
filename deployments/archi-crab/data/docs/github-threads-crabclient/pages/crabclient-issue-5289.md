# dmwm/CRABClient issue #5289: new preparelocal is not backward compatible

State: closed
Opened: 2024-01-30T21:48:01Z
Closed: 2024-04-26T13:54:45Z
Labels: bug, question, On Hold, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5289

## Opening post (belforte, 2024-01-30T21:48:01Z)

maybe we simply wait to deploy new client until new TW gas been in production for 1 month.

But maybe better to detect if CMSRunAnalysis.py can accept new argument `-json JobArgs-1.json` .

But.. how ?

## Comment (belforte, 2024-02-19T15:37:58Z)

The more I think about it, the more I believe we need to wait until all older tasks are gone.

The change in TW was introduced in [v3.240201](https://github.com/dmwm/CRABServer/releases/tag/v3.240201)
but that has not been deployed yet :-( although it passed validation on preprod.

@novicecpp @mapellidario let's think what more tests or urgent changes if any we need to TW and then update production this week.

## Comment (belforte, 2024-04-26T13:54:45Z)

we are waiting until all tasks are using new TW code
