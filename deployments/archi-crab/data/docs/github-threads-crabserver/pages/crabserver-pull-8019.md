# dmwm/CRABServer pull request #8019: Rucio ASO: Cleanup temp area

State: closed
Opened: 2023-11-23T18:42:16Z
Closed: 2023-11-27T18:52:02Z
Merged: 2023-11-27T18:52:02Z
URL: https://github.com/dmwm/CRABServer/pull/8019

## Opening post (novicecpp, 2023-11-23T18:42:16Z)

Partial fix https://github.com/dmwm/CRABServer/issues/7423

New `Cleanup` action for cleaning up temp area (and remove temp replica from Rucio DB in the future).
Need to bookkeeping PFNs in case process terminate before run `Cleanup` action in previous run.

## Comment (cmsdmwmbot, 2023-11-23T19:13:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 123 warnings and errors that must be fixed
   * 21 warnings
   * 246 comments to review
 * Pycodestyle check: succeeded
   * 257 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1771/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-23T19:26:32Z)

Ready to review.
Sorry for force-push. Forgot to commit the main files to review :man_facepalming:

## Comment (belforte, 2023-11-23T20:20:22Z)

i use force push all of the times... did not know it was bad :-(

## Comment (novicecpp, 2023-11-23T20:38:44Z)

No no. It is ok to do especially in the PR, rebase make PR branch, keep commit clean, etc.

In this context, I want to have as little notification as possible. So I prepared everything for this PR, but I found out later that I forgot to commit some files, and it was sending many noti to your email while I fixed the mistake.

## Comment (belforte, 2023-11-23T20:51:39Z)

no worry, I am very used to deleting mails :-)

## Comment (belforte, 2023-11-24T17:50:42Z)

@novicecpp I am sorry to say that I am too tired and confused and can't really go through the details of the new code. Everything looks OK from afar, but I am not able to review line-by-line today.

OTOH, here too this is new code and it there is no danger of breaking things, so you may very well merge and we start using it and we will see how it works in practice. In time I will hopefully read it a few more times and digest it.

Generally speaking the only thing which troubles me is that to "add a rm" you had to change so many files, it makes me fear that code is not well separated into independent parts with well defined interfaces, but somehow internals in one class are connected to internals in another. Hopefully it is simply a fear and things are actually clean.

## Comment (novicecpp, 2023-11-24T18:09:46Z)

Thanks a lot Stefano. I will go through comments and fix next Monday (also multipub containers PR).

> Generally speaking the only thing which troubles me is that to "add a rm" you had to change so many files, it makes me fear that code is not well separated into independent parts with well defined interfaces, but somehow internals in one class are connected to internals in another. Hopefully it is simply a fear and things are actually clean.

Most bloat code is come from passing information from one action to another and persist information between run.
In this case I need PFNs, where it is resolved in `RegisterReplicas` class. I need to do bookkeeping across run because current run we only have current PFNs but not PFNs from previous run.

Another way to do this is query replicas from Rucio like `list-file-replicas` do. 
Why don't I do this? Not sure. Maybe I did not see clear trade-off and only think about limiting request to Rucio Server.

I agree that it has too much file changes but I do not know how to improve it yet.
I will keep it in mind.

## Comment (cmsdmwmbot, 2023-11-27T17:32:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 145 warnings and errors that must be fixed
   * 29 warnings
   * 445 comments to review
 * Pycodestyle check: succeeded
   * 1091 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1773/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-27T18:16:24Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 104 warnings and errors that must be fixed
   * 17 warnings
   * 257 comments to review
 * Pycodestyle check: succeeded
   * 283 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1774/artifact/artifacts/PullRequestReport.html
