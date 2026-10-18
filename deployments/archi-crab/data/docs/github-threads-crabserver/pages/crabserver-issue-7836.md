# dmwm/CRABServer issue #7836: adapt Publisher deploy to new Publisher_rucio

State: closed
Opened: 2023-08-17T14:19:54Z
Closed: 2023-08-18T11:53:28Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7836

## Opening post (belforte, 2023-08-17T14:19:54Z)

follow up on https://github.com/dmwm/CRABServer/issues/7770

## Comment (belforte, 2023-08-17T21:23:30Z)

made good progresses in https://github.com/belforte/CRABServer/tree/deploy-Publisher_rucio
need to cleanup a bit and split the part which is about the (previously missing/lost) integration of PublisherMasterRucio and TaskPublishRucio. Currently things work if there's no migration required. MIgrations fail, to be fixed, most likely some variable is not set correcly.

## Comment (belforte, 2023-08-18T11:46:58Z)

This is solved via https://github.com/dmwm/CRABServer/pull/7838 introducing new `RunPublisher.py` which takes as arguments `--service` to decide if to run Publisher_schedd or Publisher_rucio (as set by env. var `$SERVICE` in the container) and `--testMode` to decide if to run normally via a set of slave subprocresses or in sequential mode with no subprocessed.
