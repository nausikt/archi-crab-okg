# dmwm/CRABServer pull request #8555: [CI] Add Vijay dev env

State: closed
Opened: 2024-07-23T12:20:03Z
Closed: 2024-07-24T10:52:31Z
Merged: 2024-07-24T10:52:31Z
URL: https://github.com/dmwm/CRABServer/pull/8555

## Opening post (novicecpp, 2024-07-23T12:20:03Z)

Hi @belforte @mapellidario ,

I modified `test1` in ServerUtility.py to point to Vijay dev env (cmsweb-test1/devfour/tw05).
This is now possible without rebuilding crabclient because https://github.com/dmwm/CRABServer/pull/8554.

What do you think?

cc: @aspiringmind-code

## Comment (cmsdmwmbot, 2024-07-23T12:25:22Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 1 warnings
   * 25 comments to review
 * Pycodestyle check: succeeded
   * 10 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2056/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-23T13:44:36Z)

Does Aroosha agree that we use cmsweb-test1 sort of permanently ?

## Comment (novicecpp, 2024-07-23T14:08:46Z)

No. 
And it is only temporary, until Dario left, so Vijay can use devtwo/test11/tw02.

We are aware that if something happen, DMWM can blame us 100% and no support from CMSWEB for that cluster.
I am waiting for [a new cluster](https://its.cern.ch/jira/projects/CMSKUBERNETES/issues/CMSKUBERNETES-269) but Aroosha does not have time to create for us yet.

## Comment (novicecpp, 2024-07-24T09:42:30Z)

Thanks Stefano. Let me confirm if we can use test1 without issue before merge.

## Comment (belforte, 2024-07-24T10:01:28Z)

FWIW... if this is just for little over than a month, maybe Vijay can stick to using `instace="other"` ? Anyhow, whatever is easier for you guys

## Comment (novicecpp, 2024-07-24T10:20:59Z)

I try to avoid edit all ST to support "other" instance.
And this way, we have separate instance for Vijay to run his own pipeline.

## Comment (novicecpp, 2024-07-24T10:51:57Z)

Look like it works.
```
Pushing information centrally {'workflow': '240724_105003:tseethon_crab_hc_1kj_test1_20240724_125001', 'status': 'SUBMITTED', 'subresource': 'success', 'clusterid': 9675387}
Summary of schedd failures/successes for slave process 0 (PID 188):
        crab3@vocms059.cern.ch:
                Number of successes: 1
                Number of failures:  0
Last successful submission: ClusterId 9675387 submitted to schedd crab3@vocms059.cern.ch
```
 Merging...
