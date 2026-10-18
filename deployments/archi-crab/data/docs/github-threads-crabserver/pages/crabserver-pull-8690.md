# dmwm/CRABServer pull request #8690: fix object has no attribute in manage.py

State: closed
Opened: 2024-09-04T16:41:58Z
Closed: 2024-09-04T16:42:32Z
Merged: 2024-09-04T16:42:32Z
URL: https://github.com/dmwm/CRABServer/pull/8690

## Opening post (novicecpp, 2024-09-04T16:41:58Z)

Sorry. My mistake.
```
crab3@crabserver-76dbff6cdc-8crj2:/data$ ./manage.py stop 
Traceback (most recent call last):
  File "./manage.py", line 65, in <module>
    env['SERVICE'] = args.service
AttributeError: 'Namespace' object has no attribute 'service'
```

I forgot that `args.service` will not available for the `stop, status, env` command.
