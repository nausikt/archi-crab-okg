# dmwm/CRABServer issue #8804: Python3.12 support: Use importlib instead of deprecated imp module 

State: closed
Opened: 2024-11-21T11:37:20Z
Closed: 2026-03-03T18:51:42Z
URL: https://github.com/dmwm/CRABServer/issues/8804

## Opening post (belforte, 2024-11-21T11:37:20Z)

In view of  deprecated `imp` being removed we need to make sure that server code does not use it.

Maybe also a good time to look into replacing use of `__import__()` with [importlib.import_module()](https://docs.python.org/3/library/importlib.html#importlib.import_module).

Better yet, try to run e.g. TW in a python3.12 container

reference: https://github.com/dmwm/CRABClient/pull/5350
