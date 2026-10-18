# dmwm/CRABServer issue #8016: Run tests in CI when changing puppet configuration

State: open
Opened: 2023-11-18T14:30:35Z
Labels: Area: CI/CD, OPERATION, Postmortem
URL: https://github.com/dmwm/CRABServer/issues/8016

## Opening post (novicecpp, 2023-11-18T14:30:35Z)

From postmortem  [2023-09-27 Rucio authentication fail on TaskWorker](https://cmscrab.docs.cern.ch/incident/2023-09-27-rucio-authentication-fail.html).

"all changes to prod go through some automatic testing first" - Stefano. 
It will help us detect errors when Puppet config changes (Upgrade OS, new condor version, etc.) if it affects the code.

It will be the part of new CI pipeline in https://github.com/dmwm/CRABServer/issues/7958.
