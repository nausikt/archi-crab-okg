# dmwm/CRABServer issue #8127: crab-dev client broken in IB

State: closed
Opened: 2023-12-19T22:18:14Z
Closed: 2023-12-20T09:22:17Z
Labels: Type: Bug, Status: In Progress, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8127

## Opening post (belforte, 2023-12-19T22:18:14Z)

while running Jenkins CCV on all releases, I found that submission does not work for crab dev (the default) when using python2 (CMSSW_10_1 or earlier).
``
21:36:47 Traceback (most recent call last):
21:36:47   File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02816/share/cms/crab-dev/v3.231204.00/bin/crab.py", line 17, in <module>
21:36:47     from ServerUtilities import FEEDBACKMAIL
21:36:47   File "/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02816/share/cms/crab-dev/v3.231204.00/lib/ServerUtilities.py", line 230
21:36:47     truncMsg += f"\n[... message truncated to the first {msgLimit - 100} chars ...]"
21:36:47                                                                                    ^
21:36:47 SyntaxError: invalid syntax`
``
this is the bug #8028 introduced in server v3.231171 and now fixed with #8030 

So I have asked for a rebuild of crab-dev in IB with latest server version v3,231215 https://github.com/cms-sw/cmsdist/pull/8899

## Comment (belforte, 2023-12-20T09:22:17Z)

fixed in last night IB. Thanks to Shahzad
