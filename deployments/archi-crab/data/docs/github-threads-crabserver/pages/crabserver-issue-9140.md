# dmwm/CRABServer issue #9140: enable jobs to use BEARER_TOKEN if present

State: closed
Opened: 2025-08-01T13:08:39Z
Closed: 2025-08-22T18:11:32Z
Labels: Type: Enhancement, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/9140

## Opening post (belforte, 2025-08-01T13:08:39Z)

GOAL: Make it possible to use tokens for data read and local stageout, but do not fail if they are not present.

- [x] in e.g. dagman_bootstrap_startup.sh check that `condor_store_cred query-oauth` returns exit code 0 (meaning that `crabtw` has access to a token on that AP)
- [x] if token is OK. Set a flag: `touch TOKEN_OK` or similar
- [x] in PreJob, if `TOKEN_OK` file is present, add to JDL 
    ` use_oauth_services = cms_crab`
- [x] in `gWMS-CMSRunAnalysis.sh`
     if `/srv/.condor_creds/cms_crab.use` is present, do `export BEARER_TOKEN_FILE=/srv/.condor_creds/cms_crab.use`


This will not tell if it is using token or proxy to read data, the only way would be to `unset X509_USER_PROXY` and check that it still works.
Better to do that in test submissions.

## Comment (stlammel, 2025-08-01T14:11:13Z)

Hallo Stefano,
   you only have a token in the job, not in the schedd. (Only condor/root has access
to the token on the submit node.) So, i think the dagman_bootstrap_startup.sh first
three steps will not apply.
   Where to set BEARER_TOKEN_FILE we should discuss and agree. I am not in favour
of each team doing that on their own (and hardcoding filenames, etc.).
   Thanks,
         cheers,  Stephan

## Comment (belforte, 2025-08-01T14:18:49Z)

I beg to disagree. The submitter on the AP (`crabtw`) user has access to its token too:

```console
bash-5.1$ hostname
crab-sched-901.cern.ch
bash-5.1$ whoami
crabtw
bash-5.1$ httokendecode 
{
  "wlcg.ver": "1.0",
  "sub": "58ba8516-2e94-4888-bce5-0187f7b4ebb9",
  "aud": "https://wlcg.cern.ch/jwt/v1/any",
  "nbf": 1753687733,
  "scope": "condor:/WRITE openid storage.create:/store/temp/user offline_access profile storage.read:/ storage.modify:/store/temp/user email wlcg",
  "iss": "https://cms-auth.cern.ch/",
  "exp": 1754119733,
  "iat": 1753687733,
  "jti": "2e568d85-9c62-4750-bc90-c1da823ef75e",
  "client_id": "48620efa-e001-4c1d-84fc-4640d9498a11"
}
bash-5.1$ 
```

Anyhow, this is more for my testing that actual production. I will be happy to change once we settle on a common location/naming etc. I need a GH branch in order to run a test instance.

## Comment (stlammel, 2025-08-01T14:22:21Z)

The token on the schedd should be in /var/lib/condor/oauth_credentials which should
NOT be user readable. Where is the token located? and how did you tell httokendecode
where it is?
 - Stephan

## Comment (belforte, 2025-08-01T14:27:51Z)

from httokendecode help:
```
If file name not given, follows WLCG Bearer Token Discovery
  which is to first try $BEARER_TOKEN, next $BEARER_TOKEN_FILE,
  and next ${XDG_RUNTIME_DIR:-/tmp}/bt_u`id -u`.
```
so it uses `/tmp/bt_u501` which AFAICT is constantly refreshed
Indeed  `/tmp/bt_u501` is the same file as `/var/lib/condor/oauth_credentials/crabtw/cms_crab.use` (from `diff`)

## Comment (belforte, 2025-08-01T14:29:01Z)

I simply wanted a way to tell if I am submitting from a schedd which is properly setup, if I add ` use_oauth_services = cms_crab` to the JDL and there's no token, submission fails.

## Comment (belforte, 2025-08-01T14:29:54Z)

need to get my hands dirty with this stuff and see where I go :-)

## Comment (stlammel, 2025-08-01T14:35:31Z)

Ahh, interesting. HTCondor copies it into /tmp. This might just be during the duration
of jobs plus cleanup. We should check with the HTCondor developers if we can rely on
this. I did not recall seeing this in the documentation.

If you want to know if OAuth credentials are available, i would use the
condor_store_cred command with query-oauth. A bit more complex but more
direct/robust.
 - Stephan

## Comment (belforte, 2025-08-01T16:47:54Z)

thanks for the tip @stlammel . It all works now, unsetting X509_USER_PROXY in the beginning of the gird job wrapper. But I believe that I do not have a way to tell in the WN if read via token will work or not, so am keeping this for testing (and I'll stay away from CERN, at least), waiting for the "global decision" which you mentioned.

## Comment (stlammel, 2025-08-01T18:01:29Z)

Great Stefano!
The idea is to add the token for a while and see how this goes. If token access is not
supported by the storage service the xrootd client should fall back to x509.
Maybe we can setup an extra, small HammerCloud once the python3 port of HC
become available. Or we could ask Noy and/or Vijay to exercice/verify things with
all sites?
 - Stephan

## Comment (belforte, 2025-08-02T13:42:14Z)

Unless there is some feedback from cmsRun whether it is using token or proxy, simply adding the token will not show anything.

## Comment (stlammel, 2025-08-02T22:05:47Z)

If i recall the information is available by increasing
the logging level for XrdAdapter. It should be in the
notes for the enhancements Pau made a few years
ago. I'll look it up on Monday.
Thanks,
 - Stephan
________________________________
From: Stefano Belforte ***@***.***>
Sent: Saturday, August 2, 2025 08:42
To: dmwm/CRABServer ***@***.***>
Cc: Stephan Lammel ***@***.***>; Mention ***@***.***>
Subject: Re: [dmwm/CRABServer] enable jobs to use BEARER_TOKEN if present (Issue #9140)

[https://avatars.githubusercontent.com/u/1837785?s=20&v=4]belforte left a comment (dmwm/CRABServer#9140)<https://github.com/dmwm/CRABServer/issues/9140#issuecomment-3146508485>

Unless there is some feedback from cmsRun whether it is using token or proxy, simply adding the token will not show anything.

—
Reply to this email directly, view it on GitHub<https://github.com/dmwm/CRABServer/issues/9140#issuecomment-3146508485>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/ABJETF5KBXOQPNXX33LMP7L3LS54ZAVCNFSM6AAAAACC4XIESWVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTCNBWGUYDQNBYGU>.
You are receiving this because you were mentioned.Message ID: ***@***.***>

## Comment (belforte, 2025-08-05T20:37:31Z)

@stlammel ping : lookup Pau notes for a way to tell if  XrdAdapter uses X509 or token

## Comment (stlammel, 2025-08-05T20:57:06Z)

cc-ed you on the pong

## Comment (belforte, 2025-08-06T12:22:41Z)

if Pau does not answer, maybe Matti knows ?

## Comment (belforte, 2025-08-20T13:15:58Z)

ready for deployment
I tested that works on vocms059 (no cred daemon) and on crab-sched-901 (token enabled).

see also https://its.cern.ch/jira/browse/CMSSI-124?focusedId=7072279&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-7072279 and https://its.cern.ch/jira/browse/CMSSI-124?focusedId=7072298&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-7072298
