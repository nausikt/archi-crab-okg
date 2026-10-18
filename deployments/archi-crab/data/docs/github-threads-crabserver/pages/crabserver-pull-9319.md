# dmwm/CRABServer pull request #9319: Use RRN and Exitcodes to overhaul resubmission and retry policy

State: closed
Opened: 2026-06-01T06:56:11Z
Closed: 2026-06-15T09:58:50Z
Merged: 2026-06-15T09:58:50Z
URL: https://github.com/dmwm/CRABServer/pull/9319

## Opening post (aspiringmind-code, 2026-06-01T06:56:11Z)

Fix #9318 
For larger discussion on how we reached here, see #9264 and (few last comments in) #9276 

---

## Design Write-Up: CRABServer Resubmission Policy Refactor

---

This PR introduces three interlocking concepts:

1. **RRN (Resubmission Retry Number)** : a new, independent, per-job counter that counts genuine job execution attempts across all resubmission epochs.
2. **EXIT_RETRY_POLICY** : a declarative dictionary in `RetryJob.py` that maps exit codes to retry actions (delay, memory boost, runtime boost, site change).
3. **`resubmit_record.json` and epoch tracking** : a mechanism to allow user-triggered resubmissions to reset RRN counters for targeted jobs, enabling a clean slate while preserving history. Note that epoch is a counter, not time.

---

### The Three Counters: `dag_retry`, `crab_retry`, and `rrn`

Understanding the difference between these is essential.

| Counter | Owned By | What It Counts | Resets? | Stored In |
|---|---|---|---|---|
| `dag_retry` (`$RETRY`) | DAGMan | DAGMan node submission attempts (pre+job+post cycle) within current DAG run | **Never** | DAGMan internal state |
| `crab_retry` | CRAB PostJob | Number of times PostJob has completed (job ran + postjob ran) | **Never** | `retry_info/job.<id>.txt` |
| `rrn` | CRAB PreJob/AdjustSites | True number of execution attempts (auto + user-triggered) | Only on user resubmit | `rrn_info/job.<id>.txt` |

`crab_retry` is used as a key/index into `resubmit_info/job.<id>.txt` to store per-attempt parameters (memory, runtime, site lists, exit code info). It is strictly increasing and never resets, it serves as a stable record key.

`rrn` is used exclusively to answer: "Has this job been tried enough times overall?" It resets to 0 when the user explicitly resubmits, giving the job a fresh budget of `CRAB_NumAutomJobRetries` (now **10**, up from 2) attempts. PreJob stamps `CRAB_RRN` into the job's classAd so PostJob can read it without touching the filesystem.

`dag_retry` still controls the DAGMan machinery, but PostJob no longer uses it as the gate for "too many retries" , it uses `rrn` instead.

---

### The Lifecycle of a Single Job Attempt

**Step 1 — PreJob runs:**
- Calls `get_rrn()`: reads `rrn_info/job.<id>.txt`, increments the `rrn` field, writes it back (atomic rename, file-locked).
- Stamps `My.CRAB_RRN = <rrn>` into the job submit classAd.
- Reads `resubmit_info/job.<id>.txt` at key `crab_retry - 1` (the previous attempt's data).
  - If `increase_memory` is set, multiplies current memory by `memory_factor` (capped at 7500 MB).
  - If `increase_runtime` is set, multiplies current walltime by `runtime_factor` (capped at 47 h).
- Reads `change_site` from the previous attempt. If set, and there is more than one available site, removes the previous failing site from the candidate set.
- Checks `retry_delay_until` from `resubmit_info` for the current `dag_retry` key. If now < that timestamp, returns True from `needsDefer()` and the job is deferred (held and re-released after the delay).
- Writes the chosen parameters into `resubmit_info/job.<id>.txt` at key `str(crab_retry)`.

**Step 2 — Job runs on the worker node.**

**Step 3 — RetryJob runs (if the job finished with non-zero exit code):**
- Calls `apply_retry_policy(exitCode)`.
- Looks up `exitCode` in `EXIT_RETRY_POLICY`. Falls back to `"default"` (neutral, no adjustments) if not found.
- Calls `store_retry_actions(policy, exitCode)`: writes into `resubmit_info/job.<id>.txt` at key `str(crab_retry)`:
  - `retry_delay_until = time.time() + policy["delay"]` (typically 900 s)
  - `increase_memory`, `increase_runtime`, `change_site` booleans and their factors
  - `site` = the site where this attempt ran (so PreJob can discard it next time if needed)
  - `exitCode`
- If the policy type is `"recoverable"`, dispatches to a handler (if registered), then raises `RecoverableError`.
- If the policy type is `"neutral"`, returns without raising, falls through to the existing `FatalError` raise at the bottom of `check_exit_code`.

**Step 4 — PostJob runs:**
- Calls `get_rrn()`: reads `CRAB_RRN` from the job classAd (stamped by PreJob). Falls back to `rrn_info/job.<id>.txt` if classAd unavailable (e.g., PreJob itself crashed before the job ran).
- Calls `get_max_retry()`: reads `CRAB_NumAutomJobRetries` from the task classAd (default 10).
- If `retryjob_retval == RECOVERABLE_ERROR`: checks `rrn >= max_retry`. If yes → fatal. Otherwise → recoverable (DAGMan will retry).

---

### The EXIT_RETRY_POLICY Dictionary

The old `RetryJob.py` had a linear `if/elif` chain. The new code replaces it with a data-driven dictionary:

```python
EXIT_RETRY_POLICY = {
    1:     {"type": "recoverable", "delay": 900, "msg": "...bootstrap failure..."},
    50115: {"type": "recoverable", "delay": 900, "msg": "..no FJR..", "increase_memory": True, "memory_factor": 1.3},
    195:   {"type": "recoverable", "delay": 900, "msg": "..no FJR..", "increase_memory": True, "memory_factor": 1.3},
    60403: {"type": "recoverable", "delay": 900, "msg": "..stageout timeout..", "increase_runtime": True, "runtime_factor": 1.3},
    243:   {"type": "recoverable", "delay": 900, "msg": "..stageout timeout..", "increase_runtime": True, "runtime_factor": 1.3},
    8020:  {"type": "recoverable", "delay": 900, "msg": "..FileOpenError..", "change_site": True, "handler": "handle_file_open_or_root_error"},
    8021:  {"type": "recoverable", "delay": 900, "msg": "..FileReadError..", "change_site": True, "handler": "handle_file_open_or_root_error"},
    ...
    "default": {"type": "neutral", "delay": 900, "msg": "..."}
}
```

Key additions:
- `increase_memory` / `memory_factor`: triggers a 1.3× memory increase on the *next* attempt.
- `increase_runtime` / `runtime_factor`: triggers a 1.3× walltime increase on the *next* attempt.
- `change_site`: triggers removal of the failing site from the candidate set on the *next* attempt.
- `handler`: name of a method on `RetryJob` to call before raising `RecoverableError` (for exit-code-specific logic like checking corrupted files or CVMFS issues).
- `"neutral"` type: the exit code is not recognized as explicitly recoverable; falls through to the existing fatal-error path rather than either retrying blindly or failing definitively.

The three handler methods (`handle_file_open_or_root_error`, `handle_sigabrt`, `handle_cvmfs_or_cms_exception`) contain the same logic as the old inline `if` blocks, they are just extracted into named methods and dispatched via the policy table.

---

### User-Triggered Resubmission and RRN Reset

When a user calls `crab resubmit`, `DagmanResubmitter.py` runs. The new code adds:

```python
newEpoch = currentEpoch + 1
resubmitRecord = json.dumps({
    'epoch': newEpoch,
    'job_ids': task['resubmit_jobids']  
})
schedd.edit(rootConst, "CRAB_ResubmitEpoch", str(newEpoch))
schedd.edit(rootConst, "CRAB_ResubmitRecord", classad.quote(resubmitRecord))
```

Both `epoch` and `job_ids` are written atomically as a single JSON classAd value (`CRAB_ResubmitRecord`). This prevents AdjustSites from ever seeing a mismatched (new epoch, old job list) pair.

When DAGMan restarts and `AdjustSites.py` runs:
1. `writeResubmitRecord(ad)` reads `CRAB_ResubmitRecord` from the task classAd and writes it to `rrn_info/resubmit_record.json`. Idempotent: skips if the on-disk epoch already matches.
2. `resetRRN()` reads `rrn_info/resubmit_record.json`. For each targeted job (or all jobs if `job_ids` is null), opens `rrn_info/job.<id>.txt`, checks `last_reset_epoch`. If `last_reset_epoch < current_epoch`, sets `rrn = 0`. If `last_reset_epoch >= current_epoch`, we skip with continue. This idempotency in == means DAGMan can restart AdjustSites multiple times safely. The > case should not happen until things have gone very wrong.

After this reset, when PreJob runs for a resubmitted job, `get_rrn()` finds `rrn = 0` and increments it to 1, effectively giving the job a new budget of `max_retry` attempts.

### `reuse_rrn`: Handling Interrupted PreJob

There is a subtle race condition: PreJob can crash or be killed after incrementing RRN but before the job actually runs. This also happens when a resubmission of a different job id happens while another is running. When DAGMan retries the node, PreJob runs again. At this point:
- `retry_info` shows `pre > post` (PreJob ran more times than PostJob)
- `job_out.<id>.<retry>` does not exist (job never ran)

Originally, this case set `prejob_exit_code = 1` (error) only if a job_out existed, implying the job had run. In the new code an `else` branch is added: when `pre > post` and no `job_out`, it sets `self.reuse_rrn = True`. Then `get_rrn()`, instead of incrementing, just returns the current `rrn` value unchanged. This prevents RRN from being double-incremented for a single logical job attempt where PreJob happened to restart.

---

### Summary of Key Changes

| Aspect | Existing | New |
|---|---|---|
| Retry gate counter | `dag_retry` (DAGMan internal) | `rrn` (CRAB-owned, per job) |
| Default max retries | 2 | 10 |
| Max retries storage | `$MAX_RETRIES` baked into DAG | `CRAB_NumAutomJobRetries` in task classAd |
| Exit-code handling | `if/elif` chain in `RetryJob` | Declarative `EXIT_RETRY_POLICY` dict |
| Memory auto-boost | Not present | 1.3× on exit 50115/195, capped 7500 MB |
| Runtime auto-boost | Not present | 1.3× on exit 60403/243, capped 47 h |
| Site change on failure | Not present | Discard failing site on exit 8020/8021 |
| Retry delay enforcement | Not present | `retry_delay_until` checked in PreJob |
| User resubmit resets budget | `adjustMaxRetries` increased max_retries by 1 + numAutomJobRetries  | Explicitly via RRN reset + epoch mechanism |
| Idempotent resubmit record | N/A | Yes, `last_reset_epoch` per job |
| Interrupted PreJob | Exit code 1 if job_out exists | `reuse_rrn=True` — no double-increment |

## Comment (cmsdmwmbot, 2026-06-01T07:01:31Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 155 comments to review
 * Pycodestyle check: succeeded
   * 580 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2826/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-01T07:18:37Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 155 comments to review
 * Pycodestyle check: succeeded
   * 584 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2827/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-05T09:55:33Z)

Please add in the top description what RRN stands for. Also a note in the code may help !

## Comment (aspiringmind-code, 2026-06-05T12:22:27Z)

> I believe that it would be important to write down somewhere the "design", and avoid that the reader has to reconstruct it by reading and testing the code as we had to do with current one. New code surely is elegantly written and clear, but the overall interplay of DagmanResubmitter, AdjustSites, and Post/Pre/RetryJob deserves some text.

I have added the design write up at the top

## Comment (belforte, 2026-06-05T13:05:29Z)

WOW, your have been amazingly fast in adding an extensive documentation !!! I am afraid I will not be as fast in digesting !

## Comment (belforte, 2026-06-11T14:18:48Z)

Hi @aspiringmind-code  ! I have finally made it to digest the new documentation and read all code. It all looks fine to me. Just let me recap here all my suggestions (very few !):
1. add a comment at AdustSites.py:228 , see above
2. when something that "should never happen" happens, better to exit with error
3. should use JSON format for the various info files and get rid of ast_literal_eval
4. I think that the way PreJob exits with status 1 when "Post did not run" is flawed, but this pre-dates your changes. So let's leave it at is, but do not emulate in future code if any ! 

Thanks for this,
now we need to plan how to introduce this in production !

## Comment (cmsdmwmbot, 2026-06-15T09:22:54Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 155 comments to review
 * Pycodestyle check: succeeded
   * 584 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2835/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2026-06-15T10:00:00Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 155 comments to review
 * Pycodestyle check: succeeded
   * 586 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2836/artifact/artifacts/PullRequestReport.html
