# dmwm/CRABServer issue #7502: Collect statistics on datasets usage in CRAB

State: open
Opened: 2023-01-20T11:59:16Z
URL: https://github.com/dmwm/CRABServer/issues/7502

## Opening post (belforte, 2023-01-20T11:59:16Z)

This issue tracks progress of work initiated by @dynamic-entropy also building up on https://github.com/dmwm/CRABServer/projects/14

We have 2 ambitious goals:

 1.  understand dataset fragmentation (when a small datasets is made of several blocks places "one here, one there" well enough to give us if we should embark in "coalescing datasets before submitting tasks" or not and what we may gain (may include understanding of error reasons as well)
 
 2.  understand dataset use and reuse and tape recall performance and well enough to tell us if we could extend the use of T2 space as a dynamic cache rather than a place of static datasets pre-location waiting for users to access them

## Comment (belforte, 2023-01-20T12:10:01Z)

as agreed in CRAB meeting, I kick this off by pasting here the summary of the presentation made by @dynamic-entropy which had been sitting in meeting minutes for months by now.

FYI @dynamic-entropy @dciangot @KatyEllis  @mapellidario @novicecpp . Feel free to add and better clarify current situation (e.g. I had a chat with Rahul on zoom before Xmas, but did not take notes) and what other or different goals we should have. I only wanted to have a place where we write things, not to impose my view.

```
Rahul showed some slides on his latest work with the dataset usage by CRAB.
There are some slightly confusing results, for example why there is a peak of usage ~40 days
after the first usage. Is this one user?
This repo can be cloned and run on SWAN: https://github.com/dynamic-entropy/CRABAnalysis.
The “crab_historical.ipynb” is the desired notebook. 

Update from Rahul:
Rahul showed his Jupyter notebooks showing e.g. a histogram of dataset popularity
for CRAB jobs in the last 2 years.
He described wanting to run a ‘simulation’ to find ways to improve placement of data for CRAB jobs.
Rahul working on command to insert “user data” from  local disk to Rucio managed storage.
See https://github.com/dmwm/CMSRucio/issues/275  . See above on new reporting guideline.

Reposting lines for Rahul still unclear, there’s a codi document to keep track
of questions which we are editing, but not clear that changes to it are noticed.
We agree with Diego that we will ask him to report in this meeting weekly
on work on “the CRAB active dataset” and “what data is on disk, why”,
and encourage him to use group channels in MatterMost
so we can all help and at least make sure that he gets coherent messages.
```
