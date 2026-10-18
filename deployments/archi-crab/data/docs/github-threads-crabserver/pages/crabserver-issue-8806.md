# dmwm/CRABServer issue #8806: add a canary (qa) deployment for TW

State: closed
Opened: 2024-11-21T16:05:22Z
Closed: 2024-12-06T13:52:26Z
URL: https://github.com/dmwm/CRABServer/issues/8806

## Opening post (belforte, 2024-11-21T16:05:22Z)

with ref to #8650 

@aspiringmind-code and @belforte had a chat today. Here's notes to guide development:

## Design in words

At very high level we decide which TW is master and which canary and the fraction to be sent. This goes in the conifg. And everything else is “implementation”

Master(primary) TW does scheduling and marks some tasks (up to 2*Nslaves at every poll cycle) with status HOLDING and its TWNAME. We want to change so that X% of those tasks end up with the canary TW name instead.

## Implementation guidelines

### Configuration params:
* I am the master TW (could be the default)
* I am a canary (qa) TW (call it secondary or slave) (default is no)
* If I am master:
   * A param has the name of the canary
   * A param has the fraction to send to the canary


### MasterWorker changes:
* If I am master:
   * _selectWork (move tasks from WAIT to NEW)
   * _lockWork (change to HOLDING and put TWname in DB) changes (1)
   * New step (if we decide to add) (2) 
   * _getWork (3) (picks tasks in HOLDING with my TW name in the DB)
   * One of (1) (2) (3) needs to be changed to send X% of tasks to the canary by setting status HOLDING and canary TW name
* If I am Canary:
   * Skip _selectWork and _lockWork. Only do _getWork and following steps

### Extra niceties
* keep track in DB task table if this task was processed  by the primary or the canary TW ? Where does it help ? we already have the TW name
* keep track in DB task table of the version of the TW used to process this task ? still some work.. is it useful ?
* the I-am-master and I-am-slave params are mutually exclusive, can (should?) easily check in TW code, but do we also want something puppet-side to make sure that we do not run two master at same time ? Do we need it ?

## Comment (aspiringmind-code, 2024-11-22T11:30:39Z)

Configuration and implementation can be seen [here](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/292) and [here](https://github.com/dmwm/CRABServer/pull/8808)

## Comment (belforte, 2024-12-06T13:52:26Z)

done and deployed
