# dmwm/CRABClient pull request #5247: Use isEnoughRucioQuota from ServerUtilities.py

State: closed
Opened: 2023-10-31T11:59:50Z
Closed: 2023-11-27T16:17:27Z
Merged: 2023-11-27T16:17:27Z
URL: https://github.com/dmwm/CRABClient/pull/5247

## Opening post (novicecpp, 2023-10-31T11:59:50Z)

Together with CRABServer PR https://github.com/dmwm/CRABServer/pull/7987

Use isEnoughRucioQuota from CRABServer's `ServerUtilities.py`, minimum CRABServer version is [v3.231103](https://github.com/dmwm/CRABServer/releases/tag/v3.231103).

~~Note for one big change; I have moved initialize Rucio client to SubCommand class method because we need to get proper Rucio account to get account usage. You can only allow to get usage from your own account unless you have admin privilege. The problem occur when we want to use group area where it has different account.~~

~~In example, users want store outputs to Rucio group area which need different Rucio account (In our case, we need `crab_test_group` account, not `belforte` or `dmapelli` account). To get the account, we parse the LFN by using `getRucioAccountFromLFN()` from ServerUtilities.py.~~

~~But, LFN information for some command (e.g., `status`) are available inside `__call__` method. [Here an example](https://github.com/novicecpp/CRABClient/blob/38517e8e10f884c9f732736dca3aa6e3c88efbe7/src/python/CRABClient/Commands/status.py#L68).~~

EDITED:

In the end (after reviewew), I have decided to stick with `self.cmdconf['requiresRucio']=True` feature because, in theory, you can get quota from any user, but there is an permission issue in Rucio server so workaround code has been put in place (see comment in https://github.com/dmwm/CRABClient/pull/5247#issuecomment-1825785879).

## Comment (cmsdmwmbot, 2023-10-31T12:01:36Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 30 warnings and errors that must be fixed
   * 17 warnings
   * 475 comments to review
 * Pycodestyle check: succeeded
   * 324 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/986/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-10-31T12:41:17Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 25 warnings and errors that must be fixed
   * 17 warnings
   * 475 comments to review
 * Pycodestyle check: succeeded
   * 324 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/987/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-03T15:33:09Z)

I can see why you did this, but in view of introducing more commands with `self.cmdconf['requiresRucio']=True` I would like to keep Rucio client initialization in SubCommand, like before this PR. And inside specific commands, where a different account is needed, and where the LFN is known, we can switch account name in the client, even possibly restoring it if we want to make it possible to combine commands in a single script via the python API. 
What do you think ?

## Comment (novicecpp, 2023-11-15T13:08:52Z)

Rebase wrong branch :man_facepalming: 
Sorry for noise.

## Comment (cmsdmwmbot, 2023-11-15T13:10:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 25 warnings and errors that must be fixed
   * 17 warnings
   * 475 comments to review
 * Pycodestyle check: succeeded
   * 324 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/996/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-11-15T15:38:43Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 10 warnings
   * 372 comments to review
 * Pycodestyle check: succeeded
   * 270 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/997/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-15T15:41:06Z)

@belforte I have adjusted this PR according to your comments. Please review again.
No rush :)

## Comment (cmsdmwmbot, 2023-11-15T15:41:22Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 10 warnings
   * 372 comments to review
 * Pycodestyle check: succeeded
   * 270 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/998/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-20T11:49:06Z)

also note this very odd output. Rucio says that
 it failed, but prints quotas anyhow.
We need to know what exactly to expect here.
```
belforte@lxplus805/~> rucio whoami
email      : Stefano.Belforte@cern.ch
deleted_at : None
updated_at : 2020-04-28T23:25:20
suspended_at : None
account_type : USER
account    : belforte
status     : ACTIVE
created_at : 2020-04-28T23:25:20
belforte@lxplus805/~> rucio list-account-usage crab_test_group
+----------------+------------+------------+--------------+
| RSE            | USAGE      | LIMIT      | QUOTA LEFT   |
|----------------+------------+------------+--------------|
| T1_DE_KIT_Disk | 863.937 MB | 500.000 GB | 499.136 GB   |
| T2_IT_Legnaro  | 0.000 B    | 2.000 TB   | 2.000 TB     |
+----------------+------------+------------+--------------+
2023-11-20 12:46:29,507	ERROR	Access to the requested resource denied.
Details: Account belforte can not list global account usage.
belforte@lxplus805/~> 
```

hm.. repeating that command I get what looks random occurrence of the 3 possibilities:
1. only the error
2. output and error like example above
3. output with no error

I suspect that there are multiple pods with different configurations and it depends where the query lands to. Anyhow Rahul is away and for Eric this is Thanksgiving week. So we can't follow up

## Comment (cmsdmwmbot, 2023-11-24T14:50:06Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 16 warnings and errors that must be fixed
   * 10 warnings
   * 372 comments to review
 * Pycodestyle check: succeeded
   * 270 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/1017/artifact/artifacts/PullRequestReport.html

## Comment (novicecpp, 2023-11-24T14:56:30Z)

Well, it is indeed the problem we discussed with Eric in DM Dev channel in MM.
But for this PR and the fact that you can probe your own quota stats by default, I initialize a new client with the proper account from parsing LFN, so it works with both group accounts and as an API.

## Comment (belforte, 2023-11-24T17:59:38Z)

Very nice, thanks.

## Comment (belforte, 2023-11-24T18:02:43Z)

we should put here the minimum needed CRABServer tag to have the correct ServerUtilities

## Comment (novicecpp, 2023-11-27T16:17:17Z)

[v3.231103](https://github.com/dmwm/CRABServer/releases/tag/v3.231103), also updated in the issue's description.
