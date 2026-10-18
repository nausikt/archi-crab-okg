# dmwm/CRABServer issue #8933: remove code related to HTCondor v1 vs. v2 API. Only V2 now

State: open
Opened: 2025-02-17T22:02:27Z
Labels: Status: In Progress, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8933

## Opening post (belforte, 2025-02-17T22:02:27Z)

get rid of all the `if's` like 

```python
if 'useHtcV2' in os.environ:
```
and all the code which deals with finding/putting `useHtcV2` in the environment  including hiera files in Puppet

## Comment (belforte, 2025-02-19T09:17:32Z)

switch for v1/v2 API in code was removed in https://github.com/dmwm/CRABServer/pull/8936
Still to do:

* look for any python file still using v1 API like src/python/TaskWorker/Actions/Recurring/RenewRemoteProxies.py
   * that did not work in v2 last year, maybe htcondor developers fixed this by now ?
* cleanup hiera files and template in puppet
* any other place ?

## Comment (belforte, 2025-03-31T08:51:11Z)

* clean up to be done in "puppet land":
```console
LapSB:it-puppet-hostgroup-vocmsglidein$ rg -i htcv2 
data/fqdns/crab-preprod-tw02.cern.ch.yaml
29:tw_useHtcV2: "True"

data/fqdns/crab-prod-tw01.cern.ch.yaml
25:tw_useHtcV2: "True"

data/fqdns/crab-prod-tw02.cern.ch.yaml
24:tw_useHtcV2: "True"

data/fqdns/crab-dev-tw01.cern.ch.yaml
26:tw_useHtcV2: "True"

data/fqdns/crab-preprod-tw01.cern.ch.yaml
29:tw_useHtcV2: "True"

code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb
72:<% if !@tw_useHtcV2.nil? && !@tw_useHtcV2.to_s.empty? -%>
73:config.TaskWorker.useHtcV2 = <%= @tw_useHtcV2.to_s %>
128:if getattr(config.TaskWorker, 'useHtcV2', None):
129:    os.environ['useHtcV2'] = 'True'
131:    os.environ.pop('useHtcV2', None)

code/manifests/crabtaskworker/indocker.pp
19:  $tw_useHtcV2 = hiera('tw_useHtcV2', 'False')
LapSB:it-puppet-hostgroup-vocmsglidein$ 
```

* `RenewRemoteProxies.py` can now be addresses since the method has ben ported to v2:
`<bound method Schedd.refreshGSIProxy of <htcondor2._schedd.Schedd object at 0x7fa1a45b2f10>>`
in `'$CondorVersion: 24.0.6 2025-03-05 BuildID: 790851 PackageID: 24.0.6-1 `
