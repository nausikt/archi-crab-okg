# dmwm/CRABServer pull request #8526: Publisher rucio to check block completion 8491

State: closed
Opened: 2024-06-26T10:35:34Z
Closed: 2024-06-26T17:01:53Z
Merged: 2024-06-26T17:01:53Z
URL: https://github.com/dmwm/CRABServer/pull/8526

## Opening post (belforte, 2024-06-26T10:35:34Z)

initial implementation.
* If a Rucio group scope was used, code here uses the destination LFN to figure it out. After #8525 we will pick scope directly from CRAB DataBase.
* I have also introduced the `config.RUCIO` section in the configuration to make it easy to instantiate the Rucio client. I will add it to the PublisherConfig template too: https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/215

## Comment (cmsdmwmbot, 2024-06-26T10:40:58Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2029/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2024-06-26T10:55:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2030/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-26T12:55:29Z)

interesting comment about testing automatic splitting. Of coure I need to test this RutioUtils with TW, which I have not done yet, confident that my change was backward compatible ( :crossed_fingers: ), but I  am curious what I am missing about autosplit !

## Comment (belforte, 2024-06-26T12:55:41Z)

thanks for reading !!

## Comment (novicecpp, 2024-06-26T13:02:32Z)

> but I am curious what I am missing about autosplit !

Sorry, not autosplit but PreDag (which is used by autosplit). 
Just a reminder that we do talk to rucio in PreDag. I modified RucioUitls long time ago, and it broke without knowing until user reported it.

## Comment (belforte, 2024-06-26T13:15:01Z)

Ah.. now I remember. when we run TW code in the scheduler <strike>we do not have the config. from puppet. Must be sure that we carry all the info in the tarball ! Thanks for pointing out.</strike>
I stand corrected. PreDag builds the config on the fly since in the scheduler we need to use user's proxy as credential.
Again.. lot's of history, there is no technical need for accessing Rucio in there, it is only used for preparing the PFN for fall-back direct stageout, which was already done in the TW. The PFN could be passed.

 Let me add to the issue and check before merging

## Comment (belforte, 2024-06-26T13:16:13Z)

> Sorry, not autosplit but PreDag (which is used by autosplit).

PreDag is used only by autosplit, and in a way it is its engine. You were correct.

## Comment (belforte, 2024-06-26T15:55:46Z)

testing in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/7641939

## Comment (belforte, 2024-06-26T16:50:05Z)

this PR is backward compatible !
