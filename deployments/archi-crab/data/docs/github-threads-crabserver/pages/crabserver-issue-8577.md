# dmwm/CRABServer issue #8577: make sure that our T1Overflow works with new JobRouter

State: closed
Opened: 2024-08-01T15:50:39Z
Closed: 2024-10-17T13:51:29Z
Labels: Priority: High, Area: HTCondor, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8577

## Opening post (belforte, 2024-08-01T15:50:39Z)

HTCondor JobRouter will remove some deprecated functionalities in HTC 24.0
see https://htcondor.readthedocs.io/en/main/grid-computing/job-router.html
Those will also disappear in some 23.x but at least Stefano does not know `x` currently.

(those deprecations notices are there since at least 3 years)

- [x] review our use of JobRouter and check if we are using them
- [ ] if yes, do the needed changes and validate before we can switch production schedulers to new HTC

## Comment (belforte, 2024-08-05T14:45:54Z)

rats
![image](https://github.com/user-attachments/assets/664cd184-a874-4fe1-b02f-39f151779afd)

and of course our [config](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/templates/modules/condor/90_jobrouter.config.erb#L11) is based on `JOB_ROUTER_ENTRIES_CMD`

which means that we need to fully review/redo

## Comment (belforte, 2024-08-05T17:49:46Z)

At first sight we can replace the script with a set of static route tables, one for each T1.

## Comment (belforte, 2024-08-28T09:45:50Z)

On HOLD waiting for #8660

## Comment (aspiringmind-code, 2024-09-19T07:48:50Z)

@belforte Since #8660 is completed, should we remove the On Hold status?

## Comment (belforte, 2024-09-19T08:00:47Z)

thanks @aspiringmind-code .
Now that we are deploying HTC versions which do not support old way to pass commands to JobRouter, it is time to look into removing those commands as pert https://github.com/dmwm/CRABServer/issues/8577#issuecomment-2269595447

We currently force backward compatibility via setting HTC config. param 
[JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES](https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#JOB_ROUTER_USE_DEPRECATED_ROUTER_ENTRIES) to True as per #8660

## Comment (aspiringmind-code, 2024-10-17T13:51:29Z)

Fixed in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/260
