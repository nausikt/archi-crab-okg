# dmwm/CRABServer issue #8631:  improve error reporting when user indicates bad vogroup

State: closed
Opened: 2024-08-17T14:29:04Z
Closed: 2024-08-17T14:29:57Z
URL: https://github.com/dmwm/CRABServer/issues/8631

## Opening post (belforte, 2024-08-17T14:29:04Z)

reference: [cms-talk](https://cms-talk.web.cern.ch/t/submitfailed-could-not-get-a-proxy-valid-for-at-least-5-days-from-myproxy-cern-ch/45978/3)

the problem is that error message returned to user it the cryptic `Could not get a proxy valid for at least 5-days from myproxy.cern.ch for ...` instead of slightly more the telling `User is not authorized to request attribute '/cms/cms' or attribute does not exist.`

## Comment (belforte, 2024-08-17T14:29:57Z)

I do not think we can fix in a simple way.
Everything happens inside WMCore/Credential/Proxy which does not return usable msg's nor exceptions. It would be easier to change https://github.com/dmwm/CRABServer/blob/master/src/python/TaskWorker/Actions/MyProxyLogon.py to use explicit myproxy-* and voms* commands.

Let's wait for something like this to happen again and do that effort at that time.
