# dmwm/CRABServer pull request #8853: CMSSW multi microarch support: set env after sandbox extraction

State: closed
Opened: 2024-12-02T16:19:59Z
Closed: 2024-12-02T17:00:40Z
Merged: 2024-12-02T17:00:40Z
URL: https://github.com/dmwm/CRABServer/pull/8853

## Opening post (smuzaffar, 2024-12-02T16:19:59Z)

@belforte , for multi microarch enabled CMSSW, scram runtime env should be set after the sandbox extraction. This will allow scram to select the correct/best micro arch.

This change should not break existing cmssw. Setting up scram runtime just after scram project or after extracting the sandbox should behave the same way for non-multi microarch releases.

## Comment (cmsdmwmbot, 2024-12-02T16:21:02Z)

Can one of the admins verify this patch?

## Comment (belforte, 2024-12-02T17:00:37Z)

thanks @smuzaffar 
looks good to merge

## Comment (smuzaffar, 2024-12-05T13:41:14Z)

thanks @belforte .

By the way, is this already deployed on crab dev server? I would like to test it for [new IB](https://github.com/dmwm/WMCore/issues/12168#issuecomment-2520351777)

## Comment (belforte, 2024-12-05T13:55:03Z)

sorry for my confusion. This is already deployed in production now.

## Comment (smuzaffar, 2024-12-05T14:08:24Z)

great, thanks @belforte
