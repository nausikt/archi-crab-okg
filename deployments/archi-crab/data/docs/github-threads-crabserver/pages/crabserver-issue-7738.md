# dmwm/CRABServer issue #7738: add creation of /home/crab3/logs in TW

State: closed
Opened: 2023-07-10T17:53:41Z
Closed: 2024-02-07T10:45:35Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7738

## Opening post (belforte, 2023-07-10T17:53:41Z)

after I issued `ai-rebuild crab-prod-tw0` the GenerateMONIT crontab was not running (no data in Grafana).

I tested running interactively and error was
```
crab3@crab-prod-tw01 ~]$ python /home/crab3/GenerateMONIT.py
Traceback (most recent call last):
  File "/home/crab3/GenerateMONIT.py", line 394, in <module>
    main()
  File "/home/crab3/GenerateMONIT.py", line 310, in main
    handler = logging.FileHandler(logdir + logfile)
  File "/data/srv/TaskManager/v3.210429/slc7_amd64_gcc630/external/python/2.7.13-comp2/lib/python2.7/logging/__init__.py", line 913, in __init__
    StreamHandler.__init__(self, self._open())
  File "/data/srv/TaskManager/v3.210429/slc7_amd64_gcc630/external/python/2.7.13-comp2/lib/python2.7/logging/__init__.py", line 943, in _open
    stream = open(self.baseFilename, self.mode)
IOError: [Errno 2] No such file or directory: '/home/crab3/logs/GenMonit-20237.log'
[crab3@crab-prod-tw01 ~]$ 
```
Looks like code could not create the `logs` dir. Things worked after `mkdir logs`.
- [ ]  Either do this in puppet, or modify GenerateMONIT.py code

Also
- [x] why where we not getting mails about crontab failing ? something wrong in puppet ?

## Comment (belforte, 2023-07-10T21:33:38Z)

the lack of mails is explained by this "very aggressive" piece of the crobtab
```
python /home/crab3/GenerateMONIT.py >/dev/null 2>&1
```
we can do better

## Comment (belforte, 2024-02-07T10:45:35Z)

we move GenerateMonit to docker, will take care in there
