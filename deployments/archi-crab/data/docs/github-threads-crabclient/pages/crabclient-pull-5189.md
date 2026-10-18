# dmwm/CRABClient pull request #5189: add Data.rucioScope

State: closed
Opened: 2023-02-27T20:22:29Z
Closed: 2023-03-01T16:37:20Z
URL: https://github.com/dmwm/CRABClient/pull/5189

## Opening post (belforte, 2023-02-27T20:22:29Z)

if rucioScope is set in the configuration, add it to user_config dict so that TW will lookup dataset information in Rucio only

## Comment (belforte, 2023-02-27T20:23:02Z)

i have tested it locally on lxplus

## Comment (cmsdmwmbot, 2023-02-27T20:27:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 21 comments to review
 * Pycodestyle check: succeeded
   * 388 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/930/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-27T20:38:04Z)

I need to add some validation of the scope, especially submit should immediately fail if used w/o FileBased splitting

## Comment (belforte, 2023-02-27T22:37:39Z)

the only error in pylint is this one which is totally harmless, but I do not know how to fix
I need that line `# pylint: disable=bad-whitespace` to avoid useless noise from pylint when testing locally
```
    src/python/CRABClient/ClientMapping.py
        E0012, line 3: Bad option value 'bad-whitespace' 
```

## Comment (belforte, 2023-02-27T22:46:34Z)

On second thought, in line with what is done for other configuration parameters, validation and especially check of consistency among parameter values is done server side. I have added the check on splitting in TaskWorker. This PR is good as it for me. Please review.

## Comment (belforte, 2023-02-28T08:15:38Z)

@mapellidario sorry to say that once this is merged it would be good to make a new CRABClient tag, but I think full validation does not need to be repeated.

## Comment (mapellidario, 2023-02-28T08:48:24Z)

This looks good to me, despite I don't have much experience with client arguments. We could wait for wa's opinion, but it's also true that it feels pretty harmless. I am ok with you merging this by yourself!

In any case, tags are cheap! I can make a new one and add it to IB after we merge this PR. :)

## Comment (belforte, 2023-03-01T16:37:20Z)

In the end we have a solution which requires no change to CRABClient !
Let's forget about this then.
