# dmwm/CRABClient issue #5337: add support for CRAB3_CACHE_FILE=/dev/null

State: closed
Opened: 2024-10-18T13:18:10Z
Closed: 2024-12-04T20:01:42Z
Labels: bug, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5337

## Opening post (belforte, 2024-10-18T13:18:10Z)

ref. https://cms-talk.web.cern.ch/t/adapting-usage-of-crab3-file-in-case-multiple-processes-trying-to-access-it/54334/4

current code does
```
DEBUG 2024-10-18 13:00:15.261 UTC: 	 Executing command: 'status'
DEBUG 2024-10-18 13:00:15.261 UTC: 	 Could not find CRAB cache file /dev/null; creating a new one.
ERROR 2024-10-18 13:00:15.302 UTC: 	 Unhandled Exception!
ERROR 2024-10-18 13:00:15.302 UTC: 	 [Errno 13] Permission denied: '/dev/null.1120937'
```

## Comment (ArturAkh, 2024-11-27T20:42:14Z)

Hi @belforte,

It seems like there is still some trouble when using `CRAB3_CACHE_FILE=/dev/null`:

```bash
[aakhmets@lxplus917 CMSSWWithCrab]$ crab resubmit -d /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/crab/crab_data_2018UL_tau_Tau_Run2018A --maxmemory 4000
Rucio client intialized for account aakhmets
Found no jobs to resubmit. Only jobs in status failed can be resubmitted. Jobs in status finished can also be resubmitted, but only if the jobids are specified and the force option is set.
[aakhmets@lxplus917 CMSSWWithCrab]$ export CRAB3_CACHE_FILE=/dev/null
[aakhmets@lxplus917 CMSSWWithCrab]$ crab resubmit -d /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/crab/crab_data_2018UL_tau_Tau_Run2018A --maxmemory 4000
Error: Please indicate the CRAB project directory with --dir=<project-directory>.
```

I think this is somewhat related to the following lines of code:

https://github.com/dmwm/CRABClient/blob/da79107c9f00eb1378c7da5ad57f46107f65c8d3/src/python/CRABClient/Commands/SubCommand.py#L666-L691

It seems like when not using the variable being set tu `/dev/null` the resubmission works as intended. Right after doing that, I end up with the error of a missing option, while I've clearly have added it in the command.

Would you please have a closer look?

## Comment (ArturAkh, 2024-11-27T20:43:25Z)

Submission and status query work fine with `CRAB3_CACHE_FILE=/dev/null`, though

## Comment (belforte, 2024-11-27T21:07:23Z)

thanks @ArturAkh for reporting. I guess I did not test all use cases :-(
Will look closer

## Comment (belforte, 2024-11-27T21:18:32Z)

I can easily reproduce, so should be able to fix.

## Comment (ArturAkh, 2024-11-27T21:27:40Z)

Thanks a lot, @belforte!

## Comment (belforte, 2024-11-27T21:37:26Z)

the problem is that `resubmit`, like other commands, most notably `recover`, internally calls other commands. In this case `status`. But current code relies on the fact that crabcache file exists and is pointing to current task, i.e. the `-d <projdir>` from CLI is not propagated. By the way this opens to an interesting race condition in case multiple clients run at same time with same $HOME, which apparently have not surfaced so far.

I could easily fix `resubmit` into working. But at this point prefer to make sure that the `projdir` is correctly propagated in all cases, including when the initial command does not have the `-d` option (e.g. for `crab report`)

@ArturAkh let me know if you want a recipe for running your own version of CRABClient with just resubmit fixed.

## Comment (ArturAkh, 2024-11-27T21:44:36Z)

Ok thanks for the clarification, @belforte!

I agree that having the project directory properly propagated would be the solution to go for.

The issue is not urgent, so there is no need to rush :) Just wanted to bring it up since I 've stumbled across that.

In any case, I'd appreciate it very much if you would provide me with a recipe to run custom crab client to try thing out :)

## Comment (belforte, 2024-11-27T21:55:49Z)

happy to do !
Instructions to run your own  Client are in https://cmscrab.docs.cern.ch/crab-components/crab-client.html#using-crabclient-directly-from-your-github-repository
All you need is to go to your cloned CRABClient repository and apply these changes:

```diff
diff --git a/src/python/CRABClient/Commands/resubmit.py b/src/python/CRABClient/Commands/resubmit.py
index 9178495..940a42e 100644
--- a/src/python/CRABClient/Commands/resubmit.py
+++ b/src/python/CRABClient/Commands/resubmit.py
@@ -31,7 +31,7 @@ class resubmit(SubCommand):
 
     def __call__(self):
 
-        statusDict = getMutedStatusInfo(self.logger)
+        statusDict = getMutedStatusInfo(logger=self.logger, projdir=self.options.projdir)
         jobList = statusDict['jobList']
 
         if self.splitting == 'Automatic' and statusDict['dbStatus'] == 'KILLED':
diff --git a/src/python/CRABClient/UserUtilities.py b/src/python/CRABClient/UserUtilities.py
index f6fd71d..47125dc 100644
--- a/src/python/CRABClient/UserUtilities.py
+++ b/src/python/CRABClient/UserUtilities.py
@@ -193,7 +193,7 @@ def setConsoleLogLevel(lvl):
         for h in logging.getLogger('CRAB3.all').handlers:
             h.setLevel(lvl)
 
-def getMutedStatusInfo(logger=None, proxy=None):
+def getMutedStatusInfo(logger=None, proxy=None, projdir=None):
     """
     Mute the status console output before calling status and change it back to normal afterwards.
     """
@@ -202,6 +202,9 @@ def getMutedStatusInfo(logger=None, proxy=None):
     if proxy:
         cmdargs.append("--proxy")
         cmdargs.append(proxy)
+    if projdir:
+        cmdargs.append("-d")
+        cmdargs.append(projdir)
     cmdobj = getattr(mod, 'status')(logger=logger, cmdargs=cmdargs)
     loglevel = getConsoleLogLevel()
     setConsoleLogLevel(LOGLEVEL_MUTE)

```

## Comment (belforte, 2024-11-27T22:30:47Z)

Interestingly `crab recover` does not suffer of this problem when checking task status.

Because it already passed `-d projdir` as arg to `status`, differencly from   https://github.com/dmwm/CRABClient/blob/9ada90b8ce350ab4bd64870692afa7f822333824/src/python/CRABClient/UserUtilities.py#L196

so:
- [x] give a better name (silenceLogging ?) to https://github.com/dmwm/CRABClient/blob/9ada90b8ce350ab4bd64870692afa7f822333824/src/python/CRABClient/Commands/recover.py#L711 and move it to ClientUtilities
- [ ] use it also inside  https://github.com/dmwm/CRABClient/blob/9ada90b8ce350ab4bd64870692afa7f822333824/src/python/CRABClient/UserUtilities.py#L196
- [x] modify `getMutedStatusInfo` as in the patch above
- [x] modify all places where   `getMutedStatusInfo` is called in the Client to pass the `projdir` arg
- [x] look for any other place where a command is called inside another one (none at first look)

not so bad !

## Comment (ArturAkh, 2024-11-28T08:06:37Z)

Thanks a lot, Stefano, sounds like a good plan :)

I'll try the instructions for a customized client out.

## Comment (belforte, 2024-12-04T19:23:36Z)

logging in CRABClient is more tricky than I thought. Mostly if I put my hands in there I could not resist making larger chances to make things clear and flush to file more frequently. I better leave it alone and just add `projdir` where needed.
