# dmwm/CRABServer issue #7802: force a user siteWhiteList using Data.userInputFiles

State: open
Opened: 2023-08-10T13:22:16Z
Labels: Type: Bug, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7802

## Opening post (belforte, 2023-08-10T13:22:16Z)

see https://cms-talk.web.cern.ch/t/8020-error-when-launching-more-than-3-4-tasks-accessing-data-on-the-same-tier/28237

current documentation "strongly recommends" a white list https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
but it is really a very bad idea to submit jobs which can target any possible site as the default !
