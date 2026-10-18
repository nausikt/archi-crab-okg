# dmwm/CRABServer issue #8613: remove all instances of xquery

State: closed
Opened: 2024-08-12T19:31:41Z
Closed: 2024-08-12T20:03:22Z
Labels: Priority: High, Area: HTCondor
URL: https://github.com/dmwm/CRABServer/issues/8613

## Opening post (belforte, 2024-08-12T19:31:41Z)

it is deprecated in HTCondor and in last round of "modernization" I missed a few places
1. in `AdjustSites` it is in a very old and obscure comment: remove. THere is also obsolete code there for the case when "CRABServer REST talks to the schedd", which is not happening anymore. REST does not make any HTC call. Remove that as well
2. in `GenerateMONIT` and `RenewRemoteProxies` we were anyhow using `list(schedd.xquery())` which is exactly what `schedd.query()` does !
