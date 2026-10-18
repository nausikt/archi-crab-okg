# dmwm/CRABServer issue #9130: Pipeline tasks should not have fixed instances

State: closed
Opened: 2025-07-10T22:10:45Z
Closed: 2025-10-14T13:34:28Z
URL: https://github.com/dmwm/CRABServer/issues/9130

## Opening post (aspiringmind-code, 2025-07-10T22:10:45Z)

See [here](https://github.com/aspiringmind-code/CRABServer/blob/bede18b544bdac1a0253873b61a84effd6ab7683/test/statusTrackingTasks/HC-splitByFile.py#L9) for example. Pipeline tasks should always run on the deployed instance with latest changes. Having fixed instance in these scripts defeats the purpose of checking with latest changes. This creates a mismatch situation where we might be deluded into a false sense of security by running tests on a machine that doesn't even have the changes we are testing. For my pipeline somehow weirdly some tasks are running on crab-dev-tw04 which should not be the case.
Make sure REST_instance is properly propagated everywhere and the tasks run only on the intended VM/REST instance with the deployed changes. @belforte @sinonkt  FYI

## Comment (nausikt, 2025-07-10T22:15:41Z)

Thanks Vi! for putting efforts on investigating these. I'll better aware of it, Thanks to your observation!
False sense of security are so scaryyy😱

## Comment (aspiringmind-code, 2025-07-10T22:30:19Z)

Ok I might have panicked a bit. For all tests, REST_instance is changed See [here](https://gitlab.cern.ch/crab3/CRABServer/-/jobs/58609774#L657) for example. The problem is with some CCV and Status Tracking tasks that somehow have crab-dev-tw04 in my [pipeline](https://gitlab.cern.ch/crab3/CRABServer/-/pipelines/12412106).

## Comment (belforte, 2025-07-11T08:48:02Z)

sounds that you have this under total control. Thanks

## Comment (belforte, 2025-10-10T12:32:37Z)

Is this still a relevan issue ? Or was it fixed in some possibly unrelated work in the pipeline ? I do not find the `tw04` string in the code base nor in `.gitlab-ci.yml`

## Comment (aspiringmind-code, 2025-10-14T13:34:28Z)

This issue has been fixed. Thanks!
