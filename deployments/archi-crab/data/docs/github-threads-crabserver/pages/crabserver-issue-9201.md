# dmwm/CRABServer issue #9201: move handling of htcondorPool and htcondorSchedds list to TW config and manage them via puppet

State: closed
Opened: 2025-10-01T20:59:10Z
Closed: 2025-10-16T11:25:45Z
Labels: Type: Enhancement, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9201

## Opening post (belforte, 2025-10-01T20:59:10Z)

see #9167 

so that we can deprecate the external config. for crab server

This may also require to cleanup the use of web proxy, i.e remove `proxiedurl` from schedd list, keep only name and weight

## Comment (nausikt, 2025-10-02T16:05:59Z)

- [x] Write micro-ADR, have discussion, see also [MR#371-comment](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/371#note_10200202)
- [x] introduce `htcondorPool`, `htcondorSchedds` via crabtaskworker hostgroup hiera, see Also [ai/it-puppet-hostgroup-vocmsglidein, MR#371](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/371)
- [x] verify whether it propagates to all TWs, both in `qa`, `prod` envs.
- [x] switch TaskWorker code to use this new `attrs` from `TaskWorkConfig.py` instead, then clean-up `scheddObj`, `proxiedUrl`, ... etc. https://github.com/dmwm/CRABServer/pull/9203

CC. @belforte

## Comment (nausikt, 2025-10-03T09:36:45Z)

Thank you for quick review! I've wrote micro-ADR as you suggested there, [MR#371-comment](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/371#note_10200202).

## Comment (nausikt, 2025-10-06T10:20:40Z)

I've fixed, re-propagated on to `qa`, and did e2e test at `test14` once again. It's working fine now. will proceeding to the last mile.

P.S. Apologize for slipped away mess, i've extensively tested rendering/validity of python file on my local though. but unfortunately before pushed, i blindly replaced my TaskWorkerConfig.py.erb from my slack workspace. and didn't do e2e test properly last Friday. just checked the new attrs was there, Sorry Man! @belforte
```
> puppet apply --hiera_config hiera.yaml render.pp
tmp
├── data
│   └── common.yaml
├── hiera.yaml
├── render.pp
└── TaskWorkerConfig.py.erb
> cat TaskWorkerConfig.py.erb | grep code
code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb
```

## Comment (nausikt, 2025-10-07T13:41:55Z)

NO URGENT, Ciao Stefano! @belforte, please take your time with your family.

For Clarity, let me laid out a cleanup plan, and listen to your guidances on [4,5] that's non-obvious to me please?
- [x] After, we merged/switched to TaskWorker side, https://github.com/dmwm/CRABServer/pull/9203
- [x] releasing to TW canary for reasonable amount of time.

Then, we good to deprecate dependencies on central config backend-urls at REST in the following places:
### Straightforward places
- [ ] **[1]** backendurls endpoint that just serves retrieved external config.
*P.S. where we use it as adhoc endpoint during this refactoring.*
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTServerInfo.py#L45-L54
- [ ] **[2]** inside `getCentralConfig(extconfigurl)` utility function, we can safely remove `backend-urls` and no longer need to retrieve `htcondorScheddsLink`, htcondor{Pool|Schedds}` relevant, stuffs there.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/Utilities.py#L127-L131
- [ ] **[3]**  `ProxiedUrl` that could be embed as a `static` pattern, thus no longer need to fetch from dynamically external config.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTTask.py#L236-L257

### Non-trivial places
- [ ] **[4]** logic on REST that retreived backend-urls to just to doing some kind of setting default value to `collector` equal to `htcondorPool` from global external config. (wrote 10 yrs++ ago)
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/DataWorkflow.py#L151-L155
> This one might be trivial at first glance by just migrating this logic to TW, where backend-urls info was there.
> BUT AFAIU,  collector was expected to be dumped into database, `tm_collector` task information? by other mean expected to be resolved earlier in crab submit lifecycle given current design? do we have any TaskAction perfect with to write/send this resolved information of `finalized` solver, back to REST when we do submit?

- [ ] **[5]** The last script that still call **[1]** *backendurls* endpoint, which i don't know whether it's still be used or we could safely deprecated them.
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/scripts/Monitor/dashbgen.sh#L50-L68

## Comment (belforte, 2025-10-07T13:56:24Z)

let's worry later about the cleanup and do one thing at a time, so it is easier to have a conversation

## Comment (belforte, 2025-10-07T14:01:31Z)

but I'd like to fully get rid of any reference to `central config` and of 
` conn_handler` .  I am surprised that submitting a task requires a `collector` to be specifies. DataWorkflow.py needs some proper review.

## Comment (belforte, 2025-10-15T13:46:21Z)

@nausikt should this be closed and a new opened about cleanup ?
