# dmwm/CRABServer issue #7513: Disaster recovery - documentation

State: closed
Opened: 2023-01-27T16:02:58Z
Closed: 2024-10-31T16:12:33Z
Labels: Priority: Medium, Status: In Progress, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/7513

## Opening post (novicecpp, 2023-01-27T16:02:58Z)

RFC for [CRAB Disaster Recovery and Backup](https://cmscrab.docs.cern.ch/technical/crab-disaster-recovery-and-backup.html) documentation.

Feel free to put your comment here or edit [crab-disaster-recovery-and-backup.md](https://gitlab.cern.ch/crab3/cms-crab-docs/-/blob/d7a04c56cb0bb92391449d360e3629455abd4164/docs/technical/crab-disaster-recovery-and-backup.md) directly.

@belforte @mapellidario @KatyEllis please review.

## Comment (belforte, 2023-01-28T18:17:22Z)

comments:

1. I think that this should be removed, it may be intersesting to have in the general CRAB REST setup documentatio, but it does not help disaster recover
```
It is possible to ask DBA to roll back our schemas to any point in time within the last six months. But it will spawn a new schema instead of reverting to the current one.
```
2. files in S3 are removed automatically, I will change this line.
```
We never clean up, but it is bound to the lifetime of the task.
```
3. I checked our S3 documentation and found that the current automatic expiration policy is not documented, nor it is documented how to check it. We need to fix this and document how to (re)created the S3 containers.
4. Losing one Schedd should be better described. If we loose VM but CEPH volumes are saved, we can recreate VM and connect same volumes, tasks will be automatically restarted. If we loose one or both volumes, we loose everything

Do you need help with the Runbook for recovery ? I think we should write separate recovery procedure "from scratch" for each component. Also make sure we include things like openstack keys for crab-secretes. More than a disaster here, if Dario leaves CMS we need new S3 tokens.

## Comment (belforte, 2023-01-28T21:14:32Z)

answering my concern in 3. above, for lack of a better place I dump here this:
```bash
belforte@lxplus8s15/~> s3cmd getlifecycle s3://crabcache_prod
<?xml version="1.0" ?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
	<Rule>
		<ID>p845g9ez7o36wijg25vg5div2pfj8eshm6srktlfa0qy6b4u</ID>
		<Prefix/>
		<Status>Enabled</Status>
		<Expiration>
			<Days>33</Days>
		</Expiration>
	</Rule>
</LifecycleConfiguration>
```
I made `s3md` work by following blindly instructions in https://clouddocs.web.cern.ch/object_store/s3cmd.html

**N.B.** the Openstack project name is `"CMS CRAB"`

## Comment (mapellidario, 2023-01-30T13:12:02Z)

The only suggestion I have is that we can actually backup the github issues and pull requests to gitlab [1].

I have never done anything similar so I can not estimate how long it takes (~1h? ~1d?), but it does not seem too complicated. The only thing we need to be aware is that if we want the authors of the issues/pullrequests to be consistent, we need to add to our profile in gitlab.cern.ch the email that we use in github, as the gitlab docs mentions it:

> Before you begin, ensure that any GitHub user you want to map to a GitLab user has a GitLab email address that matches their [publicly visible email address](https://docs.github.com/en/rest/users#get-a-user) on GitHub. 

This webpage explains it a bit better [2], it should be enough to browse to [3] and add there our github email address. We may also want to contact Diego before starting the import.

[1] https://docs.gitlab.com/ee/user/project/import/github.html#import-your-github-repository-into-gitlab
[2] https://jsramblings.com/keep-authors-when-importing-from-github-to-gitlab/
[3] https://gitlab.cern.ch/-/profile/emails

## Comment (mapellidario, 2023-01-30T13:15:12Z)

>  I think we should write separate recovery procedure "from scratch" for each component

I agree. I suggest that we write a specific page "Install from scratch" for each component inside its directory. For example, I would place the REST "install from scratch" here [1].

Then either at the end of the Disaster recovery page that Wa created or in another new page, we link all the "install from scratch" pages. This is to avoid some repetitions among the "disaster recovery" pages and the "usual documentation about each component" ones.

[1]: https://gitlab.cern.ch/crab3/cms-crab-docs/-/tree/master/docs/technical/crab-rest

## Comment (belforte, 2023-01-30T14:09:27Z)

> The only suggestion I have is that we can actually backup the github issues and pull requests to gitlab [1].

CMSSW is using this already. So in case we can get instructions from e.g. Shahzad. Yet I am not sure that it is needed. In any case it would be better to have a CMS-wide (or at least O&Cwide solution), there are many GH backup tools around

## Comment (mapellidario, 2023-01-30T14:17:16Z)

CMSSW is backing up code, not issues or PRs [1]. Or are they using a different repo for the issues?

[1] https://gitlab.cern.ch/cms-sw/cmssw/-/issues

## Comment (belforte, 2023-01-30T14:23:38Z)

I see. thanks Dario. But let's move to a different place the discussion on GH backup. Does not belong to this document. At this moment we have no backup and can only recover code from local clones.

## Comment (novicecpp, 2023-02-01T13:55:14Z)

Thanks for comment! I fixed the docs as Stefano suggested.
I agree to change runbook to "install from scratch" and put it on the component docs.

Lets me list things I need to do:
- [x] Sync issue from GH (open new issue)
- [ ] "Install from scratch" section for each crab component (open new issue)
- [ ] Add more info each component to answer these questions:
  - What is it?
  - How code/data are managed?
  - What happen if we lose all data?
  - Backup procedure?
  - Support contact?

## Comment (novicecpp, 2024-10-31T16:12:33Z)

Here is the [disaster recovery docs](https://cmscrab.docs.cern.ch/crab-disaster-recovery-and-backup.html) but we still lack the "Install from scratch". 

I am closing the issue for now, feel free to reopen it later.
