# dmwm/CRABClient issue #5295: improve help for crab recover

State: closed
Opened: 2024-03-06T09:14:47Z
Closed: 2025-06-24T09:04:51Z
Labels: enhancement, Support, Documentation, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5295

## Opening post (belforte, 2024-03-06T09:14:47Z)

current text is below. I see a few things to improve
- [x] I have no clue what `strategy` means. I  doubt users will know. Please clarify
- [x] ~~it should be possible to make help print the list in a given order (the order they are declared ? So that the list starts with what users are more likely to use, then rarely used things like `--proxy` and at the bottom things for CRAB operators~~ this is not possible, command specific options are listed first, followed by what's common to all commands. Let's fall back to
   - [x] reorder the common options and improve description of `--instance`
- [x] there's too many spaces in top description in `task     did not process `

```text
belforte@lxplus812/TC3> crab recover --help
Usage: crab.py recover [options] [args]

     given a taskname, create a new task that process only what the original
task     did not process yet

Options:
  -h, --help            show this help message and exit
  --strategy=STRATEGY   When using lumibased splitting, sets crab report
                        --recovery=$option
  --destinstance=DESTINSTANCE
                        (Experimental) The CRABServer instance where you want
                        to submit the recovery task to. Should be used by crab
                        operators only
  --forcekill           Allows to kill failing task submitted by another user.
                        Effective only for crab operators
  --proxy=PROXY         Use the given proxy. Skip Grid proxy creation and
                        myproxy delegation.
  -d PROJDIR, --dir=PROJDIR
                        Path to the CRAB project directory for which the crab
                        command should be executed.
  --task=CMPTASK        The complete task name. Can be taken from 'crab
                        status' output, or from dashboard.
  --instance=INSTANCE   Running instance of CRAB service. Valid values are
                        dict_keys(['prod', 'preprod', 'auth', 'test1',
                        'test2', 'test3', 'test4', 'test5', 'test6', 'test11',
                        'test12', 'stefanovm', 'stefanovm2', 'other']).
belforte@lxplus812/TC3> 
```
