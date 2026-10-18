# dmwm/CRABClient issue #5346: crab client does not respect X509_USER_PROXY

State: closed
Opened: 2024-11-05T09:29:18Z
Closed: 2024-11-05T10:44:10Z
URL: https://github.com/dmwm/CRABClient/issues/5346

## Opening post (smuzaffar, 2024-11-05T09:29:18Z)

While `crab submit --proxy $X509_USER_PROXY -c task.py` works [a] but fails when run without `--proxy $X509_USER_PROXY ` option [b]. Why crab does not check for `X509_USER_PROXY` env variable and use it as proxy if set ?

[a]
```
> crab submit --proxy $X509_USER_PROXY -c task.py 
Will use CRAB configuration file task.py
Importing CMSSW configuration /build/muz/x/CMSSW_14_2_X_2024-11-04-2300/pset.py
Finished importing CMSSW configuration /build/muz/x/CMSSW_14_2_X_2024-11-04-2300/pset.py
Sending the request to the server at cmsweb.cern.ch
Success: Your task has been delivered to the prod CRAB3 server.
Task name: 241105_092019:cmsbot_crab_1730798416
Project dir: ./crab_1730798416
Please use ' crab status -d ./crab_1730798416 ' to check how the submission process proceeds.
Log file is /build/muz/x/CMSSW_14_2_X_2024-11-04-2300/crab_1730798416/crab.log
```

[b]
```
> voms-proxy-info
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot/CN=1362862742
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmsbot/CN=545661/CN=Robot: CMS Build Bot
type      : RFC3820 compliant impersonation proxy
strength  : 2048
path      : /build/muz/x/x509_up31567
timeleft  : 11:49:14
key usage : Digital Signature, Key Encipherment
> crab submit -c task.py 
Will use CRAB configuration file task.py
Problems delegating My-proxy.
Error trying to create credential:
 Problems delegating My-proxy. Error executing export GT_PROXY_MODE=rfc ; myproxy-init -d -n -s myproxy.cern.ch -C ~/.globus/usercert.pem -y ~/.globus/userkey.pem -x -R '/DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=(817881|373708)/CN=Robot: cms crab|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1' -x -Z '/DC=ch/DC=cern/OU=computers/CN=crab-(preprod|prod)-tw(01|02).cern.ch|/DC=ch/DC=cern/OU=computers/CN=crab-dev-tw(01|02|03|04).cern.ch|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=(817881|373708)/CN=Robot: cms crab|/DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=crabint1/CN=373708/CN=Robot: CMS CRAB Integration 1' -l a89d85b5d3b5e016ca3701eebcb42631cde823ba -t 168 -c 720:00:

/bin/sh: myproxy-init: command not found

Log file is /build/muz/x/CMSSW_14_2_X_2024-11-04-2300/crab_1730798866/crab.log

```

## Comment (belforte, 2024-11-05T09:42:21Z)

crab client does use $X509_USER_PROXY
the problem here is that `myproxy-*` client is missing.

When using --proxy option, CRAB does not do any check on credentials and does not verify what's on myproxy. But in the "normal" mode it makes sure that there is a credential in myproxy.cern.ch valid long enough to run the task.

The $X509_USER_PROXY is only used to contact CMSWEB, but actual submision on the server side will be done with credentials retrieved from myproxy.cern.ch

I guess this is SL7, right ?

## Comment (belforte, 2024-11-05T09:43:07Z)

Let me know if you need more details and/or help to make things work for you.

## Comment (smuzaffar, 2024-11-05T10:06:26Z)

ah ok, yes , `myproxy-init` was missing. If I run `crab submit` in env where `myproxy` is available then it works.

As I was able to submit using `--proxy option`  (even though myproxy tools were missing) so I was wondering why crab does not make use of `X509_USER_PROXY` if set (it will be same as passing `--proxy option`)

## Comment (belforte, 2024-11-05T10:32:06Z)

I extended `--proxy` option to skip myproxy as well exactly because `myproxy-init` is missing in the EL7 container :-) 
can we close this ?
