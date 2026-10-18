# dmwm/CRABClient pull request #5315: completions - generate_completions script works in py3

State: closed
Opened: 2024-05-14T14:23:40Z
Closed: 2024-05-23T09:24:28Z
Merged: 2024-05-23T09:24:28Z
Labels: Done
URL: https://github.com/dmwm/CRABClient/pull/5315

## Opening post (mapellidario, 2024-05-14T14:23:40Z)

fixes #5314 

### status

tested on my laptop, but i have a small question before merging

### solution

This PR serves multiple purposes:

- make bash autocompletion respect the order at which we provide the commands. see the use of `-o nosort` in `complete -F _UseCrab -o filenames -o nosort crab`
- do not edit the `etc/crab-bashpcimpletion.sh` directly, generate it programmatically from `scripts/generate-completions.py`
  - make `generate-completions.py` work with python3
    - use `importlib` instead of  `imp`
  - make `generate-completions.py` generate the completion in our desired ordering, see the use of the `weights` variable.

open questions:

- [ ] I did not replicate to the variable `weights` the exact sorting that we have now yet. 
  - take a look at `etc/crab-bash-completion.sh` line 26. the order here is what bash shows when you press `crab <tab><tab>` (the order of line 32 will be the same as line 26)
  - what is the exact order that we want here?

### comment 

I decided to revamp the `generate_completion.py` script because I did not want to think about adding manually all the new commands introduced with `crab recover` :)

## Comment (cmsdmwmbot, 2024-05-14T14:25:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 22 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1057/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-05-14T16:11:00Z)

thanks Dario. I am not able to review this. I never knew that `generate_completion.py` existed and have no idea how and when to use it. Can you simply describe how things will work ?
Do we need to run it by hand every time we add or remove a command and pipe output to etc/crab-bash-completion.sh ?
Do you intend to have GH do this at any PR or tag ?

## Comment (belforte, 2024-05-14T16:11:27Z)

And for sure I do not understand the code inside those scripts !

## Comment (mapellidario, 2024-05-15T11:16:04Z)

I added a commit with and improved comment that i hope is clear enough.

So, at the moment I think we can use it instead of manually editing the file, which means run this script "only" when we add a crab client command or change an option in an existing command. 

In the future we can integrate this as part of the crab client build process, so that the completions are generated for every new deployment. I do not think the effort is worth at the moment.

## Comment (cmsdmwmbot, 2024-05-15T11:17:41Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 8 warnings and errors that must be fixed
   * 23 comments to review
 * Pycodestyle check: succeeded
   * 20 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1058/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-05-17T13:40:32Z)

I addressed the some comments from pylint (the ones that i could quickly get rid of without a proper and useless refactoring). If everything goes well, I will merge this PR

## Comment (cmsdmwmbot, 2024-05-17T13:40:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 20 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1059/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2024-05-23T09:24:15Z)

jenkins looks good to me, i will merge
