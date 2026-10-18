# dmwm/CRABServer issue #9224: remove LDAP depenency

State: closed
Opened: 2025-10-20T14:24:00Z
Closed: 2026-01-30T13:05:33Z
Labels: Type: Enhancement, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/9224

## Opening post (belforte, 2025-10-20T14:24:00Z)

DagmanCreator uses LDAP to get content of e-group `highPrioUsers` in
https://github.com/dmwm/CRABServer/blob/bad7564a9705d2da18d31e21353f6a1482bd417c/src/python/TaskWorker/Actions/DagmanCreator.py#L1190-L1196

In that we allow for a list of high-prio e-groups to be passed in TW config file, but since years we only use
e-group `cms-crab-HighPrioUsers`

Info for that can be pulled from CRIC with an HTTP call https://cms-cric.cern.ch/api/accounts/group/query/?json
(maybe there's a way to retrieve only that group ?)

ALso, CRIC group can be populated from a list of e-groups, so we do not loose generality by sticking with CRIC group `CMS_CRAB_HighPrioUsers`

That will allow deprecating
https://github.com/dmwm/CRABServer/blob/9812df1e758317ea53af08d8e64a5d8cfd787d52/src/python/CMSGroupMapper.py#L20

and hence to remove dependency from LDAP

## Comment (belforte, 2026-01-28T14:14:11Z)

information can be retrieved for a single group:

On 28/01/2026 15:08, Panos Paparrigopoulos wrote:
> Hi Stefano,
>
> The name filter in the URL should do it:
>
> https://cms-cric.cern.ch/api/accounts/group/query/?json&name=CMS_CRAB3_Admin
>
> I hope that’s what you needed :) 
>
> Cheers,
> Panos
>
>> On 28 Jan 2026, at 15:07, Stefano Belforte <Stefano.Belforte@cern.ch> wrote:
>>
>> Hi, is there a way to qualify the URL
>>
>> https://cms-cric.cern.ch/api/accounts/group/query/?json
>>
>> so that it reports only the data for a given group ?
>>
>> Thanks
>>
>> Stefano
>>
>

## Comment (belforte, 2026-01-28T15:44:06Z)

so we have
```
}belforte@lxplus802/~> X5curl "https://cms-cric.cern.ch/api/accounts/group/query/?json&name=CMS_CRAB_HighPrioUsrs"
{
  "CMS_CRAB_HighPrioUsers": {
    "egroups": [
      "cms-crab-HighPrioUsers"
    ], 
    "last_modified": "2024-02-02T13:07:45.328702", 
    "name": "CMS_CRAB_HighPrioUsers", 
    "role": "high-priority-users", 
    "tag_name": "crab3", 
    "tag_relation": "group", 
    "users": []
  }
}belforte@lxplus802/~> 
```

Need to call this from python to parse the JSON. [WMCore CRIC](https://github.com/khurtado/WMCore/blob/master/src/python/WMCore/Services/CRIC/CRIC.py) class which we use does not have the group API and IIUC always insert a `&preset=" argument in the URL which the group API does not support.

## Comment (belforte, 2026-01-28T16:44:04Z)

Now that we have `requests` python package via PIP in our container, a simple implementation would be
```python
import requests
url="https://cms-cric.cern.ch/api/accounts/group/query/?json&name=CMS_CRAB_HighPrioUsers"
cert='/data/certs/robotcert.pem'
key='/data/certs/robotkey.pem'
r=requests.get(url,cert=(cert,key),verify=False)
```
after which
```
>>> r.json()
{'CMS_CRAB_HighPrioUsers': {'egroups': ['cms-crab-HighPrioUsers'], 'last_modified': '2024-02-02T13:07:45.328702', 'name': 'CMS_CRAB_HighPrioUsers', 'role': 'high-priority-users', 'tag_name': 'crab3', 'tag_relation': 'group', 'users': []}}
```
the `users` list will eventually contain a list of dicts, the key `login` will contain the user name. e.g.
```
>>> urlA="https://cms-cric.cern.ch/api/accounts/group/query/?json&name=CMS_CRAB3_Admin"
>>> r=requests.get(urlA,cert=(cert,key),verify=False)
/usr/local/lib/python3.8/site-packages/urllib3/connectionpool.py:1043: InsecureRequestWarning: Unverified HTTPS request is being made to host 'cms-cric.cern.ch'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
>>> for u in r.json()['CMS_CRAB3_Admin','users']: print(u['login'])
... 
belforte
>>> 
```

But I will also explore using `CRABServer/src/pyhton/RESTInteractions.py` in case it offers caching.

## Comment (belforte, 2026-01-28T17:50:45Z)

oh rats !!!

 CRABServer/src/pyhton/RESTInteractions.py does an urlQuote of the whole URL
https://github.com/dmwm/CRABServer/blob/bad7564a9705d2da18d31e21353f6a1482bd417c/src/python/RESTInteractions.py#L158-L159
but while
https://cms-cric.cern.ch/api/accounts/group/query/?json works,
https://cms-cric.cern.ch/api/accounts/group/query%3Fjson returns `code=404, reason=Not Found`

So it works fine with CRABServer, but can't be used here.
(commenting out that line makes things work, but I am not sure if some CRABServer call would break, maybe it was put there for a reason... the #2557 quoted in the comment does not correspond to anything in this GH repo)

I could look at using full blown WMCore/Service/Service which amounts to a small rewriting of WMCore's CRIC class 

Maybe I better stick with the simple `requests` and write a small caching on file myself.

## Comment (belforte, 2026-01-28T17:51:51Z)

this works
```python
import requests

TWCONFIG = '/data/srv/TaskManager/current/TaskWorkerConfig.py'
from WMCore.Configuration import loadConfigurationFile
cfg = loadConfigurationFile(TWCONFIG)
cert = cfg.TaskWorker.cmscert
key = cfg.TaskWorker.cmskey

url="https://cms-cric.cern.ch/api/accounts/group/query/?json&name=CMS_CRAB3_Admin"
r=requests.get(url,cert=(cert,key),verify=False)
print(r.json()['CMS_CRAB3_Admin','users'])
```

## Comment (belforte, 2026-01-30T10:13:12Z)

There is another LDAP dependency in looking for for a possible e-group which lists allowed local users in SITECONF
https://github.com/dmwm/CRABServer/blob/bad7564a9705d2da18d31e21353f6a1482bd417c/src/python/CMSGroupMapper.py#L93-L101

But no site is using `/cvmfs/cms.cern.ch/SITECONF/<site>/GlideinConfig/local-egroups.txt` so we can simply deprecate this !

## Comment (belforte, 2026-01-30T11:14:03Z)

New code is now in    https://github.com/belforte/CRABServer/tree/get-hiprio-users-from-cric-9224 and it works. LDAP dependency has been removed.

But we should add an in-memory caching layer to avoid querying CRIC too often.

## Comment (oljemark, 2026-02-09T12:54:49Z)

Hi, @belforte . Is #2557 this one (https://github.com/dmwm/WMCore/issues/2557), talking about spaces in CRAB URL's ?

## Comment (belforte, 2026-02-09T13:37:18Z)

Thanks @oljemark . I think you are right. And indeed the commit quoted as resolution at the end of that issue indicates that spaces were coming from the early CRAB3 implementation with RequestManager, which was later abandoned.
I have never seen spaces in any CRAB3 URL I dealt with.

So maybe we can remove that URL quoting in https://github.com/dmwm/CRABServer/blob/bad7564a9705d2da18d31e21353f6a1482bd417c/src/python/RESTInteractions.py#L158-L159 but all in all I would rather be conservative and stick with using `requests` for talking with CRIC. Hopefully new WMS tool will have better documented API's to being with,  which can be uses with modern Python clients w/o writing out own HTTP handlers.
