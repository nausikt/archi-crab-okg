# dmwm/CRABServer pull request #9382: protect against being run on old job. Fix #9378

State: closed
Opened: 2026-08-10T14:55:38Z
Closed: 2026-08-10T19:32:51Z
Merged: 2026-08-10T19:32:51Z
URL: https://github.com/dmwm/CRABServer/pull/9382

## Opening post (belforte, 2026-08-10T14:55:38Z)

(no text)

## Comment (cmsdmwmbot, 2026-08-10T15:00:21Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 278 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2879/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-08-10T18:21:36Z)

@belforte No objections. 

Although Claude suggested us a little bit more cheaper[?] implementation by `Query just the job`.

Especially without projection/limit we're pulling full ClassAds for every proc in the cluster. And matching on cluster alone means a sibling proc still in the queue masks the condition we're testing for. What do you think?

```python
constraint = f"ClusterId=={self.dag_clusterid} && ProcId=={self.dag_procid}"
ads = self.schedd.query(constraint=constraint, projection=['ClusterId'], limit=1)
```

## Comment (belforte, 2026-08-10T19:25:08Z)

our cluster are one job only, by construction, so I did not bother to add process number.
I am not sure if restricting list of classAds would make a difference to the schedd retrieval, surely it is immaterial as far as amount of data transferred, anyhow I will add the projection cut. Makes it look more elegant !

## Comment (nausikt, 2026-08-11T07:28:52Z)

> our cluster are one job only, by construction, so I did not bother to add process number. I am not sure if restricting list of classAds would make a difference to the schedd retrieval, surely it is immaterial as far as amount of data transferred, anyhow I will add the projection cut. Makes it look more elegant !

Thanks for education! Apologize for my switched-off brain review.
