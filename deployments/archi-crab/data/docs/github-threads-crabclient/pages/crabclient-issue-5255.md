# dmwm/CRABClient issue #5255: cleanup useless options from crab-bash-completion.sh

State: closed
Opened: 2023-11-27T16:02:05Z
Closed: 2023-11-27T20:41:12Z
Labels: Done
URL: https://github.com/dmwm/CRABClient/issues/5255

## Opening post (belforte, 2023-11-27T16:02:05Z)

most commands take crab instance from the working directory, but autocompletion still suggests that it can be used as option, e.g.
```
 crab kill --help
Usage: crab.py kill [options] [args]

     Command to kill submitted tasks. The user must give the crab project
directory for the task he/she wants to kill.

Options:
  -h, --help            show this help message and exit
  --killwarning=KILLWARNING
                        A warning message to be appended to the warnings list
                        shown by "crab status"
  --proxy=PROXY         Use the given proxy. Skip Grid proxy creation and
                        myproxy delegation.
  -d PROJDIR, --dir=PROJDIR
                        Path to the CRAB project directory for which the crab
                        command should be executed.
  --instance=INSTANCE   Running instance of CRAB service. Valid values are
                        dict_keys(['prod', 'preprod', 'auth', 'test1',
                        'test2', 'test3', 'test4', 'test5', 'test6', 'test11',
                        'test12', 'stefanovm', 'stefanovm2', 'other']).

```
