# dmwm/CRABServer issue #7735: add a Jenkins test for Tape Recall

State: open
Opened: 2023-07-08T16:27:32Z
Labels: Type: Question, Priority: High, Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7735

## Opening post (belforte, 2023-07-08T16:27:32Z)

currently we never test this, we risk breaking it w/o noticing

## Comment (belforte, 2023-07-09T17:29:17Z)

I still do not know how to do this. As soon as we submit on a dataset/block which is on tape, the test can not be done again until the data has been remove from disk. Maybe we need to add a "test" flag ? Or simply kill that task ans its rule before it runs ? Something like:
submit, check that it reaches taperecall, kill.
But still if the data makes it to disk, we need different data in order to try again...
pick a RAW block at random ? and make sure that it is not on disk ?
Create an ad-hoc dataset and remove  disk replica if any before submitting the test ?

Nothing looks very appealing

## Comment (belforte, 2023-08-17T10:20:07Z)

No good ideas yet, no point in having this top priority
