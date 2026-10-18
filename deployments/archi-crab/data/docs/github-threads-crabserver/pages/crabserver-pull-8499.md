# dmwm/CRABServer pull request #8499: add /etc/condor/condor_config to TW Fix #8497

State: closed
Opened: 2024-06-14T20:59:29Z
Closed: 2024-06-18T17:14:10Z
Merged: 2024-06-18T17:14:10Z
URL: https://github.com/dmwm/CRABServer/pull/8499

## Opening post (belforte, 2024-06-14T20:59:29Z)

(no text)

## Comment (cmsdmwmbot, 2024-06-14T21:02:50Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2016/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-06-18T08:07:35Z)

thanks Wa. Sorry I had meant to explain why I asked for a review here but somehow it got lost. Of course the change in itself is a no-brainer, but I meant to let you comment on the specific way I implemented in Dockerfile. You made me worry about having too many `RUN` and hence too many layers and too large images. But I do not have a proper understanding.

## Comment (novicecpp, 2024-06-18T10:49:41Z)

> You made me worry about having too many RUN and hence too many layers and too large images.

You understand it correctly. But this change is not much compare to largish `pip install` and `gfal-*` layer. 
One thing you need to keep in mind is, make sure that when you create new directory and copy file has proper permission you want for service, avoid `chmod` like I do in [cicd/crabtaskworker_pypi/Dockerfile#L134](https://github.com/dmwm/CRABServer/blob/8e4ff122b8d64c4b7fb7f2594748b13b2455b91a/cicd/crabtaskworker_pypi/Dockerfile#L134)
