# dmwm/CRABServer issue #8464: automatic splitting does not work anymore

State: closed
Opened: 2024-06-03T18:53:52Z
Closed: 2024-06-03T21:34:03Z
Labels: Type: Bug, Status: In Progress, Area: HTCondor, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8464

## Opening post (belforte, 2024-06-03T18:53:52Z)

after last changes for modern HTCondor the main dag in automatic splitting writes in
`task_process/RestInfoForFileTransfers.json`

{'host': 'cmsweb-testbed.cern.ch:8443', 'dbInstance': 'preprod', 'proxyfile': '/data/srv/glidecondor/condor_local/spool/5130/0/cluster9615130.proc0.subproc0/e080907cad69528d423bbe562e2f8f9873b2c933'}

i.e. the full path for the proxy file,
this conflicts with code in FTS_Transfers
https://github.com/dmwm/CRABServer/blob/7ac2b90193632df3757bcf3bf7750ff27bf736a3/scripts/task_process/FTS_Transfers.py#L75

and the directory path is added twice making FTS calls fail.

## Comment (belforte, 2024-06-03T19:05:12Z)

The effect of this is that ASO stays in "transferring" forever, which I did not notice initially sine ASO was stuck for everybody due to #8460

## Comment (belforte, 2024-06-03T19:47:11Z)

testing fix in https://cmsweb-testbed.cern.ch/crabserver/ui/task/240603_193544%3Abelforte_crab_20240603_213540

## Comment (belforte, 2024-06-03T21:32:03Z)

test worked.
Will merge and deploy to preprod for more validation
