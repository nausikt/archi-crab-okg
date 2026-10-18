# dmwm/CRABServer issue #7661: expand tar archives in user sandbox

State: closed
Opened: 2023-06-12T14:00:47Z
Closed: 2023-07-01T13:09:25Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7661

## Opening post (belforte, 2023-06-12T14:00:47Z)

if user sandbox contains a tar archive, expand it.
Solves https://github.com/dmwm/CRABClient/issues/5198

## Comment (belforte, 2023-06-12T14:01:44Z)

do it now, so I close on requests for CRAB from Kevin.

## Comment (belforte, 2023-06-15T08:26:28Z)

relevant code is
https://github.com/dmwm/CRABServer/blob/f8177524190d57f89801f3bfa617d0cd31e88612/scripts/CMSRunAnalysis.py#L407-L417

Note that all sandbox files will be placed in $CMSSW_BASE directory in the worker node

## Comment (belforte, 2023-06-18T23:25:32Z)

as already noted in the CRABClient issue, the plan is:

look for files whose name contains `.tar.` or ends with `.tar` or `.tgz` or `.tbz`

## Comment (belforte, 2023-06-30T10:54:28Z)

I got it wrong.
User's `jobType.inputFiles` need to be expanded in `/srv` (the current working directory when the application is run)
see: https://github.com/dmwm/CRABServer/issues/7705

## Comment (belforte, 2023-07-01T13:09:25Z)

fixed via #7708
