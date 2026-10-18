# dmwm/CRABServer pull request #7759: pass JSON to json.loads. Fix #7758

State: closed
Opened: 2023-07-14T13:09:36Z
Closed: 2023-08-02T17:52:19Z
URL: https://github.com/dmwm/CRABServer/pull/7759

## Opening post (belforte, 2023-07-14T13:09:36Z)

(no text)

## Comment (cmsdmwmbot, 2023-07-14T13:15:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 27 comments to review
 * Pycodestyle check: succeeded
   * 15 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1592/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-14T13:16:58Z)

@mapellidario can you kindly also test this ? Hint: start REST with a custom url for `data.extconfigurl` in `/data/srv/current/config/crabserver/config.py`, then break the document and hopefully see the error being reproduced at next update (once every 30min, but you can also shorten changing `1800` in
https://github.com/dmwm/CRABServer/blob/dd72fb69508d9858479b91d05386ec57b6dbb616/src/python/CRABInterface/Utilities.py#L174
)
Then put in the "fix" and check that error is gone.
Of course if you spot problems and solve them during the review, even better.

## Comment (mapellidario, 2023-07-26T15:23:12Z)

test this please

## Comment (cmsdmwmbot, 2023-07-26T15:27:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 27 comments to review
 * Pycodestyle check: succeeded
   * 15 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1632/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-07-26T16:09:35Z)

#### problem

Despite pylint does not find any problem [1], the changes proposed with this PR make appear a bug that was there for a long time. We are using `extConfSchedds` before it is defined [2].

That happens because when we first read the config properly from the web, we remove the `"modes"` key from the dict https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/src/python/CRABInterface/Utilities.py#L144

Then, the config is no longer available on the web, we use the cached value, the value returned by `retrieveConfig()` is the one of the last time the web was ok and it does not contain the "modes" key, so we skip `if 'modes' in extConfCommon:`, we do not define `extConfSchedds`, but we try to read from it later on.

#### possible solutions

I would either remove 

1. https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/src/python/CRABInterface/Utilities.py#L144

2. or https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/src/python/CRABInterface/Utilities.py#L154-L155

I tested 2. and all looks ok, however you may have a better idea of why 1. and 2. are there, so I think it should you the one who decides which solution is the best

---

[1] https://cmssdt.cern.ch/dmwm-jenkins/job/DMWM-CRABServer-PR-pylintpy3/377/artifact/pylintpy3Report.json in this pylint report there is no mention to `extConfSchedds`

(yeah, pylint was ok, but its output was not parsed correctly and no message was sent to this PR. see #7787 ) 

[2] rest log

<details>

```plaintext
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw instantiating a new connection - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw connected, client: 19.11.0.0.0, server: 19.17.0.0.0, stmtcache: 50 - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw ping - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw check [select sysdate from dual] - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw connection established - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  Reading https://dmapelli.web.cern.ch/public/crab/20230726-rest-config/cmsweb-rest-config.json returned 404.
Using cached values for external configuration. - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw disconnecting - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  SERVER DATABASE ERROR 500/403 Execution error __builtins__.UnboundLocalError e566195efd29745f9bbb65c85858da35 [instance: dev] (local variable 'extConfSchedds' referenced before assignment); last statement: None; binds: None, None; offset: None - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]    Traceback (most recent call last): - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]      File "/data/repos/WMCore/src/python/WMCore/REST/Server.py", line 1797, in dbapi_wrapper - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]        return handler(*xargs, **xkwargs) - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]      File "/data/repos/CRABServer/src/python/CRABInterface/RESTServerInfo.py", line 37, in get - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]        return getattr(RESTServerInfo, subresource)(self, **kwargs) - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]      File "/data/repos/CRABServer/src/python/CRABInterface/Utilities.py", line 178, in wrapped_func - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]        args[0].centralcfg = ConfigCache(centralconfig=getCentralConfig(extconfigurl=args[0].config.extconfigurl, mode=args[0].config.mode), cachetime=mktime(gmtime())) - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]      File "/data/repos/CRABServer/src/python/CRABInterface/Utilities.py", line 157, in getCentralConfig - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]        extConfCommon["backend-urls","htcondorSchedds"] = extConfSchedds - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]    UnboundLocalError: local variable 'extConfSchedds' referenced before assignment - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09] crabserver-7cc4dc8f64-z5rtg 188.185.21.36:39338 "GET /crabserver/dev/info?subresource=delegatedn HTTP/1.1" 500 Internal Server Error [data: 1142 in 745 out 437311 us ] [auth: ok "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=dmapelli/CN=817881/CN=Dario Mapelli" "" ] [ref: "https://cmsweb-test11.cern.ch" "curl/7.76.1" ] - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog
[26/Jul/2023:15:56:09]  RESTSQL:CJLuiZdQslRw DISCONNECTED cmsweb_analysis_dev@int2r timeout=300 inuse=0 idle=0 - Podname=crabserver-7cc4dc8f64-z5rtg Type=cherrypylog

```

</details>

## Comment (belforte, 2023-07-31T16:06:11Z)

hmm... it is the usual code written by others, where I changed here and there w/o ever fully understanding... so I guess we need to "review from scratch".
Maybe we can trust the comment
https://github.com/dmwm/CRABServer/blob/1ebaa01e363c4ed6c0e31564f1590548a7dfb962/src/python/CRABInterface/Utilities.py#L126
and start by cleaning up a bit. So far I have no idea why `del extConfCommon['modes'] ` is there.

Nor the [commit](https://github.com/dmwm/CRABServer/commit/c56580b172d21706f652462010f7fee610ffa4a8) where it was introduced nor the respective issue #6009 say anything about this.

## Comment (belforte, 2023-07-31T16:30:17Z)

I suspect the root of the problem is that the same varaible name `extConfCommon` is used both for the JSON read from gitlab (with the so called new format) and for the dictionary used internally (with the so called old format).  IIUC the current code caches the latter, but in order to use it, sends the cached object back through the reformatting.

Maybe moving L156 to L125 is a better solution ?

## Comment (belforte, 2023-08-01T17:02:36Z)

@mapellidario do IIUC that here I should push a tentative fix and you can test it, since you are setup for that ? How can we speed up ? Maybe I can access your test setup and try on the fly there ? Or we do it together ?

## Comment (mapellidario, 2023-08-01T17:22:50Z)

I suggest we do it together at first, then if we can not sort it out in let say a few hours, I write better instructions so that you can replicate the test yourself (it's pretty simple, I promise).

## Comment (belforte, 2023-08-02T16:58:40Z)

there's a bigger mess than this.
Current code uses `retrieveConfig()` for two different URL's (central config and htcondor schedulers) but there is only one fallback. 

I am refactoring a bit.

## Comment (belforte, 2023-08-02T17:52:19Z)

I think I have it. Let me close this and make a new one.
