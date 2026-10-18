# dmwm/CRABClient pull request #5377: put scriptExe in /debug folder. FIx #5376

State: closed
Opened: 2025-03-03T17:41:33Z
Closed: 2025-03-04T14:42:21Z
Merged: 2025-03-04T14:42:21Z
URL: https://github.com/dmwm/CRABClient/pull/5377

## Opening post (belforte, 2025-03-03T17:41:33Z)

(no text)

## Comment (cmsdmwmbot, 2025-03-03T17:45:26Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1102/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-03-04T10:55:52Z)

For example, in [Recover.py](https://github.com/dmwm/CRABClient/blob/bf347bd46487754cc4388af7a8c77a835496df44/src/python/CRABClient/JobType/Recover.py#L158) script, addMonFiles() function is called without addFiles() being called first. Your fix works for Analysis.py script as addFiles() is called first there. Please make sure that Recover.py doesn't give a problem...otherwise LGTM.

## Comment (belforte, 2025-03-04T10:56:34Z)

hmm.. :thinking: 
Thanks for pointing out, I better review. Since I did not test, my bad.

## Comment (cmsdmwmbot, 2025-03-04T11:36:29Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 2 warnings and errors that must be fixed
   * 29 comments to review
 * Pycodestyle check: succeeded
   * 21 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1103/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-04T11:36:30Z)

Indeed I had initially made the change in the wrong line ! :sob: That's fixed in last commit.
Now I will review what happens in recover.py
Thanks a lot Vijay !

## Comment (belforte, 2025-03-04T11:44:00Z)

usage in `Recover.py` is OK, it is a clone of what done in `analysis.py` in order to do a new submission
https://github.com/dmwm/CRABClient/blob/bf347bd46487754cc4388af7a8c77a835496df44/src/python/CRABClient/JobType/Recover.py#L153-L165

The thing is that user sandbox is not modified in the `crab recover` process, so it is simply downloaded and uploaded again as a way to refresh expiration in S3. While the debug tarball needs to be modified because the CRAB config.py file was changed inside `recover.py`

Side note: ideally we should not have  two files with almost same name in the repository (`recover` and `Recover`). Oh well...

## Comment (belforte, 2025-03-04T14:45:22Z)

now that it is merged, I can run CV test using client from GH head
- [x] preprod TW https://github.com/dmwm/CRABServer/issues/8964
- [x] prod TW https://github.com/dmwm/CRABServer/issues/8965 - landed on canary tw02, same release as preprod :-(
- [x] https://github.com/dmwm/CRABServer/issues/8966 - landed on canary tw02 as well :-(

preprod TW is OK. I could not force to run on current prod, but we are about to deploy new tag there, so let's call this good enough.
