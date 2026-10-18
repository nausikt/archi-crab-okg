# dmwm/CRABServer pull request #9314: enforce useGzip everywhere we instantiate DbsApi.

State: closed
Opened: 2026-05-13T22:44:51Z
Closed: 2026-06-22T09:36:03Z
Merged: 2026-06-22T09:36:03Z
URL: https://github.com/dmwm/CRABServer/pull/9314

## Opening post (nausikt, 2026-05-13T22:44:51Z)

Resolve #9313

## Comment (cmsdmwmbot, 2026-05-13T22:47:09Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 48 comments to review
 * Pycodestyle check: succeeded
   * 43 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2822/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-05-14T12:18:37Z)

thanks @nausikt for having given it a try. I will use your branch as base for some testing and a bit of "refinement": not all DBS urls's need zipping and I want to use this also in data discovery

## Comment (belforte, 2026-06-17T13:42:20Z)

I am finally moving on with testing. Had to blacklist tons of tasks in order to have # of acquired back to reasonable value and be able to stop/start Publisher w/o breaking running processes.
<img width="453" height="213" alt="image" src="https://github.com/user-attachments/assets/07f2f18e-d804-4c25-9ff1-bcecb0092cde" />

The I moved STATS.txt to old-STATS.txt and restarted Publisher form local repo with
```
diff --git a/src/python/Publisher/PublisherDbsUtils.py b/src/python/Publisher/PublisherDbsUtils.py
index e3f21324..ab9af3b4 100644
--- a/src/python/Publisher/PublisherDbsUtils.py
+++ b/src/python/Publisher/PublisherDbsUtils.py
@@ -114,7 +114,7 @@ def setupDbsAPIs(sourceURL=None, publishURL=None, DBSHost=None, logger=None):
         publish_read_url = publishURL + '/DBSReader'
         publishURL += '/DBSWriter'
     logger.info("DBS Destination API URL: %s", publishURL)
-    destApi = DbsApi(url=publishURL, debug=False)
+    destApi = DbsApi(url=publishURL, debug=False, useGzip=True)
     logger.info("DBS Destination read API URL: %s", publish_read_url)
     destReadApi = DbsApi(url=publish_read_url, debug=False)
     logger.info("DBS Migration API URL: %s", publish_migrate_url)
[crab3@crab-prod-tw01 CRABServer]$ 
```
so that the new STATS.txt logs times for block insertion with gzip enabled.

FYI @nausikt

## Comment (belforte, 2026-06-17T14:40:54Z)

Publications are being done. Hard to say if time is decreased since we always put in different things, it more like "N-days and distribution of times is clearly different". Alas I did not put timestamps in STATS.txt

## Comment (belforte, 2026-06-17T15:37:41Z)

here's times distrubutions from old-STATS.txt (697,570 entries)
<img width="569" height="416" alt="image" src="https://github.com/user-attachments/assets/37cd460c-eb98-445c-b52e-6005b1a547ca" />

## Comment (belforte, 2026-06-17T15:42:49Z)

and here's with `gzip` and so far 574 entries. To early to tell 
<img width="559" height="427" alt="image" src="https://github.com/user-attachments/assets/1d0a0260-7ced-438e-bd20-545b62aad12a" />

FWIW, here are the two distributions superimposed and zooming on the 0-30sec range
<img width="573" height="429" alt="image" src="https://github.com/user-attachments/assets/55ccdc8b-3914-4cf5-8c95-ef32a057a8e5" />

## Comment (belforte, 2026-06-18T13:45:14Z)

now with ten time more statistics (8471 entries) for new STATS.txt
left: full time range (300sec=5min is CMSWEB FE timeout) - right: zoom on 0-50 sec
blue: current code - red: with gzip
<img width="567" height="424" alt="image" src="https://github.com/user-attachments/assets/8405235c-e047-4e45-9dba-c1cdb2ad95c6" />

I conclude that everything works and improvement is clearly visible. So we can make this change persistent. 

The only other API which may benefit from `gzip` in Publisher is `destReadApi` which retrieves a list of filenames, all other calls to DBS have very little data exchange
https://github.com/dmwm/CRABServer/blob/1858c33b7adc155b77a67877b6f7a42baa1c2cd3/src/python/Publisher/TaskPublish.py#L106-L108

Now let's look at TaskWorker

## Comment (cmsdmwmbot, 2026-06-18T13:56:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 17 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2838/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-18T14:01:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2839/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-18T14:02:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2840/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-06-18T14:02:34Z)

Cool! done Stefano. Sorry for re-request review too soon.

## Comment (belforte, 2026-06-18T14:23:28Z)

let me now make sure that I understand how to enforce gzip in data discovery via WMCore DBSReader class

## Comment (belforte, 2026-06-18T17:08:26Z)

I get a server error when trying to add `useGzip` to WMCore'a DBSReader. 
Please change the title of this to "enforce useGzip in Publisher" and let's have a separate issue about TaskWorker, which honestly I do not know if it is worth pursuing since most likely problem is somewhere in DBS or WMCore :-(

## Comment (cmsdmwmbot, 2026-06-19T11:40:02Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 6 comments to review
 * Pycodestyle check: succeeded
   * 5 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2841/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-06-21T18:40:53Z)

Can't merge this PR. somehow the automatic jenkin lintings are blocking & looks pretty weird to me.
Their error warning its seems not aligned with current code base. Let me get back to investigate this on monday na.

*P.S. i already pylint pep8, ask ChatGPT but seems like Jenkins bot may have cached of old version code?*

```bash
src/python/Publisher/PublisherDbsUtils.py:22: [E261] at least two spaces before inline comment
src/python/Publisher/PublisherDbsUtils.py:26: [E302] expected 2 blank lines, found 1
src/python/Publisher/PublisherDbsUtils.py:47: [E302] expected 2 blank lines, found 1
src/python/Publisher/PublisherDbsUtils.py:319: [E133] closing bracket is missing indentation
src/python/Publisher/PublisherDbsUtils.py:392: [E133] closing bracket is missing indentation
```

## Comment (belforte, 2026-06-22T09:25:58Z)

@nausikt IIUC merging is not blocked by Jenkins, but by `Commits must have verified signatures.`
I do not know how to fix that ! And fear that my commits do not have signature either.

The fact that Jenkins marks the "default" check as failed even if all its tests succeeded has been there since ever and we never understood why. So far it was harmless... 

Maybe you can relax the rules on the repository to allow unsigned commits until we have learnt how to sign ?

## Comment (nausikt, 2026-06-22T09:35:58Z)

Ahhh i see, Thanks! the oldest commit one was left, i've re-signed now.
