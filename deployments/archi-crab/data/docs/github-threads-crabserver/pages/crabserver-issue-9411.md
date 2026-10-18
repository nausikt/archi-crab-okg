# dmwm/CRABServer issue #9411: add node specific condor shedd customization to puppet

State: open
Opened: 2026-09-03T16:25:53Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9411

## Opening post (belforte, 2026-09-03T16:25:53Z)

after creating https://its.cern.ch/jira/browse/CMSSI-165 I realized that the customization has to be in the repository for the node's hostgroup, not necessarely in SI repository.

So we can go ahead and introduce this in our own repo, just like we use out hostgroup to push `90_jobrouter.config` to all `crabschedd`s.
