# dmwm/CRABServer pull request #8087: jenkins test - add client validation test for crab recover

State: closed
Opened: 2023-12-04T14:35:59Z
Closed: 2024-08-23T11:07:56Z
Merged: 2024-08-23T11:07:56Z
Labels: Status: Done
URL: https://github.com/dmwm/CRABServer/pull/8087

## Opening post (mapellidario, 2023-12-04T14:35:59Z)

related to #6540

### status

tested on my laptop, it works

### description

Adds the following tests to client validation

- `crab status ---task --instance`
- `crab recover --dir`
- `crab recover --task --instance`

## Comment (cmsdmwmbot, 2023-12-04T14:37:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1777/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-12-04T16:47:31Z)

looks good. If you want to test w/o touching master, you can create a `testJenkins` branch (delete the one I made few days ago), merge there and then select it here
![image](https://github.com/dmwm/CRABServer/assets/1837785/a75a7347-0972-49fd-ba10-ade94675b62a)
at the bottom of https://cmssdt.cern.ch/dmwm-jenkins/view/CRAB/job/CRABServer_ExecuteTests/build?delay=0sec

## Comment (belforte, 2024-04-18T12:35:07Z)

@mapellidario any reason why this was not merged ? Is there some open action ?

## Comment (belforte, 2024-06-27T11:20:50Z)

@mapellidario ping
