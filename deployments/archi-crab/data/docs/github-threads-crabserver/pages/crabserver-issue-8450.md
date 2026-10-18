# dmwm/CRABServer issue #8450: avoid passing "bytes" to HTCondor when it expects strings

State: closed
Opened: 2024-05-31T15:06:57Z
Closed: 2024-05-31T15:22:36Z
URL: https://github.com/dmwm/CRABServer/issues/8450

## Opening post (belforte, 2024-05-31T15:06:57Z)

see point 1. in https://github.com/dmwm/CRABServer/issues/8272#issuecomment-1986511011

places to change
https://github.com/dmwm/CRABServer/blob/b12964501c116f758375c61389c6498c4baedb47/src/python/HTCondorLocator.py#L125
https://github.com/dmwm/CRABServer/blob/b12964501c116f758375c61389c6498c4baedb47/src/python/HTCondorLocator.py#L184
