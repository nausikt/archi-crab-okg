# dmwm/CRABServer issue #8686: Add private task examples to "status Tracking" directory

State: open
Opened: 2024-09-03T16:43:05Z
Labels: Type: Question
URL: https://github.com/dmwm/CRABServer/issues/8686

## Opening post (novicecpp, 2024-09-03T16:43:05Z)

Private tasks are basically another StatusTracking test, but separate from [test/statusTrackingTasks](https://github.com/dmwm/CRABServer/tree/f5687adbf5fddeb21526c33b623b2f5025e17945/test/statusTrackingTasks) that we can run it on-demand. 

Ideally, trigger pipeline with variable like `RUN_STATUS_TRACKING_PRIVATE` to run the private tasks on gitlab. Need to add some switch in StatusTracking script to switch back and forth between usual one and private one.

## Comment (belforte, 2024-12-12T10:09:40Z)

I am not sure what the idea behind this is. Need to think.
