# dmwm/CRABClient pull request #5250: crab recover - new command

State: closed
Opened: 2023-11-10T12:24:12Z
Closed: 2023-12-01T13:14:15Z
Merged: 2023-12-01T13:14:15Z
URL: https://github.com/dmwm/CRABClient/pull/5250

## Opening post (mapellidario, 2023-11-10T12:24:12Z)

### scope

First implementation of automatic submission of a recovery task, without the need for users to follow instructions at [1]

how to trigger this new functionality: from crab client, run `crab recover --task=<taskname>`.

This command **supports** the recovery task for a task that

- has jobtype analysis
- uses a splitting algorithm that is aware of lumisections (automatic, lumibased, eventawarelumibased)

This command supports, but we have **not thoroughly** tested

- recover of a task submitted with automatic splitting [**]. User are encouraged to use it, but some extra caution may be needed.

does **not** support recovery of a task

- filebased splitting: will be done at a later stage
- privatemc: makes little sense, a user can just submit a new task.

### status

- [x] needs a reivew
- [x] ~~need to suppress debug logs, which may be useful for the review~~

changes  since out chat on 2023-11-10 afternoon:

- (functional) I changed the default strategy to "notPublished"
- (functional) killed is a final state. cooloff is a transient state, held is a transient state
- (functional) improve error message when crab report outputs are empty [5]
- (functional) improved stdout log messages
- (technical) crab remake does not need to be changed. It was a merge error on my side.
    - I needed to account for this `if` not having a return [4] 
- (technical) suppress debug messages
- (technical) use exceptions, not asserts, suggested by @novicecpp 
- (technical) jobtype Recover.py load task configuration only once, not twice as copycat.py needs to do.

### details

Entrypoint: the new file `src/python/CRABClient/Commands/recover.py`. 

Since I needed to convert a manual list of actions into a crab client command, I opted for a procedural approach. I grouped the manual actions in steps, I created a function `step*` for very step. Some steps have side effects.

apart from technicalities, we should focus our attention to

- how do we decide that the original task is actually in a final state and not in a transient state? I am not sure that the current policy can identify a static automatic splitting task.

technical details that may be not trivial to grasp

- i take the task config, pset and script exe from the original sandboxes
- I override task config options via crab submit command line options, see [2]
- I use the "Recover" jobtype, which means that the command "submit.py" will call at [3]  the new file `src/python/CRABClient/JobType/Recover.py`
- `src/python/CRABClient/JobType/Recover.py` is a modification of `src/python/CRABClient/JobType/CopyOfTask.py`, which is the original copycat implementation by @novicecpp 
    - Since I do not want to get credits for something I did not do, I can remove that file from this PR before merging. It is here just because it will be easier to compare the two when reviewing
- differences between mine and Wa's implementation
    - Wa's copyoftask assumes that the task that needs to be copied is specified in the task config
    - while in this PR we want to specify the original task name in the command line. 
    - Wa did not need to change the lumimask
    - Wa did not need to care about publishing the output in the same DBS dataset as the original task

---

[**]

when we recover a task that has been submitted with automatic splitting we can have

- some jobs are still in a transient state. crab recover will kill the task, but will not submit the recovery task. The user will need to run crab recover again
- all jobs finished and some failed. crab recover will kill the task (disabling resubmission in the future), will check all job user status, will proceed with crab submit
- all the jobs that have been submitted already are in a final state, but not all jobs have been submitted yet. crab recover will kill the task, will check that all jobs in the schedd are in a final state, then will proceed with crab submit
    - danger: since crab recover does not wait, there is a small possibility that some new jobs are submitted between the execution of crab kill and crab report.
    - however, TW should kill all those jobs soon enough not to have them create any new output file. I am confident that this will not cause any problem

[1] https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#Recovery_task
[2] https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#Passing_CRAB_configuration_param
[3] https://github.com/dmwm/CRABClient/blob/0edda22ce9af3ff76a41bc25fecb269762f54a6f/src/python/CRABClient/Commands/submit.py#L107

[4] https://github.com/dmwm/CRABClient/blob/a18cbd0856b48ad4d2db728e613efd9ac9edc0f4/src/python/CRABClient/Commands/remake.py#L23

[5] 

- `231110_180452:dmapelli_crab_test_20231110_190450` : original failing task. 3/5 jobs published
- recovered by `231110_185245:dmapelli_crab_20231110_195244` (crab report created `notPublished.json`). 2/2 jobs published
- recovered again by `231110_190318:dmapelli_crab_20231110_200317`. bug, should not have been submitted. 1/2 jobs published
- recovered again by `231110_194043:dmapelli_crab_20231110_204042`. bug, should not have been submitted. 2/2 jobs published
- bug fixed, but now crab recover fails with a cryptic message that I am not really sure how to improve. I will need to sleep on this.

<details><summary>231110_180452:dmapelli_crab_test_20231110_190450 , on prod</summary>

```plaintext
> crab recover --task=231110_180452:dmapelli_crab_test_20231110_190450 --proxy=$X509_USER_PROXY
[...]
DM DEBUG - report, retval: {'numFilesProcessed': 1, 'numEventsRead': 1800, 'numEventsWritten': {'EDM': 1800, 'TFile': 0, 'FAKE': 0}, 'inputDatasetLumis': {'1': [[1, 49], [51, 67], [69, 129], [131, 235], [237, 238], [240, 255], [257, 301], [303, 415], [417, 516], [518, 526], [528, 555], [557, 1173], [1175, 1209], [1211, 1252], [1254, 1436], [1438, 1451], [1453, 1583], [1585, 1605], [1607, 1947], [1949, 1992], [1994, 2603], [2605, 3142], [3144, 3334]]}, 'inputDatasetDuplicateLumis': {}, 'lumisToProcess': {'1': [[419, 419], [592, 592], [652, 652], [1261, 1261], [1849, 1849], [1858, 1858], [2083, 2083], [2465, 2465], [2702, 2702], [2748, 2748]]}, 'processedLumis': {'1': [[419, 419], [592, 592], [652, 652], [1261, 1261], [2702, 2702], [2748, 2748]]}, 'outputDatasetsLumis': {'/GenericTTbar/dmapelli-crab_test_20231110_190450-bb695911428445ed11a1006c9940df69/USER': {'1': [[419, 419], [592, 592], [652, 652], [1261, 1261], [1849, 1849], [1858, 1858], [2083, 2083], [2465, 2465], [2702, 2702], [2748, 2748]]}}, 'outputDatasetsNumEvents': {'/GenericTTbar/dmapelli-crab_test_20231110_190450-bb695911428445ed11a1006c9940df69/USER': 3000}, 'outputFilesDuplicateLumis': {}, 'notProcessedLumis': {}, 'commandStatus': 'SUCCESS'}
DM DEBUG - report, after, self.configuration: None
DM DEBUG - recovery task will process lumis contained in file crab_test_20231110_190450/results/notPublishedLumis.json
Command recover failed
```

</details>

## Comment (cmsdmwmbot, 2023-11-10T12:28:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 47 warnings and errors that must be fixed
   * 14 warnings
   * 493 comments to review
 * Pycodestyle check: succeeded
   * 917 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/988/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T13:37:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 492 comments to review
 * Pycodestyle check: succeeded
   * 918 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/989/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T13:39:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 492 comments to review
 * Pycodestyle check: succeeded
   * 918 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/990/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T18:42:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 819 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/991/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T18:49:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 819 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/992/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T18:59:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 819 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/993/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T19:15:27Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 819 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/994/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-10T20:12:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 820 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/995/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-17T16:26:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 820 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/999/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-20T15:23:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 12 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 820 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1000/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-20T16:12:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 449 comments to review
 * Pycodestyle check: succeeded
   * 823 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1001/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T14:07:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 45 warnings and errors that must be fixed
   * 13 warnings
   * 450 comments to review
 * Pycodestyle check: succeeded
   * 828 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1002/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T15:01:58Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 50 warnings and errors that must be fixed
   * 13 warnings
   * 451 comments to review
 * Pycodestyle check: succeeded
   * 824 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1003/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T15:17:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 46 warnings and errors that must be fixed
   * 13 warnings
   * 452 comments to review
 * Pycodestyle check: succeeded
   * 843 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1004/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T15:19:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 46 warnings and errors that must be fixed
   * 13 warnings
   * 452 comments to review
 * Pycodestyle check: succeeded
   * 843 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1005/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T15:21:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 46 warnings and errors that must be fixed
   * 13 warnings
   * 452 comments to review
 * Pycodestyle check: succeeded
   * 843 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1006/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-21T16:13:35Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 47 warnings and errors that must be fixed
   * 13 warnings
   * 455 comments to review
 * Pycodestyle check: succeeded
   * 843 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1007/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-11-21T16:15:08Z)

@novicecpp, I implemented your suggestions, added a couple of checks, improved a bit the messages to stdout. All changes are in the commits with today's date, should be quick to review. thanks again! :)

If you like it, I think this is ready to merge, I have no other changes in this scope. I will open new PRs with the next changes

## Comment (mapellidario, 2023-11-24T10:44:48Z)

After a chat with Stefano yesterday, i decided to change a couple of things in this PR:

- [x] If a task can not be recovered, we should not raise an exception, but we should return a exitcode 0 with "commandStatus" : FAILED.
    - this is required to be consistent with other crab commands
    - exitcode different from zero is only for bugs that should be acted upon
    - if the crab client decides that something should not be done, then it returns zero, with a commandStatus that is different from SUCCESS
- [x] in order to be consistent with other crab client commands, crab recover should work also if the user already has a project directory / work area. this would also avoid adding extra logic in the testing infrastructure, that is already equipped to pass to every command a project directory

## Comment (cmsdmwmbot, 2023-11-24T13:20:34Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 46 warnings and errors that must be fixed
   * 13 warnings
   * 466 comments to review
 * Pycodestyle check: succeeded
   * 850 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1016/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-11-28T14:44:04Z)

@belforte I have a question. Do you remember why we validate the config twice in `SubCommand.__init__()` [1]?

[1] https://github.com/dmwm/CRABClient/blob/54a66e6aa147d19748c1f5fb23e22baba6e06db1/src/python/CRABClient/Commands/SubCommand.py#L391-L392

## Comment (belforte, 2023-11-28T18:53:39Z)

I think I simply did a mistake in https://github.com/dmwm/CRABClient/commit/fdf647763298e1d190ab3751ed05399aca13d054 
since calling validate multiple times is "idempotent", we never noticed.
Thanks for spotting this.

## Comment (cmsdmwmbot, 2023-11-30T15:36:36Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 428 comments to review
 * Pycodestyle check: succeeded
   * 963 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1036/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-30T15:44:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 428 comments to review
 * Pycodestyle check: succeeded
   * 963 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1037/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-30T15:46:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 428 comments to review
 * Pycodestyle check: succeeded
   * 963 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1038/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-30T15:49:45Z)

**ALL Commands** !! Wow. Looks very smart, but I have a couple questions:
1. if user specifies a task name (like in remake) there should be an instance too (OK default to prod)
2. there should be some warning/notification to users that a new proj directory is being createdf
3. since it nows applies to all commands, the variable should not be called `cmptask` (which is quite  cryptic anyhow)

## Comment (mapellidario, 2023-11-30T16:19:38Z)

> if user specifies a task name (like in remake) there should be an instance too (OK default to prod)

This is already taken care of at [1]. We always set "requiresRest" when we set "requiresDirOption" [2]

> there should be some warning/notification to users that a new proj directory is being createdf

I relied only on the output of  `crab remake` which is not suppressed, but ok I added a logger.info

> since it nows applies to all commands, the variable should not be called cmptask (which is quite cryptic anyhow)

I did not change that, it has always been called that way. I think "complete" does not mean "task that recover should complete", but "full taskname, for example `231127_113158:dmapelli_crab_recover_20231127_123157` and not only `recover_20231127_123157`". If you have a better name for such a variable I am all ears.

[1] https://github.com/dmwm/CRABClient/blob/5b4dfb633cd41233233c920e2ae8cab16b46c6c2/src/python/CRABClient/CRABOptParser.py#L101

[2] https://github.com/dmwm/CRABClient/blob/5b4dfb633cd41233233c920e2ae8cab16b46c6c2/src/python/CRABClient/ClientMapping.py#L134

## Comment (cmsdmwmbot, 2023-11-30T16:28:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 44 warnings and errors that must be fixed
   * 13 warnings
   * 431 comments to review
 * Pycodestyle check: succeeded
   * 979 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1039/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-30T22:08:56Z)

Oh man !! I had just removed `--instance` from the autocompletion for all commands since they were only accepting `-d` ! That was supposedly a harmless cleanup.

This adding `--task` to all commands is a largish change for being hidden inside "add a new command".
But I am leaning to accept it. Although I am not sure that we want to encourage people to use it.

last commit is good, thanks

## Comment (belforte, 2023-11-30T22:13:10Z)

you can merge and than make a new issue/PR to add `instance` back in  https://github.com/dmwm/CRABClient/blob/master/etc/crab-bash-completion.sh .  Too bad that you did not pay attention to https://github.com/dmwm/CRABClient/pull/5259 or https://github.com/dmwm/CRABClient/issues/5255

I did not "advertise" more since I did not know that you were planning to do this.

## Comment (mapellidario, 2023-12-01T12:31:51Z)

sure, i will take care of adding `--instance` back to bash completions.

moreover, maybe it would be better to make a separate PR for adding `--task` to every command? I can do it , no problem

## Comment (belforte, 2023-12-01T12:33:55Z)

if you alreay put the code in for the `--task`, I think it is not worth to take it out and add it in a separe PR. But if you kow how to do it with 2 oneliners in git.. feel free

## Comment (mapellidario, 2023-12-01T13:14:01Z)

Created a separate PR for the use of --task in every command, rebased this PR onto it. merging myself since already approved

## Comment (cmsdmwmbot, 2023-12-01T13:15:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1042/artifact/artifacts/PullRequestReport.html
