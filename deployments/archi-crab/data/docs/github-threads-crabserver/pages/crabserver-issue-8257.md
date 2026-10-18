# dmwm/CRABServer issue #8257: port all VM's to alma9

State: closed
Opened: 2024-02-23T09:15:49Z
Closed: 2024-05-16T09:59:26Z
Labels: Type: Enhancement, Priority: High, alma9
URL: https://github.com/dmwm/CRABServer/issues/8257

## Opening post (belforte, 2024-02-23T09:15:49Z)

with SL7 end of life we should move all VM's to alma9

This is hopefully simple for TW and Publisher (we can still use SL7 containers, but should move those as well at some point, if nothing else because things which we install via yum, may not be available anymore at some point).
More work for schedulers.

Let's try to use this a an umbrella issue for more detailed work. Add more as needed

- [x] make scheduler scripts run on alma9 #8256
- [x] move all schedulers to alma9 and htcondor23 #8258
- [x] move TW VM's to alma9 #8261
- [ ] move containers away from sl7 (new PyPi ones will be based on debian so this may be "already done")

## Comment (belforte, 2024-05-16T09:59:26Z)

All Done
