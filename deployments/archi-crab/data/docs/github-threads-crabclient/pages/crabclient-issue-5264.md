# dmwm/CRABClient issue #5264: need to use python2 for CMSSWS_10_1

State: closed
Opened: 2023-11-30T22:01:30Z
Closed: 2023-12-01T09:50:37Z
Labels: bug, critical
URL: https://github.com/dmwm/CRABClient/issues/5264

## Opening post (belforte, 2023-11-30T22:01:30Z)

it has python3 but not `past`.
In my previous tests I was fooled by having `past` in my `.local` so that `from past.builtins import basestring` was still working. Ref  https://github.com/dmwm/CRABServer/issues/8041

## Comment (belforte, 2023-12-01T09:28:21Z)

fix was wrong, see https://github.com/dmwm/CRABServer/issues/8048#issuecomment-1834884308
