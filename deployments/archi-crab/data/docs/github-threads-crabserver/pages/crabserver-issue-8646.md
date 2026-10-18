# dmwm/CRABServer issue #8646: initial CRAB UI page is almost empty

State: closed
Opened: 2024-08-25T16:27:38Z
Closed: 2024-09-03T13:52:48Z
Labels: Type: Bug, Type: Support, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8646

## Opening post (belforte, 2024-08-25T16:27:38Z)

![image](https://github.com/user-attachments/assets/194d5b25-0d19-4d9d-be91-74cfae062bd7)



I think it is because the query `crabserver/prod/workflow?workflow=taskname` now returns an almost empty JSON

```text
belforte@lxplus9101/~> curl -s --cert $X509_USER_PROXY --key $X509_USER_PROXY  https://cmsweb.cern.ch:8443/crabserver/prod/workflow?workflow=240821_071926:oglez_crab_og08_21_091918__JetMET1_Run2024F-PromptReco-v1_NANOAOD|jq
{
  "result": [
    {
      "status": "",
      "command": "",
      "taskFailureMsg": "",
      "taskWarningMsg": [],
      "submissionTime": 0,
      "statusFailureMsg": "",
      "jobList": [],
      "schedd": "",
      "splitting": "",
      "taskWorker": "",
      "webdirPath": "",
      "username": ""
    }
  ]
}
belforte@lxplus9101/~> 
```


That JSON is prepared in
https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/HTCondorDataWorkflow.py#L105-L119

which I deprecated ! I had not realized that it is used in here. It is so difficult to track code in those REST* files !

It should be easy to fill those fields using info from
https://cmsweb.cern.ch/crabserver/prod/task?subresource=search&workflow=240821_071926:oglez_crab_og08_21_091918__JetMET1_Run2024F-PromptReco-v1_NANOAOD
which retrieves every column
https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/RESTTask.py#L81-L93

I simply need to dig out the code which I used to create `webdirPath`
Code is in https://github.com/dmwm/CRABServer/blob/5c7777045b33302fb97128ed29d4627141e009ec/src/python/CRABInterface/HTCondorDataWorkflow.py#L170
and following lines

More difficult is to find my way in the jquery code to find which query to change. I may decide to restore the deprecated code (or rename it) and do all the work in the REST, sending to the UI the correct JSON

Thanks @mapellidario for tips about using Web Developer Tools panel in the browser to identify the relevant HTTP calls. The error about webproxy was alas a red herring.

## Comment (belforte, 2024-08-25T16:48:29Z)

the query flow is:
* UI calls `workflow?workflow=taskname`
* that is served by RESTUserWorkflow and since there's no `subresource` field in the URL, code is https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/RESTUserWorkflow.py#L652-L656
* that in turn calls `status` function from HTCondorDataWorkflow which is our `userworkglowmanager` because of this line
```data.workflowManager = 'HTCondorDataWorkflow'``` [1]
in CRABServer's `config.py`

The decision to call `RESTUserWorkflow` or `RESTWorkerWorklow` is based on API being respecitively `workflow` or `workflowdb` as per https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/RESTBaseAPI.py#L58-L65

[1] things are bit twisty:
 * RESTUserWorflows calls DataUserWorkflow https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/RESTUserWorkflow.py#L34
 
 * DataUserWorkflows uses https://github.com/dmwm/CRABServer/blob/a1e9ca08f0972cb8a4db48570e9fd0ee91fd79b2/src/python/CRABInterface/DataUserWorkflow.py#L11

## Comment (belforte, 2024-09-02T19:16:59Z)

FWIW I looked at the code which I removed and contained what was used earlier in that `status` function and decided that it is a nightmare to fix it and get it back since it simply was doing too much
https://github.com/dmwm/CRABServer/blob/5c7777045b33302fb97128ed29d4627141e009ec/src/python/CRABInterface/HTCondorDataWorkflow.py#L170

## Comment (belforte, 2024-09-02T19:49:53Z)

best seems to change 
https://github.com/dmwm/CRABServer/blob/247a64e437c99ac046cc882c6d1eb82785aa1c2b/src/script/task_info.js#L824

to use RESTTask API, like in this used to show the full content of task table
https://github.com/dmwm/CRABServer/blob/247a64e437c99ac046cc882c6d1eb82785aa1c2b/src/script/task_info.js#L823

adding a "status" subresource so to make it easy to used a "slightly manipulated" version of "search"

## Comment (belforte, 2024-09-02T22:39:45Z)

more work than I thought, but I have something that works now
![image](https://github.com/user-attachments/assets/399d0eac-8c3d-4701-997c-deef5b28a1b3)

What I do not understand is that `tm_task_command` appears always empty, also using production REST and Task Info view
![image](https://github.com/user-attachments/assets/0ed7b0a6-9eed-4279-911c-12fbcf6d5d37)

But I verified in the code and it must be initialized to `SUBMIT` when task raw is inserted
https://github.com/dmwm/CRABServer/blob/247a64e437c99ac046cc882c6d1eb82785aa1c2b/src/python/CRABInterface/DataWorkflow.py#L179

I am sure it was there "recently". But this must be something else somewhere else :-(

## Comment (belforte, 2024-09-02T22:59:17Z)

I submitted a new task and `command` field is now OK.
Maybe we have some call down the line which resets it. Pff...
