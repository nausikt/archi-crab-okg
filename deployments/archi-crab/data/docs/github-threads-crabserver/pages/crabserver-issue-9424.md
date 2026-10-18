# dmwm/CRABServer issue #9424: change Oracle passwords after Oct 1, 2026

State: open
Opened: 2026-09-18T15:37:36Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9424

## Opening post (belforte, 2026-09-18T15:37:36Z)

Dear CERN Oracle Community,

Please take a moment to  read the following Service Change announcement, oriented towards making Oracle account passwords compliant with the CERN Password Rules.


https://cern.service-now.com/service-portal?id=outage&n=OTG0163272


Important dates to remember :

1-Oct-2026 Password validation campaign starts for PROD and non-PROD databases

11-Jan-2026 Campaign ends for non-PROD databases

5-Apr-2027 Campaign ends for PROD databases

Warning: accounts whose password have not been validated/verified will be locked.

Please take notice of potential impact when the clients use very old Oracle client libraries (older than 12c).

Please contact oracle.support@cern.ch if you have further questions

Nilo Segura
On behalf of the Oracle Support Team : IT/DA

## Comment (belforte, 2026-09-18T15:38:33Z)

I have sent this to Kate


Subject: 	Re: CERN Oracle databases password verification campaign to start 1-Oct-2026
Date: 	Fri, 18 Sep 2026 17:35:40 +0200
From: 	Stefano Belforte <stefano.belforte@cern.ch>
To: 	Katarzyna Maria Dziedziniewicz-Wojcik <katarzyna.maria.dziedziniewicz@cern.ch>
CC: 	stefano.belforte@cern.ch


Hi Kate,

I will surely take care schema-owner passwords for accounts
which I own  (i.e. all DB's used by CRAB),
but how should we handle the special accounts
 cms_analysis_reqmgr_r and cms_analysis_reqmgr_w 
which we use to read / write in cms_analysis_reqmgr@cmsr ?
They have passwords whith "never expires" and I have no clue
how to change. Yet those are not compliant with current rules (too short).

Thanks

Stefano

## Comment (belforte, 2026-09-18T19:38:03Z)

reply from Kate is fully reassuring

 Ciao Stefano,

Yes, all the passwords will need to be changed, the unexpiring ones too. We will help track what's using the wrong password (hosts, IPs, os usernames etc). There will be views available to check it, otherwise I can always help. We'll figure this out. We will also implement a grace period when both passwords work to allow smoother transition.

Cheers,
Kate
