# dmwm/CRABServer issue #7736: test building with new htcondor binding in WMCOMP

State: closed
Opened: 2023-07-09T17:21:13Z
Closed: 2023-07-21T13:29:12Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7736

## Opening post (belforte, 2023-07-09T17:21:13Z)

see https://github.com/cms-sw/cmsdist/pull/8582

## Comment (mapellidario, 2023-07-17T15:03:48Z)

I will start with a question for @belforte. 

I agree, I do not see why we should import htcondor in crabserver, I checked and it seems to be used only in https://github.com/dmwm/CRABServer/blob/master/src/python/CRABInterface/HTCondorDataWorkflow.py . However, it does not look like we use this module anymore. Can we simply remove this module and drop the dependency to htcondor in crabserver?

## Comment (belforte, 2023-07-17T16:02:38Z)

It is not easy to tell what in CRABInterace is used and what it is not. Marco M. and predecessors have been too smart here. It depends on CRABServer configuration which kind of workflows is called.
This is why I have never dared to remove files in there.
OTOH e.g. crab status was redesigned long time ago to use the cached file prepared by task wrapper on the scheduler, we do no try to ask condor.

Of course first thing is to check that we can still build and run. Code cleanup will come later.

## Comment (mapellidario, 2023-07-17T19:30:33Z)

I tried removing py3-htcondor, but crabserver fails to start [1]. We need to carefully remove some python files if we want to drop the dependency in the specfile

<details>

```plaintext
[17/Jul/2023:21:25:37]  INFO: loading data into /crabserver
Traceback (most recent call last):
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/Utils/TokenManager.py", line 23, in <module>
    import jwt
ModuleNotFoundError: No module named 'jwt'
/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/external/py3-cryptography/3.2.1-comp2/lib/python3.8/site-packages/cryptography/hazmat/bindings/openssl/binding.py:175: CryptographyDeprecationWarning: OpenSSL version 1.0.2 is no longer supported by the OpenSSL project, please upgrade. The next version of cryptography will completely remove support for it.
  warnings.warn(
[17/Jul/2023:21:25:38]  ERROR: terminating due to error: Traceback (most recent call last):
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/WMCore/REST/Main.py", line 441, in start_daemon
    self.run()
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/WMCore/REST/Main.py", line 502, in run
    self.install_application()
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/WMCore/REST/Main.py", line 280, in install_application
    obj = getattr(module, class_name)(self, view, path)
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/CRABInterface/RESTBaseAPI.py", line 58, in __init__
    self._add( {'workflow': RESTUserWorkflow(app, self, config, mount, extconfig),
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/CRABInterface/RESTUserWorkflow.py", line 34, in __init__
    self.userworkflowmgr = DataUserWorkflow()
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/CRABInterface/DataUserWorkflow.py", line 15, in __init__
    mod = __import__('CRABInterface.%s' % self.workflowManager, fromlist=self.workflowManager)
  File "/data/srv/HG2306b-711d31aabce5f9698fb0715c5fa1dab2/sw.dmapelli/slc7_amd64_gcc630/cms/crabserver/v3.230714-97650e1c3efc5171afa97a1288a8f1d2/lib/python3.8/site-packages/CRABInterface/HTCondorDataWorkflow.py", line 12, in <module>
    import classad
ModuleNotFoundError: No module named 'classad'

[17/Jul/2023:21:25:38]  WATCHDOG: server exited with exit code 1
Cannot find crabserver's PID file
^C
```

</details>

## Comment (belforte, 2023-07-17T20:19:02Z)

yeah.. that's how [/HTCondorDataWorkflow.py](https://github.com/dmwm/CRABServer/blob/master/src/python/CRABInterface/HTCondorDataWorkflow.py) sneaked in from a call to `DataUserWorkflow.py` 
that\s the only file in CRABServer where `import classa` appears.
The trick is this line in `/srv/current/config/crabserver/config.py`
```
data.workflowManager = 'HTCondorDataWorkflow'
```
which directs the server to use `HTCondorDataWorkflow`  as per
https://github.com/dmwm/CRABServer/blob/2365939e2777e4afa2077f2c6b485b899c1facde/src/python/CRABInterface/DataUserWorkflow.py#L13-L16

See also this [old note](https://github.com/dmwm/CRABServer/issues/5690#issuecomment-395351592) from Marco

It is well past the time where it would make sense to have a workflow other than HTCondor, so
we may look into getting rid of those lines which Stefano can not possibly understand and simplify here as well.

If we want to hack our way into cleaning up, I suspect best way is to take one  crab-dev* machine and do brute force iterations of edit/start -d . Starting point IMHO is to remove https://github.com/dmwm/CRABServer/blob/2365939e2777e4afa2077f2c6b485b899c1facde/src/python/CRABInterface/HTCondorDataWorkflow.py#L42
which AFAICT is not used anywhere (and with it the methods called only in there, of course)

## Comment (belforte, 2023-07-17T20:32:57Z)

you can also test "removing dependencies" as simply as "delete files in `/data/srv/current/sw.crab_master/slc7_amd64_gcc630/external/` (even simply rename in order to quickly revert). And if you end up in a mess, just restart the pod and the container will be refreshed.

## Comment (mapellidario, 2023-07-21T13:21:50Z)

The test were ok. A couple of jobs failed, mainly at MIT and vanderbilt, likely for problems with the storage. 

I am inclined to consider  the use of the recent version of  `py3-htcondor` in TW validated. Stefano, do you agree?

## Comment (mapellidario, 2023-07-21T13:29:12Z)

Good, thanks, let's close then! :)
