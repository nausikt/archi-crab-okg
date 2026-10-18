# dmwm/CRABServer issue #9060: add target RSE to tape recall table

State: closed
Opened: 2025-05-01T10:53:23Z
Closed: 2025-05-08T15:46:07Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9060

## Opening post (belforte, 2025-05-01T10:53:23Z)

with ref to our table or pending tape recalls 

![Image](https://github.com/user-attachments/assets/51a40b61-7ad0-47b8-bae4-2eb22211bc29)

and to discussion in [Apr 30th meeting](https://indico.cern.ch/event/1543469/)

Add a column next to `Tape` with the destination RSE.

To keep things fit, maybe shorten the ruleId ?

Since all our rules have a single RSE as destination if should be enough to look up the first lock in the rule. Unless a better idea comes from [MatterMostd](https://mattermost.web.cern.ch/cms-o-and-c/pl/tfmhj95sspd3xe44o7ncuecbsr)

FYI @KatyEllis

## Comment (belforte, 2025-05-01T10:56:08Z)

@aspiringmind-code maybe something for the summer student ? The Rucio part will be on you/me, but then there's something to learn about OpenSearch and Grafana. Surely not enough to fill 2 months, but if we stay with "monitoring" it could be part of a list of tasks.

## Comment (belforte, 2025-05-08T08:47:45Z)

example after the change (from test dashboard)

![Image](https://github.com/user-attachments/assets/cd21fd22-20b4-4a34-ae9a-902549e8080c)
