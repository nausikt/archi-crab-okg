# dmwm/CRABServer issue #8332: replace HTCondorUtils.quote/unquote with classad.(un)quote

State: closed
Opened: 2024-04-11T18:42:20Z
Closed: 2024-04-19T15:41:10Z
Labels: Priority: High, Status: In Progress, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8332

## Opening post (belforte, 2024-04-11T18:42:20Z)

there's non reason anymore to have our implementation, HTCondor classad library fully supports all classAd manipulations

## Comment (belforte, 2024-04-11T18:43:44Z)

do this as part of porting to new HTCondor bindings #8272 , since this is the time we put our hands in this part of the code and if we do not do it know, we may never do

## Comment (belforte, 2024-04-11T20:48:05Z)

There's more cleanup that can be done in classAd manipulation area.
I am putting some comments in DagmanSubmitter as a start
That may make all this part more readable.

After a bit of reading, that will come via #8336
