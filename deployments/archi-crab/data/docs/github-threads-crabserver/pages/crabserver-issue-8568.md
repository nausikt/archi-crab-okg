# dmwm/CRABServer issue #8568: Process fds count in REST is broken in new PyPI image

State: closed
Opened: 2024-07-29T15:20:25Z
Closed: 2024-07-29T16:23:28Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8568

## Opening post (novicecpp, 2024-07-29T15:20:25Z)

In REST, we depend monitoring scripts/binaries from [RPM version of cmsweb image](https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/cmsweb/Dockerfile#L72-L81).
And then we add our entrypoint, [monitor.sh](https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/crabserver/monitor.sh) to [our RPM image](https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/crabserver/Dockerfile#L26).

This step is lost when migrating to a new PyPI image, [making the monitoring fail](https://mattermost.web.cern.ch/cms-o-and-c/pl/ezawwczcojndbgtzsdz1qyan5o).

Note that process fds count is a must for REST service.

## Comment (mapellidario, 2024-07-30T09:05:45Z)

A very similar thing happened for the TW image [1], should we re-open this issue or should we create a new one?

---

[1] https://monit-grafana.cern.ch/goto/IG-A4MrSR?orgId=11

<details>

![image](https://github.com/user-attachments/assets/25f7d390-bba8-44a5-96f4-c52876a51766)

</details>

## Comment (belforte, 2024-07-30T09:42:05Z)

new one
