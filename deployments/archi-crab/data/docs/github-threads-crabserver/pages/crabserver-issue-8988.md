# dmwm/CRABServer issue #8988: make it possible to build with WMCore 2.3.10 and later

State: closed
Opened: 2025-03-17T16:25:48Z
Closed: 2025-07-09T09:08:44Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8988

## Opening post (belforte, 2025-03-17T16:25:48Z)

It looks like we need to move [setup.py](https://github.com/dmwm/CRABServer/blob/master/setup.py) from `distutils` to `setuptools` 

reference: https://github.com/dmwm/WMCore/issues/12309

More could be needed.

As we put our hands in setup.py, an interesting option could also be to do like in the REST and do not build WMCore, but simply point $PYTHONPATH to the code (even using a zip archive like in the job wrapper). 

The move to setuptools will still be needed for python 3.12, but not having WMCore in the setup.py may make things simpler.

## Comment (belforte, 2025-03-17T16:31:01Z)

@aspiringmind-code @sinonkt dealing with these things is beyond my skill level. Please decide who of you will do and fix the assignement accordingly. I will be there to explain why and how we need WMCore, what we use from it etc. But do not really undersand how current setup.py works.

## Comment (aspiringmind-code, 2025-03-18T10:40:39Z)

Krittin and I decided that I can take this issue.

## Comment (aspiringmind-code, 2025-05-06T17:12:41Z)

Issue understood. CRAB will merge changes on its end after resolution of [WMCore Issue](https://github.com/dmwm/WMCore/issues/12358)

## Comment (belforte, 2025-07-08T14:55:27Z)

@aspiringmind-code is it possible that this was simply forgotten ? I presume that it would work now, or am I missing something ?

## Comment (aspiringmind-code, 2025-07-09T09:08:44Z)

Yes, this was[ fixed.](https://github.com/dmwm/CRABServer/pull/9081) Thanks!
