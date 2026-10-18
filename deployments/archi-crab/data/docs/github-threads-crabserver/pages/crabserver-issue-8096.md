# dmwm/CRABServer issue #8096: restrict access to our vms - force 2FA for schedds and TW's

State: closed
Opened: 2023-12-12T17:12:04Z
Closed: 2024-02-15T14:30:03Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8096

## Opening post (mapellidario, 2023-12-12T17:12:04Z)

We would like to restrict the access to TW VM's and schedd machines, forcing two factor authentication.

We have multiple options:

- 1) make VM's  available only via aiadm
- 2) enable 2fa on the hosts themselves [1]

---

[1] https://config.docs.cern.ch/access/multifactor.html
~~https://indico.cern.ch/event/1267808/contributions/5324574/attachments/2616286/4522008/From%20IT%20with%20Love.pdf slide 4, `include multifactor`. We may ask nikos, spyros or other friends from cern it how to do it :)~~

## Comment (mapellidario, 2024-01-31T17:24:52Z)

@belforte and @novicecpp I am experimentig with two factor authentication on crab-dev-tw02, I followed instructions at [1].

Can you confirm that:

- from lxplus, you need to insert the second factor, and that you can login into crab-dev-tw02
- from aiadmin, you do not need to insert the second factor to login into crab-dev-tw02
- that this is the desired behaviour

?

thanks! :)

[1] https://config.docs.cern.ch/access/multifactor.html#trusting-aiadm

## Comment (belforte, 2024-01-31T17:43:39Z)

Yes to all. Thanks a lot !

## Comment (novicecpp, 2024-02-01T14:47:17Z)

Same to me. Very nice. Thanks.

Could you apply to tw03 too? I want test ansible with multiple node. Single node is working fine.

## Comment (mapellidario, 2024-02-01T16:37:42Z)

Good! thanks for confirming. I will apply to all dev and preprod machines (waiting for about 2h for puppet to run on all machines)

- [x] `crabdev_taskworker`: `crab-dev-tw*`
- [x] `crabdev_schedd`: vocms068 vocms069, crab-preprod-scd03
- [x] `qa` : `vocms059`, `crab-preprod-*`

If we like it, I will apply the changes also to prod machines on monday

## Comment (novicecpp, 2024-02-02T06:40:28Z)

Running Ansible with multiple machines works. Thanks.
However, you need to establish a socket to aiadm (`ControlMaster=auto`) and provide 2nd factor before running it. Otherwise, Ansible will pass the 2nd factor to only one node, and the other node's connection will fail.

## Comment (belforte, 2024-02-02T10:08:40Z)

Please, update Ansible instructions in https://github.com/dmwm/CRABServer/tree/master/scripts/Utils/crab-shutdown
(the only place where we have them :-( )
Better yet, a page in https://cmscrab.docs.cern.ch/technical/crab-schedd/how-tos.html on "how to execute a command on all schedds"

## Comment (belforte, 2024-02-02T11:11:15Z)

**OUCH** 
Jenkins can not log on TW VM's anymore in order to deploy new images.

We can of course login ourselves and do it by hand. Yet it is not as convenient, also Jenkins has the nice feature of seding a msg and recording log.

Ideas ?

## Comment (novicecpp, 2024-02-02T12:03:29Z)

Like `$_aiadm_ips` in https://config.docs.cern.ch/access/multifactor.html#trusting-aiadm but we need to ask Shahzad what IP (or hostgroup) of the Jenkins instance.

## Comment (mapellidario, 2024-02-07T14:39:23Z)

## Problem

If I adapt the suggestion at [1] and create a list of ips with values both from the `aiadm` and the `vocmssdt` hostgroup [2], then SSH fails [3] complaining that a line sshd_config is too long [4] (openssh version `7.4p1`).

## Possible solutions

1. Move our machines to alma9, maybe the more recent version of openssh (`8.7p1`) has a higher limit of characters per line in `sshd_config`
    1. I can not find a "line %d too long" in https://github.com/openssh/openssh-portable/blob/master/readconf.c as in this commit https://github.com/openssh/openssh-portable/commit/61b8ef6a66efaec07e023342cb94a10bdc2254dc , so maybe recent versions of openssh do not have any limit. I could not find a definitive answer though
2. `multifactor` puppet module writes multiple lines `Match User "root" Address "137.138.53.187,...` if the list of ips is too long.
    - we would need to open a GH here: https://gitlab.cern.ch/ai/it-puppet-module-multifactor/-/issues/new
4. Only add a couple of machines from `vocmssdt` to the list of trusted IPS (hoping that the IPs do not change over time)
5. Stop using Jenkins to deploy our services until we migrate our machines to alma9

What do you suggest?

---

[1] https://config.docs.cern.ch/access/multifactor.html#trusting-aiadm

[2]

```ruby
  $_aiadm_ips_hash = cernlib::hostgroups2ips('aiadm', true, ['global'], false)
  $_aiadm_ips = $_aiadm_ips_hash['ipv4'] + $_aiadm_ips_hash['ipv6']
  # Test for sanity.
  unless $_aiadm_ips.length() >= 2 {
    fail('Something wrong querying aiadm nodes')
  }

  $_vocmssdt_ips_hash = cernlib::hostgroups2ips('vocmssdt', true, ['global'], false)
  $_vocmssdt_ips = $_vocmssdt_ips_hash['ipv4'] + $_vocmssdt_ips_hash['ipv6']
  # Test for sanity.
  unless $_vocmssdt_ips.length() >= 2 {
    fail('Something wrong querying vocmssdt nodes')
  }

  $_trusted_ips = $_vocmssdt_ips + $_aiadm_ips

  class{'multifactor::pam_2fa':
    trusted_ips => $_trusted_ips,
  }
```

[3]

```plaintext
Feb 07 12:10:24 crab-dev-tw04.cern.ch systemd[1]: Starting OpenSSH server daemon...
Feb 07 12:10:24 crab-dev-tw04.cern.ch sshd[27620]: /etc/ssh/sshd_config line 150 too long
Feb 07 12:10:24 crab-dev-tw04.cern.ch systemd[1]: sshd.service: main process exited, code=exited, status=255/n/a
Feb 07 12:10:24 crab-dev-tw04.cern.ch systemd[1]: Failed to start OpenSSH server daemon.
Feb 07 12:10:24 crab-dev-tw04.cern.ch systemd[1]: Unit sshd.service entered failed state.
Feb 07 12:10:24 crab-dev-tw04.cern.ch systemd[1]: sshd.service failed
```

[4] ok, the list of IPv4 and IPv6 addressed is 4500 characters long, which is more than 4096 bytes menitoned somewhere online https://stackoverflow.com/a/45501322

## Comment (belforte, 2024-02-07T15:01:04Z)

can you create an alma9 VM, gave it a quick test and then we go for 4) ? it seems the least effort

## Comment (mapellidario, 2024-02-09T18:02:46Z)

Restricting the whitelist to cmsjenkinsNN.cern.ch machines in `vocmssdt/jenkins` hostgroup should be enough to run our jenkins job and does not break ssh daemon config. 

I deployed it to dev machines, the jenkins job does what it is supposed to, but then failes with a weird and likely transient java error. [1]

[1] https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_Deploy_TW/547/console

## Comment (belforte, 2024-02-09T19:48:04Z)

very strange. error is not transient though. https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_Deploy_TW/548/console

## Comment (belforte, 2024-02-09T20:06:27Z)

I added a couple lines to the bash script to make sure that it completes OK and it looks like it does
and the log file is there. It is really archiving of logFile.txt in the PostBuild which fails.

```
21:01:49 + ssh -o StrictHostKeyChecking=no crab3@crab-dev-tw02.cern.ch 'docker ps'
21:01:50 + echo '$ERRR is false'
21:01:50 $ERRR is false
21:01:50 + false
21:01:50 + echo 'ALL OK'
21:01:50 ALL OK
21:01:50 + ls /var/lib/jenkins/workspace/CRABServer_Deploy_TW
21:01:50 isServiceRunning.log
21:01:50 logFile.txt
21:01:50 Archiving artifacts
21:01:50 ERROR: Step ‘Archive the artifacts’ aborted due to exception: 
```
I am out of ideas

## Comment (belforte, 2024-02-09T20:24:07Z)

I tried crab-dev-tw01 and got
```
 crab3@crab-dev-tw01.cern.ch: Permission denied (gssapi-with-mic,keyboard-interactive).
```
also after I ran puppet on the machine just in case it was needed to refresh some "who can get here w/o 2FA"

I am confused

## Comment (mapellidario, 2024-02-12T18:03:09Z)

that's because `crab-dev-tw01` is in `qa` environment, I have not ported the fix for 2fa for jenkins to qa yet. I wanted to give it a try on dev machines first. but ok, I will apply the fix to qa as well

```plaintext
[root@crab-dev-tw01 ~]# puppet agent -tv
Info: Certificate revocation is disabled, skipping CRL download
Info: Using environment 'qa'
[...]
```

## Comment (mapellidario, 2024-02-15T14:30:03Z)

Deploy from jenkins to crab-dev-tw01 worked [1]. Everything should work on prod, preprod and dev machines now, I am closing this issue. please open a new one if you find any problem.

---

[1]

https://cmssdt.cern.ch/dmwm-jenkins/job/CRABServer_Deploy_TW/562/
