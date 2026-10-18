# dmwm/CRABServer issue #8265: Cleanup old WMArchiveUploader for alma9

State: open
Opened: 2024-02-28T15:23:03Z
Labels: Status: On Hold, OPERATION, alma9
URL: https://github.com/dmwm/CRABServer/issues/8265

## Opening post (novicecpp, 2024-02-28T15:23:03Z)

Currently we install both old and new WMArchiveUploader version and only start one service at the time.

The installer of old version cause some issue with alma9:

- new git version has protection mechanism to not execute git command if owner of directory does not match. Puppet `vcsrepo` automatically add safe path to ~/.gitconfig but the path is `/data/srv/SubmissionInfrastructureScripts//WMCore`, double slash instead single slash, which is differ path for git. `vcsrepo` try to checkout to specific version and fail with `detected dubious ownership` [1], and later raise `/WMCore exists and is not the desired repository.` [2]
- `/etc/init.d` does not exist anymore (where we put old WMArchiveUploader init script). 

Plus, new scripts is now stable, it is time to clean up.

[1]
```
Notice: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/File[/data/srv/SubmissionInfrastructureScripts//WMCore]/ensure: created (corrective)
Notice: Vcsrepo[/data/srv/SubmissionInfrastructureScripts//WMCore](provider=git): Adding '/data/srv/SubmissionInfrastructureScripts//WMCore' to safe directory list
Notice: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/Vcsrepo[/data/srv/SubmissionInfrastructureScripts//WMCore]/ensure: Creating repository from latest
Error: Execution of 'git remote add origin https://github.com/dmwm/WMCore.git' returned 128: fatal: detected dubious ownership in repository at '/data/srv/SubmissionInfrastructureScripts/WMCore'
To add an exception for this directory, call:

        git config --global --add safe.directory /data/srv/SubmissionInfrastructureScripts/WMCore
```

[2]
```
Notice: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/File[/data/srv/SubmissionInfrastructureScripts
//WMCore]/owner: owner changed 'condor' to 'crabtw' (corrective)                                                                                                                              
Notice: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/File[/data/srv/SubmissionInfrastructureScripts//WMCore]/group: group changed 'condor' to 'zh' (corrective)                                                                                                                                  
Notice: Vcsrepo[/data/srv/SubmissionInfrastructureScripts//WMCore](provider=git): Adding '/data/srv/SubmissionInfrastructureScripts//WMCore' to safe directory list                           Notice: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/Vcsrepo[/data/srv/SubmissionInfrastructureScri
pts//WMCore]/ensure: Creating repository from latest                                                                                                                                          Error: Path /data/srv/SubmissionInfrastructureScripts//WMCore exists and is not the desired repository.                                                                                       
Error: /Stage[main]/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader/Hg_vocmsglidein::Crabschedd::Wmarchiveuploader::Config[/etc/wmarchive.json]/Vcsrepo[/data/srv/SubmissionInfrastructureScrip
ts//WMCore]/ensure: change from 'absent' to 'latest' failed: Path /data/srv/SubmissionInfrastructureScripts//WMCore exists and is not the desired repository.                                 
```

## Comment (novicecpp, 2024-03-14T16:14:59Z)

Scripts still running on python2, but the worst part is it use WMCore `1.3.2`, The script itself is python3 compatible (`2to3` running without error).

Need to test with py3 and the newest WMCore.

## Comment (belforte, 2024-03-14T17:45:44Z)

hmm...
I suggest that you put this aside for a moment and we review the use case.
I'd like @mapellidario to talk with WMA folks next week about it.
We do not use WMArchive. Is anybody using its archive for anything ? In the end it may not have any additional information to what we send to HDFS. The only use case I know is that P&R operators (at FNAL mostly) use it to track execution of running workflows. But for this they only care about WMA.

Dario, can you do this ?

## Comment (novicecpp, 2024-03-15T09:22:32Z)

>  I suggest that you put this aside for a moment and we review the use case.

This is what I want to hear :)

## Comment (belforte, 2024-03-15T09:26:44Z)

I think we need to move from  "it works don't fix it" to "don't need it, remove it"
Even w/o waiting for "it" to break.

## Comment (belforte, 2024-03-15T09:54:13Z)

I took the chance of a new thread in DMWM MatterMost to ping people there https://mattermost.web.cern.ch/cms-o-and-c/pl/a4c96owfwfy7zca1uznxzqbyrh

## Comment (novicecpp, 2024-03-15T11:11:06Z)

Here is dashboard from WMArchive docs we uploaded (Thanks to @amaltaro) https://monit-grafana.cern.ch/goto/vn53aZJSg?orgId=11 

I had a discussion with Alan this morning. His suggestion is to ask around to see if anyone still depends on it. Another thing to consider is if we, the CRAB team, still need some metrics from WMArchive that are not available in condor metrics. Otherwise, just deprecate it.
However, in his opinion, it should not be difficult to migrate to py3 and the most recent wmcore version because it is a standalone script that calls the wmcore library to upload data, not use it as a framework like crab rest does.

## Comment (belforte, 2024-03-15T11:33:16Z)

thanks. I surely agree with Alan that migration to py3 could be straightforward, but at the end of the day it is another service which we need to keep running 24x7 for next N years.
I like the "ask around" !! If only it were so simple as, I do not say everybody works in same aisle, but at least everybody reads same channel/mail !
We can try to give the question a little of visibility via NEWS section of O&C weekly meeting.

## Comment (belforte, 2024-03-15T11:50:43Z)

very nice dashboard by the way. I suspect that we can replicate it with data from monit_prod_condor_raw, but did not try

## Comment (belforte, 2024-03-26T15:20:21Z)

WMArchive was setup before we had HDFS, OpenSearch etc. At this point we are not sure that it is still useful for anytthing. Supporting it is an effort that we can certainly do without.
Will ask "permission to deprecate" to the community.
On Hold until then.

## Comment (belforte, 2024-04-30T09:45:03Z)

Decision to decommission WMArchive for CRAB was [announced](https://indico.cern.ch/event/1409162/contributions/5925603/attachments/2844090/4972331/CRAB%20for%20OC%20weekly%20240423.pdf) on Apr 23, 2024 weekly O&C [meeting](https://indico.cern.ch/event/1409162)

Keep it disables, wait a few months, then cleanup code

## Comment (belforte, 2024-04-30T10:00:47Z)

should close this and open one about removing WMArchive stuff.
