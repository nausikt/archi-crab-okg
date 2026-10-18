# dmwm/CRABServer issue #8263: puppet cleanup

State: closed
Opened: 2024-02-25T18:25:11Z
Closed: 2024-04-11T14:29:08Z
Labels: Status: Done, OPERATION, alma9
URL: https://github.com/dmwm/CRABServer/issues/8263

## Opening post (belforte, 2024-02-25T18:25:11Z)

some things which I found lately, up for discussion before we do

- [x] do we really need certmgr_san: "crab-dev-scd01.cern.ch, schedd/crab-dev-scd01.cern.ch" in fqdn/yaml files  ? and the corresponsding call in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/manifests/crabschedd/certificate.pp?ref_type=heads#L11-18  ? NO
- [x] related: do we need a hostcert at all ? it is renewed every year in `manifests/init.pp`. Needed for WMArchiveUploader
- [x] do we still need `umd` in https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/manifests/modules/rpms.pp?ref_type=heads#L4  NO
- [x] We need to remove all those JAT variables which we will never use anymore
- [ ] bind.pp ? What does it do ?
- [x]  `cvmfs::mount{'sft.cern.ch': }` surely we never use and anyhow cvmfs has automount now no need for `mount{'cms.cern.ch':}` either
- [x] ganglia.pp ? NO not used anymore, they removed it from SI repo as well
- [ ] blacklisting of a couple usernames in all `/data/fqdn/*yaml` files ! Remove, now nobody but "us" is allowed !
- [ ] do we use all of the stuff in `data/hostgroup` ? 
- [x]  Automatic creation of home directories (e.g. in crabschedd.pp) NOT Needed anymore

## Comment (novicecpp, 2024-02-26T11:30:34Z)

- Reply to first bullet: I believe it can be removed, but need to test. 
- ~~Second bullet: Yes. It is done behind the scene by Foreman/Puppet master.~~ See Stefano's comment below.
- 3rd bullet: I do not know. I did not have time to check when doing the refactor.

## Comment (belforte, 2024-02-26T17:14:21Z)

hostcert is taken care via `manifests/init.pp` . And that's all that we need about certificates.

## Comment (belforte, 2024-02-29T13:56:37Z)

Proposal:
  I will do clean up in the crab_alma9 branch.
  qa and master will be "cleaned" when we remove the last CC7 machine and get rid of all the `if` on OS version

How does it sound @novicecpp @mapellidario ?

## Comment (novicecpp, 2024-02-29T13:58:48Z)

Go Go :rocket:

## Comment (novicecpp, 2024-03-14T16:15:24Z)

I think I need to bring servicecert back. Otherwise, we need to re-register hostcert on VOMS and CRIC for all machines again, just for WMArchiveUploader  that we do not even know if somebody still looks at it.

@belforte as VOMS/CRIC admins, what do you think?

## Comment (belforte, 2024-03-14T17:50:15Z)

Hey ! I am unfortunately stuck with VOMS Admin, but CRIC is Panos' land !

I am not against having that certificate, if it helps. Simply could not find where it was used other than WMARchiveUploader.  Let's leave aside WMARchive for a moment.
Where do we talk to CRIC and/or VOMS ?

## Comment (novicecpp, 2024-03-15T09:33:32Z)

I mean, you have right to grant permission on both systems.

> Where do we talk to CRIC and/or VOMS ?

Not directly. But in order to access cmsweb resources,we need to register the certs to VOMS+CRIC (correct me if I am wrong). 
If we use hostcert, we need to do this procedure to all machines.
If we use servicecert, only the new hosts (crab-sched-901/903) need to register.
Either way, we need to do it, and I will ask for your help.

But let's follow up on #8265 to see whether we remove it or not.

## Comment (belforte, 2024-04-04T13:32:22Z)

Everything "doable" is done in `qa` now.
I do not have the answers to
* what is `bind.pp`
* do we need the stuff in `data/hostgroup`

## Comment (belforte, 2024-04-04T13:40:07Z)

e.g. this file defines things which we already have in the manifests
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/data/hostgroup/vocmsglidein/crabschedd.yaml?ref_type=heads

## Comment (belforte, 2024-04-11T12:34:27Z)

@mapellidario @novicecpp I think I have done all I could reasonabl do here. There is still some cleanup that can be done in `data/hostgroups` but I do not understand how it works well enough to put my hands in it now.

Do you agree with closing ?

## Comment (novicecpp, 2024-04-11T12:48:53Z)

Yes. 
I can purge `bind.pp` later after we migrate all nodes to alma9 for some time, to make sure systemd-resolved is working as expected.
It setup DNS server which for local cache (in cc6 era, maybe).

`data/hostgroups` is up to your variable overriding policy. We can talk about it later.
