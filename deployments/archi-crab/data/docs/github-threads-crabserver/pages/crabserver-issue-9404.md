# dmwm/CRABServer issue #9404: set remove reason in dagman killer

State: closed
Opened: 2026-08-28T15:37:12Z
Closed: 2026-09-23T15:14:43Z
URL: https://github.com/dmwm/CRABServer/issues/9404

## Opening post (belforte, 2026-08-28T15:37:12Z)

[schedd.act](https://htcondor.readthedocs.io/en/latest/apis/python-bindings/api/version2/htcondor2/schedd.html#htcondor2.Schedd.act) takes a reason argument.
We should use to change from the current default to e.g. 'killed by CRAB'

Possibly also detect when action is initiated by user vs. operator (in crabserver API) and tune reason accordingly

And could extend crabserver API so we can add a reason when killing is initiated by ASO in
https://github.com/dmwm/CRABServer/blob/eb8db5c5f2c432d006b54edb390abf15e8610b58/src/python/TaskWorker/Actions/PostJob.py#L3214-L3220

The relevant REST call is
https://github.com/dmwm/CRABServer/blob/eb8db5c5f2c432d006b54edb390abf15e8610b58/src/python/CRABInterface/RESTUserWorkflow.py#L629
