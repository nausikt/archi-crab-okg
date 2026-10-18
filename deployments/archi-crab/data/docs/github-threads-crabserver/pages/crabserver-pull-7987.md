# dmwm/CRABServer pull request #7987: Move Rucio check write logic to ServerUtilities.py

State: closed
Opened: 2023-10-31T12:39:06Z
Closed: 2023-11-03T15:08:27Z
Merged: 2023-11-03T15:08:27Z
URL: https://github.com/dmwm/CRABServer/pull/7987

## Opening post (novicecpp, 2023-10-31T12:39:06Z)

Fix https://github.com/dmwm/CRABServer/issues/5978 

2 news function:
- **`isEnoughRucioQuota()`** check Rucio quota with destination site. Reuse in client client `checkwrite` and `status` command. 
- **`getRucioAccountFromLFN()`** Parsing LFN to get correct Rucio account where group account always has suffix `_group` but LFN prefix will not have this suffix.
    - In example, `crab_test_group` LFN prefix is `/store/group/rucio/crab_test/`

See how we use in client side in PR https://github.com/dmwm/CRABClient/pull/5247.

## Comment (cmsdmwmbot, 2023-10-31T12:42:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 3 warnings
   * 103 comments to review
 * Pycodestyle check: succeeded
   * 153 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1730/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-10-31T13:49:24Z)

at first sight too many changes for such simple subject. Anyhow I need some time to read carefully. e.g. I am puzzled why priviliged account is named

## Comment (belforte, 2023-11-02T15:26:03Z)

OK. I believe I understand now. Couple of comment:
1. I do not like the complex tuple return from  `isEnoughRucioQuota`, a dictionary would be more clear IMHO
2. It looks like I fully overlooked `/store/group/rucio` vs. `/store/user/rucio` point when implementing checks on client side.
3. I still do not understand why you need the privileged account, AFAIK the default TW rucio account (crab_manager) should be able to list usage for any account. At least from lxplus I can do `rucio list-account-usage <account>`  for any account.

## Comment (novicecpp, 2023-11-02T15:37:13Z)

> I still do not understand why you need the privileged account, AFAIK the default TW rucio account (crab_manager) should be able to list usage for any account. At least from lxplus I can do rucio list-account-usage <account> for any account.

My bad. 
I thought you cannot get usage from other account if you do not have admin privilege.
I may confuse with some other errors while I was trying Rucio API.
I will fix.

## Comment (cmsdmwmbot, 2023-11-02T17:46:44Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 15 warnings and errors that must be fixed
   * 3 warnings
   * 103 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1736/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-02T17:53:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 13 warnings and errors that must be fixed
   * 3 warnings
   * 103 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1737/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-03T10:10:24Z)

Can you also take this change to disable in pylint W1514 and  W0707 for ServerUtilities ? We can't "fix" those as we need pyhon2 compatibility for using in Client, but better not to have so many complains from pylint  (see #7756 )

## Comment (novicecpp, 2023-11-03T12:21:18Z)

> In view of reusing getAccountFromLFN also in Client, I'd like to ask for named arguments (client=, site=, lfn=). Generally speaking it makes code more readable

Is an example in a docstring enough? You can call functions with keywords (e.g., `getRucioAccountFromLFN(lfn=/store/user/rucio/tseethon/path/to/dir)` as usual.
I do not use default values when defining functions because I want to enforce that those args are required.

## Comment (belforte, 2023-11-03T13:34:01Z)

> You can call functions with keywords (e.g., getRucioAccountFromLFN(lfn=/store/user/rucio/tseethon/path/to/dir) as usual.

I did not know !  Thanks !
all fine then

## Comment (cmsdmwmbot, 2023-11-03T15:06:54Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 3 warnings
   * 103 comments to review
 * Pycodestyle check: succeeded
   * 155 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1738/artifact/artifacts/PullRequestReport.html
