# dmwm/CRABClient issue #5351: Potential problems getting country groups in ProxyInteractions.py

State: closed
Opened: 2024-11-22T13:59:04Z
Closed: 2024-11-26T17:17:54Z
Labels: question
URL: https://github.com/dmwm/CRABClient/issues/5351

## Opening post (ArturAkh, 2024-11-22T13:59:04Z)

There might be an issue in [ProxyInteractions.py](https://github.com/dmwm/CRABClient/blob/d29ea99735597dd4d176b75fe26cb4a28250dc3a/src/python/CRABClient/ProxyInteractions.py#L87-L103)

when trying to get the group in cases like:

```bash
$ voms-proxy-info --fqan --file /tmp/x509up_u12126
/cms/country/de/Role=NULL/Capability=NULL
/cms/Role=NULL/Capability=NULL
/cms/compute/Role=NULL/Capability=NULL
/cms/compute/scope/Role=NULL/Capability=NULL
/cms/country/Role=NULL/Capability=NULL
/cms/dcms/Role=NULL/Capability=NULL
```

The handling of groups and roles would need a more general treatment (e.g. considering everything between `/cms` and the first `/Role=` as a group)

## Comment (ArturAkh, 2024-11-22T14:00:32Z)

In case of `/cms/country/de/Role=NULL/Capability=NULL`

`country` would be extracted as group, and this contradicts how the group would be assigned in the `create` method using `voms-proxy-init`, which would need `/country/de` as group.

In addition, `role` would be set to `de` instead of `NULL`, and such a role does not exist

## Comment (belforte, 2024-11-22T14:17:20Z)

Hi @ArturAkh 
until now the "logic" for VOMS  FQAN has been "/voname/groupname/"
I do not know if now we have a new use case (subgroups ?) or if the FQAN has been improperly defined.

The original documentation says that FQAN format is `/group/Role=` with Role being optional.
Slash-separated group names were not there.
See https://edms.cern.ch/file/858263/1/EGEE-II-JRA1-TEC-858263-FQAN-Matching-Rules-v1.6_doc_cpdf.pdf pag 5

Which exact problem do you have because of this ?  I have similar attributes in my proxy and everything worls.

Is there any hope that we can instead stop worrying about VOMS groups and roles in CRAB submission ? All groups are listed in the user proxy anyhow.  And I'd be very happy to simplify the code.

Should we involve "those who introduced those /../../.. attributes" ?

## Comment (ArturAkh, 2024-11-22T17:29:08Z)

Hi Stefano,

We have a use-case where regional groups like `cms:/cms/dcms` are not assigned to VOMS certificates anymore, since this procedure was managed manually. This is currently not done anymore.

At KIT - and I'd assume also at other German CMS institutions - we have used that for the access to storage. A way out of that would be for us the automatic assignment of the country group `cms:/cms/country/de`, which can be also added to the user proxy certificates as main fqdn.

This assignment is e.g. visible in the new IAM CMS service: https://cms-auth.web.cern.ch/dashboard#!/home

This use-case is not covered currently by group & role checks in crab, such that e.g. submission fails - at least when I have tested that last time with an attempt of having `cms:/cms/country/de` group as main fqan. In consequence, every new user at our institute would have problems to use crab and our storage at the same time, since they won't get `cms:/cms/dcms` anymore.

## Comment (belforte, 2024-11-22T17:34:50Z)

but the proxy which is presented to your servers should still list all those VOMS attributes. Simply CRAB will not be able to force one of them to be first of the list. 
By the way even this fails for me
```
 voms-proxy-init -voms cms:country/it
```
but
```

belforte@lxplus826/TC3> voms-proxy-info -all
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=belforte/CN=373708/CN=Stefano Belforte/CN=1398784670
issuer    : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=belforte/CN=373708/CN=Stefano Belforte
identity  : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=belforte/CN=373708/CN=Stefano Belforte
type      : RFC3820 compliant impersonation proxy
strength  : 2048
path      : /tmp/x509up_u8516
timeleft  : 186:19:38
key usage : Digital Signature, Key Encipherment
=== VO cms extension information ===
VO        : cms
subject   : /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=belforte/CN=373708/CN=Stefano Belforte
issuer    : /DC=ch/DC=cern/OU=computers/CN=cms-auth.web.cern.ch
attribute : /cms/Role=NULL/Capability=NULL
attribute : /cms/ALARM/Role=NULL/Capability=NULL
attribute : /cms/TEAM/Role=NULL/Capability=NULL
attribute : /cms/compute/Role=NULL/Capability=NULL
attribute : /cms/compute/scope/Role=NULL/Capability=NULL
attribute : /cms/country/Role=NULL/Capability=NULL
attribute : /cms/country/it/Role=NULL/Capability=NULL
attribute : /cms/integration/Role=NULL/Capability=NULL
attribute : /cms/itcms/Role=NULL/Capability=NULL
attribute : Monuserid = stefano (cms)
attribute : username = belfos (cms)
timeleft  : 186:19:38
uri       : voms-cms-auth.app.cern.ch:15000

belforte@lxplus826/TC3> 
```

## Comment (belforte, 2024-11-22T17:37:53Z)

my bad, wrong syntax, this works
```
voms-proxy-init -voms cms:/cms/country/it  
```

## Comment (belforte, 2024-11-22T17:41:01Z)

can your storage look at the list of attributes and check if country/de is there ?

## Comment (ArturAkh, 2024-11-23T07:53:53Z)

Hi Stefano,


Our storage takes /cms/country/de for writing into account, in the same way as /cms/dcms


I'll have a look at the exact error I've encountered and come back to you on Monday.

As far as I remember it was during submission of a crab task.

## Comment (ArturAkh, 2024-11-25T09:39:29Z)

Here is what I see when trying to submit a task with `country/de` group in the main fqan `/cms/country/de/Role=NULL/Capability=NULL`.

Crab configuration setup within CMSSW_13_0_21:

```python
from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.instance = 'prod'
config.General.requestName = 'data_2018UL_tau_Tau_Run2018A'
config.General.workArea = '/afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/crab'
config.section_('JobType')
config.JobType.maxMemoryMB = 4000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/cmsdriver/2018UL/nano_config.py'
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 900
config.section_('Data')
config.Data.unitsPerJob = 1000000
config.Data.splitting = 'EventAwareLumiBased'
config.Data.outputDatasetTag = 'data_2018UL_tau_Tau_Run2018A_1732527119'
config.Data.publication = True
config.Data.inputDataset = '/Tau/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD'
config.section_('Site')
config.Site.storageSite = 'T1_DE_KIT_Disk'
config.Site.whitelist = None
config.Site.blacklist = None
config.section_('User')
config.User.voGroup = 'country/de'
config.section_('Debug')
```

PSet configuration was created via:

```bash
cmsDriver.py nano --data --filein file:inputfile.root --fileout nano.root --step NANO --eventcontent NANOAOD --datatier NANOAOD --python_filename /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/cmsdriver/2018UL/nano_config.py --conditions auto:run2_data --era Run2_2018,run2_nanoAOD_106Xv2 --no_exec --nThreads 8 --nStreams 0
```

Result when running `crab submit` for the crab configuration:

```bash
[aakhmets@lxplus9119 CMSSWWithCrab]$ crab submit /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/crabconfigs/data_2018UL_tau_Tau_Run2018A.py
Will use CRAB configuration file /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/crabconfigs/data_2018UL_tau_Tau_Run2018A.py
Importing CMSSW configuration /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/cmsdriver/2018UL/nano_config.py
**************************************************************
b tagging needs to be run on uncorrected jets. Hence, the JECs
will first be undone for 'updatedPatJetsWithDeepInfo' and then applied to
'updatedPatJetsTransientCorrectedWithDeepInfo'.
**************************************************************
Finished importing CMSSW configuration /afs/cern.ch/work/a/aakhmets/private/htt_data_crab_nanoaod_submission_25-11-2024_prodreleasev12/cmsdriver/2018UL/nano_config.py
You are requesting more than 1 core per job. Please make sure that your multi-threaded code is thread-safe and CPU-efficient, and request the correct amount of memory since the default 'maxMemoryMB' value is meant for single core jobs.
Sending the request to the server at cmsweb.cern.ch
Fatal error trying to connect to https://cmsweb.cern.ch:8443/crabserver/prod/workflow using dryrun=0&workflow=crab_data_2018UL_tau_Tau_Run2018A&saveoutput=1&savelogsflag=0&inputdata=%2FTau%2FRun2018A-UL2018_MiniAODv2_GT36-v1%2FMINIAOD&nonvaliddata=0&dbsurl=https%3A%2F%2Fcmsweb.cern.ch%2Fdbs%2Fprod%2Fglobal%2FDBSReader&useparent=0&ignorelocality=0&splitalgo=EventAwareLumiBased&algoargs=1000000&totalunits=0&publication=1&publishdbsurl=https%3A%2F%2Fcmsweb.cern.ch%2Fdbs%2Fprod%2Fphys03%2FDBSWriter&publishname2=data_2018UL_tau_Tau_Run2018A_1732527119&jobtype=Analysis&generator=pythia&maxjobruntime=900&numcores=8&maxmemory=4000&priority=10&nonprodsw=0&asyncdest=T1_DE_KIT_Disk&requireaccelerator=0&vogroup=country%2Fde&oneEventMode=0&ignoreglobalblacklist=0&partialdataset=0&jobarch=el9_amd64_gcc11&jobsw=CMSSW_13_0_21&cacheurl=https%3A%2F%2Fcmsweb.cern.ch%2FS3%2Fcrabcache_prod&cachefilename=e698dbf940fa49516dde6b62f8780ee6acddcffec0027be3dfd526c59c071433.tar.gz&debugfilename=37294ab56cc27ea9357f202ddcafa1bb0702106fe54441db010418b91fe7b495.tar.gz&edmoutfiles=nano.root.
exit code from curl = 0
HTTP code/reason = 400/Bad Request .  stdout:
<!DOCTYPE html PUBLIC
"-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta>
    <title>400 Bad Request</title>
    <style type="text/css">
    #powered_by {
        margin-top: 20px;
        border-top: 2px solid black;
        font-style: italic;
    }

    #traceback {
        color: red;
    }
    </style>
</head>
    <body>
        <h2>400 Bad Request</h2>
        <p>Invalid input parameter</p>
        <pre id="traceback"></pre>
    <div id="powered_by">
      <span>
        Powered by <a href="http://www.cherrypy.dev">CherryPy 18.8.0</a>
      </span>
    </div>
    </body>
</html>

The server answered with an error.
Server answered with: Invalid input parameter
Reason is: Incorrect 'User.voGroup' parameter <class 'str'> country/de
Error Id: d682464c910061d84731ee25b2ec8f9b
```
So it might well be, that this is rather related to a server-side error

## Comment (belforte, 2024-11-25T09:44:56Z)

I am have no problem in believing that `config.User.voGroup = 'country/de'` is not working. It was coded in a world where this use case was not existing.
But my point is that even w/o anything here, the proxy which is eventually presented to the storage server will list all the VOMS attributes, including `/cms/country/de/Role=NULL/Capability=NULL` . Could the storage check for simply this to be present, instead of "this is in the first attribute in the list" ?

## Comment (ArturAkh, 2024-11-25T09:54:09Z)

I'm afraid this is not covered in the dCache implementation currently.

Only `/cms` in first fqan:

```bash
akhmet@bms1:/work/akhmet $ voms-proxy-info -fqan
/cms/Role=NULL/Capability=NULL
/cms/compute/Role=NULL/Capability=NULL
/cms/compute/scope/Role=NULL/Capability=NULL
/cms/country/Role=NULL/Capability=NULL
/cms/country/de/Role=NULL/Capability=NULL
/cms/dcms/Role=NULL/Capability=NULL
akhmet@bms1:/work/akhmet $ gfal-copy 475B44E0-2258-764C-B825-DB88FF682ACC.root  davs://cmsdcache-kit-disk.gridka.de:2880/pnfs/gridka.de/cms/disk-only/store/user/aakhmets/test.root
Copying file:///work/akhmet/475B44E0-2258-764C-B825-DB88FF682ACC.root   [FAILED]  after 0s
gfal-copy error: 17 (File exists) - TRANSFER ERROR: Copy failed (streamed). Last attempt: HTTP 403 : Permission refused  (destination)
```

`/cms/country/de` in the first fqan:

```bash
akhmet@bms1:/work/akhmet $ voms-proxy-info -fqan
/cms/country/de/Role=NULL/Capability=NULL
/cms/Role=NULL/Capability=NULL
/cms/compute/Role=NULL/Capability=NULL
/cms/compute/scope/Role=NULL/Capability=NULL
/cms/country/Role=NULL/Capability=NULL
/cms/dcms/Role=NULL/Capability=NULL
akhmet@bms1:/work/akhmet $ gfal-copy 475B44E0-2258-764C-B825-DB88FF682ACC.root  davs://cmsdcache-kit-disk.gridka.de:2880/pnfs/gridka.de/cms/disk-only/store/user/aakhmets/test.root
Copying file:///work/akhmet/475B44E0-2258-764C-B825-DB88FF682ACC.root   [DONE]  after 0s  
```

And arguing with dCache developers may not lead to solutions on a short time-scale...

## Comment (belforte, 2024-11-25T10:16:30Z)

I see. I can look into expanding the VOMS group handling to support this, it will likely require changes both in client and server. It is not a very short time scale either.
Maybe it is easier to find a way to keep using `dcms` group in IAM ?
It looks like this is the only use case for a national group, so hopefully @stlammel adn @Panos512 can make an exception ?
Until we use replace X509 with tokens ...

Artur, can you please clarify where exactly this "writing to your dCache" happens ?  Is this during final output file storage via ASO ? We do not execute `gfal-copy` for that, but delegate the proxy to FTS who will do the xfer. Can you check that FTS supports the extended group syntax `country/de` ?

## Comment (ArturAkh, 2024-11-25T10:26:40Z)

One possible solution to avoid changes in crab/dCache/FTS would be that new users with `/cms/country/de` would automatically be also assigned to `/cms/dcms` in IAM.

I hope something like that can be deployed on that level, maybe @stlammel could comment

## Comment (stlammel, 2024-11-25T14:17:21Z)

I think this is an artifact on how IAM maps groups to VOMS-groups. Panos and i will take a look. Give us a few days.
Thanks,
 - Stephan

## Comment (ArturAkh, 2024-11-25T14:43:31Z)

OK, sounds good, thanks a lot, Stephan!

## Comment (stlammel, 2024-11-26T16:55:18Z)

Panos and i took a look and we'll resolve this on IAM side. (The IAM group names were not suppose to be exposed but mapped to the existing country groups, except for "dcms" which we will likely replace with "decms". There is no option to flag groups as IAM internal, so we'll need to discuss this with the developers and get a new feature added.)
I suggest to continue use of the "dcms" group right now. Just let me or Panos know in case a user needs to be added/removed while we work on the proper solution.
Thanks,
 - Stephan

## Comment (ArturAkh, 2024-11-26T17:02:59Z)

OK, thanks, Stephan!

I'll write you a message, once our new user is able to login in IAM itself and request dcms role.

Currently, it seems like there are problems considering the user as not active, although he has CMS status already. We will wait a while and will contact you and Panos, if there are problems connecting to IAM.

## Comment (stlammel, 2024-11-26T17:08:12Z)

Hallo Artur,
   i thought we had the problem with users being deactivated/not re-activated resolved. If things don't clear automatically within half a day, please let us know.
   Thanks,
            cheers,  Stephan

## Comment (belforte, 2024-11-26T17:17:52Z)

Thanks Stephan. I am closing this.
