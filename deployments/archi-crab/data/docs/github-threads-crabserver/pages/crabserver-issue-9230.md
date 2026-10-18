# dmwm/CRABServer issue #9230: stop using `import htcondor` or `import classad` in "puppet"

State: closed
Opened: 2025-11-14T19:37:13Z
Closed: 2025-11-18T20:11:00Z
Labels: Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9230

## Opening post (belforte, 2025-11-14T19:37:13Z)

From HTC v25. onward only v2 API's are distributed.
The only supported way is:
```python
import htcondor2 as htcondor
import classad2 as classad
```

We have done this already for the code in this repository, but need to change a few files which
are installed on AP's via puppet and used in crontabs (some may even be old unused relics...)
So to avoid errors like the following one after we migrated vocms056 to HTC 25.0.3

<img width="568" height="220" alt="Image" src="https://github.com/user-attachments/assets/09a75b6b-8d9a-4fc8-8969-8de369935ad2" />

The list of files to change can be obtained e.g. like this
```console
 
LapSB:it-puppet-hostgroup-vocmsglidein$ rg "import htcondor"
code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb
136:## in every file to decide if to do "import htcondor" or "import htcondor2 as htcondor"

code/files/crabschedd/htcondor_ads.py
3:import htcondor

code/files/crabschedd/JobCleanup.py
25:import htcondor

code/files/crabschedd/check_maxdags.py
4:import htcondor

code/files/crabschedd/glexec_errors.py
4:import htcondor

code/files/crabschedd/jobhistoryfeeder.py
3:import htcondor
LapSB:it-puppet-hostgroup-vocmsglidein$ rg "import classad"
code/files/crabschedd/JobCleanup.py
26:import classad

code/files/crabschedd/jobhistoryfeeder.py
2:import classad
LapSB:it-puppet-hostgroup-vocmsglidein$ 

```

## Comment (nausikt, 2025-11-18T20:11:00Z)

Apologize for missing this issue notification, also extra delay today... Actually, this should be done in few minutes...

I've merged into `qa` as you can see [here](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/379), From now on there should be no surge of JobCleanUp failures emails coming to us, Thank you for your patience!

## Comment (nausikt, 2025-11-18T20:11:32Z)

Let me know if you need to promote this to `prod` any time.

## Comment (belforte, 2025-11-18T20:16:52Z)

yes, you should promote to prod, no reason not to. We are using V2 API everywhere

## Comment (nausikt, 2025-11-18T20:18:05Z)

Roger that Boss get it done now.

## Comment (belforte, 2025-11-18T20:22:18Z)

the problem was not the mails, was that the crontabs are not running so we would miss much needed disk cleanup when we move schedulers to HTC 25.
If you are not sure why we do things, ask. Sometimes I have bad ideas, I need critical review. And if I am right, still you need to learn how things work and mostly how to take ownership of things, even things which you understand only partially.

## Comment (nausikt, 2025-11-18T20:29:06Z)

Thanks man for emphasizing, Forgive me for my poor considered responses. So the critical things is disk SPOOL_DIR doesn't get clean-up as usual on every APs cause by centrally promoted HTC to v25 by SI team. and this enforcement fix things back to normal, including no alerts emails.

## Comment (nausikt, 2025-11-18T20:33:38Z)

So disk rising to more than 80% in some APs, are also part of this clean-up failures + surge of submissions workloads during this and last week, who accelerated the violation?

## Comment (belforte, 2025-11-18T20:35:50Z)

It is not SI which forces us to update HTCondor. It is the plain fact that we want to use the currently supported version with the best bug fixes and improvements. Also v25 has needed fixes for WMA so that they can use v2 API as well and it is good to run all schedd's with same version.

Disk usage rising above 80% is not due to lack of cleaning, is a worrying thing in itself. We usually live around 60% usage, which is OK. But do not have good handles to keep it under control.

## Comment (nausikt, 2025-11-18T20:37:25Z)

Thanks for clarity man. it's transparent now.

## Comment (belforte, 2025-11-18T20:39:05Z)

I do not know where exactly all that disk usage come from. We could consider things like compressing log files, or pushing them to S3... But I'd rather not introduce changes if we can avoid it
