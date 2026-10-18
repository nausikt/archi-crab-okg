# dmwm/CRABServer issue #8779: Include SendVenvFolder test in Client Configuration Validation of gitlab pipeline

State: closed
Opened: 2024-11-08T13:01:51Z
Closed: 2024-11-12T12:19:38Z
Labels: Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8779

## Opening post (aspiringmind-code, 2024-11-08T13:01:51Z)

Currently, Jenkins runs the SendVenvFolder test in CCV but Gitlab pipeline has it commented out as it throws an error of not finding venv folder. 
See [here](https://github.com/dmwm/CRABServer/blob/master/test/makeTests.py#L272C1-L284C72) 
Investigate and add this test as part of the pipeline.

## Comment (belforte, 2024-11-08T13:22:54Z)

hmm... `venv` folder is created here
https://github.com/dmwm/CRABServer/blob/ca67bbf5d6d5f8c2a309d5805813830d48189eb7/test/container/testingScripts/setupCRABClient.sh#L16-L18

## Comment (belforte, 2024-11-08T13:34:09Z)

and this test works when executed via Jenkins. DId you try to simply uncomment it ?

## Comment (aspiringmind-code, 2024-11-08T13:36:58Z)

@belforte  Yes, in the PR I have uncommented, that's why this issue is created as it is being left out of the Cv CCV PR.

## Comment (belforte, 2024-11-08T13:39:11Z)

I am really curious what happens differently in the pipeline which makes it fail. Feel free to point me at logs.

## Comment (belforte, 2024-11-08T18:03:38Z)

so the problem is that CRABClient is not setup with that script which I quoted, but by a new one
https://github.com/dmwm/CRABServer/blob/master/cicd/gitlab/setupCRABClient.sh
which is not simply "the old one copied to the new directory" as I thought. But at least lacks the lines which create the `venv` directory.

So fix is easy. But we need to check if there are other differences.

## Comment (belforte, 2024-11-08T18:09:19Z)

for history: the way to find out was to "notice" the following line in https://gitlab.cern.ch/crab3/CRABServer/-/jobs/45743592/raw
```
+ source /home/gitlab-runner/shell/builds/sedxNxqzs/0/crab3/CRABServer/cicd/gitlab/setupCRABClient.sh
```

## Comment (aspiringmind-code, 2024-11-12T12:19:38Z)

Thanks Stefano for the quick diagnosis! Fixed in the [PR](https://github.com/dmwm/CRABServer/pull/8696) Closing this issue.
