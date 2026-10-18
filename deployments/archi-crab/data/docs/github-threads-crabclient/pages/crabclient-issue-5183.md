# dmwm/CRABClient issue #5183:  fix getLumiListInValidFiles

State: closed
Opened: 2023-01-11T19:13:11Z
Closed: 2023-01-11T19:17:25Z
Labels: HighPrio, Py2/3
URL: https://github.com/dmwm/CRABClient/issues/5183

## Opening post (belforte, 2023-01-11T19:13:11Z)

https://github.com/dmwm/CRABClient/blob/b6102286e0f166f8a433778c5c05590f5a3cf731/src/python/CRABClient/UserUtilities.py#L1440

it is based on old python2 DBSClient which is broken with new go-based server.
Easiest is to port it to python3 (there may be some indentation to fix) so that it will work once we stop distributing old DBS client. Then we have to warn users who try to use it in python2.

Rewriting with dasgoclient to make it work anywhere is likely an overkill.

## Comment (belforte, 2023-01-11T19:17:25Z)

duplicate of #5175 which is a better solution
