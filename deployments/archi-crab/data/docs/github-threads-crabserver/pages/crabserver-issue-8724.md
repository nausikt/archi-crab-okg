# dmwm/CRABServer issue #8724: `ddm_quota` is deprecated, use `dm_weight`

State: closed
Opened: 2024-09-27T08:26:28Z
Closed: 2024-11-01T15:17:41Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8724

## Opening post (belforte, 2024-09-27T08:26:28Z)

and while we are at this, do not rely only on `ddm_weight=0` to avoid test RSE's, but explicitely avoid RSE's of type TEST

should modify

https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/RucioActions.py#L119

https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/RucioActions.py#L68

## Comment (amaltaro, 2024-09-27T10:51:09Z)

@belforte in case it makes your life easier, the expression to avoid Test RSEs that we have implemented in WMCore uses `\cms_type=test`, e.g.:
```
"rse_type=TAPE&wmcore_output_tape=True\cms_type=test"
```
HTH.

## Comment (belforte, 2024-09-27T13:20:31Z)

it does help, thanks !  in particular the reminder about the special use of `\` !

## Comment (belforte, 2024-11-01T12:41:51Z)

sounds like a good day to do this

## Comment (belforte, 2024-11-01T14:13:18Z)

https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/RucioActions.py#L119
changed to
```python
allRses = r"(tier=1|tier=2)&rse_type=DISK\cms_type=test\cms_type=temp"
```

## Comment (belforte, 2024-11-01T15:17:13Z)

closed via https://github.com/dmwm/CRABServer/pull/8762
