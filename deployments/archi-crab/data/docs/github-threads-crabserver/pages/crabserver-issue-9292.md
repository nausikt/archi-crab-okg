# dmwm/CRABServer issue #9292: continuation of migrate VM's to new hypervisors in 2026

State: closed
Opened: 2026-04-09T12:58:45Z
Closed: 2026-04-29T08:48:32Z
Labels: Priority: Medium, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9292

## Opening post (nausikt, 2026-04-09T12:58:45Z)

As a continuation of the Hardware replacement campaign 2025 [OTG0160233](https://cern.service-now.com/service-portal?id=outage&n=OTG0160233) (#8955), related announcement in [ITUM March 2026](https://indico.cern.ch/event/1611294/)

This year, we have 5 VMs affected in "CMS CRAB" project. we need to rolling-drain these Schedds (AP) in advance.

VM Name | Recommended Action | Flavor | Compatible Flavor | Status
-- | -- | -- | -- | --
crab-prod-tw02 | RESIZE | r2.2xlarge | m4.2xlarge | Done
vocms0144 | RESIZE | r2.2xlarge | m4.2xlarge | Done
vocms0195 | RESIZE | r2.2xlarge | m4.2xlarge | Done
vocms0197 | RESIZE | r2.2xlarge | m4.2xlarge | Done
vocms0199 | RESIZE | r2.2xlarge | m4.2xlarge | Done

***Please be aware that we need to recreate or resize the VMs to m4 flavors. Operations like rebuild or resize to m2 are not sufficient for this campaign.***

## Deadline
- ***July 30th 2026***

## Instruction
we can resize them to a compatible flavor indicated in the table above. Resize implies a **downtime** depending on **the amount of data on the disk** and the load on the infrastructure during the resize. It may last from 15 minutes to 8 hours.</p>

We've been recommended to run the following cmd to discard any unused filesystem blocks, making the resize operation quicker
```
fstrim -va
```

<p>The full detail of RESIZE operation instruction can be seen here: <a href="https://clouddocs.web.cern.ch/using_openstack/resizing_a_vm.html" class="external-link" target="_blank" rel="noopener nofollow" aria-label="https://clouddocs.web.cern.ch/using_openstack/resizing_a_vm.html" data-tooltip-position="top">instructions</a><br>

## Example
1) Verify current flavor, `openstack server show --fit-width vocms0197`
> | flavor                      | disk='160', ephemeral='0', extra_specs.hw_rng:allowed='True', original_name='r2.2xlarge',            |
> |                             | ram='60000', swap='0', vcpus='16'

2) Verify available & compatible flavor, `openstack flavor list`
> | <id> | r2.2xlarge | 60000 |  160 |         0 |    16 | False     |
> | <id> | m4.2xlarge | 60000 |  160 |         0 |    16 | False     |

3) On Schedd/VM, clean fs up a bit, shutdown HTCondor, shutdown VM. (After drained)
*P.S See also [How to shutdown CRAB](https://cmscrab.docs.cern.ch/operations/crab-shutdown.html#crab-shutdown-drain-schedds), https://github.com/dmwm/CRABServer/issues/6781*

3.1) as Root, keep list of running dags for holding & releasing after intervention.
```bash
condor_q -con 'jobuniverse==7&&jobstatus==2' -af clusterid > Running_DAGs.2026.migrated.hypervisor.list
```
3.2) hold DagMans, then check `condor_q -con 'jobuniverse==7&&jobstatus==2' -af clusterid` (should return nothing)
```
for dag in `cat Running_DAGs.2026.migrated.hypervisor.list`; do
        condor_qedit $dag  HoldKillSig \"SIGKILL\"
        condor_hold $dag
done
```
3.3) `condor_off`, make sure logs show
```
[root@vocms0197 ~]# tail /var/log/condor/MasterLog
04/09/26 16:25:35 The SCHEDD (pid 2076280) exited with status 0
04/09/26 16:25:35 All daemons are gone
```
3.4) `fstrim -va` (took almost 10 mins)
```
[root@vocms0197 ~]# fstrim -va
/data: 437 GiB (469189685248 bytes) trimmed on /dev/vdc
/home/grid: 150.9 GiB (162040864768 bytes) trimmed on /dev/vdb
/boot/efi: 536.5 MiB (562528256 bytes) trimmed on /dev/vda15
/: 159.5 GiB (171220905984 bytes) trimmed on /dev/vda1
```
3.5) Then, we can safely `shutdown` VM.

4) Resize, `openstack server resize --flavor m4.2xlarge vocms0197`
*verify and confirm resizing (if any there's any issue **openstack server resize revert <vm_name>***
```
openstack server show --fit-width vocms0197 # if details looks good, then confirm
openstack server resize confirm vocms0197
```
5) starting and verifying machine.
```
openstack server start vocms0197
root@vocms0197> lscpu
Architecture:                x86_64
  CPU op-mode(s):            32-bit, 64-bit
  Address sizes:             48 bits physical, 57 bits virtual
  Byte Order:                Little Endian
CPU(s):                      16
...
root@vocms0197> cat /proc/meminfo
MemTotal:       59991236 kB
```
6) `condor_on` and releasing the hold running DagMans.
```
for dag in `cat Running_DAGs.2026.migrated.hypervisor.list`; do
        condor_qedit $dag  HoldKillSig \"SIGKILL\"
        condor_release $dag
done
```
7) verify `condor_q -con 'jobuniverse==7&&jobstatus==2' -af clusterid `.
*the cmd should gave us same number of running dags been released (in my case 17 dags was running before intervention.*
8) Done.

## Comment (nausikt, 2026-04-09T15:31:59Z)

We've migrated `vocms0197` to a new hypervisor with the `m4.2xlarge` flavor.
*(same configuration of 16 vCPUs and 60 GB RAM)*

`vocms0197` is now back in service, and `vocms0199` is currently being drained.

## Comment (nausikt, 2026-04-17T15:05:26Z)

`vocms0199` is now back in service, and `vocms0195` is currently being drained.

## Comment (nausikt, 2026-04-29T08:48:32Z)

All remaining machines were force-resized by CERN IT during 20–22 April due to urgent disk issues.
