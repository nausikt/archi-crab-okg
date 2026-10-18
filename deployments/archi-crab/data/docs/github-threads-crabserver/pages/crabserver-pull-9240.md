# dmwm/CRABServer pull request #9240: Add again dagman config file

State: closed
Opened: 2025-12-05T17:12:40Z
Closed: 2026-01-20T15:19:44Z
Merged: 2026-01-20T15:19:44Z
URL: https://github.com/dmwm/CRABServer/pull/9240

## Opening post (belforte, 2025-12-05T17:12:40Z)

fix the problem which led to #9238 

In this I assume that subdag inherit the config from the main dag. Which may not be true.
Needs to be investigate for the time we put something non-trivila in dagman config. file.

## Comment (cmsdmwmbot, 2025-12-05T17:17:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded
   * 64 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2697/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-12-08T11:20:59Z)

I have asked condor support if we need a separate config file for each subdag
https://www-auth.cs.wisc.edu/lists/htcondor-users/2025-December/msg00037.shtml

and here's the reply:
"
SubDAGs will inherit the configuration file of the parents (all the way up to the root DAG in the case of a Sub-SubDAG). If the SubDAG specifies its own configuration file then DAGMan will use the SubDAG specific configuration file and completely ignore the inherited parent DAG configuration file.
"

## Comment (belforte, 2026-01-19T15:57:46Z)

this is now ready to go.
