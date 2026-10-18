# dmwm/CRABServer issue #9232: cleanup resubmission arguments

State: open
Opened: 2025-11-17T11:27:25Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9232

## Opening post (belforte, 2025-11-17T11:27:25Z)

it appears that in current code base a list of jobids is always passed from client to server at `crab resubmit` time.
This should be verified.
And if true we can remove code server side which tries to allow for the jobids to be something different from a list.
E.g.
https://github.com/dmwm/CRABServer/blob/be1912644dee64bd6d543b152b2e74c6e939e371/scripts/dagman/AdjustSites.py#L553-L559
