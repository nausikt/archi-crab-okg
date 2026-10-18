# dmwm/CRABServer issue #9272: Upgrade AP's Linux Kernel to 5.14.0-611.26.1.el9_7.x86_64 to address CVE-2022-50452 Security Vulnerabilities.

State: closed
Opened: 2026-02-12T18:06:32Z
Closed: 2026-02-25T15:51:19Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9272

## Opening post (nausikt, 2026-02-12T18:06:32Z)

As Gian Piero Siroli, Stefano pointed out.

There is a specific flaw within Linux handling of “sch_cake” in kernel version below `5.14.0-611.26.1.el9_7.x86_64`.
*P.S. See in details Red Hat's (CentOS upstream)* [CVE-2022-50452](https://cybersecuritynews.com/centos-9-vulnerability/)
_____
So, we will rolling drain and reboot following APs [1], following the Operations Checklist [2]:

*I did reboot the *vocms0197*, when at the time have least number of dagmans, running/idle jobs.*
*but its turned-out after schedd gets back up running it was extremely stressed with* [many-fold increase cpu, system loads](https://monit-grafana.cern.ch/d/JI0ulEKMz/cms-si3a-hosts-monitor?orgId=11&var-service=schedd&var-type=crabschedd&var-DS_PROMETHEUS=cmsmonitoring-victoriametrics&var-job=si&var-name=vocms0106.cern.ch&var-node=vocms0106&var-port=9100&from=1770902562000&to=1770918419000&var-productionSchedulers=All&var-schedd=All&var-User=gcoulon&var-monit_source=crab-prod-tw02.cern.ch&var-instance=vocms0197%3A9100&viewPanel=77). thus why inevitably have to draining much more.

[1] APs list
- [x] crab-preprod-scd03.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] crab-sched-901.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] crab-sched-903.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0106.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0107.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
- [x] vocms0119.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0120.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
- [x] vocms0121.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0122.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
- [x] vocms0137.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0144.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0155.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0194.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0195.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0196.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0197.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
- [x] vocms0198.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms0199.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms059.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms068.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] vocms069.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
- [x] crab-{dev|preprod|prod}-tw0X
- [x] crab-ci-runnerXX

[2] Operations Checklist. 
Checking kernel version: `wassh -c vocmsglidein/crabschedd 'uname -r'`
Upgrade kernel on every APs: `wassh -c vocmsglidein/crabschedd 'sudo dnf upgrade kernel'
```bash
# has to run as root; otherwise, the jobs cannot be found/matched/released.
condor_hold -constraint 'JobUniverse==7 && JobStatus==2' -reason "Upgrade Kernel"
condor_hold -constraint 'JobUniverse==7 && JobStatus==1' -reason "Upgrade Kernel"
condor_off -graceful
condor_status

# Maintenance then reboot
dnf upgrade kernel
reboot

condor_on
# Checking after reboot
condor_q -totals
condor_status -schedd
uname -r

# Check hold job then release
condor_q -con 'jobuniverse==7&&jobstatus==5'
condor_release -constraint 'JobUniverse==7'
```
\*\**Actually, we can simply reboot without these graceful process* in APs when have very few dagman/jobs running. 
\*\*I had tried on vocms059.cern.ch and my dagman/task reconnect and complete well. HTCondor is very resilient!

## Comment (nausikt, 2026-02-15T17:19:05Z)

We've upgraded 3 more nodes, vocom0107, vocms0120, vocms0122. I'm not sure this put too much load on the system [1,2].

I'll leaves all APs to rest for a day so the system can converge back to an equlibrium. Then we'll start rolling drain and reboot, 
**2** APs at a time, every **2** days instead.
[1]
<img width="994" height="286" alt="Image" src="https://github.com/user-attachments/assets/c7f73249-f6d3-44e6-b9db-0c4e72950c92" />
[2]
<img width="1489" height="345" alt="Image" src="https://github.com/user-attachments/assets/edf56d94-7e98-4733-bb1e-6ef8ed6aa7f1" />

## Comment (nausikt, 2026-02-24T19:50:49Z)

Guys, we've done with all crab schedds, I will proceed to crabtaskworker and ci-runners. may i touch you guys TW's test machine and preprod tomorrow morning? and do i need to announce CRAB maintainance/intervention for prod-tw01,02?
```bash
[kphornsi@aiadm99 ~]$ wassh -c vocmsglidein/crabschedd 'uname -r'
crab-preprod-scd03.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
crab-sched-901.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
crab-sched-903.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0106.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0107.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
vocms0119.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0120.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
vocms0121.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0122.cern.ch: 5.14.0-611.26.1.el9_7.x86_64
vocms0137.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0144.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0155.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0194.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0195.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0196.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0197.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0198.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms0199.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms059.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms068.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
vocms069.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
[kphornsi@aiadm99 ~]$ wassh -c vocmsglidein/crabtaskworker 'uname -r'
crab-dev-tw01.cern.ch: 5.14.0-503.33.1.el9_5.x86_64
crab-dev-tw02.cern.ch: 5.14.0-503.33.1.el9_5.x86_64
crab-dev-tw03.cern.ch: 5.14.0-427.33.1.el9_4.x86_64
crab-dev-tw04.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-dev-tw05.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-preprod-tw01.cern.ch: 5.14.0-362.24.2.el9_3.x86_64
crab-preprod-tw02.cern.ch: 5.14.0-503.33.1.el9_5.x86_64
crab-prod-tw01.cern.ch: 5.14.0-503.35.1.el9_5.x86_64
crab-prod-tw02.cern.ch: 5.14.0-362.24.2.el9_3.x86_64
```

## Comment (belforte, 2026-02-24T20:25:27Z)

I will reboot my TW (dev-tw010myself, thanks.
NO need to announce anything to users. It is an extremely short downtime for TW. If you are worried you can always disable canary, update tw02, see how it goes, then do tw01.

## Comment (nausikt, 2026-02-25T15:51:19Z)

Guys, I've done rolling upgrade and tested submission on all CRAB VMs as follows, they all back to normal operation well. 
I'll leave yours (tw01|tw02) at your convenience Stefano!
```
[kphornsi@aiadm01 ~]$ wassh -c vocmsglidein/crabtaskworker 'uname -r'
crab-dev-tw01.cern.ch: 5.14.0-503.33.1.el9_5.x86_64
crab-dev-tw02.cern.ch: 5.14.0-503.33.1.el9_5.x86_64
crab-dev-tw03.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-dev-tw04.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-dev-tw05.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-preprod-tw01.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-preprod-tw02.cern.ch: 5.14.0-611.34.1.el9_7.x86_64
crab-prod-tw01.cern.ch: 5.14.0-611.30.1.el9_7.x86_64
crab-prod-tw02.cern.ch: 5.14.0-611.27.1.el9_7.x86_64
[kphornsi@crab-ci-runner01 ~]$ uname -r
5.14.0-611.34.1.el9_7.x86_64
```
