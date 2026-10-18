# dmwm/CRABServer issue #7845: Use tokens for crab for backend service-to-service communication

State: open
Opened: 2023-08-19T14:25:18Z
Labels: Type: Enhancement, Priority: High, Status: On Hold, Area: Needed Feature
URL: https://github.com/dmwm/CRABServer/issues/7845

## Opening post (mapellidario, 2023-08-19T14:25:18Z)

Currently, we use x509 certificates for communication between our services. We need to move to tokens.

An incomplete list of the requests that **should** be authenticated with a token instead of with a certificate is

- [ ] TW, Publisher to cmsweb (crabserver, dbs, ...)
- [ ] TW to schedd (job submission)
- [ ] TW to rucio (data discovery)
- [ ] schedd to rest (postjob, ...)
- [ ] schedd to fts 
- [ ] schedd to rucio

An incomplete list of the requests that **may** be authenticated with a token instead of with a certificate is

- [ ] TW to myproxy

See the CRAB Overview [1] for ideas on what i may have missed in these lists :)

--- 

[1] https://twiki.cern.ch/twiki/bin/view/CMSPublic/CrabOverview

## Comment (belforte, 2024-08-23T10:09:50Z)

Likely for 2025, we'll define better when new DevOp is here

## Comment (novicecpp, 2024-09-24T13:04:11Z)

Here is [the commit](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/9bbb6ab019a6891967933d97ffe48937fb2ce5e9) left by Dario about the token, also available on branch [crabdev_taskworker_token](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commits/crabdev_schedd_tokens?ref_type=heads).
The [puppet env](https://gitlab.cern.ch/ai/it-puppet-environments/-/commit/2ecdb96c2430135e2c97f5b5a9ac9486b84eaad6) will be deleted soon because it no longer has the machine in that env, which is fine.

And for the record, here the explanation from Dario:
```
hello, yeah, my fault. that machine is running condor_schedd from cern repositories and condor_credmon_vault from the osg ones (this package is only distributed by osg repos), and there was a mismatch between the two that broke yum update/upgrade. 
- either you as florian to help you find in the cern repositories a condor version that matches the one from osg
- or you install condor itself from osg in that machine
you can replicate the error running yum upgrade as root user in that schedd
```

## Comment (mapellidario, 2024-09-24T13:26:06Z)

and do not forget that in order to use tokens on the schedd you also need to change the JDL for the jobs, as described [here](https://cmscrab.docs.cern.ch/crab-components/crab-schedd/schedd-tokens.html) :)
