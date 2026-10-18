# dmwm/CRABServer issue #8245: bad Rucio credential names in last PR #8223

State: closed
Opened: 2024-02-18T17:09:28Z
Closed: 2024-02-18T17:23:50Z
URL: https://github.com/dmwm/CRABServer/issues/8245

## Opening post (belforte, 2024-02-18T17:09:28Z)

I overdid correction for name does not follow standard in #8223   These lines are wrong
https://github.com/dmwm/CRABServer/blob/5f5960a01702e80e072486bfc6f5e30b80b484e5/src/python/RucioUtils.py#L29-L30

The attributes name in the TaskWorkerConfig.py file are still
 * `config.Services.Rucio_cert`
 * `config.Services.Rucio_key`
