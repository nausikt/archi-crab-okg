# dmwm/CRABServer issue #9208: High-Mem CRAB Jobs monitoring and dashboard to demystifies the situation.

State: closed
Opened: 2025-10-10T10:30:06Z
Closed: 2026-08-24T15:47:03Z
Labels: Priority: High, Area: MONIT, Area: HTCondor, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9208

## Opening post (nausikt, 2025-10-10T10:30:06Z)

Here is what i've digested from experts's discussions.

There are 2 category of questions/purposes for these dashboard and monitoring to addressed.
1. **Reassuring/Confirming** of this widespread phenomenon, make CRAB fact-based transparent in this phenomenon. [1]
2. **Improved/Easing High-Mem job tracing routine monitoring**, for tracking down **abuse** case. [2]

______
### [1] Bird-Eye views for this specific widespread phenomenon.
**Objectives**:
1. make phenomenon transparent.
2. At least, we should been able to confirm the before/after effects of our following actions by ourself,
 1) Reduce Max for 1 core from 5 to 3 GB in initial submission.  
 2) Allow user to ask more (up to 5) in crab resubmit.

these dashboards should be able to shown **back then** cores-mem utilization, thus could be use as one of *quick* post-analysis tools, for any enforcements/policies we just introduced or upcomming in the future. 

Serving as one-bottomline metrics and dashboards for us (also future operators) as a summary of this whole phenomenon, such that we can just have a glance and can tell whether everything is O.K. or need to dive deeper in [2]
_____
### [2] Easy to trace, `abuse` use-cases
**Objectives**:
1. As name implied.
2. reduce tracing time from abuse-to-user, so operators can warn user.
3. has potential to gathering facts fast for identifying novel `abuse` use-cases.

this collection of dashboard, quite close to what SI have as Marco & Antonio Perez's shown or what Open Search could offers that CRAB already have as you plotted. but we will port it to grafana and emphasized/highlights on
1. mem-per-core utilization of both avg. and max mem usages
2. "ask for more cores for more memory but actually never used" abuse.
3. ambient copy-paste config low-utilization jobs.
_______
TLDR; We will have 1 set of Big-picture dashboards and 1 set of Finer-grained dashboards, both will serve different purposes. 

Please, @belforte guides me on how to do these things properly and really addressed the problem we all faced, forgive me for any missing crucial details, please kindly pointed me out.

P.S. Apologize for the delayed. Yesterday, is not going well from my side. 😷

## Comment (belforte, 2026-08-24T15:45:43Z)

I am not sure that we need to do anything in this area
