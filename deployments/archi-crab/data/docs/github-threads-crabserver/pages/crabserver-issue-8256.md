# dmwm/CRABServer issue #8256: port scheduler scripts to Alma9

State: closed
Opened: 2024-02-23T09:08:47Z
Closed: 2024-03-06T22:43:05Z
Labels: Priority: High, alma9
URL: https://github.com/dmwm/CRABServer/issues/8256

## Opening post (belforte, 2024-02-23T09:08:47Z)

We need to move all schedulers to Alma9 by end of May.

all scripts which we run in the schedulers need to be compatible with alma9
Besides possible (hopefully none) differences due to different default python
(we use OS python3 in the schedulers) we have a few places where we
point to SL7 binaries

I start the list with things I know about by mnemory, Others may exist and need to be found and fixed

- [x] `pycurl3` from our repo https://github.com/dmwm/CRABServer/blob/3af9d658271a101db02194f48c5cecaf5fab7725/scripts/task_process/task_proc_wrapper.sh#L100
- [x] `curl` from cmssw on /cvmfs https://github.com/dmwm/CRABServer/blob/3af9d658271a101db02194f48c5cecaf5fab7725/scripts/task_process/task_proc_wrapper.sh#L101
- [x] Rucio installation from /cvmfs https://github.com/dmwm/CRABServer/blob/3af9d658271a101db02194f48c5cecaf5fab7725/scripts/task_process/task_proc_wrapper.sh#L105-L109

- [x] `dag_bootstrap_startup.sh` should stop calling `source /cvmfs/cms.cern.ch/slc7_amd64_gcc900/external/curl/7.59.0/etc/profile.d/init.sh` which breaks htcondor by pointing to sl7 gcc

## Comment (novicecpp, 2024-02-23T11:22:49Z)

I am adding the util scripts we have in puppet's [crabschedd.pp](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/manifests/crabschedd.pp) (grep for `.py`).

 * I believe those are listed in https://github.com/dmwm/CRABServer/issues/8258#issuecomment-1969450020 and are fixed now in the new [crab_alma9](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/tree/crab_alma9?ref_type=heads) branch in there @novicecpp  let me know if you find that I am still missing something.

## Comment (belforte, 2024-03-06T22:43:05Z)

closed via https://github.com/dmwm/CRABServer/pull/8270 and #8271
