# dmwm/CRABServer pull request #9061: report last error for jobs in any state. Fix #9059

State: closed
Opened: 2025-05-02T10:28:47Z
Closed: 2025-05-06T08:14:28Z
Merged: 2025-05-06T08:14:27Z
URL: https://github.com/dmwm/CRABServer/pull/9061

## Opening post (belforte, 2025-05-02T10:28:47Z)

(no text)

## Comment (cmsdmwmbot, 2025-05-02T10:30:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 28 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2443/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-02T11:56:57Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2444/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-05-05T09:45:15Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 12 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2446/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-05T09:48:50Z)

thanks for the review Vijay. But the new code while possibly working was not making sense.
I have rewritten i. Hopefully, it is also more clear now (I had problems navigating my own comments!).
You can see "just those changes" by looking at fist commit.

## Comment (belforte, 2025-05-05T14:41:52Z)

thanks @aspiringmind-code 

>  So now we make use of errdict directly to add Error to the nodes.

I think we could also before, but the original developer did not notice it. Maybe a part was that there are so many dictionaries which until a few weeks ago had absolutely no documentation.
could even get rid of `errdict`:
```python
 for jobid in fjrReports.keys():
        if jobid in nodes:
            nodes[jobid,'Error'] = fjrReports[jobid]
```
I do not know if it would be more clear, or less clear.

Let me know if it is OK to merge

## Comment (aspiringmind-code, 2025-05-06T08:25:49Z)

I think errdict is good to have. Ok to merge imho.
