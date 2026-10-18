# dmwm/CRABServer issue #8274: add a delay when retrying to pull crabconfig JSON from gitlab 

State: closed
Opened: 2024-03-07T09:34:00Z
Closed: 2024-08-30T09:51:42Z
Labels: Type: Bug, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8274

## Opening post (belforte, 2024-03-07T09:34:00Z)

```

On 3/6/24 22:07, Ismael Posada Trobo wrote:
>
> Dear Muhammad,
>
>  
>
> This is Ismael Posada, from GitLab Service.
>
>  
>
> We communicate with you in order to ask you to please cease immediately the activity from the cluster “cmsweb-k8s-prodsrv-v-zone-a-2-5ffxu34ncym4-node-0.cern.ch”, owned by you, that is performing a high request rate against the “/crab3/CRAB3ServerConfig/-/raw/master/cmsweb-shedds-config.json” endpoint (in the https://gitlab.cern.ch/crab3/CRAB3ServerConfig repository)
>
>  
>
> Due to this high activity, we are observing an episode where you are exceeding the rate limits during a prolonged period of time.
>
>  
>
> Please, act as soon as possible, otherwise we will escalate this to our Security Team.
>
>  
>
> Thank you for your cooperation.
>
>  
>
> Cheers,
>
> Ismael
```

## Comment (belforte, 2024-03-07T09:44:19Z)

configuration files in gitlab are pulled in https://github.com/dmwm/CRABServer/blob/822a6b76113bca2b7ffbcaab6aa6c69d16420ef0/src/python/CRABInterface/Utilities.py#L97

but avoiding the DOS attack is not that easy, since the call fails, there's no cached value and a new call is made every time a client contacts the REST. We do not have retry loops in the REST code itself here.
It may also be that it is not as much retry in the client(s) as queries from multiple clients (all postjobs and transfer scripts e.g.).

So I am not sure if we can (easily) do something.

Ismale point to https://docs.gitlab.com/ee/administration/settings/user_and_ip_rate_limits.html#response-headers but it seems a tool for them, not us.

## Comment (belforte, 2024-05-16T18:22:36Z)

Maybe we could avoid the "pull every 30min from gitlab in case we changed it" and rather push a config. change via K8s when a change is committed ?
@novicecpp  @mapellidario since we are fresh of discussion on K8s deployment.. 
given also that changes to that configuration happens rarely (mostly to disable/enable schedd's)

If we look carefully at  https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/blob/master/cmsweb-rest-config.json?ref_type=heads we may even conclude that it is very static and could be part of the K8s template. And the only dynamic thing is the list of schedulers.
Of course the problem of the day was a typo in the list of schedulers ! And we should ask ourselves... why is that managed via the REST rather than be a TW configuration handled via puppet ? Now we change in gitlab and REST picks it every 30 min. If we do it via puppet it takes 2h.. so what ?

Nor puppet nor K8s existed when the current mechanism was thought of, and pushing changed to the REST required a new CMSWEB deployment which they would only do once a month. Now things are much different.

## Comment (novicecpp, 2024-05-17T07:03:53Z)

I agree. Decommission the crab3/CRAB3ServerConfig entirely. 
- `delegate-dn` to CRABServerAuth.py
- `cmsweb-shedds-config.json` to `cfg` directory in TW machine and new config to json path.
- `htcondorPool` to TaskWorkerConfig.py (not 100% sure)
- I do not know about `modes`.

## Comment (belforte, 2024-05-17T08:47:03Z)

`modes` has lot of history of course, but at this point is a way for the CRABServer config,py to find out which S3 bucket to use for cache (i.e. sandboxes et al.). We may very well put the bucket name in the config. The full URL is part of backward-compatibility with old CRABCache service, not strictly needed since "always the same" but we may want to keep the door open to moving from S3 to something else, who knows.

## Comment (belforte, 2024-05-23T11:12:18Z)

let's plan for Vijay to do this. Still falls in "code refactoring".

## Comment (belforte, 2024-08-28T21:15:13Z)

Need to close and open a new one about getting rid of  crab3/CRAB3ServerConfig

## Comment (belforte, 2024-08-30T09:51:42Z)

replaced by #8675
