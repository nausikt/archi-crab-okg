# dmwm/CRABServer issue #8126: fix mail sending from our VM

State: closed
Opened: 2023-12-19T21:12:43Z
Closed: 2024-03-13T14:20:01Z
Labels: Status: On Hold, Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8126

## Opening post (belforte, 2023-12-19T21:12:43Z)

@mapellidario @novicecpp can you kindly take care ? I never understood how those mails from "root user" of
our VM's are configured and where we should put our hands in puppet for this. AFAICT we
define the "To:" only as argument to `sendmail::root_email: ` puppet "thing". Maybe you can get some help
from someone at CERN who knows puppet ?

-------- Forwarded Message --------
Subject: 	[Action needed] Incorrect configuration of FROM address in automatic e-mails
Date: 	Tue, 19 Dec 2023 15:27:03 +0100
From: 	mail.mailing@cern.ch
Reply-To: 	service-desk@cern.ch
To: 	cms-service-crab3htcondor-admins@cern.ch



Dear E-GROUP CMS-SERVICE-CRAB3HTCONDOR-ADMINS,

You receive this e-mail because you are responsible for one or more devices which sends e-mails through CERNMX.cern.ch and those e-mails are violating e-mail best practices.[1]

Mentioned e-mails are sent "FROM" domain(s) that are not managed by CERN e-mail service: for example "toto@gmail.com" or "toto@subdomain.cern.ch". This approach is known as "spoofing" [2] and widely used by spammers. E-mails from spoofed domains can be delivered to "Junk Email" folder because CERN is not authorized to send messages on behalf of other domains.

In H1 2024 we must migrate CERNMX.cern.ch to a new infrastructure aligned with Exchange Online requirements. The new deployment will block the possibility of "spoofing" domains that are not managed by CERN E-Mail Service.

To avoid any problems, *please change the configuration of your application to use a supported FROM address* (e.g. yourservice-noreply@cern.ch, noreply@cern.ch, address of your service account). If this solution is not applicable or you have any other questions please contact service-desk@cern.ch.

Below you can find a list of the devices and number of e-mails, and one example per device:

  * VOCMS059 (5 emails in the past 3 months)
      o Date: 2023-11-26T12:00:01.256Z, From: root@vocms059.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * CRAB-PROD-TW02 (14 emails in the past 3 months)
      o Date: 2023-11-25T02:25:02.934Z, From:
        root@crab-prod-tw02.cern.ch, Recipients:
        cms-service-crab-operators@cern.ch
  * VOCMS068 (11 emails in the past 3 months)
      o Date: 2023-10-22T11:00:01.970Z, From: root@vocms068.cern.ch,
        Recipients: cms-service-crab3htcondor-monitor@cern.ch
  * CRAB-DEV-TW03 (58 emails in the past 3 months)
      o Date: 2023-10-22T11:00:01.974Z, From:
        root@crab-dev-tw03.cern.ch, Recipients:
        cms-service-crab-operators@cern.ch
  * VOCMS0122 (13 emails in the past 3 months)
      o Date: 2023-10-22T22:08:52.145Z, From: root@vocms0122.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * VOCMS0121 (7 emails in the past 3 months)
      o Date: 2023-10-22T22:26:39.038Z, From: root@vocms0121.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * CRAB-DEV-TW04 (11 emails in the past 3 months)
      o Date: 2023-10-08T11:00:04.085Z, From:
        root@crab-dev-tw04.cern.ch, Recipients:
        cms-service-crab-operators@cern.ch
  * VOCMS0197 (14 emails in the past 3 months)
      o Date: 2023-11-11T23:38:46.829Z, From: root@vocms0197.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * VOCMS0199 (9 emails in the past 3 months)
      o Date: 2023-11-22T02:32:21.343Z, From: crab3@vocms0199.cern.ch,
        Recipients: cms-htcondor-admins@cern.ch
  * CRAB-PROD-TW01 (13 emails in the past 3 months)
      o Date: 2023-11-22T11:56:03.055Z, From:
        crab3@crab-prod-tw01.cern.ch, Recipients:
        cms-service-crab-operators@cern.ch
  * VOCMS0198 (5 emails in the past 3 months)
      o Date: 2023-11-23T00:32:42.615Z, From: crab3@vocms0198.cern.ch,
        Recipients: cms-htcondor-admins@cern.ch
  * CRAB-DEV-TW01 (1 emails in the past 3 months)
      o Date: 2023-11-28T12:00:04.083Z, From:
        root@crab-dev-tw01.cern.ch, Recipients:
        cms-service-crab-operators@cern.ch
  * VOCMS0195 (3 emails in the past 3 months)
      o Date: 2023-11-14T11:08:09.443Z, From: crab3@vocms0195.cern.ch,
        Recipients: cms-htcondor-admins@cern.ch
  * VOCMS0119 (2 emails in the past 3 months)
      o Date: 2023-11-02T11:10:23.516Z, From: root@vocms0119.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * VOCMS0155 (1 emails in the past 3 months)
      o Date: 2023-11-02T23:02:08.640Z, From: root@vocms0155.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * CRAB-PREPROD-SCD03 (4 emails in the past 3 months)
      o Date: 2023-10-18T13:36:38.869Z, From:
        crab3@crab-preprod-scd03.cern.ch, Recipients:
        cms-htcondor-admins@cern.ch
  * VOCMS0106 (1 emails in the past 3 months)
      o Date: 2023-09-25T22:00:51.667Z, From: root@vocms0106.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * VOCMS0120 (1 emails in the past 3 months)
      o Date: 2023-10-20T04:10:22.700Z, From: root@vocms0120.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch
  * VOCMS0107 (2 emails in the past 3 months)
      o Date: 2023-12-12T23:02:18.807Z, From: root@vocms0107.cern.ch,
        Recipients: cms-service-crab-operators@cern.ch

Best regards,
The CERN E-Mail Service

[1] Anonymous SMTP <https://mailservices.docs.cern.ch/Miscellaneous/Anonymous_smtp/>

[2] Email spoofing <https://en.wikipedia.org/wiki/Email_spoofing>

## Comment (mapellidario, 2023-12-20T11:59:25Z)

I asked germano https://its.cern.ch/jira/projects/CMSVOC/issues/CMSVOC-520

## Comment (belforte, 2024-02-07T10:29:31Z)

Wait for next VOC. Does not seem urgent

## Comment (belforte, 2024-03-04T10:18:43Z)

We have some hopes that this goes away when moving to Alma9. Let's migrate and see. #8257

## Comment (belforte, 2024-03-04T10:20:53Z)

Stefano will anyhow ask helpdesk
https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3779263

## Comment (belforte, 2024-03-05T16:20:18Z)

So far I see two different issues:
 * mails from condor daemons, the "sender" is controlled via [/etc/condor/config.d/82_cms_schedd_crabschedd_generic.config, line 190](https://gitlab.cern.ch/CMSSI/cmsgwms-htcondor-configurations/-/blob/cern/configs/82_cms_schedd_crabschedd_generic.config?ref_type=heads#L190)  and we should change it
 * mails from cron daemon. CERN expert is investigating see [INC3779263](https://cern.service-now.com/service-portal?id=ticket&table=incident&n=INC3779263)
    * according to export new alma9 machine is fine. We get mail `From: (Cron Daemon) <root_crab-sched-903@cern.ch>` which is good.

## Comment (belforte, 2024-03-13T14:20:01Z)

Mails from condor has been fixed via https://gitlab.cern.ch/CMSSI/cmsgwms-htcondor-configurations/-/commit/25a349695f9e34b01376107f72d89700f032957b

Mail from crontabs will be fixed as we move to alma9

Closing
