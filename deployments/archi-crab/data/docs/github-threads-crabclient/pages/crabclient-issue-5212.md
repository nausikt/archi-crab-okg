# dmwm/CRABClient issue #5212: crabclient does not check proxy expiration when using --proxy 

State: open
Opened: 2023-09-26T13:25:14Z
Labels: Low Priority
URL: https://github.com/dmwm/CRABClient/issues/5212

## Opening post (mapellidario, 2023-09-26T13:25:14Z)

When running crab client with an expired proxy passed via `--proxy` option, crab client fails with the cryptic message

```plaintext
Singularity> crab status -d crab_recover_20230925_162750 --proxy=$X509_USER_PROXY
Fatal error trying to connect to https://cmsweb-test11.cern.ch:8443/crabserver/devtwo/info?subresource=version using subresource=version.
The server answered with an error.
Log file is /path/to/crab.log
```

maybe we can do better and check if the proxy is valid beforehand. 

I will assign low priority because I know that this is usually not a problem, since the user is supposed to be responsible of his own proxy if he uses the `--proxy` option.

fyi: @novicecpp

## Comment (belforte, 2023-09-27T21:17:22Z)

ideally `--proxy` option is also meant to cover situation where not even voms-proxy-into is available. We could rather look into improving the message, in particular if `--proxy` was used.
