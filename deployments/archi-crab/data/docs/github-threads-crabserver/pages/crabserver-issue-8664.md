# dmwm/CRABServer issue #8664: Action Items from Udine Workshop

State: closed
Opened: 2024-08-28T15:43:17Z
Closed: 2024-09-11T09:40:50Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8664

## Opening post (belforte, 2024-08-28T15:43:17Z)

I collect here all Action items from  https://docs.google.com/document/d/1KPd77i91R5iqHBrvw8kz821UpqUxwqnJTQEL_pqDE5g/edit as a task list.
Can check as done as we move each to its own GH issue

- [x] Puppet, systemctl units, runners configurations, how to register a new runner with gitlab server - [Done](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/private-runners.html)
- [x] More git push option scripts and documentation - DONE [1](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/triggering.html#variables-in-rules) [2](https://github.com/dmwm/CRABServer/tree/5a53de7f51ac449d4e71dd201605954cce57c550/cicd/trigger-ci)
- [x] Document kubeconfig: form users_config to variable inside gitlab [Done](https://cmscrab.docs.cern.ch/technical/crab-cicd/gitlab/variables.html#kubeconfig_file)
- [x] Add crab-secret ssh privatekey for crab3 user in runner machine - DONE
- [x] Change s3 secrets: from dario to stefano: - #8673
- [x] Add a “GIT Etiquette” section to docs Stefano #8665
- [x] Add TW VM name to the entries in opensearch (generatemonit and TW logstash) #8678
 - [x] Create a crabserver_qa deployment with  1 pod - overridden by #8650
 - [x] Recover. GH issue: close the main one, open a new one with list of missing features (recover by file) - https://github.com/dmwm/CRABClient/issues/5330
 - [x] Document how to debug monitoring container Dario, done
 - [x] Documentation: list of opensearch instances, url, how to access, where the data come from #8695 
 - [x] CRAB Spark: troubleshoot tape recall (ex. how long does the rules take to complete copy from tape) is broken, a.k.a. close https://github.com/dmwm/CRABServer/issues/7798 **Wa**
 - [x] CRAB Spark: add a couple of panels in crab overview. [Done](https://github.com/dmwm/CRABServer/pull/8672#issue-2494835952)
 - [x] Following up with Aroosha for REST logs in S3 **Wa**
 - [x] Documentation: refactor crab docs as agreed - #8666
 - [x] Check documentation about how to debug crab client #8694 
 - [x] Crabint1 [acron](https://cern.service-now.com/service-portal?id=service_element&name=ACRON-Service) job to cleanup eos directory - #8644
 - [x] Change pylint config to accept f-string in log [(starting point)](https://gitlab.cern.ch/CMSDOCKS/dmwm/-/tree/master?ref_type=heads) https://github.com/dmwm/CRABServer/issues/7557 - **Wa**
 - [x] Detail the work needed to change TW/Pub config as agreed - #8528
 - [x] Configuration, REST. Prepare configmap for config.py, with delegate DNs ([here](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json?ref_type=heads#L4)) https://github.com/dmwm/CRABServer/issues/8685 - **Wa**  
 - [x] Make it clear that when retrievers DN list changes, HC credentials in myproxy need refreshin - ([Done](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json?ref_type=heads#L4))
 - [x] Fix release pipeline that still broken [Pipeline #7968420](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7968420) - DONE
 - [x] GH issue - canary deployments - #8650
 - [x] GH issue - schedd automatic reboot - #8651
 - [x] Open new PR about refactor of controller scripts - #8658
 - [x] preparelocal+submit dryrun - write something so that stefano can pick it up https://github.com/dmwm/CRABServer/issues/6544#issuecomment-2329859381 
 - [x] Add private task examples to “status Tracking” directory https://github.com/dmwm/CRABServer/issues/8686 -  **Wa**

## Comment (belforte, 2024-09-11T09:40:51Z)

everything is now followed up in its one thread. Thanks everybody !
