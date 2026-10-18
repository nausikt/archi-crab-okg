# dmwm/CRABServer pull request #9431: attached CRAB_UselEmail which retrieved via CRIC.

State: closed
Opened: 2026-09-26T10:29:30Z
Closed: 2026-09-28T13:23:44Z
Merged: 2026-09-28T13:23:44Z
URL: https://github.com/dmwm/CRABServer/pull/9431

## Opening post (nausikt, 2026-09-26T10:29:30Z)

CRAB_UserEmail classAds for downstream mail sending mechanics inside PostJob, Jobwrapper. 

See also #9422, #9419

## Comment (cmsdmwmbot, 2026-09-26T10:34:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 comments to review
 * Pycodestyle check: succeeded
   * 113 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2925/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-09-26T11:56:13Z)

tested on test14.

https://cmsweb.cern.ch/scheddmon/059/crabint1/260926_104146:crabint1_crab_maxMemoryMB/SPOOL_DIR/Job.submit
```
My.CRAB_UserDN = "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1"
My.CRAB_UserHN = "crabint1"
My.CRAB_UserEmail = "cms.crab.integration1@cern.ch"
```

## Comment (belforte, 2026-09-27T11:03:01Z)

is this the only place where a classAd is set to the `'undefined'` string ?

## Comment (nausikt, 2026-09-27T11:45:38Z)

No, there's other place set 'underfined' the same way.
```python
393:        jobSubmit['My.CRAB_UserEmail'] = classad.quote(userEmail) if userEmail else 'undefined'
396:        # for VOMS role and group, PostJob and RenewRemoteProxies code want the undefined value, not "
398:        jobSubmit['My.CRAB_UserRole'] = classad.quote(userRole) if userRole else 'undefined'
400:        jobSubmit['My.CRAB_UserGroup'] = classad.quote(userGroup) if userGroup else 'undefined'
451:        jobSubmit['My.JOBGLIDEIN_CMSSite'] = classad.quote('$$([ifThenElse(GLIDEIN_CMSSite is undefined, "Unknown", GLIDEIN_CMSSite)])')
```

## Comment (belforte, 2026-09-28T12:14:00Z)

thanks. I never remember all details of classAds and JDL defintions and was worried of introducing a new way which may not work.
Looks good, you can merge.

## Comment (nausikt, 2026-09-28T13:23:25Z)

Thank you Stefano.
