# dmwm/CRABServer issue #9204: access to TWLog via UI is broken

State: closed
Opened: 2025-10-07T16:08:41Z
Closed: 2025-10-14T09:10:37Z
Labels: Type: Bug, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9204

## Opening post (belforte, 2025-10-07T16:08:41Z)

quite likely as a consequence of recent changes to REST

The UI page is

<img height="500" alt="Image" src="https://github.com/user-attachments/assets/1158f97e-1235-45ad-afcd-9f185c562ad2" />

where clearly the URL "proposed" (which appears at the bottom when the mouse hover on the TaskWorker log link) is  wrong
`https://cmsweb-test2.cern.ch/crabserver/`/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348`

contains the "extra text" `ui/task/crabserver/dev/`. The way to call the cache download API should be
`https://cmsweb-test2.cern.ch/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348`

But when I try that I do not get the log content, but a pre-signed URL for S3
```console
belforte@lxplus807/TC3> X5curl "https://cmsweb-test2.cern.ch/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348"
{"result": [
 "https://s3.cern.ch/crabcache_dev/belforte/251002_154351%3Abelforte_crab_20251002_174348/twlog?AWSAccessKeyId=715203df6482458ba839e73e6dab634b&Signature=leJxNPiXGoMnNAvTUwjCpK%2FfVbk%3D&Expires=1762444781"
]}
belforte@lxplus807/TC3> 
```

That pre-signed URL works finely, but either I forgot how `cache` API works, or something is badly wrong.

## Comment (belforte, 2025-10-07T16:37:02Z)

Yes, I had forgotten how `cache` API works. From the [documentation](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTCache.py#L30-L54) the desired URL should have `subresource=retrieve`, not `subresource=download`. Indeed this works almost as desired
https://cmsweb-test2.cern.ch/crabserver/dev/cache?subresource=retrieve&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348

with the only defect that it returns a JSON structure
`{"result": ["<actual twlog content as a string>"]}`
while we'd like simply `result[0]`
OTOH, returning such JSON is standard behavior of the CRABServer REST class. 

In conclusion it all looks like the "age-old" code in the UI has not been adapted for the fact that I changed the cacheUrl value !!

https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L284-L301

## Comment (belforte, 2025-10-07T16:40:12Z)

I can certainly welcome a bit of help from someone who understans `js` scripting, if nothing else to chase where `cacheUrl` is picked from ! @nausikt

## Comment (nausikt, 2025-10-07T16:41:34Z)

> Yes, I had forgotten how `cache` API works. From the [documentation](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTCache.py#L30-L54) the desired URL should have `subresource=retrieve`, not `subresource=download`. Indeed this works almost as desired https://cmsweb-test2.cern.ch/crabserver/dev/cache?subresource=retrieve&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348
> 
> with the only defect that it returns a JSON structure `{"result": ["<actual twlog content as a string>"]}` while we'd like simply `result[0]` OTOH, returning such JSON is standard behavior of the CRABServer REST class.
> 
> In conclusion it all looks like the "age-old" code in the UI has not been adapted for the fact that I changed the cacheUrl value !!
> 
> [CRABServer/src/script/task_info.js](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L284-L301)
> 
> Lines 284 to 301 in [c45cf9b](/dmwm/CRABServer/commit/c45cf9bd796bde455d6288a88a1c28d5c46f16cd)
> 
>  function displayTaskWorkerLog(errHandler) { 
>      var xmlhttp = new XMLHttpRequest(); 
>   
>      if (cacheUrl === undefined || cacheUrl === "") { 
>          errHandler(new TaskInfoUndefinedError()); 
>          return; 
>      } 
>      var S3,url; 
>      if(cacheUrl.indexOf("S3")!=-1) 
>          S3=true; 
>      else 
>          S3=false; 
>   
>      if(S3==true) 
>          url=cacheUrl.split("S3")[0]  + "crabserver/" + dbVersion + "/cache?subresource=download&objecttype=twlog&taskname="+inputTaskName; 
>      else 
>          url = cacheUrl + "/logfile?name=" + inputTaskName + "_TaskWorker.log&username=" + username;

Congrats! Okk since problem are well defined now, i can take care the REST!

## Comment (belforte, 2025-10-07T16:41:45Z)

`tm_cache_url` stored in DB's `tasks` table still has `S3` in it
```
tm_cache_url	S3/crabcache_dev
```

## Comment (belforte, 2025-10-07T16:43:08Z)

but I fear that with such value this line will go nuts
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L298

## Comment (nausikt, 2025-10-07T17:00:40Z)

> but I fear that with such value this line will go nuts
> 
> [CRABServer/src/script/task_info.js](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L298)
> 
> Line 298 in [c45cf9b](/dmwm/CRABServer/commit/c45cf9bd796bde455d6288a88a1c28d5c46f16cd)
> 
>  url=cacheUrl.split("S3")[0]  + "crabserver/" + dbVersion + "/cache?subresource=download&objecttype=twlog&taskname="+inputTaskName;

Man, could it be because cacheUrl  back then looks like these?
```
https://cmsweb-test2.cern.ch/S3/crabcache_dev
http://s3.cern.ch/crabcache_dev
https://cmsweb-testbed.cern.ch/S3/crabcache_prod
https://cmsweb-auth.cern.ch:8443/crabcache
https://cmsweb.cern.ch/S3/crabcache_prod
https://cmsweb-test2.cern.ch/S3/crabcache_dev
https://cmsweb-testbed.cern.ch/S3/crabcache_prod
https://cmsweb.cern.ch/S3/crabcache_prod
```

Such that changes
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTUserWorkflow.py#L533-L534

into something like these should solved the issue?
```python
cacheurl = f"{self.restHost}/S3/{self.config.s3_bucket}"
```
P.S. I think we might not need to touch js.

## Comment (nausikt, 2025-10-07T17:31:07Z)

> > but I fear that with such value this line will go nuts
> > [CRABServer/src/script/task_info.js](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L298)
> > Line 298 in [c45cf9b](/dmwm/CRABServer/commit/c45cf9bd796bde455d6288a88a1c28d5c46f16cd)
> > url=cacheUrl.split("S3")[0]  + "crabserver/" + dbVersion + "/cache?subresource=download&objecttype=twlog&taskname="+inputTaskName;
> 
> Man, could it be because cacheUrl back then looks like these?
> 
> ```
> https://cmsweb-test2.cern.ch/S3/crabcache_dev
> http://s3.cern.ch/crabcache_dev
> https://cmsweb-testbed.cern.ch/S3/crabcache_prod
> https://cmsweb-auth.cern.ch:8443/crabcache
> https://cmsweb.cern.ch/S3/crabcache_prod
> https://cmsweb-test2.cern.ch/S3/crabcache_dev
> https://cmsweb-testbed.cern.ch/S3/crabcache_prod
> https://cmsweb.cern.ch/S3/crabcache_prod
> ```
> 
> Such that changes
> 
> [CRABServer/src/python/CRABInterface/RESTUserWorkflow.py](https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/python/CRABInterface/RESTUserWorkflow.py#L533-L534)
> 
> Lines 533 to 534 in [c45cf9b](/dmwm/CRABServer/commit/c45cf9bd796bde455d6288a88a1c28d5c46f16cd)
> 
>   
>  cacheurl = f"S3/{self.config.s3_bucket}"   # record S3 bucket in task table 
> into something like these should solved the issue?
> 
> cacheurl = f"{self.restHost}/S3/{self.config.s3_bucket}"
> P.S. I think we might not need to touch js.

Forgive me, removing the baseURL actually was originally your goal.

I found that utilize `window.location.origin` this way might solved issue, by letting UI pick up their own baseURL on client side in browser.
```javascript
const url = new URL(`/crabserver/${dbVersion}/cache`, window.location.origin);
url.search = new URLSearchParams({
  subresource: 'download',
  objecttype: 'twlog',
  taskname: inputTaskName,
}).toString();

console.log(url.toString());
// e.g. https://cmsweb.cern.ch/crabserver/v1/cache?subresource=download&objecttype=twlog&taskname=...
```
 OR
```javascript
url= window.location.origin + "/crabserver/" + dbVersion + "/cache?subresource=download&objecttype=clientlog&taskname="+inputTaskName;
```

## Comment (nausikt, 2025-10-07T18:38:16Z)

### In Summary.
the extra uri came from when we call ajax with pre-mature url cause by `cacheUrl.split("S3")[0]` was empty string,
As a result, our ajax call ended up like. 

[1]
```javascript
$.ajax("crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348")
// Output link url: https://cmsweb-test14.cern.ch/crabserver/ui/task/251007_114139%3Akphornsi_crab_test14-20251007-2/dbver/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348
```
where ajax treat our url as ***Relative*** URI such that it append our relative uri after current monitoring base URI `https://cmsweb-test14.cern.ch/crabserver/ui/task/251007_114139%3Akphornsi_crab_test14-20251007-2/dbver`.

So, our patch will ensure that ajax got provided with ***Absolute*** URI as following. thus it could resolved as expected.
[2]
```javascript
$.ajax(window.location.origin + "/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348")
// Output link url: https://cmsweb-test14.cern.ch/crabserver/dev/cache?subresource=download&objecttype=twlog&taskname=251002_154351:belforte_crab_20251002_174348
```

[1],[2]
<img width="1455" height="527" alt="Image" src="https://github.com/user-attachments/assets/2dc73ecc-c1f3-4044-9f76-908ebae5d79f" />

Ajax's Actual Request [1] 
<img width="544" height="59" alt="Image" src="https://github.com/user-attachments/assets/68c09365-e2a1-458b-9b5e-9f1df580bf8b" />

Ajax's Actual Request [2] 
<img width="547" height="45" alt="Image" src="https://github.com/user-attachments/assets/09ed3818-22e6-485c-93c1-14b409d6b87e" />

## Comment (belforte, 2025-10-07T19:02:37Z)

Thanks a lot @nausikt .
I am too tired to try to understand now what you wrote, given also that I never understood how this things works in the first place.

But let me clarify the fundamentals.
Current code still suffer of "history". As you may have noticed from CMSWEB repo, once upon a time there was a `crabcache` service in cmsweb. When we moved to use S3, a backward/forward-compatible code was put int. And alas never cleaned up.
But we will never to back. Which is why I was trying to remove that `https://...` stuff from `tm_cache_url` but had to keep `S3` in there to avoid changing too much code downstream .

As things stand now, the REST only needs to know the S3 bucket name which it is supposed to use (see crabserver/config.py) and everybody who wants information (including the UI !) should only ask the REST for what it needs using the `cache` API and never never care that things come from S3 or from anything else.
`S3` string should only appear inside `RESTCache.py`

Indeed the `S3` in the various methods in `ServerUtilities.py` has no real reason to be there other then "Stefano wanted to make it clear that those ultimately talk to S3", but they could work with any different cache implementation as long as it proviedes the same semantycs. i.e. retrieve URL's (presigned or not) which allow to PUT and GET the various objects.

If we can make that clear and clean everywhere, things will be easier to read and debug.

So my (only partially achieved) goal was not "remove the baseURL" but remove all code which refers to the ancient implementation of CRAB Cache and have a clean thing which only needs an S3 bucket name to work. Everything else is an accidental detail, not a goal.

## Comment (nausikt, 2025-10-07T19:13:00Z)

> Thanks a lot [@nausikt](https://github.com/nausikt) . I am too tired to try to understand now what you wrote, given also that I never understood how this things works in the first place.
> 
> But let me clarify the fundamentals. Current code still suffer of "history". As you may have noticed from CMSWEB repo, once upon a time there was a `crabcache` service in cmsweb. When we moved to use S3, a backward/forward-compatible code was put int. And alas never cleaned up. But we will never to back. Which is why I was trying to remove that `https://...` stuff from `tm_cache_url` but had to keep `S3` in there to avoid changing too much code downstream .
> 
> As things stand now, the REST only needs to know the S3 bucket name which it is supposed to use (see crabserver/config.py) and everybody who wants information (including the UI !) should only ask the REST for what it needs using the `cache` API and never never care that things come from S3 or from anything else. `S3` string should only appear inside `RESTCache.py`
> 
> Indeed the `S3` in the various methods in `ServerUtilities.py` has no real reason to be there other then "Stefano wanted to make it clear that those ultimately talk to S3", but they could work with any different cache implementation as long as it proviedes the same semantycs. i.e. retrieve URL's (presigned or not) which allow to PUT and GET the various objects.
> 
> If we can make that clear and clean everywhere, things will be easier to read and debug.
> 
> So my (only partially achieved) goal was not "remove the baseURL" but remove all code which refers to the ancient implementation of CRAB Cache and have a clean thing which only needs an S3 bucket name to work. Everything else is an accidental detail, not a goal.

Thank you Man! for clarifications! me too too tired now LoL, let me digest them tomorrow.

## Comment (belforte, 2025-10-08T08:40:10Z)

@nausikt if you reply by mail, please do not quote previous message

## Comment (belforte, 2025-10-08T08:52:27Z)

could this help ?
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L820

Maybe adding cacheUrl with the API for subresource=downaload in there is all we need 

As usual it looks to me that there is some confusion in this script, with some parts using those prebuild URL's and some building them on the fly using window.location etc. But likely it is simply me not understanding.

## Comment (nausikt, 2025-10-08T09:02:50Z)

Thank you Stefano, for pointed out. 

It's true `setUrls(dbVersion)` sound like a good place. It does confused me too.

## Comment (belforte, 2025-10-08T09:09:47Z)

of course I have no idea why it is not there already !

## Comment (belforte, 2025-10-08T09:45:02Z)

Krittin, if I am allowed a general advice, when possible always try to understand the full picture and go for the simplest solution down at the core. Not for the quickest, point-like fix. I.e. try to remove rather than add one spaghetti to the code mess :-)

## Comment (nausikt, 2025-10-08T09:53:10Z)

Sure, Man! Thanks for the advice, I'll make sure, i've digested your fundamental clarifications first, for this and next time.

BTW can you try this please, I'm struggling a bit to set up browser proxies to access from home. (following your doc)
https://cmsweb-test14.cern.ch/crabserver/ui/task/251008_094133%3Akphornsi_crab_test14-20251008-2

## Comment (nausikt, 2025-10-08T10:00:13Z)

Spaghetti code in frontend could be refactoring in many way, Normally i will introduced React/Svelt Framework for this identical task it's much easier to maintain.

But i guessed, it might overdo in this case. i will focus on refactoring with the legacy tech then.

## Comment (belforte, 2025-10-08T10:02:36Z)

let's not go for a full rewrite unless really needed. All in all it has been working for 10+ years

## Comment (belforte, 2025-10-08T10:06:20Z)

I am on the road too. But your fix does not work yet.

## Comment (belforte, 2025-10-08T10:08:05Z)

i.e. it says to clink on the link https://cmsweb-test14.cern.ch/crabserver/ui/task/251008_094133%3Akphornsi_crab_test14-20251008-2/dbver/crabserver/devfour/cache?subresource=download&objecttype=twlog&taskname=251008_094133:kphornsi_crab_test14-20251008-2

## Comment (belforte, 2025-10-08T10:10:53Z)

note that it still has an extra `ui/task/...../crabserver/` before the `cache?` API
and AFAIU we should ask the user to click on the pre-signed URL for s3.cern.ch returned by that API call. Not on the API call itself.

## Comment (nausikt, 2025-10-08T10:11:40Z)

Okk, Please take your time, Acknowledged Stefano, I understood the process, will make it easier for me to test this part.

## Comment (belforte, 2025-10-08T12:32:42Z)

IIUC, these lines were meant to accomplish the "query the server cache API and put the resulting pre-signed URL in the "taskworker-log-link" which the user is prompted to click on. The developer of the time (Prajesh) said that he could not find a way to directly query S3 and show the actual log content
https://github.com/dmwm/CRABServer/blob/c45cf9bd796bde455d6288a88a1c28d5c46f16cd/src/script/task_info.js#L297-L321

## Comment (nausikt, 2025-10-08T12:44:05Z)

Understood, may i ask from the UX point of view?

Would it be better for user to not clicking the link at all, clicking just the TaskWorker log Tab should shown the log content right away or is there any rationales behind? (*** seems not from what you mentioned above? ***)

I understood how s3 pre-signed url works, to limit access to only authorized user for limited time.
But this UI, could be done as chain of promises to get `Presigned-url` -> `download Content` -> `Rendered` right away by single clicked on `TaskWorker Log` tab. Would you like me to refactored it that way? 

What we gains: 
1. reduced 1 click for every Log viewer tabs.
2. code will be hopefully more intuitive by my refactoring for future devOps.

## Comment (belforte, 2025-10-08T13:01:40Z)

as a start.. I doubt any user ever clicked on that link. This i mostly for us, much more convenient than logging
in the TW and looking for the right file. Same for config and pset.
That said, I personally would like single click access to the log. But it depends on amount of effort. Two clicks is not that much time ! Not knowing how much work it takes to do, I can not make a decision. But you can.


THere is an odd thing though. WHen looking at tasks in production I see different behavior in e.g.
1) https://cmsweb.cern.ch/crabserver/ui/task/251006_125614%3Aatrianto_crab_final_hybridNew_limits_13_slices_envelope_3_func_alpha0p19_W-0p0043_7600_1444
2) https://cmsweb.cern.ch/crabserver/ui/task/251006_121604:lanyov_crab_aod25_zmu1_f1_v7

both are different from what happens in test clusters and they differ from each other !

try to look at Config and PSet for both. Hopefully you notice same differences as I do. If not... I can show on zoom

## Comment (nausikt, 2025-10-08T13:06:51Z)

> as a start.. I doubt any user ever clicked on that link. This i mostly for us, much more convenient than logging in the TW and looking for the right file. Same for config and pset. That said, I personally would like single click access to the log. But it depends on amount of effort. Two clicks is not that much time ! Not knowing how much work it takes to do, I can not make a decision. But you can.
> 
> THere is an odd thing though. WHen looking at tasks in production I see different behavior in e.g.
> 
> 1. https://cmsweb.cern.ch/crabserver/ui/task/251006_125614%3Aatrianto_crab_final_hybridNew_limits_13_slices_envelope_3_func_alpha0p19_W-0p0043_7600_1444
> 2. https://cmsweb.cern.ch/crabserver/ui/task/251006_121604:lanyov_crab_aod25_zmu1_f1_v7
> 
> both are different from what happens in test clusters and they differ from each other !
> 
> try to look at Config and PSet for both. Hopefully you notice same differences as I do. If not... I can show on zoom

Roger that, I will do it man, the efforts not that much given it's already aligned with this priority bug.
Ack on 2 unexpected different behavior, will take that into account/considerations as well.

## Comment (belforte, 2025-10-08T13:13:41Z)

much to my surprise, reloading 1) gives now same look as 2). But in both case the Config/PSet content is displayed immediately, while for the dev cluster I need to "click on the link below"

## Comment (nausikt, 2025-10-13T20:44:03Z)

FYI, somehow on my test14, pre-signed url already works [1] in every tabs  with current PR though:
https://cmsweb-test14.cern.ch/crabserver/ui/task/251007_114139%3Akphornsi_crab_test14-20251007-2/dbver/devfour

P.S. But i will fix content should rendered right away anyhow soon.

[1] Already got downloadable link (no extras relative uri), properly pointed to s3:
<img width="1019" height="492" alt="Image" src="https://github.com/user-attachments/assets/7c57875a-dbb1-447e-b0fb-3edbb4bc821b" />

[2] Hovered pre-signed uri looks good.
<img width="1018" height="331" alt="Image" src="https://github.com/user-attachments/assets/db1fd30a-0397-4d45-96e5-640e483d1f61" />

## Comment (belforte, 2025-10-14T08:06:06Z)

thanks. https://cmsweb-test14.cern.ch/crabserver/ui/task/251007_114139%3Akphornsi_crab_test14-20251007-2/dbver/devfour already looks good enough !

I am still puzzled by the different look for cmsweb.cern.ch though

<img width="885" height="891" alt="Image" src="https://github.com/user-attachments/assets/7643889e-2383-40a9-bd3b-49e62a7a40be" />

## Comment (belforte, 2025-10-14T08:06:47Z)

I do not mind the other way, am simply curious

## Comment (nausikt, 2025-10-14T08:15:10Z)

***cmsweb.cern.ch*** is origin, and will not suffering with CORS, unlike other **cmsweb-test\***.
P.S. Config/PSet was serving directly from webdir via cmsweb.cern.ch.

<img width="1078" height="640" alt="Image" src="https://github.com/user-attachments/assets/7b21dc52-d3b8-45e7-bbc8-f0a814833876" />

## Comment (nausikt, 2025-10-14T08:28:17Z)

We can mitigate this CORS meanwhile unifying things by serving Config/PSet the same way as TW/Upload log via pre-signed url approach. 

P.S. this way will also allow me to clean-up proxiedUrl and simplify code into single unified way of serving content that could works across ***cmsweb\****.
P.S The other way around would be to simply add cmsweb-test* to the allowed cross-origin list from main production **cmsweb.cern.ch/scheddmon** side.

Please, let me know your thoughts.

## Comment (belforte, 2025-10-14T08:46:13Z)

I am sorry but it is the first time I hear "CORS'. Anyhow it is fine to have a differnt look for cmsweb and cmsweb-test.
Simpler, unified code is always a plus, but you'd need to retrieve a tar from S3 and expand it inside the browser ... is that doable ? is it too much effort ? of course we could change things and store individual files, not tarball, but that may require changes in many places plus client/server synchronization.

maybe just leave it as it ?

## Comment (nausikt, 2025-10-14T09:09:28Z)

Got it, Stefano.

retrieve S3, expand, ... etc should be done on server side, but i see your point even its already have a boilerplate around, it's clearly not worth it, since its mostly tolerable and code base around this area is not crucial to be simplified.

I will open js code simplification and improving TW/Upload log retrieving UX as 1 click as a another low priority issue then.
