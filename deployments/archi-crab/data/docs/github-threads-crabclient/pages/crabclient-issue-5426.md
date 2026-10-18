# dmwm/CRABClient issue #5426: deprecate distutils module to be able to support py3.12++

State: open
Opened: 2026-03-04T00:44:01Z
URL: https://github.com/dmwm/CRABClient/issues/5426

## Opening post (nausikt, 2026-03-04T00:44:01Z)

Regarding https://github.com/dmwm/CRABServer/issues/8956, making all CRAB code base support py3.12+

We have to revise how we [setup CRABClient](https://github.com/dmwm/CRABClient/blob/master/setup.py), steer away from distutils here may not trivial like my recent [CRABServer side PR](https://github.com/dmwm/CRABServer/pull/9260).

I'll have a look in details how we revised CRABServer setup and adopt a similar approach here.

## Comment (belforte, 2026-03-04T09:50:26Z)

I suspect that this `setup.py` is an old, obsolete thing. Of course we need to check with Shahzad on what exactly he does to deploy new CRABClient releases in CVMFS, but my understanding is that it is only a matter of GH cloning as per:
https://cmscrab.docs.cern.ch/crab-components/crab-client.html#using-crabclient-directly-from-your-github-repository

## Comment (belforte, 2026-03-04T09:52:29Z)

see e.g. https://github.com/cms-sw/cmsdist/blob/IB/CMSSW_16_1_X/master/crab-build.file
