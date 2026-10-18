# dmwm/CRABServer issue #8561: Change entrypoint of Publisher process to simple binary script

State: closed
Opened: 2024-07-25T12:39:25Z
Closed: 2024-07-26T10:26:58Z
URL: https://github.com/dmwm/CRABServer/issues/8561

## Opening post (novicecpp, 2024-07-25T12:39:25Z)

Relate to https://github.com/dmwm/CRABServer/issues/8540 but this time is for Publisher.

Some code changes are needed:
- Make the args name consistence for both TW and PB, i.e., replace `--testMode` with `--sequential/pdb/console`.
- Fix import path. For example https://github.com/dmwm/CRABServer/blob/92b017fa77241833f684bdc1aa9104577540dc65/src/python/Publisher/PublisherMaster.py#L30-L31
    It works because we run PB with command `python3 /path/to/RunPublisher.py`, so basedir of `RunPublisher.py`, `/path/to`, is automatically included in `PYTHONPATH`. 
- Also include a simple fix of https://github.com/dmwm/CRABServer/issues/8442
