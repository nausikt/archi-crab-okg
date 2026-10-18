# dmwm/CRABServer issue #7841: allow tape recall of any data tier as long as size is small

State: closed
Opened: 2023-08-18T18:56:58Z
Closed: 2023-09-05T09:18:13Z
Labels: Type: Enhancement, Type: Support, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7841

## Opening post (belforte, 2023-08-18T18:56:58Z)

In the end, there's no point in asking users who want a small Alca/RAW/DQM/GEN... whatever to ask DataOps for small datasets.

It is OK to ask for a list of blocks in case the dataset is too big and then verify that the list is below a certain threshold, but when the full dataset is below that threshold.. why bother ?

This will limit requests on cms-talk/jira and overal save us time.

## Comment (belforte, 2023-08-18T18:58:06Z)

@novicecpp this seems a natural extension of the work which you did to support list of blocks, so hopefully it is OK for you to do. If not, feel free to assign to me.

## Comment (novicecpp, 2023-09-01T14:24:08Z)

Ref: https://cms-talk.web.cern.ch/t/stage-request-for-hi-virgin-raw-data/28554/3
