# dmwm/CRABServer issue #8025: Jenkins fails with CMSSW_10 and 9 (at least)

State: closed
Opened: 2023-11-28T11:01:47Z
Closed: 2023-11-29T16:25:31Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8025

## Opening post (belforte, 2023-11-28T11:01:47Z)

crab submit fails with what looks like use of wrong python3

```

10:43:26 Traceback (most recent call last):
10:43:26   File "/data/CRABTesting/CRABClient/bin/crab.py", line 17, in <module>
10:43:26     from ServerUtilities import FEEDBACKMAIL
10:43:26   File "/data/CRABTesting/CRABClient/src/python/ServerUtilities.py", line 31, in <module>
10:43:26     from past.builtins import basestring
10:43:26 ModuleNotFoundError: No module named 'past'
10:43:26 
```

## Comment (belforte, 2023-11-28T14:18:57Z)

interestingly the error is different for CMSSW_9, while it works finely if I try crab submit on lxplus8 or lxplus7

```
10:48:53 Traceback (most recent call last):
10:48:53   File "/data/CRABTesting/CRABClient/bin/crab.py", line 17, in <module>
10:48:53     from ServerUtilities import FEEDBACKMAIL
10:48:53   File "/data/CRABTesting/CRABClient/src/python/ServerUtilities.py", line 230
10:48:53     truncMsg += f"\n[... message truncated to the first {msgLimit - 100} chars ...]"
10:48:53                                                                                    ^
10:48:53 SyntaxError: invalid syntax
10:48:53 
10:48:53 Starting task submission for Client Validation testing.
10:48:53 
10:48:53 
10:48:53 Submitting file: ./crabConfiguration.py
10:48:53 Traceback (most recent call last): File "/data/CRABTesting/CRABClient/bin/crab.py", line 17, in <module> from ServerUtilities import FEEDBACKMAIL File "/data/CRABTesting/CRABClient/src/python/ServerUtilities.py", line 230 truncMsg += f"\n[... message truncated to the first {msgLimit - 100} chars ...]" ^ SyntaxError: invalid syntax
```

## Comment (belforte, 2023-11-28T14:24:53Z)

Of course it is likely that both are due to obsolete container. We need to use singularity everywhere.

## Comment (belforte, 2023-11-28T19:28:14Z)

switching to singularity solves the problem with CMSSW_10.
But the error with CMSSW_9 is reproducible also locally[1] and IIUC it means that even if we import only one variable definition, the whole file is parsed by the current python interpreter, so there can't be any py3 specific code like
using the `f-string` in https://github.com/dmwm/CRABServer/blob/c8eb1c7dcb10d7fabd405fd30e8ae2e1f06835a1/src/python/ServerUtilities.py#L230

This means that a lot of changes which at least I did lately are going to make things fail when using python2 and must be corrected. A better solution is of course not to import in CRABClient the full ServerUtilities (e.g. there is no use for `truncateError` in Client. But that's quite some work.

@mapellidario @novicecpp I need your wisdom here

[1]
```
belforte@lxplus746/TC3> echo $CMSSW_BASE
/afs/cern.ch/work/b/belforte/CMSSW/SL7/CMSSW_9_4_13
belforte@lxplus746/TC3> which crab
~/WORK/CRAB3/CRABClient/bin/crab
belforte@lxplus746/TC3> crab submit 
Traceback (most recent call last):
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/bin/crab.py", line 17, in <module>
    from ServerUtilities import FEEDBACKMAIL
  File "/afs/cern.ch/user/b/belforte/WORK/CRAB3/CRABClient/src/python/ServerUtilities.py", line 230
    truncMsg += f"\n[... message truncated to the first {msgLimit - 100} chars ...]"
                                                                                   ^
SyntaxError: invalid syntax
belforte@lxplus746/TC3> 

```

## Comment (belforte, 2023-11-28T19:31:47Z)

I do not understand how Jenkins could work for CMSSW_7... 
If I try locally inside `cmssw-el6` singularity I get same error as with CMSSW_9 (syntax error), which makes a lot of sense.

But the Jenkins log has these odd lines
```
10:50:48 using CMSSW_7 on SL6. Setup/cvmfs/cms.cern.ch/slc6_amd64_gcc900/external/curl/7.59.0
10:50:49 Cloning into 'CRABClient'...
10:50:54 cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54 cp: cannot create regular file `CRABClient/src/python/': No such file or directory
10:50:54 cp: cannot stat `/build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/src/python/CRABClient/WMCoreConfiguration.py': No such file or directory
10:50:54 setupCRABClient.sh: line 67: /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/etc/crab-bash-completion.sh: No such file or directory
10:51:02 CRAB client v3.231010
10:51:02 
```
not in particular that it points to the current crab client version (with an older ServerUtilities).
pff....

## Comment (belforte, 2023-11-29T16:08:29Z)

Let's separate:

* Jenkins problems with 10 and 9 are solved by using Singularity for SCRAM_ARCH=*7
  * https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ExecuteTests/jobConfigHistory/showDiffFiles?timestamp1=2023-10-20_15-36-17&timestamp2=2023-11-29_17-00-57
 
* Code used in Client must "compile" with python2, even if it will never be executed
   * Server side: just `ServerUtilities` : #8028
   * Client Side : https://github.com/dmwm/CRABClient/issues/5261

## Comment (belforte, 2023-11-29T16:25:31Z)

So this is solved. There is something strange with Jenkins for SL6... let's track separately : #8029
