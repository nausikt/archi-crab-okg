# dmwm/CRABServer issue #7542: condor_chirp - summary of current problems

State: closed
Opened: 2023-02-17T17:37:49Z
Closed: 2024-08-23T10:57:05Z
Labels: Type: Bug, Priority: Medium, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7542

## Opening post (mapellidario, 2023-02-17T17:37:49Z)

### What happens, brief

We have problems with condor_chirp both in production and with the new jobwrapper. I am still not sure if the two are not correlated and I think that my investigation for the new jobwrapper can help with current production problems.

fyi: @belforte @mmascher @novicecpp 

##### production

Stefano noticed two similar errors with condor_chirp in production jobs running in slc6 that failed [1].
condor_chirp does not seem to have problems with jobs that finish successfully in production [2]

The current code that we run in production is [3].

##### new jobwrapper

While debugging https://github.com/dmwm/CRABServer/pull/7510 I came across a similar error and made some investigations.

With el8 and cc7 everything works. With scl6 I'm having some troubles.

### Cause of the problem (as far as i understand it)

I think all boils down to which python version is selected by `gwms-python`. When it selects py2.6, condor_chirp fails. This happens also in production when a job fails. When it selects python >= 2.7 everything is ok.

### what can we do in CRAB?

I think we have a couple of options:

a. Merge the PR https://github.com/dmwm/CRABServer/pull/7510 as is now (we use `gwms-python` for parsing the json with the exit code)
  - this will make all the jobs running in slc6 to have a wrong `Chirp_CRAB3_Job_ExitCode` until we manage to make gwms-python can select python >=2.7 (maybe from comp?). This can be done in crab or in gwms.
  - the regression with current production will not be great. the exit code from condor_chirp is already broken in production with jobs that fail, we will temporarily break it also for successful jobs
  - This would be the only problem that I know of with the new jobwrapper, it does not seem to affect many users and will be like this only until we find a fix

b. Change crab code in https://github.com/dmwm/CRABServer/pull/7510 so that we force gwms-python to select a comp python >=2.7.
  - ~~I am still not sure how to do it, it will postpone the release of jobwrapper yet again~~
  - This seems reasonably simple, see comment below

~~I think that the pressure to push the jobwrapper onwards is greater than having condor_chirp exit code correct for only a small fraction of jobs.~~

~~Stefano, would you be ok to introduce temporarily a small regression to relieve us from the stress of not having the new jobwrapper in production?~~

Stefano, I would ask you still one more day to improve #7510 to fix this, then I will be ok deploying the new  jobwrapper to production.

Marco, do you think that you can do anything with gwms-python on gwms side? Or do you think that it would be easier to force it to select python 2.7 in CRAB land? I mean, if we are the only ones encountering this problem it may be easier to deal with it ourselves.

Please, notice that even if we change in #7510 the code that parses the json with the exit code from using python to something in bash/grep [4], condor_chirp will still use gwms-python and have problems with all slc6 jobs.

### what happens, long

I run many tests:

- multiple cmssw version
- multiple OS
- letting jobs finish correctly and killing them by setting a very short max runtime
- changing the env where condor_chirp is called
   1. leaving the env as is at the end of the job (current code in #7510), or
   2. sourcing the startup environment just before running condor_chirp. (which would be the same as using `cleanEnv=True`). You can appreciate the difference between these cases in the logs by looking at the pythonpath just before condor_chirp runs. This is achieved by running `.  $JOBSTARTDIR/startup_environment.sh` just before running condor_chirp. This file should already be present in current production [4], but with the new jobwrapper it is more complete and trustworthy [5].

If the information that follows is not enough, I can quickly run some more tests. I am used to it at this point and can quickly test anything you want

##### production

I managed to replicate on test11 what we see in production, running a task [230217_155816:dmapelli_crab_20230217_165813](https://cmsweb-test11.cern.ch/crabserver/ui/task/230217_155816:dmapelli_crab_20230217_165813) where i forced the job failure. In this case, test11 code is the same as production with some debugging added just before running condor_chirp [6] .

- [job_out.1.0.txt](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230217_155816:dmapelli_crab_20230217_165813/job_out.1.0.txt) (job retried because "removed due to wall clock time limit"). slc6, cmssw 7, job ok, gwms-python 2.7.13, condor_chirp ok ✅
- [job_out.1.1.txt](https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230217_155816:dmapelli_crab_20230217_165813/job_out.1.1.txt). slc6, cmssw 7, job failed, gwms-python 2.6.6, condor_chirp failed 🚫

So: gwms-python tends to select py2.7 from COMP, unless something goes wrong (for example on job failures) and it selects py2.6

##### new jobwrapper

the most results notable are

- task [230217_141417...](https://cmsweb-test11.cern.ch/crabserver/ui/task/230217_141417:dmapelli_crab_20230217_151412). slc6, cmssw7 , job ok, leave env as is, `gwsm-python` points to 2.6.6: condor_chirp failed 🚫

- task [230217_143047...](https://cmsweb-test11.cern.ch/crabserver/ui/task/230217_143047:dmapelli_crab_20230217_153045). slc6, cmssw 7, job ok, sourced container startup environment, `gwsm-python` points to 2.6.6: condor_chirp failed 🚫

The new jobwrapper always use a COMP environment with py3, also on slc6. gwms-python seem to prefer py2, there is no py2.7 from comp, it only finds the system python, which is py2.6 and is too old for condor_chirp. 

---

[1]

- slc6, cmssw 9, job failed with 8028: https://cmsweb.cern.ch:8443/scheddmon/0194/byates/230215_164126:byates_crab_MC13TeV_2016_TTJets_psweights/job_out.2.2.txt

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 8028 ====
/usr/bin/python: htchirp is a package and cannot be directly executed
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 1 ========
```

- slc6, cmssw 7, job failed with 10034: https://cmsweb.cern.ch:8443/scheddmon/0107/sandhya/230216_091629:sandhya_crab_20230216_101618/job_out.788.1.txt

[2] slc6, cmssw 9, job ok: https://cmsweb.cern.ch:8443/scheddmon/0194/byates/230215_164126:byates_crab_MC13TeV_2016_TTJets_psweights/job_out.20.0.txt

[3] crabserver, the version that we are currently running in production https://github.com/dmwm/CRABServer/blob/8a048d18ce07bb2487786bbec09c66d7e0d35a61/scripts/gWMS-CMSRunAnalysis.sh

[4] https://github.com/dmwm/CRABServer/blob/1a4d80d610b6f9cab65580946e3bf0cb5fa07920/scripts/gWMS-CMSRunAnalysis.sh#L56-L62

[5]

```plaintext
set > startup_environment.sh
sed -e 's/^/export /' startup_environment.sh > tmp_env.sh
mv tmp_env.sh startup_environment.sh
```

[6] `declare -p > startup_environment.sh`

[7] https://github.com/dmwm/CRABServer/compare/v3.221124...mapellidario:20230215_jobwr_dbg_1

## Comment (mapellidario, 2023-02-17T17:54:01Z)

i can confirm that by sourcing a py2.7 COMP environment just before running condor_chirp in `gWMS-.. .sh`  [1], then condor_chirp works as expected even with a successful slc6 job using the new jobwrapper [2].

I do not have more time today, I can come back to this issue on monday, but I think I can update #7510 with a switch. If I detect an slc6 OS, I source py2.7 from COMP before running condor chirp.

Sorry for the noise, I am still open to better suggestions.

And sorry if it took almost a whole week to debug the problem :sob: 

[1]

```diff
+   .  /cvmfs/cms.cern.ch/COMP/slc6_amd64_gcc493/external/py2-future/0.18.2/etc/profile.d/init.sh
    #check if the command condor_chirp exists
    command -v condor_chirp > /dev/null 2>&1
```

[2] https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230217_174333:dmapelli_crab_20230217_184329/job_out.2.0.txt

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

## Comment (belforte, 2023-02-19T11:57:22Z)

thanks Dario for thorough investigation,
but I beg to disagree with your approach here, possibly because I am simply lost in this long list of tests.
I would rather approach this as:
1. you can't solve all world's problems
2. what exactly is failing at this point  ? If is only chirping of the job exit code when running on SL6 ... well, so be it and move on with life. Did you look at the fraction of jobs which use SL6 ? [1]
3. anyhow first thing is to test `condor_chirp` in the startup environment: does it work there ? 
  * YES: ok, go to 2.
  * NO: hand it to SI (it is not our task to decide where they find python in the containers that they start and by attempting to do it we risk overlooking something, as Marco indicated pilots are common to CMS and other VO's). 

I fear that you have spent more time already in this then it makes sense.

Rather, as discussed already, we should really avoid calling python inside "chirp the exit code" and do the FJR parsing before we leave the python env. or "prase in bash". Best thing IMHO is that when that FJR is created, the exit code is saved in a file.

And in the spirit of "JobWrapper restructuring using COMP env from /cvmfs" (a real nice thing which we did not have when the current wrapper was written), move execution of cmscp.py inside its own wrapper  so that gWMS-CMSRunAnalysis.sh has no "python discovery" in it .

I believe in "simplify our wrapper and unify differenr implementation of same functionalities" more than in "solving all those odd problems which occupy 1/10^6 of the phase space while still taking a large fraction of our time".

[1] last year from [2]
![image](https://user-images.githubusercontent.com/1837785/219945744-7c80afd3-57c2-4dd8-bc63-7be37d74f230.png)
[2] https://monit-grafana.cern.ch/goto/n5WR0s1Vz?orgId=11

## Comment (mapellidario, 2023-02-20T12:20:23Z)

> Rather, as discussed already, we should really avoid calling python inside "chirp the exit code" and do the FJR parsing before we leave the python env. or "prase in bash". Best thing IMHO is that when that FJR is created, the exit code is saved in a file.

Ok, but you still want to call condor_chirp at the very end? because condor_chirp is bash script that wraps `gwms-python -m htchirp` [1], so if we dont fix gwms-python, it doesnt matter how we extract the exit code from the FJR, we still can not use condor_chirp to add it to the classads.

> test condor_chirp in the startup environment

when the container is SLC6, it does not work. SLC6 container ships py2.6, which condor_chirp is not compatible with.

We have not noticed it in production before now because gwms-python found py2.7 from COMP instead.

> If is only chirping of the job exit code when running on SL6 ... well, so be it and move on with life

Good! :)

> Did you look at the fraction of jobs which use SL6 ?

Yes, they are not many, about 1%.

SCRAM_ARCH in CRAB jobs last month (source [2], exported to csv and aggregated on a spreadsheet):

```plaintext
arch | fraction
-----|---------
el8  | 0.015
slc7 | 0.97
slc6 | 0.012
```

CMSSWMajorVersion when using `slc6*` (source [3]):

```
version | Count  | fraction
--------|--------|---------
8_X_X   | 122718 | 0.70537
10_X_X  | 37682  | 0.21659
9_X_X   | 10444  | 0.06003
7_X_X   | 3132   | 0.01800
```

I had to use opensearch because on grafana I could only group by CMSSWMajorVersion [4], not for scram_arch as well.

> I believe in "simplify our wrapper and unify differenr implementation of same functionalities" more than in "solving all those odd problems which occupy 1/10^6 of the phase space while still taking a large fraction of our time".

I know, I know, I know. :)

---

[1] https://github.com/glideinWMS/glideinwms/blob/8cedeaff71e692d53c6a27e8c63dfc334432371b/creation/web_base/condor_chirp#L21

[2] https://monit-opensearch.cern.ch/dashboards/goto/71c65475a4d31f87ce74a5e0b6b0d1b0?security_tenant=global

[3] https://monit-opensearch.cern.ch/dashboards/goto/e815a89ec7bfe0f9ca701c974a76a8d3?security_tenant=global

[4] https://monit-grafana.cern.ch/goto/mCFni_1Vk?orgId=11

## Comment (belforte, 2023-02-20T12:36:22Z)

fixing `gwm-python` on SL6 is not something we can do, even if we knew how.  But we should not use `gwms-python` in our code. Exactly because it is out of CMS control and it may change at any time (even disapper) based on wat gwms developers do.

## Comment (belforte, 2024-08-23T10:57:05Z)

rare enough and hopefully use or SLC6 going down enough that we do not worry
