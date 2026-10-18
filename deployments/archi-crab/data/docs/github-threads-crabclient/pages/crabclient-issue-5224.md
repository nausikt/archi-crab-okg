# dmwm/CRABClient issue #5224: all commands must return a dict containing `commandStatus` key

State: closed
Opened: 2023-10-16T16:38:28Z
Closed: 2023-10-17T17:46:57Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5224

## Opening post (belforte, 2023-10-16T16:38:28Z)

This is needed so that `crab.py` can know if a command succeeded of failed and properly set the exit code.
Currently commands always exit with 0 and rely on user reading the messages to tell if things worked.
This prevents constructing a decent testing.

Progress tracker

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

## Comment (belforte, 2023-10-16T20:20:42Z)

I have a problem with `remake` which does not return a dictionary, but the name of the remade directory.
Changing this will require changin our Jenkins test (easy).  But is any user relying on it ?
https://github.com/dmwm/CRABClient/blob/a18cbd0856b48ad4d2db728e613efd9ac9edc0f4/src/python/CRABClient/Commands/remake.py#L39

I had the same problem with `checkusername` but there I **assumed** that nobody is calling that inside a script, it is strictly a diagnostic command.

## Comment (belforte, 2023-10-16T20:41:39Z)

same problem with `crab tasks` which does not return a dictionary, but a list of lists (!) e.g.
```
command returned:
[['231016_155423:belforte_crab_20231016_175412', 'SUBMITTED'],
 ['231009_204109:belforte_crab_20231009_224054', 'SUBMITTED'],
 ['231009_203927:belforte_crab_20231009_223911', 'KILLED'],
 ['231009_165015:belforte_crab_20231009_185002', 'SUBMITTED'],
 ['231009_164650:belforte_crab_20231009_184637', 'SUBMITTED'],
 ['231009_164308:belforte_crab_20231009_184252', 'SUBMITTED'],
 ['231009_160730:belforte_crab_20231009_180715', 'SUBMITTED'],
 ['231009_150007:belforte_crab_20231009_165954', 'SUBMITTED'],
 ['231009_143454:belforte_crab_20231009_163437', 'SUBMITTED'],
 ['230927_224134:belforte_crab_20230928_004125', 'SUBMITTED']]
```

I have to wonder if anybody every used this ! The REST API is already flawed since it returns a list of lists... oh well.
https://github.com/dmwm/CRABClient/blob/master/src/python/CRABClient/Commands/tasks.py

## Comment (belforte, 2023-10-16T21:35:18Z)

an "interesting" possibility is simply to warn users with code like this
```python
        import sys
        caller = sys._getframe(1)
        if not 'crab.py' in caller.f_code.co_filename:
            self.logger.warning("ATTENTION return value for tasks API has been changed to a dictionary")
        returnDict = {'commandStatus': 'SUCCESS', 'taskList': result}
        return returnDict
```

as expected there's no difference with CLI:
```
belforte@lxplus808/TC3> crab tasks --days=3

List of tasks from 2023-10-13 until 2023-10-16
Beware that STATUS here does not include information from grid jobs
================================================================================
NAME								STATUS
================================================================================
231016_155423:belforte_crab_20231016_175412
								SUBMITTED
--------------------------------------------------------------------------------


Log file is /afs/cern.ch/work/b/belforte/CRAB3/TC3/crab.log
belforte@lxplus808/TC3
```

But with my new TestAPI.py script (soon to be committed) to repo:
```
belforte@lxplus808/TC3> ~/TestAPI.py tasks --days 4
testing:  tasks

List of tasks from 2023-10-12 until 2023-10-16
Beware that STATUS here does not include information from grid jobs
================================================================================
NAME								STATUS
================================================================================
231016_155423:belforte_crab_20231016_175412
								SUBMITTED
--------------------------------------------------------------------------------


ATTENTION return value for tasks API has been changed to a dictionary
command returned:
{'commandStatus': 'SUCCESS',
 'taskList': [['231016_155423:belforte_crab_20231016_175412', 'SUBMITTED']]}
belforte@lxplus808/TC3> 
```

@novicecpp @mapellidario can you please offer advice ?

## Comment (belforte, 2023-10-16T22:02:24Z)

I have tentatively fixed `tasks.py` that way. WIll try the same for `remake` and go back to https://github.com/dmwm/CRABClient/issues/5223

Of course the Jenkins test will have to be made forward/backward compatible, at least for next N months.

## Comment (novicecpp, 2023-10-17T10:53:17Z)

I like this approach. 

I have no historical knowledge that if there is any analysis tool rely on CRABClient API. We need to announce this in cms-talk ("O&C/Computing Tools" with "announcement" tag) as soon as it in crab-dev to get feedback and see if there is anybody rely on client API.

## Comment (belforte, 2023-10-17T15:40:17Z)

From "conversations with users in cms-talk or HN before" we know that many users adopted the `multicrab` script from the twiki or wrote/adapted similar ones, in particular users like the possibility to edit the configuration object in the script to e.g. make it easy to submit those 100 tasks on 100 datasets in a few minutes.
There also users who have scripts which loops on `crab status + crab resubmit` and I expect them to use API more than CLI.

But hopefully they do not use `remake` or `tasks`. Those were the only two which did not return a dictionary.
