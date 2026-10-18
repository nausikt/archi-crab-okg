# dmwm/CRABServer pull request #7581: REST - new endpoint counttasksbyuserandstatus

State: closed
Opened: 2023-04-04T15:34:02Z
Closed: 2023-04-05T11:18:29Z
Merged: 2023-04-05T11:18:29Z
URL: https://github.com/dmwm/CRABServer/pull/7581

## Opening post (mapellidario, 2023-04-04T15:34:02Z)

Fixes #7580 

### status

tested on test11 with `devtwo` and `prod` DB

```plaintext
> curl --cert $X509_USER_PROXY --key $X509_USER_PROXY "https://cmsweb-test11.cern.ch:8443/crabserver/prod/task?subresource=counttasksbyuserandstatus&minutes=60"
{"desc": {"columns": ["tm_username", "tm_task_status", "count(*)"]}, "result": [
 ["alebihan", "SUBMITTED", 48]
,["azacharo", "SUBMITTED", 30]
,["asotorod", "SUBMITTED", 11]
,["sciaba", "SUBMITTED", 7]
,["sanayak", "SUBMITTED", 5]
,["evourlio", "SUBMITTED", 4]
,["azacharo", "TAPERECALL", 3]
,["dmroy", "SUBMITTED", 2]
,["msergeev", "SUBMITTED", 1]
,["iparaske", "KILLED", 1]
,["cgalloni", "SUBMITTED", 1]
,["ckowal", "SUBMITTED", 1]
,["bgreenbe", "SUBMITTED", 1]
]}
```

### details

simply added a new query and subresource

## Comment (cmsdmwmbot, 2023-04-04T15:36:19Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 5 warnings
   * 38 comments to review
 * Pycodestyle check: succeeded
   * 206 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1482/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-04T15:40:14Z)

LGTM. Thanks. I am not a fan of adding "specialized API's" would prefer to have fewer more generic ones which possibly return more data from which the client can pick, than the current situation. But I not it is not "cleanup time" !! Just a thought in case sometimes we can do the job by slightly generalizing existing API's

## Comment (mapellidario, 2023-04-05T11:17:50Z)

> would prefer to have fewer more generic ones which possibly return more data from which the client can pick

this is a valid point, i thought we were all in for monitoring queries that return only little data. I will merge this PR and open a new GH issue about the cleanup
