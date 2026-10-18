# dmwm/CRABServer issue #9221: LogPipeline failed to captured crabserver-canary info thus canary response disappeared from CRAB crabserver timber monitoring.

State: closed
Opened: 2025-10-16T16:05:26Z
Closed: 2025-10-27T13:15:44Z
Labels: Type: Bug, Priority: Medium, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/9221

## Opening post (nausikt, 2025-10-16T16:05:26Z)

In the light of revising CRAB logstash's Grok on an on going [dmwm/CMSKubernetes#PR1661](https://github.com/dmwm/CMSKubernetes/pull/1661).

We also would like to fix this logstanding leftover issue of `crabserver-canary` doesn't appeared in [CRAB crabserver timber](https://monit-grafana.cern.ch/d/VML5DJEnk/crab-crabserver-timber?orgId=11&refresh=1m&from=now-12h&to=now&viewPanel=42).

As i've investigated, It still not obvious for me why `crabserver-canary` missing, everythings looks already right IMO, as you can see in [1], [2], [3], [4] but AToW i can confirm that filebeat [4], [5] writing & redirecting canary logs well to logstash grok.

So appologize for the delay of upstream PR, Since i've to copied realworld log both **primary** & **canary**, reproducing bugs  in **preprod** and test grok on finer details there. 

______
[1] Expected to work, Problematic Grok in **prod**:

> grok {
         match => { "message" => '\[%{NOTSPACE:timestamp_temp}\] %{DATA:backend} %{IPORHOST:clientip}     "%{WORD:method} %{NOTSPACE:request} %{DATA:httpversion}" %{NUMBER:code:int} %{DATA} \[data: (-|%{NUMB    ER:bytes_sent:int}) in (-|%{NUMBER:bytes_received:int}) out (-|%{NUMBER:time_spent_ms:int}) us \] \[a    uth: %{DATA} "%{DATA:dn}".*\] \[ref: "%{DATA}.*" "%{DATA:client}" \]' }
}

[2] Primary pod log in **prod**:
> 2025-10-16T15:08:40.857261Z stdout F [16/Oct/2025:17:08:40] crabserver-66d49b5bd-wd8gw 188.185.89.202 "GET /crabserver/prod/fileusertransfers?subresource=getById&id=e28266858f132b68c1af41b6bf010184e3bbeab99ea84fbfa145e022 HTTP/1.1" 200 OK [data: 1627 in 240 out 3133 us ] [auth: ok "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=jmurugan/CN=892934/CN=Jeevesh Murugan" "" ] [ref: "https://cmsweb.cern.ch" "CRABSchedd/v3.250820" ] - Podname=crabserver-66d49b5bd-wd8gw Type=cherrypylog

[3] Canary pod log in **prod**:
> 2025-10-16T14:33:11.787480461Z stdout F [16/Oct/2025:16:33:11] crabserver-canary-5655cf459f-bmsmp 188.184.89.113 "PUT /crabserver/prod/filemetadata HTTP/1.1" 200 OK [data: 3275 in 66 out 6399 us ] [auth: ok "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=ecannaer/CN=832417/CN=Ethan Michael Cannaert" "" ] [ref: "https://cmsweb.cern.ch" "CRABSchedd/v3.250820" ] - Podname=crabserver-canary-5655cf459f-bmsmp Type=cherrypylog


[4] Filebeat input log redirecting config. that already valid.
```yaml
- type: container
      paths:
        - /var/log/pods/crab_crabserver*/crabserver/*.log
      include_lines:
        - '\] (crabserver|crabserver-canary)-\w+-\w+ \d'
      tags:
        - "crabhttpcall"
```

[5] But I can confirm that canary pod logs was handled well by filebeat [4] across daemonset pods.
```bash
k -n crab get pods -l app=filebeat-crab -o name | xargs -I{} kubectl -n crab exec {} -- sh -lc 'ls -alh /var/log/pods | grep crab_crabserver'
drwxr-xr-x.  3 root root   24 Oct 14 13:53 crab_crabserver-66d49b5bd-wd8gw_45a80867-173c-43fd-b376-57b24cb67157
drwxr-xr-x.  3 root root   24 Oct 14 13:53 crab_crabserver-66d49b5bd-h2mxg_598cd490-f60b-4f24-99be-5da1b28a4235
drwxr-xr-x.  3 root root   24 Oct 14 13:53 crab_crabserver-66d49b5bd-2w5bt_5a4380f1-000b-46e6-8d11-ca35cbc8dbaf
drwxr-xr-x.  3 root root   24 Oct 14 13:53 crab_crabserver-66d49b5bd-gpqnh_e51b4ccc-35a5-4554-af03-94f7ec7ba888
drwxr-xr-x.  3 root root   24 Oct 14 13:53 crab_crabserver-canary-5655cf459f-bmsmp_09dfd620-10ed-4877-8fd6-71e52ff9dce1
....
```

## Comment (nausikt, 2025-10-27T12:13:58Z)

Current ***prod*** grok [1] seems to work correctly in capturing the canary log [2], but still doesn't appear in timber though.

I will be skeptical on first mile and investigate more on last mile e.g. from `filebeat` -> `logstash` and from `logstash` -> `timber`.

[1] 
```bash
\[%{NOTSPACE:timestamp_temp}\] %{DATA:backend} %{IPORHOST:clientip} "%{WORD:method} %{NOTSPACE:request} %{DATA:httpversion}" %{NUMBER:code:int} %{DATA} \[data: (-|%{NUMBER:bytes_sent:int}) in (-|%{NUMBER:bytes_received:int}) out (-|%{NUMBER:time_spent_ms:int}) us \] \[auth: %{DATA} "%{DATA:dn}".*\] \[ref: "%{DATA}.*" "%{DATA:client}" \]
```

[2] 
```bash
grok ❯ python test/test_grok.py

========== Processing: ./test/logs/canary.0.log ==========

========== Summary ==========
[OK] Total of 1677 lines were matched.
[FAIL] Total of 23739 lines were failed.

========== Preview, matched of ./test/logs/canary.0.log ==========
[OK] line 1: {'timestamp_temp': '16/Oct/2025:16:29:26', 'backend': 'crabserver-canary-5655cf459f-bmsmp', 'clientip': '188.185.89.202', 'method': 'PUT', 'request': '/crabserver/prod/fileusertransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2255, 'bytes_received': 36, 'time_spent_ms': 6436, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=jingyu/CN=757615/CN=Jingyu Luo', 'client': 'CRABSchedd/v3.250820'}
[OK] line 18: {'timestamp_temp': '16/Oct/2025:16:29:26', 'backend': 'crabserver-canary-5655cf459f-bmsmp', 'clientip': '188.185.101.116', 'method': 'PUT', 'request': '/crabserver/prod/filemetadata', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2376, 'bytes_received': 66, 'time_spent_ms': 5459, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=adattamu/CN=868108/CN=Aryaa Dattamunsi', 'client': 'CRABSchedd/v3.250820'}
[OK] line 31: {'timestamp_temp': '16/Oct/2025:16:29:26', 'backend': 'crabserver-canary-5655cf459f-bmsmp', 'clientip': '188.185.89.194', 'method': 'POST', 'request': '/crabserver/prod/filetransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 1711, 'bytes_received': 40, 'time_spent_ms': 4556, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=jingyu/CN=757615/CN=Jingyu Luo', 'client': 'CRABSchedd/v3.250820'}
[OK] line 59: {'timestamp_temp': '16/Oct/2025:16:29:27', 'backend': 'crabserver-canary-5655cf459f-bmsmp', 'clientip': '188.184.75.82', 'method': 'POST', 'request': '/crabserver/prod/task', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 1697, 'bytes_received': 70, 'time_spent_ms': 110784, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=rosingh/CN=853383/CN=Rohit Kumar Singh', 'client': 'CRABSchedd/v3.250820'}

========== Processing: ./test/logs/primary.0.log ==========

========== Summary ==========
[OK] Total of 771 lines were matched.
[FAIL] Total of 11526 lines were failed.

========== Preview, matched of ./test/logs/primary.0.log ==========
[OK] line 15: {'timestamp_temp': '16/Oct/2025:17:07:04', 'backend': 'crabserver-66d49b5bd-wd8gw', 'clientip': '188.185.101.116', 'method': 'PUT', 'request': '/crabserver/prod/filemetadata', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2406, 'bytes_received': 66, 'time_spent_ms': 5013, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=adattamu/CN=868108/CN=Aryaa Dattamunsi', 'client': 'CRABSchedd/v3.251002'}
[OK] line 28: {'timestamp_temp': '16/Oct/2025:17:07:04', 'backend': 'crabserver-66d49b5bd-wd8gw', 'clientip': '188.184.75.82', 'method': 'PUT', 'request': '/crabserver/prod/fileusertransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2253, 'bytes_received': 36, 'time_spent_ms': 4045, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=adattamu/CN=868108/CN=Aryaa Dattamunsi', 'client': 'CRABSchedd/v3.251002'}
[OK] line 41: {'timestamp_temp': '16/Oct/2025:17:07:04', 'backend': 'crabserver-66d49b5bd-wd8gw', 'clientip': '188.184.73.32', 'method': 'POST', 'request': '/crabserver/prod/filetransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 1710, 'bytes_received': 40, 'time_spent_ms': 3726, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=yilinz/CN=848685/CN=Yilin Zhou', 'client': 'CRABSchedd/v3.250820'}
[OK] line 54: {'timestamp_temp': '16/Oct/2025:17:07:04', 'backend': 'crabserver-66d49b5bd-wd8gw', 'clientip': '188.184.89.113', 'method': 'PUT', 'request': '/crabserver/prod/fileusertransfers', 'httpversion': 'HTTP/1.1', 'code': 200, 'bytes_sent': 2255, 'bytes_received': 36, 'time_spent_ms': 5552, 'dn': '/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=adattamu/CN=868108/CN=Aryaa Dattamunsi', 'client': 'CRABSchedd/v3.251002'}
```

## Comment (belforte, 2025-10-27T13:15:20Z)

if this is not straightforward, what about finalizing grok pattern around current setup and complete transition to argocd. Then come back to the missing pods mistery ?

## Comment (nausikt, 2025-10-27T13:15:45Z)

OMG, it's the **first mile**, even **Filebeat** configmap was renewed in live `prod`, but we didn't triggered rollout restart to let daemonset pick up new config.

P.S. Now, i start to appreciated `kustomize` features even more, that they try to suffixing the configmap name/ and their corresponding deployment mounting config (suffix with content hash), which will automatically triggered rollout restart every time content changed.

[1] filebeat.yml config inside mounted in pod, wasn't refreshed for all this time though.
```bash
filebeat@filebeat-crab-27jgb:~$ cat /etc/filebeat.yml
filebeat.inputs:
- type: container
  paths:
    - /var/log/pods/crab_crabserver*/crabserver/*.log
  include_lines:
    - '\] crabserver-\w+-\w+ \d'
  tags:
    - "crabhttpcall"
- type: container
  paths:
    - /var/log/pods/crab_crabserver*/crabserver/*.log
  include_lines:
    - 'MeasureTime:seconds - '
    - 'MeasureSize:bytes - '
  tags:
    - "crabrest"
output.logstash:
  hosts: ["logstash:5044"]
  compression_level: 3
  bulk_max_size: 4096
queue.mem:
  events: 65536
logging.metrics.enabled: false
logging.level: infofilebeat@filebeat-crab-27jgb:~$
```

[2] Logstash start to pick up canary logs from filebeat thus Timber is starting to show canary response status by pod now.
Or you can have a look at Grafana [CRAB crabserver timber](https://monit-grafana.cern.ch/d/VML5DJEnk/crab-crabserver-timber?orgId=11&refresh=1m&from=now-12h&to=now&viewPanel=42).
<img width="1474" height="741" alt="Image" src="https://github.com/user-attachments/assets/c4401407-7302-4233-b8bb-e8ce20d730e6" />

## Comment (nausikt, 2025-10-27T13:16:32Z)

> if this is not straightforward, what about finalizing grok pattern around current setup and complete transition to arguscd. Then come back to the missing pods mistery ?

Ack Stefano, will get it done now.

## Comment (belforte, 2025-10-27T13:22:58Z)

do I read it correctly that arguscd would have fixed this as well ?

## Comment (nausikt, 2025-10-27T13:34:22Z)

> do I read it correctly that arguscd would have fixed this as well ?

In Short: **No**, having to implement a bit.

ArgoCD alone, in case of configmap content changed. will **not** automatically trigger rollout restart on relevant deployment/daemonset.

We have to implement this features in `Helm` templating [1] ourself, thus deployment or daemonset aware of content changes somehow.

OR in case of `Kustomize`'s configMapGenerator, it will take care of suffixing the configmap name as another way to versioning it thus automatically rollout restart for us by default.

[1] Exp, trivial implementation on Helm chart.
```yaml
spec:
  template:
    metadata:
      annotations:
        configHash: "{{ .Values.configMap | toYaml | sha256sum }}"
```

## Comment (belforte, 2025-10-27T13:48:52Z)

😮 
do I have to fear that same "config change does not trigger restart" applies to e.g. changes to CRAB's config.py or CRABServerAuth.py ?
Sorry for being so confused here, I do not really understand what configmap refers to.
Anyhow your [1] looks very good. Thanks !!!

## Comment (nausikt, 2025-10-27T13:53:35Z)

We have to fear man... it does applied to all configmaps in general. but don't worry we will patch this feature covered all configmaps in upstream PR, helm chart update, as well.
