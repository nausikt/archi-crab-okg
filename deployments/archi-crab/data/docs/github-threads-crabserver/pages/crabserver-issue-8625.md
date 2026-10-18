# dmwm/CRABServer issue #8625: odd race condition when using voms-proxy-info in TW

State: closed
Opened: 2024-08-15T09:09:24Z
Closed: 2024-09-04T14:02:54Z
Labels: Type: Bug, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/8625

## Opening post (belforte, 2024-08-15T09:09:24Z)

`Problem handling 240814_001706:ecannaer_crab_clustAlg_Suu4_chi1p5_WBHT_2016_nom_AltDatasets_000 because of invalid literal for int() with base 10: '[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/760874 because it is locked by another process (errno = 11)\\n447504' failure, traceback follows\nTraceback (most recent call last):\n  File "/usr/local/lib/python3.8/site-packages/WMCore/Credential/Proxy.py", line 738, in getTimeLeft\n    timeLeft = int(timeLeftLocal.strip())\nValueError: invalid literal for int() with base 10: '[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/760874 because it is locked by another process (errno = 11)\\n447504'\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 96, in executeAction\n    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)\n  File "/data/srv/current/lib\n[... message truncated to the first 1000 chars ...]`

## Comment (belforte, 2024-08-16T15:31:06Z)

in this case WMCore/Credential/Proxy failes because of a problem with `/tmp/hsperfdata_crab3/760874`    
that is a file created by [JavaVM](https://stackoverflow.com/a/2655306)

It is true that `voms-proxi-*` is now a Java application, but one would have thought that it was possible to run two instances at same time. Of course if the file is named after the user `crab3` and the lock owned by the process (the TW slave) there is a chance that different processes try to use it at same time :-(

From [reading around]() it looks like this can only be disabled with a Java option, i.e. inside voms-proxy* commands themselves. I.e, should be reported as a bug to voms-proxy-utils developers.

Maybe... just maybe,the problem is that WMCore/Credential/Proxy.py tries to parse the output of `voms-proxy-info -timeleft` assuming it is a number of seconds. But in this case a warning line is inserted and the is stdout
```
[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/760874 because it is locked by another process (errno = 11)
447504
``` 
while the exit code is still 0

The only improvement I can imagine is to add `tail -1` to
```python
timeLeftCmd = 'voms-proxy-info -file ' + proxy + ' -timeleft'
```
in https://github.com/dmwm/WMCore/blob/39c50491199ff505886caed4ab1d3661844b2329/src/python/WMCore/Credential/Proxy.py#L731

## Comment (belforte, 2024-08-17T10:21:44Z)

Need to be fixed in WMCore, I created issue and PR
 https://github.com/dmwm/WMCore/issues/12075 and https://github.com/dmwm/WMCore/pull/12076

## Comment (belforte, 2024-08-26T19:53:59Z)

same problems happens also in the chain
https://github.com/dmwm/CRABServer/blob/085885f202f307bb0720e127d5ffeb5c4fe5c4b7/src/python/TaskWorker/Actions/MyProxyLogon.py#L38
which calls (as in example which triggered this issue)
https://github.com/dmwm/WMCore/blob/d618b120c6189cb8d9c89e28f202b440ab6f2bae/src/python/WMCore/Credential/Proxy.py#L722
but if the first `voms-proxy-info -timeleft` is OK there is another call in
https://github.com/dmwm/WMCore/blob/d618b120c6189cb8d9c89e28f202b440ab6f2bae/src/python/WMCore/Credential/Proxy.py#L757
via
https://github.com/dmwm/WMCore/blob/d618b120c6189cb8d9c89e28f202b440ab6f2bae/src/python/WMCore/Credential/Proxy.py#L743

which at times can give same error
```
2024-08-26 21:20:27,861:ERROR:Handler:Problem handling 240816_093326:gcoulon_crab_Analysis_2018_HSCPgmsbStau_M-308_CodeV1p1_v1 because of invalid literal for int() with base 10: '[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/3201703 because it is locked by another process (errno = 11)\n568368\n' failure, traceback follows
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/WMCore/Credential/Proxy.py", line 776, in getVomsLife
    result = int(ACtimeLeftLocal)
ValueError: invalid literal for int() with base 10: '[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/3201703 because it is locked by another process (errno = 11)\n568368\n'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/Handler.py", line 96, in executeAction
    output = work.execute(nextinput, task=self.task, tempDir=self.tempDir)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/MyProxyLogon.py", line 80, in execute
    (userproxy, usergroups) = self.tryProxyLogon(proxycfg=proxycfg)
  File "/data/srv/current/lib/python/site-packages/TaskWorker/Actions/MyProxyLogon.py", line 38, in tryProxyLogon
    timeleft = proxy.getTimeLeft(userproxy)  # this is the way to tell if proxy creation succeeded
  File "/usr/local/lib/python3.8/site-packages/WMCore/Credential/Proxy.py", line 755, in getTimeLeft
    ACTimeLeftLocal = self.getVomsLife(proxy)
  File "/usr/local/lib/python3.8/site-packages/WMCore/Credential/Proxy.py", line 778, in getVomsLife
    result = sum(int(x) * 60 ** i for i, x in enumerate(reversed(ACtimeLeftLocal.split(":"))))
  File "/usr/local/lib/python3.8/site-packages/WMCore/Credential/Proxy.py", line 778, in <genexpr>
    result = sum(int(x) * 60 ** i for i, x in enumerate(reversed(ACtimeLeftLocal.split(":"))))
ValueError: invalid literal for int() with base 10: '[0.002s,warning,perf,memops] Cannot use file /tmp/hsperfdata_crab3/3201703 because it is locked by another process (errno = 11)\n568368\n'

2024-08-26 21:20:27,862:INFO:Worker:Uploading failure message to the REST:
```

## Comment (belforte, 2024-08-27T13:23:26Z)

another problem [surfaced](https://cms-talk.web.cern.ch/t/crab3-issue-issue-with-crab-task-submission-in-submitfailed-status/46677) lately. I added logging and exception handling and got this in the log which **I annotate** here

2024-08-27 11:50:34,795:INFO:MyProxyLogon:try first to retrieve credential with login name woji_CRAB 
2024-08-27 11:50:35,321:ERROR:Proxy:Unable to retrieve delegated proxy using login woji_CRAB for user DN /DC=ch/
DC=cern/OU=Organic Units/OU=Users/CN=woji/CN=871516/CN=Wonjae Ji! Exit code:1 output: **this comes from myproxy-logon**
2024-08-27 11:50:35,732:ERROR:Proxy:Will check proxy lifetime on file /data/certs/creds/ba4cdc8605a942bc85a822a2
0f83b056c9d2ad70 **since no info is passed back by Proxy.py, I need to check the lifetime but the file is not there**
2024-08-27 11:50:36,143:ERROR:Proxy:Retrieved timeLeftLocal is: **i.e. a null string**
2024-08-27 11:50:36,144:ERROR:Proxy:Got exception invalid literal for int() with base 10:   **now I catch this inside Proxy.py instead of raising an unexpected exception which makes MyProxylogon fail**
2024-08-27 11:50:36,145:ERROR:Proxy:Repeat voms-proxy-info with full output  **I added this diagnostics**
2024-08-27 11:50:36,556:ERROR:Proxy:CMD: env -i sh -c 'voms-proxy-info -file /data/certs/creds/ba4cdc8605a942bc8
5a822a20f83b056c9d2ad70 -timeleft '
2024-08-27 11:50:36,556:ERROR:Proxy:RC: 1
2024-08-27 11:50:36,557:ERROR:Proxy:OUT: 
2024-08-27 11:50:36,557:ERROR:Proxy:ERR: Proxy not found: /data/certs/creds/ba4cdc8605a942bc85a822a20f83b056c9d2
ad70 (No such file or directory)

2024-08-27 11:50:36,557:ERROR:MyProxyLogon:Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=woji/CN=871516/CN=Wonjae Ji. **and I let it exit with timeleft=0 which causes this**
2024-08-27 11:50:36,558:ERROR:MyProxyLogon:Will try again in verbose mode  ** and it works after that**

**Interpretation**
it seems pretty clear that when we do `voms-proxy-info` on a non-existing file, the error message goes to stderr, and stdout is empty. That's how we can get an empty string in `timeLeftLocal` which of course can't be parsed as an `int`.
But the only way for this to happen, is that `voms-proxy-info` somehow returns with exit code = 0, since in [Proxy.py](https://github.com/dmwm/WMCore/blob/d618b120c6189cb8d9c89e28f202b440ab6f2bae/src/python/WMCore/Credential/Proxy.py#L722-L750) we have
```python
        timeLeft = 0
        timeLeftCmd = 'voms-proxy-info -file ' + proxy + ' -timeleft | tail -1'
        timeLeftLocal, _, self.retcode = execute_command(self.setEnv(timeLeftCmd), self.logger, self.commandTimeout)
        if self.retcode != 0:
            self.logger.error("Error while checking proxy timeleft for %s" % proxy)
            return timeLeft
        try:
            timeLeft = int(timeLeftLocal.strip())
        except ValueError:
            timeLeft = sum(int(x) * 60 ** i for i, x in enumerate(reversed(timeLeftLocal.strip().split(":"))))
```

With that the TW was reporting `''` as the timeLeftLocal string, and thus raising a silent `ValueError` at `int(timeLeftLocal.strip())` and a fatal one from the `sum(int(x)`

I patched crab-prod-tw01 to use
```python
        self.logger.error("Will check proxy lifetime on file %s", proxy)
        timeLeftCmd = 'voms-proxy-info -file ' + proxy + ' -timeleft | tail -1'
        timeLeftLocal, _, self.retcode = execute_command(self.setEnv(timeLeftCmd), self.logger, self.commandTimeout)

        if self.retcode != 0:
            self.logger.error("Error while checking proxy timeleft for %s" % proxy)
            return timeLeft
        try:
            self.logger.error("Retrieved timeLeftLocal is: %s", timeLeftLocal)
            timeLeft = int(timeLeftLocal.strip())
        except ValueError:
            try:
                timeLeft = sum(int(x) * 60 ** i for i, x in enumerate(reversed(timeLeftLocal.strip().split(":"))))
            except Exception as e:
                self.logger.error("Got exception %s", e)
                self.logger.error("Repeat voms-proxy-info with full output")
                timeLeftCmd = 'voms-proxy-info -file ' + proxy + ' -timeleft '
                out, err, ret = execute_command(self.setEnv(timeLeftCmd), self.logger, self.commandTimeout)
                self.logger.error("CMD: %s", self.setEnv(timeLeftCmd))
                self.logger.error("RC: %s", ret)                                                               
```
and problem was solved, with the log above which suggests that `if self.retcode != 0:` was `False` !!!!!!

## Comment (belforte, 2024-08-27T13:43:15Z)

The above is really hard to digest, given also that the error was reproducible in crab-prod-tw01 but  tasks from those users went fine on same container running on my crab-dev-tw01 when I tried to debug.
But I do not see any alternative to bite the bullet, and catch any possible exception while logging also the output of first command.
WIll make a new PR for WMCore

## Comment (novicecpp, 2024-08-27T13:50:57Z)

You do `<command> | tail -1`, so the exit code you got comes from the `tail` command.

## Comment (belforte, 2024-08-27T13:52:06Z)

:scream:

## Comment (belforte, 2024-08-27T13:54:27Z)

thank you @novicecpp . :sob: :sob: 
 I will do the `tail` on the stdout after I checked the exit code, and anyhow have good exception handling

## Comment (novicecpp, 2024-08-28T07:54:08Z)

Do you know why it only happens to some but not all users?
I could not reproduce it in my test12.

## Comment (belforte, 2024-08-28T08:07:14Z)

I could not reproduce it either after asking users to submit to my test2. It may have something to do with the presence of an expired proxy in /data/cert/creds so that after myproxy-logon fails there a file for voms-proxy-info to query, and this triggered the "extra `| tail`" bug.

Or do you refer to original extra line from JVM ?

## Comment (novicecpp, 2024-08-28T08:35:20Z)

No, and what you said makes sense. I never tested that.

## Comment (belforte, 2024-08-28T08:41:36Z)

I tried to understand better, but the bug with `| tail` confused me.

## Comment (belforte, 2024-08-29T15:35:43Z)

now running in production TW the modified WMCore/Credential/Proxy.py as per
https://github.com/dmwm/WMCore/pull/12084
all good.

Keep this open until that is merged, tagged and incorporated in our TW build

## Comment (belforte, 2024-09-03T20:49:30Z)

last fix (hopefully final since I already tested in production !) is in WMCore tag 2.3.6.rc2
https://github.com/dmwm/WMCore/releases/tag/2.3.6rc2

## Comment (belforte, 2024-09-04T14:02:54Z)

deployed in production today
https://cms-talk.web.cern.ch/t/production-taskworker-updated-to-v3-240809-p1-stable/47746/1
