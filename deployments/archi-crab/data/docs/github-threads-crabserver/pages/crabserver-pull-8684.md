# dmwm/CRABServer pull request #8684: fix the X509_USER_CERT path, and also add X509_USER_PROXY here,

State: closed
Opened: 2024-09-03T15:51:28Z
Closed: 2024-09-04T17:39:49Z
Merged: 2024-09-04T17:39:49Z
URL: https://github.com/dmwm/CRABServer/pull/8684

## Opening post (novicecpp, 2024-09-03T15:51:28Z)

which already overridden by entrypoint.sh/setup.sh

## Comment (cmsdmwmbot, 2024-09-03T15:54:49Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2158/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-09-03T20:41:22Z)

I am very confused too. And I believe that we never use $X509 authentication in the server. As far as other services go, REST only talks to CRIC which I believe does not requires authentication (and we want to remove the call to CRIC anyhow).
I have started crabserv on cmsweb-test2 in debug mode and X509_USER_PROXY is not in `os.environ`, yet it works.

Hard to say if X509_USER_CERT/KEY are used anywhere, since it is possible that e.g. pycurl looks for them and we do not see it

Some tool falls back to X509_USER_PROXY if USER_CERT/KEY are not defined, or even viceversa, picking whatever they find that works. But IIUC until now we did not have X509_USER_PROXY, so... why add it ?

## Comment (novicecpp, 2024-09-03T21:46:56Z)

> I have started crabserv on cmsweb-test2 in debug mode and X509_USER_PROXY is not in os.environ, yet it works.

The service can start but `workflow` API does not work. 

> But IIUC until now we did not have X509_USER_PROXY, so... why add it ?

We actually have it [here in entrypoint.sh](https://github.com/dmwm/CRABServer/blob/f5687adbf5fddeb21526c33b623b2f5025e17945/cicd/crabserver_pypi/entrypoint.sh#L28).

## Comment (novicecpp, 2024-09-03T21:49:41Z)

This PR simply to make sure everything is set the same way as current prod does, in order to move entrypoint.sh to helm.

## Comment (belforte, 2024-09-03T22:17:03Z)

OK. You win. Let's do. But I am still puzzled !
If we have it, why I did not find it in os.environ ? One day I'll want to understand.
Do you know a query which failed w/o X509_USER_PROXY ? `workflow` API has a lot of stuff

## Comment (novicecpp, 2024-09-04T16:53:36Z)

For the record, it didn't even start if we did not set any proxy and got this exception:
```
[04/Sep/2024:18:11:25]  INFO: final CherryPy configuration: {'engine.autoreload.on': False,
 'request.methods_with_bodies': ('POST', 'PUT', 'DELETE'),
 'request.show_tracebacks': False,
 'server.environment': 'production',
 'server.max_request_body_size': 0,
 'server.socket_host': '0.0.0.0',
 'server.socket_port': 8270,
 'server.socket_queue_size': 100,
 'server.thread_pool': 2,
 'tools.cms_auth.group': None,
 'tools.cms_auth.key_file': '/data/srv/current/auth/crabserver/header-auth-key',
 'tools.cms_auth.on': True,
 'tools.cms_auth.role': None,
 'tools.cms_auth.site': None,
 'tools.encode.on': True,
 'tools.log_headers.on': True,
 'tools.log_tracebacks.on': True,
 'tools.proxy.base': 'crabserver-76dbff6cdc-8crj2:8270',
 'tools.proxy.on': True,
 'tools.time.on': True,
 'tools.trailing_slash.on': True}
[04/Sep/2024:18:11:25]  INFO: loading data into /crabserver
<@========== WMException Start ==========@>
Exception Class: WMException
Message: Request requires a host certificate and key
        ClassName : None
        ModuleName : WMCore.Services.Requests
        MethodName : getKeyCert
        ClassInstance : None
        FileName : /data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py
        LineNumber : 469
        ErrorNr : WMCORE-11

Traceback:

<@---------- WMException End ----------@>
Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Service.py", line 150, in __init__
    self["requests"] = requests(cfg_dict['endpoint'], cfg_dict)
  File "/data/srv/current/lib/python/site-packages/Utils/PortForward.py", line 68, in portMangle
    return callFunc(callObj, url, *args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py", line 131, in __init__
    self['key'], self['cert'] = self.getKeyCert()
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py", line 469, in getKeyCert
    raise WMException('Request requires a host certificate and key',
WMCore.WMException.WMException: <@========== WMException Start ==========@>
Exception Class: WMException
Message: Request requires a host certificate and key
        ClassName : None
        ModuleName : WMCore.Services.Requests
        MethodName : getKeyCert
        ClassInstance : None
        FileName : /data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py
        LineNumber : 469
        ErrorNr : WMCORE-11

Traceback:

<@---------- WMException End ----------@>
[04/Sep/2024:18:11:26]  ERROR: terminating due to error: Traceback (most recent call last):
  File "/data/srv/current/lib/python/site-packages/WMCore/REST/Main.py", line 441, in start_daemon
    self.run()
  File "/data/srv/current/lib/python/site-packages/WMCore/REST/Main.py", line 502, in run
    self.install_application()
  File "/data/srv/current/lib/python/site-packages/WMCore/REST/Main.py", line 280, in install_application
    obj = getattr(module, class_name)(self, view, path)
  File "/data/srv/current/lib/python/site-packages/CRABInterface/RESTBaseAPI.py", line 58, in __init__
    self._add( {'workflow': RESTUserWorkflow(app, self, config, mount, extconfig),
  File "/data/srv/current/lib/python/site-packages/CRABInterface/RESTUserWorkflow.py", line 39, in __init__
    self.tagCollector = TagCollector(logger = self.logger, anytype = 1, anyarch = 1)
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/TagCollector/TagCollector.py", line 39, in __init__
    super(TagCollector, self).__init__(configDict)
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Service.py", line 150, in __init__
    self["requests"] = requests(cfg_dict['endpoint'], cfg_dict)
  File "/data/srv/current/lib/python/site-packages/Utils/PortForward.py", line 68, in portMangle
    return callFunc(callObj, url, *args, **kwargs)
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py", line 131, in __init__
    self['key'], self['cert'] = self.getKeyCert()
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py", line 469, in getKeyCert
    raise WMException('Request requires a host certificate and key',
WMCore.WMException.WMException: <@========== WMException Start ==========@>
Exception Class: WMException
Message: Request requires a host certificate and key
        ClassName : None
        ModuleName : WMCore.Services.Requests
        MethodName : getKeyCert
        ClassInstance : None
        FileName : /data/srv/current/lib/python/site-packages/WMCore/Services/Requests.py
        LineNumber : 469
        ErrorNr : WMCORE-11

Traceback:

<@---------- WMException End ----------@>
```

which point to this code

https://github.com/dmwm/WMCore/blob/213189431a6aeae29781429eb0478e79e2de8664/src/python/Utils/CertTools.py#L17-L27

```
    envPairs = [('X509_HOST_KEY', 'X509_HOST_CERT'),  # First preference to HOST Certificate,
                ('X509_USER_PROXY', 'X509_USER_PROXY'),  # Second preference to User Proxy, very common
                ('X509_USER_KEY', 'X509_USER_CERT')]  # Third preference to User Cert/Proxy combinition
```

## Comment (cmsdmwmbot, 2024-09-04T17:04:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2162/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-09-04T17:12:19Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2163/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-09-04T17:33:15Z)

I think it work in your case because it fall through "Third preference", the `X509_USER_CERT`. 
In the older image it set to 
https://github.com/dmwm/CRABServer/blob/88794af941de62774572cc0d7f86791da775e4f9/cicd/crabserver_pypi/manage.sh#L55-L56

The `$AUTHDIR` is 
https://github.com/dmwm/CRABServer/blob/88794af941de62774572cc0d7f86791da775e4f9/cicd/crabserver_pypi/manage.sh#L36
and the `$srv` is `crabserver`.

In the current image I forgot `crabserver` in the path
https://github.com/dmwm/CRABServer/blob/1cfacb06c91b6e4e44412a42cd900ae67589d032/cicd/crabserver_pypi/manage.sh#L24-L26

And then, there is no X509_USER_PROXY, and X509_USER_CERT, so it make the service crash.

## Comment (novicecpp, 2024-09-04T17:39:16Z)

With this PR, the env is setup correctly inside pod. 

```
crab3@crabserver-55bb56cbcb-6zwcn:/data$ cat /proc/41/environ | tr '\0' '\n' | sort
...
WDIR=/data
X509_USER_CERT=/data/srv/current/auth/crabserver/dmwm-service-cert.pem
X509_USER_KEY=/data/srv/current/auth/crabserver/dmwm-service-key.pem
X509_USER_PROXY=/etc/proxy/proxy
_=/usr/local/bin/wmc-httpd
crab3@crabserver-55bb56cbcb-6zwcn:/data$ ls -alh /data/srv/current/auth/crabserver/
total 16K
drwxr-xr-x. 1 crab3 crab3  130 Sep  4 19:34 .
drwxr-xr-x. 1 root  root    24 Sep  4 18:57 ..
-rw-r--r--. 1 crab3 crab3 2.6K Sep  4 19:34 CRABServerAuth.py
drwxr-xr-x. 2 crab3 crab3   43 Sep  4 19:34 __pycache__
-rw-r--r--. 1 crab3 crab3 3.5K Sep  4 19:34 dmwm-service-cert.pem
-rw-r--r--. 1 crab3 crab3 1.8K Sep  4 19:34 dmwm-service-key.pem
-rw-r--r--. 1 crab3 crab3   20 Sep  4 19:34 header-auth-key
crab3@crabserver-55bb56cbcb-6zwcn:/data$ ls /etc/proxy/proxy -ahl
lrwxrwxrwx. 1 root 2000 12 Sep  4 19:34 /etc/proxy/proxy -> ..data/proxy
```

## Comment (belforte, 2024-09-04T18:38:58Z)

WOW The Tag Collector !!!!! I had even forgotten that it exists !
```
  File "/data/srv/current/lib/python/site-packages/WMCore/Services/TagCollector/TagCollector.py", line 39, in __init__
```
at least now I know why we use X509 authentication.

Differently from CRIC I do not have a good plan about how to remove that (yet).

thanks for fixing the environment !
