# dmwm/CRABServer issue #9215: Change submission classAds from CUDA* to DESIRED_GPU*

State: closed
Opened: 2025-10-14T15:33:21Z
Closed: 2026-01-22T10:01:03Z
Labels: Type: Bug
URL: https://github.com/dmwm/CRABServer/issues/9215

## Opening post (belforte, 2025-10-14T15:33:21Z)

along the lines of what done already for WMA.
References:
https://github.com/dmwm/WMCore/issues/12437
which is about "number, not strings" as a correction on
https://github.com/dmwm/WMCore/issues/11942#issuecomment-3049044064

see also
https://mattermost.web.cern.ch/cms-o-and-c/pl/9donquy4pi8s3yoz8oufse6bco
and replies to it

Check with SI for more details.

This is likely also a proper time to document the `task['tm_user_config','acceleratorparams']`
i.e. `Site.acceleratorparams` in crabConfig.py

## Comment (belforte, 2025-10-14T15:42:36Z)

@nausikt priority/urgency of this is unclear atm. See the thread in MM. I am not aware of any user trying to use GPU via CRAB yet. But there's a general "we live in AI world" feeling that this may happen at some point. We have been in this "feeling" for > 1 year now. Nothing visible has happened yet.

## Comment (nausikt, 2025-10-14T15:44:07Z)

Okk, Acknowledged Stefano! will do it asap before/after `crab recovery`

## Comment (belforte, 2025-10-15T08:52:17Z)

after quick chat with @mmascher  in MatterMost:
* I am not sure that DESIRED_gpu_minimum_capability needs to be specified if no requested  by user. 
* If user wants to indicate, eventually we need to have a string representing a float or an integer, like minimumCapability="1.2" or "3" (so we do not  try in crabConfig to parse integer vs. float) and do `jobSubmit['MY.Desired_gpu_minimum_capability']=minumCapability`
* if a default is needed, IIUC we can use `jobSubmit['MY.Desired_gpu_minimum_capability']="0"`

## Comment (belforte, 2025-12-18T15:03:23Z)

I got it all wrong about what we should set in classAd !!!!
Please see
https://cms-talk.web.cern.ch/t/exclude-certain-cuda-devices-when-running-crab-with-requireaccelerator-true/140075/15
and posts right before/after that.

Note that MY..... are still needed, but will be used for monitoring not matching !
See also
https://github.com/dmwm/WMCore/commit/7d6e7d5f460d2e4eb34f99846d706a1da2e2aa8e

## Comment (belforte, 2025-12-18T15:04:56Z)

@nausikt I am about to leave for my Holiday, and will not have time to study and understand. I suspect Marco will also not be available, so I am not sure that it is worth for you to spend time on this now.
We can go back to this in January

## Comment (nausikt, 2025-12-18T17:05:27Z)

> [@nausikt](https://github.com/nausikt) I am about to leave for my Holiday, and will not have time to study and understand. I suspect Marco will also not be available, so I am not sure that it is worth for you to spend time on this now. We can go back to this in January

Thank you for your tireless user support, behalf of us so far!

Please, take your long due *well-deserved* break. Go fully signed off! and let me hold the fort—allow me to try my best to address users issues if there's any after these.

*P.S. Also, please *No Worry*! for a few of my upcoming PRs that we will review them later together in January, I just want to get it done for peace of mind, bring proper closure to my 2025 year, otherwise i will forget them LoL*
