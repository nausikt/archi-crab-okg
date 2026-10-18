# dmwm/CRABServer issue #9393: fix lifetime of proxy sent to schedd

State: closed
Opened: 2026-08-24T09:08:44Z
Closed: 2026-08-24T10:14:11Z
URL: https://github.com/dmwm/CRABServer/issues/9393

## Opening post (belforte, 2026-08-24T09:08:44Z)

we currently use
https://github.com/dmwm/CRABServer/blob/fc9b728ee00162aedcc66eeee0ff9872e1d34e87/src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py#L136

but this pushed a 24h proxy to schedd, while we create 7-days ones.

This is uselessly dangerous in case RenewRemoteProxies has a problem for a day or so.

After looking at [documentation](https://htcondor.readthed ocs.io/en/latest/apis/python-bindings/api/version2/htcondor2/schedd.html#htcondor2.Schedd.refreshGSIProxy) it is clear that we should set ` lifetime=0` instead.

<img width="739" height="291" alt="Image" src="https://github.com/user-attachments/assets/998a2df4-1ee0-455d-a203-b6e555e39b08" />
