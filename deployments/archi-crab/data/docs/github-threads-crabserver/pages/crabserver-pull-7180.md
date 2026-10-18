# dmwm/CRABServer pull request #7180: Regexps - scramarch: replace 'slc[0-9]{1}' with [a-z]+[0-9]{1,2}

State: closed
Opened: 2022-03-24T14:28:32Z
Closed: 2022-03-24T14:36:31Z
Merged: 2022-03-24T14:36:31Z
URL: https://github.com/dmwm/CRABServer/pull/7180

## Opening post (mapellidario, 2022-03-24T14:28:32Z)

#### status

tested on 4 tasks, ready to merge

#### descrption

Changes the regex for validating the scram architecture. The REST interface that we have in production now allows only `slc*`, but we want to support also `cs8_*` or `alma8_*`.

Reference: https://cms-talk.web.cern.ch/t/crab-submission-for-cs8-alma8-cmssw-release/8566/7

## Comment (cmsdmwmbot, 2022-03-24T14:31:12Z)

Jenkins results:
 * Python2 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1190/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2022-03-24T14:32:45Z)

After a message in a private chat, I assume that @belforte wants me to merge this myself. I am doing it now!

## Comment (amaltaro, 2022-03-24T14:39:14Z)

Hmm, we might use it in WMCore as well :-D
