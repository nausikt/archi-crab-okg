# dmwm/CRABServer pull request #7716: RUCIO_Transfers.py: Improving readability

State: closed
Opened: 2023-07-05T10:34:13Z
Closed: 2023-07-06T08:37:22Z
Merged: 2023-07-06T08:37:22Z
URL: https://github.com/dmwm/CRABServer/pull/7716

## Opening post (novicecpp, 2023-07-05T10:34:13Z)

This PR replaces [#7693](https://github.com/dmwm/CRABServer/pull/7693) to focus on readability.

- The separation between rucio replica and the metadata we use for crab rest. The metadata is called fileDoc.
- Change the return variable structure from prepare().
- Rename update to rest method to reflect state change.
- Remove `initReplicasInContainer()` and use `populateLFN2DatasetMap()` directly where it needed.
- remove "skip monitoring lock for the files in the same run.", the useless statement.

## Comment (cmsdmwmbot, 2023-07-05T10:37:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1579/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-05T13:47:01Z)

thanks. This looks good to me. I can't swear that changes are all applied consistently etc., but they all look proper and I think it is easier to run and test than try to find possible name mismatch by reading the code.
