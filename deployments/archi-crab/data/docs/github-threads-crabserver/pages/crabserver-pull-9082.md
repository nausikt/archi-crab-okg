# dmwm/CRABServer pull request #9082: Enable CRIC service and wmcore cache on TaskWorker

State: closed
Opened: 2025-05-19T12:44:42Z
Closed: 2025-07-29T20:19:02Z
URL: https://github.com/dmwm/CRABServer/pull/9082

## Opening post (nausikt, 2025-05-19T12:44:42Z)

enabling of _expandSites, _checkSites and _checkASODestination functionalities on TaskWorker. Suppressing CRIC service debugging log and also utilizing WMCore's Service cache mechanism by enabling usestalecache. regarding #6917

## Comment (cmsdmwmbot, 2025-05-19T12:47:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 87 comments to review
 * Pycodestyle check: succeeded
   * 343 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2454/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-05-22T11:59:28Z)

which tests did you run ?
I tried to point my TW to your branch and submitted with 
`config.Site.whitelist = ['T2_IT_*']`
but that was not expanded inside the TW, the same  `= ['T2_IT_*']` was passed to the scheduler and submission failed inside the dagman because in there we expect a list of site names, no `*`.

## Comment (belforte, 2025-05-22T12:24:11Z)

at first sight at least these two lines need changing
https://github.com/dmwm/CRABServer/blob/44564702517657f69da9d667db70105da0360ae3/src/python/TaskWorker/Actions/DagmanCreator.py#L347-L348

I wonder if a safer and simpler alternative would be to expand the black/white list in the beginning of DagmanCreator and replace the value in the `task` dictionary, leaving the current coder otherwise unchanged.
Maybe even overwrite the field in the DB with the expanded list. 

And btw no need to port here the _checkASO thing, banned destinations is always empty and we should simply remove all code about it.

There is no need for CRIC in PreDag. Another useless change.

## Comment (belforte, 2025-05-22T14:18:04Z)

a more drastic alternative would be to add a new action in the Handler, where black/white list are expanded, subtracted, combined with global blacklist and a list of possible sites written in the task dictionary which can be used but all the following code which will become more simple.

## Comment (cmsdmwmbot, 2025-06-05T10:52:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 87 comments to review
 * Pycodestyle check: succeeded
   * 343 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2493/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-06T09:17:14Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 87 comments to review
 * Pycodestyle check: succeeded
   * 343 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2494/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-10T17:38:21Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 87 comments to review
 * Pycodestyle check: succeeded
   * 343 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2497/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-10T19:09:05Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 87 comments to review
 * Pycodestyle check: succeeded
   * 343 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2498/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-06-10T20:40:34Z)

Thanks @belforte! with your walkthrough/guidelines it's much obvious to me how to patch & debugging things in CRAB.
And Finally! I quite confident that this PR is works and ready for merge.

***In Short***: I've fixed this PR as you mentioned and tested by both [manual submissions on test14](https://cmsweb-test14.cern.ch/crabserver/ui/task/250610_194559%3Akphornsi_crab_20250610_214552) and through all test cases in pipeline [here](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12200601).

So, could you please have a final review and give me green or red light? for the merge please? Thanks!
_______
#### **In Details**
You were right this PR didn't worked at first glance. Actually it's silently stuck at SUBMITTED state till eternity when things goes wrong, and At that time, It's not apparent to me where to find more clues since the job itself not considered to be failed either.
```
[kphornsi@lxplus953 workspace]$ crab status -d /tmp/crabStatusTracking/crab_20250610_135115
Rucio client intialized for account kphornsi
CRAB project directory:		/tmp/crabStatusTracking/crab_20250610_135115
Task name:			250610_115120:kphornsi_crab_20250610_135115
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:	SUBMITTED
....
Task bootstrapped at 2025-06-10 12:06:16 UTC. 5966 seconds ago
Task bootstrapped on schedd more than 99 minutes ago
But no status info is available yet. If this persists report it to cmstalk+computing-tools@dovecotmta.cern.ch
Log file is /tmp/crabStatusTracking/crab_20250610_135115/crab.log
```
After i've investigated deeper, My clumsy indeed! Thanks for pointed this out, where i've overlooked, before we dumped task infos including site {white|black}list into ClassADs string, that needed to be expanded as well. with the aforementioned flaws All jdl and Dags of every jobs were left unexpanded as you can see below job's artifacts at Schedd. (** I ignored details around *prejob* and *adjustedout* for easy readability)
```
[root@vocms059 cluster10240013.proc0.subproc0]# grep -iR 'CRAB_Site' *
_CONDOR_JOB_AD:CRAB_SiteBlacklist = { "T2_ES_IFCA" }
_CONDOR_JOB_AD:CRAB_SiteWhitelist = { "T1_*","T2_US_*","T2_IT_*","T2_DE_*","T2_ES_*","T2_FR_*","T2_UK_*" }
dag_bootstrap.out:CRAB_SiteBlacklist = { "T2_ES_IFCA" }
dag_bootstrap.out:CRAB_SiteWhitelist = { "T1_*","T2_US_*","T2_IT_*","T2_DE_*","T2_ES_*","T2_FR_*","T2_UK_*" }
Job.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
Job.submit:My.CRAB_SiteWhitelist = {"T1_*", "T2_US_*", "T2_IT_*", "T2_DE_*", "T2_ES_*", "T2_FR_*", "T2_UK_*"}
subdag.jdl:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
subdag.jdl:My.CRAB_SiteWhitelist = {"T1_*", "T2_US_*", "T2_IT_*", "T2_DE_*", "T2_ES_*", "T2_FR_*", "T2_UK_*"}
WEB_DIR/SPOOL_DIR/Job.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
WEB_DIR/SPOOL_DIR/Job.submit:My.CRAB_SiteWhitelist = {"T1_*", "T2_US_*", "T2_IT_*", "T2_DE_*", "T2_ES_*", "T2_FR_*", "T2_UK_*"}
WEB_DIR/SPOOL_DIR/dag_bootstrap.out:CRAB_SiteBlacklist = { "T2_ES_IFCA" }
WEB_DIR/SPOOL_DIR/dag_bootstrap.out:CRAB_SiteWhitelist = { "T1_*","T2_US_*","T2_IT_*","T2_DE_*","T2_ES_*","T2_FR_*","T2_UK_*" }
WEB_DIR/SPOOL_DIR/subdag.jdl:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
WEB_DIR/SPOOL_DIR/subdag.jdl:My.CRAB_SiteWhitelist = {"T1_*", "T2_US_*", "T2_IT_*", "T2_DE_*", "T2_ES_*", "T2_FR_*", "T2_UK_*"}
[root@vocms059 cluster10240013.proc0.subproc0]#
```

After patched and fixed some JSON-Serializable bugs, it's went well and completed as expected. as you can see in the following evidences that it's really works on TaskWorker side and CRIC-related functionality were no longer facilitated by CRABServer. (P.S. breakpoint were before site list expanding at TaskWorker).
```
-> siteWhitelist = self._expandSites(set(kwargs['task','tm_site_whitelist']))
(Pdb) kwargs['task','tm_site_whitelist']
['T1_*', 'T2_US_*', 'T2_IT_*', 'T2_DE_*', 'T2_ES_*', 'T2_FR_*', 'T2_UK_*']
(Pdb) ### ^--- The above was unexpanded list sent from CRABServer! 
          ### ^--- (hold implication that CRABServer wasn't the one who resolved Site{BlackWhite}List) 
          ### ^--- Thus plain user's input was forward to TaskWorker here ###
(Pdb) n
Site T2_DE_* expanded to ['T2_DE_DESY', 'T2_DE_RWTH'] during validate
Site T2_FR_* expanded to ['T2_FR_GRIF', 'T2_FR_IPHC'] during validate
Site T2_US_* expanded to ['T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt', 'T2_US_Wisconsin'] during validate
Site T1_* expanded to ['T1_DE_KIT', 'T1_ES_PIC', 'T1_FR_CCIN2P3', 'T1_IT_CNAF', 'T1_PL_NCBJ', 'T1_RU_JINR', 'T1_UK_RAL', 'T1_US_FNAL'] during validate
Site T2_ES_* expanded to ['T2_ES_CIEMAT', 'T2_ES_IFCA'] during validate
Site T2_IT_* expanded to ['T2_IT_Bari', 'T2_IT_Legnaro', 'T2_IT_Pisa', 'T2_IT_Rome'] during validate
Site T2_UK_* expanded to ['T2_UK_London_Brunel', 'T2_UK_London_IC', 'T2_UK_SGrid_Bristol', 'T2_UK_SGrid_RALPP'] during validate
-> siteBlacklist = self._expandSites(set(kwargs['task','tm_site_blacklist']))
(Pdb) siteWhitelist
{'T2_IT_Bari', 'T2_UK_SGrid_RALPP', 'T2_UK_London_IC', 'T2_US_Nebraska', 'T1_PL_NCBJ', 'T2_FR_IPHC', 'T2_US_Caltech', 'T1_DE_KIT', 'T2_US_Florida', 'T1_RU_JINR', 'T2_US_MIT', 'T2_UK_London_Brunel', 'T1_US_FNAL', 'T2_DE_DESY', 'T2_FR_GRIF', 'T1_ES_PIC', 'T2_UK_SGrid_Bristol', 'T2_US_Vanderbilt', 'T2_DE_RWTH', 'T2_US_Purdue', 'T2_US_Wisconsin', 'T2_IT_Rome', 'T1_UK_RAL', 'T2_ES_CIEMAT', 'T2_US_UCSD', 'T2_IT_Legnaro', 'T2_ES_IFCA', 'T1_IT_CNAF', 'T1_FR_CCIN2P3', 'T2_IT_Pisa'}
(Pdb) ### ^--- Then, Site{White/Black}List were successfully expanded on TaskWorkers ###
```
As a result, they were properly expanded and running fine as we expected!
```
[kphornsi@vocms059 250610_194559:kphornsi_crab_20250610_214552]$ grep -iR CRAB_Site
SPOOL_DIR/Job.9.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.9.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.4.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.4.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
grep: SPOOL_DIR/_condor_stderr: Permission denied
SPOOL_DIR/Job.5.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.5.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.2.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.2.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/_CONDOR_JOB_AD:CRAB_SiteBlacklist = { "T2_ES_IFCA" }
SPOOL_DIR/_CONDOR_JOB_AD:CRAB_SiteWhitelist = { "T2_UK_SGrid_RALPP","T2_FR_GRIF","T2_DE_RWTH","T2_US_UCSD","T1_IT_CNAF","T2_UK_SGrid_Bristol","T1_PL_NCBJ","T2_US_Nebraska","T1_US_FNAL","T1_DE_KIT","T2_UK_London_IC","T2_IT_Bari","T1_UK_RAL","T2_IT_Pisa","T2_UK_London_Brunel","T2_IT_Rome","T2_FR_IPHC","T2_US_Florida","T2_US_Purdue","T1_FR_CCIN2P3","T1_ES_PIC","T2_US_Vanderbilt","T2_US_MIT","T2_ES_CIEMAT","T2_ES_IFCA","T2_DE_DESY","T2_IT_Legnaro","T2_US_Wisconsin","T2_US_Caltech","T1_RU_JINR" }
SPOOL_DIR/Job.6.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.6.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.1.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.1.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.7.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.7.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.8.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.8.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.10.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.10.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/Job.3.submit:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/Job.3.submit:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
SPOOL_DIR/dag_bootstrap.out:CRAB_SiteBlacklist = { "T2_ES_IFCA" }
SPOOL_DIR/dag_bootstrap.out:CRAB_SiteWhitelist = { "T2_UK_SGrid_RALPP","T2_FR_GRIF","T2_DE_RWTH","T2_US_UCSD","T1_IT_CNAF","T2_UK_SGrid_Bristol","T1_PL_NCBJ","T2_US_Nebraska","T1_US_FNAL","T1_DE_KIT","T2_UK_London_IC","T2_IT_Bari","T1_UK_RAL","T2_IT_Pisa","T2_UK_London_Brunel","T2_IT_Rome","T2_FR_IPHC","T2_US_Florida","T2_US_Purdue","T1_FR_CCIN2P3","T1_ES_PIC","T2_US_Vanderbilt","T2_US_MIT","T2_ES_CIEMAT","T2_ES_IFCA","T2_DE_DESY","T2_IT_Legnaro","T2_US_Wisconsin","T2_US_Caltech","T1_RU_JINR" }
SPOOL_DIR/subdag.jdl:My.CRAB_SiteBlacklist = {"T2_ES_IFCA"}
SPOOL_DIR/subdag.jdl:My.CRAB_SiteWhitelist = {"T2_UK_SGrid_RALPP", "T2_FR_GRIF", "T2_DE_RWTH", "T2_US_UCSD", "T1_IT_CNAF", "T2_UK_SGrid_Bristol", "T1_PL_NCBJ", "T2_US_Nebraska", "T1_US_FNAL", "T1_DE_KIT", "T2_UK_London_IC", "T2_IT_Bari", "T1_UK_RAL", "T2_IT_Pisa", "T2_UK_London_Brunel", "T2_IT_Rome", "T2_FR_IPHC", "T2_US_Florida", "T2_US_Purdue", "T1_FR_CCIN2P3", "T1_ES_PIC", "T2_US_Vanderbilt", "T2_US_MIT", "T2_ES_CIEMAT", "T2_ES_IFCA", "T2_DE_DESY", "T2_IT_Legnaro", "T2_US_Wisconsin", "T2_US_Caltech", "T1_RU_JINR"}
```
And here is final status of submitted test task that looked identical with the one i got from test2.
```
[kphornsi@lxplus953 workspace]$ crab status -d /tmp/crabStatusTracking/crab_20250610_214552
Rucio client intialized for account kphornsi
CRAB project directory:		/tmp/crabStatusTracking/crab_20250610_214552
Task name:			250610_194559:kphornsi_crab_20250610_214552
Grid scheduler - Task Worker:	crab3@vocms059.cern.ch - crab-dev-tw05
Status on the CRAB server:	SUBMITTED
Task URL to use for HELP:	https://cmsweb-test14.cern.ch/crabserver/ui/task/250610_194559%3Akphornsi_crab_20250610_214552
Dashboard monitoring URL:	https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=kphornsi&var-task=250610_194559%3Akphornsi_crab_20250610_214552&from=1749581159000&to=now
Warning:			The following sites from the user site whitelist are blacklisted by the CRAB server: ['T2_UK_SGrid_Bristol']. Since the CRAB server blacklist has precedence, these sites are not considered in the user whitelist.
Warning:			The following sites appear in both the user site blacklist and whitelist: ['T2_ES_IFCA']. Since the whitelist has precedence, these sites are not considered in the blacklist.
Status on the scheduler:	COMPLETED

Jobs status:                    finished     		100.0% (10/10)

Publication status of 1 dataset(s):	new          		100.0% (10/10)
(from CRAB internal bookkeeping in transferdb)

Output dataset:			/GenericTTbar/kphornsi-autotest-1749584752-94ba0e06145abd65ccb1d21786dc7e1d/USER
Output dataset DAS URL:		https://cmsweb.cern.ch/das/request?input=%2FGenericTTbar%2Fkphornsi-autotest-1749584752-94ba0e06145abd65ccb1d21786dc7e1d%2FUSER&instance=prod%2Fphys03

Warning: the max jobs runtime is less than 30% of the task requested value (60 min), please consider to request a lower value for failed jobs (allowed through crab resubmit) and/or improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task.

Warning: the average jobs CPU efficiency is less than 50%, please consider to improve the jobs splitting (e.g. config.Data.splitting = 'Automatic') in a new task

Summary of run jobs:
 * Memory: 96MB min, 796MB max, 315MB ave
 * Runtime: 0:04:43 min, 0:05:23 max, 0:04:47 ave
 * CPU eff: 5% min, 13% max, 8% ave
 * Waste: 1:07:39 (58% of total)

Log file is /tmp/crabStatusTracking/crab_20250610_214552/crab.log
```

## Comment (nausikt, 2025-06-10T21:17:17Z)

> at first sight at least these two lines need changing
> 
> https://github.com/dmwm/CRABServer/blob/44564702517657f69da9d667db70105da0360ae3/src/python/TaskWorker/Actions/DagmanCreator.py#L347-L348
> 
> I wonder if a safer and simpler alternative would be to expand the black/white list in the beginning of DagmanCreator and replace the value in the `task` dictionary, leaving the current coder otherwise unchanged. Maybe even overwrite the field in the DB with the expanded list.
> 
> And btw no need to port here the _checkASO thing, banned destinations is always empty and we should simply remove all code about it.
> 
> There is no need for CRIC in PreDag. Another useless change.

Regarding simpler alternative and elegance action in handler, I thought of opening new issue and PR as a kind of code clean-up/refactoring after this changes were bulletproof in canary. 

Separate elegance clean-up from this issue which mostly concern about migrating functionality from CRABServer to TaskWorker, and ensure everything works as usual.

## Comment (belforte, 2025-06-11T07:41:27Z)

yes and no. I agree that "it works" usually go before "it is beautiful", but having non-needed changes may obscure thing, makes reviewing harder and adds useless work to cleanup.
Please try in PreDag to call DagmanCreator with `resourceCatalog=None` and make sure to test with automatic splitting (only situation where PreDag is used) and a white/black list with `*` (note that it is not part of the tests in the pipeline)

## Comment (nausikt, 2025-06-11T08:31:16Z)

> yes and no. I agree that "it works" usually go before "it is beautiful", but having non-needed changes may obscure thing, makes reviewing harder and adds useless work to cleanup. Please try in PreDag to call DagmanCreator with `resourceCatalog=None` and make sure to test with automatic splitting (only situation where PreDag is used) and a white/black list with `*` (note that it is not part of the tests in the pipeline)

Understood! and seems like i am not thoughtful enough regarding testing coverage.
*Question*: when done with testing, should we gradually added these test cases to the pipeline every time we introduce new  test cases?

## Comment (cmsdmwmbot, 2025-06-26T11:29:55Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 86 comments to review
 * Pycodestyle check: succeeded
   * 369 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2510/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-26T12:39:56Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 39 warnings and errors that must be fixed
   * 5 warnings
   * 99 comments to review
 * Pycodestyle check: succeeded
   * 350 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2511/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-06-26T13:28:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 40 warnings and errors that must be fixed
   * 5 warnings
   * 101 comments to review
 * Pycodestyle check: succeeded
   * 353 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2512/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-06-26T14:35:43Z)

@belforte kwargs['task'] seems to be the only key that was properly relayed through chain of actions though :sob:

it's still not apparent to me whether there is some kind of context scope var in WMCore framework. So i've try relaying it through args in Result(task=..., result=(...<args>...) but it's still required lot of changes at the result of each downstream TaskAction.

## Comment (nausikt, 2025-06-26T14:37:19Z)

Options left [?] are: 
[1] keep looking for things like context scope in handler that could be good place to pass along resolved var (e.g. `possiblesites`) efficiently throughout chain of actions.
[2] move `SiteInfoResolver` action from *After* *MyProxyLogon* to **Just Right Before** **DagmanCreator** where we actually start using site infos.
[3] save it in kwargs['task'] anyway. 

Would love to hear your thoughts @belforte

## Comment (cmsdmwmbot, 2025-06-26T15:03:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 31 warnings and errors that must be fixed
   * 5 warnings
   * 102 comments to review
 * Pycodestyle check: succeeded
   * 354 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2513/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2025-06-26T15:21:33Z)

` kwargs['task']` is the right place. What do you want to save in there ?

## Comment (nausikt, 2025-06-27T06:58:58Z)

> ` kwargs['task']` is the right place. What do you want to save in there ?

possiblesites that was subtracted by global black list.

I also wish to port further site-related logics (the resolving of availablesites, blocks with or w/o locations/banned locations) to bring high cohesive/correlated stuffs together into SiteResolver but seems like it tightly coupling with SplitterResults, require to loop through jobgroup for locations info retrieval. 

https://github.com/dmwm/CRABServer/blob/c378484de98e554338cfc38b20a94a4498967a71/src/python/TaskWorker/Actions/DagmanCreator.py#L869-L1024

May be i should port and introduced them as functions in SiteInfoResolver class for better clarity and reusability.

## Comment (belforte, 2025-06-27T08:03:47Z)

maybe we do not need those lines after `if ignorelocality` ? is that the only place which makes you think of doing more than simply overwriting black and white lists in `task[]` with the expanded ones after resolving the `*`'s ?

## Comment (nausikt, 2025-06-27T08:08:04Z)

Yes, it's the only place that i think of made it into functions for hopefully better clarity.

## Comment (belforte, 2025-06-27T08:12:45Z)

will this go away if we enforce that users provide a site white list whenever they set `ignoreLocality = True` ?
Better simplify the code then make it more complex !

## Comment (nausikt, 2025-06-27T08:36:00Z)

Yes, it does simplify, can we enforce?

For clarity, I sincerely would like to simplifying things by turn all logics that resolved **availablesites** into better smaller fns with clarity naming that perform atomic task, Right now, the logics there were a little bit spaghetteid inside gigantic createSubDag fn, which probably require our mental efforts to comprehend every time we revisited this code.

## Comment (belforte, 2025-06-27T08:45:38Z)

> Yes, it does simplify, can we enforce?

why not ?

> For clarity, I sincerely would like to simplifying things by turn all logics that resolved availablesites into better smaller fns

go for it ! :rocket:

## Comment (nausikt, 2025-06-27T08:51:33Z)

> > Yes, it does simplify, can we enforce?
> 
> why not ?
> 
> > For clarity, I sincerely would like to simplifying things by turn all logics that resolved availablesites into better smaller fns
> 
> go for it ! 🚀

Okkk, For clarity we will enforce ignoreLocality by just don't take user input 'tm_ignore_locality' into account then.
```
ignoreLocality = kwargs['task','tm_ignore_locality'] == 'T'
```

## Comment (belforte, 2025-06-27T09:07:03Z)

hmm... looks like we are on different wave lengths.
Users are and will be free to use ignoreLocality (even if our doc says "not use it"), but we will enforce that when they use it they provide and explicit white list (even as large as T1*,T2*,T3*) so that you have something to resolve in the SiteResolve action. Then in DBSDataDiscovery we will keep current logic where the user provided white list is ANDed with block locations if ignoreLocality is False, or used as it is if ignoreLocality is True.

I expect that Splitter will not mention ignoreLocality. 

FWIW i wanted to cal that "OverrideLocation" which would have been much more clear, people deploying the intial xrootd data federation wanted something which emphasized more the concept "Any data Anywhere Anytime".

Hope things are more clear now.
We can talk about ignore locality on zoom this afternoon otherwise.

## Comment (nausikt, 2025-06-27T09:17:17Z)

> hmm... looks like we are on different wave lengths. Users are and will be free to use ignoreLocality (even if our doc says "not use it"), but we will enforce that when they use it they provide and explicit white list (even as large as T1*,T2*,T3*) so that you have something to resolve in the SiteResolve action. Then in DBSDataDiscovery we will keep current logic where the user provided white list is ANDed with block locations if ignoreLocality is False, or used as it is if ignoreLocality is True.
> 
> I expect that Splitter will not mention ignoreLocality.
> 
> FWIW i wanted to cal that "OverrideLocation" which would have been much more clear, people deploying the intial xrootd data federation wanted something which emphasized more the concept "Any data Anywhere Anytime".
> 
> Hope things are more clear now. We can talk about ignore locality on zoom this afternoon otherwise.

Wavelength adjusted! it much clearer now, let me digesting things and back to you this afternoon.

## Comment (cmsdmwmbot, 2025-07-03T10:38:37Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 30 warnings and errors that must be fixed
   * 5 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 358 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2517/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T09:30:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 30 warnings and errors that must be fixed
   * 5 warnings
   * 105 comments to review
 * Pycodestyle check: succeeded
   * 358 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2518/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T09:41:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 29 warnings and errors that must be fixed
   * 5 warnings
   * 103 comments to review
 * Pycodestyle check: succeeded
   * 356 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2519/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T09:57:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 350 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2520/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T10:07:45Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 19 warnings and errors that must be fixed
   * 5 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 350 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2521/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T11:12:49Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 5 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 350 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2522/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2025-07-07T12:27:46Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 5 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 349 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2523/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-07-08T14:25:16Z)

@belforte I've done with SiteInfoResolver TaskAction and ready for the review again. (Wishfully waiting for the green merge button... 🥲)

I will skipped refactoring **createSubDag** function for now because as i try myself (Also consulted with ChatGPT) it might not worth the efforts as you can see [1]. 

Will proceeding to testing more coverages as you mentioned e.g. splitting=automatic, bunch of * pattern... etc..

Regarding refactoring/clean up, In my PoV, It does reduced boilerplate, gave us a bit more clarity but the refactored function will not be use elsewhere yet, so it might not worth add more complication into this PR (Increases our risk of losing robustness), so it could be postpone as new cleanup issue. 
Would like to hear your thoughts around these.

[1]
```python
def resolve_available_sites(self, jobgroup, kwargs, global_blacklist, acceleratorsites, ignoreLocality, stage):
    jobs = jobgroup.getJobs()
    jgblocks = set()
    allblocks = set()

    for job in jobs:
        if stage == 'probe':
            random.shuffle(job['input_files'])
        for inputfile in job['input_files']:
            jgblocks.add(inputfile['block'])
            allblocks.add(inputfile['block'])

    self.logger.debug("Blocks: %s", list(jgblocks))

    if not jobs:
        locations = set()
    else:
        locations = set(jobs[0,'input_files',0,'locations'])
    self.logger.debug("Locations: %s", list(locations))

    if not locations and not ignoreLocality:
        return jgblocks, 'no_locations', locations

    if ignoreLocality:
        availablesites = kwargs['task','all_possible_processing_sites'] 
    else:
        availablesites = locations - global_blacklist

    self.logger.debug("Available sites: %s", list(availablesites))

    if kwargs['task','tm_activity'] in self.config.TaskWorker.ActivitiesToRunEverywhere and kwargs['task','tm_site_whitelist']:
        availablesites = set(kwargs['task','tm_site_whitelist'])

    if not availablesites:
        return jgblocks, 'banned_locations', locations

    if kwargs['task','tm_user_config','requireaccelerator']:
        availablesites &= acceleratorsites
        if availablesites:
            msg = f"Site.requireAccelerator is True. CRAB will restrict sites to run the jobs to {list(availablesites)}."
            self.logger.warning(msg)
            self.uploadWarning(msg, kwargs['task','user_proxy'], kwargs['task','tm_taskname'])
        else:
            return jgblocks, 'banned_locations', locations

    available = set(availablesites)
    siteWhitelist = set(kwargs['task','tm_site_whitelist'])
    siteBlacklist = set(kwargs['task','tm_site_blacklist'])

    if siteWhitelist:
        available &= siteWhitelist
        if not available:
            self._warn_user_skipped_blocks('whitelist', jgblocks, availablesites, kwargs)
            return jgblocks, 'banned_locations', locations

    available -= (siteBlacklist - siteWhitelist)
    if not available:
        self._warn_user_skipped_blocks('blacklist', jgblocks, availablesites, kwargs)
        return jgblocks, 'banned_locations', locations

    return jgblocks, 'ok', locations, availablesites


def _warn_user_skipped_blocks(self, reason, jgblocks, availablesites, kwargs):
    trimmedList = sorted(list(jgblocks))[:3] + ['...']
    if reason == 'whitelist':
        msg = f"{len(jgblocks)} block(s) {trimmedList} present at {list(availablesites)} will be skipped because those sites are not in user white list"
    else:
        msg = f"{len(jgblocks)} block(s) {trimmedList} present at {list(availablesites)} will be skipped because those sites are in user black list"
    self.logger.warning(msg)
    self.uploadWarning(msg, kwargs['task','user_proxy'], kwargs['task','tm_taskname'])
```

## Comment (belforte, 2025-07-08T16:33:01Z)

I am afraid that I do not understand your last comment. I do not see why we want ChatGpt involved and have no idea what that code snippet is, I failed to find `resolve_available_sites` in the change list, was I simply confused ? Also it looks like you did not define [1].

That said, form a look at changes I would say:
* there are some unrelated changes which are OK but should better be part of a differe "cleanup" PR, e.g. remove of 'envForCMSWEB` in PreDag.
* it seems that DBSDataDiscovery and other actions are modified only in order to pass ResourceCatalog to DataDiscovery. Why not put the call in there and leave the other actions alone ?
* why MakeFakeFileSet calls self.resourceCatalog.getAllPSNs() ? I thought you wanted to add the list of all possible sites to the task dictionary
* ~the handling of ignoreLocality in dagmanCreator is wrong, now you should assume that there is always a site white list.~  that was a misunderstanding on my side. Krittin explained in Zoom. Thanks

Overall I am confused, and suspect that you are too

## Comment (nausikt, 2025-07-09T09:37:55Z)

Thank you Stefano for your review and patience, Apologize for confusing you. please, let me try to clarify my last comment.

0. Regarding the ChatGPT snippet, I'm trying to convey that **IF** it were to be refactored, it might look something like that. However, the improved readability may not be worth the risk of losing robustness by overcomplicating this PR further at this stage. (** I'll will keep in mind not to flooding you with unnecessary details like that again.) 

**In Response to reviews:**

1. the removed of `envForCMSWEB` in PreDag. IIUC, we need to be within `envForCMSWEB` context only when we need to instantiate CRIC service instance. but in this PR we moved the instantiation to the beginning of handleNewTask, Handler instead. So IMHO, i think it would be great to keep changing here, get rid of `envForCMSWEB` to avoid further misleading on the necessity of it there.
      \>  should we stand on Keep changing (the removed of `envForCMSWEB`)? 

2. That's **TRUE** resourceCatalog could be instantiation inside DataDiscovery thus avoid unnecessary complication of passing down the args for all inherited classes.
      (P.S. At first thought, I got stuck with the idea of making CRICService as a singleton service that could be shared across the entire application)
      \> Now, I lean toward giving up on singleton service pattern and converging to your suggestion by double instantiation them to reduced unnecessary complications.

3. It would be great to be done that way, BUT there is one thing i really not sure about whether MakeFakeFileSet subtly need just plain full list of sites here? or the filtered from global_blacklist one is fine. Because the current `all_possible_processing_sites` saved list was *substracted* by global_blacklist beforehand.
      \> if the definition of `all_possible_processing_sites` is **_all processing sites not in blacklist_** and also applied to  MakeFakeFileSet context then It good to be used there as well thus we reduced the unnecessary of passing down resourceCatalog and also utilize `all_possible_processing_sites` more here.
 
4. I've no confident at all that i understand what's gone wrong here, could you please point me out via zoom chat please?

## Comment (belforte, 2025-07-09T15:28:19Z)

summary of zoom chat about 1. 2. 3. 4. in comment above:
1. `envForCMSWEB` is not needed anywhere anymore since a couple of years. Just a cleanup that was never done. Let's not mix with this
2. OK
3. it is fine to remove globally blacklisted sites from "all_psn" in the beginning of the task handling and only use what's left (i.e. sites which work) anywhere we want "all sites where we can submit)
4. Stefano misunderstood. All fine.

## Comment (cmsdmwmbot, 2025-07-10T07:45:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 18 warnings and errors that must be fixed
   * 5 warnings
   * 97 comments to review
 * Pycodestyle check: succeeded
   * 349 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2529/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2025-07-29T20:19:02Z)

This was migrated to https://github.com/dmwm/CRABServer/pull/9132.
