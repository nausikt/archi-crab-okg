# dmwm/CRABServer pull request #8884: Fix #8809

State: closed
Opened: 2025-01-20T09:49:08Z
Closed: 2025-01-20T11:37:50Z
Merged: 2025-01-20T11:37:50Z
URL: https://github.com/dmwm/CRABServer/pull/8884

## Opening post (aspiringmind-code, 2025-01-20T09:49:08Z)

See https://github.com/dmwm/CRABServer/issues/8809

- Remove CHECK_TEST_RESULT variable to make it easier to understand and streamlining
- Make the pipeline more robust using rules like skip_check and skip_submit
- Now we only need to set three variables: SUBMIT_STATUS_TRACKING, CLIENT_CONFIGURATION_VALIDATION and CLIENT_VALIDATION_SUITE for both task submission and checking of their respective actions. By default, they are all set to true.
- We additionally have three skip variables SKIP_BUILD, SKIP_DEPLOY and SKIP_SUBMIT which can be used if so desired. By default they are all set to false.

## Comment (cmsdmwmbot, 2025-01-20T09:53:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2321/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-01-20T10:04:19Z)

> Now we only need to set three variables: SUBMIT_STATUS_TRACKING, CLIENT_CONFIGURATION_VALIDATION and CLIENT_VALIDATION_SUIT

should `SUBMIT_` be removed from the name of the first variable then, for consistency ? Same for `_SUIT` in the last.

## Comment (belforte, 2025-01-20T10:18:28Z)

thanks Vijay, I agree with plan in the top bullet list, but am not able to relate it to the code. Can we have a sort of walk-through ?

## Comment (aspiringmind-code, 2025-01-20T10:30:10Z)

Yes, sure

## Comment (cmsdmwmbot, 2025-01-20T10:31:03Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2322/artifact/artifacts/PullRequestReport.html
