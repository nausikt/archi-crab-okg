# dmwm/CRABServer pull request #9286: add script from Claude

State: closed
Opened: 2026-03-27T10:43:27Z
Closed: 2026-03-27T10:50:25Z
Merged: 2026-03-27T10:50:25Z
URL: https://github.com/dmwm/CRABServer/pull/9286

## Opening post (belforte, 2026-03-27T10:43:27Z)

Since I am annoyed by having to type things like

git push gitlab $TAG  -o ci.variable="SKIP_BUILD=true"  -o ci.variable="SKIP_DEPLOY=true"   -o ci.variable="VERBOSE=1" -o ci.variable="CLIENT_VALIDATION=false" -o ci.variable="CLIENT_CONFIGURATION_VALIDATION=false"  -o ci.variable="STATUS_TRACKING=true" -o ci.variable="DEBUG_TEST=true" 

I asked Claude to write a python script to use CLI options.
Python, not bash, because options parsing in bash would be harder for me to understand and change.
Here it is. Not perfect IMHO since I failed to specify what e.g. to do when no option is passed (default to dry run ?).
But that's now easy to change once we has decided what we want.

Note that it decided by itself to add the help, introduce the dry run and the shortened options . The markdown file is the copy/paste of what Claude wrote in the chat when it produced it.

## Comment (cmsdmwmbot, 2026-03-27T10:47:40Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 20 comments to review
 * Pycodestyle check: succeeded
   * 29 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2761/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-03-27T10:50:20Z)

very safe PR, since it just adds two scripts for users
