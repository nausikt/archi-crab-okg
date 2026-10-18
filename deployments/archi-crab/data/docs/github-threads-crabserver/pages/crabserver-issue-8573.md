# dmwm/CRABServer issue #8573: monit - TW stopped sending data to logstash-opensearch after latest deployment to production

State: closed
Opened: 2024-07-30T12:34:12Z
Closed: 2024-12-12T10:13:54Z
Labels: Type: Bug, Priority: High, Area: MONIT, PyPI
URL: https://github.com/dmwm/CRABServer/issues/8573

## Opening post (mapellidario, 2024-07-30T12:34:12Z)

The most recent TW image `v3.240716-stable` does not send data to logstash-opensearch, so some panels in "CRAB Overview" dashboard are now empty [1].

This issue is similar to https://github.com/dmwm/CRABServer/issues/8568

fyi: @novicecpp 

---

[1] https://monit-grafana.cern.ch/goto/IG-A4MrSR?orgId=11

<details>

![image](https://github.com/user-attachments/assets/25f7d390-bba8-44a5-96f4-c52876a51766)

</details>

## Comment (belforte, 2024-12-12T10:13:54Z)

fixed
