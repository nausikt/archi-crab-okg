# dmwm/CRABServer issue #8185: fix Jenkins StatusTracking tests

State: closed
Opened: 2024-01-17T15:12:12Z
Closed: 2024-04-24T10:33:21Z
Labels: Priority: High, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/8185

## Opening post (belforte, 2024-01-17T15:12:12Z)

- [x]  authentication problem for `crab_test` Rucio group. [CMSTRANSF-802](https://its.cern.ch/jira/projects/CMSTRANSF/issues/CMSTRANSF-802)
   * this is working now, but we should use a different e-group to avoid spamming Shahzad
- [ ] given how ST works, it is bad to have some tests with and some w/o publications.
   - [ ] Those different configs should be used in CCV tests
   - [x] ST tests are meant for running tasks with several jobs and verify that all complete OK, ideally we should check publication on all of them. Mostly as a transient after introducing publication check there is now an overall switch to check/not-check publication.
   - [x] if a way is found to make the publication check behave correctly in the two cases, I have no objection to using it, as long as it is a simple thing.

## Comment (belforte, 2024-01-19T17:05:24Z)

one simple, if crude, way to deal with publication could be to disable publication check in 

https://github.com/dmwm/CRABServer/blob/d22b6c243edfefa3856343d6bcf0e70a8e4cf90e/test/container/testingScripts/statusTracking.py#L66
when ` task['taskName']` contains the 'nopub' string

## Comment (belforte, 2024-01-22T14:45:07Z)

I have made StatusTracking test skips tasks with "nopublication" in the name. Keep this open for the other two action: change e-group for Rucio and add pub/nopub to CCV

## Comment (belforte, 2024-04-24T10:33:21Z)

e-group was done. Changes to CCV are better tracked in ad hoc issue. But atm I have no appetite for moving publication tests from ST to CCV.
