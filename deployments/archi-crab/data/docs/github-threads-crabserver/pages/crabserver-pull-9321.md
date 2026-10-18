# dmwm/CRABServer pull request #9321: Fix heavy query

State: closed
Opened: 2026-06-04T15:14:06Z
Closed: 2026-06-06T14:07:38Z
Merged: 2026-06-06T14:07:38Z
URL: https://github.com/dmwm/CRABServer/pull/9321

## Opening post (nausikt, 2026-06-04T15:14:06Z)

Resolve #9320 

I have tested the extended sql queries and it looks good with roughly 2 orders of magnitude speed up [1].

[1]
```sql
SQL> SELECT COUNT(*) FROM tasks WHERE tm_task_status = 'SUBMITTED' and ROWNUM <= 1000 AND tw_name LIKE 'crab-prod-tw01' ORDER BY tm_start_time ASC;

  COUNT(*)
----------
      1000

Elapsed: 00:00:02.21
SQL> SELECT COUNT(*) FROM tasks WHERE tm_task_status = 'SUBMITTED' and ROWNUM <= 1000 AND tw_name LIKE 'crab-prod-tw01' and tm_start_time > SYSDATE - INTERVAL '1' MONTH ORDER BY tm_start_time ASC;

  COUNT(*)
----------
      1000

Elapsed: 00:00:00.01
```

## Comment (cmsdmwmbot, 2026-06-04T15:17:39Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 35 comments to review
 * Pycodestyle check: succeeded
   * 207 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2828/artifact/artifacts/PullRequestReport.html

## Comment (nausikt, 2026-06-04T16:18:26Z)

@belforte Ciao Stefano, 

**\*Despite** GET workflowdb (/workflowdb) ***\~ 10 seconds*** (**GetReadyTasks_sql** we solved above)

there is other 2 endpoints that seems to execute slow queries as well, would like you to comments please?
___________

### [1] POST workflowdb (/workflowdb) ***\~ 3 seconds***
*IIUC, we can't do anything better for this endpoint. since they are update operation* (only indexing may help)
- [x] [No Action] which execute **SetStatusTask_sql**, **SetFailedTasks_sql**, **SetInjectedTasks_sql**, and UpdateWorker_sql 

### [2] GET RESTFileTransfers (fileTransfersDB database) ***\~10~14 seconds***
- [ ] which execute **GetGroupedTransferStatistics0_sql**, **GetGroupedTransferStatistics1_sql**, ..., **GetGroupedTransferStatistics5a_sql** that's looks fine.

**Except** GetGroupedTransferStatistics0_sql query who seems to scans the whole table as well, this query *alone* took 10 seconds [1].

**BUT** in this case adding time filtering alone will worsen the performance and require indexing of `tm_creation_time` [2], which make sense since *filetransferdb* have over **136M** records on the other hand **tasks** have **5M** records.

Do we required such scanning and grouping by aso_worker of the whole history?
_______
[1] GetGroupedTransferStatistics0_sql
```sql
SQL> SELECT count(*) as count, tm_aso_worker, tm_transfer_state FROM filetransfersdb GROUP BY tm_aso_worker, tm_transfer_state;
8 rows selected.
Elapsed: 00:00:10.97
```
[2] Adding time filtering alone might not fixed and likely required indexing in combination.
```sql
SQL> SELECT count(*) as count, tm_aso_worker, tm_transfer_state FROM filetransfersdb WHERE tm_creation_time > SYSDATE - INTERVAL '2' MONTH GROUP BY tm_aso_worker, tm_transfer_state;
many minutes...went by......no...responses....
```
[3] **GetGroupedTransferStatistics\*\*_sql** queries
https://github.com/dmwm/CRABServer/blob/53ba4e7d7778d2776581e8f52f6f30644df942d9/src/python/Databases/FileTransfersDB/Oracle/FileTransfers/FileTransfers.py#L136-L201

[4] slow responses endpoints
<img width="1481" height="648" alt="Image" src="https://github.com/user-attachments/assets/49e43b4a-5714-417c-a9bd-212752a86e9c" />

## Comment (belforte, 2026-06-04T16:37:42Z)

thanks for the investigation and the details. I need time to think about transfersdb, but am puzzled that a record update takes so long in task table. Worth checking with Kate if we could add an index (on status ?)

hmm.. are those  GetGroupedTransferStatistics queries just for our monitoring ? I am puzzled that simply counting rows can take long ! We surely do not use all of them but it takes some effort to find which ones are used and which are not.

## Comment (nausikt, 2026-06-04T16:44:48Z)

Ahh, forgive me, we did have some indexing on `filetransfersdb` though i still i don't understand why when i added time filtering on `tm_creation_time` make things slower.
```python
        self.create['i_transfers']  = "CREATE INDEX TM_TASKNAME_IDX            ON FILETRANSFERSDB (TM_TASKNAME)"
        self.create['i_workers']    = "CREATE INDEX TM_WORKER_STATE            ON FILETRANSFERSDB (TM_ASO_WORKER, TM_TRANSFER_STATE) COMPRESS 2"
        self.create['i_publishers'] = "CREATE INDEX TM_WORKER_PUB_STATE        ON FILETRANSFERSDB (TM_ASO_WORKER, TM_PUBLICATION_STATE) COMPRESS 2"
        self.create['i_pubtrans']   = "CREATE INDEX FILETRANSFERSDB_NEW2       ON FILETRANSFERSDB (TM_PUBLISH, TM_PUBLICATION_STATE, TM_TRANSFER_STATE) COMPRESS 3"
        self.create['i_creation']   = "CREATE INDEX TM_CREATION_TIME_LOCAL_IDX ON FILETRANSFERSDB (TM_CREATION_TIME) COMPRESS 1"
```

## Comment (nausikt, 2026-06-04T16:46:16Z)

> thanks for the investigation and the details. I need time to think about transfersdb, but am puzzled that a record update takes so long in task table. Worth checking with Kate if we could add an index (on status ?)
> 

Agree, index on status like her suggestion might be a good shot.

## Comment (nausikt, 2026-06-04T16:50:34Z)

> hmm.. are those GetGroupedTransferStatistics queries just for our monitoring ? 

Yes, likely been call by only `aso_metrics_ora.py`.

## Comment (nausikt, 2026-06-04T16:55:40Z)

> I am puzzled that simply counting rows can take long ! 

grouping by 2 fields (aso_worker and their transfer_state) of over 138M records can be very expensive na.

## Comment (belforte, 2026-06-04T19:51:32Z)

> grouping by 2 fields (aso_worker and their transfer_state) of over 138M records can be very expensive na.

ouch !!

## Comment (belforte, 2026-06-04T20:15:07Z)

but we have an index on ` (aso_worker and their transfer_state) ` shouldn't it help ?
Since we have only two values for aso_worker (schedd and rucio), we could make two COUNT w/o aggregation but with a selection. Would that help ? We could add an index on aso_worker.
I think that the current index is meant to help the Publisher when it looks for all files which have a given aso_worker and are in status NEW or ACQUIRED
Are you sure that we are looking at the correct query ? there could be other places where we do a filetransfers GET. Maybe we should change this https://github.com/dmwm/CRABServer/blob/53ba4e7d7778d2776581e8f52f6f30644df942d9/src/script/Monitor/aso_metrics_ora.py#L52
to use a different agent name so we can tell who makes the call
But indeed those GET appear to be every 5 min which is the period of aso_metrics_ora updates :-(

## Comment (nausikt, 2026-06-05T10:13:28Z)

> but we have an index on `(aso_worker and their transfer_state)` shouldn't it help ?

That puzzled me too. but i think i got some clues here.

the TM_WORKER_STATE composite index, (tm_aso_worker, tm_transfer_state) seems to do its job [2.2] if the query are being **selective** _enough_. and don't touch the main **culprit** combination, **_(schedd, 3 (DONE))_** [1,2.1]

Based on that, **GetGroupedTransferStatistics0_sql** [1] looks like the main culprit query because it's the only one who care about DONE state w/o selective clauses.

P.S. Unlike other queries which will have at least e.g. tm_username or the indexed tm_publication_state or non-DONE state over indexed tm_transfer_state as a selective clauses as you mentioned.   

**Conclusion:** any query that touch **_(schedd, 3 (DONE))_** w/o more selective clauses will behave like full-table scans regardless of indexing.

_______
[1] The Distribution is **_extremely skewed_**, leaning toward (schedd, 3 (DONE)) combination ~ **135M** records (***98.32%***)
```sql
COUNT        TM_ASO_WORKER    TM_TRANSFER_STATE
-----------  ----------------  -----------------
135,068,603  schedd            3
1,948,555    schedd            2
291,942      schedd            6
46,684       schedd            0
15,307       schedd            5
5,670        rucio             3
4            NULL              0
1            NULL              6
```
[2] if split query into 2 selection COUNT w/o aggregation.
- 2.1 Dominance part (schedd, 3) ~135M records alone still took 12s equivalent to full-table scans processing time. 
```sql
SQL> SELECT tm_transfer_state, COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' GROUP BY tm_transfer_state;

TM_TRANSFER_STATE   COUNT(*)
----------------- ----------
                6     291942
                2    1948464
                5      16206
                3  135073328
                0      46664

Elapsed: 00:00:12.01
```
2.2 Being selective on only rucio as aso_worker utilize composite index well resulting in an extreme fast scan over this large table. 
```sql
SQL> SELECT tm_transfer_state, COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'rucio' GROUP BY tm_transfer_state;

TM_TRANSFER_STATE   COUNT(*)
----------------- ----------
                3       5670

Elapsed: 00:00:00.01
````
______

### On Publisher side
Both queries [3] and [4] seem selective/specific enough thus may enjoy indexed/partitioned, and most importantly, they don’t touch state = 3 (DONE). So I guess they are less likely to be the culprit.

[3] Acquire Publication (NEW → ACQUIRED)
```sql
    AcquirePublication_sql = "UPDATE filetransfersdb SET tm_last_update = :last_update, \
                                                         tm_publication_state = :new_publication_state, \
                                                         tm_aso_worker = :asoworker \
                              WHERE (tm_aso_worker = :asoworker or tm_aso_worker is NULL) AND \
                                    tm_transfer_state = :transfer_state AND \
                                    tm_publish = :publish_flag AND \
```

[4] Retrieve Acquired Files (ACQUIRED status)
```sql
    GetDocsPublication0_sql = "SELECT f.tm_publication_state, f.tm_transfer_state, f.tm_aso_worker, f.tm_taskname, f.tm_username, \
                                      f.tm_destination, f.tm_source_lfn, f.tm_destination_lfn, \
                                      f.tm_last_update, f.tm_dbs_blockname, f.tm_block_complete,\
                                      t.tm_user_role, t.tm_user_group, \
                                      t.tm_input_dataset, t.tm_cache_url, t.tm_dbs_url \
                                      FROM filetransfersdb f \
                                      LEFT OUTER JOIN tasks t ON t.tm_taskname = f.tm_taskname \
                                      WHERE f.tm_publication_state = :state AND \
                                      f.tm_transfer_state = :transfer_state AND \
                                      f.tm_aso_worker = :asoworker AND rownum < :limit \
                                      ORDER BY rownum"
```
 
> there could be other places where we do a filetransfers GET. Maybe we should change this
> 
https://github.com/dmwm/CRABServer/blob/53ba4e7d7778d2776581e8f52f6f30644df942d9/src/script/Monitor/aso_metrics_ora.py#L52
> 
> 
> to use a different agent name so we can tell who makes the call

Roger that. 🫡


Noted: NEW = state 0, ACQUIRED = state 1

## Comment (nausikt, 2026-06-05T10:58:35Z)

Here's when we explicitly exclude `(schedd, 3 (DONE))` and specifically count with aso_worker=`schedd` separately. 
it will speed the query up from **12s** to **0.3s**.

```sql
SQL> SELECT tm_transfer_state, COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' GROUP BY tm_transfer_state;

TM_TRANSFER_STATE   COUNT(*)
----------------- ----------
                6     291942
                2    1948464
                5      16206
                3  135073328
                0      46664

Elapsed: 00:00:12.01
```

```sql
SQL> SELECT tm_transfer_state, COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state IN (0, 2, 5, 6) GROUP BY tm_transfer_state;

TM_TRANSFER_STATE   COUNT(*)
----------------- ----------
                0      46878
                2    1948469
                5      11155
                6     291942

Elapsed: 00:00:00.31
```

## Comment (belforte, 2026-06-05T13:33:23Z)

so you are saying that counting the DONE takes long because almost all publications are DONE (which is good). OK.

Indeed we do not need to count DONE in the full table (which only has last 3 or 4 months, anyhow, unless something went badly wrong with periodic cleanup or old partitions). We'd need to review the monitoring plots and  check if we drop some, or if that info is plainly unused. At first guess it may only be relevant for [this panel](https://monit-grafana.cern.ch/goto/LOEuyhxvg?orgId=11) which is nice, but we never look at.

Would the counting be  faster if we explicitely select the status instead of grouping on it ?

## Comment (nausikt, 2026-06-05T14:34:12Z)

> Would the counting be faster if we explicitely select the status instead of grouping on it ?

I was wondering too, but your sub queries approach is on par with grouping query above with the same 0.3s for non-DONE state.
```sql
SQL> SELECT COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state = 2;
SQL> SELECT COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state = 0;
SQL> SELECT COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state = 6;
SQL> SELECT COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state = 5;

Elapsed: 00:00:00.23
Elapsed: 00:00:00.01
Elapsed: 00:00:00.01
Elapsed: 00:00:00.02
```

But slight improvement for `state=3`, down from 10~12s to 8.3s
```sql
SQL> SELECT COUNT(*) FROM FILETRANSFERSDB WHERE tm_aso_worker = 'schedd' AND tm_transfer_state = 3;

  COUNT(*)
----------
 135290672

Elapsed: 00:00:08.36
```

## Comment (nausikt, 2026-06-05T14:40:44Z)

So, if we would like to keep counting DONE, it seems we can't go below ***9s***, given the same publishing workloads.

## Comment (belforte, 2026-06-05T15:20:28Z)

It appears that COUNT() is a full table scan.

We could certainly reduce the rate at which we report this in aso_metrics_ora to e.g. once per hour. But one long query every 5 min is not that troubling.  IIUC the only fast way would be to have a separate table with all the DONE records so we just ask for the number of rows. Or we can keep a counter, somehow ? DONE is terminal status, it never gets changed (differently e.g. from FAILED).

But... while this is academically interesting... I am not sure that it is worth pursueing.

Can you check how many partitions we keep ? Maybe we can reduce that number and gain 20 or 30% that way ?

## Comment (nausikt, 2026-06-05T15:41:00Z)

Not sure, i can't look into the partition details neither by `cms_analysis_reqmgr_r` nor `cms_analysis_reqmgr_w`. seems like its own by Kate? with `cms_anaylysis_reqmgr` user account?
```sql
SQL> SELECT owner, table_name, partitioned FROM all_tables WHERE table_name = 'FILETRANSFERSDB';

OWNER       = CMS_ANALYSIS_REQMGR
TABLE_NAME  = FILETRANSFERSDB
PARTITIONED = YES

SQL> SELECT table_name, partition_name, high_value FROM user_tab_partitions WHERE table_name = 'FILETRANSFERSDB' ORDER BY partition_position;

no rows selected
```

## Comment (belforte, 2026-06-05T15:44:42Z)

password for cms_anaylysis_reqmgr is in `crab-secrets/kubernetes/OraclePasswords.sops`

## Comment (nausikt, 2026-06-05T15:52:57Z)

interesting, It was partitioned monthly, up to 5 months. lets me figure out how to keep less.
```sql
SQL> SELECT table_name, partition_name, high_value FROM user_tab_partitions WHERE table_name = 'FILETRANSFERSDB' ORDER BY partition_position;
TABLE_NAME                 PARTITION_NAME        HIGH_VALUE
-------------------------  --------------------  ----------------------------------------
FILETRANSFERSDB            SYS_P544189           TIMESTAMP' 2026-03-01 00:00:00'
FILETRANSFERSDB            SYS_P544918           TIMESTAMP' 2026-04-01 00:00:00'
FILETRANSFERSDB            SYS_P545823           TIMESTAMP' 2026-05-01 00:00:00'
FILETRANSFERSDB            SYS_P547127           TIMESTAMP' 2026-06-01 00:00:00'
FILETRANSFERSDB            SYS_P548191           TIMESTAMP' 2026-07-01 00:00:00'
```

## Comment (nausikt, 2026-06-05T15:55:37Z)

seems like we don't have scheduled job that drops partitions older than 2–3 months? and we manually drop by database admin in the past?

## Comment (nausikt, 2026-06-05T15:58:11Z)

Forgive me, there is partition policy mentioned in crab doc [here](https://cmscrab.docs.cern.ch/crab-components/crab-rest/database-admin.html#change-the-current-policies)

## Comment (belforte, 2026-06-05T16:03:10Z)

so we have current partition ( 1June yo 1 July) plus last 3. Could cut to last 2 and save 25~30% depending on how much is in current partition ... nothing dramatic.

Unless there is a simple way to increment a counter every time we set a row to DONE and simply retrieve that counter, I'd say that we can't do anything. Do you want to ask Kate ?

## Comment (belforte, 2026-06-05T16:05:20Z)

Maybe keeping only last 2 is good anyhow for all tables. I can't see a reason to look at those data for tasks which we purged.

## Comment (nausikt, 2026-06-05T16:07:33Z)

We seems to have scheduled job to drop partitions on monthly-basis. though i've no confident on how its work yet.

[1] `etc/oracle-admin/partitions.sql`, [doc](https://cmscrab.docs.cern.ch/crab-components/crab-rest/database-admin.html#install-the-plsql-code-from-scratch)
```sql
  DBMS_SCHEDULER.CREATE_JOB (
   job_name           =>  'JOB_DEL_PART_FILETRANSFERSDB',
   job_type           =>  'STORED_PROCEDURE',
   job_action         =>  'DEL_PART_FILETRANSFERSDB',
   start_date         =>  '26-MAY-21 11.00.00 AM',
   repeat_interval    =>  'FREQ=MONTHLY',
   comments           =>  'This job will execute DEL_PART_FILETRANSFERSDB procedure and remove oldest partition of FILETRANSFERSDB table,selected by DELETE_PARTITION_MAIN procedure.',
   enabled            =>  TRUE);
```

## Comment (nausikt, 2026-06-05T16:16:16Z)

> Unless there is a simple way to increment a counter every time we set a row to DONE and simply retrieve that counter, I'd say that we can't do anything. Do you want to ask Kate ?

Agree nothing we can do, unless asking Kate. 

but i would rather try bring back / verify periodically drop partitions mechanism to no longer than 2 months.

The procedure (DEL_PART_FILETRANSFERSDB) seems to be there but some how its no longer triggered this recent months, which caused partitions to accumulated and response time rised from 7....10....12s? or could it possibly be OracleDB upgrade intervention recently interrupted the mechanism somehow? let me investigate...

## Comment (belforte, 2026-06-05T16:35:52Z)

AFAIU the procedure runs every months and deletes the oldest partition. If we want to reduce how many we keep I suspect we need to be bold and drop manually one partition. Same procedure runs on preprod DB which should be a good place to practice !

Would you like to talk to Kate about how to replace COUNT(*)   ? Or do you want me to do it ? You certainly know more than I do about SQL, so it may be a good thing for you to get to know Kate.

## Comment (belforte, 2026-06-05T16:41:44Z)

AFAIK keeping last 3 months is current design. I was afraid that some partition drop did not run/work and we accumulated more, but with current situation I have no idea why time to count did increase. Maybe we somehow published more. Maybe it is the effect of beginning of month vs. end of month ?

## Comment (belforte, 2026-06-05T16:42:48Z)

For sure Oracle intervention by Oracle admins are safe. Those people are very good professionals.

## Comment (belforte, 2026-06-05T16:45:50Z)

by the way, IIUC you found that the bad query is on `transfer_state`, not `publication_state`.

## Comment (nausikt, 2026-06-05T16:50:12Z)

Ahhh I see, that make sense, thanks for the summary. Roger that!

> Would you like to talk to Kate about how to replace COUNT(*)   ? Or do you want me to do it ? You certainly know more than I do about SQL, so it may be a good thing for you to get to know Kate.

O.K. let me reach out to her next week, though i've ask ChatGPT for fancy tricks in Oracle DB e.g. Materialized View to stored aggregated queries in another views, but have very low confident that it will fit our use cases perfectly.

"Published more" sounds likely to me na, but have to wait and see whether its expected phenomenon at the end of data-taking.

Yes, for GET transferdb `transfer_state`, but for POST transferdb `publication_state` also another suspicious culprit one responsible for their 3s slow mutate/update operation.

## Comment (belforte, 2026-06-05T16:57:51Z)

I asked Claude for suggestions, here it is. Shall we start with an index ?

<html><head></head><body><p>Yes, there are several good approaches. Let me walk through them from best to most complex:</p>
<h2>1. Filtered Index (Quickest Win)</h2>
<p>If you're frequently querying a specific value like <code>'DONE'</code>, a filtered/function-based index can make the COUNT near-instant:</p>
<pre><code class="language-sql">-- Oracle: standard index on the column
CREATE INDEX idx_myvar ON mytable (MyVar);

-- Then your COUNT uses the index instead of scanning the table
SELECT COUNT(*) FROM mytable WHERE MyVar = 'DONE';
</code></pre>
<p>Oracle can do an <strong>index range scan</strong> and count index entries without touching the table at all. This alone often reduces query time from minutes to milliseconds.</p>
<hr>
<h2>2. Materialized View (Best Balance)</h2>
<p>A materialized view pre-computes the grouped counts and can <strong>refresh automatically</strong>:</p>
<pre><code class="language-sql">CREATE MATERIALIZED VIEW mv_myvar_counts
REFRESH FAST ON COMMIT  -- auto-refreshes on every COMMIT
AS
SELECT MyVar, COUNT(*) AS cnt
FROM mytable
GROUP BY MyVar;

-- Your query then hits the tiny MV instead of millions of rows:
SELECT cnt FROM mv_myvar_counts WHERE MyVar = 'DONE';
</code></pre>
<p><strong>Requirements for FAST refresh:</strong> you need a materialized view log on the base table:</p>
<pre><code class="language-sql">CREATE MATERIALIZED VIEW LOG ON mytable
WITH ROWID, SEQUENCE (MyVar)
INCLUDING NEW VALUES;
</code></pre>
<p>This is the most <strong>Oracle-idiomatic</strong> solution and avoids any application-layer changes.</p>
<hr>
<h2>3. Counter Table with Triggers (Your Idea)</h2>
<p>Yes, your idea works — and it's a classic pattern. You maintain a summary table and fire a trigger on updates:</p>
<pre><code class="language-sql">-- Summary table
CREATE TABLE myvar_counts (
    myvar_value VARCHAR2(50) PRIMARY KEY,
    cnt         NUMBER DEFAULT 0
);

-- Trigger on the main table
CREATE OR REPLACE TRIGGER trg_myvar_count
AFTER UPDATE OF MyVar ON mytable
FOR EACH ROW
BEGIN
    -- Decrement old value
    IF :OLD.MyVar IS NOT NULL THEN
        UPDATE myvar_counts SET cnt = cnt - 1
        WHERE myvar_value = :OLD.MyVar;
    END IF;
    -- Increment new value
    IF :NEW.MyVar IS NOT NULL THEN
        UPDATE myvar_counts SET cnt = cnt + 1
        WHERE myvar_value = :NEW.MyVar;
    END IF;
END;
</code></pre>
<p>⚠️ <strong>Caveats with this approach:</strong></p>
<ul>
<li>Triggers fire row-by-row, so <strong>bulk updates are slow</strong> (e.g. <code>UPDATE mytable SET MyVar='DONE' WHERE ...</code> affecting 100k rows = 100k trigger fires)</li>
<li>Counter table can become a <strong>hot block</strong> contention point under high concurrency</li>
<li>You need INSERT/DELETE triggers too to keep counts accurate</li>
</ul>
<hr>
<h2>4. Approximate Count (Oracle 12c+)</h2>
<p>If you just need a fast <em>estimate</em>, Oracle has:</p>
<pre><code class="language-sql">SELECT APPROX_COUNT_DISTINCT(MyVar) FROM mytable;
-- or
SELECT MyVar, APPROX_COUNT(*) ... -- via SQL Tuning Advisor hints
</code></pre>
<hr>
<h2>Recommendation</h2>

Scenario | Best Approach
-- | --
Read-heavy, rare writes | Materialized View
Just need fast WHERE = 'X' | Index on MyVar (try this first)
App controls all writes | Counter table + trigger
Estimate is acceptable | APPROX_COUNT


<p><strong>Start with the index</strong> — it requires zero application changes and often solves the problem entirely. If you need the full <code>GROUP BY</code> across all values to be fast, add the <strong>Materialized View</strong> on top.</p></body></html>

## Comment (nausikt, 2026-06-05T17:02:04Z)

Ahhh, Looks good to me.

I didn't noticed that Materialized View can auto-refreshes on every COMMIT like that. At first, i thought that we need to enable scheduled-job something.

O.K. let me try this sequence before consulting with Kate.

## Comment (nausikt, 2026-06-05T17:04:25Z)

but will that refreshes on every COMMIT torture the db more? 

P.S. O.K. the recommendation state quite clear, it may not suit our use cases which we write very frequently.

## Comment (belforte, 2026-06-05T17:08:14Z)

I have not understood the materialized view thing  :white_flag:

## Comment (belforte, 2026-06-05T17:11:42Z)

I was simplifying the question for Claude, we have two variables (worker and state), and already an index on that...  I guess that we need to give Claude the full info if we want help. Maybe better ask Kate !

## Comment (nausikt, 2026-06-05T17:14:47Z)

Yes, we already have composite indexes there and introducing standalone index of `tm_transfer_state` will not be helpful.

## Comment (belforte, 2026-06-05T19:55:51Z)

let's fix the query on task table in the meanwhile, to signal Kate that we are doing our best ;-)
I will not be working until Tuesday.

## Comment (nausikt, 2026-06-05T20:02:22Z)

Cool, i'm doing it now. please feel free to approve in advance if you might not be around.

## Comment (cmsdmwmbot, 2026-06-05T20:12:43Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 231 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2829/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-06T13:57:46Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 231 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2830/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-06T14:05:48Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 2 warnings
   * 46 comments to review
 * Pycodestyle check: succeeded
   * 231 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2831/artifact/artifacts/PullRequestReport.html

## Comment (oljemark, 2026-06-07T11:30:23Z)

Hello, everyone. Based on the pylint unused-variable warning reported above: Is the post method, here (https://github.com/oljemark/CRABServer/commit/6be9b3f453c371ef42a74c1a5c176a5beea05154) still in use? I saw the specific resubmittedjobs keyword was already removed in 2021, and I see no other instances of resubmitted_jobs that are not pandas_resubmitted_jobs, under the obsolete/ folder. The only usage of this keyword I see is for task monitoring in CRAB2, in 2013.

## Comment (nausikt, 2026-06-08T08:12:48Z)

Thank you so much @oljemark! for your active participating so far.

Agree, would you be happy to open a PR for these too? otherwise i'll probably include in the next PR.

## Comment (belforte, 2026-06-09T08:58:19Z)

POST is used, but the param `resubmittedjobs` is indeed obsolete and can be cleaned up. Thanks for catching this.
