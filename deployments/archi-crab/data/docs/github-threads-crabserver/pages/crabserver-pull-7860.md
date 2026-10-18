# dmwm/CRABServer pull request #7860: Attach Rucio's replication rule to Publish Container

State: closed
Opened: 2023-08-30T18:55:12Z
Closed: 2023-09-05T09:17:50Z
Merged: 2023-09-05T09:17:50Z
URL: https://github.com/dmwm/CRABServer/pull/7860

## Opening post (novicecpp, 2023-08-30T18:55:12Z)

Now we have 2 rules, one is locking Transfer Container where contains all files that want to transfer to destination, another one is locking Publish Container where contains only EDM files that need to publish to DBS.

Move `add_replication_rule()` to `checkOrCreateContainer()` and make `checkOrCreateContainer()` return rule ID, so we can reuse this method to create both Transfer/Publish container.

## Comment (cmsdmwmbot, 2023-08-30T19:00:57Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 24 warnings and errors that must be fixed
   * 2 comments to review
 * Pycodestyle check: succeeded
   * 22 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1685/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-08-31T07:14:57Z)

should the rule on the transfer container have an expiration date ? Even if we plan to remove it later... things can happen.

## Comment (novicecpp, 2023-08-31T09:10:02Z)

For me, no. I rather leave it to users decision. Avoid "I want to keep it forever but I forgot to extend the rule. Now my files are gone." to happen. Also scrape early idea that we want to let user specify how long the rule keep locking,  replace by tools or some tutorial to interact with the rule directly.

On Aug 31, 2023 09:15, Stefano Belforte ***@***.***> wrote:

should the rule on the transfer container have an expiration date ? Even if we plan to remove it later... things can happen.

—
Reply to this email directly, view it on GitHub<https://github.com/dmwm/CRABServer/pull/7860#issuecomment-1700490617>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AAR45KAEEJURDIDIDWMUR4LXYA2XXANCNFSM6AAAAAA4E6SDOU>.
You are receiving this because you authored the thread.Message ID: ***@***.***>

## Comment (novicecpp, 2023-09-04T18:26:59Z)

We definitely need 2 rules for each container, so I will merge this to this to master. 
Then, we can have discussion about length of the rules in separate issue.

@belforte (User) Documentation is in progress. First draft will be ready on this Wednesday.

## Comment (belforte, 2023-09-05T08:32:34Z)

OK. Go ahead and merge
