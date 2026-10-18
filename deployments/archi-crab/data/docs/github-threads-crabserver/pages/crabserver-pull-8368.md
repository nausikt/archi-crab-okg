# dmwm/CRABServer pull request #8368: Publisher support for PyPI image

State: closed
Opened: 2024-04-30T00:40:01Z
Closed: 2024-05-08T09:56:30Z
Merged: 2024-05-08T09:56:30Z
URL: https://github.com/dmwm/CRABServer/pull/8368

## Opening post (novicecpp, 2024-04-30T00:40:01Z)

Please see detail changes in https://github.com/dmwm/CRABServer/issues/7560#issuecomment-2083944687.

CI pipeline is not ready yet but manual deploy with this change is working fine for `Publisher_schedd`.

@belforte, @mapellidario, either one of you approves is enough for me. No need to read line by line, just give me the pointer where you have a question and I will explain/fix it.

## Comment (cmsdmwmbot, 2024-04-30T00:42:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1964/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-04-30T22:12:45Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1965/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-07T09:08:54Z)

wow, lot's of things to read in here. One question, you are changing PublisherFiles location, does it need a corresponding change in the publisher config  (i.e. puppet) ?

## Comment (novicecpp, 2024-05-07T09:15:59Z)

Yes https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/43ba14e4b1a9923e027ec8f23e3531af3991c96d

After this merge, I will test in preprod and re-deploy Publisher to **ALL**  environment.

## Comment (belforte, 2024-05-07T09:41:22Z)

I am bit worried about the need to syncronize puppet change with container change everywhere at same time, IIUC. I always struggle with that.

As to the actual body of this, sorry I did not look yet, was  a bit scare by so maby changed files. I may have some time this afternoon. Tuesday morning is bad for me.

## Comment (novicecpp, 2024-05-07T10:05:23Z)

> I am bit worried about the need to syncronize puppet change with container change everywhere at same time, IIUC. I always struggle with that.

IIUC, WMCore Configuration does not have a live configuration update, so updating the puppet will not affect the running process immediately (unless it restarts itself, which is pretty rare).

> As to the actual body of this, sorry I did not look yet, was a bit scare by so maby changed files. I may have some time this afternoon. Tuesday morning is bad for me.

No problem. I can wait.
You can skip reviewing this PR if you would like. Dario already approves, and a change that affects production is what I explained above.

## Comment (cmsdmwmbot, 2024-05-07T10:17:38Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1971/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-05-07T11:02:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1972/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-07T13:36:34Z)

>      IIUC, WMCore Configuration does not have a live configuration update, so updating the puppet will not affect the running process immediately (unless it restarts itself, which is pretty rare).

True.  But Publisher calls executes TaskPublish.py via
`python3 <path>/TaskPublish.py --conf .... --taskname ....`
and it uses ` config.General.taskFilesDir` to know where to pick the JSON input file for every task.

If we move files to a different direcotry `/data/srv/Publisher/PublisherFiles` instead of `/data/srv/Publisher_Files` that and possibly other things will break if the directory content is not ported over. 

I think that we should stop the container and start with a modified runContainer which mounts the old directory in the new place or something like that.

I am starting to worry that this is not fully under control yet.

## Comment (novicecpp, 2024-05-07T13:37:33Z)

:scream:

## Comment (belforte, 2024-05-07T13:55:46Z)

code aside, isn't the true that we simply want to do `mv Publisher_Files Publisher/PublisherFiles` ?
Maybe as simple as 
Stop containers, mv  directories in /data/container, run puppet, cross fingers, restart containers ?

## Comment (novicecpp, 2024-05-07T14:05:31Z)

No no.

In the `master` branch,  we do `-v /data/container/Publisher_schedd/PublisherFiles:/data/srv/Publisher_files` (Reminder, `-v` or "bind mount" format is `-v <host_path>:<container_path>`).
This PR, I do `-v /data/container/Publisher_schedd/PublisherFiles:/data/srv/Publisher/PublisherFiles`.

No need to move data in the host space, only stop the Publisher before applying the Puppet.

## Comment (belforte, 2024-05-07T14:10:14Z)

Beg to disagree.
I think it will be more clear and easier to support if directory structure in the host matches what's used in the container, and have a single mount point for `-v /data/container/Publisher_rucio:/data/srv/Publisher`. Once Publishers are stopped, there's no cost in one `mv`
But of course we can get there in steps :-)

## Comment (belforte, 2024-05-07T14:40:27Z)

overall I have no problems with this, other than the concern about the transition from old to new configuration.

## Comment (novicecpp, 2024-05-07T15:52:21Z)

Ah...I understand you now. 
We cannot mount to `/data/srv/Publisher` directly because it contains `manage.sh/start.sh/stop.sh/etc` scripts. 
I incline to your idea, but we need to rewire the path inside the container a bit (from `/data/srv/Publisher/logs` to something like `/data/srv/Publisher/hostdisk/logs`.

Let me close this and open another issue/pr for it.

Thanks for comments Stefano, especially on how Publisher work!.

## Comment (belforte, 2024-05-07T17:29:50Z)

Thanks for pointing out how I forgot that /data/srv/Publisher must be a real directory inside the container !

## Comment (novicecpp, 2024-05-08T10:06:12Z)

FYI, [I have forced Puppet to pull the runContainer.sh version before this PR](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/4492461407a92097a8da335b1bccbab602998d56) to prevent breaking Monit scripts.

I will crosscheck and apply this PR to Puppet next week.

## Comment (belforte, 2024-05-08T10:10:30Z)

I fully trust you
