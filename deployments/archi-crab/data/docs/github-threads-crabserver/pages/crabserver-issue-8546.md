# dmwm/CRABServer issue #8546: stop extending TapeRecall rule when data is on disk

State: closed
Opened: 2024-07-05T14:16:32Z
Closed: 2024-07-11T10:48:12Z
URL: https://github.com/dmwm/CRABServer/issues/8546

## Opening post (belforte, 2024-07-05T14:16:32Z)

Now dataset is locked on disk as soon as task is submitted. No need to extend TapeRecall rule for TASKLIFETIME days.
Something like "NOW + 4 days" will be plenty.
https://github.com/dmwm/CRABServer/blob/61ebff7ce5974ce98625d4f174b19e26da535a90/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L127-L129

## Comment (belforte, 2024-07-05T14:17:37Z)

more warming up exercise for you @aspiringmind-code :-)

## Comment (belforte, 2024-07-05T14:18:04Z)

and a way to start looking at Rucio too

## Comment (belforte, 2024-07-11T10:48:08Z)

closed via #8548
