# dmwm/CRABServer issue #8015: Setup test with Rucio Integration server

State: open
Opened: 2023-11-18T13:05:38Z
Labels: RUCIO, Postmortem
URL: https://github.com/dmwm/CRABServer/issues/8015

## Opening post (novicecpp, 2023-11-18T13:05:38Z)

Postmortem [2023-09-27 Rucio authentication fail on TaskWorker](https://cmscrab.docs.cern.ch/incident/2023-09-27-rucio-authentication-fail.html)

The main 2 cases that we need Rucio Integration server:
- Rucio Server upgrades.
- API that need privileged account (e.g., tape recall) , to prevent mess up with production.

Last time I ran against integration server, it simply did not work. We need CMSRucio dev for help.
