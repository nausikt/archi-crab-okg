# dmwm/CRABServer pull request #9096: retry_call for rucio

State: closed
Opened: 2025-05-27T09:27:26Z
Closed: 2025-07-04T12:45:52Z
Merged: 2025-07-04T12:45:52Z
URL: https://github.com/dmwm/CRABServer/pull/9096

## Opening post (aspiringmind-code, 2025-05-27T09:27:26Z)

Fix #9052

## Comment (cmsdmwmbot, 2025-05-27T09:31:05Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2485/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-05-27T09:32:03Z)

@belforte This is a work in progress. I'd like your input. Did you envision something like this? Should I change RETRIES and DELAY values? Any other changes? Thanks!

## Comment (belforte, 2025-05-27T13:16:30Z)

in this `retry_call` is not specific of Rucio so could go in a more general "utility" file.

As to what I had in mind, I was dreaming of a more transparent implementation.

While this will work, I am not happy with having to change every line where we have a call to Rucio client everywhere in the code base.
Is there some way to make it automatic that the object returned by `getNativeRucioClient()` has retry logic inside it ?

Would decorators help ?

## Comment (aspiringmind-code, 2025-05-27T13:22:13Z)

Yes, I agree that using decorators would be better.

## Comment (belforte, 2025-05-27T14:13:16Z)

I believe that we can achieve what I dreamt of by having a new myRucio client which implements all methods which we use from Rucio client and for each wraps a call to Rucio with `retry_call`. But while that's OK for calls to http where we only need to expose put/get/post/delete, Rucio has so many methods that this is certainly crazy.
Maybe there is no way ?

## Comment (cmsdmwmbot, 2025-06-17T13:48:20Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 19 comments to review
 * Pycodestyle check: succeeded
   * 19 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2507/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-17T14:10:59Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 91 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2508/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-06-17T14:16:15Z)

@belforte @sinonkt  In the last commit, I built a proxy class that wraps a real Client and delegates all calls to it, while adding automatic retry for all its methods. To propagate this change, wherever we use `from rucio.client import Client` we can simply shift to `from RucioUtils import Client` I have shown that in a few scripts. There are more places where we will need to change the import statement and will have to make sure different scripts can import from RucioUtils. This is not tested. Do you like this approach? This imo is a concise way to add retries and bring uniformity around rucio calls.

## Comment (belforte, 2025-06-17T14:38:03Z)

I love this.
I fear a bit that it is so transparent to be confusing... but maybe I am simply scared of changes. Like all old men :-)

## Comment (belforte, 2025-06-17T14:40:27Z)

I would like to understand how this works, just for may education. Maybe we can go through it in some chat ?

## Comment (nausikt, 2025-06-17T15:02:02Z)

> @belforte @sinonkt In the last commit, I built a proxy class that wraps a real Client and delegates all calls to it, while adding automatic retry for all its methods. To propagate this change, wherever we use `from rucio.client import Client` we can simply shift to `from RucioUtils import Client` I have shown that in a few scripts. There are more places where we will need to change the import statement and will have to make sure different scripts can import from RucioUtils. This is not tested. Do you like this approach? This imo is a concise way to add retries and bring uniformity around rucio calls.

I love this approach— it's much more elegant and will definitely provide a solid foundations for us to addressing further complex features around Rucio.

Something minor to add here which you might already planned out, I would love to see `getNativeRucioClient` to simply return `self._client` and all things regarding client initialization was moved out and done centrally in your proxied class thus we utilized proxied class even more. (At my first glance, It's not obvious to me that should we stick to have singleton of rucio client? or we should allow instantiation of new client instance via `getNativeRucioClient`) 

So far, It's Looks like a really good direction to me! Thanks!

## Comment (aspiringmind-code, 2025-06-18T08:41:44Z)

@belforte @sinonkt Thanks for your kind and encouraging remarks. Yes, we can discuss more regarding this over zoom chat.

## Comment (cmsdmwmbot, 2025-06-30T09:14:30Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 1 warnings
   * 33 comments to review
 * Pycodestyle check: succeeded
   * 91 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2514/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-30T09:57:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 1 warnings
   * 143 comments to review
 * Pycodestyle check: succeeded
   * 122 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2515/artifact/artifacts/PullRequestReport.html

## Comment (aspiringmind-code, 2025-06-30T12:47:57Z)

See [Pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12335238) especially the status tracking Rucio tasks.
Also from TW log example of attempts introduced in RucioUtils shown below:
```
2025-06-30 12:05:39,231:WARNING:RucioUtils,25:Failed to execute 'add_replication_rule' (attempt 2/3): A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated

2025-06-30 12:08:40,458:WARNING:RucioUtils,25:Failed to execute 'add_replication_rule' (attempt 3/3): A duplicate rule for this account, did, rse_expression, copies already exists.
Details: (cx_Oracle.IntegrityError) ORA-00001: unique constraint (CMS_RUCIO_PROD.RULES_SC_NA_AC_RS_CO_UQ_IDX) violated
2025-06-30 12:08:40,458:ERROR:RucioUtils,33:Operation 'add_replication_rule' failed after 3 attempts
2025-06-30 12:08:40,458:DEBUG:RucioActions,90:A duplicate rule for this account, did, rse_expression, copies already exists. Use that
```

## Comment (cmsdmwmbot, 2025-07-01T07:44:12Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 1 warnings
   * 143 comments to review
 * Pycodestyle check: succeeded
   * 123 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2516/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-07-03T10:36:48Z)

Sorry for delay @aspiringmind-code 
I have no issues with the code, would have used different names though, like stop using getNativeRucioClient name. But I guess we can do such things more easily after this is merged.

## Comment (aspiringmind-code, 2025-07-04T12:45:40Z)

Thanks!
