# dmwm/CRABServer issue #8480: overflow to T1 broken

State: closed
Opened: 2024-06-06T14:05:25Z
Closed: 2024-06-07T10:36:18Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8480

## Opening post (belforte, 2024-06-06T14:05:25Z)

it is not working since a while
![image](https://github.com/dmwm/CRABServer/assets/1837785/6f0f079e-3c05-4b8c-8314-64e932041d0e)

I think it was broken my me in March when I removed creation of `/etc/condor/config.d/90_jobrouter.config` in puppet https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/2a3422ba2d3b8101414bc9606d67331bce3d4b94

So even if we have `enable_overflow: true` in the `data/fqdns/vocms*.yaml` files, the condor config. variable `JAT_ENABLE_OVERFLOW` is not set and JobAutoTuner log has
```
2024-04-08 13:08:04,345:INFO:JobAutoTuner,261:============  JobAutoTuner-py3 starting ==============
2024-04-08 13:08:04,345:ERROR:JobAutoTuner,70:ERR: Could not find/read the config parameter: JAT_ENABLE_OVERFLOW. Not enabling the service! Additional info: Config key not set in condor.
2024-04-08 13:08:04,345:INFO:JobAutoTuner,272:-------------------- Overflow.py was not enabled  --------------------
```

More changes are needed, because when I set it to True via 99_local_tweaks, log is
```
2024-06-06 15:58:20,328:INFO:JobAutoTuner,264:-------------------- Routes added by Overflow.py  --------------------
2024-06-06 15:58:20,328:INFO:JobAutoTuner,107:=================== An Overflow object instance start! ===================
2024-06-06 15:58:20,897:ERROR:JobAutoTuner,82:ERR: SubScriptAlarm: at: 2024-06-06 15:58:20.897397 / additional info: 
Overflow failed with exception: 'ServerTime'
Exception: None
Traceback (most recent call last):
  File "/data/srv/crab/JobAutoTuner.py", line 267, in main
    overflow.run()
  File "/data/srv/crab/JobAutoTuner.py", line 256, in run
    self.overflow(jobsInThisSchedd)
  File "/data/srv/crab/JobAutoTuner.py", line 210, in overflow
    if self.needOverflow(jobObj):
  File "/data/srv/crab/JobAutoTuner.py", line 177, in needOverflow
    currIdleTime = jobObject["ServerTime"] - jobObject["QDate"]
KeyError: 'ServerTime'
2024-06-06 15:58:20,905:INFO:JobAutoTuner,273:===================================================================
```
So two action items, and no quick solution:
- [x] find simplest way pass enable_oveflow flag from hiera to JobAutoTuner and implement it
- [x] fix JobAutoTuner.py code  (`ServerTime is supposed to [exist](https://htcondor.readthedocs.io/en/latest/classad-attributes/job-classad-attributes.html#ServerTime) )

## Comment (belforte, 2024-06-06T14:08:17Z)

the problem with ServerTime is very strange, it **is** always defined
```
belforte@vocms0137/crab> condor_q -con 'jobuniverse==5&&jobstatus==1' -af servertime|uniq
1717682834
belforte@vocms0137/crab> 
```
seems problem with python bindings. There was a bug in HTC that made it go missing, was fixed in 10.0.2 https://htcondor.readthedocs.io/en/v10_0/version-history/lts-versions-10-0.html#version-10-0-2

yet...
```
[crabtw@vocms0137 ~]$ python3
Python 3.9.18 (main, Jan 24 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> htcondor.version()
'$CondorVersion: 10.2.0 2023-01-05 BuildID: 621409 PackageID: 10.2.0-1 $'
>>> constraint="jobuniverse==5"
>>> projection=['ServerTime']
>>> sk=htcondor.Schedd()
>>> rr=sk.query(constraint, projection)
>>> rr[0]
[  ]
>>> 
```
while from my account, where I have more recent bindings in my local
```
belforte@vocms0137/~> python3
Python 3.9.18 (main, Jan 24 2024, 00:00:00) 
[GCC 11.4.1 20231218 (Red Hat 11.4.1-3)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import htcondor
>>> htcondor.version()
'$CondorVersion: 23.7.2 2024-05-16 BuildID: UW_Python_Wheel_Build $'
>>> constraint="jobuniverse==5"
>>> projection=['ServerTime']
>>> sk=htcondor.Schedd()
>>> rr=sk.query(constraint, projection)
>>> rr[0]
[ ServerTime = 1717687105 ]
>>> 
```
looks like 10.2.0 is some separate branch (non LTS) which did not get the fix.

Of course we could use `time.time()` instead, since script runs on same machine as the scheduler, no reason to ask the scheduler what the time is !

## Comment (belforte, 2024-06-07T10:36:19Z)

puppet hiera fixed via
* https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/905544d208813fac37b5bd9e8a9c00c27e3ea3a6
* https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/8e9ace19586b87255f4bef784ac3468f6c1cb57a
Things are OK now
![image](https://github.com/dmwm/CRABServer/assets/1837785/bc7fc358-25df-4669-ad3f-3abed59fe097)
