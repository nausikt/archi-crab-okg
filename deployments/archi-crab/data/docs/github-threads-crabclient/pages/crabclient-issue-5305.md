# dmwm/CRABClient issue #5305: improve error handling on getoutput

State: open
Opened: 2024-04-26T14:25:18Z
Labels: MediumPrio
URL: https://github.com/dmwm/CRABClient/issues/5305

## Opening post (belforte, 2024-04-26T14:25:18Z)

a spurios "failed to retrieve file" is generated when gfal_copy contains a line with the `error` string 
https://github.com/dmwm/CRABClient/blob/d4b4151f668ba23cb069569e9613c83776630f6b/src/python/CRABClient/Commands/remote_copy.py#L356
even if the message was harmless and transfer worked OK.  E.g. 
```
TLS: Unable to create TLS context; invalid private key.
TLS: 47882433451776:error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch:crypto/x509/x509_cmp.c:303:
```

see https://github.com/dmwm/CRABServer/issues/8357

It is better to rely on gfal-copy exit code first. And only parse stderr in case of failure so somehow translate known messages into more clear error categories.

relevant code is in
https://github.com/dmwm/CRABClient/blob/d4b4151f668ba23cb069569e9613c83776630f6b/src/python/CRABClient/Commands/remote_copy.py#L295-L301
https://github.com/dmwm/CRABClient/blob/d4b4151f668ba23cb069569e9613c83776630f6b/src/python/CRABClient/Commands/remote_copy.py#L333

## Comment (belforte, 2024-04-26T14:26:55Z)

Not very urgent since so far the spurious `TLS error` only appear when running in Jenkins nodes. But it indicates a fragility
