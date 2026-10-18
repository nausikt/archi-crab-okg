# dmwm/CRABServer issue #9181: add httokendecode to JobWrapper

State: closed
Opened: 2025-09-08T20:33:40Z
Closed: 2025-09-09T10:13:50Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9181

## Opening post (belforte, 2025-09-08T20:33:40Z)

looks like there's no progress in getting httokendecode added to our containers.
Since it is useful to check token in the job wrapper and it is a 150-line bash script, I am copying it from lxplus and adding to our JobWrapper.
Will be easy to remove once we have a more proper way to make it available via either gWms or CMSSW singularity.
