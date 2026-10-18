# dmwm/CRABServer pull request #7547: Fix default values when TW fetch task, change default to None

State: closed
Opened: 2023-02-22T12:20:22Z
Closed: 2023-02-24T17:03:53Z
Merged: 2023-02-24T17:03:53Z
URL: https://github.com/dmwm/CRABServer/pull/7547

## Opening post (novicecpp, 2023-02-22T12:20:22Z)

I forget to put new default values in [RESTWorkerWorkflow](https://github.com/novicecpp/CRABServer/blob/9f6fd04c5061a3dce9a38718d4363be1142dfbc6/src/python/CRABInterface/RESTWorkerWorkflow.py#L157) for new `inputblocks` user config.
I think I can do it better but have no idea right now.

Also, change default from `[]` to `None`, follow practice from pylint (explanation from [stackoverflow](https://stackoverflow.com/questions/26320899/why-is-the-empty-dictionary-a-dangerous-default-value-in-python)).

## Comment (cmsdmwmbot, 2023-02-22T12:26:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 6 warnings
   * 62 comments to review
 * Pycodestyle check: succeeded
   * 136 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1439/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-22T12:31:33Z)

read out loud 10 times: never assume that you can change code at same time in 2 services

## Comment (belforte, 2023-02-23T08:56:59Z)

are you waiting for my approval ? Or... ?

general observation: all in all `['tm_user_config']` is  "optional things" and it may be good to never take it for granted that all possible prams in there are present before using them in the code. In this way it is different from other `tm_*` params which comes from DB and thus are always present.

Yeah.. one may wonder if we wouldn't be better off by saving in the DB a JSON document with all those things instead of storing as separate columns things which we never change nor query on but simply store/fetch. Well.. for next time we write a tool like CRAB from scratch.

## Comment (belforte, 2023-02-23T08:59:06Z)

I rather worry about:
* where exactly do we keep track of all keys which may be in `tm_user_config` ?

## Comment (novicecpp, 2023-02-24T10:53:12Z)

> I rather worry about:
> 
>     * where exactly do we keep track of all keys which may be in `tm_user_config` ?

As it shown in this PR, [RESTUserWorkflow](https://github.com/dmwm/CRABServer/blob/27fe22629968c70171c1a44976a6538cf702f823/src/python/CRABInterface/RESTUserWorkflow.py#L564) when we receive input from the user and [RESTWorkerWorkflow](https://github.com/dmwm/CRABServer/blob/27fe22629968c70171c1a44976a6538cf702f823/src/python/CRABInterface/RESTWorkerWorkflow.py#L157) when we use it.
You can see that it need to change both files, which I completely forgot to change it, thus this PR. 
That why I am not merge it yet because I am not satisfy with current solution, waiting for new ideas/comments. 

> general observation: all in all ['tm_user_config'] is "optional things" and it may be good to never take it for granted that all possible prams in there are present before using them in the code. In this way it is different from other tm_* params which comes from DB and thus are always present.

It fine for me if we treat all keys in `user_config` as optional and check if keys exist in TW instead.

## Comment (belforte, 2023-02-24T11:18:34Z)

Why not merge this anyhow and have a separate discussion about how to best keep track, sanitize, set defaults... whatever. ?

I do not have  a very clear understanding of this and I may have made suggestions which I now disagree with !  In a way this resembles a lot the discussion we are having in https://its.cern.ch/jira/browse/CMSKUBERNETES-220

## Comment (novicecpp, 2023-02-24T17:03:44Z)

I have open new issue here: https://github.com/dmwm/CRABServer/issues/7552
I am merging this and let's discuss there.
