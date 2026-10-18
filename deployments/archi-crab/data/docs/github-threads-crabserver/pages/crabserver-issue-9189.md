# dmwm/CRABServer issue #9189: stop using PostJobPrio1,2

State: closed
Opened: 2025-09-19T12:00:17Z
Closed: 2025-09-26T08:03:11Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9189

## Opening post (belforte, 2025-09-19T12:00:17Z)

as discussed with Jamie, in preparation of future deprecation and to simplify our code

On 19/09/2025 13:51, Stefano Belforte wrote:
>
> here's original motivation and "blame target"
>  https://github.com/dmwm/CRABServer/commit/56b0297a1ca394cc2d0f238a3e6775b3295f5e76
>
>
> So it was some kind of cake frosting which we can surely do w/o
>
> based on experience. For peace of mind I will remove it from the code.
>
> Stefano
>
>
>
> On 19/09/2025 13:44, Stefano Belforte wrote:
>>
>> CRAB uses PostJobPrio1 and PostJobPrio2. It has been there since ever
>> and I can't say off the top of my head what it does for us and why is there.
>> Which makes me thing that nothing will break if it is taken away.
>> I will did a bit.
>>
>> Stefano
>>
>>
>> On 19/09/2025 12:20, Marco Mascheroni wrote:
>>> Thanks a lot Jamie! Tier0 jobs all belong to the same user and Tier0 has its own accounting group. so I think we have what we need with USE_GLOBAL_JOB_PRIOS=True
>>>
>>> >  CMS uses PostJobPrio1 and PostJobPrio2. I’m unaware of anyone else who uses the Pre or Post attributes. If we wanted to remove the Pre and Post attributes, would it be feasible for CMS to adjust to using just JobPrio?
>>>
>>> I think this is a question for the WMCore team:
>>>
>>> https://github.com/dmwm/WMCore/blob/904ab737b46f4f0bbfcf3de48bfa4b21b8c4d612/src/python/WMCore/BossAir/Plugins/SimpleCondorPlugin.py#L650-L651
>>>
>>> Alan, how much is the PostJobPrio used? 
>>>
>>> Jamie, can the JobPrio be an expression? Or better, has anybody ever used an expression for the JobPrio?
>>>
>>> From: Jaime Frey [<jfrey@cs.wisc.edu>](mailto:jfrey@cs.wisc.edu)
>>> Sent: Thursday, September 18, 2025 17:40
>>> To: Florian Von Cube [<ralf.florian.von.cube@cern.ch>](mailto:ralf.florian.von.cube@cern.ch)
>>> Cc: Marco Mascheroni [<marco.mascheroni@cern.ch>](mailto:marco.mascheroni@cern.ch); Antonio Linares Sancho [<a.linares@cern.ch>](mailto:a.linares@cern.ch); Jan Eysermans [<jan.eysermans@cern.ch>](mailto:jan.eysermans@cern.ch); CMS Submission Infrastructure [<cms.submission.infrastructure@cern.ch>](mailto:cms.submission.infrastructure@cern.ch)
>>> Subject: Re: Question about job priority and schedd ordering in HTCondor
>>>  
>>> I can fill in some details that the summary linked below leaves out.
>>> First, there are two types of priority. One is user priority, which influences how the pool’s slots are divided between multiple submitters. A smaller numerical value is better. This value is maintained by the negotiator and you can see it with condor_userprio. The other is job priority, which influences which jobs are matched first for a given submitter. A larger numerical value is better. This value is in the job ClassAd in the schedd and the user can set it however they want in the submit file or with condor_prio.
>>>
>>> Second, if you’re using accounting groups with hierarchical group quotas, then submitters in accounting groups are considered first, with the submitters who are furtherest below their quota going first. Within an accounting group and among submitters not in an accounting group, the submitter with the best user priority is considered first by the negotiator.
>>>
>>> When a submitter has jobs on multiple schedds, the negotiator will talk with one schedd at a time in an undefined order. Each schedd will send idle jobs (actually resource requests clumped by autocluster) to the negotiator in job priority order.
>>>
>>> If you set USE_GLOBAL_JOB_PRIOS=True for your negotiator (which the CMS global pool does), that changes how the negotiator talks to the schedds for a given submitter. The negotiator will first talk to the schedd that has the job with the best job priority for that submitter and ask for more jobs to match until another schedd has the job with the best job priority (which hasn’t been considered yet in the current cycle). The negotiator then talks to that schedd. This switching back and forth between multiple schedds adds overhead to the negotiation cycle, so it’s disabled by default.
>>>
>>> And one final note and question about job priority. A job’s job priority is actually 5-value tuple, given by the attributes PreJobPrio1, PreJobPrio2, JobPrio, PostJobPrio1, and PostJobPrio2. The Pre and Post attributes are almost completely undocumented. CMS uses PostJobPrio1 and PostJobPrio2. I’m unaware of anyone else who uses the Pre or Post attributes. If we wanted to remove the Pre and Post attributes, would it be feasible for CMS to adjust to using just JobPrio?
>>>
>>>  - Jaime
>>>
>>> > On Sep 18, 2025, at 5:20 AM, Florian Von Cube [<ralf.florian.von.cube@cern.ch>](mailto:ralf.florian.von.cube@cern.ch) wrote:
>>> >
>>> > Hi all, just to add:
>>> >
>>> > I think the description of the negotiation cycle is now found here:
>>> >[ https://urldefense.com/v3/__https://htcondor.readthedocs.io/en/latest/admin-manual/cm-configuration.html*the-negotiation-cycle__;Iw!!Mak6IKo!L7b6XmRPZcQW1gdsNa1vs9xHWXlmnwMxNvqVRaxrbGpUxBYGdnnMQAPWNlVJaivtbMJFWMUXI5HXWLeeEDJgT3XJYgLlLA$](https://urldefense.com/v3/__https://htcondor.readthedocs.io/en/latest/admin-manual/cm-configuration.html*the-negotiation-cycle__;Iw!!Mak6IKo!L7b6XmRPZcQW1gdsNa1vs9xHWXlmnwMxNvqVRaxrbGpUxBYGdnnMQAPWNlVJaivtbMJFWMUXI5HXWLeeEDJgT3XJYgLlLA$)
>>> >
>>> > It states “Fetch an idle job from a condor_schedd holding jobs from that submitter.”, but doesn’t specify how exactly the schedd and job is chosen.
>>> >
>>> > Cheers,
>>> >  Florian
>>> >
>>> >> On 18 Sep 2025, at 10:27, Marco Mascheroni [<marco.mascheroni@cern.ch>](mailto:marco.mascheroni@cern.ch) wrote:
>>> >>
>>> >> Hi Jamie,
>>> >> There has been some concern about the following sentence in the 23.0 HTCondor manual:
>>> >> “With jobs from a single condor_schedd daemon, jobs are typically returned in job priority order. When more than one condor_schedd daemon is involved, they are contacted in an undefined order. All jobs from a single condor_schedd daemon are considered before moving on to the next.”
>>> >> I didn’t find the same text in the "latest" manual:
>>> >>[ https://urldefense.com/v3/__https://htcondor.readthedocs.io/en/23.0/admin-manual/user-priorities-negotiation.html*negotiation__;Iw!!Mak6IKo!L7b6XmRPZcQW1gdsNa1vs9xHWXlmnwMxNvqVRaxrbGpUxBYGdnnMQAPWNlVJaivtbMJFWMUXI5HXWLeeEDJgT3WVzOvzXQ$](https://urldefense.com/v3/__https://htcondor.readthedocs.io/en/23.0/admin-manual/user-priorities-negotiation.html*negotiation__;Iw!!Mak6IKo!L7b6XmRPZcQW1gdsNa1vs9xHWXlmnwMxNvqVRaxrbGpUxBYGdnnMQAPWNlVJaivtbMJFWMUXI5HXWLeeEDJgT3WVzOvzXQ$)
>>> >> Could you clarify whether the concept of priority is "global" in HTCondor? I’m wondering:
>>> >>    • Are slots/claims handed out in priority order across schedds during a negotiation cycle?
>>> >>    • Or does the negotiator loop scheduler by scheduler?
>>> >> My understanding is that only once claims (slots) are handed over to schedulers, priority becomes "local." But since we setCLAIM_WORKLIFE = 1200, that shouldn’t have a big effect.
>>> >> From the logs it seems that (1) is true, but from the documentation it seems (2) is true. Could you clarify?
>>> >> Thanks,
>>> >> Marco
>>> >
>>> >
>>>

## Comment (belforte, 2025-09-22T13:29:27Z)

for "hystory", more comments from the follow up in that mail thread

* 
On 19/09/2025 14:46, Stefano Belforte wrote:
> thanks Brian, wow, you are so quick and alert !!
>
> So about those two point:
>
> 1. this is prioritization non inside a task (where any job is the same), but across them,
>  we'd need at least JobPrio  or even better go in front of other users, which is a different story
> 2. I know, but day-after wisdom is that currently retries go in even too fast (run on same broken WN e.g) so I am thinking of adding a couple of hours cooloff. In practice we do not have problems with tails, other than the dreaded : some files keep failing for days, corrupted, lost, only at broken sites... you know all of that.
>
> That's at least from CRAB POV, which now has a "few more years" lifetime. As to what
> priority/share needs will be for CMS in Run4-5 age, that's not in my hands to decide.
> I assume you are aware of current process in CMS for a new WMS.
>
> Stefano
>
> On 19/09/2025 14:20, Brian Paul Bockelman wrote:
>> Hi Stefano,
>>
>> What makes you think this is not important?
>>
>> - Running a few jobs from each task as early as possible was seen as a helpful way to alert users early of broken tasks.
>> - Prioritizing job retries over first job tries of other tasks was seen as important for reducing the “tail” of the workload.
>>
>> Certainly these were seen as important at the time.  Are they no longer relevant?
>>
>> Brian 

*

On 19/09/2025 17:19, Stefano Belforte wrote:
>
> Yes,
> that's why I think we can do w/o this. Since we never really had it, nor
> desperately need it.
>
> Stefano, with love, of course
>
> On 19/09/2025 17:02, Jaime Frey wrote:
>> A few observations on the “blame target” code:
>>
>> * For jobs with the same set of job priority values, the schedd sorts lower job ids first. This is equivalent to the QDate used for PostJobPrio1.
>>
>> * By using QDate for PostJobPrio1 and crab_retry for PostJobPrio2, retry jobs take priority only over jobs submitted at the exact same time (and with the same JobPrio). The retry jobs will not be prioritized over first-try jobs that were submitted earlier, and the QDate (or the schedd’s sort by job id if you removed PostJobPrio1 and PostJobPrio2) will prioritize the retry jobs over jobs submitted later.
>>
>> * By setting PreJobPrio1 for the first few jobs in a task, those jobs will be ordered before all jobs of any priority (aside from other jobs that also set PreJobPrio1). That’s different from the intention expressed in the comment for the code.
>>
>>  - Jaime
