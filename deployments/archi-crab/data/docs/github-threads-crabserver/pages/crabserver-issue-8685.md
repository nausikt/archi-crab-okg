# dmwm/CRABServer issue #8685: Move config.py with delegate DNs to helm

State: closed
Opened: 2024-09-03T16:32:05Z
Closed: 2025-01-08T17:51:58Z
URL: https://github.com/dmwm/CRABServer/issues/8685

## Opening post (novicecpp, 2024-09-03T16:32:05Z)

`config.py` is in `crab-secrets` and also migrate the delegate DN [here](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json?ref_type=heads#L4) into `config.py`.

The `config.py` is already part of new helm chart https://github.com/dmwm/CMSKubernetes/pull/1545, also delegateDN.
But delegateDN need some code changes on REST.

## Comment (belforte, 2025-01-08T13:13:04Z)

@sinonkt here's a quick way to test change:
```
belforte@lxplus916/~> voms-proxy-init -voms cms
Enter GRID pass phrase for this identity:
Contacting voms-cms-auth.app.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u8516.

Your proxy is valid until Thu Jan 09 02:11:39 CET 2025
belforte@lxplus916/~> export  X509_USER_PROXY=`voms-proxy-info -path`
belforte@lxplus916/~> curl --cert $X509_USER_PROXY  --key $X509_USER_PROXY  https://cmsweb-testbed.cern.ch/crabserver/prod/info?subresource=delegatedn
{"result": [
 {"services": ["/DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=(817881|373708)/CN=Robot: cms crab|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1"]}
]}
belforte@lxplus916/~> 
```

replace `cmsweb-testbed` with your favorite cluster and verify that the JSON retrieved via `curl` is the same as in an un-modified cluster.

## Comment (belforte, 2025-01-08T14:25:15Z)

side note: I do not particularly like that this longish list is present separately in multiple files (e.g. https://github.com/dmwm/CMSKubernetes/blob/d1eb8a7ff4a2e66ca498ca9896fbfb00f3e8798a/helm/crabserver/config/preprod/config.py#L49 ). Requires some effort to keep consistency in the future. E.g. it is not present in current `config/prod/config.py` file.

## Comment (nausikt, 2025-01-08T17:42:27Z)

@belforte I've tested on `cmsweb-test12`. the response are identical with `cmsweb-testbed` now as following.
```
[kphornsi@lxplus910 ~]$ curl --cert $X509_USER_PROXY  --key $X509_USER_PROXY  https://cmsweb-test12.cern.ch/crabserver/devthree/info?subresource=delegatedn
{"result": [
 {"services": ["/DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=(817881|373708)/CN=Robot: cms crab|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1"]}
]}
[kphornsi@lxplus910 ~]$
```
the corresponding changes can be seen in [PR](https://github.com/dmwm/CRABServer/pull/8871).
