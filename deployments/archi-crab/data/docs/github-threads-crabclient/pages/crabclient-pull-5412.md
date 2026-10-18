# dmwm/CRABClient pull request #5412: Rest Interface curl parsing allowing HTTP2

State: closed
Opened: 2025-09-05T09:01:41Z
Closed: 2025-09-05T11:43:38Z
Merged: 2025-09-05T11:43:38Z
URL: https://github.com/dmwm/CRABClient/pull/5412

## Opening post (Lorenzov1999, 2025-09-05T09:01:41Z)

This PR weakens the conditions of the RegEx used to parse HTTP responses from the server (that at the moment requires a ".<minor version>" after HTTP), avoiding failures for HTTP2, which:
- may not have minor version
- don't provide reason next to the status code

A status code is generated from the http library, when missing.

Example outputs:
``` bash
2025-09-05 10:53 lvalenti@lxplus9106:~$ curl -v --http1.1 --cert /tmp/x509up_u156194 --key /tmp/x509up_u156194 -k https://cmsweb.cern.ch/crabserver/prod/info 2>&1 1>/dev/null | python3 parser.py
HTTP code=200, reason='OK'
2025-09-05 10:53 lvalenti@lxplus9106:~$ curl -v --http1.1 --cert /tmp/x509up_u156194 --key /tmp/x509up_u156194 -k https://cmsweb.cern.ch/crabserver/prod/fakeendpoint 2>&1 1>/dev/null | python3 parser.py
HTTP code=404, reason='Not Found'
2025-09-05 10:53 lvalenti@lxplus9106:~$ curl -v --http2 --cert /tmp/x509up_u156194 --key /tmp/x509up_u156194 -k https://cmsweb.cern.ch/crabserver/prod/fakeendpoint 2>&1 1>/dev/null | python3 parser.py
HTTP code=404, reason='Not Found'
2025-09-05 10:54 lvalenti@lxplus9106:~$ curl -v --http2 --cert /tmp/x509up_u156194 --key /tmp/x509up_u156194 -k https://cmsweb.cern.ch/crabserver/prod/info 2>&1 1>/dev/null | python3 parser.py
HTTP code=200, reason='OK'
```

Example of crab failing with HTTP2 due to the parser:
```
INFO:CRAB3.all:Fatal error trying to connect to https://cmsweb.cern.ch:8443/crabserver/prod/info?subresource=version using subresource=version.
exit code from curl = 0
HTTP code/reason = 9999/ .  stdout:
{"result": [
 ["3.3.19", "3.3.20", "v3", "development", "v3.250401"]
]}

Traceback (most recent call last):
  File "/data/hc/scr2.py", line 56, in <module>
    result = crabCommand('submit', config=config, proxy=proxy_path)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABAPI/RawCommand.py", line 28, in crabCommand
    return execRaw(command, arguments)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABAPI/RawCommand.py", line 51, in execRaw
    cmdobj = getattr(mod, command)(logger, args)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/Commands/submit.py", line 37, in __init__
    SubCommand.__init__(self, logger, cmdargs, disable_interspersed_args=True)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/Commands/SubCommand.py", line 409, in __init__
    self.checkversion()
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/Commands/SubCommand.py", line 455, in checkversion
    compatibleVersions = server_info(crabserver=self.crabserver, subresource='version')
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/ClientUtilities.py", line 692, in server_info
    dictresult, dummyStatus, dummyReason = crabserver.get(api, requestdict)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/RestInterfaces.py", line 279, in get
    return self.server.get(uri, data)
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/RestInterfaces.py", line 121, in get
    return self.makeRequest(uri=uri, data=data, verb='GET')
  File "/cvmfs/cms.cern.ch/share/cms/crab-prod/v3.250522.00/lib/CRABClient/RestInterfaces.py", line 225, in makeRequest
    raise RESTInterfaceException(stderr)
CRABClient.ClientExceptions.RESTInterfaceException:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 188.185.89.194:8443...
* Connected to cmsweb.cern.ch (188.185.89.194) port 8443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: /etc/pki/tls/certs/ca-bundle.crt
*  CApath: /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/etc/grid-security-emi/certificates
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.2 (IN), TLS header, Certificate Status (22):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [122 bytes data]
* TLSv1.2 (IN), TLS header, Finished (20):
{ [5 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [15 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Request CERT (13):
{ [7807 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [2064 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [36 bytes data]
* TLSv1.2 (OUT), TLS header, Finished (20):
} [5 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Certificate (11):
} [9958 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, CERT verify (15):
} [264 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [36 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: DC=ch; DC=cern; OU=computers; CN=cmsweb.cern.ch
*  start date: May  6 09:49:35 2025 GMT
*  expire date: Jun 10 09:49:35 2026 GMT
*  subjectAltName: host "cmsweb.cern.ch" matched cert's "cmsweb.cern.ch"
*  issuer: DC=ch; DC=cern; CN=CERN Grid Certification Authority
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x55b9a1cb8150)
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
> GET /crabserver/prod/info?subresource=version HTTP/2
> Host: cmsweb.cern.ch:8443
> user-agent: CRABClient/v3.250522
> accept: */*
> content-length: 19
> content-type: application/x-www-form-urlencoded
> 
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [10072 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 250)!
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* TLSv1.2 (OUT), TLS header, Unknown (23):
} [5 bytes data]
* We are completely uploaded and fine
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
< HTTP/2 200 
< cache-control: max-age=3600
< content-type: application/json
< date: Mon, 21 Jul 2025 07:41:36 GMT
< etag: "f121869c5a7547c1fb4ab8b0d5f17cb630de6d4e"
< response-proto: HTTP/1.1
< response-status: 200 OK
< response-status-code: 200
< response-time: 4.578157ms
< response-time-seconds: 0.004578663
< vary: Accept, Accept-Encoding
< x-content-type-options: bla
< x-rest-status: 100
< x-rest-time: 1632.929 us
< content-length: 72
< 
* TLSv1.2 (IN), TLS header, Unknown (23):
{ [5 bytes data]
100    91  100    72  100    19   2666    703 --:--:-- --:--:-- --:--:--  3370
* Connection #0 to host cmsweb.cern.ch left intact
{"result": [
 ["3.3.19", "3.3.20", "v3", "development", "v3.250401"]
]}
```

## Comment (cmsdmwmbot, 2025-09-05T09:02:02Z)

Can one of the admins verify this patch?

## Comment (Lorenzov1999, 2025-09-05T09:24:44Z)

To me it looks like this change wouldn't have impact on other things, but I am not sure if due to reasons on the CRABServer side it was a choice to only support http1.1

## Comment (nausikt, 2025-09-05T11:39:30Z)

Thank you @Lorenzov1999 for reaching out!

We've double checked & tested both regEx back then [1] and your new relaxed but generic & robust one [2]. 

We can confirm our shortcoming, and see no obvious reasons not to support all HTTP versions. (This chunk of code seems to be only place sensitive to http version)

So, I think we could safely merged this PR. @belforte 

Again. Thank you so much for your thoughtful patch and all these clarifications!

[1]
```
output: HTTP/1.1 404 Not Found -- extracted --> ['404', 'Not Found'], reason: Not Found
output: HTTP/1.1 200 OK -- extracted --> ['200', 'OK'], reason: OK
can't matched: HTTP/2 404
can't matched: HTTP/2 200
```
[2] The proposed extracting into `parts`, looks good and quite robust via filling missing reasons messages when not available.  
```
crab ❯ python test_regex.py
output: HTTP/1.1 404 Not Found -- extracted --> ['404', 'Not Found'], reason: Not Found
output: HTTP/1.1 200 OK -- extracted --> ['200', 'OK'], reason: OK
output: HTTP/2 404 -- extracted --> ['404'], reason: Not Found
output: HTTP/2 200 -- extracted --> ['200'], reason: OK
```

## Comment (belforte, 2025-09-05T11:43:30Z)

thanks @Lorenzov1999 and @sinonkt !! 
I do not think there ever was an intention not to be compliant with Http v2, but it is quite likely that when this code was written only Http v1 was around for testing.

merging

## Comment (belforte, 2025-09-05T11:55:36Z)

@Lorenzov1999 IIUC the problem was not "log is ugly" nor "console output is misleading" but "things do not work" !
Is that the case ?
If so.. why did we not catch in our tests ? are you using some new CMSSW release or non-standard environment ?

Besides curiosity, we need to know if to handle this as something to add to new release when we make it (we just deployed one this week and have no changes in the pipeline atm), or a critical bug to fix ASAP.

Thanks

## Comment (nausikt, 2025-09-05T12:24:54Z)

> @Lorenzov1999 IIUC the problem was not "log is ugly" nor "console output is misleading" but "things do not work" ! Is that the case ? If so.. why did we not catch in our tests ? are you using some new CMSSW release or non-standard environment ?
> 

@belforte , To answer your Second and Third questions. (not sure whether this is the case)

`curl` we got, provisioned from CMSSW environment [1] are strictly HTTP/1.1 only. as you can check via `curl -V | grep -Eo 'HTTP2|HTTP3'`.
[1]
```
[kphornsi@lxplus909 CRABClient]$ which curl
/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_20/external/el9_amd64_gcc12/bin/curl
```

On the other hand, `curl` on `lxplus` or my laptop in general. they support HTTP2 as default. as you can see in [2]

[2]
```
[kphornsi@lxplus909 ~]$ which curl
/usr/bin/curl
[kphornsi@lxplus909 ~]$ curl -V | grep -Eo 'HTTP2|HTTP3'
HTTP2
```

So, i guessed this might be the reasons why most of our tests passed because it's run in control env where there is specific `curl` underneath.

## Comment (Lorenzov1999, 2025-09-05T12:32:49Z)

Yes @belforte, the issue was indeed a "things do not work", but I confirm that, as @sinonkt pointed out, this happened while using CRAB outside of any CMS env.

Thank you both for the quick response!

## Comment (belforte, 2025-09-05T14:16:32Z)

thanks @Lorenzov1999 
I am amazed that CRAB could work outside CMS env (which indeeed is what we rely on to provide che python dependencies we have, among other things). I would expect that if $CMSSW* are not defined it fails miserably.
I will be very interested in knowing more about how you managed, maybe we can have an officially supported setup and add to our testing, at least for people using e.g. python3.

## Comment (Lorenzov1999, 2025-09-05T14:21:51Z)

This is just an attempt for the moment, but, if it turns out to be successful, I will remember to get in touch and discuss this further.

## Comment (Lorenzov1999, 2025-09-06T08:59:36Z)

@belforte

> Besides curiosity, we need to know if to handle this as something to add to new release when we make it (we just deployed one this week and have no changes in the pipeline atm), or a critical bug to fix ASAP.

Sorry, I missed this part.

It is not critical, so it is fine to wait for the next release if it is going to happen soonish.

But, if you plan no other changes in the near term, it would be helpful to have this fix released:)

## Comment (belforte, 2025-09-08T08:15:52Z)

OK @Lorenzov1999 , I have tagged client v3.250908 with this and queued for building https://github.com/cms-sw/cmsdist/pull/10063
In a couple of days it will be available as `crab-dev` in ITB
```
source /cvmfs/cms-ib.cern.ch/latest/cmsset_default.sh
cd CMSSW_....
cmsenv
crab-dev submit
```
I plan to wait for more changes which are now in the pipeline before creating a new crab-prod

CRABClient moves from ITB to "default CVMFS" when new CMSSW_15_1 is built.

## Comment (belforte, 2025-09-09T07:56:12Z)

@Lorenzov1999 this is now deployed in CMSSW Integration Build
```console
belforte@lxplus814/~> which crab-dev
/cvmfs/cms-ib.cern.ch/sw/x86_64/nweek-02906/common/crab-dev
belforte@lxplus814/~> crab-dev --version
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

CRAB client v3.250908
belforte@lxplus814/~> 
belforte@lxplus814/~> /cvmfs/cms-ib.cern.ch/sw/x86_64/latest/common/crab-dev --version
BEWARE: this is the development version of CRAB Client.
Be sure to have a good reason for using it

CRAB client v3.250908
belforte@lxplus814/~> 

```

## Comment (Lorenzov1999, 2025-09-10T07:15:06Z)

Thank you very much @belforte! :)
