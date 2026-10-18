# dmwm/CRABClient issue #5369: deprecate `--numcores` option for crab resubmit

State: closed
Opened: 2025-02-13T00:06:09Z
Closed: 2025-02-17T14:09:28Z
URL: https://github.com/dmwm/CRABClient/issues/5369

## Opening post (belforte, 2025-02-13T00:06:09Z)

1) it does not work . [ref](https://github.com/dmwm/CRABServer/issues/8910#issuecomment-2631061776)
2) it makes no sense. We enforce that numCores is equal to numThreads in PSet and PSet can't be changed at resubmit time.

It is not a matter of "giving a few jobs a kick" like with `--maxmemory` or `--maxjobruntime`

## Comment (belforte, 2025-02-13T09:20:01Z)

Hi @aspiringmind-code . I think it is good for you to start putting your hands in CRABClient. Action is simple here: remove the option and all related code.
Starting point:
https://github.com/dmwm/CRABClient/blob/8b8da2a40b2ee3bd8a9df03613ff291608262b56/src/python/CRABClient/Commands/resubmit.py#L234

A bit more work will be to clean up by removing support for this option in CRAB Server and DagmanResubmitter

## Comment (aspiringmind-code, 2025-02-17T12:32:56Z)

@belforte On the CRABServer side, would we also like to remove tm_numcores column from the Task table?

## Comment (belforte, 2025-02-17T13:27:17Z)

of course not. `num_cores` is needed when submitting. Simply it can't be changed afterwards, like most of the values in the Task table.

## Comment (aspiringmind-code, 2025-02-17T14:11:41Z)

I see, understood.
