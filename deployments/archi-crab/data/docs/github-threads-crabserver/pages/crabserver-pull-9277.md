# dmwm/CRABServer pull request #9277: use v2 HTCondor API. so it works with HTC 25.x and later

State: closed
Opened: 2026-02-26T15:58:22Z
Closed: 2026-02-26T15:58:38Z
Merged: 2026-02-26T15:58:37Z
URL: https://github.com/dmwm/CRABServer/pull/9277

## Opening post (belforte, 2026-02-26T15:58:22Z)

We had kept RenewRemoteProxies with HTCondort python API v1 because e at the time I did the v1/v2 changes the `schedd.refreshGSIProxy` method was not available in v2 API.

Now we have moved to using HTCondor  25.x in TW image, and the old API has been remove in there. While the `refreshGSIProxy` is now in there, and it works.
