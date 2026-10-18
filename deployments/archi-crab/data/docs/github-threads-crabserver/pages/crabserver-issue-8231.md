# dmwm/CRABServer issue #8231: new format/location for MONIT secret file on schedulers

State: closed
Opened: 2024-02-06T21:57:24Z
Closed: 2024-02-15T14:10:59Z
Labels: Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8231

## Opening post (belforte, 2024-02-06T21:57:24Z)

with ref. to https://github.com/dmwm/CRABServer/pull/8214#issue-2112910251
we (Stefano, Dario, Wa) discussed and agreed to change to

filename :  `/data/certs/monit.d/MONIT-CRAB.json`

content:
```python
{
 "url": "https://monit-metrics.cern.ch:10014/crab",
  "username": "crab", 
  "password": "PutRealPasswordHere"
}
```

we will use puppet in case we want to push to user `crab-test` instead of `crab`

@mapellidario please correct me if my memory failed me !

## Comment (belforte, 2024-02-12T21:14:30Z)

@mapellidario is it on you or on me to deploy the secret file ?

## Comment (mapellidario, 2024-02-13T16:09:50Z)

I deployed the secrets to all machines. dev, qa and master puppet branches.

- filename:  `/data/certs/monit.d/MONIT-CRAB.json` (as asked in this private message https://mattermost.web.cern.ch/cms-o-and-c/pl/mtdnsqsmeibbpcg6p4en64dxee)
- content: schema described in puppet, for example here for [tw](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/57c90b999134d10a76a7481923ecb798a245467b/code/manifests/crabtaskworker/certificate.pp#L117)
- I created a new page on our docs with a mapping between producers, credential files in tbag, opensearch instance and index:  https://cmscrab.docs.cern.ch/technical/crab-monitoring/crab-opensearch.html

check to which machines the file has been deployed with

```bash
wassh -c vocmsglidein -l root "ls /data/certs/monit.d/"
```

## Comment (belforte, 2024-02-13T17:39:52Z)

I am fine with changing the `url` format. Still find that `monit-metrics-secrets.json` is a better name than `MONIT-CRAB.json`... but I guess changing that is too much work for you.

## Comment (mapellidario, 2024-02-14T08:21:32Z)

Not a problem changing the file name, I will do it :)

## Comment (belforte, 2024-02-14T10:36:36Z)

Please no changes anymore. I do not want to edit the file again.
