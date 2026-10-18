# dmwm/CRABServer issue #9354: reduce wasted CoreHR in CRAB failed jobs

State: open
Opened: 2026-07-20T14:00:43Z
Labels: Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/9354

## Opening post (belforte, 2026-07-20T14:00:43Z)

At L1 request, we need to look into this topic since CRSG (Computing Resources Scrutiny Group) has demaded that CMS explain how much time is spent in failing jobs and which steps are being taken to improve the situation.

Urgent action is needed to avoid being penalized in computing resources assignments.

ASO failures are our dominant source of CoreHR spent in eventually failing jobs. Followed by FIle Open errors (8021/8028) and then we have 50115 which is currently a sort of catch all which should be better classified in order to think of some strategy
https://monit-grafana.cern.ch/goto/bfsoof9udhcsgb?orgId=11

<img width="1176" height="324" alt="Image" src="https://github.com/user-attachments/assets/393b4d2a-8e13-407d-8687-c18d6decd3ac" />

As a mitigation we will kill a task once a certain number of jobs failed during ASO, and notify user in the status message. Will ensure that files can be opened before starting cmsRun and will further investigate 50115.

## Comment (belforte, 2026-08-25T08:52:24Z)

That study was only looking at `Completed` jobs, picture is very different when adding `Removed` ones
https://monit-grafana.cern.ch/goto/cfw8di4bs8gzke?orgId=11

<img width="1217" height="327" alt="Image" src="https://github.com/user-attachments/assets/259e16ee-ff00-437a-9bcd-d411520c29f3" />

## Comment (belforte, 2026-08-25T08:59:59Z)

So we need to study OutOfBound and 80001
I recorded initial investigations in https://cms-talk.web.cern.ch/t/wasted-cpu-time-corehours-in-crab/147739

So we derived new subtasks
- [ ] **kill task if success rate is e.g. < 80% after 100 jobs. No matter what.** #9402 
- [ ] #9395 
- [ ] #9389 
- [ ] #9398 
- [ ] #9397
