# dmwm/CRABServer issue #8380: Upgrade to WMCore 2.3.3

State: closed
Opened: 2024-05-08T10:37:04Z
Closed: 2024-08-23T10:33:41Z
Labels: Status: In Progress, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8380

## Opening post (mapellidario, 2024-05-08T10:37:04Z)

@germanfgv pointed out that he upgraded WMCore/Lexicon.py [1] to match the new `L1SCOUT` data tier. We use the variable `DATASET_RE` from that file here [2].

CRAB can not submit tasks that process that data tier until we upgrade the REST to wmcore 2.3.2 

However, while we are at this, I suggest to:

- [x] build crabserver and tw against wmcore 2.3.3
- [x] validate new REST in preprod
- [x] deploy new REST in prod (next monday, 13th may)
- [x] validate TW in preprod
- [x] deploy TW in prod

[1] https://github.com/dmwm/WMCore/blob/e4628ce9ab25f5015b71197a42eb09d630286318/src/python/WMCore/Lexicon.py#L205
[2] https://github.com/dmwm/CRABServer/blob/9a97d9ce598f97e3ce3c007b914eb0f81765538d/src/python/CRABInterface/Regexps.py#L44

## Comment (mapellidario, 2024-05-08T16:26:29Z)

REST looks good, see #8384 

plan: I will deploy next week, it is a bit late to deploy now and tomorrow is holiday at cern and we do not want everything to fall on Stefano's shoulders :)

## Comment (belforte, 2024-05-16T21:27:41Z)

@mapellidario ping. Are you satisfied with current validation ? Time to deploy and close ?

## Comment (belforte, 2024-08-23T10:33:41Z)

all done
