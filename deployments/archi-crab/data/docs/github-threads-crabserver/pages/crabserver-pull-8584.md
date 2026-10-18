# dmwm/CRABServer pull request #8584: Allow v2 bindings 8571

State: closed
Opened: 2024-08-02T20:00:17Z
Closed: 2024-08-07T17:00:45Z
Labels: Status: On Hold, To be tested
URL: https://github.com/dmwm/CRABServer/pull/8584

## Opening post (belforte, 2024-08-02T20:00:17Z)

fix #8571

## Comment (cmsdmwmbot, 2024-08-02T20:08:18Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 37 warnings and errors that must be fixed
   * 21 warnings
   * 530 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2081/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-02T20:09:13Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 37 warnings and errors that must be fixed
   * 21 warnings
   * 530 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2082/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-03T21:36:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 38 warnings and errors that must be fixed
   * 21 warnings
   * 530 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2084/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-03T21:52:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 18 warnings
   * 525 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2085/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-08-05T08:28:59Z)

Hi Stefano, could you please rebase this pr to latest master (or maybe squash it)?
It is a bit confuse when I look at the changes that contains our previous PRs.

## Comment (cmsdmwmbot, 2024-08-05T08:35:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 18 warnings
   * 525 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2086/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-05T09:39:02Z)

may bad, I did not realize that my second commit was bringing in so much stuff.

## Comment (belforte, 2024-08-05T13:04:59Z)

Rebased.
@novicecpp the things I want your opinion most are the change to `manage.sh` and the corresponding introduction of  `useHTCbindingsV1orV2.py`

## Comment (cmsdmwmbot, 2024-08-05T13:05:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 12 warnings and errors that must be fixed
   * 18 warnings
   * 525 comments to review
 * Pycodestyle check: succeeded
   * 904 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2087/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-05T13:32:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 18 warnings
   * 525 comments to review
 * Pycodestyle check: succeeded
   * 902 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2088/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-05T14:05:24Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 warnings
   * 515 comments to review
 * Pycodestyle check: succeeded
   * 899 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2089/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2024-08-05T16:08:00Z)

Sorry, I need to go. I will review it tomorrow.

Quick comment here: Can we do simply grep like 
```bash
if grep` 'config.TaskWorker.useHtcV2 = True' $CONFIG; then
    export useHtcV2=True
fi
```
in `manage.sh`?  I want to get rid the extra `useHTCbindingsV1orV2.py` script.

Alternative and cleaner(?) solution: Late import MasterWorker.py in Main.py
https://github.com/dmwm/CRABServer/compare/master...novicecpp:CRABServer:example_1
Did you try it?

## Comment (belforte, 2024-08-05T16:25:43Z)

thank you !
I thought about the `grep` but do not like it, too fragile. The late import seems perfect instead. I will try tomorrow.

## Comment (belforte, 2024-08-05T17:54:05Z)

Actually I had thought about moving the import as well, but wanted to avoid the pylint complain and did no think of simply disabling !

## Comment (belforte, 2024-08-06T09:47:34Z)

OK. Will go for delayed import. Wait for new version before reviewing

## Comment (cmsdmwmbot, 2024-08-06T14:33:25Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 warnings
   * 513 comments to review
 * Pycodestyle check: succeeded
   * 909 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2090/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-08-06T14:36:47Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 warnings
   * 513 comments to review
 * Pycodestyle check: succeeded
   * 909 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2091/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-06T14:39:15Z)

sorry. Due to my limited GH skills I ended up squashing everything in my branch so now the functional changes are mixed in same commit with pylint fixes. I do not have the stamina  to fix all warning in so many files now, but at least there are no errors.
I still need to do a final build-and-test round
  - https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7889513
  - https://github.com/dmwm/CRABServer/issues/8587
 BOTH FAILED !!

## Comment (cmsdmwmbot, 2024-08-06T14:39:27Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 18 warnings
   * 513 comments to review
 * Pycodestyle check: succeeded
   * 909 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2092/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-08-06T15:24:56Z)

I manage to break things when merging in the changes to use the "delayed import" trick. Will fix

## Comment (belforte, 2024-08-06T20:36:51Z)

the problem is that `HTCondorLocator` is imported in the `TaskWorkerConfig.py`, therefore before the env.var. is set in `Main.py`
https://github.com/dmwm/CRABServer/blob/9be641e6de5358ab5b34a8489ebf5e11150e12d3/src/python/TaskWorker/Main.py#L78-L84
So HTCondorLocator always has v1 bindings, which means that `schedd` object in DagmanSubmitter is a v1 object to which we pass a v2 Submit object causing the failure.

A drastic solution "at the root" would be to remove this form the configuration file, we never use it to pick the function for selecting schedulers anyhow and may very well hardcode the use of `capacityMetricsChoicesHybrid`. See
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L112
and
https://github.com/dmwm/CRABServer/blob/6cacb768c2c2361497841004f14185ce0b4e2fa0/src/python/TaskWorker/Actions/DagmanSubmitter.py#L242-L246

## Comment (belforte, 2024-08-06T20:38:41Z)

I do not understand why I did not see this when testing from private branch... but that's not an useful question

## Comment (belforte, 2024-08-06T20:46:04Z)

Another (better) possibility could be to replace in the `TaskWorkerConfig.erb`
```
config.TaskWorker.useHtcV2 = <%= @tw_useHtcV2.to_s %>
```
with
```
import os
os.environ['useHtcV2'] =  "<%= @tw_useHtcV2.to_s %>"
```
and move `import HTCondorLocator` after that.
so that the `TaskWorkerConfig.py` file will look like
```python
import os
os.environ['useHtcV2'] = "True"
import HTCondorLocator
config.TaskWorker.scheddPickerFunction = HTCondorLocator.capacityMetricsChoicesHybrid
```
Also this line needs to be moved down
https://github.com/dmwm/CRABServer/blob/6cacb768c2c2361497841004f14185ce0b4e2fa0/src/python/TaskWorker/Main.py#L10

This surely is less work, and I will give it a try to confirm the bug and the solution. But I fear it will be horribly obscure, even if we plan to remove the v2 vs. v1 sometimes next year and become v2 only getting rid of all these `if`.

I am very tempted to choose the "CLEANUP" way. and get rid of the `config.TaskWorker.scheddPickerFunction`

@novicecpp I welcome your opinion, as always

## Comment (belforte, 2024-08-07T01:19:49Z)

I am testing the modified TaskWorkerConfig in
- [x] https://github.com/dmwm/CRABServer/issues/8591  (only for SST. CCV in there is broken, see comment in issue)
- [x] https://github.com/dmwm/CRABServer/issues/8592 (for CCV)

OK. It works !

## Comment (novicecpp, 2024-08-07T12:17:05Z)

I agree with solution in https://github.com/dmwm/CRABServer/pull/8584#issuecomment-2272120437.

Less work and future-proof (just yet-another-envvars). I think explicitly print the message in Main.py after config is load is enough (and of course the comments in code/config).

## Comment (belforte, 2024-08-07T13:06:52Z)

thanks @novicecpp . Let's go that way then.
I will cleanup, prepare a new tag and test it. I still do not like the obsolete code inside HTCondorLocator and the importing it in the config. We are somehow changing the configuration file semantics: from the POV of the TW code, the information will be in the `configuration` object **and** in the environment.  I'd rather have a string in the config than an import and a  pointer to a function. For my taste people tried to be too smart here.

hmm... maybe better to use puppet hiera to set a string in the configuration object
and in the TaskWorkerConfiguration code use that to set the env. var. before importing HTCondorLocator.

Eventually I would still like to go for explicitly calling one or another scheddPicker function. But at this point that's a different story.

## Comment (mapellidario, 2024-08-07T15:05:43Z)

my two cents: if you settle on an template like

```plaintext
import os
os.environ['useHtcV2'] =  "<%= @tw_useHtcV2.to_s %>"
```

you will set an environment variable also when you want to use htcondor-v1, so you should change 

```diff
- if 'useHtcV2' in os.environ:
+ if os.environ.get('useHtcV2', None) == "true"`:
```

## Comment (belforte, 2024-08-07T15:22:02Z)

thanks Dario. Yes, I am aware.  But I did not want to change again all places where I put
```

if 'useHtcV2' in os.environ:
    import htcondor2 as htcondor
    import classad2 as classad
else:
    import htcondor
    import classad
```
I was also afraid (uselessly ?) that if I start/stop/changeconfig/restart this env.var could stck around so am trying to ensure a clean start  by having in the "top place"
```
if config.TaskWorker.useHtcV2:
    os.environ['useHtcV2'] = "True"
else:
    os.environ.pop('useHtcV2', None)
```

## Comment (belforte, 2024-08-07T15:23:15Z)

I will close this PR and point to it in #8571 as a reference to be discussion and create a new PR with the new code. I need to reset my branch !
