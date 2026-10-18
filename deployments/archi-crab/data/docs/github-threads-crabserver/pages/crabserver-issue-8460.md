# dmwm/CRABServer issue #8460: adapt to FTS Client 3.13

State: closed
Opened: 2024-06-03T10:20:26Z
Closed: 2024-06-07T14:34:54Z
Labels: Type: Bug, Type: Enhancement, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8460

## Opening post (belforte, 2024-06-03T10:20:26Z)

there is (at least) one non-backward compatible change
```
all our FTS submissions fail with
    job = fts3.new_job(transfers,
TypeError: new_job() got an unexpected keyword argument 'spacetoken' 
```
I am communicating with FTS developers about this
<details><summary>mail sent to FTS developers</summary>

</details>

temporary workaround was to  force ([this](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/7028e0593ea2ce42b07f3c555a5ed744ee5a5567) commit and two following ones) older FTS version. See also https://cms-talk.web.cern.ch/t/jobs-stuck-at-transfer/41870/3?u=belforte

Waiting for clarifications from FTS developers before changing our code
https://github.com/dmwm/CRABServer/blob/f6c01ebafddb56ea7f15cbcf8f8563baae20114a/scripts/task_process/FTS_Transfers.py#L329-L331

## Comment (belforte, 2024-06-03T16:36:00Z)

here's FTS answer
```
Hello Stefano,

Apologies for creating problems for the CRAB submission system.

From the previous verison to FTS v3.13.0, the "new_job()" and "new_staging_job()" signatures have been changed.
The field "spacetoken" was renamed from "spacetoken" --> "destination_spacetoken".

We checked before releasing with Rucio and DIRAC. I apologies for not checking with CRAB as well.

To move forward:

    I will (probably) tag FTS v3.13.1 which brings back the old "spacetoken" field, but prints a deprecation warning. I assume you aren't the only system impacted.
    Are you reding these deprecation warnings? If we add them to the codebase, will you be able to see and act on them? (I'm afraid these large systems often hide these warnings)
    No matter what, whether in this release or the next big one (FTS v3.14.0), things will get uncomfortable. In FTS v3.14.0 we will add source & destination tokens to the submit functions signatures. If we add the deprecating warning, it is also in FTS v3.14.0 when we will remove the deprecated field
```

## Comment (belforte, 2024-06-03T18:38:02Z)

and this is the final word
```
en" --> "destination_spacetoken" argument backwards compatible.

All the "fts3.new_job(..)" parameters are optional, with default "None" value. The same applies for the (destination_)spacetoken. So if you don't add "spacetoken" or "destination_spacetoken" when you invoke "fts3.new_job(..)", there is no harm. It's only when you pass "spacetoken" specifically that it breaks in the new version, as seems to be in your case.

In your FTS submission code, I recommend dropping the "source_spacetoken=None" and "spacetoken=None" lines [1] (or replace "spacetoken=None" with "destination_spacetoken=None"). The backwards-compatibility fix will be released, bringing back "spacetoken". If you wait for it, no change will be needed in your code.

However, please prepare for the removal of the "spacetoken" field in FTS v3.14, as well as the addition of source + destination (access) tokens to the "fts3.new_transfer(..)" signature. I will announce those better and ahead of time.
```

## Comment (belforte, 2024-06-04T16:19:50Z)

I have removed the lines
https://github.com/dmwm/CRABServer/blob/f6c01ebafddb56ea7f15cbcf8f8563baae20114a/scripts/task_process/FTS_Transfers.py#L329-L331

new code should work with past and present FTS client. And IIUC also with coming FTS client v3.14

## Comment (belforte, 2024-06-05T12:17:34Z)

need to apply fix again to master after I had to revert to v3.240530
