# dmwm/CRABServer issue #7592: lock input data when task is submitted

State: closed
Opened: 2023-04-13T23:13:00Z
Closed: 2023-07-11T07:03:55Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7592

## Opening post (belforte, 2023-04-13T23:13:00Z)

- [x] do this in DBSDataDiscovery
 - [ ] use this chance to look at "clean up pylint complaints"
 - [ ] do we do it for RucioDataDiscovery as well ?

## Comment (belforte, 2023-07-01T13:10:25Z)

time to move to top of list

## Comment (belforte, 2023-07-07T17:40:10Z)

initial version passes initial test. Now:
 - [x] set correct expiration
 - [x] test with blocks list
 - [x] cleanup code
 - [x] improve messages
 - [x] deal with exceptions
 - [x] use a different Rucio account
 - [x] move recall and lock code outside DBSDataDiscovery - moved to #7733  
 - [x] extend to RucioDataDiscovery (after the above) - moved to #7734

## Comment (belforte, 2023-07-07T22:43:10Z)

tested in https://github.com/dmwm/CRABServer/issues/7728 before cleanup

## Comment (belforte, 2023-07-10T17:28:34Z)

Now using `crab_input` Rucio account: https://its.cern.ch/jira/browse/CMSTRANSF-655
