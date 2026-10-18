# dmwm/CRABServer issue #8731: resubmission does not work for automatic splitting

State: open
Opened: 2024-10-01T16:08:29Z
Labels: Type: Bug, Status: On Hold
URL: https://github.com/dmwm/CRABServer/issues/8731

## Opening post (belforte, 2024-10-01T16:08:29Z)

see e.g. https://cms-talk.web.cern.ch/t/crab-resubmit-still-does-not-work-properly-for-automatic-splitting/51139 and references in there.

Last time I looked at this I got convinced that resubmissions of the subdags is only possible before they have all complete. But once they do, the main dag itself is closed and restarting it will not trigger any action, there is no Rescue file for it.
Yet only the BASE (was called ROOT before) DAG is restarted
https://github.com/dmwm/CRABServer/blob/3087e063128744de967f662f70dc826a076ddf93/src/python/TaskWorker/Actions/DagmanResubmitter.py#L67-L75

It seems to me that it was like this since ever. But I never looked at  this cose before. So... hard to say.

We can possibly address this in the context of refactoring resubmission #6270
