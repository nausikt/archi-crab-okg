# dmwm/CRABServer pull request #8575: pypi - add filebeat to TW image

State: closed
Opened: 2024-07-30T16:27:22Z
Closed: 2024-07-31T12:51:12Z
URL: https://github.com/dmwm/CRABServer/pull/8575

## Opening post (mapellidario, 2024-07-30T16:27:22Z)

fix #8573 

### status

tested on crab-dev-tw02, working [1]

### description

- [x] install filebeat from elasticsearch own repos, similar to what cmsweb is doing [2]. following official instructions [3] and chosing the repo that provides software under apache 2.0 license (i do not even want to look at what the elastic license sould mean for us)
- [x] copied `monitor.sh` from ./Docker into ./cicd/crabtaskworker_pypi without any modification
- [x] run `/data/monitor.sh` from `/data/run.sh`, after `./start.sh -c`, before the while-true loop

I am open to suggestions! :)

---

[1] https://monit-grafana.cern.ch/goto/7rYneG9Sg?orgId=11 selecting `crab-dev-tw02` from the TW host dropdown menu
[2] https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/cmsweb/Dockerfile#L17 
[3] https://www.elastic.co/guide/en/beats/filebeat/current/setup-repositories.html

## Comment (cmsdmwmbot, 2024-07-30T16:32:32Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2076/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-07-30T18:58:21Z)

ouch, this was more work than I'd expected. Where we picking filebeat from until now ? Some rpm built by Alan ?

## Comment (mapellidario, 2024-07-31T10:18:42Z)

Yeah, `filebeat` in the rpm image comes from the cmsweb base image, it is this package [2] from this repo [1] 

[1] https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/cmsweb/Dockerfile#L17
[2] https://github.com/dmwm/CMSKubernetes/blob/0cb2d75f9b74ff4aea5b80f679c04651aadcf14c/docker/cmsweb/Dockerfile#L42

## Comment (belforte, 2024-07-31T10:39:04Z)

I was not aware that we use cmsweb image as a start for TW as well. My bad. The sooner we have only one way to build containers, the better

## Comment (mapellidario, 2024-07-31T12:51:12Z)

After having a chat with wa, we decided that we should explore the possibility of running a single container in the TW machines that runs only filebeat and monitors the logs from all the containers in that VM. this allows to keep the TW image "clean". I will close this PR, in case we change idea again in the future we can re-open this one

## Comment (belforte, 2024-07-31T12:59:51Z)

Nice idea. SHould that contrainer do also the monitoring for grafana ? I am not sure what we gain by running it on crab-prod-tw02 other than making sure that the VM is running !
