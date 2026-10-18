# dmwm/CRABServer issue #9271: GOALS for 2026

State: open
Opened: 2026-02-11T09:19:16Z
URL: https://github.com/dmwm/CRABServer/issues/9271

## Opening post (belforte, 2026-02-11T09:19:16Z)

Picking up from #8879 
legend: Qx = milestone for that quarter , Hx = milestone for that half year

## Ported over from 2025
- [ ] **Q2** reboot each schedd every 6 months or so (automatically).  #8651
- [ ] **H2** use of tokens for talking to CMSWEB #7845 (predicated on CMS TokenTeam progresses)
- [x] **Q1** ArgoCD for our K8s applications #9188
- [ ] **H2** use submitted task info in task scheduling #9073
- [x] **H1** revisit JobRetry.py policies (more retries, re-eval site list ...) #9264

## new for 2026
 - [ ] **H1** Prototype AI Chatbot for user support
 - [x] **H1** Rebuild CRABServer, TW into Alma9 py3.9, bumped to WMCore freeze. https://github.com/dmwm/CRABServer/issues/8956, https://github.com/dmwm/CRABServer/pull/9265
 - [ ] **H2** Final AI Chatbot for user support
 - [ ] **Q3** Mitigation of time wasted in failed jobs #9354 
 - [ ] **H2** add configurable cooloff to automatic resubmissions #9348  
## always ongoing
- [ ] cleanup code source (remove "transients" from past migrations)
- [ ] cleanup an update documentation
