# dmwm/CRABServer issue #8987: document incident 2k Task Processes were killed and restarted unexpectedly, 11th March

State: open
Opened: 2025-03-14T11:39:21Z
Labels: Type: Documentation, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8987

## Opening post (nausikt, 2025-03-14T11:39:21Z)

Hints from Stefano:
I also noticed. But have no explanation. It appears like a "lot" of processes were killed and restarted. First time I see it.
interestingly it seems same time as the similarly unusual peaking of SUBMIT FAILED 

Stefano found plenty of 
```
Could not find any schedd to submit to. Exception was raised: 
No CRAB schedds returned by collector query. 
COLLECTOR_HOST parameter is cmsgwms-collector-global.cern.ch:9620,cmsgwms-collector-global.fnal.gov:9620
```

which very likely related to the newly introduced Global Pool Central Manager at FNAL. 
either due to DNS alias switching or some delay in DNS propagation might causes this issue.
Ref: https://cms-talk.web.cern.ch/t/cmssrv2313-fnal-gov-is-the-new-global-pool-central-manager-at-fnal/117886

**BUT**, there should still be ~no submit failed since we separated submit refused.
_________
See also Grafana here: https://monit-grafana.cern.ch/d/CsnjLe6Mk/crab-overview?orgId=11&from=1741428257119&to=1741687457119&refresh=1h&viewPanel=115


![Image](https://github.com/user-attachments/assets/223b4e38-b86c-4ea9-bfc8-8c334e66d67b)
