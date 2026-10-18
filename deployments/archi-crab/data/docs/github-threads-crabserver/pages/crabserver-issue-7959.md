# dmwm/CRABServer issue #7959: improve runtime check on CPU abuse

State: open
Opened: 2023-10-18T13:37:15Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7959

## Opening post (belforte, 2023-10-18T13:37:15Z)

We currently have this in our scheduler config

SYSTEM_PERIODIC_REMOVE = .... || ((RemoteSysCpu + RemoteUserCpu) > (2 * RequestCpus * (Currenttime - JobCurrentStartExecutingDate))=?=True))

Which is meant to kill jobs which are using 2 time more CPU time than Clock time.
On some new machines somehow job initialization steps cause this to trigger in <20 seconds, before the user application starts.

We should change adding the requirement of a minimum running time, 5 minutes e.g.

So somehow add `&&(Currenttime - JobCurrentStartExecutingDate)>5*60` but I am not sure of how exactly to place this in the classAd, consultation with SI is needed, I think HTCondor has some way to test classAd expressions too.

The file to change on the machines is `/etc/condor/config.d/82_cms_schedd_crabschedd_generic.config` which comes via puppet from https://gitlab.cern.ch/CMSSI/cmsgwms-htcondor-configurations/-/blob/cern/configs/82_cms_schedd_crabschedd_generic.config?ref_type=heads#L213

See the discussion in https://mattermost.web.cern.ch/cms-o-and-c/pl/qw47wth4e7bzdncqnxw1py951e

## Comment (belforte, 2023-10-18T13:42:45Z)

**NOTICE** I have temporarily changed `/etc/condor/config.d/82_cms_schedd_crabschedd_generic.config` on vocms098 and disabled puppet on it
```
[root@vocms068 ~]# cat $(puppet config print  agent_disabled_lockfile); echo ""
{"disabled_message":"Stefano says: keep stable"}
[root@vocms068 ~]# 
```
we need to get enable again the agent in one or two weeks or the machine will be kicked out of the hostgroup

## Comment (belforte, 2023-10-18T13:44:14Z)

**NOTICE2** It would be good to have a way to push a different condor env via puppet on test machines like `vocms068` before applying to production schedulers. Is that possible now ? We may want to add to our documentation

## Comment (novicecpp, 2023-10-18T13:52:42Z)

Quick and dirty way to override config in puppet:
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/compare/7aa922ddccf16ea70ca7ff79367e771938bb915b...62d9302b2872d366a61d19d6b32f7878547bab73?from_project_id=4758&straight=false

(The change already committed in `crabdev_schedd` env/branch).

One quick question, do you need to restart condor/services/jobs to make new periodic remove effective?

## Comment (belforte, 2023-10-18T14:46:07Z)

awsome !
quick answer to quick question:  `sudo condor_reconfig`

## Comment (belforte, 2023-10-18T14:52:06Z)

It will only apply to new jobs. Jobs already submitted will not be changed not even if you restart everything, you would need to do a `condor_qedit`. But of course there's no such need here

## Comment (mmascher, 2023-10-18T15:08:36Z)

> Marco Mascheroni can you tell us the correct syntax to change RemoveHighCpu so that it waits until e.g. 5min from job start ? Please answer in [dmwm/CRABServer#7959](https://github.com/dmwm/CRABServer/issues/7959)

This is what I would do (not tested):

```
RemoveThreshold = ((JobUniverse=!=7)&&(JobUniverse=!=12)&&(((NumJobStarts>9)=?=True)||((NumShadowStarts>19)=?=True)) || ((DiskUsage>27000000)=?=True))
RemoveHighCpu = ((RemoteSysCpu + RemoteUserCpu) > (200 * RequestCpus * (Currenttime - JobCurrentStartExecutingDate))=?=True)
TenMinutesRuntime = ((Currenttime - JobCurrentStartExecutingDate) > 600)

SYSTEM_PERIODIC_REMOVE = ($(RemoveThreshold) || $(RemoveHighCpu) && $(TenMinutesRuntime))
SYSTEM_PERIODIC_REMOVE_REASON = \
   strcat("Job removed by SYSTEM_PERIODIC_REMOVE due to ", \
        ifThenElse(($(RemoveThreshold)), "** NumJobStarts OR NumShadowStarts or DiskUsage over limit", \
               ifThenElse(($(RemoveHighCpu) && $(TenMinutesRuntime)), "** CPU usage over limit ", \
                        "undefined reason." \
                               ) \
                                    ) \
                                       )

```
