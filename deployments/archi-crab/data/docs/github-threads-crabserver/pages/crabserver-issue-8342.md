# dmwm/CRABServer issue #8342: use new format for periodic remove reason

State: closed
Opened: 2024-04-16T14:06:01Z
Closed: 2024-09-16T08:43:20Z
Labels: Type: Question, Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8342

## Opening post (belforte, 2024-04-16T14:06:01Z)

See https://its.cern.ch/jira/browse/CMSSI-113

 As of HTCondor > 9.5, the can be achieved using `SYSTEM_PERIODIC_REMOVE_NAMES` :  https://htcondor.readthedocs.io/en/latest/admin-manual/configuration-macros.html#SYSTEM_PERIODIC_HOLD_NAMES 
 
 Code to replace is in
 https://github.com/dmwm/CRABServer/blob/6f65ad6a5dd413d6f4aa078aae86dd5ceb63edf5/src/python/TaskWorker/Actions/DagmanCreator.py#L161-L175

This will need changing too
https://github.com/dmwm/CRABServer/blob/6f65ad6a5dd413d6f4aa078aae86dd5ceb63edf5/src/python/TaskWorker/Actions/RetryJob.py#L257-L278

## Comment (belforte, 2024-08-14T08:28:33Z)

hmm... The current [documentation](https://htcondor.readthedocs.io/en/latest/search.html?q=periodic_remove_name&check_keywords=yes&area=default#) lists SYSTEM_PERIODIC_REMOVE_NAMES (part of schedd config) but not for the plain PERIODIC_REMOVE that we can [put in JDL](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html#submit-description-file-commands)

I can ask HTC support, but sounds like this can be closed
All in all current code is not that hard to read

Let's make a "can this be understood" test with @aspiringmind-code

## Comment (belforte, 2024-09-16T08:43:20Z)

I showed the code to @aspiringmind-code and we agreed to leave it as is.
