# dmwm/CRABServer issue #8768: add proper support for tm_user_webdir = None

State: closed
Opened: 2024-11-06T20:53:21Z
Closed: 2024-11-07T11:51:54Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/8768

## Opening post (belforte, 2024-11-06T20:53:21Z)

current code fails with HTTP 500.
Returning "None" is a gentler way which allows the calling client to deal with it.
Ref: https://github.com/dmwm/CRABServer/issues/6544#issuecomment-2460705998

code is
https://github.com/dmwm/CRABServer/blob/483adb22e60031b98fb5c157b6a0b11e09fc78d7/src/python/CRABInterface/RESTTask.py#L218-L224

And in the example reported in there the DB has this (from the [UI](https://cmsweb-test2.cern.ch/crabserver/ui/task/241106_202543%3Abelforte_crab_20241106_212539) )
![image](https://github.com/user-attachments/assets/4dd4ccfe-62a4-47ae-99bb-d5c22ed1b542)

## Comment (belforte, 2024-11-07T11:51:54Z)

closed via #8767
