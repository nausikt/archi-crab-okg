# dmwm/CRABServer issue #8337: modernize HTCondor calls

State: closed
Opened: 2024-04-15T21:30:56Z
Closed: 2025-02-17T21:50:56Z
Labels: Priority: High, Area: Code Cleanup, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8337

## Opening post (belforte, 2024-04-15T21:30:56Z)

Stop using what HTCondor deprecated over the years before they remove it.

Also take advantage of new bindings to simplify wherever possible.

- [x] #8285 
- [x] #8331 
- [x] #8332
- [x] #8336 
   - [x] #8456 
- [x] #8333 
- [x] #8447 
- [x] #8450 
- [x] #8338
- [x] #8339
- [x] #8342
- [x] #8488
- [x] #6270

## Comment (belforte, 2024-06-10T11:57:20Z)

My branch https://github.com/belforte/CRABServer/tree/modernize_HTC currently has fixes for the above up to "remove calls to HTC inside REST". But I want to cleanup further.

I also still need to test (and likely put code in for):
- [x] extraJDL
- [x] acceleratorparams
- [x] dealing with user-insreted extra spaces in extraJDL

## Comment (belforte, 2024-06-11T20:45:42Z)

There's some more cleanup to be done, in particular I want to avoid using `ROOT` as task type since it is a "special" classAd and I already suffered enough of the ambiguity. As ToddM [wrote](https://lists.cs.wisc.edu/archive/htcondor-users/2024-June/msg00022.shtml) "it happens to be magical"
But I could not think of a good name yet to replace in current list of TaskType values: "ROOT PROCESSING TAIL" 
Should also rename `TaskType` to `CRAB_DagType` since those are condor jobs in scheduler universe which run the various dagmans, `ROOT ` is always there, the others are for automatic splitting. But I need to fully understand automatic splitting machinery first. 

moved to new issue: #8488

## Comment (belforte, 2025-02-17T21:50:56Z)

refactoring crab resubmit will not be "immediate". And is not directly related. Let's close this in the meanwhile
