# dmwm/CRABServer issue #7515: crabserver REST - use cherrypy monitoring as WMCore does

State: open
Opened: 2023-01-30T14:32:43Z
Labels: Priority: Medium, Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/7515

## Opening post (mapellidario, 2023-01-30T14:32:43Z)

Valentin recently implemented a way for exporting cherrypy statistics in a format that is compatible with prometheus scraping [1]. 

We should consider adding this to crabserver REST as well, as this can improve our understanding of our REST server.

[1] https://github.com/dmwm/WMCore/pull/9940
