# dmwm/CRABServer issue #8550: new DN for cmscrab service account

State: closed
Opened: 2024-07-19T07:49:21Z
Closed: 2024-08-12T08:15:01Z
Labels: Status: In Progress, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8550

## Opening post (belforte, 2024-07-19T07:49:21Z)

Account is now owned by Stefano, instead of Dario [1]. That meant that certificate will  have a new DN (the owner HR id is part of it). From
* `DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = cmscrab, CN = 817881, CN = Robot: cms crab`
to
* `DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = cmscrab, CN = 373708, CN = Robot: cms crab`

The certificate which we are currently using expires on Nov 2 [2]

Here we track actions to be done

- [x] generate new certificate and add to `crab-secrets` [3]
- [x] add new DN to list of retrievers in our CRABServer config [gitlab commit](https://gitlab.cern.ch/crab3/CRAB3ServerConfig/-/commit/fe3c89500bafe328e08fab5ae322e86cbe3d95a1)
- [x] add new DN to CRIC [Done by Panos](https://cms-cric.cern.ch/accounts/account/detail/11851/)
- [x] add new DN to IAM . Done by Stefano  [4]
- [x] add new DN to those who can use Rucio `crab*` accounts [CMSTRANSF-947](https://its.cern.ch/jira/browse/CMSTRANSF-947)
- [x] add new DN to myproxy authorized retrieves. Fill [form](https://cern.service-now.com/service-portal?id=sc_cat_item&name=myproxy-registration-removal&se=myproxy-service) - [RFQ2750509](https://cern.service-now.com/service-portal?id=ticket&table=u_request_fulfillment&n=RQF2750509)
- [x] test that everything works with new DN
- [x] put new certificate's PEM files in the `tbag` [5] so that they will be used by all TW's with next puppet run

**Notes**

[1] Old owner should use [MyAccounts](https://account.cern.ch/account/Management/MyAccounts.aspx) page to transfer onwership. Select the service account, then croll down in that page to the button
![image](https://github.com/user-attachments/assets/df7f4d20-5eb1-434f-a9b4-699b799eec06)

[2]
```
LapSB:crab-secrets$ openssl x509 -noout -subject -dates -in service-account/20230929-cmscrab-robot.p12
Enter pass phrase for PKCS12 import pass phrase:
subject=DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = cmscrab, CN = 817881, CN = Robot: cms crab
notBefore=Sep 29 13:49:29 2023 GMT
notAfter=Nov  2 13:49:29 2024 GMT
LapSB:crab-secrets$ 
```

[3]
create cert at [CERN CA](https://ca.cern.ch/ca/user/Request.aspx?template=EE2Robot, download .p12) and the follow [cms-crab instructions](https://cmscrab.docs.cern.ch/technical/cmscrab-service-account.html#create-the-certificate-for-the-service-account).
Check
```
LapSB:crab-secrets$  openssl x509 -noout -subject -dates -in service-account/20240719-cmscrab-robot.p12
Enter pass phrase for PKCS12 import pass phrase:
subject=DC = ch, DC = cern, OU = Organic Units, OU = Users, CN = cmscrab, CN = 373708, CN = Robot: cms crab
notBefore=Jul 19 12:14:37 2024 GMT
notAfter=Aug 23 12:14:37 2025 GMT
LapSB:crab-secrets$ 
```

[4] Added to James Letts' list of certificate like done so far for all CRAB service certs. Waiting to be able to use service accounts for this

[5]
```text
tbag set --hg vocmsglidein/crabtaskworker --file <new_cmscrab_cert>.pem cmscrab_robotcert
tbag set --hg vocmsglidein/crabtaskworker --file <new_cmscrab_key>.pem cmscrab_robotkey
```

## Comment (belforte, 2024-08-11T16:26:12Z)

I am testing the new cert. in crab-dev-tw01. I am pointing to it for
- `config.Services.Rucio_cert/key``
- config.TaskWorker.cmscert/key`
- `config.MyProxy.serverhostcert/key`

and cleaned current credential cache to force myproxy retrieval.

## Comment (belforte, 2024-08-11T16:28:45Z)

a simple submission from my account worked
- [x] https://cmsweb-test2.cern.ch/crabserver/ui/task/240811_162343%3Abelforte_crab_20240811_182335

I have also sent Jenkins CCV +SST to test full Rucio ASO functionality as well
- [x] https://github.com/dmwm/CRABServer/issues/8609

## Comment (belforte, 2024-08-11T17:06:13Z)

I did not test Publisher, but a cert. that works for TW will work there as well

## Comment (belforte, 2024-08-12T08:15:01Z)

Everything works. Will replace in tbag
