# dmwm/CRABServer pull request #9166: useless if. We only use S3 for cache

State: closed
Opened: 2025-09-01T15:27:27Z
Closed: 2025-09-03T14:59:33Z
Labels: Status: On Hold
URL: https://github.com/dmwm/CRABServer/pull/9166

## Opening post (belforte, 2025-09-01T15:27:27Z)

@aspiringmind-code @sinonkt 
I am cleaning/clarifying the use of "crabcache", to avoid confusion.

Changes to CRAAB3Configuration.json and to CRABClient are useful too. To allow smooth transition, can you help me how to rewrite this line
https://github.com/dmwm/CRABServer/blob/205ef56bfb11930c637a4473c40b4a1a2c926774/src/python/CRABInterface/Regexps.py#L49

so it also accepts strings of the format `S3/crabcache_(prod|preprod|dev)` and possibly later simply the bucket name `crabcache_prod` etc. ?

## Comment (cmsdmwmbot, 2025-09-01T15:29:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 1 warnings
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2591/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-09-01T16:13:45Z)

Hi @belforte, For clarity, 
Our current regex already support/allows those `S3/crabcache_(preprod/prod/dev)` pattern. and thus allows every URI patterns occures, in CRAB3ServerConfig/*.json, in the following list of urls.
```
https://cmsweb-testbed.cern.ch/crabcache
https://cmsweb-testbed.cern.ch/crabcache
https://cmsweb.cern.ch/crabcache
https://cmsweb-testbed.cern.ch:8443/crabcache
https://cmsweb-testbed.cern.ch:8443/crabcache
https://cmsweb-test2.cern.ch/S3/crabcache_dev
http://s3.cern.ch/crabcache_dev
https://cmsweb-testbed.cern.ch/S3/crabcache_prod
https://cmsweb-auth.cern.ch:8443/crabcache
https://cmsweb.cern.ch/S3/crabcache_prod
https://cmsweb-test2.cern.ch/S3/crabcache_dev
https://cmsweb-testbed.cern.ch/S3/crabcache_prod
https://cmsweb.cern.ch/S3/crabcache_prod
```

Did you means we would like to strictly allowed only `S3/crabcache_(preprod/prod/dev)`? and discard other testing url patterns?

## Comment (nausikt, 2025-09-01T16:29:48Z)

@belforte Forgive me, this PR is chain of another [crab3/CRAB3ServerConfig#MR6](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/merge_requests/6)

which those non `S3/crabcache_*` already clean-up.

## Comment (nausikt, 2025-09-01T16:36:23Z)

```python
RX_CACHEURL = re.compile(r"^https?://([-\w\.]*)\.cern\.ch+(:\d+)?/S3/crabcache_(preprod|prod|dev)$") 
```
This regex should strictly works for `S3/crabcache_*` pattern.

P.S there is some unused? patterns left in `cmsweb-rest-config-full.tpl` that i'm not sure whether it gonna be use somewhere else.
```
7:            "cacheSSL" : "https://cmsweb-testbed.cern.ch/crabcache",
22:            "cacheSSL" : "https://cmsweb-testbed.cern.ch/crabcache",
93:            "cacheSSL" : "https://cmsweb.cern.ch/crabcache",
```

## Comment (belforte, 2025-09-01T16:37:06Z)

I'd like to remove the useless `https://cmsweb.cern.ch` from the CRAB3SServerConfig json.
In a way I'd like to fully get rid of this "external config" things and those obscure "modes".
THe only customization that we have now is to use a different S3 bucket, and it would be much more clear if we put that in CRABServer's config.py in CMSKubernetes.

Currently we
- disguise the S3 bucket name as an URL
- put in a JSON file which the  REST fetches every 30 minutes
- so that the Client can retrieved it at `crab submit` time and pass it to the REST again via the DB
- so that the REST knows which bucket to use

Sounds pretty damn stupid.

And I fear that if I am not here, it would take you a long time to figure this out.

## Comment (belforte, 2025-09-01T16:38:57Z)

Is ` cmsweb-rest-config-full.tpl` used anywhere ?

## Comment (nausikt, 2025-09-01T16:41:16Z)

> I'd like to remove the useless `https://cmsweb.cern.ch` from the CRAB3SServerConfig json. In a way I'd like to fully get rid of this "external config" things and those obscure "modes". THe only customization that we have now is to use a different S3 bucket, and it would be much more clear if we put that in CRABServer's config.py in CMSKubernetes.
> 
> Currently we
> 
> * disguise the S3 bucket name as an URL
> * put in a JSON file which the  REST fetches every 30 minutes
> * so that the Client can retrieved it at `crab submit` time and pass it to the REST again via the DB
> * so that the REST knows which bucket to use
> 
> Sounds pretty damn stupid.
> 
> And I fear that if I am not here, it would take you a long time to figure this out.

I see, Thanks so much.

> Is ` cmsweb-rest-config-full.tpl` used anywhere ?

No, from any repos (e.g. CRASServer, CRABClient, CRAB3ServerConfig).

## Comment (belforte, 2025-09-01T16:41:54Z)

allow me better clarify, I'd like to accept EITHER
`r"^https?://([-\w\.]*)\.cern\.ch+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?$"`
OR the simpler
`r"^S3/anysensiblestring$"`

## Comment (cmsdmwmbot, 2025-09-01T16:48:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 5 warnings
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 121 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2592/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-09-01T17:06:16Z)

> allow me better clarify, I'd like to accept EITHER `r"^https?://([-\w\.]*)\.cern\.ch+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?$"` OR the simpler `r"^S3/anysensiblestring$"`

I've tested the following regex.
```python
RX_CACHEURL  = re.compile(r"^(S3/([\w/_\.]*(\?\S+)?)?|https?://([-\w\.]*)\.cern\.ch+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?)$")
```

now, It's generous for both patterns.
```
✓ https://cmsweb-testbed.cern.ch/crabcache
✓ https://cmsweb-testbed.cern.ch/crabcache
✓ https://cmsweb.cern.ch/crabcache
✓ https://cmsweb-testbed.cern.ch:8443/crabcache
✓ https://cmsweb-testbed.cern.ch:8443/crabcache
✓ https://cmsweb-test2.cern.ch/S3/crabcache_dev
✓ http://s3.cern.ch/crabcache_dev
✓ https://cmsweb-testbed.cern.ch/S3/crabcache_prod
✓ https://cmsweb-auth.cern.ch:8443/crabcache
✓ https://cmsweb.cern.ch/S3/crabcache_prod
✓ https://cmsweb-test2.cern.ch/S3/crabcache_dev
✓ https://cmsweb-testbed.cern.ch/S3/crabcache_prod
✓ https://cmsweb.cern.ch/S3/crabcache_prod
✓ S3/crabcache_prod
✓ S3/crabcache_dev
✓ S3/crabcache_preprod
```

## Comment (cmsdmwmbot, 2025-09-02T18:59:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 5 warnings
   * 68 comments to review
 * Pycodestyle check: succeeded
   * 189 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2596/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-09-02T19:18:01Z)

@sinonkt let me test more and possibly do further restructuring before you spend time reviewing.

## Comment (belforte, 2025-09-02T20:00:34Z)

I tried to embed this in a more complete plan for the removal of this "external configuration" legacy thing
https://github.com/dmwm/CRABServer/issues/9167

## Comment (belforte, 2025-09-03T14:59:28Z)

let's close this and I will open a new one where more comprehensively address the points from #9167
