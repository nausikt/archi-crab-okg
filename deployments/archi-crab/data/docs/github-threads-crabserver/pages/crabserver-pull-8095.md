# dmwm/CRABServer pull request #8095: crab shutdown - ansible playbooks for dagman hold and release

State: closed
Opened: 2023-12-12T15:16:56Z
Closed: 2023-12-12T17:13:17Z
Merged: 2023-12-12T17:13:17Z
URL: https://github.com/dmwm/CRABServer/pull/8095

## Opening post (mapellidario, 2023-12-12T15:16:56Z)

I would like to add to dmwm/CRABServer the ansible scripts that I ended up using for holding and releasing the dagmans. 

I had some problems with escaping the single and double quotes to use condor commands with `wassh`, so I quickly drafted and used a couple of ansible playbooks this I would like to share.

@belforte and @novicecpp : every suggestion is always welcome, especially deciding which directory we should use to place such files :)

## Comment (cmsdmwmbot, 2023-12-12T15:21:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1783/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-12-12T16:18:47Z)

thanks Dario. I like it. Can you help an old dummy like me with an example of how to configure my laptop so that I can ssh to a schedd from here ?
That said, I think that we should restrict access to schedd, like to the VM's where we run TW, via 2FA, i.e. only accept it via aiadm
It looks like I can do
```
 ssh -J belforte@aiadm.cern.ch belforte@vocms0144.cern.ch
```
but I do not know if Ansible can.

## Comment (mapellidario, 2023-12-12T16:29:28Z)

> Can you help an old dummy like me with an example of how to configure my laptop so that I can ssh to a schedd from here ?

sure, i will not put it here though, I will add to our usual mkdocs

> That said, I think that we should restrict access to schedd

I fully agree, I will create a GH issue

## Comment (belforte, 2023-12-12T16:34:53Z)

seems this is what I was looking for
in `~/.ssh/config` :
```
Host vocms*.cern.ch
        ProxyJump lxtunnel.cern.ch
```
or use `aiadm` in place of `lxtunnel`

## Comment (mapellidario, 2023-12-12T17:10:28Z)

I added portions of my ssh config at https://cmscrab.docs.cern.ch/operators/dev/ssh.html

## Comment (mapellidario, 2023-12-12T17:13:13Z)

and created https://github.com/dmwm/CRABServer/issues/8096. I will merge this PR, please feel free to reach out if you have some more questions or requests :)
