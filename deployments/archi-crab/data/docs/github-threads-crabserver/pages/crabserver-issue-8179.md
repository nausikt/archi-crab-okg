# dmwm/CRABServer issue #8179: Jenkins tests for Rucio ASO fail to submit with dev client

State: closed
Opened: 2024-01-12T15:04:21Z
Closed: 2024-01-12T15:14:45Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/8179

## Opening post (belforte, 2024-01-12T15:04:21Z)

error is
```
Will use CRAB configuration file ./rucio_transfers.py Error while loading CRAB configuration: cannot import name 'getUsernameFromCRIC' from 'CRABClient.UserUtilities'
```

which is "natural" since that method was moved to ClientUtilities and users are supposed to use `getUsername` and be happily ignorant about whether we get that from CRIC , IAM, SSO, or wherever else in the future.

That decision to go make user only use `getUsername` is so old in my mind that I am suprised that it was only finalized in v3.231201
https://github.com/dmwm/CRABClient/commit/317824c1730669e5ecccd38d57ee3e76211a6227#diff-d027900a9545b3917b2fff49bbe456f602712944d04744da4c02ccdb6fab863c

Anyhow, this is easy to fix.
