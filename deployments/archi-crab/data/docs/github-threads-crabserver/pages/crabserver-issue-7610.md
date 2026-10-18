# dmwm/CRABServer issue #7610: tune RSE list for large dataset recalls

State: closed
Opened: 2023-04-20T14:26:23Z
Closed: 2023-04-27T13:54:54Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7610

## Opening post (belforte, 2023-04-20T14:26:23Z)

this is to keep track of discussion which we started today in CRAB Meeting.
current policy:
*  if dataset < 50TB --> use `grouping=ALL` : Rucio places data in a single site
 * otherwise, pick (size/50TB+1) RSE's from the list and hand those to Rucio using `grouping=DATASET`

Questions:
1. keep 50TB as threshold ? move to 100 TB ?
2. there are recall requests for 450TB samples, does it make sense to scatter in 10 sites ? Should we put a cap on the number of sites ?
3. how does `grouping=DATASET` work ? Will Rucio try to spread evenly, or try to put all at a single site if that site has enough quota ? Rucio [documentation](https://rucio.cern.ch/documentation/client_api/ruleclient#add_replication_rule) says:
   * ALL -  All files will be replicated to the same RSE.
    * DATASET - All files in the same dataset will be replicated to the same RSE.
    * NONE - Files will be completely spread over all allowed RSEs without any grouping considerations at all.


 
@KatyEllis volunteered to follow up on 3. with Rucio developers

## Comment (belforte, 2023-04-25T21:14:15Z)

thanks to @mrceyhun  I have looked at size distribution for (MINI)AOD(SIM) datasets.
https://monit-grafana.cern.ch/goto/iYTDX6P4z?orgId=11
![image](https://user-images.githubusercontent.com/1837785/234411663-ed818ffa-24f9-412f-aa00-7e0074626493.png)
(in the plot above I selected >5TB in top menu and added legenda for visibility)

Clearly the recalled datasets at O(450)TB are odd outliers (B-Parking) and moataset we may want to recall are below 100TB and if we wanted to split, I would split sort of 100 TB per site `nsites = int(size/100) + 1`

@KatyEllis do you agree ?
I'd like to push this change in coming release

## Comment (belforte, 2023-04-27T13:29:58Z)

in todays CRAB meeting we agreed to simply use `grouping=alll` for all datasets. And monitor how it goes.

As a matter of caution, I will keep current code in place, simply raise the current limit for dataset splitting from 50 to 1000 TB.
https://github.com/dmwm/CRABServer/blob/f785d252ec2153bd207127b765f8f756ffeea1cc/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L175
We reject anyhow requests above 1PB.
https://github.com/dmwm/CRABServer/blob/f785d252ec2153bd207127b765f8f756ffeea1cc/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L140-L141

## Comment (KatyEllis, 2023-04-27T13:43:42Z)

That sounds like a good plan. Let's monitor how it goes.
