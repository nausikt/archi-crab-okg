# dmwm/CRABServer issue #7894: Service certificate needed to authenticate against Rucio

State: closed
Opened: 2023-09-28T19:45:40Z
Closed: 2023-10-19T15:09:41Z
Labels: Priority: Critical
URL: https://github.com/dmwm/CRABServer/issues/7894

## Opening post (ericvaandering, 2023-09-28T19:45:40Z)

I now believe that the issue we experienced with Rucio on Sep 27/28 is that Apache on Alma9 (and/or its version of OpenSSL) is unwilling to accept host certificate as a client certificate. As far as I can tell, the two certs which have problems are host certs and all the certs which don't have problems are user or service account user certificates.

Alan is going to verify this with a new robot certificate he's obtained. If true, CRAB will need to do the same so that we are not held back from upgrading Rucio.

I have looked if there is a way to change this behavior on the Rucio side and have found nothing.

## Comment (belforte, 2023-09-28T20:28:50Z)

Dario, Wa, can you kindly follow up ? Thanks

Eric, our DN is
/DC=ch/DC=cern/OU=computers/CN=tw/crab-prod-tw01.cern.ch
note `CN=tw` which makes it a service certificate, not a host one.  Isn't that enough ?
Does Rucio/Alma want the "Robot" string in the DN ?

## Comment (ericvaandering, 2023-09-28T20:36:04Z)

Every one that fails has OU=computers. Every one that succeeds has OU=Users.

I tried explicitly today with your certificate and the Rucio robot certificate and removing all rucio tokens between attempts.

Both are fine with Rucio 1.31 (Centos 7). Rucio works OK on Rucio 32 (Alma 9), CRAB does not. 

One of the Rucio guys told me to check to make sure your certificate was not 1024 bits. It's not, it's 4096 while mine is only 2048. 

So I posit that there is *something* that the Apache/OpenSSL server does not like about OU=computers certificates and how they are generated or signed.

I have added a crab_input user to Rucio integration and we can test there before going back to the latest production.

## Comment (belforte, 2023-09-28T20:44:02Z)

Got it/ I see that Alan got
```
subject= /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmst1/CN=718748/CN=Robot: cms t1
```
so we need the same. @mapellidario @novicecpp you can check with him or Panos on how to get one for CRAB.
We also need to figure out if we want to use the same on all machines or have a few prod/preprod/test ones.

## Comment (ericvaandering, 2023-09-28T20:58:18Z)

Once you have them, please let me know the DNs and which accounts they belong to. We'll start with integration, as I said. 

Thanks for your cooperation!

## Comment (novicecpp, 2023-09-28T21:23:05Z)

Dario and I will take care tomorrow.

## Comment (mapellidario, 2023-09-29T14:27:07Z)

We have a robot certificate for our crab's service account `cmscrab`. I added the `.p12` file in the crab secrets repository together with the pwd to open it, then extracted it to cert+key in `crab-preprod-tw01`.

```plaintext
[crab3@crab-preprod-tw01 ~]$ export X509_USER_CERT=~/.globus/robocert.pem
[crab3@crab-preprod-tw01 ~]$ export X509_USER_KEY=~/.globus/robokey.pem
[crab3@crab-preprod-tw01 ~]$ openssl x509  -subject -dates -noout  -in $X509_USER_CERT
subject= /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=817881/CN=Robot: cms crab
notBefore=Sep 29 13:49:29 2023 GMT
notAfter=Nov  2 13:49:29 2024 GMT
```

However I am not sure what needs to be done now. How shall we properly map it to the service account in voms, cric and then rucio?

## Comment (belforte, 2023-09-30T11:09:27Z)

Mapping in RUcio rests with Rahul and/or Eric
I have now added it to VOMS to facilitate import in CRIC if/as needed. But am not sure whether Rucio requires that.
As long as we only plan to use this for Rucio, I guess we wait for more instructions from Eric

## Comment (ericvaandering, 2023-10-02T08:02:00Z)

Since it's been tested, I guess the next step is I add the DN to the production and you can switch at your leisure. Then, at some later point I can restore the auth server to the latest version and you will not notice. I've added the DN to all 4 CRAB accounts in production Rucio.

## Comment (belforte, 2023-10-02T09:46:31Z)

I am not sure that CRAB Robot cert. was tested with latest Rucio version on ITB.
Is e.g.  preprod running that way ? @mapellidario @novicecpp even if you wrote things in MatterMost, can you add a couple lines here ?

## Comment (belforte, 2023-10-02T09:50:24Z)

>  4 CRAB accounts in production Rucio.

Interesting ! I am aware of `crab_server`, `crab_tape_recall` and `crab_input`,what's the 4th one ? @ericvaandering

## Comment (ericvaandering, 2023-10-02T10:01:54Z)

`crab_test_group`

## Comment (novicecpp, 2023-10-02T10:33:24Z)

Thanks Eric. 
If we are not in hurry, I will switch CRAB Taskworker to use Robot cert next week.

## Comment (ericvaandering, 2023-10-02T11:13:44Z)

I'd really prefer to resolve this during this week if we can. What's the reason for picking next week?

## Comment (novicecpp, 2023-10-02T18:24:41Z)

Because we have O&C week, I usually avoid touching production when I do not have full time focus on it. 
But sure, we can do it this week.

## Comment (novicecpp, 2023-10-02T18:25:35Z)

I switched TW to robot cert on preprod (CRAB integration test server), and it works fine.
I also tested with Rucio CLI for all accounts and found it did not work with `crab_test_group`, but it is fine because it is not used in TW.

## Comment (novicecpp, 2023-10-02T18:28:24Z)

I will switch the production on this Wednesday.

## Comment (belforte, 2023-10-02T18:51:13Z)

AFAICT crab-preprod-tw01 is using robot cert, but pointing to standard (production) Rucio server at `cms-rucio`
```
[crab3@crab-preprod-tw01 current]$ openssl x509 -noout -subject -in /data/certs/robotcert.pem
subject= /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=cmscrab/CN=817881/CN=Robot: cms crab
[crab3@crab-preprod-tw01 current]$ grep -i rucio TaskWorkerConfig.py 
config.Services.Rucio_host = 'https://cms-rucio.cern.ch'
config.Services.Rucio_account = 'crab_server'
config.Services.Rucio_authUrl = 'https://cms-rucio-auth.cern.ch'
config.Services.Rucio_caPath = '/etc/grid-security/certificates/'
config.Services.Rucio_cert = '/data/certs/robotcert.pem'
config.Services.Rucio_key = '/data/certs/robotkey.pem'
```
I thought we want to test with new Rucio version on Rucio integration server.
I see that there is a `TaskWorkerConfig-test.py` there which points to Rucio `int`, but it is not what's being used
```
crab3       14  0.1  0.2 426712 36296 pts/0    Sl+  19:51   0:04 python3 /data/srv/TaskManager/v3.230921-839a45450c3aae116b7f80aa57567361/slc7_amd64_gcc630/cms/crabtaskworker/v3.230921-839a45450c3aae116b7f80aa57567361/lib/python3.8/site-packages/TaskWorker//MasterWorker.py --config /data/srv/TaskManager/current/TaskWorkerConfig.py --logDebug
```

Maybe I am simply confused ?

## Comment (novicecpp, 2023-10-02T19:37:56Z)

I already tested with integration server on both TW and Jupyter when [Eric asked us](https://mattermost.web.cern.ch/cms-o-and-c/pl/ncko6x95hbfipf3brs6wsteubc) to test.

https://cmsweb-testbed.cern.ch/crabserver/ui/task/230929_155845%3Atseethon_crab_hc_1kj_preprod_20230929_175843
(Note that it SUBMITFAILED due to my account do not have write permission to integration area in CERN EOS)

## Comment (belforte, 2023-10-02T20:04:32Z)

thanks for reassuring me

## Comment (ericvaandering, 2023-10-03T12:16:54Z)

I added the certificate to crab_test_group. I issued the command before, so I'm not sure why it wasn't there. Now I issued the command AND checked the results!

## Comment (belforte, 2023-10-09T19:37:13Z)

@ericvaandering CRAB TaskWorker is now running with the robot cert. and the fix for automatic splitting. We are ready for you to switch production Rucio server to new version at your convenience.

## Comment (belforte, 2023-10-09T19:38:51Z)

We can close this after upgrade is done and things keep working :-)

## Comment (ericvaandering, 2023-10-09T19:39:59Z)

Great. Thank you! WMAgent is not ready just yet. I think we are targeting Wednesday.

## Comment (belforte, 2023-10-19T15:09:42Z)

All done and working
