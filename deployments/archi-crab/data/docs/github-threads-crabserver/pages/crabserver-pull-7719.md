# dmwm/CRABServer pull request #7719: RUCIO_Transfers.py: Add checksums to json FJR for non-EDM outputs

State: closed
Opened: 2023-07-06T08:59:50Z
Closed: 2023-07-18T13:30:21Z
Merged: 2023-07-18T13:30:21Z
URL: https://github.com/dmwm/CRABServer/pull/7719

## Opening post (novicecpp, 2023-07-06T08:59:50Z)

Fix https://github.com/dmwm/CRABServer/issues/7718

As @mapellidario suggested, put it in `cmscp.py` where the `addoutput` key is created. The rest already handled by `PostJob.py`.
I discovered last Tuesday that JobWrapper ALWAYS use `Utils.FileTools.calculateChecksums` to calculate checksums of output file in [CMSRunAnalysis.py#L455-L470](https://github.com/novicecpp/CRABServer/blob/db9c3bdcf78c1361fa7a59c2ec6c20a69ec5588f/scripts/CMSRunAnalysis.py#L455-L470) ([recent job](https://cmsweb.cern.ch:8443/scheddmon/0107/afelizia/230706_082652:afelizia_crab_crab_afelizia_2023-07-06_UTC10-25-47/job_out.21.0.txt) in the production).


It is works so far for my test tasks [230704_055629:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20230704_075628](https://monit-grafana.cern.ch/d/cmsTMDetail/cms_task_monitoring?orgId=11&var-user=tseethon&var-task=230704_055629:tseethon_crab_rucio_transfers_hc1kj_withnonedm_test12_20230704_075628&from=1688450189000&to=now).

## Comment (cmsdmwmbot, 2023-07-06T09:05:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1580/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-07-07T15:15:28Z)

perfect
