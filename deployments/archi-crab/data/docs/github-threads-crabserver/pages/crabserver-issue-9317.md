# dmwm/CRABServer issue #9317: Commented-out functions ever used?

State: closed
Opened: 2026-05-19T12:13:43Z
Closed: 2026-05-20T09:50:12Z
URL: https://github.com/dmwm/CRABServer/issues/9317

## Opening post (oljemark, 2026-05-19T12:13:43Z)

Looking at commented-out code, test_prepare_duplicate_replicas(), from here https://github.com/dmwm/CRABServer/blob/master/test/python/ASO/Rucio/Actions/test_RegisterReplicas.py#L162 , was never used, right? It was introduced in #7637 (#7649).

The only other extant "#def " occurrences I found were from the same commit, test_Transfer_readInfo() and test_Transfer_readInfo_filenotfound(), the former being called an "old relic" here https://github.com/dmwm/CRABServer/blob/master/test/python/ASO/Rucio/test_Transfer.py#L71-L72
So were the latter pre-existing / never-used functions only on the rucio_transfers branch (which is gone) or is there some lost history  (like PR #6844 talking about ASOConfig as an old relic to remove)?

## Comment (belforte, 2026-05-20T08:44:34Z)

Hi @oljemark 
everything in current CRABServer/test/python is actually unused. It is was an "exercise" in using pytest and unittest packages to add unit tests to CRAB code which alas never converged to full program of covering the whole tool. Given the manpower situation, that effort was abandoned when the guy who kickstarted it left.
Consensus was that it is too much work to retrofit all code that we have, given that changes are now rare.

I can certainly agree that this is not  professionally maintained and documented package, but since it is now clear that it will not outlive me, we can hopefully keep it sort of frozen for then next few years.

## Comment (belforte, 2026-05-20T08:51:47Z)

there quite some confused "history" so some files in CRABServer/test are actually used in new CI pipeline, even if those should better live elsewhere, but proper cleanup and related fixing of the code is very low in priority.

## Comment (belforte, 2026-05-20T08:52:04Z)

Do you agree to close this ?

## Comment (oljemark, 2026-05-20T09:04:01Z)

Hi, @belforte . Yes, certainly.

## Comment (oljemark, 2026-08-05T12:35:44Z)

Hi again, @belforte . Re: unit tests, I was just wondering if the old unit tests in PostJob.py, starting here (https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L3159) do anything anymore? Possibly setup() still dumps the test JSON file here (https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L3207)? 
At least the three helper functions here (https://github.com/dmwm/CRABServer/blob/cd03a20b880425c44f5140b44be5f10462439367/src/python/TaskWorker/Actions/PostJob.py#L3187-L3194) had their last calls removed in the Python 3 migration 16a275f025f0bf7627420c1e81900823b00bfbb4 when the testExistent() / testNonexistent() functions were removed.

## Comment (belforte, 2026-08-05T12:46:27Z)

I have never seen those test being used, and I never tried myself. We do not have any automated way to run them.
For sure so many things have changed in postJob since then that tests are either failing or not covering enough to be trusted.
Hopefully those tests helped the initial implementers to come up with a working script. But now we only do small incremental changes and strive to check them in realistic conditions.
