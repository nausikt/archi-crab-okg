# dmwm/CRABServer issue #7549: Investigate FJR to WMArchive to AMQ path

State: closed
Opened: 2023-02-22T13:30:54Z
Closed: 2024-06-26T21:02:34Z
Labels: Type: Question, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7549

## Opening post (belforte, 2023-02-22T13:30:54Z)

with ref. to https://github.com/dmwm/CMSRucio/issues/403 

* How does information like ExitCode and name of input file reach AMQ now, so that it can be used there for flagging file replicas which are suspected to be corrupted ?
* Can this be done inside the existing daemons ?
* Should we better plan to setup a different path ?
  * do in in the spider which feeds MONIT ? (can we make it talk to Rucio ?)
  * do it in CRAB's PostJob or task_wrapper ? (can we give it access to a Rucio account enabled to do ?)
  * some ad-hoc script/daemon/service  ?
  * can we make spiter/PJ/... simply send MSG's to AMS ?
 
Can/should do this in coordination with Yuyi, does it make sense for AMQ to receive messages and act ?

## Comment (belforte, 2023-06-30T17:46:19Z)

As of now.. I think this path is simply too much intricated

## Comment (belforte, 2024-06-26T21:02:34Z)

Investigation was done, and this route did not look viable
