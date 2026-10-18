# dmwm/CRABServer issue #8955: migrate VM's to new hypervisors

State: closed
Opened: 2025-02-27T15:42:25Z
Closed: 2025-05-19T09:07:12Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8955

## Opening post (belforte, 2025-02-27T15:42:25Z)

see https://indico.cern.ch/event/1519112/contributions/6392454/attachments/3021998/5332144/250226%20-%20O&C%20Weekly%20News%20-%20v2.pdf slide 5

Ediz is coordinating this for CMS O&C

Many (all ?) CRAB VM's affected by this are schedulers, so migration can overlap and be coordinated with #8954 

@aspiringmind-code @sinonkt I leave it to you whether to work on this together or assign to just one. I have no idea of how much work is needed.
JUst keep in mind that if a VM needs to be cold migrated/rebuild we should be able to detach CEPH volumes and mount then on the new node.

## Comment (nausikt, 2025-05-19T09:07:12Z)

This issue considered to be done by us. Thanks! @aspiringmind-code's for helping around migrating the trickiest VM (crab-prod-tw01). @belforte
