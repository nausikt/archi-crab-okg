# dmwm/CRABServer issue #8445: Publisher logs changed during rrefactoring - out of sync with logstash pattern

State: closed
Opened: 2024-05-30T16:14:30Z
Closed: 2024-06-11T06:51:15Z
Labels: Type: Bug, Priority: High, Area: MONIT, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8445

## Opening post (mapellidario, 2024-05-30T16:14:30Z)

since yesterday morning, when wa deployed the new publisher, we do not have some information about publisher in opensearch [1].

@novicecpp discovered that the bug was introduced in this [2] commit, because the new format [3] does not match with the pattern [4].

We should fix either the logs or the grok pattern

---

[1] https://monit-grafana.cern.ch/goto/aY7hrIyIg?orgId=11

![image](https://github.com/dmwm/CRABServer/assets/16376695/f51f286c-d6c8-4667-8954-97abb68fa681)

[2]

https://github.com/dmwm/CRABServer/commit/5ca7cae6d4ebe374f945eb46a7768a64c2b24fa2#diff-05952067180be4a11094445f167e8f83f9446df94a9d97ffc6a25a1eb1105a6cL727-R530

[3]

```plaintext
2024-05-30 14:10:51,016:INFO:PublisherMaster,531:Taskname 240530_110157:agungord_crab_CMSDAS_Data_analysis_test0 is OK. Published 22 in 1 blocks.
```

[4]

https://github.com/dmwm/CMSKubernetes/blob/169a72709365ad6e9d7acb8ad789880018f03fcc/kubernetes/cmsweb/monitoring/crab/logstash.conf#L116-L123

https://github.com/dmwm/CRABServer/blob/master/src/script/Monitor/logstash/crabtaskworker.conf#L68-L76

## Comment (belforte, 2024-05-30T20:44:32Z)

I believe it can be closed as fixed via https://github.com/dmwm/CRABServer/pull/8446
But since I was not part of the saga, I leave final word to you.
Many thanks to both for finding and fixing my mistake.
