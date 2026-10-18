# dmwm/CRABServer issue #8928: add a flag in task Table to indicate that task was UPLOADED to S3

State: closed
Opened: 2025-02-17T14:11:13Z
Closed: 2025-05-22T10:49:09Z
Labels: Type: Enhancement, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8928

## Opening post (belforte, 2025-02-17T14:11:13Z)

for tasks submitted w/o dry run, UPLOADED is a transient status, tasks get there after QUEUED and progress immediately to SUBMITTED and possibly other statuses.
This makes it difficult to tell from Client is task is ready to run `crab preparelocal`  as discussed in https://github.com/dmwm/CRABClient/issues/5371#issuecomment-2662962817

Desired behavior could be that when Uploader action is completed a flag is set in the DB and client checks that, keeping UPLOADED status as it was until a few months ago only for tasks "halted" for dry-run submission which wait for a `crab proceed` command in order to progress to SUBMITTED.

Consistently with 
https://cmscrab.docs.cern.ch/crab-design/crab-task-state.html

## Comment (aspiringmind-code, 2025-04-08T10:42:23Z)

[Completed](https://github.com/dmwm/CRABServer/issues/8973)

## Comment (belforte, 2025-04-08T13:24:27Z)

Well... we have the column in the DB but do not write to it yet.
I am reopening, but if you prefer a more ad-hoc issue, feel free to close again and open a new one.
