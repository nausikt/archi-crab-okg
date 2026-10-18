# dmwm/CRABServer pull request #8492: [PYPI] bump htcondor in pypi image to 23.0.12

State: closed
Opened: 2024-06-13T15:04:24Z
Closed: 2024-06-14T19:47:11Z
Merged: 2024-06-14T19:47:11Z
URL: https://github.com/dmwm/CRABServer/pull/8492

## Opening post (novicecpp, 2024-06-13T15:04:24Z)

Same as upstream https://github.com/dmwm/WMCore/commit/a1fd9035e3f7548b784abc228c8b03cd30152854`
`10.2.x` does not available anymore:
```
ERROR: Could not find a version that satisfies the requirement htcondor~=10.2.3 (from versions: 9.0.17, 10.0.3, 10.0.4, 10.0.6, 10.0.7, 10.0.8, 10.0.9, 10.3.0, 10.5.0, 10.6.0, 10.7.0, 10.8.0, 10.9.0, 23.0.0, 23.0.1, 23.0.2, 23.0.3, 23.0.4, 23.0.6, 23.0.8, 23.0.10, 23.1.0, 23.2.0, 23.3.0, 23.4.0, 23.5.2, 23.6.1, 23.7.2, 23.9.0a2)
ERROR: No matching distribution found for htcondor~=10.2.3
```
Full logs: https://gitlab.cern.ch/crab3/CRABServer/-/jobs/40026384

## Comment (cmsdmwmbot, 2024-06-13T15:06:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2014/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-13T15:30:27Z)

we can surely go for `~=10`.
But support for 10 will stop in September, so we may also start moving to 23.0, which is already tested
in e.g. vocms059 and in my TW
https://htcondor.readthedocs.io/en/main/version-history/introduction-version-history.html

## Comment (novicecpp, 2024-06-14T10:04:46Z)

Agreed. And now all `10.x` versions are gone...
WMCore people also has the same issue: https://mattermost.web.cern.ch/cms-o-and-c/pl/w51kmcsyxtdtdmst9ks3pckdge

Bumping to `23.0.x`.

## Comment (cmsdmwmbot, 2024-06-14T10:11:51Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2015/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-14T11:29:43Z)

will this automatically pick latest 23.0.X for X>12 ? If so.. why do we need 12 in there ? To confuse ourselves ?

## Comment (novicecpp, 2024-06-14T11:36:29Z)

Ah, I see.

Should be `htcondor~=23.0`.

## Comment (mapellidario, 2024-06-14T12:27:07Z)

From the documentation [1], `~=23.0.12` is expanded to `>=23.0.12 AND ==23.0.*`, while `~=23.0` is expanded to `>=23.0 AND ==23.*`. 

[1] https://packaging.python.org/en/latest/specifications/version-specifiers/#compatible-release

## Comment (novicecpp, 2024-06-14T12:29:18Z)

Thanks Dario. 
I am merging then.
(patch version 12 is the latest)

## Comment (belforte, 2024-06-14T12:49:29Z)

hmm. thanks Dario. So we could use `~=23.0.0` if we want latest in 23.0.x ?
Simply I find it a bit confusing to explicitly indicate 12, but we can surely use `~=23.0.12`

## Comment (belforte, 2024-06-14T12:59:35Z)

> now all 10.x versions are gone...

?? 10.0.9 (LTS) is still there. Also 10.5 and later (feature releases). Our bad to have been using 10.2 or 10.4 w/o a proper understanding of HTC version numbering (not that SI had been given any guidance :-(  )

Anyhow, let's stick with 23.0 for a bit more and then think about 24.0 !

## Comment (mapellidario, 2024-06-14T13:00:07Z)

If we simply want the latest `23.0.X`, we can use `==23.0.*`. 

However, if for any reason there is another package that requires htcondor 23.0.5, pip happily installs it and not the latest and shiniest.

In we instead use ` ~=23.0.12`, it means that we tried and tested 23.0.12, it works, we are satisfied with and please pip do not pick anything previous that, if there is another package that requires htcondor 23.0.5, pip will fail.

## Comment (belforte, 2024-06-14T13:14:05Z)

thanks Dario for explanation. I surely never imagined that we could have another pip install elsewhere. But future is always a surprise.  All OK!!

## Comment (belforte, 2024-06-14T13:45:38Z)

I wonder if Wa forgot to merge, or is simply coming back later.
