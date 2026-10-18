# dmwm/CRABServer pull request #7888: remove all uses of -p, --parameter-set with cmsRun

State: closed
Opened: 2023-09-19T13:09:56Z
Closed: 2023-09-20T14:34:30Z
Merged: 2023-09-20T14:34:30Z
URL: https://github.com/dmwm/CRABServer/pull/7888

## Opening post (kpedro88, 2023-09-19T13:09:56Z)

This PR is the CRAB version of https://github.com/cms-sw/cmssw/pull/42798.

It is already unnecessary to use the `-p` or `--parameter-set` flag before specifying the `config.py` file for `cmsRun`, so this PR can be merged immediately with no change in functionality.

After https://github.com/cms-sw/cmssw/pull/42650 is merged, subsequent CMSSW releases will no longer support the `-p`, `--parameter-set` flags; the `config.py` file will always be provided as a positional argument. (This goes toward better command-line argument support following Python standards.)

## Comment (cmsdmwmbot, 2023-09-19T13:11:02Z)

Can one of the admins verify this patch?

## Comment (belforte, 2023-09-19T13:53:22Z)

thnaks @kpedro88 I'll take care. Please note that code in `test-old` is unused. But we'll need to fix documentation as well. I'll do it. But not today

## Comment (belforte, 2023-09-20T14:34:26Z)

very good, thanks @kpedro88

## Comment (belforte, 2023-09-21T15:56:41Z)

@kpedro88 this is now deployed on crab preprod instance, I have launched basic validation
but it is usable by others as well.
Simply put this in crabConfig.py
```
config.section_("General")
config.General.instance = 'preprod'
```
