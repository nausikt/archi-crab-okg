# dmwm/CRABServer pull request #9242: Robustify monit_reportrecallquota, inhibit flooding emails.

State: closed
Opened: 2025-12-08T14:23:18Z
Closed: 2025-12-08T15:16:48Z
URL: https://github.com/dmwm/CRABServer/pull/9242

## Opening post (nausikt, 2025-12-08T14:23:18Z)

Resolve #9241

Ciao @belforte,

IMO, I think just skipping accounts quota checking for this cycle, is Good enough, we don't need retry/attempts with max_attempts/exponential backoff in this case?
\> Since, CRON are retrying mechanism by itself. just skipped noises and wait for the next cycle?

P.S. Forgive me, I better try to bring RucioUtils like getRucioUsage into the loop of Vijay's Robustified RucioClient wrapper, to utilized it OR try to figure out why its not covered in each currently flooding cases, happened right now.

If we could used Vijay's wrapper it would be much more elegant/intuitive, Let me get back to you with new PR instead.

## Comment (belforte, 2025-12-08T17:04:42Z)

I think you should make sure that you understand what is going on, before you change the code.
DO you know for certain whether the script ultimately fails or not ? 
AFAIK we are using the retries in Rucio client which Vijay put it.

## Comment (nausikt, 2025-12-08T17:07:38Z)

Yes, in this PR, i'm not understood yet. Hopefully, what i try to stated in #9243 does.
