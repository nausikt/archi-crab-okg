# dmwm/CRABServer issue #8497: add back a dummy condor_config file

State: closed
Opened: 2024-06-14T20:19:14Z
Closed: 2024-06-18T17:14:11Z
Labels: Status: Done, Area: HTCondor, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8497

## Opening post (belforte, 2024-06-14T20:19:14Z)

we used to have an empty `condor_config` file in TW.
Annoyed by that "stupid thing"  I removed it, since it sitll works.
But 
1. we get an annoying message every time we start it [1]
2. v2 bindings fail w/o it. HTC folks will fix it, but  I need it for testing.

[1]
```
/data/srv/TaskManager$ /usr/local/lib/python3.8/site-packages/htcondor/__init__.py:49: UserWarning: Neither the environment variable CONDOR_CONFIG, /etc/condor/, /usr/local/etc/, nor ~condor/ contain a condor_config source. Therefore, we are using a null condor_config.
  _warnings.warn(message)
```
