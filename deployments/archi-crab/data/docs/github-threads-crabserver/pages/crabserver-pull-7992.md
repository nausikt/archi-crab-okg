# dmwm/CRABServer pull request #7992: Add playbook to download task_process from schedd

State: closed
Opened: 2023-11-02T15:27:27Z
Closed: 2023-11-03T11:51:57Z
Merged: 2023-11-03T11:51:57Z
URL: https://github.com/dmwm/CRABServer/pull/7992

## Opening post (novicecpp, 2023-11-02T15:27:27Z)

May I ask permission to save my small ansible playbook here for testing Rucio ASO locally? @belforte @mapellidario

## Comment (cmsdmwmbot, 2023-11-02T15:30:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1734/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-02T15:31:32Z)

Sure. Though it would be better to have a more descriptive directory name !

## Comment (mapellidario, 2023-11-02T15:35:26Z)

If i understand correctly, the ansible playbook is used to make sure that you download the proper files from the schedd, then it is up to the developer to make sure to have a working python environment to run the script, right?

I agree with Stefano, we may find a better directory, keeping in mind that we already have `test/python/ASO/Rucio`, for example. Maybe we can create `test/python/ASO/env` ?

## Comment (belforte, 2023-11-02T15:39:08Z)

`test/Playbook/ASORucio` ? Or does it need to be called `something env` ? So we may add more Ansible things later, whatever that exactly is.

## Comment (novicecpp, 2023-11-02T15:50:51Z)

Actually, I just want to add a new line in.gitignore, which is gone every time I switch branches from one to another (and remove from PR). 
`test/Playbook/ASORucio` is good for me. I try to avoid `test/python/` where it is preserved for unittest's files.

Answer Dario: Yes. Local environment setup is still mess (especially the python version), so I am not put it in README for now.

## Comment (cmsdmwmbot, 2023-11-02T15:58:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1735/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-11-03T10:39:23Z)

@novicecpp you can merge whenever you like

## Comment (novicecpp, 2023-11-03T11:51:36Z)

Thanks!
