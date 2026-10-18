# dmwm/CRABServer issue #8258: move all schedulers to Alma9

State: closed
Opened: 2024-02-23T09:17:03Z
Closed: 2024-04-17T13:57:18Z
Labels: Status: In Progress, OPERATION, alma9
URL: https://github.com/dmwm/CRABServer/issues/8258

## Opening post (belforte, 2024-02-23T09:17:03Z)

Needs to be completed by end of May, as per request from Submission Infrastructure

Code developments needed:
- [x] Depends on #8256

## Comment (belforte, 2024-02-23T10:04:31Z)

**Strategical points**
* Stefano and Marco discussed a possible plan, and Marco also talked with Jaime.
* HTCondor23 is very little changed from HTCondor10 (it is effectively an Htcondor11, they decide to change numeration of versions to use the year as major version number, htcondor24 is still not out !)
* We can expect full compatibility:
   1). a scheduler with HTCondor23 can run in a pool where CentralManagers are HTCondo10 and viceversa. We can independently update schedulers one at a time and SI can independently work on collector and negotiator as they like
   2).  current python bindings (HTCcondor10) work with schedulers at HTC23. We can update all schedulers and only later worry about having HTC23 bindings in TW
   3) there is no change in condor logs format, so we can upgrade to HTC23 a running scheduler and it will resume all jobs which were running when it was stopped.
   4) corrollary of 3) : since all condor information is on /data disk (a CEPH volume) we expect to be able to shutdown one scheduler, rebuild the same VM on alma9, reconnect same CEPH volumes, and restart having it pickup where it left.

## Comment (belforte, 2024-02-23T10:37:41Z)

**STATUS as of Feb 22**

I have moved  [1] `crab-preprod-scd03` to HTCondor23 (`23.0.2-1.el7`) and it is working in ITB pool with current TW which uses HTCondor10 python bindings, this verifies 1) and 2) above.

I am running more jobs while looking at adding an alma9 machine.

[1] list of actions I took, before I forget
 * [change]( https://gitlab.cern.ch/ai/it-puppet-environments/-/commit/b572a1640b995e0a2292c9039fe74efbed9a8780) the `crabdev_schedd` puppet environment so that it picks `vocmshtcondor` module from `update_condor` branch in SI repo
    * that is needed because the master and qa branches in their repo do not have the settings for the HTCondor23 repository [ref](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/compare/master...update_htcondor?from_project_id=10641&straight=false) 
 * [change](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/c5b3cdd16ebd0c3f36f6534145ad3c6937152e83
) YAML file for `crab-preprod-scd03` in `crabdev_schedd` branch of our repository to use  `condor_version: 23.0.2-1.el7` 
 * `condor_off`, run puppet, `condor_on` .. it took a bit, but it came up OK. Not very challenging since there was no running jobs. We need to do it again on a busy schedd

## Comment (belforte, 2024-02-23T23:02:50Z)

**Alma9**

I created a puppettized VM with
```
belforte@aiadm01/~> ai-bs  --landb-responsible cms-service-crab3htcondor-admins    --nova-flavor m2.medium --alma9 --foreman-environment "crabdev_schedd" -g "vocmsglidein/crabschedd" crab-sched-901
```

but puppet fails with

Could not retrieve catalog from remote server: Error 500 on SERVER: Server Error: Evaluation Error: Error while evaluating a Function Call, On 23rd August 2023 UMD repsitories do not exist for for EL8 and newer - please report if this is no longer true (file: /mnt/puppetnfsdir/environments/crabdev_schedd/modules/umd/manifests/init.pp, line: 24, column: 5) on node crab-sched-901.cern.ch

Looks like we need a new puppet environment where to test changes to the puppet configuration. This is quickly getting more work than I thought.

## Comment (belforte, 2024-02-23T23:38:28Z)

My ignorance run deeper. I have created that test sched on CC7, expecting something that "works like crab-preprod-scd03" but this time puppet fails with
```
Could not retrieve catalog from remote server: Error 500 on SERVER: Server Error:
Function lookup() did not find a value for the name 'glidecondor_pool' on node crab-sched-701.cern.ch
```
and I can't log on the machine, do not know if because puppet did not complete or because something else is/was wrong.
```
belforte@aiadm84/~> ssh crab-sched-701
belforte@crab-sched-701: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

## Comment (belforte, 2024-02-23T23:50:28Z)

maybe ` did not find a value for the name 'glidecondor_pool' on node crab-sched-701.cern.ch` is because there was no YAML file for this host in `/data/fqdns` in gitlab. I [added it](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/130) let's see what happens when puppet runs again
Can't simply add a small machine w/o ceph volumes with our puppet setup and I'd rather not change existing profiles. Giving up

## Comment (belforte, 2024-02-26T11:40:23Z)

after consulting with @novicecpp I decided to go for a new puppet environment  `crab_alma9`. I will aim to create a simlple VM where I can log in first and then add various packages.

## Comment (belforte, 2024-02-28T16:33:06Z)

**Update on alma9**
(I will delete previous comments)

There are now two small VM's running with alma9 puppettized as CRAB schedulers.
* `crab-sched-901`  currently runs `HTCondor 10.2.0-1.el9`
* `crab-sched-901`  currenlty runs `HTCondor 23.0.3-1.el9`

Both are part of ITB poo.. Both are in Foreman hostgroup [vocmsglidein/crabschedd](https://judy.cern.ch/hosts?search=hostgroup_title+%3D+%22vocmsglidein%2Fcrabschedd%22) using  puppet environment [crab_alma9](https://gitlab.cern.ch/ai/it-puppet-environments/-/blob/master/crab_alma9.yaml?ref_type=heads) i.e. puppet manifests and from [crab_alma9](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/tree/crab_alma9?ref_type=heads) branch of our repo

The way to get there was:
1. start with `crab_alma9` branch from current `qa`
1. create VM's with ` ai-bs  --landb-responsible cms-service-crab3htcondor-admins    --nova-flavor m2.medium --alma9 --foreman-environment "crab_alma9" -g "vocmsglidein" crab-sched-901`  to have minimal set of manifests. Create `data/fqdns` for them as a copy of another sched. Slowly change things in the manifest until errors are gone and I can log in. Trickiest part was AFS where a reboot was needed. At this point one can only login with a K5 token using `ssh root@crab-sched-901`
2. move machine to `vocmsglidein/crabschedd` hostgroup and again go through puppet errors solving one module at a time, now faster because I can use `puppet agent -tv`.
3. history of changes is not very useful (likely) and is in gitlab history for the `crab_alma9` branch
4. ask Florian to add repository for condor 10 on el9 to their [yum_repos.pp](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/blob/update_htcondor/code/manifests/yum_repos.pp?ref_type=heads) (branch `update_condor`) so that condor install works

7. ask Florian to put tokens for the new machines in tbag

## Comment (belforte, 2024-02-28T17:06:15Z)

TO DO

 - [x] Install FTS python client https://fts3-docs.web.cern.ch/fts3-docs/docs/cli/installation.html
 - [x] Test Rucio client from CVMFS
 - [ ] WMArchiveUploader setup fails in puppet ( #8265 )
 - [x] firewall : import code from hostgroup-cmssi firewall.pp
 - [ ] Prometheus: I am not sure what needs to be done, we have a lot of port open listed in our firewall, but it is different from what SI uses. time to review ?
 - [x] in `crabschedd/condor.pp` introduce a condor config file with the line` SHADOW = $(SBIN)/condor_shadow`  [ref.](https://mattermost.web.cern.ch/cms-o-and-c/pl/56aj5fz8f3gizmys7p33be3wna) - now in `/etc/condor/config/d/83_...`
 - [x] There's a bunch of scripts in `code/files/crabschedd` which need to be adapted to `python3`, not `python` (scripts which come with CRAB submission already run in python3)
    - [x]  cron.wrapper.sh --> created cron.wrapper.py3.sh
    - [x] CrabDag.py (used in JobCleanup.py compiles in py3) --> no change
    - [x] JobCleanuipAlarms.py (used in JobCleanup.py compiles in py3) --> no change
    - [x] JobCleanup.py --> created JobCleanup-py3.py
        - [x] stderr opened but not closed. Give error mail in py3. To fix. 
    - [x] jobhistoryfeeder.py (run as crontab) --> jobhistoryfeeder-py3.py
    - [x] glexec_errors.py (unused ? a gWMS leftover to remove ?) --> try to ignore
    - [x] htcondor_ads.py (unused ? seems connected to glexec)) --> try to ignore
    - [x] check_maxdags.py (unused ? seems connected to glexec)) --> try to ignore
 - [x] also py3 compatibility for `/data/srv/SubmissionInfrastructureScripts/JobAutoTuner.py` and its dependencies. Currently pulled by [vocmshtcodor](https://gitlab.cern.ch/ai/it-puppet-module-vocmshtcondor/-/blob/update_htcondor/code/manifests/structure.pp?ref_type=heads) should move to our repo #8266

## Comment (belforte, 2024-03-06T16:03:28Z)

I can now submit with CRAB to e.g. `crab-sched-901` which runs condor 10 on alma9. But
still need to work on the httpd retrieval of crab status_cache file.

## Comment (belforte, 2024-03-06T17:36:18Z)

task is running and FTS ASO works. It looks I only need redirection rules in cmsweb for access from offsite. Have opened PR https://github.com/dmwm/deployment/pull/1307

## Comment (belforte, 2024-03-11T19:11:10Z)

**Status update**
I have ported changes for alma9 to `qa` branch and modified `crab_alma9` environment to use that (still need an ad hoc env in order to override vocmshtcondor with the version which has alma9 repo, i.e. condor_update branch in there).

Now both vocms059 (in qa) and crab-sched-901/3 work using "same puppet". Jenkins test suite works on vocms059:  #8276 

I.e. we are technically ready to more more schedulers to alma9. 

Actions
 - [x] fix JobCleanup scrip - [Done](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/5fb167a5d3e90d5497ba9d34f9e4a51dd9c8b936)
- [ ] fix WmaUploader for alma9 in qa #8265 
- [ ] fix Prometheus for alma9 #8282 
- [x] move one of the new alma9 schedd's to gobal pool (`crab-sched-901`)
- [x] test `crab-sched-901` in global pool with realistic tasks (Jenkins)
- [ ] move vocms059 to alma9 and run all jenkins tests
- [ ] align `master` to `qa` in puppet
- [ ] test moving crab-preprod-scd03 to alma9 while it has some active tasks 
- [ ] drain one production scheduler and do the same
- [ ] schedule same action for other schedds

## Comment (novicecpp, 2024-03-13T11:05:30Z)

Luckily, node_exporter is provided by MONIT for alma9.
```
[root@crab-sched-903 ~]# yum provides node_exporter
Last metadata expiration check: 1:19:27 ago on Wed 13 Mar 2024 10:37:34 AM CET.
node_exporter-1.6.1-1.al9.cern.x86_64 : Exporter for machine metrics
Repo        : monit-exporters9al-stable
Matched from:
Provide    : node_exporter = 1.6.1-1.al9.cern

node_exporter-1.7.0-1.al9.cern.x86_64 : Exporter for machine metrics
Repo        : monit-exporters9al-qa
Matched from:
Provide    : node_exporter = 1.7.0-1.al9.cern

node_exporter-1.7.0-1.al9.cern.x86_64 : Exporter for machine metrics
Repo        : monit-exporters9al-stable
Matched from:
Provide    : node_exporter = 1.7.0-1.al9.cern
```

## Comment (belforte, 2024-03-14T15:01:33Z)

**new problem**
- [x] when a job is resubmitted RetryJob (called by PostJob) fails
```
Thu, 14 Mar 2024 14:45:51 CET(+0100):INFO:PostJob Executing condor_q -l 129.0 > ./finished_jobs/job.52.1
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob History file ./finished_jobs/job.52.1 created
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob ====== Starting to parse job ad file ./finished_jobs/job.52.1.
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob        -----> Attempt # 0 of 1 -----
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob        -----> Succeeded to parse job ad file -----
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob ====== Finished to parse job ad.
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob ====== Starting to analyze job exit status.
Thu, 14 Mar 2024 14:45:53 CET(+0100):INFO:PostJob        -----> RetryJob log start -----
Thu, 14 Mar 2024 14:45:53 CET(+0100):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
/usr/include/c++/11/bits/basic_string.h:1059: std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::operator[](std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::size_type) [with _CharT = char; _Traits = std::char_traits<char>; _Alloc = std::allocator<char>; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::reference = char&; std::__cxx11::basic_string<_CharT, _Traits, _Alloc>::size_type = long unsigned int]: Assertion '__pos <= size()' failed.
```
I could not find a way to re-rerun PostJob for retries interactively and use `pdb`, but I found #8284 Let'see how it goes after that's fixed
Alas it did not help. Investigating
Let's move to an ad-hoc issue #8285

For the time being mitigated via https://github.com/dmwm/CRABServer/pull/8287 . Now in master.

## Comment (belforte, 2024-03-15T17:16:33Z)

When running Jenkins tests on `crab-sched-901` it ran out of memory and could not be recovered. I deleted the VM and am re-creating with 15GB of RAM

## Comment (belforte, 2024-03-15T19:45:34Z)

**small issue**
the new "unified" `qa` branch did not have the switch to pick gfal2 form epel for alma9. Some things only appears when creating a new VM !
Fixed via https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/159

## Comment (belforte, 2024-03-15T19:55:13Z)

**run Jenkins on alma9 `crab-sched-901` after rebuilding as `r2.large`**. One at at a time !
Memory usage peaked at about 4GB. Which matches with the `m2.medium` VM to roll over (effectively a 3GB machine). https://monit-grafana.cern.ch/goto/Jk5fPM1IR?orgId=11

- [x] ClientValidation https://github.com/dmwm/CRABServer/issues/8292
- [x] ClientConfigValidation  https://github.com/dmwm/CRABServer/issues/8293
- [x] StatusTracking  https://github.com/dmwm/CRABServer/issues/8294

## Comment (belforte, 2024-03-15T21:30:25Z)

**NEW PROBLEM**
`/usr/bin/time` is missing on alma9. Although `time` command works. This breaks ASO-Rucio in
https://github.com/dmwm/CRABServer/blob/f6a59639d8614fb094f3444c97325f28ef16f10b/scripts/task_process/task_proc_wrapper.sh#L19

need to get it via `yum install time`

Taken care of in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/160

## Comment (belforte, 2024-03-16T10:01:41Z)

all Jenkins tasks ran finely, including resubmission and stageout.
Publication for ASO-Rucio was not done. I will investigate, possibly an unrelated problem.
My Publisher_rucio on crab-dev-tw01 was configred for wrong DB.
I am submitting a new StatusTracking test
- [x] https://github.com/dmwm/CRABServer/issues/8295

## Comment (belforte, 2024-03-26T15:43:51Z)

test of "time to switch"
- issued ` ai-rebuild --cc7 crab-preprod-scd03.cern.ch` at 16:07
- at same time changed condor version in puppet from  `23.0.2-1.el9` to `23.0.2-1.el7`

..hm... VM is no stuck in`error` . From `openstack show server crab-preprod-scd03` I get the fault message `{'code': 500, 'created': '2024-03-26T15:07:28Z', 'message': 'libvirtError'} `

Tried to issue `ai-rebuild` again, but 
```
Couldn't rebuild node (Invalid volume: volume 'a4540dd2-033b-48d5-b98d-1e1998bfeb7b'
 status must be 'in-use'. Currently in 'reserved' status (HTTP 400) 
(Request-ID: req-65dc91ce-625a-49df-be24-07393bcab84c))

```
asked IT for help: https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3803299

## Comment (novicecpp, 2024-03-27T09:35:11Z)

> asked IT for help: https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3803299

Could you add me to watchlist? I do not have permission to see it.

## Comment (belforte, 2024-03-27T09:37:59Z)

Done. Added @mapellidario too.

## Comment (belforte, 2024-04-02T20:20:41Z)

time for an update, before I loose track of all things I have done
*non-production schedulers
  * vocms068 still CC7
  * vomcs069, crab-preprod-scd03, crab-sched-901, crab-sched-903 now Alma9

* TaskWorker in production now submits Alma9-compatible scripts. We expect new submissions to work.
* vocms059 with Alma9, passes tests, but not in production (as usual) - final
* vocms0106 with Alma6 is not in production and filled with user jobs. - final
* vocms0107 is ready with Alma6, but not enabled in production yet
   * we should submit some test tasks and then enable if vocms0106 shows no issues
* vocms0119 and vocms0120 are "Prepared" i.e. went through the [Preparation step](https://codimd.web.cern.ch/LZFd9zUfTIa9wjeYLYKhjw?view#Preparation) but still CC7
* vocms0121, 122, 137, 144, 155 are in draining

## Comment (belforte, 2024-04-04T12:26:08Z)

I think we need a table for production schedulers that we'll keep editing


|scheduler | drain | environment | [prepared](https://codimd.web.cern.ch/LZFd9zUfTIa9wjeYLYKhjw?view#Preparation) | [migrated](https://codimd.web.cern.ch/LZFd9zUfTIa9wjeYLYKhjw?view#Migration) | OS | InProduction|
|--- | --- | --- | --- | --- | --- | --- | 
| vocms0106 | done | qa | Y | Y | Alma9| Y |
| vocms0107 | done | qa | Y | Y | Alma9 | Y |
| vocms0119|  done | qa | Y | Y | Alma9 | Y |
| vocms0120 | done | qa | Y | Y | Alma9 | Y |
| vocms0121 | done | qa | Y | Y | Alma9 | Y |
| vocms0122 | done | qa | Y| Y | Alma9 | Y |
| vocms0137 | done | qa | Y | Y | Alma9 | Y |
| vocms0144 | done| qa | Y | Y | Alma9 | Y |
| vocms0155 | done| qa | Y | Y | Alma9 | Y |
| vocms0194 | done | qa | Y | Y | Alma9 | Y |
| vocms0195 | done | qa | Y | Y | Alma9 | Y |
| vocms0196 | done | qa | Y | Y | Alma9 | Y |
| vocms0197 | done | qa | Y | Y | Alma9 | Y |
| vocms0198 | done | qa | Y | Y | Alma9 | Y |
| vocms0199 | done | qa | Y | Y | Alma9 | Y |

## Comment (belforte, 2024-04-17T13:57:18Z)

All CRAB schedulers are running on Alma9 hosts now.

## Comment (amaltaro, 2024-04-17T14:18:20Z)

This is amazing! 
Stefano, did you use the same Openstack project as the current SLC7 CRAB schedds? I see you are also putting these nodes into the hostgroup [vocmsglidein/crabschedd](https://judy.cern.ch/hosts?search=hostgroup_title+%3D+%22vocmsglidein%2Fcrabschedd%22).

I am just curious, in the end I think we/WM will stick with whatever SI recommends us to use, in terms of hostgroup, puppet templates and HTCondor version.

## Comment (belforte, 2024-04-17T14:39:58Z)

yes to both. It was mostly an exercise in puppet, several things changed since CC7 times.
We kept nodes in same openstack project and hostgroup as they were before.

Do you use puppet to install the agent ? If not.. none of this matters for you !

To be on the safe side  I did the changes in qa and moved schedulers from master to qa in puppet when migrating them. We already reconciled qa and master branches but need one last touch to SI's master to put schedulers back in production. We build on top of SI htcondor puppet module and the way puppet works, by default it picks the same branch there than in our repo. SI master will be Alma9-ready in a couple of weeks (from Florian).

You can also have a new puppet environment, I started that way for my first tests so not to affect not even ITB schedulers in qa. But IMHO there is no reason to use different openstack project unless you need to mix puppet branches from different gitlab repositories, which I hope you don't.

Then there are a few things due to "moving a shedulers that has jobs and DAGs in". Depending on your eventual plan, we can go into details.

If I manged to confuse you, we can have a chat !

## Comment (amaltaro, 2024-04-17T18:22:27Z)

Thank you for this clarification, Stefano.

We do not use puppet to manage/install the agent, only to bootstrap the node and set condor up. I try to stay away of puppet templating as much as I can, but I remember back in the days that the gitlab repositories for vocms and for glideinwms were separated. I honestly have no idea how the situation is nowadays.

For now, SI provided us new nodes in qa and (I guess) under their own Openstack project. But before moving to production - and master branch - I think we will have to recreate those nodes under CMS Production project. Thanks!

## Comment (belforte, 2024-04-17T21:04:13Z)

I would imagine that whatever the arrangement is now, it can continue. 

IIUC your machines are now in hostgroup `vocms/production/sched` so manifests in there need to be made 'alma9 ready'. I see that Bockjoo is actively working on this in  https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocms  in these days.
Which makes me wonder why you asked SI, not Bockjoo, to get you new nodes.

But the "vocms" thing with its multiple OS project and 3 layers of hostgroups is too much for me to really understand.

Most likely I am simply confused.
Indeed I should wonder if it would be better to unify also CRAB and SI under the VOCMS umbrella for easier sharing of things. 
That was my dram several years ago... but people working on puppet at the time, could not manage to do it, possibly because of operators coming and going and so many things going on and.. all usual problems. And now that we diverged and learnt how to change things w/o asking our friendly VOC's...it is not clear thate the effort would be worth. oh my.. so much duplicated work :-(
