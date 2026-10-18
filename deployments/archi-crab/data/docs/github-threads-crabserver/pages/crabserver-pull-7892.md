# dmwm/CRABServer pull request #7892: restcache, download sandbox - check username present if not upload

State: closed
Opened: 2023-09-25T09:55:46Z
Closed: 2023-10-02T09:27:25Z
Merged: 2023-10-02T09:27:25Z
URL: https://github.com/dmwm/CRABServer/pull/7892

## Opening post (mapellidario, 2023-09-25T09:55:46Z)

Related to #6540 

While developing the command `crab getsandbox`, I made by mistake a call that made the crabserver fail with an http error 500. I do not think that our production code ever makes suche a request, but it would be better to make the crabserver fail properly.

Basically, it is possible that `ownerName` is empty and that the line `objectPath = ownerName + '/sandboxes/' + tarballname` fails with "can append string to None".

## Comment (cmsdmwmbot, 2023-09-25T09:59:25Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 4 warnings and errors that must be fixed
   * 2 warnings
   * 16 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1713/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-09-25T12:04:01Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 1 warnings and errors that must be fixed
   * 2 warnings
   * 13 comments to review
 * Pycodestyle check: succeeded
   * 3 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1714/artifact/artifacts/PullRequestReport.html

## Comment (mapellidario, 2023-09-25T12:13:02Z)

I will not fix the warning about

https://github.com/dmwm/CRABServer/blob/84ea9f28d724b4999fc0d80d18ff4fdcd7336491/src/python/CRABInterface/RESTCache.py#L189-L190

I am not sure if the content of the file is really text and not binary, and i am not sure it is worth checking

## Comment (belforte, 2023-09-25T12:44:47Z)

shouldn't we rather catch such problems in the REST args validation step https://github.com/dmwm/CRABServer/blob/a389d295e7efd6e4c5d21b9bdc3826e0f0485bb4/src/python/CRABInterface/RESTCache.py#L93

## Comment (belforte, 2023-09-25T12:50:48Z)

about https://github.com/dmwm/CRABServer/pull/7892#issuecomment-1733575213 (which I agree with)
I think is better to put this note as a comment in the code and add a `  # pylint: disable=...` to line 189

## Comment (mapellidario, 2023-09-26T09:31:52Z)

I replicated the error [1] using

```python
           downloadFromS3(crabserver=self.crabserver,
                        filepath=localSandboxPath,
                        objecttype='sandbox', logger=self.logger,
                        tarballname=sandboxFilename, 
                        # username=username
                        )
```

Indeed it is strange that `validation()` did not complain, I will have a look

---

[1]

<details>

```plaintext
[26/Sep/2023:11:28:50]  SERVER DATABASE ERROR 500/403 Execution error __builtins__.TypeError e08c00a28b3fa0aab1e64bc8f5ec739d [instance: devtwo] (unsupported operand type(s) for +: 'NoneType' and 'str'); last statement: None; binds: None, None; offset: None - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]    Traceback (most recent call last): - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]      File "/data/srv/HG2309a-f777499c9b3e957c44b9e3d0eedbf9bf/sw.crab_master/slc7_amd64_gcc630/cms/crabserver/v3.230921-bc8b2be3edf40cd586c7b14d2ff961e0/lib/python3.8/site-packages/WMCore/REST/Server.py", line 1797, in dbapi_wrapper - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]        return handler(*xargs, **xkwargs) - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]      File "/data/srv/HG2309a-f777499c9b3e957c44b9e3d0eedbf9bf/sw.crab_master/slc7_amd64_gcc630/cms/crabserver/v3.230921-bc8b2be3edf40cd586c7b14d2ff961e0/lib/python3.8/site-packages/CRABInterface/RESTCache.py", line 118, in get - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]        objectPath = ownerName + '/sandboxes/' + tarballname - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50]    TypeError: unsupported operand type(s) for +: 'NoneType' and 'str' - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
[26/Sep/2023:11:28:50] crabserver-7877fb5d9c-62zzn 128.141.161.154:34982 "GET /crabserver/devtwo/cache?subresource=download&objecttype=sandbox&tarballname=67f92c1368a1d8fdae9a57173b0d150d8fb17bcae61c77a9f5a78263fe53cff0.tar.gz HTTP/1.1" 500 Internal Server Error [data: 13052 in 745 out 435045 us ] [auth: ok "/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=dmapelli/CN=817881/CN=Dario Mapelli" "" ] [ref: "https://cmsweb-test11.cern.ch" "CRABClient/development" ] - Podname=crabserver-7877fb5d9c-62zzn Type=cherrypylog
```

</details>

## Comment (mapellidario, 2023-09-26T13:40:41Z)

Ok, found it.

when calling without passing a username [1], the line

```python
            validate_str('username', param, safe, RX_USERNAME, optional=True)
```

Adds `"username" = None` to the arguments [2], since we specify `optional=True`.

This is why i think we need to add additional checks to make sure that the username is properly set when we actually need it.

[1]

<details>

both

```python
            downloadFromS3(crabserver=self.crabserver,
                        filepath=localSandboxPath,
                        objecttype='sandbox', logger=self.logger,
                        tarballname=sandboxFilename, 
                        # username=username
                        username=""
                        )
```

and

```python
            downloadFromS3(crabserver=self.crabserver,
                        filepath=localSandboxPath,
                        objecttype='sandbox', logger=self.logger,
                        tarballname=sandboxFilename, 
                        # username=username
                        )
```

give the same result, because if `username=""` the

https://github.com/dmwm/CRABServer/blob/84ea9f28d724b4999fc0d80d18ff4fdcd7336491/src/python/ServerUtilities.py#L761-L762

do no set the username argument and the query to the server is same as the username has not been set.

</details>

[2]

<details>

```plaintext
(Pdb) param
RESTArgs(args=[], kwargs={'subresource': 'download', 'objecttype': 'sandbox', 'tarballname': 'd2d9aa4fbc541eb86e77896e6f9194239bc25046a00e793d6c338a21e88d50bc.tar.gz'})
(Pdb) safe
RESTArgs(args=[], kwargs={})
(Pdb) c
--Return--
> /data/repos/CRABServer/src/python/CRABInterface/RESTCache.py(98)validate()->None
-> validate_str('subresource', param, safe, RX_SUBRES_CACHE, optional=False)
(Pdb) param
RESTArgs(args=[], kwargs={})
(Pdb) safe
RESTArgs(args=[], kwargs={'subresource': 'download', 'objecttype': 'sandbox', 'taskname': None, 'username': None, 'tarballname': 'd2d9aa4fbc541eb86e77896e6f9194239bc25046a00e793d6c338a21e88d50bc.tar.gz'})
(Pdb)
```

</details>

## Comment (belforte, 2023-09-27T22:22:53Z)

does `username=""` fail even if you specify `optional=False`
I am not questioning the need, simply it would be good to have all validation in the validate method

## Comment (belforte, 2023-09-29T09:48:51Z)

I was picky w/o having looked properly at the code. Sorry.
This is good, thanks

## Comment (mapellidario, 2023-10-02T09:27:02Z)

> does username="" fail even if you specify optional=False

yeah, because as mentioned in the details under [1] in https://github.com/dmwm/CRABServer/pull/7892#issuecomment-1735566976 , when we use `username=""` the client does not even set the argument in the request, so the validation with `optional=False` fails.

Moreover i do not think we can simply set `optional=False`, because the subresource "upload" does not need it [1] and we would need to change the client code to add it.

In any case, thanks for checking, I will merge this

---

[1] https://github.com/dmwm/CRABServer/blob/84ea9f28d724b4999fc0d80d18ff4fdcd7336491/src/python/CRABInterface/RESTCache.py#L127
