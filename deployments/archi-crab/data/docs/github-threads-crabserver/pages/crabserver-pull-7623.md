# dmwm/CRABServer pull request #7623: jobwrapper - many small improvements

State: closed
Opened: 2023-04-28T17:02:17Z
Closed: 2023-05-16T10:50:51Z
Merged: 2023-05-16T10:50:51Z
URL: https://github.com/dmwm/CRABServer/pull/7623

## Opening post (mapellidario, 2023-04-28T17:02:17Z)

#### status

tested on test11

- [x] hammercloud https://cmsweb-test11.cern.ch/crabserver/ui/task/230428_162937%3Admapelli_crab_jobwr5_20230428_182936
- [x] montecarlo  https://cmsweb-test11.cern.ch/crabserver/ui/task/230428_164602%3Admapelli_crab_jobwr5_20230428_184559
- [x] retrieve logs of killed job: https://cmsweb-test11.cern.ch/crabserver/ui/task/230504_191507%3Admapelli_crab_jobwr5_20230504_211505

I propose to merge this PR, create a new tag and continue testing in testbed.

#### details

This PR gathers many small improvements to the jobwrapper. 

First of all, I propose change how we manage stdout+stderr of cmsRun / user script. Instead of keeping it in the Popen stdout (which is a pipe [1], and hence in memory), we redirect both stdout and stderr to the file `cmsRun-stdout.log.tmp`. This has two main advantages for CRAB. 

- We do not run out of memory if the job processes many events, as it can happen with automatic splitting on nanoaod. 
- We can to retrieve the stdout+err from cmsRun if it gets killed by the periodic removal 

We decided to buffer the stdout+stderr for up to one line. I am reluctant to buffer more than one line, I worry that it can cause stdout and stderr to go out of order with each other. I do not think it is necessary to turn off buffering. 

It is possible that writing often to the local disk can increase I/O and slow down execution. We will keep an eye out for this.

Secondly, I added some auxiliary functions to `gWMS-CMSRunAnalysis.py` that allow to check the content of the files where we keep information about the cmsRun execution (`cmsRun-stdout.log`, `FrameworkJobReport.xml`, ... ).

Thirdly, I added a trap on sigterm. Combined with the previous two addition, this allows to print the partial cmsRun stdout+stderr in case the job is gracefully killed by condor, for example due to a periodic removal policy. Before this PR, we would have lost stdout+stderr entirely, since at the moment it makes sense to run run `CMSRunAnalysis.py:logCMSSW()` only after the cmsRun execution finishes. We already have a way of intercepting the sigterm from condor [2],  but `CMSRunAnalysis.py:logCMSSW()` requires `cmsRun-stdout.log` to be present on disk (and before this PR we only write such file after the cmsRun completes), so even if condor sends a sigterm to all the child processes and we catch the sigterm in cmsrunanalysis.py, there is no file on disk to dump when the job is killed. This is still untested, as i did not managed yet to have my jobs killed by a periodic removal.

Lastly, I decided to stop using `jobReport.json.$CRAB_Id` for extracting the chirp exit code. I do not want condor_chirp to use python to parse a json. I do not want to rely on `gwms-python` to discover python for me. Moreover, on the remote nodes we do not have `jq` and I did not find a valid alternative to parse a json with pure bash. I'd rather create a new file `jobReport.exitCode.txt` that only contains the exit code, that chirp can read with a simple `cat`.

[1] https://github.com/dmwm/WMCore/blob/31d65166dc62c7251edd52890bc4ac2f0b79d7fe/src/python/WMCore/WMRuntime/Tools/Scram.py#L367
[2] https://github.com/dmwm/CRABServer/blob/3d7cb32e23e1b3c0da6fd2f93c7f646f093509a5/scripts/CMSRunAnalysis.py#L54
[] bash stdout and stderr: https://stackoverflow.com/a/16283739
[] https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html

---

Addendum

After reading [a.1], it is clear that dealing with termination signals does only depend on the receiving hand, it also depends on to which process the sigterm is sent to, whether only to the parent process or to the whole parent group.

In our case, we could catch the sigterm in cmsrunanalysis.py [a.2] only if condor sends a sigterm to all the processes in the `gWMS-CMSRunAnalysis.sh` group, for example. But this is not the default "send a sigterm" behavior. By default, only the parent process is killed, the child processes are killed independently only afterwards. As Stefano found, the condor docs are pretty vague [a.3].

In this PR, we could avoid writing `cmsRun-stdout.log.tmp` and only write to `cmsRun-stdout.log`, then hope that condor sends a sigterm to all the processes in the parent group id and let logCMSSW() print the cmsRun content. 

However, using traps in `gWMS-CMSRunAnalysis.sh` feels a bit more robust to changes on how condor kills our processes. I would keep this PR as it is now.

[a.1] https://www.baeldung.com/linux/signal-propagation 
[a.2] https://github.com/dmwm/CRABServer/blob/3d7cb32e23e1b3c0da6fd2f93c7f646f093509a5/scripts/CMSRunAnalysis.py#L54
[a.3] https://htcondor.readthedocs.io/en/latest/users-manual/priorities-and-preemption.html#details-about-how-htcondor-jobs-vacate-machines

## Comment (cmsdmwmbot, 2023-04-28T17:07:48Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1509/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-04-28T17:17:49Z)

> It is possible that writing often to the local disk can increase I/O and slow down execution. We will keep an eye out for this.

how ?

## Comment (belforte, 2023-05-02T15:18:06Z)

As a general comment, I got completely lost in the long discussion in the top comment. And II also have difficulties to connect it to the code changes. 
I suggest to move all the "why did I decided to do this" to some "footnote" and start with a terse description of the new behavior, in terms of what files get printed where.
IIUC the application stdout is redirected to some `.tmp` file and at some point that is `mv'ed` to the `non.tmp` version which is printed to stdout and so sent back. But it is not clear if I got it right, and when/under-which-condition things happen one way o the other.
If we do not take this chance to clarify in writing the relative role of `gWMS-CMSrunAnalysis.sh` `CMSRunAnalysis.sh` `CMSRunAnalysis.py` `cmscp.py` etc... we will never do.

## Comment (mapellidario, 2023-05-02T15:25:27Z)

I eventually managed to get my jobs killed: https://cmsweb-test11.cern.ch/crabserver/ui/task/230502_122418%3Admapelli_crab_jobwr5_20230502_142335

However, I overlooked something big. when a job is killed, the stdout of the job is lost, condor does not retrieve it the file, the file `Output = job_out.$(CRAB_Id)` is never created and the postjob can not run the function `handle_webdir()` . 

So far, I do not have any simple idea to get that stdout back...

## Comment (mapellidario, 2023-05-03T15:54:41Z)

##### Let's start with the bad news. 

I submitted a couple of tasks whose job were designed to be killed by condor, this time with more sane limits (thanks stefano for suggesting them)

- [230503_122305:dmapelli_crab_jobwr5_20230503_142302](https://cmsweb-test11.cern.ch/crabserver/ui/task/230503_122305%3Admapelli_crab_jobwr5_20230503_142302): runtime limited at 10min
- [230503_122155:dmapelli_crab_jobwr5_20230503_142153](https://cmsweb-test11.cern.ch/crabserver/ui/task/230503_122155%3Admapelli_crab_jobwr5_20230503_142153). ram limited to 700MB, runtime limited to 5min.

Then i submitted a task and manually run condor_rm on one of the jobs

- [230503_121933:dmapelli_crab_jobwr5_20230503_141930](https://cmsweb-test11.cern.ch/crabserver/ui/task/230503_121933:dmapelli_crab_jobwr5_20230503_141930)
  - job 1 killed at 14.27 cern time, at least 5min after i saw the job running from the schedd.

In all the cases above, when jobs are been killed the stdout is lost. I also had a chat with Nikos and he as well is not sure how to get the stdout of a job that is killed. 

At this point it feels like we need to implement some new feature to preserve the stdout of a job that is about to be killed. I am not sure it is worth doing it now, maybe one of the questions that we can add to the long list for our summer student is "how often are jobs killed by the periodic removal?", so that we can gauge if the effort is worth.

#### on a more positive note

I run some jobs on lxplus with preparelocal. After adding to the script run_job.sh the same functions that I added to `gWMS-...`, I made sure that they work as expcted. So I think we should be able to detect termination signals sent to our job, which means that the prerequisites for further development are there. 

I will attach some tests.

<details><summary>1. killed the job with ctrl c</summary>

```plaintext
==== CMSSW JOB Execution started at Wed May  3 10:55:16 2023 ====
^CTraceback (most recent call last):
  File "CMSRunAnalysis.py", line 649, in <module>
    applicationExitCode = executeUserApplication(cmd, scram, cleanEnv=False)
  File "CMSRunAnalysis.py", line 438, in executeUserApplication
    ret = scram(command, runtimeDir=os.getcwd(), cleanEnv=cleanEnv)
  File "/afs/cern.ch/user/d/dmapelli/crab/jobruntime/crab_jobwr5_20230502_145819.0/WMCore.zip/WMCore/WMRuntime/Tools/Scram.py", line 422, in __call__
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/subprocess.py", line 1024, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/subprocess.py", line 1866, in _communicate
    ready = selector.select(timeout)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/selectors.py", line 415, in select
    fd_event_list = self._selector.poll(timeout)
KeyboardInterrupt
The job received a termination signal:  INT
the file cmsRun-stdout.log.tmp exists
the file cmsRun-stdout.log.tmp is non-empty. wc (newlines, words, bytes):  11 38 521 cmsRun-stdout.log.tmp
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp] **************************************************************
[cmsRun-stdout.log.tmp] Geant4 version Name: geant4-10-07-patch-02 [MT]   (11-June-2021)
[cmsRun-stdout.log.tmp] << in Multi-threaded mode >>
[cmsRun-stdout.log.tmp] Copyright : Geant4 Collaboration
[cmsRun-stdout.log.tmp] References : NIM A 506 (2003), 250-303
[cmsRun-stdout.log.tmp] : IEEE-TNS 53 (2006), 270-278
[cmsRun-stdout.log.tmp] : NIM A 835 (2016), 186-225
[cmsRun-stdout.log.tmp] WWW : http://geant4.org/
[cmsRun-stdout.log.tmp] **************************************************************
[cmsRun-stdout.log.tmp]
```

</details>

2. kill -s term only on the pid of  run_job.sh: nothing happens

<details><summary>3. kill -s term on run_job.sh and all its descendant processes</summary>

when cmsRun is running we have

```plaintext
> [12:42] lxplus908 crab_jobwr5_20230502_145819.0
> ps ufx
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
dmapelli  704519  0.0  0.0  21132  8392 pts/6    Ss   11:38   0:00 -zsh
dmapelli  720954  0.0  0.0   7256  3916 pts/6    S    12:21   0:00  \_ /bin/bash -e /cvmfs/cms.cern.ch/common/cmssw-el8
dmapelli  721190  0.0  0.1 1185540 32524 pts/6   Sl   12:21   0:00      \_ Apptainer runtime parent
dmapelli  721208  0.0  0.0  13004  3304 pts/6    S    12:21   0:00          \_ /usr/bin/sh -c [ "el9_amd64" != "$(/cvmfs/cms.c
dmapelli  721265  0.0  0.0  22624  4464 pts/6    S    12:21   0:00              \_ /bin/bash
dmapelli  724677  0.0  0.0  12984  3240 pts/6    S+   12:41   0:00                  \_ bash run_job.sh 1
dmapelli  724703  0.1  0.0  13264  3676 pts/6    S+   12:41   0:00                      \_ /bin/bash ./CMSRunAnalysis.sh -a sa
dmapelli  724770  5.6  0.0  37316 22280 pts/6    S+   12:41   0:00                          \_ python3 CMSRunAnalysis.py -r /a
dmapelli  724938  1.6  0.0  13012  3248 pts/6    S+   12:42   0:00                              \_ /bin/bash
dmapelli  724939 19.3  0.3 245832 105368 pts/6   D+   12:42   0:00                                  \_ cmsRun -p PSet.py -j Fr
```

then i killed run_job.sh and all its descendant processes

```plaintext
> [12:42] lxplus908 crab_jobwr5_20230502_145819.0
> kill -s term -- -724677
```

the result was

```plaintext
> [12:42] lxplus908 crab_jobwr5_20230502_145819.0
> ps ufx
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
dmapelli  704519  0.0  0.0  21132  8392 pts/6    Ss   11:38   0:00 -zsh
dmapelli  720954  0.0  0.0   7256  3916 pts/6    S    12:21   0:00  \_ /bin/bash -e /cvmfs/cms.cern.ch/common/cmssw-el8
dmapelli  721190  0.0  0.1 1185540 32524 pts/6   Sl   12:21   0:00      \_ Apptainer runtime parent
dmapelli  721208  0.0  0.0  13004  3304 pts/6    S    12:21   0:00          \_ /usr/bin/sh -c [ "el9_amd64" != "$(/cvmfs/cms.c
dmapelli  724939 37.9  2.7 1386612 827896 pts/6  tl   12:42   0:09 cmsRun -p PSet.py -j FrameworkJobReport.xml
dmapelli  725053  0.0  0.0  14660  3400 pts/6    S    12:42   0:00  \_ (CMSSW stack trace helper) -c date; gdb -quiet -p 72493
dmapelli  725065  0.0  0.0  12536  3212 pts/6    S    12:42   0:00      \_ /bin/bash /cvmfs/cms.cern.ch/el8_amd64_gcc10/cms/cm
dmapelli  725072  305  6.3 2440576 1885540 pts/6 Rl   12:42   0:24      |   \_ gdb-10.2 -quiet -p 724939
dmapelli  725066  0.0  0.0  15772  1180 pts/6    S    12:42   0:00      \_ /bin/sed -n -e s/^\((gdb) \)*// -e /^#/p -e /^Threa

```

and after around one minute the cmssw stacktrace ends.

On the stdout I got

```plaintext
==== CMSSW JOB Execution started at Wed May  3 10:42:04 2023 ====
ERROR: Caught Wrapper ExecutionFailure - detail =
sighandler() takes 1 positional argument but 2 were given
Terminated
Sanitize FJR
The job received a termination signal:  TERM
the file cmsRun-stdout.log.tmp exists
the file cmsRun-stdout.log.tmp is non-empty. wc (newlines, words, bytes):  16 59 658 cmsRun-stdout.log.tmp

ERROR: Exceptional exit at Wed May  3 10:42:20 2023 (10040): sighandler() takes 1 positional argument but 2 were given
ERROR: Traceback follows:
 Traceback (most recent call last):
  File "CMSRunAnalysis.py", line 649, in <module>
    applicationExitCode = executeUserApplication(cmd, scram, cleanEnv=False)
  File "CMSRunAnalysis.py", line 438, in executeUserApplication
    ret = scram(command, runtimeDir=os.getcwd(), cleanEnv=cleanEnv)
  File "/afs/cern.ch/user/d/dmapelli/crab/jobruntime/crab_jobwr5_20230502_145819.0/WMCore.zip/WMCore/WMRuntime/Tools/Scram.py", line 422, in __call__
    self.stdout, self.stderr = proc.communicate()
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/subprocess.py", line 1024, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/subprocess.py", line 1866, in _communicate
    ready = selector.select(timeout)
  File "/cvmfs/cms.cern.ch/COMP/slc7_amd64_gcc630/external/python3/3.8.2-comp/lib/python3.8/selectors.py", line 415, in select
    fd_event_list = self._selector.poll(timeout)
TypeError: sighandler() takes 1 positional argument but 2 were given

== Execution site for failed job from site-local-config.xml: T2_CH_CERN
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp] **************************************************************
[cmsRun-stdout.log.tmp] Geant4 version Name: geant4-10-07-patch-02 [MT]   (11-June-2021)
[cmsRun-stdout.log.tmp] << in Multi-threaded mode >>
[cmsRun-stdout.log.tmp] Copyright : Geant4 Collaboration
[cmsRun-stdout.log.tmp] References : NIM A 506 (2003), 250-303
[cmsRun-stdout.log.tmp] : IEEE-TNS 53 (2006), 270-278
[cmsRun-stdout.log.tmp] : NIM A 835 (2016), 186-225
[cmsRun-stdout.log.tmp] WWW : http://geant4.org/
[cmsRun-stdout.log.tmp] **************************************************************
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp] A fatal system signal has occurred: external termination request
[cmsRun-stdout.log.tmp] The following is the call stack containing the origin of the signal.
[cmsRun-stdout.log.tmp]
[cmsRun-stdout.log.tmp] Wed May  3 12:42:20 CEST 2023

Singularity>
```

</details>

## Comment (belforte, 2023-05-03T17:01:58Z)

@mapellidario can you be specific about "stdout is lost" ? Do you mean that the cmsRun stdout is not captured, or that the full job stdout is missimg ? I do not have example at hand, but we have ample evidence of jobs killed by periodic remove for which condor did bring back the job output, as we specify in the classAd. So I am also confuse what exactly you asked to Nikos and what he said
https://github.com/dmwm/CRABServer/blob/29619d6bfc8b7808ac7d4e2ef83dbbea65e0deb0/src/python/TaskWorker/Actions/DagmanCreator.py#L121-L127

## Comment (mapellidario, 2023-05-03T17:05:54Z)

Aha! I will have a look at what the options you linked do.

What I mean is that in all the tests I did, the job log on the schedd says "the postjob has not processed the job output". 

Maybe something is wrong with the config of my tasks

## Comment (belforte, 2023-05-03T17:10:07Z)

I know what you mean, that's the same that I saw in your task which failed after very short time due to very low memory limit and I thought it was that limit to cause this.
But for sure we both have seen user jobs with exit code 50660/4 and a proper stdout, simply w/o the CMSSW part.

Please do not waste time looking up condor manuals, and trust the work which we did years ago. This thing works. Stdout/err of evicted jobs are usually returned.

## Comment (mapellidario, 2023-05-04T12:53:20Z)

UH! on production we do have our job stdout indeed! see the task [1].

Ok, now i need to start the bug hunting.


[1] https://cmsweb.cern.ch/crabserver/ui/task/230504_104540%3Admapelli_crab_jobwr5_20230504_124537 , 3 jobs killed because of walltime limit set to 10min.

## Comment (cmsdmwmbot, 2023-05-04T19:21:32Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1514/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-05-04T19:37:32Z)

Aha! It was the traps not doing what i expected all along! I removed the traps, and "replaced" them with always looking for `cmsRun-stdout.log.tmp` and print its content if it is there [2] (I renamed the argument `debug` of `check_file_exist` with `printfile`, sounds a bit better).

See task [1]. I manually killed with condor_rm job 1 after a few minutes, and let job 2 being killed by periodic removal after 10m.

Tomorrow I will try to make this PR more comprehensible and run some more tests, but so far so good :)

---

[1] https://cmsweb-test11.cern.ch/crabserver/ui/task/230504_191507%3Admapelli_crab_jobwr5_20230504_211505
[2]

```bash
    check_file_exist cmsRun-stdout.log.tmp DUMMY printfile
    check_file_exist cmsRun-stdout.log DUMMY
```

## Comment (mapellidario, 2023-05-12T10:04:52Z)

#### conclusion

Thank you Stefano, `print_line` adds a significant overhead. I will remove it

#### experiment

I created a script with only the `print_file` function and executed it on the output of [1]. Then I run the script twice, 

- I set `keepAtStart=500`, `keepAtEnd=500`, `maxLineLen=30`, processing a file with 10k lines, 10k characters each line.
- `time print_file test.txt` takes 9s
- I used PS4, suggested at [2]
    ```bash
    set -x
    PS4='+ $(date "+%s.%N ($LINENO) ")'
    time print_file test1.txt
    ```
    in total it takes 12s (this has a 30% overhead, but allows to compute the time taken by each command). It shows that every execution of `read line` takes 7ms, then awk takes 4ms to 5ms.
- accounting for the overhead of PS4, we can estimate that for every line that we want to print `read line` takes 5ms and awk 3ms
- I repeated the experiment with shorter lines. `read line` takes less time, but awk still takes at least 2ms

Without executing `print_line` the script takes 0.4s **in total**.

#### Analysis

- if we do not use `print_line`, we can expect that printing 1000 lines takes about 0.5s (on an ssd) (0.5ms each line)
- if we use `print_line`, every line that we print "costs" at least 2ms (fixed, because of awk) and 1ms for every 1000 characters in the line (because of `read line`).

---

[1] `cat /dev/urandom | tr -dc 'A-Za-z0-9' | fold -w 10000 | head -n 10000 | pv > ./test1.txt`
test1.txt contains 10k lines of 10k characters each.

[2] https://stackoverflow.com/a/4338046

## Comment (cmsdmwmbot, 2023-05-12T11:33:50Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 32 warnings and errors that must be fixed
   * 14 warnings
   * 128 comments to review
 * Pycodestyle check: succeeded
   * 78 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1515/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-05-12T15:29:56Z)

I looked at code now and it looks fine.
Maybe some `echo` too many, but that's OK.

## Comment (mapellidario, 2023-05-16T10:50:24Z)

After private discussion, we agreed to merge this, create a new tag, deploy in preprod and test it for a few days
