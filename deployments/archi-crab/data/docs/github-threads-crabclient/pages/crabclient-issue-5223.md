# dmwm/CRABClient issue #5223: make sure crab exit with non 0 exit code in case of errr

State: closed
Opened: 2023-10-13T22:52:39Z
Closed: 2023-10-18T22:36:51Z
Labels: bug, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5223

## Opening post (belforte, 2023-10-13T22:52:39Z)

with ref to https://github.com/dmwm/CRABServer/issues/7933
THere is currently a mess in CRABClient.

Various commands return a value, even a dictionary which says `{'status' : 'FAILED'}` but this is never used, since the call is
https://github.com/dmwm/CRABClient/blob/a18cbd0856b48ad4d2db728e613efd9ac9edc0f4/bin/crab.py#L143-L146

(of course I may have misunderstood...)

and any returned value is ignored.
We should rely on raising an exception in order to report a failure which e.g. Jenkins test can use (curent CrabClientValidation tests issues all sort of commands and simply checks that exit code is non zero !)

I am afraid I need to check all commands:

- [x] checkdataset
- [x]  checkusername
- [x]  checkwrite
- [x]  createmyproxy
- [x]  getlog
- [x]  getoutput
- [x]  kill
- [x]  preparelocal
- [x]   proceed
- [x]   remake
- [x]   report
- [x]   resubmit
- [x]  status
- [x]   submit
- [x]   tasks
- [x]   uploadlog

## Comment (belforte, 2023-10-13T22:53:27Z)

I need a decent validation test in order to work with Rucio client in CRAB, so this is TOP prio

## Comment (belforte, 2023-10-13T22:58:01Z)

question : maybe commands returns a `statudict` "thinking" of use via CRAB API ? Bu why only some ?
e.g. `checkusername.py` returns the username ! but AFAICT it is never used.

YES, the value returned by each command is passed back to the caller of the CRAB API
https://github.com/dmwm/CRABClient/blob/a18cbd0856b48ad4d2db728e613efd9ac9edc0f4/src/python/CRABAPI/RawCommand.py#L13-L15

## Comment (belforte, 2023-10-16T16:22:07Z)

I came to the conclusion that when command returns e.g. {'status': 'FAILED'}, crab CLI should exit with code 1, not 0.
(e.g. checkwrite fails to write)
So that we can check this an error in our tests, at least for the simple testes which we have now where we expect success.
This implies that
 * **ALL COMMANDS MUST RETURN A DICTIONARY {'commandStatus':'SUCCESS/FAILED'}**
 * Can not use key `status` to avoid conflict with what is returned by `status` command !

This an important change, even if very little code, deserves its own Issue and PR: https://github.com/dmwm/CRABClient/issues/5224

## Comment (belforte, 2023-10-18T08:08:19Z)

last merge was only a parital fix in order to align with master

## Comment (belforte, 2023-10-18T09:56:14Z)

from latest Jenkins, these needs looking at
1.  what about this error ?
```
___
TEST_COMMAND: crab report  --outputdir=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --proxy=/tmp/x509up_u501  --dir=crab_20231017_235457  
TEST_RESULT: OK                                                                                 
TEST_MESSAGE:
Running crab status first to fetch necessary information.
Rucio client intialized for account cmsbot
Error: Cannot get all the needed information for the report. Notice, if your task has been submitted more than 30 days ago, then everything has been cleaned.
Will save lumi files into output directory /build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir
```

2. all getoutput say "no files to retrie", something wrong in the test ! So I can't check
```
___________
TEST_COMMAND: crab getoutput  --parallel=10  --wait=4  --outputpath=/build/cmsbld/jenkins/workspace/CRABServer_ClientValidation/CRABServer/test/container/testingScripts/logdir  --dump --jobids=2,3  --checksum=yes  --proxy=/tmp/x509up_u501  --dir=crab_20231017_235457  
TEST_RESULT: OK                                                                                 
TEST_MESSAGE:
Rucio client intialized for account cmsbot
Rucio client intialized for account cmsbot
No files to retrieve.
____________
```

## Comment (belforte, 2023-10-18T11:03:32Z)

also something is wrong with my recent change, this message was meant not to appear when using `crab` command !
And it does not appear for `crab checkusername` and `crab tasks` which I tested yesterday. Oh well...
```
belforte@lxplus810/bot> crab remake --task 231017_215457:cmsbot_crab_20231017_235457
Remaking crab_20231017_235457 folder.
Remaking .requestcache file.
Success: Finished remaking project directory crab_20231017_235457
ATTENTION return value for 'remake' has been changed to a dictionary
 format is {'commandStatus': 'SUCCESS' or 'FAILED',
            'workDir': name of the work directory created}
Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/dbg/bot/crab.log
belforte@lxplus810/bot> 
```

## Comment (belforte, 2023-10-18T16:04:20Z)

OK, in `remake.py` there was another level of call, I should put the message in the `__call__` method of the comand, not in a function called inside it.

## Comment (belforte, 2023-10-18T16:18:51Z)

I tried the commands in https://github.com/dmwm/CRABClient/issues/5223#issuecomment-1768098638 after remaking the task in my directory and they work now. So the error seems genuine, but maybe as simple as jobs had not completed when test ran ?

## Comment (belforte, 2023-10-18T16:34:50Z)

yeah.. when Jenkins ran status was `transferring`.
What should we do ? Ideally this ClientVaildation test should be able to be retried later, like we do for ConfigValidation and StatusTracking, but it is some work which should better be delayes until we have [new CI/CD pipeline](https://github.com/dmwm/CRABServer/issues/7958)

So for the time being I keep those above as "non error", i.e. fine to exit with exit code 0

## Comment (belforte, 2023-10-18T17:19:33Z)

in the end I have to make `crab report` exit with exit code != 0  in case of `Cannot get all the needed information for the report.`
It is the simplest and cleanest way to enforce returning a proper dictionary, one case which I missed in https://github.com/dmwm/CRABClient/pull/5225

## Comment (belforte, 2023-10-18T17:31:26Z)

Well.. as good as I can do by looking at code and running simple tests. Will see as we use more and run more Jenkins.

## Comment (belforte, 2023-10-18T22:36:51Z)

closed via https://github.com/dmwm/CRABClient/pull/5231
