# dmwm/CRABServer pull request #7620: Refactor tape recall

State: closed
Opened: 2023-04-27T23:25:54Z
Closed: 2023-05-03T12:09:02Z
Merged: 2023-05-03T12:09:02Z
URL: https://github.com/dmwm/CRABServer/pull/7620

## Opening post (belforte, 2023-04-27T23:25:54Z)

this PR does 2 main things:
1. when a task in status TAPERECALL is killed, it goes in KILLRECALL
2. introduces a new recurring action TapeRecallManager which will replace current TapeRecallStatus and handle both TAPERECALL and KILLRECALL states

improvements:
- when it kills tasks in TAPERECALL it also removes the Rucio recall rule
- when a rule completes and task is released for submission, it extends rule lifetime for another 30 days
- less code, get rid of useless instantiation of a new MasterWorker in TapeRecallStatus
- paves the way to further code cleanup and unification with other TW places

This is not fully tested yet, but ready for a first review.

**IMPORTANT NOTE**
when we will want to test and deploy, we must change also REST or tasks will never go into KILLRECALL

## Comment (cmsdmwmbot, 2023-04-27T23:31:52Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 11 warnings
   * 90 comments to review
 * Pycodestyle check: succeeded
   * 388 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1505/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-04-28T12:43:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 11 warnings
   * 90 comments to review
 * Pycodestyle check: succeeded
   * 388 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1506/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-28T12:50:41Z)

I tested this on `test2` and it was all OK . But just one dataset.

## Comment (mapellidario, 2023-04-28T17:04:42Z)

>  get rid of useless instantiation of a new MasterWorker wet TapeRecallStatus

wow, thank you! :)

## Comment (belforte, 2023-04-28T17:14:16Z)

More tests. Everything fine in latest version.

## Comment (belforte, 2023-04-28T17:14:41Z)

please test this

## Comment (belforte, 2023-04-28T17:25:35Z)

Ready for @novicecpp to review. Code works, but I will  still be happy to get guidance on how better to structure.

## Comment (cmsdmwmbot, 2023-05-02T08:27:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 12 warnings
   * 90 comments to review
 * Pycodestyle check: succeeded
   * 388 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1511/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-05-02T15:59:35Z)

Thanks @novicecpp , great review.
You have two questions
>     Do you have a doc explaining how and why states are changed (or a state machine diagram)? I want to understand why we need KILLFAILED but not KILLRECALLFAILED.

 We have [this](https://twiki.cern.ch/twiki/bin/view/CMSPublic/CMSCrabTaskStates) which is alas obsolete already since it does not have TAPERECALL. It was done with a too-much-human-intensive tool, we shoudl redo in a simpler form which has a chance of being ketp current. Anyhow the thing is that KILLFAILED means "could not talk to condor scheduler to kill dagman there", but for a task in TAPERECALL there is no action, only change status from TAPERECALL to KILLED. If that were to fail, we could not set to KILLRECALLFAILED either. 
 As a second order correction, we could use KILLRECALLFAILED to indicate that we failed to remove the Rucio rule, I had not thought about that. But am not sure that we care to know and investigate those (the only use of KILLFAILED is that user may tell  us so we check what went wrong inside TW) instead of simply forget and let rule expire.
 So all in all I'd keep things as they are, with the action item to create a new stage diagram picture. 
 A better diagram is not easy. There is an original sin here. The people who initially designed things did not think in terms of FSM. So the task status field does nor specify the status, e.g. for a task in QUEUED it only means that TW is working on it, but it could be doing submission, resubmission, kill, or progress after dry run. :sob: 

>    getRESTParams() code itself is fine. But the end goal should be to make the config object ready to fetch its attribute. Checking or manipulating configuration should be done before passing it to the class.

I surely agree. But lack the imagination to figure out what exactly could be done to make this happen. Something like "first time we read config file we should create `restHost` and `dbInstance` so that they are accessed au-pair with all other params ?"

Your in-line comments are very good and true, give me some time to address them all. Thanks

## Comment (belforte, 2023-05-02T16:21:55Z)

I tried one online tool and created the picture below. Doing that I realized that the FSM diagram in the twiki is fully obsoleted. Since I was pissed off with that "it does not only matter which status you are in, but also how you got there", I had them switch to use "status + command" as "actual status". I.e. a task can be in "NEW with Command = SUBMIT" or in "NEW with Command = KILL"

So this picture is likely not correct either (it should be carefully compared with the code), and lacks info on what caused the state transitions. It i is very difficult to get rid of original sins.
![TaskFSM](https://user-images.githubusercontent.com/1837785/235808696-b27ddb7a-3a21-4654-ab09-c47d4797cd48.png)

## Comment (belforte, 2023-05-02T21:49:35Z)

I need to make a list of action items here:
- [x] fix https://github.com/dmwm/CRABServer/pull/7620#discussion_r1182258009 (correct use of `elif` )
- [x] fix https://github.com/dmwm/CRABServer/pull/7620#discussion_r1182259853 (introduce RULE_LIFETIME in ServerUtilities and use also in DBSDataDiscovery)
- [x] fix https://github.com/dmwm/CRABServer/pull/7620#discussion_r1182261164  (remove useless `if` )
- [x] make sure that MAX_DAYS_FOR_RECALL is never larger than RULE_LIFETIME https://github.com/dmwm/CRABServer/pull/7620#discussion_r1182292925 .
   * idea: in DBSDataDiscover/requestTapeRecall set the initiall lifetime for the rule at MAX_DAYS_FOR_RECALL + 7days (7 days is some comfortable margin in case TW or TapeRecallManager is not working for a few days so that we do not loose track of pending requests). Keep RULE_LIFETIME as the value which is set when recall is complete and we set task to NEW. Maye call it 'INPUT_DATA_LOCKING_LIFETIME' ? and reuse in future general "input locking" ? Or use directly TASK_LIFETIME and do w/o a RULE_LIFETIME ?
- [x]  explain in comments why it is ok that MAX_DAYS_FOR_RECALL is different (shorter) than RULE_LIFETIME https://github.com/dmwm/CRABServer/pull/7620#discussion_r1182295772
- [x] map server instance to restHost+dbInstance at time of config. file read and deprecate getRESTParams() . Moved to https://github.com/dmwm/CRABServer/issues/7624
- [x] review Task FSM diagram, document it, fix TASKDBSTATUSES* in ServerUtilities.py and setup a zoom meeting to review this. Moved to #7625

## Comment (cmsdmwmbot, 2023-05-02T23:49:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 28 warnings and errors that must be fixed
   * 19 warnings
   * 245 comments to review
 * Pycodestyle check: succeeded
   * 607 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1512/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-05-03T05:29:44Z)

Thanks for answering the questions. It is clear to me now.

## Comment (novicecpp, 2023-05-03T05:29:54Z)

> [ ] map server instance to restHost+dbInstance at time of config. file read and deprecate getRESTParams()

We should open a separate issue for this. The refactoring stuff needs some time to think about how to do it properly. My rough idea is the same as you said in https://github.com/dmwm/CRABServer/pull/7620#issuecomment-1531726093 .

> [ ] review Task FSM diagram, document it

My suggestion is to create diagrams as code via PlantUML https://plantuml.com/state-diagram .
It is a nice tool to generate diagram images for you. We can commit PlantUML code in git, and easy to edit later.
There is https://github.com/mikitex70/plantuml-markdown which supports generating images on the fly in `mkdocs`, but I never try it. Initially, we can render locally and commit both image and code. 
Diagram images from https://github.com/dmwm/CRABServer/issues/7463 are generated by PlantUML in my local machine (not the kube one, I draw it in draw.io).
I would be happy to help work on this.

## Comment (belforte, 2023-05-03T12:05:57Z)

@novicecpp I think I fixed the issues which you raised in comments withing the code and moved last two boxes to separate issues.
Let me know if you have further comments or requests.

## Comment (belforte, 2023-05-03T12:08:37Z)

sorry, I requested a new review by mistake.
