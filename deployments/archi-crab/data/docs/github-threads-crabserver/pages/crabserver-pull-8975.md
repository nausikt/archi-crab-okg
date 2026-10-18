# dmwm/CRABServer pull request #8975: Enable new code in cache status

State: closed
Opened: 2025-03-10T21:00:19Z
Closed: 2025-03-12T21:09:58Z
Labels: Status: On Hold, PR: do not merge
URL: https://github.com/dmwm/CRABServer/pull/8975

## Opening post (belforte, 2025-03-10T21:00:19Z)

this enables "new" code in cache-status.py which aimed to be simply a reformatting for "readibility". This step should have been done about 3 years ago, but somehow fell into a crack.
I would like to have this consolidated before progressing with reporting DAG status to DB. Since new code is easier to deal with.
But since cache_status is critical, we need to check very well.

Initial test is in https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10996720 - OK
Adding Status Tracking https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/10996905 - OK

## Comment (cmsdmwmbot, 2025-03-10T21:02:52Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 8 comments to review
 * Pycodestyle check: succeeded
   * 32 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2395/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-11T10:13:25Z)

thanks @aspiringmind-code for quick review.
I am waiting to merge though as I am not sure if we want to change master branch with this now. Let's talk about it.

## Comment (belforte, 2025-03-12T13:22:33Z)

I decided for a new branch: https://github.com/dmwm/CRABServer/tree/addInfoToTasks-03-25

## Comment (belforte, 2025-03-12T17:28:49Z)

I believe I have  a bug :-(
it keeps saying in the log
```
DEBUG:root:cache file found, opening
DEBUG:root:no usable cache file found, creating
```
investigating

## Comment (belforte, 2025-03-12T19:19:35Z)

@aspiringmind-code it appears that nor me nor you noticed that
```python
getattr(aDict, key, None)
```
does not work, always returns `None`. The correct way for a python dictionary is
```python
aDict.get(key)
```
which already returns `None` if the key is missing (not missing key exception). I guess at the time I wrote that I was in python2 world and confused about those thing. Code sort of works the way it is now, but there is no check-pointing, it parses the full log every time. Which may explain why in some limited testing it appeared to be fine. With large tasks the condor log is a very large file O(100MB) and we had been having problems before the check-pointing was introduced.

## Comment (belforte, 2025-03-12T21:09:58Z)

closing. Work moved to addInfoToTasks-03-25 branch

## Comment (aspiringmind-code, 2025-03-13T09:34:48Z)

Very good catch indeed. getattr() works for objects with attributes and not dictionaries key-value pairs.

## Comment (belforte, 2025-03-13T09:46:27Z)

yeah.. it took me a few years to get that, and I am not sure it is firm in my brain even now :sob:
