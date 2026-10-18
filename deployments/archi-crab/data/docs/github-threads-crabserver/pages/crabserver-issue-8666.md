# dmwm/CRABServer issue #8666: refactor crab-doc

State: closed
Opened: 2024-08-28T16:00:30Z
Closed: 2024-09-10T14:17:31Z
Labels: Type: Documentation, Status: In Progress
URL: https://github.com/dmwm/CRABServer/issues/8666

## Opening post (belforte, 2024-08-28T16:00:30Z)

In Udine we agreed to refactor the crab-doc MD documentation along the following scheme

![image](https://github.com/user-attachments/assets/a8f579b1-e691-4c04-9466-df6e10c46d68)

![image](https://github.com/user-attachments/assets/66c6892c-690f-4e81-a610-20f0093cffa7)

text version, for copy/paste
```text
Proposed index layout 
Day1
Operations
Development environment
Inventory (Accounts, machines, storage)
CRAB design
CRAB Components
CRAB internal Infrastructure
Past incidents
How to mainain this document (better title needed)
Bits and pieces (miscellanea)


EXAMPLE
Day1
What to read, what to do, egroups, mail list, mm channels, cric/voms
New DevOp training: what to read, tutorials to do, CERN courses… Orientation in CMS O&C world (Organization, IAM, CRIC, DBS, Rucio, WMA, DQM, cmsweb..)
Operations  / For operators
Duties, what to look for, how to react to (known) problems, troublushoot user errors
Development environment / For Developers
How to setup, how to use, best practices… Setup of lxplus, laptop, git branches, pr’s, connect to Judy from outside - how to run things in debug mode
Inventory (Accounts, machines, storage)
What we have now but try to point to where info if as much as possible rather then have lists to maintain
CRAB design
Description of how things work, add here also the more detailed things about e.g. S3 or ASO-Rucio
CRAB Components (Services)
TW, Pub, REST, Client
CRAB Monitoring
Which data we use
How those are send
How are stored
How are displayed
CRAB internal Infrastructure
Oracle, puppet, gitlab, GitHub, K8s, logstash, filebeat
External Infrastructure (how we actually use those things in our life)
Rucio, DBS, DAS, CMSWEB
Past incidents
How to mainain this document (better title needed)
Bits and pieces (miscellanea)

```

## Comment (belforte, 2024-09-04T16:18:18Z)

Am initial draft of the restructured index is in https://gitlab.cern.ch/belforte/cms-crab-docs/-/tree/refactoring?ref_type=heads

I thought it is too many changes for modifying the actual document immediately.

@novicecpp

## Comment (novicecpp, 2024-09-04T16:32:02Z)

Thanks Stefano.
If you satisfy with the result, please push to `crab3` and leave the restructuring directory to me.
Well, it will break the link we already shared in the GH issues but at least we can use the broken url as a clue to find the new url.

## Comment (belforte, 2024-09-04T18:48:11Z)

I will wait for you and Vijay to have a a look next week and possibly comment. I may still change things over next dasy. But it is a work which takes time. I only hope to achieve the "if you add a page you may have an idea where to put it".

## Comment (belforte, 2024-09-10T14:17:31Z)

closed via https://gitlab.cern.ch/crab3/cms-crab-docs/-/commit/e33228f8031be8bc045306483ef882dedfe40482 and https://gitlab.cern.ch/crab3/cms-crab-docs/-/commit/3ba44a14990e615e1398bbae11b64ca05c7d66c9
