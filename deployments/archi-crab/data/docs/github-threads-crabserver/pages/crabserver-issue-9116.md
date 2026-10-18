# dmwm/CRABServer issue #9116: enforce users to specify SiteWhitelis for data w/o location from RUcio

State: closed
Opened: 2025-06-27T19:25:45Z
Closed: 2025-07-03T13:25:04Z
URL: https://github.com/dmwm/CRABServer/issues/9116

## Opening post (belforte, 2025-06-27T19:25:45Z)

we must have user specify a site white list when they submit
- [x] with `ignoreLocality = True` 
     * this is done already in Client  since 8 years ! https://github.com/dmwm/CRABClient/issues/4646
- [x] using `config.Data.userInputFiles`
- [x] look if there's any other use case for this

This should be enforced in TW first, so we do it "now" or in client so users get an immediate message. Can surely do in both as well.

## Comment (belforte, 2025-06-27T19:27:02Z)

FYI @sinonkt

## Comment (belforte, 2025-07-01T19:08:52Z)

enforcing added in CRABClient, but not deployed yet.  https://github.com/dmwm/CRABClient/issues/5400

## Comment (belforte, 2025-07-03T13:24:36Z)

I think enforcing in the Client is enough. On server side it will be OK to assume that whitelist is present in such cases and let code raise a fatal exception if not.
