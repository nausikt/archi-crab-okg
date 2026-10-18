# dmwm/CRABServer issue #8110: Latest WMCore broke jobwrapper 

State: closed
Opened: 2023-12-18T00:33:48Z
Closed: 2024-04-24T12:36:14Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8110

## Opening post (novicecpp, 2023-12-18T00:33:48Z)

I tried to run latest WMCore's master with patch from https://github.com/dmwm/WMCore/pull/11790 and found error in jobwrapper:

```
==== FAILURE WHEN LOADING WMCORE AT Sun Dec 17 23:24:40 2023 UTC ====
Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 585, in <module>
    from WMCore.WMRuntime.Bootstrap import setupLogging
  File "<frozen zipimport>", line 259, in load_module
  File "/srv/WMCore.zip/WMCore/WMRuntime/Bootstrap.py", line 28, in <module>
    from WMCore.BossAir.Plugins.BasePlugin import BasePlugin
ModuleNotFoundError: No module named 'WMCore.BossAir'
```
From https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231217_231359:tseethon_crab_20231218_001357/job_out.1.2.txt

Import `BossAir` in `WMRuntime/Bootstrap.py` was introduced in https://github.com/dmwm/WMCore/pull/11812.
It maybe just simple as `crabtaskworker` [WMCore's build_system](https://github.com/dmwm/WMCore/blob/87ea437f508308b5e1d544a234a80e2a9911d5c1/setup_dependencies.py#L222C1-L226) did not include `WMCore.BossAir` package.

I will open PR to WMCore later (after new year).

## Comment (novicecpp, 2023-12-18T01:59:15Z)

I have added `WMCore.BossAir` to `crabtaskworker` in https://github.com/novicecpp/WMCore/commit/98f570d7e8c34a84222bda99d4ecac76049b771d and now it is working fine.

https://cmsweb.cern.ch:8443/scheddmon/059/tseethon/231218_002532:tseethon_crab_20231218_012531/job_out.8.0.txt

## Comment (belforte, 2024-02-19T15:44:03Z)

@novicecpp should we change the dependency in WMCore master then ? IIUC this means that we will need to wait for a new WMCore release with that in order to build again.
Picking up specific changes aside (like storage.json or support for rhel9) it is good to use current production WMCore release.

## Comment (novicecpp, 2024-02-19T15:44:55Z)

~~No, see https://github.com/dmwm/CRABServer/issues/8110.~~

Sorry, I thought this is CRABClient issue.

## Comment (belforte, 2024-02-19T15:48:52Z)

OK. Let's keep it open then

## Comment (novicecpp, 2024-02-19T15:56:43Z)

In summary, we cannot bump to latest version until this issue is resolved.

## Comment (belforte, 2024-02-19T18:25:48Z)

Let's open a PR for WMCore then

## Comment (belforte, 2024-04-24T10:26:58Z)

@novicecpp can we close this ?

## Comment (novicecpp, 2024-04-24T12:36:14Z)

Yes! Thanks.
