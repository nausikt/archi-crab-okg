# dmwm/CRABServer issue #7609: schedd - use a smaller openstack flavor

State: closed
Opened: 2023-04-20T11:53:16Z
Closed: 2024-02-07T11:00:59Z
Labels: Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7609

## Opening post (mapellidario, 2023-04-20T11:53:16Z)

#### introduction

CMS O&C have been asked to assess whether the CPU usage in CERN Openstack is reasonable.

Usage in this context means "number of CPUs that are allocated to instantiated physical or virtual machines", there is no distinction between idle or busy CPUs, nor between "normal" and overcommitted VM flavors.  

#### details

In CRAB, we use CPUs mainly for our schedd VMs. If we want to reduce the number of CPUs that we allocate, this is where to start having a look at.

We had many ideas on how to achieve this, but the easiest and more promising is to simply switch to a smaller openstack flavor, from `r2.2xlarge ` (16cpu, 60GB) to `r2.xlarge ` (8cpu, 30GB).

According to our grafana dashboard [1], this flavor should suit our needs

#### plan

agreed

- [ ] create a couple of `r2.xlarge` schedd VM
- [ ] add it to the global pool
- [ ] let them run for some months
- [ ] assess theit cpu and memory usage over time

Still open question

- [ ] do we need/want to remove a running schedd? i would say we do not really need to... 
- [ ] should we also reduce the size of the itb schedd? or do CMS SI need them to be as big as current production schedds for their scale tests? I will ask Nikos.

---

[1] https://monit-grafana.cern.ch/goto/4kCVgxE4z?orgId=11

## Comment (novicecpp, 2023-04-20T15:52:23Z)

> do we need/want to remove a running schedd? i would say we do not really need to...

Point is to make sure new smaller machine have same load as old one. You may drain the old one or adjust weight in https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-shedds-config.json

## Comment (belforte, 2024-02-07T11:00:56Z)

we are happy as we are
