# dmwm/CRABServer issue #7704: remove old rules for crab_tape_recall account

State: closed
Opened: 2023-06-29T22:37:33Z
Closed: 2023-06-30T21:44:54Z
Labels: Status: Done, Priority: TOP, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7704

## Opening post (belforte, 2023-06-29T22:37:33Z)

ref: 
[CMSTRANSF-638](https://its.cern.ch/jira/projects/CMSTRANSF/issues/CMSTRANSF-638) and [MatterMost](https://mattermost.web.cern.ch/cms-o-and-c/pl/mdm9cqttcpfwtx8ymb8crjuwoc)

TODO:
delete all the rules for crab_tape~recall which do not have a sane expiration time.
(i.e. have no expiration or have an expiration more than e months in the future)

## Comment (belforte, 2023-06-30T20:37:20Z)

Done. Here's screen dump
```
[crab3@crab-preprod-tw01 TaskManager]$ source env.sh
Define environment for TASKWORKER in /data/srv/TaskManager
[crab3@crab-preprod-tw01 TaskManager]$ export CRYPTOGRAPHY_ALLOW_OPENSSL_102=1
[crab3@crab-preprod-tw01 TaskManager]$ export X509_USER_CERT=/data/certs/servicecert.pem 
[crab3@crab-preprod-tw01 TaskManager]$ export X509_USER_KEY=/data/certs/servicekey.pem 
[crab3@crab-preprod-tw01 TaskManager]$ export RUCIO_ACCOUNT=crab_tape_recall
[crab3@crab-preprod-tw01 TaskManager]$ rucio whoami
/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/external/py3-cryptography/3.2.1-comp2/lib/python3.8/site-packages/cryptography/hazmat/bindings/openssl/binding.py:175: CryptographyDeprecationWarning: OpenSSL version 1.0.2 is no longer supported by the OpenSSL project, please upgrade. The next version of cryptography will completely remove support for it.
  warnings.warn(
email      : stefano.belforte@cern.ch
account_type : SERVICE
deleted_at : None
updated_at : 2020-10-15T20:57:44
suspended_at : None
account    : crab_tape_recall
status     : ACTIVE
created_at : 2020-10-15T20:57:44
[crab3@crab-preprod-tw01 TaskManager]$ python3
Python 3.8.2 (default, Jan 22 2021, 17:57:37) 
[GCC 6.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import datetime
>>> 
>>> from rucio.client import Client
/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/external/py3-cryptography/3.2.1-comp2/lib/python3.8/site-packages/cryptography/hazmat/bindings/openssl/binding.py:175: CryptographyDeprecationWarning: OpenSSL version 1.0.2 is no longer supported by the OpenSSL project, please upgrade. The next version of cryptography will completely remove support for it.
  warnings.warn(
>>> rucio=Client()
>>> rucioClient=rucio
>>> 
>>> rucio.whoami()
{'email': 'stefano.belforte@cern.ch', 'account_type': 'SERVICE', 'deleted_at': None, 'updated_at': '2020-10-15T20:57:44', 'suspended_at': None, 'account': 'crab_tape_recall', 'status': 'ACTIVE', 'created_at': '2020-10-15T20:57:44'}
>>> account = 'crab_tape_recall'
>>> # get rules for this account
>>> ruleGen=rucio.list_replication_rules({'account':account})
>>> rules = list(ruleGen)
>>> print(f"{len(rules)} rules exist for account {account}")
517 rules exist for account crab_tape_recall
>>> today=datetime.datetime.now()
>>> 
>>> oldRules=[]
>>> for rule in rules:
...     created = rule['created_at']
...     days = (today-created).days
...     #print(created, days)
...     if days > 60:
...         oldRules.append(rule['id'])
... 
>>> print(f"{len(oldRules)} are older than 60 dasy" )
179 are older than 60 dasy
>>> print(oldRules[0])
5653c29369aa431f836d68d5d99eca32
>>> for r in oldRules:
...     rucio.delete_replication_rule(r)
... 
True
True
[....]
True
True
>>> 

```
Now it will take 1h before rules are really deleted from Rucio.

## Comment (belforte, 2023-06-30T21:40:01Z)

Cleanup completed:
```
>>> ruleGen=rucio.list_replication_rules({'account':account})
>>> rules = list(ruleGen)
>>> print(f"{len(rules)} rules exist for account {account}")
338 rules exist for account crab_tape_recall
>>> today=datetime.datetime.now()
>>> 
>>> oldRules=[]
>>> for rule in rules:
...     created = rule['created_at']
...     days = (today-created).days
...     #print(created, days)
...     if days > 60:
...         oldRules.append(rule['id'])
... 
>>> print(f"{len(oldRules)} are older than 60 dasy" )
0 are older than 60 dasy
>>> 

```
