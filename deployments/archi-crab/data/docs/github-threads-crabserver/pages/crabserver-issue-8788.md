# dmwm/CRABServer issue #8788: improve error reporting from GenerateMONIT

State: closed
Opened: 2024-11-13T17:47:21Z
Closed: 2024-11-15T19:18:12Z
Labels: Type: Enhancement, Type: Support, Status: Done
URL: https://github.com/dmwm/CRABServer/issues/8788

## Opening post (belforte, 2024-11-13T17:47:21Z)

we only get mails with
```text
Lock created. Start data collection
Traceback (most recent call last):
  File "/data/srv/monit/GenerateMONIT.py", line 413, in <module>
    main()
  File "/data/srv/monit/GenerateMONIT.py", line 395, in main
    metrics = pr.execute()
  File "/data/srv/monit/GenerateMONIT.py", line 292, in execute
    schedd = htcondor.Schedd(scheddAdd)
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_schedd.py", line 81, in __init__
    location = c.locate(DaemonType.Schedd)
  File "/usr/local/lib/python3.8/site-packages/htcondor2/_collector.py", line 174, in locate
    return _collector_locate_local(self, self._handle, int(daemon_type))
RuntimeError: Unable to locate local daemon.
```

should at least tell which schedd gave the error
