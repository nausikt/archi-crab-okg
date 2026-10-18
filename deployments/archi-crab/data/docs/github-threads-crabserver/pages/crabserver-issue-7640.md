# dmwm/CRABServer issue #7640: properly report failure to access datasets on T3_CH_CERNBOX

State: closed
Opened: 2023-05-24T07:44:34Z
Closed: 2023-05-24T15:03:24Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7640

## Opening post (belforte, 2023-05-24T07:44:34Z)

see
https://cms-talk.web.cern.ch/t/crab-submitfailed-with-message-no-locations-found-for-dataset/24558/2

current message is confusing

The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset '/ste1_GENSIM/toakhter-ste1_GENSIM-684b129ece2da2a1e4721679166b15e5/USER'. (or at least for the part of the dataset that passed the lumi-mask and/or run-range selection). 

should be something like
```
input dataset located on CERNBOX. Can not be accessed via CRAB
```

## Comment (belforte, 2023-05-24T07:45:30Z)

It is not a top priority, but since I a working on DBSDataDiscovery now, let's do it while I have code at my fingertips
