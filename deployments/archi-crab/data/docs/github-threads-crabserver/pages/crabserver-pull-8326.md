# dmwm/CRABServer pull request #8326: Oracle - many new things cumulated over many months

State: closed
Opened: 2024-04-09T15:11:10Z
Closed: 2024-04-29T14:46:33Z
Merged: 2024-04-29T14:46:33Z
URL: https://github.com/dmwm/CRABServer/pull/8326

## Opening post (mapellidario, 2024-04-09T15:11:10Z)

fixes #7154 
fixes #6472 
fixes #5632
fixes #7458 

### description

This PR adds some things related to the oracle DB management:

- [x] Adjust Create.py so that they create partitioned tables, tested
- [x] Adjust Create.py so that they create proper indexes, same as production, tested
- [x] added partitions.sql that contains all the procedures, functions and scheduled jobs for dropping old partitions. tested.

Together with all the information at [1] this should be enough to take care of the DB for the years to come :)

This PR supersedes all the information that is contained in obsolete and archived repositories in gitlab [2].

---

[1]

- https://cmscrab.docs.cern.ch/technical/crab-rest/database-admin.html
- https://cmscrab.docs.cern.ch/technical/crab-rest/database.html

[2] https://gitlab.cern.ch/groups/crab3/-/archived

## Comment (cmsdmwmbot, 2024-04-09T15:14:40Z)

Jenkins results:
 * Python3 Pylint check: succeeded
   * 3 warnings
   * 5 comments to review
 * Pycodestyle check: succeeded
   * 13 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/1929/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2024-04-17T22:18:37Z)

@mapellidario I haven't reviewed the documentation yet, but you can still merge this

## Comment (belforte, 2024-04-17T22:21:15Z)

about documentation at the top of https://cmscrab.docs.cern.ch/technical/crab-rest/database.html#crab-database-developer
I do not understand
```
We use Oracle Database to store the task state. With the current policy: we store data for only 30 days.

It is possible to ask DBA to roll back our schemas to any point in time within the last six months. But it will spawn a new schema instead of reverting to the current one.
```
we do not loose data from DB after 30 days. And last line sort of makes no sense. "rolling back" is not "reverting to the current one"

## Comment (belforte, 2024-04-17T22:23:04Z)

https://cmscrab.docs.cern.ch/technical/crab-rest/database-faqs.html#database-faqs

what is " kill it through WebUI." ?

## Comment (mapellidario, 2024-04-29T14:42:29Z)

> about documentation at the top of https://cmscrab.docs.cern.ch/technical/crab-rest/database.html#crab-database-developer I do not understand
> 
> ```
> We use Oracle Database to store the task state. With the current policy: we store data for only 30 days.
> 
> It is possible to ask DBA to roll back our schemas to any point in time within the last six months. But it will spawn a new schema instead of reverting to the current one.
> ```
> 
> we do not loose data from DB after 30 days. And last line sort of makes no sense. "rolling back" is not "reverting to the current one"

I did not write that page. However it should be a bit more clear now.

## Comment (mapellidario, 2024-04-29T14:44:06Z)

> https://cmscrab.docs.cern.ch/technical/crab-rest/database-faqs.html#database-faqs
> 
> what is " kill it through WebUI." ?

I did not write that page. However, I think it means that from the "sessionmanager web ui" that is mentioned in the sentence before. I updated that sentence and should be a bit more clear now

## Comment (mapellidario, 2024-04-29T14:44:54Z)

Thanks Stefano for the review, I will merge this PR

## Comment (belforte, 2024-04-29T14:52:22Z)

very good, thanks
