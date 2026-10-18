# dmwm/CRABServer issue #7939: define and implement  inferface of CRABClient and Rucio python client. 

State: closed
Opened: 2023-10-12T08:34:02Z
Closed: 2023-10-12T08:50:27Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7939

## Opening post (belforte, 2023-10-12T08:34:02Z)

Scope creep from “run jobs on the grid” to “and also manage my data”, which points to incorporating Rucio python client into CRAB Client ,
After discussion with Eric and Shahzad in [cmsdist](https://github.com/cms-sw/cmsdist/issues/8737)  and initial integration in [crab and crab.py](https://github.com/dmwm/CRABClient/issues/5213) The plan is 
 * do it for CMSSW_12_6 or later  integrating Rucio python client
 * later look into extending down to CMSSW_11 and hopefully CMSSW_10_6 (used for UL)
 * no support for earlier releases beside the current couple of cases where we fork a pyhon script (e.g. checkwrite)

## Comment (belforte, 2023-10-12T08:50:27Z)

oopss.... this should be in CRABClient repo. Moving
