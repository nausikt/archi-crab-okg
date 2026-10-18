# dmwm/CRABServer pull request #7634: add crab-task-state.puml

State: closed
Opened: 2023-05-12T16:15:39Z
Closed: 2023-05-25T08:31:41Z
URL: https://github.com/dmwm/CRABServer/pull/7634

## Opening post (belforte, 2023-05-12T16:15:39Z)

as per action item 4.d in [yesterday's meeting](https://docs.google.com/document/d/1HqO_mXG5rFM9BgYhkFiig1h6ltFA80GmGJatA0_5vnA/edit) I have [removed](https://github.com/dmwm/CRABServer/pull/7633) old `doc` directory content and am creating a new `doc/puml` where to store flow/state diagrams which may help to understand the code

## Comment (belforte, 2023-05-12T16:17:17Z)

@mapellidario @novicecpp see if you like this.

## Comment (cmsdmwmbot, 2023-05-12T16:23:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1519/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-05-15T07:27:54Z)

Shall we put `puml` directory to `etc` or new directory like (yet another) `docs`?
I would like to have another directory at root level for put stuff that not the code but we need to put it in this repo.

## Comment (belforte, 2023-05-15T13:18:26Z)

I like `etc/puml`

## Comment (belforte, 2023-05-25T08:31:41Z)

will make new one with `etc/puml`
