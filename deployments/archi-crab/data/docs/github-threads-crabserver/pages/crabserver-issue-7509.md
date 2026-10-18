# dmwm/CRABServer issue #7509: jobwrapepr - using wrong python for condor_chirp

State: closed
Opened: 2023-01-27T13:36:29Z
Closed: 2023-02-20T14:41:13Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7509

## Opening post (mapellidario, 2023-01-27T13:36:29Z)

### description

When a job finishes, we use condor_chirp to retrieve its exit code: 

The log should look like

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
==== Long exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

but I noticed that with the new jobwrapper I was getting (for example, at https://cmsweb.cern.ch:8443/scheddmon/059/dmapelli/230127_122119:dmapelli_crab_20230127_132116/job_out.1.0.txt ):

```plaintext
======== Figuring out long exit code of the job for condor_chirp ========
/srv/condor_exec.exe: line 63: python: command not found
==== Failed to load the long exit code from jobReport.json.1. Falling back to short exit code ====
==== Short exit code of the job is 0 ====
======== Finished condor_chirp -ing the exit code of the job. Exit code of condor_chirp: 0 ========
```

### solution

force python3 at this line:

https://github.com/dmwm/CRABServer/blob/f01f865625031b93709f311425b44b49923adae3/scripts/gWMS-CMSRunAnalysis.sh#L56

a PR is on its way
