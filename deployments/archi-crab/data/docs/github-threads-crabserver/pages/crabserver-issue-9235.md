# dmwm/CRABServer issue #9235: local group not added anymore to My.CMSGroups ?

State: closed
Opened: 2025-11-19T13:14:26Z
Closed: 2026-04-30T14:51:49Z
Labels: Status: In Progress, Area: Code Cleanup, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9235

## Opening post (belforte, 2025-11-19T13:14:26Z)

There at least one case where the user membership in local groups is not added to `CMSGroups` classAd
See https://cms-talk.web.cern.ch/t/issue-with-processing-private-mc-samples-using-crab/138451/4

pasting here most relevant text
```text
 matching doesnt work because of stringListsIntersect(CMSGroups,“T3_US_FNALLPC”)`

The user is among the local users at LPC:

[mmascher@vocms0106 ~]$ grep jingyu /cvmfs/cms.cern.ch/SITECONF/T3_US_FNALLPC/GlideinConfig/local-users.txt
jingyu

```

As @mmascher pointed out,  CRAB should be setting the group information here? https://github.com/dmwm/CRABServer/blob/b84f876e8c0acc51c27318f846a668c25b03e0a2/src/python/TaskWorker/Actions/DagmanCreator.py#L405-L408

## Comment (belforte, 2025-11-19T14:00:13Z)

as simple as "/cvmfs" is not mounted inside the container.
```
crab3@crab-prod-tw01:/data/srv/TaskManager$ ls -ld /cvmfs
drwxr-xr-x. 2 root root 0 Aug 21 15:43 /cvmfs
crab3@crab-prod-tw01:/data/srv/TaskManager$ ls -ld /cvmfs/cms.cern.ch/
ls: cannot access '/cvmfs/cms.cern.ch/': No such file or directory
crab3@crab-prod-tw01:/data/srv/TaskManager$ 
```

## Comment (belforte, 2025-11-19T17:03:16Z)

It turned out to be the old problem that at times the mount of CVMFS inside the container goes belly up.
I fixed it by restarting the container (`docker stop; docker start`) on prod and canary TW.
The more drastic procedure described in https://cmscrab.docs.cern.ch/crab-components/crab-taskworker/how-to.html#cvmfs-failed-to-mount to address the case when CVMFS fails at "VM-level" was not necessary.

We can do a few things, not necessarily one excluding the other:
1. find a way to set an alert/alarm so that we do not run long time with this
2. ask CVMFS support if there is more robust solution than fuse mount, like https ? (all in all CMVFS can be cached via squid)
3. bypass CVMFS, clone https://gitlab.cern.ch/SITECONF in the container and do a periodic `git pull` (e.g. when memory cache expires, see code in [CMSGroupMapper.py](https://github.com/dmwm/CRABServer/blob/0ac5f0097f4d11af2a97caadeb886bf9f6118ec6/src/python/CMSGroupMapper.py#L51)
4. do 3. in the VM in /data disk, refresh via crontab and mount the local directory in the container
5. like 4. but instead of clone/fetch, do a straight `cp` from CVMFS
6. like 5. but only propagate changes
   * ` rsync -av /cvmfs/cms.cern.ch/SITECONF/ /data/container/SITECONF/`
   * inside the container that is available as `/data/hostdisk/SITECONF/` so we should modify the code https://github.com/dmwm/CRABServer/blob/3f5c584e274884c08139fb5662cb0d5f79e48e95/src/python/CMSGroupMapper.py#L65
     

FYI @aspiringmind-code  I defer to you on deciding how to proceed

## Comment (belforte, 2025-11-19T17:04:25Z)

keeping open until a follow-up strategy is defined and ad-hoc issue(s) opened.

## Comment (belforte, 2025-11-19T19:50:06Z)

@aspiringmind-code about 1. the place where to catch the problem could be
https://github.com/dmwm/CRABServer/blob/0ac5f0097f4d11af2a97caadeb886bf9f6118ec6/src/python/CMSGroupMapper.py#L65-L73
where today `os.path.isdir(base_dir)` was simply returning `False`. No exception raised and no action taken.

## Comment (belforte, 2025-11-20T08:48:07Z)

the clear symptom was that `ls` inside the container showed no directory
so maybe a simple alert could be crontab in the TW which does something like
`docker exec -ti TaskWorker ls /cvmfs/cms.cern.ch/SITECONF`
and prints to stdout  in case of error, generating a mail to operators

e.g.
```
belforte@crab-dev-tw04/~> docker exec -ti TaskWorker ls /cvmfs/cms.cern.ch/SITECONF
ls: cannot access '/cvmfs/cms.cern.ch/SITECONF': No such file or directory
belforte@crab-dev-tw04/~> 
```
even if the first time I executed it returned nothing, the second the error.

## Comment (belforte, 2026-01-20T15:30:59Z)

In December @nausikt has added a crontab to alert if SITECONF access is lost inside the container (option 1.)
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/master/code/manifests/crabtaskworker/checksiteconf.pp?ref_type=heads

we should decide if to stay with that, or to bypass mounting CVMFS mounting inside the container via option 5.

## Comment (belforte, 2026-02-13T15:07:26Z)

The problem has not occurred again since November, so I am not sure if it is worth pursuing. If we moved cmvfs reading into a local (disk or memory) caching we could simply put an error reporting in there and fall back to stale cache. Current code in `CMSGroupMapper.py` "looks like doing memory caching", but in reality it does not as described in https://github.com/dmwm/CRABServer/issues/9270#issuecomment-3834561226

What I would not like to do is to raise a fatal exception inside every `crab submit` given that most submission do not care about having the local group added to the JDL.

Maybe we should pursue the creation of a global caching object at TW startup time, pass it to all subprocesses, and in there take care of cache refreshing. We can certainly detect a too much stale cache there, the question is what to do. I would like to e.g. send a mail to operators, but am currently failing to do this inside the container. @aspiringmind-code @nausikt any suggestion ? Or is your preference for forgetting about this.

Or maybe log the issue in twlog, catch in in logstash and raise an alert in Grafana  ? That'd be sort of the "ideal" patch, but we do not have a well established procedure (i.e. instructions for dummies) so I am a bit scared of getting lost.

The alternative is of course to setup crontab in the VM, so we do get mails, and avoid using cvmfs at all inside the container.

## Comment (nausikt, 2026-02-13T15:56:39Z)

> The problem has not occurred again since November, so I am not sure if it is worth pursuing. If we moved cmvfs reading into a local (disk or memory) caching we could simply put an error reporting in there and fall back to stale cache. Current code in `CMSGroupMapper.py` "looks like doing memory caching", but in reality it does not as described in [#9270 (comment)](https://github.com/dmwm/CRABServer/issues/9270#issuecomment-3834561226)
> 

I like the way we reading cvmfs into a local disk first then directly mounted it to the container, its does decoupling us from any unstable mounting issue. (not sure you means we gonna have crontab to periodically moved to local disk twice a day or something?) 
> 
> Maybe we should pursue the creation of a global caching object at TW startup time, pass it to all subprocesses, and in there take care of cache refreshing. We can certainly detect a too much stale cache there, the question is what to do. I would like to e.g. send a mail to operators, but am currently failing to do this inside the container. [@aspiringmind-code](https://github.com/aspiringmind-code) [@nausikt](https://github.com/nausikt) any suggestion ? Or is your preference for forgetting about this.
> 

The global caching object is intriguing to me as a generic caching mechanism. Especially if we have many attrs worth caching that also shared across TW actions. But right now i saw just one `/cvmfs/cms.cern.ch/SITECONF` for CMSGroups resolving. (**CRIC calls seems to already have their own http caching mechanism wrapped.)

So IMHO, if we find few more worthy attrs to cache... then i think its worth to let me pursue the ideal solution. 
*P.S. alternative also fine for me!*

## Comment (belforte, 2026-02-13T16:35:20Z)

thanks @nausikt . I'll be happy to work on the "extra config caching module" (as often,  hardest part is to find a good name). If I only could solve the `mail` problem !

## Comment (belforte, 2026-02-13T16:52:05Z)

sending mail was solved thanks to [tip](https://mattermost.web.cern.ch/cms-o-and-c/pl/7amnio8j9bykmq9pif6mszpmra) from  @juanpablosalas and [example](https://docs.python.org/3/library/email.examples.html) in python doc 
here's the incantation
```text
crab3@crab-dev-tw01:/data/srv/TaskManager$ python3
Python 3.8.16 (default, May 23 2023, 14:26:40) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from email.message import EmailMessage
>>> msg = EmailMessage()
>>> msg['Subject'] = "this is a test"
>>> msg['to']="stefano.belforte@cern.ch"
>>> msg['from']="TW-noreply@cern.ch"
>>> msg.set_content("do not reply. Ignore!")
>>> print(msg)
Subject: this is a test
to: stefano.belforte@cern.ch
from: TW-noreply@cern.ch
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0

do not reply. Ignore!

>>> import smtplib
>>> s = smtplib.SMTP(host='cernmx.cern.ch', port=25)
>>> s.send_message(msg)
{}
>>> s.quit
```
and this is my Thunderbird window

<img width="324" height="154" alt="Image" src="https://github.com/user-attachments/assets/27c9ea8d-8168-4aeb-aa61-5dbbb0d3c7b2" />

## Comment (belforte, 2026-02-13T17:42:30Z)

> (**CRIC calls seems to already have their own http caching mechanism wrapped.)

like for CMSGroupMapper.py, this does not work in our case because every TW action is called in its own subprocess, so objects do not persist  in memory from one `crab submit` to the next. We need to put them explicitly among the `args` in the child intiialization
https://github.com/dmwm/CRABServer/blob/7aca6b02074c205a4d44f68118d14734d8e8a28c/src/python/TaskWorker/Worker.py#L105-L106
https://github.com/dmwm/CRABServer/blob/7aca6b02074c205a4d44f68118d14734d8e8a28c/src/python/TaskWorker/ChildWorker.py#L50-L51

## Comment (nausikt, 2026-02-13T18:30:07Z)

Stefano please allows me to clarify. IIUC, In case of CRIC calls, since we've derived from WMCore CRIC Service. 
I think its implicitly been ***file-based caching***.
## on CRAB Side
Every calls goes through the derived **_getResult** function as you can see below.
https://github.com/dmwm/CRABServer/blob/7aca6b02074c205a4d44f68118d14734d8e8a28c/src/python/TaskWorker/WorkerUtilities.py#L16-L18

https://github.com/dmwm/CRABServer/blob/7aca6b02074c205a4d44f68118d14734d8e8a28c/src/python/TaskWorker/WorkerUtilities.py#L131-L143

## on WMCore Side
Then Implicitly in [WMCore/Services/CRIC/CRIC.py](https://github.com/dmwm/WMCore/blob/c11eef48bbd189affcd683aaf5a344ae475d17a4/src/python/WMCore/Services/CRIC/CRIC.py#L60-L71) which inherited [WMCore/Services/Service.py](https://github.com/dmwm/WMCore/blob/master/src/python/WMCore/Services/Service.py)
```python
    def _getResult(self, uri, callname="", args=None, unflatJson=True):
        """
        Either fetch data from the cache file or query the data-service
        :param metricNumber: a number corresponding to the SSB metric
        :return: a dictionary
        """
        cachedApi = "%s.json" % callname
        apiUrl = '%s?json&preset=%s' % (uri, callname)

        self['logger'].debug('Fetching data from %s, with args %s', apiUrl, args)
        # need to make our own encoding, otherwise Requests class screws it up
        if args:
            apiUrl = "%s&%s" % (apiUrl, urlencode(args, doseq=True))

        data = self.refreshCache(cachedApi, apiUrl)
        results = data.read()
        data.close()

        results = json.loads(results)
        if unflatJson:
            results = unflattenJSON(results)
        return results
```
It does check cache hit/expired, call/read/write cache file behind the scene through **refreshCache** function.
as we can see below with default=1hr.
```python
def refreshCache(self, cachefile, url='', inputdata=None, openfile=True,
                     encoder=True, decoder=True, verb='GET', contentType=None, incoming_headers=None, binary=False):
        """
        See if the cache has expired. If it has make a new request to the
        service for the input data. Return the cachefile as an open file object.
        If cachefile is None returns StringIO.

        :param cachefile: cache file name
        :param url: url value
        :param inputdata: HTTP (JSON) payload string
        :param openfile: flag to use open file, boolean
        :param encoder: flag to use encoder, boolean
        :param decoder: flag to use decode, boolean
        :param verb: HTTP method, string
        :param contentType: HTTP content type value, string
        :param incoming_headers: set of HTTP headers, dict
        :param binary: use binary mode to decode HTTP data, boolean
        :return: either file object or StringIO
        """
        inputdata = inputdata or {}
        incoming_headers = incoming_headers or {}
        verb = self._verbCheck(verb)

        cachefile = self.cacheFileName(cachefile, verb, inputdata)

        if cache_expired(cachefile, self["cacheduration"]):
            self.getData(cachefile, url, inputdata, incoming_headers, encoder, decoder, verb, contentType, binary=binary)
        else:
            self['logger'].debug('Data is from the Service cache')

        # cachefile may be filename or file object
        if openfile and not isfile(cachefile):
            if binary:
                return open(cachefile, 'rb')
            return open(cachefile, 'r', encoding='utf-8')
        else:
            return cachefile
```
Thus, i believe its likely been cached across TW action's subprocesses.
*P.S. I used to test individual TW Action with cache_duration=few seconds, and see how its works back then. its generated
an intermediate cache file and been reused well, no http calls were requested.*

## Comment (belforte, 2026-02-13T20:39:23Z)

🙇‍♂️ 
thanks @nausikt 
I humbly bow. I had written w/o checking. My bad. I apologize for having turned my brain off. Very good to have you here  :-)

## Comment (nausikt, 2026-02-14T15:58:09Z)

@belforte humbly bow🙇‍♂️ (Thanks) to you! for having me on your board!

## Comment (belforte, 2026-02-19T16:01:19Z)

recap of what we agreed on (somehow each step is predicated on the one before)

- [x]  introduce a crontab in puppet which `rsync`'s `SITECONF` from `cvmfs` to `/data/container/TaskWorker/groups/SITECONF` (a directory) and get lilst of highpriority users from CRIC into `/data/container/TaskWorker/groups/highPriorityUsers.json` (a file)
    - [x] in `crabdev` env for developing/finalizing
    - [x] in `qa` for testing 
    - [x] in `prod`
- [x]  change code to read from there. Reading from local disk during each submit handling is no problem, no need for memory caching, so we minimize changes. Current master already does not use `config.TaskWorker.highPrioEgroups = ['cms-crab-HighPrioUsers']` in TW config.
   - [x] code and test #9278 . Merged but not  in [v3.260226](https://github.com/dmwm/CRABServer/releases/tag/v3.260226) 
   - [x] create new tag with it - v3.260330
   - [x] deploy - in canary since April 7 - in production (v3.260415) since April 15
   - [x] remove from puppet ```code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb
161:config.TaskWorker.highPrioEgroups = ['cms-crab-HighPrioUsers']``` 
- [x] remove from puppet current crontab ` class { 'hg_vocmsglidein::crabtaskworker::checksiteconf': }`
     - [x] in qa https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/445 
     - [x] in master
- [x] stop mounting of CVMFS inside the container (change runContainer.sh) #9308 

@aspiringmind-code @nausikt do you agree with this ? Did I miss something ?

## Comment (nausikt, 2026-02-19T21:07:25Z)

I agree. 

For clarity, about CRIC in 1. you mean we gonna have another cron to periodically fetch `highPrioEgroups ` from CRIC as file?
such that its more dynamic an up-to-date than previous method, propagating via puppet through TW config?

## Comment (belforte, 2026-02-20T09:43:46Z)

I am simply stating the fact that we will never use anything else than current high priority e-group for setting high priority in submissions. It has been like that since years. We never changed what's in  `config.TaskWorker.highPrioEgroups = ['cms-crab-HighPrioUsers']` since it was first introduced 🤷 
If really needed, it will be simple enough to change the crontab.

## Comment (aspiringmind-code, 2026-02-20T10:03:17Z)

> [@aspiringmind-code](https://github.com/aspiringmind-code) [@nausikt](https://github.com/nausikt) do you agree with this ? Did I miss something ?
Agreed. Sounds good. Thanks!

## Comment (belforte, 2026-04-22T13:18:54Z)

the new way is now implemented in production, all that is left is to cleanup obsolete crontab and remove obsolete mounting in runContainer.sh as per https://github.com/dmwm/CRABServer/issues/9235#issuecomment-3928199878

## Comment (belforte, 2026-04-30T14:51:49Z)

All actions defined in https://github.com/dmwm/CRABServer/issues/9235#issuecomment-3928199878 have been completed now. This can be closed.
