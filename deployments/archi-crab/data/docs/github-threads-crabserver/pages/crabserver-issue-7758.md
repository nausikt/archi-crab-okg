# dmwm/CRABServer issue #7758: CRABREST should survive extended GitLab downtimes

State: closed
Opened: 2023-07-13T14:19:31Z
Closed: 2023-08-08T15:36:36Z
Labels: Type: Enhancement, Status: Done, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7758

## Opening post (belforte, 2023-07-13T14:19:31Z)

yesterdya gitlab was donw for 7 hours (scheduled maintenace) and all CRAB REST instance stopped working.
Most likely caching of [external config](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json) had expired.

Attemps to download again form gtlaib were (of course) failing, e.g. from `cmsweb-test2`

```
12/Jul/2023:20:49:56]  Reading http://gitlab.cern.ch/crab3/CRAB3ServerConfig/raw/master/cmsweb
Using cached values for external configuration. 
[12/Jul/2023:20:49:56]  RESTSQL:sgDkfTlyjmnH disconnecting 
[12/Jul/2023:20:49:56]  SERVER DATABASE ERROR 500/403 Execution error __builtins__.TypeError b49dd11f86c962b5498a762d255fcea1 [instance: dev] (the JSON object must be str, bytes or bytearray, not dict); last statement: None; binds: None, None; offset: None 
[12/Jul/2023:20:49:56]    Traceback (most recent call last): 
[12/Jul/2023:20:49:56]      File "/data/repos/WMCore/src/python/WMCore/REST/Server.py", line 1797, in dbapi_wrapper 
[12/Jul/2023:20:49:56]        return handler(*xargs, **xkwargs) 
[12/Jul/2023:20:49:56]      File "/data/repos/CRABServer/src/python/CRABInterface/RESTTask.py", line 55, in get 
[12/Jul/2023:20:49:56]        return getattr(RESTTask, subresource)(self, **kwargs) 
[12/Jul/2023:20:49:56]      File "/data/repos/CRABServer/src/python/CRABInterface/Utilities.py", line 175, in wrapped_func 
[12/Jul/2023:20:49:56]        args[0].centralcfg = ConfigCache(centralconfig=getCentralConfig(extconfigurl=args[0].config.extconfigurl, mode=args[0].config.mode), cachetime=mktime(gmtime())) 
[12/Jul/2023:20:49:56]      File "/data/repos/CRABServer/src/python/CRABInterface/Utilities.py", line 124, in getCentralConfig 
[12/Jul/2023:20:49:56]        extConfCommon = json.loads(retrieveConfig(extconfigurl)) 
[12/Jul/2023:20:49:56]      File "/data/srv/HG2305c
[12/Jul/2023:20:49:56]        raise TypeError(f'the JSON object must be str, bytes or bytearray, ' 
[12/Jul/2023:20:49:56]    TypeError: the JSON object must be str, bytes or bytearray, not dict 
[12/Jul/2023:20:49:56] crabserver

```

## Comment (novicecpp, 2023-07-13T14:49:14Z)

Ah, I remembered this. We didn't handle 5xx properly (gitlab return 5xx html page). Let me handle this.

## Comment (belforte, 2023-07-13T15:40:15Z)

don't we have code to catch any http error in downloading from gitlab and use cache instead ?
WHen cache expires and gitlab is  down, there's not much to handle other then printing "gitlab is not responding"

## Comment (belforte, 2023-07-13T15:45:47Z)

https://github.com/dmwm/CRABServer/blob/dd72fb69508d9858479b91d05386ec57b6dbb616/src/python/CRABInterface/Utilities.py#L111-L116

## Comment (belforte, 2023-07-13T15:48:47Z)

maybe a stupid bug like we store a dictionary and centralCfgFallback and try to read as JSON, which may have worked in py2 times, but eventually python decided to be serious about such matters ?

## Comment (belforte, 2023-07-13T15:56:34Z)

We did not write it down in the comments, but now I remember that there as a discussion and the consensus was
- always use cached value, silently, and if RESTconfig is stale for a while.. so be it.
We do not change it often anyhow. And when we do change, we will check that change has effect
- only fail if REST just started (no cached value) and fails to talk to gitlab,

So somehow, the machinery to reuse the cached value is not working anymore. I am pretty sure that it was tested. at the time. 
Anyhow, should be easy to test and debug on a test REST

## Comment (novicecpp, 2023-07-19T09:09:19Z)

I found relate issue https://github.com/dmwm/CRABServer/issues/7362 (DNS entry not found). 
Maybe it is better to wrap whole `retrieveConfig()` in  try-except `Exception` and load fallback config there.

Anyhow, we still need to fire alert if rest use fallback config too long.

## Comment (belforte, 2023-07-19T09:44:00Z)

as discussed also in #7362 and alert here is not needed. It could be a good place to learn how to generate alerts via logstash/grafana but I suspect none of us has time for quite a while
