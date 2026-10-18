# dmwm/CRABServer pull request #8901: retrieve clusterid column from DB. Fix #8900

State: closed
Opened: 2025-01-29T21:34:30Z
Closed: 2025-01-30T15:55:06Z
Merged: 2025-01-30T15:55:06Z
URL: https://github.com/dmwm/CRABServer/pull/8901

## Opening post (belforte, 2025-01-29T21:34:30Z)

(no text)

## Comment (belforte, 2025-01-29T21:35:18Z)

already tested in crab-dev-tw01

## Comment (cmsdmwmbot, 2025-01-29T21:36:10Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 14 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2357/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-30T10:51:43Z)

thanks Vijay, yeah.. I have been lazy. Let me add the try...except, thanks for prodding !

## Comment (belforte, 2025-01-30T15:13:29Z)

there is a problem though. HTTP call is already retried up to 20 times with exponential backoff (20*retry# secs) inside the crabserver object
https://github.com/dmwm/CRABServer/blob/8599a93ac74bdbabe5c04c90a271f38148b49b14/src/python/TaskWorker/MasterWorker.py#L216-L217
so I would not know what to do after catching an exception other than... "failing" !

And by they way, when crabserver object eventually fails, it raises a generic `Exception`, not an HTTP one.

 If I do nothing here, the DagmanKiller exits on the exception and control is passed to the Handler which  retries any action "no matter what" up to 5 times
https://github.com/dmwm/CRABServer/blob/3db5af84122652734b5cc035ba2f40f1f0e84e04/src/python/TaskWorker/Actions/Handler.py#L127 again with increasing delay,

If things still fail... user will have to issue `crab kill` again.

So I think the only "problem" is that the retry policy is not obvious nor written in any prominent place and even I forgot and had to look it up now !!!

Indeed there are places where code still looks for http exception, from old implementation of access to CRAB REST, like
https://github.com/dmwm/CRABServer/blob/8599a93ac74bdbabe5c04c90a271f38148b49b14/scripts/AdjustSites.py#L316-L324
which was coded 10y ago.

So much cleanup .....

Let me know what you think !
