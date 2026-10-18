# dmwm/CRABClient issue #5216: Enable some configuration validation

State: closed
Opened: 2023-10-09T16:20:43Z
Closed: 2023-10-09T19:23:02Z
Labels: Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5216

## Opening post (belforte, 2023-10-09T16:20:43Z)

IN view of having deprecated params ( #5210 ) it is useful to add back some configuration validation.
I verified that this part works also in python3

https://github.com/dmwm/CRABClient/blob/3e3582d4738a400b29d291b9bc11897b943d029a/src/python/CRABClient/Commands/SubCommand.py#L151-L162

and this could be enabled to check for misstyped, only the `SpellChecker.correct` is broken in python3, but we can do w/o it
https://github.com/dmwm/CRABClient/blob/3e3582d4738a400b29d291b9bc11897b943d029a/src/python/CRABClient/Commands/SubCommand.py#L164-L174

while the part about type checking is where I stumbled when initially porting to python3 and that we can surely leave to python to raise exception when parameter type is not correct.

I also want to add a check for deprecated params

## Comment (belforte, 2023-10-09T19:23:03Z)

solved via https://github.com/dmwm/CRABClient/pull/5215
