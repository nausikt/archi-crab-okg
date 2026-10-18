# dmwm/CRABServer issue #8366: Set FRONTIER_ID variable 

State: closed
Opened: 2024-04-29T14:59:00Z
Closed: 2024-04-29T17:25:05Z
URL: https://github.com/dmwm/CRABServer/issues/8366

## Opening post (vzokay, 2024-04-29T14:59:00Z)

Hello,

The Frontier team would like to ask for the addition of an environmental variable `FRONTIER_ID` in CRAB jobs. The reason for this is to get more information in our logs in order to diagnose intermittent slowdowns we've observed with some jobs in the last couple of months. 
As mentioned during a chat with @mapellidario, this is already done in WMAgent, to which he quickly found the relevant PR: 
   * dmwm/WMCore#5038 

Thank you @mapellidario @belforte for looking into this and for your time!

All the best,
Vaiva

## Comment (belforte, 2024-04-29T15:12:45Z)

Do I understand correctly that `FRONTIER_ID` should be set before starting `cmsRun` with value
`CRAB <taskanme>` ?

e.g.
```
CRAB 240425_061854:xiaoyul_crab_20240425_081720
```

## Comment (vzokay, 2024-04-29T16:02:33Z)

Thank you for your prompt response! I'm passing Dave D's message:

> That would work.  Actually it would improve our squid log parsing a little bit if there wasn't a space in it, since the wmagent id doesn't have one.  So either delete the space or replace it with an underscore or hyphen

## Comment (belforte, 2024-04-29T16:11:45Z)

Doesn't Dave D. have a GH account so we can speed up communication w/o bother 3rd parties (you) ?

OK. I will add an hyphen `-`

## Comment (belforte, 2024-04-29T16:19:27Z)

now it is
`CRAB-240425_061854:xiaoyul_crab_20240425_081720`

## Comment (vzokay, 2024-04-29T16:32:02Z)

Sure, apologies for the inconvenience.
Passing it over to @DrDaveD
