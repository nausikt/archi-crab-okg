# dmwm/CRABServer issue #7527: remove hack now that partialDataset=True is available

State: open
Opened: 2023-02-09T22:50:52Z
Labels: Priority: Medium, Status: Available, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7527

## Opening post (belforte, 2023-02-09T22:50:52Z)

this should go with the `elseif` at the bottom becoming an `if`
https://github.com/dmwm/CRABServer/blob/c484c2377476c3eeca32207fc4d2117bfdf714e2/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L429-L442
