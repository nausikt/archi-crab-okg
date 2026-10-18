# dmwm/CRABServer pull request #7545: Switching crablog's handlers between file and stdout using env var

State: closed
Opened: 2023-02-20T17:36:19Z
Closed: 2023-02-21T12:01:22Z
Merged: 2023-02-21T12:01:22Z
URL: https://github.com/dmwm/CRABServer/pull/7545

## Opening post (novicecpp, 2023-02-20T17:36:19Z)

*Tested in `test12`. Will test in preprod again before merge.*

Use environment variable `CRABSERVER_LOGSTDOUT` to switch crablog's handlers, instead of checking `data.loggingFile` from `config.py`:
- `CRABSERVER_LOGSTDOUT=t` will output crablog to stdout.
- else to file using `TimedRotatingFileHandler` (previous behavior).

This will allow us to **deploy only k8s manifest, without changing content of `config.py`** to make log-to-stdout work properly. Make it more easy to operate when you hurry to roll everything back or after you are done rollback and want to deploy it again, without keep forget to apply `config.py`. 

Env name and value come from new manifest [crabserver.yaml](https://github.com/dmwm/CMSKubernetes/blob/eca72978f74ea49f020a31eee866bd96f0ba7ef2/kubernetes/cmsweb/services/crabserver.yaml#L65-L66) which also use in the [run.sh](https://github.com/dmwm/CMSKubernetes/blob/eca72978f74ea49f020a31eee866bd96f0ba7ef2/docker/crabserver/run.sh#L73).

Also, put `setFormatter` back to `TimedRotatingFileHandler` that I forget to add it in https://github.com/dmwm/CRABServer/pull/7496.

## Comment (cmsdmwmbot, 2023-02-20T17:41:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 6 warnings and errors that must be fixed
   * 1 warnings
   * 20 comments to review
 * Pycodestyle check: succeeded
   * 18 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1436/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-21T11:36:33Z)

only one comment, can you change LOGSTDOUT to LOG2STDOUT ? a bit more descripting and in line "usual practice".

## Comment (novicecpp, 2023-02-21T11:47:19Z)

No, because I already use `CRABSERVER_LOGSTDOUT` in [k8s-manifest](https://github.com/dmwm/CMSKubernetes/blob/eca72978f74ea49f020a31eee866bd96f0ba7ef2/kubernetes/cmsweb/services/crabserver.yaml#L65-L66)/[run.sh](https://github.com/dmwm/CMSKubernetes/blob/eca72978f74ea49f020a31eee866bd96f0ba7ef2/docker/crabserver/run.sh#L73) and those config are not in our repository, need to open new pr, and ask CMSWEB to merge.
Well, we can change it locally but I do not want to risk myself checkout the wrong commit and deploy it.

Sorry for bad variable name. I will add a comment.

## Comment (novicecpp, 2023-02-21T12:00:06Z)

Thanks Stefano.

## Comment (cmsdmwmbot, 2023-02-21T12:02:53Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1437/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-21T12:07:15Z)

a general comment for future similar things:
it is a bit fragile (or simply unconvenient) to force the env.var. to be exactly `t` to enable some feature. Usually people check for 'true` with any capitalization or abbreviation, or at least `t|T|true|True|TRUE` but in case of variables with an explicit action name like "log to stdout" it will be sufficient to check that the variable is set.
