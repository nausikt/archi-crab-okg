# dmwm/CRABServer issue #9167: remove CRAB Server external_config

State: closed
Opened: 2025-09-02T19:59:30Z
Closed: 2025-12-03T15:48:36Z
Labels: Status: In Progress, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9167

## Opening post (belforte, 2025-09-02T19:59:30Z)

CRABServer pulls from gitlab the external config https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json

In a way I'd like to fully get rid of this "external config" things and those obscure "modes".

The only customization that we have now via `'mode` is to use a different S3 bucket, and it would be much more clear if we put that in CRABServer's config.py in CMSKubernetes.

Currently we

* disguise the S3 bucket name as an URL
* put in a JSON file which the REST fetches every 30 minutes
* so that the Client can retrieved it at crab submit time and pass it to the REST again via the DB
* so that the REST knows which bucket to use

Sounds pretty damn stupid.

And I fear that if I am not here, it would take you a long time to figure this out.

**Plan**

- [x] change server `config.py` to support new code by adding following two lines:
   * `data.s3_bucket = 'crabcache_dev'` or `crabcache_preprod` or `crabcache_prod` as appropriate for each cluster
   * `data.compatibleClientVersions = ["v3", "development"]`
   - [x] in test and preprod https://github.com/dmwm/CMSKubernetes/pull/1657
   - [x] in prod
- [x] change REST ( #9180 ) to:
    - [x] pick bucket from config (alredy picks delegate-dn from there), save it in DB and  ignore `cacheurl` HTTP param in RESTUserWorkflow.py so that it does not matter whether client sends it or not.
    - [x] remove `banned-out-destinations` which we never used
    - [x] remove from  TW  as well (unused code anyhow) #9176 
    - [x] move `compatible version` to CRABServer/.../config.py
- [x] deploy new REST 
   - [x] in preprod (testbed)
   - [x] in prod 
- [x] change `config.py` and   [cmsweb-rest-config.json](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json) to eliminate now-useles things (see description in #9180)
   - [x] in test
   - [x] in preprod (testbed)
- [x] cleanup   `cmsweb-rest-config.json` by making it the same as `cmsweb-rest-config-test.json`
    - [x] and verify that prod still work !!! 
- [x] change `config.py` in production while keeping it pointing to   `cmsweb-rest-config.json`
- [x] change client not to send useless `cacheurl`  https://github.com/dmwm/CRABClient/issues/5411 and once in production (in CrabClient in v3.251020 running in prod CVMFS since Oct 30)
   - [x] remove `cacheurl` submit argument for submit from RESTUserWorkflow.py (where it is now optional) - https://github.com/dmwm/CRABServer/pull/9227

- [x] move handling of `"htcondorPool"` and `htcondorScheddsLink` (i.e. list of enabled schedulers) to TW and manage them via puppet #9201 
- [x] deploy new TW, then
   - [x] remove them for REST code `"htcondorPool"` and `htcondorScheddsLink`  #9220 
   - [x] remove all references to "external config" everywhere

And finally we can:
- [x] get rid of ` @conn_handler()` everywhere in CRABServer repo

Some of those actions can be pursued independently. I will open ad-hoc issues and possibly hand to DevOps
