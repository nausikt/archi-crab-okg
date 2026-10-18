# dmwm/CRABServer pull request #7708: expand user tar files in /srv . Correct fix for #7661

State: closed
Opened: 2023-06-30T17:22:25Z
Closed: 2023-06-30T22:57:53Z
Merged: 2023-06-30T22:57:53Z
URL: https://github.com/dmwm/CRABServer/pull/7708

## Opening post (belforte, 2023-06-30T17:22:25Z)

(no text)

## Comment (cmsdmwmbot, 2023-06-30T17:27:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 33 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1570/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T21:13:29Z)

test in https://cmsweb-test2.cern.ch/crabserver/ui/task/230630_211255%3Abelforte_crab_20230630_231250 FAILED

## Comment (cmsdmwmbot, 2023-06-30T22:02:00Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1573/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T22:03:03Z)

test again after fixing above problem: https://cmsweb-test2.cern.ch/crabserver/ui/task/230630_220112%3Abelforte_crab_20230701_000107
fails again

## Comment (cmsdmwmbot, 2023-06-30T22:26:03Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1574/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T22:34:50Z)

new test: https://cmsweb-test2.cern.ch/crabserver/ui/task/230630_223358%3Abelforte_crab_20230701_003353

## Comment (belforte, 2023-06-30T22:44:55Z)

OK. Now user tar files are correclty expanded https://cmsweb.cern.ch:8443/scheddmon/0195/belforte/230630_223358:belforte_crab_20230701_003353/job_out.1.0.txt

## Comment (cmsdmwmbot, 2023-06-30T22:52:10Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 76 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1575/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-06-30T22:57:44Z)

now [job stdout](https://cmsweb.cern.ch:8443/scheddmon/0195/belforte/230630_225136:belforte_crab_20230701_005132/job_out.2.0.txt) has 
```

==== Sandbox untarring in job's top dir STARTING at Fri Jun 30 22:53:29 2023 ====
expanding sandbox.tar.gz in /srv

expanding kh.tar in /srv

expanding kh2.tgz in /srv

expanding kh3.tar.gz in /srv

==== Sandbox untarring FINISHED at Fri Jun 30 22:53:31 2023 ====
```
