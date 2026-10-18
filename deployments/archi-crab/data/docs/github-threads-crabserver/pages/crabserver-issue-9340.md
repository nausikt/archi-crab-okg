# dmwm/CRABServer issue #9340: Reduce Redundance across short and long exit codes in RetryJob

State: closed
Opened: 2026-07-03T19:32:58Z
Closed: 2026-07-22T14:25:34Z
Labels: Type: Enhancement, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/9340

## Opening post (belforte, 2026-07-03T19:32:58Z)

https://github.com/dmwm/CRABServer/blob/7ae2e893a540c8044a108b0cd6a7f10b0e2cd690/src/python/TaskWorker/Actions/RetryJob.py#L22-L30

## Comment (belforte, 2026-07-13T12:53:08Z)

do we have to worry that short exit code may not be unique ?
Look for duplicates in the full list
```python
from WMExceptions import WM_JOB_ERROR_CODES

long2short={}
short2long={}
for ec in WM_JOB_ERROR_CODES:
    short = ec & 0xFF
    if short == ec:
        continue
    long2short[ec] = short
    if short in short2long:
        short2long[short].append(ec)
    else:
        short2long[short] = [ec]
print(f"all error codes in WM_JOB_ERROR_CODES: {len(WM_JOB_ERROR_CODES)}")
print(f"all long exit codes        : {len(long2short)}")
print(f"ambiguous short exit codes : {len(long2short) - len(short2long)}")
print("LIst of ambiguous short exit codes")
for s,long in short2long.items():
    if len(long) > 1:
        print(f"short ec {s} can come from {long}")
```

    all error codes in WM_JOB_ERROR_CODES: 160
    all long exit codes        : 116
    ambiguous short exit codes : 16
    LIst of ambiguous short exit codes
    short ec 88 can come from [7000, 8024]
    short ec 89 can come from [7001, 8025]
    short ec 90 can come from [7002, 8026]
    short ec 69 can come from [8005, 80453]
    short ec 72 can come from [8008, 99400]
    short ec 73 can come from [8009, 99401]
    short ec 81 can come from [8017, 50513]
    short ec 249 can come from [11001, 60409]
    short ec 190 can come from [50110, 71102]
    short ec 191 can come from [50111, 71103]
    short ec 193 can come from [50113, 71105]
    short ec 232 can come from [50664, 99304]
    short ec 233 can come from [50665, 99305]
    short ec 157 can come from [60317, 99997]
    short ec 158 can come from [60318, 99998]
    short ec 159 can come from [60319, 99999]

```python

```

* `[7000..7002]` likley obsolete, in case only used by WMCore 
* `11001` only used by WMCore
* `[71000.. -->]` only used by WMCore
8017: "ScheduleExecutionFailure."

Only **real duplicate** is our **`50513: "Failure to run SCRAM setup scripts." short exit code 81`**
which clashes with CMSSW's **`8017: "ScheduleExecutionFailure."`**. We do no set that in our code, but it may come from error in `Scram` class from WMCore.

## Comment (belforte, 2026-07-13T13:49:09Z)

we treat 8017 as fatal and 50513 as recoverable, so short exit code is not useful here. OTOH we very very seldom (never ?) need to look up short exit code anymore, so will list this one short exit code **81** explicitly with a comment and to be safe call it fatal.
