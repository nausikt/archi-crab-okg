# cms-sw/cmsdist issue #8566: setup of DBS_CLIENT via CRAB broken in CMSSW 12 +

State: closed
Opened: 2023-06-23T16:41:50Z
Closed: 2023-06-28T07:02:42Z
Labels: pending-assignment
URL: https://github.com/cms-sw/cmsdist/issues/8566

## Opening post (belforte, 2023-06-23T16:41:50Z)

this line
https://github.com/cms-sw/cmsdist/blob/d34e50e14f8a0cb4bd911942ecb1f14586451923/crab/crab-setup.sh.file#L15
fails becasue `python` can not be found resulting in an annoying message.

Rather than fixing for python3, I propose to remove this, since old [DBS Client](http://github.com/dmwm/DBS) is not compatible with current DBS server. 
We should also stop pulling in old DBS Client in https://github.com/cms-sw/cmsdist/blob/IB/CMSSW_13_2_X/master/crab-build.file

@smuzaffar if you agree I will make a PR for both files and the crab-prod/pre/dev spec files

## Comment (cmsbuild, 2023-06-23T16:42:12Z)

A new Issue was created by  @belforte Stefano Belforte.

@Dr15Jones, @perrotta, @dpiparo, @rappoccio, @makortel, @smuzaffar can you please review it and eventually sign/assign? Thanks.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-issues.html">here</a>

## Comment (smuzaffar, 2023-06-24T11:25:42Z)

@belforte , I have no objections, if you think this is not going to break crab/dbs then please go ahead and open a PR
