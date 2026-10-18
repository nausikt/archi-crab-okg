# dmwm/CRABServer issue #8673: use Stefano's OS token as S3 secrets in REST

State: closed
Opened: 2024-08-29T16:32:24Z
Closed: 2024-09-03T17:13:01Z
Labels: Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8673

## Opening post (belforte, 2024-08-29T16:32:24Z)

currently we are using Dario's.
Should move to Stefano's.
I.e. change 
```
s3 = {'access_key':'ab00fcc889f248c495d2875f15a3badb',
      'secret_key':'**********************************************'}
```
in all `CRABServerAuth.sops.py` files in `crab-secrets`

```text

LapSB:kubernetes$ pwd
/home/belforte/CRAB/crab-secrets/kubernetes
LapSB:kubernetes$ tree
.
|-- OraclePasswords.sops
|-- preprod
|   `-- crabserver
|       |-- CRABServerAuth.sops.py
|       `-- config.py
|-- prod
|   `-- crabserver
|       |-- CRABServerAuth.sops.py
|       `-- config.py
|-- sample
|   `-- crabserver
|       |-- CRABServerAuth.py
|       `-- config.py
|-- test11
|   `-- crabserver
|       |-- CRABServerAuth.sops.py
|       `-- config.py
|-- test12
|   `-- crabserver
|       |-- CRABServerAuth.sops.py
|       `-- config.py
`-- test2
    `-- crabserver
        |-- CRABServerAuth.sops.py
        `-- config.py

12 directories, 13 files
LapSB:kubernetes$ 

```

## Comment (belforte, 2024-09-03T15:28:06Z)

S3 keys changed in crab-secret files via https://gitlab.cern.ch/crab3/crab-secrets/-/commit/6fbc29cd15e5b0173b471d35737d97019db360f1

## Comment (belforte, 2024-09-03T15:40:52Z)

deployed and tested on cmsweb-test2

## Comment (belforte, 2024-09-03T17:13:01Z)

deployed also on
* cmsweb-test11
* cmsweb-testbed (preprod)
* cmsweb (prod)

Wa will take care himself of cmsweb-test12
