# dmwm/CRABServer pull request #9024: update DAG node_status every 2 min. Fix #9012

State: closed
Opened: 2025-03-31T10:07:33Z
Closed: 2025-03-31T12:54:17Z
Merged: 2025-03-31T12:54:17Z
URL: https://github.com/dmwm/CRABServer/pull/9024

## Opening post (belforte, 2025-03-31T10:07:33Z)

(no text)

## Comment (belforte, 2025-03-31T10:09:20Z)

@aspiringmind-code change is trivial, in a way, and  we simply have to test. But I will appreciate if you cross-check my understanding of the HTCondor documentation.

## Comment (cmsdmwmbot, 2025-03-31T10:11:28Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 4 comments to review
 * Pycodestyle check: succeeded
   * 74 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2416/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-03-31T12:54:11Z)

Thanks Vijay !
I had not read that ! Most of our DAGs are not that large. But Marco indicated 10MB/s due to this and since I/O is a  critical resource, rewriting a file every 30 sec even if no change seems silly.
The reasoning is in the linked-to iussue.

## Comment (aspiringmind-code, 2025-03-31T13:08:38Z)

Understood, thanks!
