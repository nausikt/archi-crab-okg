# dmwm/CRABServer issue #7948: lock input data also when partialDataset=True

State: closed
Opened: 2023-10-16T10:30:05Z
Closed: 2023-11-09T16:40:53Z
Labels: Type: Enhancement, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7948

## Opening post (belforte, 2023-10-16T10:30:05Z)

since now we encourage users to use dataset not fully recalled from tape
https://github.com/dmwm/CRABServer/blob/65bd86caae2b590c148284ea62c3b7b124584162/src/python/TaskWorker/Actions/Recurring/TapeRecallManager.py#L140-L143

we should lock those files on disk like we do for everything else.
Need to make a file list, since some blocks may be only partially on disk.

## Comment (belforte, 2023-11-08T20:46:42Z)

let's start by locking by full blocks(Rucio datasets) even if it triggers some silent tape recall. We'll worry about going down to file level if really needed.
