# dmwm/CRABServer issue #8266: move to this repo code for JobAutoTuner and reformat

State: closed
Opened: 2024-02-29T13:32:16Z
Closed: 2024-03-04T16:26:55Z
Labels: Type: Enhancement, Area: Code Cleanup, Priority: TOP, OPERATION, alma9
URL: https://github.com/dmwm/CRABServer/issues/8266

## Opening post (belforte, 2024-02-29T13:32:16Z)

Code for the JobRouter that we use in condor scheduler is now taken from
https://gitlab.cern.ch/CMSSI/SubmissionInfrastructureScripts

and it includes both the overflow functionality, which we use, and the job memory/time tuning, which we do not.

Goals

- [x] port to python3
- [x] Move to this repository to ease maintenance
- [x] Change name so that we can transition smoothly to use new code in puppet
- [x] remove unused functionalities
- [x] reformat so that we can start with simple code that only implements the functionality that we need and add more if/when needed
- [x] minimize the number of parameters passed via hiera variables

I tried to remove last two points since the way we use JobRouter via  in `/etc/condor/config.d/90_jobrouter.config`
```
JOB_ROUTER_ENTRIES_CMD=/data/srv/SubmissionInfrastructureScripts/JobAutoTuner.py
```
was deprecated in HTCondor and will stop working "during HTCondor23 lifetime" and fully gone in HTC24 as per [their documentation](https://htcondor.readthedocs.io/en/latest/grid-computing/job-router.html#deprecated-routing-table-entry-classad-attributes)

But in order to remove dependency from WMCore  and place it in a different directory and simply for mind sanity since in the in the end I needed to fix undefined variables and bad indentations and so to read it, I decided to also simplify drastically.

The deprecation of `JOB_ROUTER_ENTRIES_CMD` means that if we ever want more than "from European T1's to closeby T2's" we will have to do it all differently anyhow.

## Comment (belforte, 2024-03-04T16:26:55Z)

closed via #8268
