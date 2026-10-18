# dmwm/CRABServer issue #9363: get list of FTS failure reasons in filetransfersdb table and check if we can improve classification

State: closed
Opened: 2026-07-22T11:07:43Z
Closed: 2026-08-28T15:30:21Z
URL: https://github.com/dmwm/CRABServer/issues/9363

## Opening post (belforte, 2026-07-22T11:07:43Z)

(no text)

## Comment (belforte, 2026-07-22T11:08:51Z)

goal is to break down the 60324 errors into sub-categories which may deserve different handling than dump retry (or task kill)

## Comment (belforte, 2026-07-22T14:37:17Z)

failure reason is in
https://github.com/dmwm/CRABServer/blob/30824ef153a0f3204d639587b799be5194c1f873/src/python/Databases/FileTransfersDB/Oracle/Create.py#L66

Note that we allow max 1K char here. I think the `[...CUT..]` is added in https://github.com/dmwm/CRABServer/blob/30824ef153a0f3204d639587b799be5194c1f873/src/python/TaskWorker/Actions/PostJob.py#L464 because reason used t be long and was always being cut. Ideally length of reason should be checked before adding this.

## Comment (nausikt, 2026-07-22T15:01:28Z)

Thanks for hints!

## Comment (nausikt, 2026-07-23T15:14:18Z)

Here's some quick summary of monthly distribution of file transfer failures [1,2], just to give us brief overview of the problem at hands. It doesn't tied with wasted CoreHR failed condor job id/req yet. 

**Next:** i will join transfer_failures with the actual wasted failed jobs to see real distribution & characteristic there. 
*P.S. lmk if you see i've carried away*

Total transfer failures: **751,307** 

Summarized reason | Distribution | Occurrences | Full failure message
-- | -- | -- | --
Destination storage full — HTTP 507 | 44.89% | 337,281 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 507 : Insufficient Storage
Transfer expired in queue | 26.69% | 200,558 | Job has been canceled because it stayed in the queue for too long (max-time-in-queue timeout)
Remote server error — HTTP 500 | 5.76% | 43,305 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 500 : Unexpected server error: 500
Source connection interrupted — curl 56 | 3.82% | 28,719 | SOURCE [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
Destination permission denied — HTTP 403 | 2.86% | 21,461 | DESTINATION [1] HTTP 403 : Permission refused
Destination unreachable — curl 7 | 2.80% | 21,069 | DESTINATION [112] Result curl error (7): Couldn't connect to server after 1 attempts
Destination SSL connection failure — curl 35 | 2.73% | 20,506 | DESTINATION [13] Result curl error (35): SSL connect error after 1 attempts
Destination connection interrupted — curl 56 | 2.61% | 19,592 | DESTINATION [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
Third-party-copy connection terminated | 1.77% | 13,269 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Connection terminated abruptly; Status of TPC request unknown
Destination connection timeout — curl 28 | 1.14% | 8,533 | DESTINATION [110] curl error (28): Timeout was reached
Source permission denied — HTTP 403 | 1.10% | 8,276 | SOURCE [1] HTTP 403 : Permission refused
Source file not found — HTTP 404 | 0.68% | 5,076 | TRANSFER [2] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 404 : File not found
Transfer permission denied — HTTP 403 | 0.64% | 4,820 | TRANSFER [1] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 403 : Permission refused
Certificate or remote-key validation failure — curl 60 | 0.32% | 2,390 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (60): SSL peer certificate or SSH remote key was not OK
Invalid or missing destination URL — curl 3 | 0.32% | 2,367 | DESTINATION [5] curl error (3): URL using bad/illegal format or missing URL
Other unlisted failure reasons | 1.87% | 14,085 | Not included in the provided query output
Total | 100.00% | 751,307 | —

[1] Group by failure reasons.
```sql
SELECT tm_transfer_failure_reason, COUNT(*) AS occurrences FROM filetransfersdb WHERE tm_creation_time >= SYSDATE - 30 AND tm_transfer_failure_reason IS NOT NULL GROUP BY tm_transfer_failure_reason ORDER BY occurrences DESC FETCH FIRST 100 ROWS ONLY;
```
[2] Total failure count
```sql
SELECT COUNT(*) AS failure_count FROM filetransfersdb WHERE tm_creation_time >= SYSDATE - 30 AND tm_transfer_failure_reason IS NOT NULL;
```

## Comment (nausikt, 2026-07-23T15:46:13Z)

One thing puzzled me is that over the last 6 months [1], somehow there's no of `CUT... fts_job_url` pattern been added into `tm_transfer_failure_reason` in filetransfersdb? [2]. 

Therefore, In case of fts job logs in details are needed, i will trace backed from PostJob or other way around instead e.g. reconstructed url from `tm_fts_id`.

[1]
```sql
SQL> SELECT COUNT(*) AS failure_count FROM filetransfersdb WHERE tm_creation_time >= ADD_MONTHS(SYSDATE, -6) AND tm_transfer_failure_reason LIKE '%CUT%';

FAILURE_COUNT
-------------
            0
```

[2]
https://github.com/dmwm/CRABServer/blob/30824ef153a0f3204d639587b799be5194c1f873/src/python/TaskWorker/Actions/PostJob.py#L460-L464

## Comment (nausikt, 2026-07-23T15:52:48Z)

Got my answer: the PostJob flow just dumped more reasons into PostJob logs, no synchronized back to `filetransferdb`.

## Comment (belforte, 2026-07-28T13:52:53Z)

I think that we already classify HTTP 507  (top of the list) with exit code 60323 and do not retry the transfer
https://github.com/dmwm/CRABServer/blob/0a4d004e1d6d686e3496b62d62ca96061dd9c2cb/src/python/ServerUtilities.py#L181-L192

Of course there can be bugs in the code...

Yet is odd that it is the most common error, in light of the ration of 60324 to 60323 in OpenSearch
https://github.com/dmwm/CRABServer/issues/9354#issue-4929686198

PostJob uses 60324 when it can't classify better the error message, so should be rare. I am very puzzled.

We may have to take a some PostJobs with 60324 and check what was happening. pfff....

OTOH I do not know what to do with `Transfer expired in queue`, sounds like we could benefit from introducing a new exit code !

Anyhow the table clearly indicates that there are cases where source/destination errors are separated, we need to reflect this in our exit code as well. What about introducing a new exit code also for "error at the source" ? Source errors can be transient (connection interrrupted) or fatal (file not found).  We should be careful not to introduce too many new exit codes.
Our current list is (from [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes)
```
60321 - Site related issue: no space, SE down, refused connection.
60322 - User is not authorized to write to destination site.
60323 - User quota exceeded.
60324 - Other stageout exception. 
```

## Comment (nausikt, 2026-07-28T17:18:34Z)

@belforte Yeah Thanks for all hints! I believe i got a good grasp of how the ASO worker and FTS work.

I will gathered raw FTS jobs log only for 60324 (quried from grafana-OS) failed jobs for fine-grained classification as you guided.
```
tm_jobid 
-> tm_id (tm_id are many-to-one with fts_id, also fts_id will be available later during post job life-cycle)
      Then, Normal ASO --> fts_id https://fts3-cms.cern.ch:8449/fts3/ftsmon/#/job/%s
            Rucio ASO --> fts_id --> rule_id -> external_id --> https://fts3-cms.cern.ch:8449/fts3/ftsmon/#/job/%s
```

Right now, i'm cooking up some pipeline for this investigation. will let you know when result available at https://cms-docs.web.cern.ch/CRAB/... tonight.

## Comment (belforte, 2026-07-28T17:42:46Z)

do we really need FTS logs ? Messages in your table look informative 
enough to me.
Maybe we can go through the table together ?Message ID: 
***@***.***>

## Comment (nausikt, 2026-07-28T18:55:33Z)

Sorry, Stefano for late reply. Yeah looks enough for me too, i just found few ~2% that reason not well defined by upstream and the text may much longer than 1000 chars. (I saw it truncated so just curious will dig into them later, we may report these to FTS folks)

[1] one example of 60234 that should matched 60317 (transfer timeout, unrecoverable? thus killable?) but our hardcode regexes missed them.
```sql
SQL> SELECT tm_transfer_failure_reason from filetransfersdb WHERE tm_taskname = '260728_065846:taehee_crab_260728_v2_QCD_Bin-PT-30to50_TuneCP5_13p6TeV_pythia8' and tm_jobid = '145' and tm_creation_time >= SYSDATE - 40  FETCH FIRST 1 ROWS ONLY;

TM_TRANSFER_FAILURE_REASON
--------------------------------------------------------------------------------
DESTINATION [110] curl error (28): Timeout was reached
```

Let me do my job! (also try not to let you work on your retirement and vacation time!)

## Comment (belforte, 2026-07-29T08:44:56Z)

> DESTINATION [110] curl error (28): Timeout was reached

This looks very clear to me. What more do you want to find ?

We use 60317 to indicate that CRAB waited 24h and then gave up, killed the transfer, and submitted a new job. I.e. situations where we have no information at all from FTS.

I know that this is not explained clearly in the twiki or similar, but you can always ask.

## Comment (nausikt, 2026-07-29T16:19:13Z)

Timeframe: 25-07-2026 00:00:00 - 27-07-2026 23:59:59

condor_raw_metrics: sum CoreHr ~= 820K (wasted) coreHrs
```json
{
  "bool": {
    "filter": [
      {
        "match_phrase": {
          "data.CMS_SubmissionTool": "CRAB"
        }
      },
      {
        "term": {
          "data.ExitCode": 60324
        }
      },
      {
        "match_phrase": {
          "data.Status": "Completed"
        }
      }
    ]
  }
}
```

condor_agg_metrics: sum sumCoreHr ~=  328k wasted (coreHr)
```
{
  "bool": {
    "filter": [
      {
        "exists": {
          "field": "data.CMS_JobType"
        }
      },
      {
        "exists": {
          "field": "data.Site"
        }
      },
      {
        "exists": {
          "field": "data.Tier"
        }
      },
      {
        "exists": {
          "field": "data.CMSPrimaryDataTier"
        }
      },
      {
        "match_phrase": {
          "data.Status": "Completed"
        }
      },
      {
        "match_phrase": {
          "data.Type": "analysis"
        }
      },
      {
        "match_phrase": {
          "data.CMS_SubmissionTool": "CRAB"
        }
      },
      {
        "term": {
          "data.ExitCode": 60324
        }
      }
    ],
    "must_not": [
      {
        "match_phrase": {
          "data.Tier": "Unknown"
        }
      }
    ]
  }
}
```

## Comment (belforte, 2026-08-03T15:44:48Z)

Hi @nausikt . I am making progress on "killing task after too many ASO errors", but I think that we need to improve on error characterization in order to make a reasonably educated decision and to report a message to users which can be somehow useful.

E.g. I found that 60324 is a default catch-all which also includes cases where CRAB retries automatically submitting another job. But we do not have a simple way to count how many times the resubmission fixes the problem. and  to connect that to the actual FTS error.

So we need more work on this, possibly linking FTS error msg with job exit code. But that would require combining info from transfersdb and OpenSearch (we do not have job exit codes in our DB). Or devise some way to modify PostJob to report this "somewhere", deploy and run for a month to collect data.

We need to talk, to think, to take decisions. And I am still waiting for some explanation on the fact that the most common msg which you found is one which should currently resutl in 60323, while in OpenSearch that exit cose is present much less frequently, https://github.com/dmwm/CRABServer/issues/9363#issuecomment-5105034441
Did you do any check on that ?

## Comment (nausikt, 2026-08-03T16:03:31Z)

Acknowledged, Thanks and Congrats for the progress.

It's likely simply that CRAB's FTS error regexes haven't kept up with changes to the upstream error logging messages.

No further checking yet, is 5 PM tomorrow O.K. to you for the talk?

## Comment (belforte, 2026-08-03T16:14:22Z)

> It's likely simply that CRAB's FTS error regexes haven't kept up with changes to the upstream error logging messages.

Nope. Certainly not with `"regex": ".*HTTP 507.*"` it should certainly match   `Destination storage full — HTTP 507`

I am very puzzled.

## Comment (nausikt, 2026-08-05T12:47:54Z)

> So we need more work on this, possibly linking FTS error msg with job exit code. But that would require combining info from transfersdb and OpenSearch (we do not have job exit codes in our DB). Or devise some way to modify PostJob to report this "somewhere", deploy and run for a month to collect data.
> 

We will go this way. kind of Dario/Wa's pyspark job approach.
```
Scheduler (Cron, daily/hourly up to us)
        │
        ▼
Spark Job ──► Read HDFS (raw_crab_condor_job)
        │
        ├──► Read Oracle via JDBC (transfersdb for failure_reasons)
        │
        ├──► Join + Transform
        │
        └──► Write to OpenSearch index
        │
        ▼
Prod FTS Error Grafana 
(*that could look back efficiently for cleaned historical + real-time report)
```
We could the same and come up with another variant for 50115 (or even 8021,8023) where we joined cmsRun, jobFJR logs instead.

For the characterizations and preemption let's discuss this afternoon na.

## Comment (nausikt, 2026-08-05T12:52:03Z)

P.S. FWIU from Stephan & Carlos, the condor jobs data in hdfs is the most primitive ones and is retained for up-to 6 months evens longer than kept in OS counterpart.

## Comment (belforte, 2026-08-05T13:00:21Z)

do we dump transfersdb table in HDFS too ? Or only task table ?

## Comment (nausikt, 2026-08-05T13:04:52Z)

No transfersdb dumping.

Data | HDFS Path | Format | Used In
-- | -- | -- | --
CRAB task table (taskdb) | /project/awg/cms/crab/tasks/{END_DATE}/ | avro | and
Rucio rules history | /project/awg/cms/rucio/{END_DATE}/rules_history/ | avro |  
Condor raw job metrics | /project/monitoring/archive/condor/raw/metric | JSON/Avro-mapped schema

## Comment (nausikt, 2026-08-05T13:09:02Z)

Will it still worth it to dumping in a clean organized streamlined way or ad-hoc joining is good enough? 

i saw you mentioned in FTS error tickets that we will no longer bother submit fts jobs and submitting less and less of them over time, moving toward fully outsource Rucio.

## Comment (nausikt, 2026-08-11T13:07:20Z)

Grateful for production-ready crab-spark workbench & how to bootstrapping things, secret & envs set-up, path configuring, CMSSpark utilities fns, so on and so forth by Dario, Wa & Eakong! [1]

They save me decades again!

- [1] https://github.com/dmwm/CRABServer/tree/master/src/script/Monitor/crab-spark

## Comment (belforte, 2026-08-11T13:38:19Z)

> i saw you mentioned in FTS error tickets that we will no longer bother submit fts jobs and submitting less and less of them over time, moving toward fully outsource Rucio.

that will happen with the new WMS tool and the demise of CRAB. No changes in CRAB are foreseen in that area.

## Comment (belforte, 2026-08-11T13:40:33Z)

Stefano and Krittin discussed this topic and what to do in a chat on Thursday, notes are in https://docs.google.com/document/d/1B6JUlf0d_1Mim59ZTZHtkU3IoDlGUZpCRWk0FaH1snw/edit?tab=t.0#heading=h.xukn13bkm73n

We do not need to do all possible actions described there.

## Comment (belforte, 2026-08-11T14:25:57Z)

@nausikt if you want to unleash more broadly your data analytics skills, here are a few questions which came to my mind yesterday when I was looking at failed jobs with 60324 vs. failed transfers with HTTP 507 vs. wasted core HR
* can we aggregate by tasks ?
   * is the wasted CPU sort of scattered all around due to glitches and transients (those curl errors...) so many tasks where only a small fraction of jobs fail ? (hence killing tasks will not help)
   * is the wasted CPU concentrated in tasks where most jobs fail ? (hence kill tasks will help a lot)
* I have seen a couple of tasks where more transfers succeeded but still O(20%) or more failed, is that representative ? Should we study this to decide when to actually kill things ?

* can we/should we correlate with wasted coreHr in order to decide if to kill ?

* would it help to aggregate by user ?

## Comment (nausikt, 2026-08-11T15:13:09Z)

Roger that, thank you teacher. I got my SWAN Analytix Hadoop access now. will make sure my brain is switched-on. LoL

<img width="1259" height="466" alt="Image" src="https://github.com/user-attachments/assets/97480c6f-80c6-465b-8569-a964c2efcee4" />

## Comment (nausikt, 2026-08-11T15:32:40Z)

The mountains of non-seasonal 60324 resonated with me and your fundamental questions raised above.

Try to correlate with users, or also each Site's SE which FTS has to contact, might reveal some underlying flooding/transients.

## Comment (nausikt, 2026-08-12T10:28:07Z)

Summarized reason | Distribution | Occurrences | Full failure message
-- | -- | -- | --
Transfer expired in queue | 51.76% | 81,363 | Job has been canceled because it stayed in the queue for too long (max-time-in-queue timeout)
Source connection interrupted — curl 56 | 19.23% | 30,225 | SOURCE [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
Transfer got no response from server — curl 52 | 5.54% | 8,704 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (52): Server returned nothing (no headers. no data)
Destination SSL connection failure — curl 35 | 5.50% | 8,640 | DESTINATION [13] Result curl error (35): SSL connect error after 1 attempts
Destination connection timeout — curl 28 | 4.79% | 7,522 | DESTINATION [110] curl error (28): Timeout was reached
Destination storage full — HTTP 507 | 4.65% | 7,314 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 507 : Insufficient Storage
Destination returned no response — curl 52 | 2.26% | 3,560 | DESTINATION [112] Result curl error (52): Server returned nothing (no headers. no data) after 1 attempts
Remote server error — HTTP 500 | 1.42% | 2,229 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 500 : Unexpected server error: 500
Destination permission denied — HTTP 403 | 1.15% | 1,808 | DESTINATION [1] HTTP 403 : Permission refused
Third-party-copy timeout (601–842 s) | 0.90% | 1,408 | TRANSFER [110] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy timeout of 601s
Source permission denied — HTTP 403 | 0.81% | 1,276 | SOURCE [1] HTTP 403 : Permission refused
Partial file transferred — curl 18 | 0.45% | 705 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (18): Transferred a partial file
Destination connection interrupted — curl 56 | 0.28% | 440 | DESTINATION [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
Third-party-copy connection terminated | 0.27% | 417 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Connection terminated abruptly; Status of TPC request unknown
Destination unreachable — curl 7 | 0.25% | 389 | DESTINATION [112] Result curl error (7): Couldn't connect to server after 1 attempts
Transfer permission denied — HTTP 403 | 0.23% | 364 | TRANSFER [1] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 403 : Permission refused
Destination timeout (900 s) | 0.10% | 164 | DESTINATION [110] timeout of 900s
Source unreachable — curl 7 | 0.09% | 140 | SOURCE [112] Result curl error (7): Couldn't connect to server after 1 attempts
Transfer SSL connection failure — curl 35 | 0.07% | 110 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (35): SSL connect error
Source rate-limited — HTTP 429 | 0.06% | 102 | SOURCE [5] Result HTTP 429 : Unexpected server error: 429 after 1 attempts
Source SSL connection failure — curl 35 | 0.05% | 78 | SOURCE [13] Result curl error (35): SSL connect error after 1 attempts
Transfer connection interrupted — curl 56 | 0.03% | 53 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (56): Failure when receiving data from the peer
Transfer bad request — HTTP 400 | 0.03% | 44 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 400 : Server Error
Source connection timeout — curl 28 | 0.03% | 43 | SOURCE [110] curl error (28): Timeout was reached
Transfer stalled — no FTS status update | 0.02% | 31 | No FTS server has updated the transfer status the last 900 seconds. Probably stalled
Source server error — HTTP 500 | 0.02% | 28 | SOURCE [5] Result HTTP 500 : Unexpected server error: 500 after 1 attempts
Transfer connection timeout — curl 28 | 0.01% | 12 | TRANSFER [110] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (28): Timeout was reached
Transfer failed — reason truncated | 0.00% | 5 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy
Endpoint refused connection (pool07.ifca.es) | 0.00% | 4 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Connect to pool07.ifca.es:1094 failed: Connection refused
Revoked host certificate (pool06.ifca.es) | 0.00% | 4 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: The peer's certificate ... CN=pool06.ifca.es ... Certificate was revoked
Source/destination file size mismatch | 0.00% | 4 | DESTINATION [22] Source and destination file size mismatch
Total | 100.00% | 157,186 | —

## Comment (nausikt, 2026-08-12T10:52:03Z)

### The ordering trap

STAGEOUT_ERRORS is a dict iterated in insertion order (60317 → 60321 → 60322 → 60323), so the first matching key wins. If you add a broad .*HTTP 5\d\d.* to 60321 to catch the HTTP 500s, it will also match HTTP 507 : Insufficient Storage and silently steal 7,368 events away from 60323 — turning your single largest actionable signal (destination site out of space) into generic "storage not accessible." Either make the 5xx regex exclude 507 (.*HTTP 5(?!07)\d\d.*) or keep it narrow by matching the FTS phrasing Unexpected server error: 500 as above.

## Comment (nausikt, 2026-08-12T11:00:23Z)

| Failure reason | Occurrences | Suggested code | Proposed regex | isPermanent |
| -- | -- | -- | -- | -- |
| Job canceled — max-time-in-queue | 81,154 | 60317 | `.*stayed in the queue for too long.*` | False |
| curl 56 (peer dropped data) — SOURCE/DEST/TRANSFER | 30,669 | 60321 | `.*curl error \(56\).*` | False |
| curl 52 (server returned nothing) | 12,302 | 60321 | `.*curl error \(52\).*` | False |
| curl 35 (SSL connect error) | 8,764 | 60321 | `.*curl error \(35\).*` | False |
| curl 28 (timeout reached) | 7,463 | 60321 | `.*curl error \(28\).*` | False |
| HTTP 500 / 429 / 400 from remote | 2,364 | 60321 | `.*Unexpected server error\: 5\d\d.*`, `.*HTTP 4[0-9,0-9] \: Server Error.*` | False |
| copy timeout of *N*s + `timeout of 900s` | 1,573 | 60317 | `.*timeout of \d+s.*` | False |
| curl 18 (partial file) | 705 | 60321 | `.*curl error \(18\).*` | False |
| curl 7 (couldn't connect) | 527 | 60321 | `.*curl error \(7\).*` | False |
| TPC terminated abruptly, status unknown | 417 | 60321 | `.*Connection terminated abruptly.*` | False |
| Stalled — no FTS status update | 31 | 60317 | `.*Probably stalled.*` | False |
| Connection refused (pool07) | 4 | 60321 | `.*[Cc]onnection refused.*` | False |
| Certificate revoked / rejected (pool06) | 4 | new | `.*certificate.*was rejected.*` or `.*[Cc]ertificate was revoked.*` | True |
| Source/destination size mismatch | 4 | new | `.*file size mismatch.*` | False |

## Comment (nausikt, 2026-08-12T15:52:26Z)

Below was queried from over 2 months (**12-06-2026** to **12-08-2026**) with 300 distinct aggregate failure reasons.

I will refine and analyze based on these subset of failure reasons.

Summarized reason | Distribution | Occurrences | Full failure message | Exit code
-- | -- | -- | -- | --
Destination storage full — HTTP 507 | 43.40% | 885,756 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 507 : Insufficient Storage | 60323
Transfer expired in queue | 18.62% | 380,097 | Job has been canceled because it stayed in the queue for too long (max-time-in-queue timeout) | 60317
Destination permission denied — HTTP 403 | 7.25% | 147,947 | DESTINATION [1] HTTP 403 : Permission refused | 60322
Remote server error — HTTP 500 (TRANSFER) | 6.87% | 140,287 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 500 : Unexpected server error: 500 | new
Source connection interrupted — curl 56 | 6.84% | 139,545 | SOURCE [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts | 60321
Destination connection interrupted — curl 56 | 4.42% | 90,231 | DESTINATION [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts | 60321
Source permission denied — HTTP 403 | 1.58% | 32,199 | SOURCE [1] HTTP 403 : Permission refused | 60322
Destination SSL connection failure — curl 35 | 1.60% | 32,712 | DESTINATION [13] Result curl error (35): SSL connect error after 1 attempts | 60321
Destination unreachable — curl 7 | 1.50% | 30,698 | DESTINATION [112] Result curl error (7): Couldn't connect to server after 1 attempts | 60321
Destination connection timeout — curl 28 | 1.38% | 28,219 | DESTINATION [110] curl error (28): Timeout was reached | 60321
Invalid or missing destination URL — curl 3 | 1.34% | 27,450 | DESTINATION [5] curl error (3): URL using bad/illegal format or missing URL | new
Third-party-copy connection terminated | 1.02% | 21,062 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Connection terminated abruptly; Status of TPC request unknown | 60321
Destination server error — HTTP 500 (per-URL, single user) | 0.76% | 15,538 | DESTINATION [5] HTTP 500 : Unexpected server error: 500 with url davs://eoshome-y.cern.ch:8444/eos/user/y/yurenw/... | new
Transfer permission denied — HTTP 403 | 0.75% | 15,211 | TRANSFER [1] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 403 : Permission refused | 60322
Transfer got no response from server — curl 52 | 0.45% | 9,228 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (52): Server returned nothing (no headers. no data) | 60321
Source file not found — HTTP 404 | 0.45% | 9,243 | TRANSFER [2] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 404 : File not found | new
Destination returned no response — curl 52 | 0.18% | 3,647 | DESTINATION [112] Result curl error (52): Server returned nothing (no headers. no data) after 1 attempts | 60321
Source connection timeout — curl 28 | 0.17% | 3,442 | SOURCE [110] curl error (28): Timeout was reached | 60321
dCache mover reply timeout | 0.15% | 3,009 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: java.io.IOException: timed out while waiting for mover reply | 60317
Certificate or remote-key validation failure — curl 60 | 0.15% | 3,010 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (60): SSL peer certificate or SSH remote key was not OK | new
Endpoint connect/read timeout (java) | 0.14% | 2,832 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Connect to cmseos.fnal.gov:9000 [...] failed: Connect timed out | 60321
Transfer stalled — no FTS status update | 0.13% | 2,746 | No FTS server has updated the transfer status the last 900 seconds. Probably stalled | 60317
Source unreachable — curl 7 | 0.12% | 2,548 | SOURCE [112] Result curl error (7): Couldn't connect to server after 1 attempts | 60321
Third-party-copy timeout (601–813 s) | 0.12% | 2,482 | TRANSFER [110] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy timeout of 601s | 60317
Partial file transferred — curl 18 | 0.09% | 1,831 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (18): Transferred a partial file | 60321
Transfer SSL connection failure — curl 35 | 0.08% | 1,546 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (35): SSL connect error | 60321
Revoked or mismatched host certificate | 0.08% | 1,654 | TRANSFER [5] ... Transfer failure: (certificate_unknown) The peer's certificate ... CN=llrgreosmgm.in2p3.fr ... Certificate was revoked at: Sat Jul | new
No write pools online (dCache) | 0.05% | 1,057 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Failed to select pool: No write pools online for [...linkgroup=spacemanager_linkGroup_dpmpool2] | 60323
Rucio LFN→PFN mapping failure | 0.06% | 1,164 | Failed to map lfn to pfn: RSE does not support requested protocol.\nDetails: No protocols found for this RSE | new
Source SSL connection failure — curl 35 | 0.07% | 1,364 | SOURCE [13] Result curl error (35): SSL connect error after 1 attempts | 60321
Destination timeout (900/1800 s) | 0.05% | 940 | DESTINATION [110] timeout of 900s | 60317
Transfer bad request — HTTP 400 | 0.04% | 731 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 400 : Server Error | new
Transfer failed — reason truncated | 0.03% | 620 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy | unclassified
Source timeout (900/1800 s) | 0.02% | 468 | SOURCE [110] timeout of 900s | 60317
Source cert/key not OK — curl 60 | 0.02% | 390 | SOURCE [13] Result curl error (60): SSL peer certificate or SSH remote key was not OK after 1 attempts | new
Host name resolution failure — curl 6 | 0.02% | 346 | SOURCE [113] Result curl error (6): Couldn't resolve host name after 1 attempts | 60321
Authentication error — HTTP 401 | 0.02% | 315 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 401 : Authentication Error | 60322
Rate-limited — HTTP 429 | 0.01% | 171 | SOURCE [5] Result HTTP 429 : Unexpected server error: 429 after 1 attempts | new
Delegation failure (SOAP fault) | 0.01% | 122 | TRANSFER [13] ... copy 0) Could not get the delegation id: Could not get proxy request: SOAP 1.1 fault ... "Connection timed out" | unclassified
Network unreachable | 0.00% | 84 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Network is unreachable | 60321
Space reservation not authorized | 0.00% | 68 | TRANSFER [5] ... Failed to select pool: diskCacheV111.services.space.SpaceAuthorizationException: Unable to reserve space: user not authorized to reserve space in any linkgroup. | 60323
Server error — HTTP 501/502 | 0.00% | 33 | DESTINATION [112] HTTP 501 : Server Error | new
Connection refused (pool07.ifca.es) | 0.00% | 4 | TRANSFER [5] ... Transfer failure: Connect to pool07.ifca.es:1094 [...] failed: Connection refused (Connection refused) | 60321
Source/destination file size mismatch | 0.00% | 20 | DESTINATION [22] Source and destination file size mismatch | unclassified
Canceled by user (gfal2) | 0.00% | 18 | DESTINATION [125] [gfal2_cancel] operation canceled by user | unclassified
Failed sending data to peer — curl 55 | 0.00% | 7 | SOURCE [112] Result curl error (55): Failed sending data to the peer after 1 attempts | 60321
Total | 100.00% | 2,041,047 | — |

## Comment (nausikt, 2026-08-25T16:26:59Z)

Before, i revise regexes. could you @belforte  review the following names and its definition please?

## [60323] 507 Insufficient Storage, 43.40% (Existing, Permanent)
Definition: Destination storage full — HTTP 507
raw_reason:  43.40% | 885,756 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 507 : Insufficient Storage
Action: **NO**, current Regexes already covered.
IsPermanent: **True**
```json
{
    60323: [
                           {"regex": ".*does not have enough space.*",
                            "error-msg": "User quota exceeded.",
                            "isPermanent": True},
                           {"regex": ".*disk quota exceeded.*",
                            "error-msg": "Disk quota exceeded.",
                            "isPermanent": True},
                           {"regex": ".*HTTP 507.*",
                            "error-msg": "HTTP 507: Disk quota exceeded or Disk full.",
                            "isPermanent": True},
                           {"regex": ".*status code 507.*",
                            "error-msg": "HTTP 507: Disk quota exceeded or Disk full.",
                            "isPermanent": True},
    ]
}
```

## [60AAA], Local FTS MaxTimeOut, 18.62% (New?, Transient)
***Newly*** spilt from 60317 - Forced timeout for stuck stage out?? 
or it considered to be global ASO Transfer forced timed out*, (**I guessed the former**)
Definition: Job canceled, Transfer expired in queue 
raw_reason: 18.62% | 380,097 | Job has been canceled because it stayed in the queue for too long (max-time-in-queue timeout)
New RegEx: `.*stayed in the queue for too long.*`
IsPermanent: **False**

Existing ASO Transfer 60317
```json
{ 60317: [
         {"regex": ".*Cancelled ASO transfer after timeout.*",
          "error-msg": "ASO Transfer canceled due to timeout.",
          "isPermanent": True}
  ],
}
```

## [60322], 403 Permission denied, 10% (Existing, Permanent)
Definition: Source|Transfer|Destination Permission denied.
raw_reasons:
7.25% | 147,947 | DESTINATION [1] HTTP 403 : Permission refused
1.58% | 32,199 | SOURCE [1] HTTP 403 : Permission refused
0.75% | 15,211 | TRANSFER [1] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 403 : Permission refused
Action: **NO**, current Regexes already covered. (maybe need to check case sensitivity)
IsPermanent: **True**
```json
{
             60322: [
                           {"regex": ".*permission denied.*",
                            "error-msg": "Permission denied.",
                            "isPermanent": True},
                           {"regex": ".*Permission refused.*",
                            "error-msg": "Permission denied.",
                            "isPermanent": True},
                           {"regex": ".*operation not permitted.*",
                            "error-msg": "Operation not allowed.",
                            "isPermanent": True},
                           {"regex": ".*mkdir\\(\\) fail.*",
                            "error-msg": "Can`t create directory.",
                            "isPermanent": True},
                           {"regex": ".*open/create error.*",
                            "error-msg": "Can`t create directory/file on destination site.",
                            "isPermanent": True},
                           {"regex": ".*mkdir\\: cannot create directory.*",
                            "error-msg": "Can`t create directory.",
                            "isPermanent": True},
                           {"regex": ".*530-login incorrect.*",
                            "error-msg": "Permission denied to write to destination site.",
                            "isPermanent": True},
                          ],
}
```

## [60BBB], PeerDroppedData, 11.2% (New Transient)
Definition: Source|Destination interrupted.
raw_reasons:  
6.84% | 139,545 | SOURCE [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
4.42% | 90,231 | DESTINATION [112] Result curl error (56): Failure when receiving data from the peer after 1 attempts
New Regexes:  `.*curl error \(56\).*` 
IsPermanent: **False**


## [60CCC], 500 Novel FTS ServerFault, 7.7% (new transient?)
*yurenw Again! him alone took 0.76% LoL*
Definition: Remote/Destination (FTS) server error | HTTP 500/501/502
raw_reasons:
6.87% | 140,287 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 500 : Unexpected server error: 500
0.76% | 15,538 | DESTINATION [5] HTTP 500 : Unexpected server error: 500 with url davs://eoshome-y.cern.ch:8444/eos/user/y/yurenw/...
0.00% | 33 | DESTINATION [112] HTTP 501 : Server Error
New Regexes: `.*Unexpected server error\: 5\d\d.*`, `.*HTTP 5[0-9,0-9]*`
IsPermanent: **False**

## [60DDD], 40X BadRequest, Permanent bad url/illegal format and 404 file not found, 1.8% (New Permanent)
Defintion: Source file not found, Invalid or missing destination URL, Authentication error, Rate-limited — HTTP 401|404|429.
raw_reasons:
0.45% | 9,243 | TRANSFER [2] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 404 : File not found
1.34% | 27,450 | DESTINATION [5] curl error (3): URL using bad/illegal format or missing URL
0.02% | 315 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy HTTP 401 : Authentication Error
0.01% | 171 | SOURCE [5] Result HTTP 429 : Unexpected server error: 429 after 1 attempts
New Regexes: ` .*HTTP 404 \: File not found.*`, `.*curl error \(3\)\: URL using bad/illegal format or missing URL.*`, `.*HTTP 401*`, `.*HTTP 429*`
IsPermanent: **True**

## [60EEE], SSL connection failure, 1.8% (New Transient)
Definition: Source|Transfer|Destination SSL connection failure 
raw_reasons: 
1.60% | 32,712 | DESTINATION [13] Result curl error (35): SSL connect error after 1 attempts
0.07% | 1,364 | SOURCE [13] Result curl error (35): SSL connect error after 1 attempts
0.08% | 1,546 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (35): SSL connect error
New Regexes:  `.*curl error \(35\).*`
IsPermanent: **False**

## [60FFF], Src|Dest Unreachable, 1.6% (New Transient)
Definition: curl 7 (couldn't connect), Source|Destination unreachable
raw_reasons:
0.12% | 2,548 | SOURCE [112] Result curl error (7): Couldn't connect to server after 1 attempts
1.50% | 30,698 | DESTINATION [112] Result curl error (7): Couldn't connect to server after 1 attempts
New Regexes:  `.*curl error \(7\).*`
IsPermanent: **False**

## [60GGG], Src|Dest (FTSClient?) Connection Timeout 1.6% (New Transient)
Definition: curl 28 (timeout reached), Source|Destination connection timeout
raw_reasons:
1.38% | 28,219 | DESTINATION [110] curl error (28): Timeout was reached
0.17% | 3,442 | SOURCE [110] curl error (28): Timeout was reached
New Regexes: `.*curl error \(28\).*`
IsPermanent: **False**

## [60HHH], Third-party-copy connection terminated, 1.0% (New Transient?)
Definition: Third-party-copy connection terminated abruptly
raw_reasons:
1.02% | 21,062 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Connection terminated abruptly; Status of TPC request unknown
New Regexes: `.*Connection terminated abruptly.*`
IsPermanent: **False**

## [60III], Transfer|Destination got no response from server, 0.6% (New Transient?)
Definition: curl 52 (server returned nothing)
raw_reasons:
0.45% | 9,228 | TRANSFER [112] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (52): Server returned nothing (no headers. no data)
0.18% | 3,647 | DESTINATION [112] Result curl error (52): Server returned nothing (no headers. no data) after 1 attempts
New Regexes: `.*curl error \(52\).*` 
IsPermanent: **False**?

## Comment (nausikt, 2026-08-25T16:33:29Z)

It seems to me that 60321 no longer match and completely obsolete. So many new ExitCodes was either breakdown from `60321` or `60317` in some sense.
```json
{  
     60321: [
                         {"regex": ".*reports could not open connection to.*",
                            "error-msg": "Storage element is not accessible.",
                            "isPermanent": False},
                           {"regex": ".*451 operation failed\\: all pools are full.*",
                            "error-msg": "Destination site does not have enough space on their storage.",
                            "isPermanent": True},
                           {"regex": ".*system error in connect\\: connection refused.*",
                            "error-msg": "Destination site storage refused connection.",
                            "isPermanent": False}
                          ],
}
```

## Comment (nausikt, 2026-08-25T17:03:47Z)

## Other possilby new Transient/Permanent BUT Niche
*shall we leave them with 60324 (No-Name) for now, breakdown later?*

- **dCache mover reply timeout**
| 0.15% | 3,009 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: java.io.IOException: timed out while waiting for mover reply
- **Certificate or remote-key validation failure — curl 60**
| 0.15% | 3,010 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (60): SSL peer certificate or SSH remote key was not OK
- **Endpoint connect/read timeout (java)**
| 0.14% | 2,832 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Connect to cmseos.fnal.gov:9000 [...] failed: Connect timed out
- **Transfer stalled — no FTS status update**
| 0.13% | 2,746 | No FTS server has updated the transfer status the last 900 seconds. Probably stalled | 60317
Third-party-copy timeout (601–813 s) | 0.12% | 2,482 | TRANSFER [110] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy timeout of 601s
- **Partial file transferred — curl 18**
| 0.09% | 1,831 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy curl error (18): Transferred a partial file
- **Revoked or mismatched host certificate**
| 0.08% | 1,654 | TRANSFER [5] ... Transfer failure: (certificate_unknown) The peer's certificate ... CN=llrgreosmgm.in2p3.fr ... Certificate was revoked at: Sat Jul
- **No write pools online (dCache)**
| 0.05% | 1,057 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Failed to select pool: No write pools online for [...linkgroup=spacemanager_linkGroup_dpmpool2]
- **Rucio LFN→PFN mapping failure**
| 0.06% | 1,164 | Failed to map lfn to pfn: RSE does not support requested protocol.\nDetails: No protocols found for this RSE
- **Destination timeout (900/1800 s)**
| 0.05% | 940 | DESTINATION [110] timeout of 900s
**Source timeout (900/1800 s)** 
| 0.02% | 468 | SOURCE [110] timeout of 900s
- **Source cert/key not OK — curl 60**
| 0.02% | 390 | SOURCE [13] Result curl error (60): SSL peer certificate or SSH remote key was not OK after 1 attempts | new
- **Transfer failed — reason truncated**
| 0.03% | 620 | TRANSFER [13] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: copy
- **Host name resolution failure — curl 6**
| 0.02% | 346 | SOURCE [113] Result curl error (6): Couldn't resolve host name after 1 attempts
- **Delegation failure (SOAP fault)**
| 0.01% | 122 | TRANSFER [13] ... copy 0) Could not get the delegation id: Could not get proxy request: SOAP 1.1 fault ... "Connection timed out"
- **Network unreachable**
| 0.00% | 84 | TRANSFER [5] TRANSFER ERROR: Copy failed (3rd pull). Last attempt: Transfer failure: Network is unreachable
- **Space reservation not authorized**
| 0.00% | 68 | TRANSFER [5] ... Failed to select pool: diskCacheV111.services.space.SpaceAuthorizationException: Unable to reserve space: user not authorized to reserve space in any linkgroup.
- **Connection refused (pool07.ifca.es)**
| 0.00% | 4 | TRANSFER [5] ... Transfer failure: Connect to pool07.ifca.es:1094 [...] failed: Connection refused (Connection refused) | 60321
- **Source/destination file size mismatch**
| 0.00% | 20 | DESTINATION [22] Source and destination file size mismatch
- **Canceled by user (gfal2)**
| 0.00% | 18 | DESTINATION [125] [gfal2_cancel] operation canceled by user
- **Failed sending data to peer — curl 55**
| 0.00% | 7 | SOURCE [112] Result curl error (55): Failed sending data to the peer after 1 attempts

## Comment (belforte, 2026-08-25T17:21:58Z)

I agree that none of the current regexps for 60321 matches anymore, but maybe the description
` Site related issue: no space, SE down, refused connection. ` Still can be used  ? E.g. cases where we do not know if source or destination was bad.
Goal is not to have one exit code for every possible message, of course. But to categorize all possible messages in "string which make sense for possible actions", even as simple actions as pointing to the site to contact.

YOu should be careful with isPermanent T/F. In a way all errors are transient, we know that we can transfer files to all T2's, even filled user quota is a temporary problem.

Our initial goal is to make sure that we detect an handle properly at least all errors which point to full user quota.

## Comment (nausikt, 2026-08-25T17:26:50Z)

Thank you for thought-provoking review, will re-think accordingly na.
