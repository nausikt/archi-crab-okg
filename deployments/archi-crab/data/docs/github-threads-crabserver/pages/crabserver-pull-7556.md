# dmwm/CRABServer pull request #7556: add RucioDataDiscovery fix #7538

State: closed
Opened: 2023-02-27T20:51:49Z
Closed: 2023-03-10T14:08:18Z
Merged: 2023-03-10T14:08:18Z
URL: https://github.com/dmwm/CRABServer/pull/7556

## Opening post (belforte, 2023-02-27T20:51:49Z)

RucioDataDiscovery will be put in the list of Actions for the submitted task by Actions/Handler.py whenever the new parameter `rucioscope` is set to a string in `tm_user_config` dictionary.
RucioDataDiscover will raise a fatal exception if the task was submitted with a splitting algorithm different from `FileBased` but should otherwise support all features DBSDataDiscovery: blacklists, whitelists, taperecall.

## Comment (cmsdmwmbot, 2023-02-27T22:22:42Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 17 warnings
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 587 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1444/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-02-28T12:08:56Z)

@belforte Could you write down limitation of the new RucioDataDiscovery compared to DBS one, in PR description?
Also, which commit hash you copy `DBSDataDiscovery.py` from?

## Comment (belforte, 2023-02-28T16:11:59Z)

@novicecpp : I have filled the PR description with the information about what RucioDataDiscovery will do. But I do not understand the question about `DBSDataDiscovery.py`, I have not changed it. Do you mean that I do not have fully uptodate code in RucioDataDiscovery for the parts which are common ? That's alas possible, and that's why we should move the common parts to methods which are called in both places. For the moment having something that works at least with common use case (input is fully on disk) should be good enough. Indeed this requires the dataset name to obey DBS syntax. But that's only a matter of client/rest interface. If a rucio container name in any-string format were put in `tm_inputdataset`, I expect RucioDataDiscovery to work.

## Comment (belforte, 2023-02-28T16:16:11Z)

I would leave "allow any string as Rucio container" to a new issue. With this at least we have something to test and if some user wants to try processing a bunch of file they can easily create a good-looking-DBS-style name.
Of course there can be bugs :-)

## Comment (novicecpp, 2023-02-28T16:47:48Z)

> Do you mean that I do not have fully uptodate code in RucioDataDiscovery for the parts which are common?

Yes. I want it for diff and see what did you change in the new `RucioDataDiscovery.py`.

## Comment (belforte, 2023-02-28T17:00:21Z)

that's beyond my git skills. I have rebased my branch to squash commit history
But from a plain `diff -y` I see that the support for `inputblocks` is missing :-(
I guess I started from `master` as of a few days ago

## Comment (belforte, 2023-02-28T17:03:30Z)

git network graph suggests that I started from master as of Feb 20th.

## Comment (novicecpp, 2023-02-28T17:04:31Z)

Thanks. Let me have a look.

## Comment (belforte, 2023-02-28T17:09:34Z)

we should really demote this to "stepping stone simply to check that nothing is broken and allow progress". The more I think about it, the  more I think I need to put in the original idea of supporting a generic `user.joe:thisismygreatcontaineroftheday-jun-3-2025` thing. OK. you win.

## Comment (belforte, 2023-02-28T21:08:37Z)

thanks for thorough review, I will go through things tomorrow.

At the moment I will address your two questions

> Why secondary dataset is not support?

because it relies on lumi info to know which files from secondary dataset to couple with files in primary dataset for processing and without DBS there is no such info.
AFAIU secondary input in CMSSW works like this:
hey cmsRun, please process this file, one event at a time of course, and for each event look in those other files for the same event, and combine the data in memory so I can process child and parent at same time accessing objects in either.
In there event means the triplet (run/lumi/event).
I am not sure how CMSSW implements it, but I think it reads the list or (run/lumi/event) in all files indicated as secondary, and uses it to pick correct data. So the list of those file can'be "a 500TB, 100K file dataset"

>    I do not understand what you wrote in [RucioDataDiscovery.py#L367-L372](https://github.com/dmwm/CRABServer/blob/98b3af84f8fd3dfdcb64c86de625b9379b8bb893/src/python/TaskWorker/Actions/RucioDataDiscovery.py#L367-L372). Could you explain?

I am not sure I fully understand it either ! Let's talk about it in zoom.. It was mostly a rant/note to myself. And all in al any comment of the kind "this could be done better" w/o details is of little value. That should indeed be clarified or removed.

## Comment (belforte, 2023-02-28T21:18:17Z)

> +1 for use scope:container. We can simply select RucioDataDiscovery in handler by check the first char if it is / (assume proper format for RucioDataDiscovery is already check in REST).

sure, the Handler and following part does not worry me. I simply went for what was easier to change in client/REST, and of course did not require a new DB column, even if I start to think that this may be better. I implemented before a full design was laid down and reviewed, simple as that.

## Comment (belforte, 2023-02-28T21:21:41Z)

yeah.. this is a bit like current RUCIO_Transfers.py. A demonstration that it can work, and a way to get experience with it, but needs some polishing before being called production.

## Comment (cmsdmwmbot, 2023-03-01T10:35:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 17 warnings
   * 161 comments to review
 * Pycodestyle check: succeeded
   * 587 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1445/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-01T18:08:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 16 warnings
   * 130 comments to review
 * Pycodestyle check: succeeded
   * 566 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1446/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-03-01T18:09:06Z)

@novicecpp I still need to fix REST and Handler part for new design.

## Comment (cmsdmwmbot, 2023-03-01T18:10:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 16 warnings
   * 130 comments to review
 * Pycodestyle check: succeeded
   * 566 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1447/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-01T19:59:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 16 warnings
   * 127 comments to review
 * Pycodestyle check: succeeded
   * 564 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1448/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-01T20:26:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 12 warnings
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 566 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1449/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-01T20:28:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 12 warnings
   * 75 comments to review
 * Pycodestyle check: succeeded
   * 566 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1450/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-01T20:30:33Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 10 warnings
   * 65 comments to review
 * Pycodestyle check: succeeded
   * 543 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1451/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-03-06T16:49:45Z)

I think this is ready for final review.
I will rebase and squash committs but content should not change. Anyhow we will test more. I only verified new functionalities. Hopefully nothing got broken.

## Comment (belforte, 2023-03-10T12:35:57Z)

squashed commits

## Comment (cmsdmwmbot, 2023-03-10T12:36:23Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 13 warnings
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 537 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1464/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-10T12:37:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 13 warnings
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 537 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1465/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-03-10T12:50:39Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 7 warnings and errors that must be fixed
   * 13 warnings
   * 117 comments to review
 * Pycodestyle check: succeeded
   * 531 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1466/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-03-10T14:08:12Z)

OK in my tests. If problems will appear in further validation, let's open ad-hoc issues
