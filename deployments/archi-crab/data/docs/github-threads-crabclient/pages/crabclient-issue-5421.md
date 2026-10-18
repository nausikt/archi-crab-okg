# dmwm/CRABClient issue #5421: adapt crab submit --dryrun to new arguments passing

State: closed
Opened: 2025-10-17T15:03:07Z
Closed: 2025-10-20T09:33:58Z
Labels: bug, Done, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5421

## Opening post (belforte, 2025-10-17T15:03:07Z)

with latest TW `crab submit --dryrun` fails with
```text
Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 661, in <module>
    options = parseArgs()
  File "CMSRunAnalysis.py", line 318, in parseArgs
    print("userSandbox:   ", input_params.userSandbox)
AttributeError: 'Values' object has no attribute 'userSandbox'
```

most like;u this line which "executes the dry run" does not work anymore
https://github.com/dmwm/CRABClient/blob/cf12e7446250e5518d2cba98e046eacf808b2387/src/python/CRABClient/Commands/submit.py#L473

becasue `CMSRunAnalysis.py` now only accepts the `--jobId` as argument

dryrun needs to edit arguments to change number of events to run on.

Some changes are needed

## Comment (belforte, 2025-10-20T09:33:58Z)

Closed via #5422
