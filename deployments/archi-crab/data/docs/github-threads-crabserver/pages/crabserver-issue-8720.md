# dmwm/CRABServer issue #8720: remove obsolete `site.ad` file from TW and schedulers

State: closed
Opened: 2024-09-26T16:32:11Z
Closed: 2024-09-30T13:02:45Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8720

## Opening post (belforte, 2024-09-26T16:32:11Z)

since a long time only `site.ad.json` is used ! ref: https://github.com/dmwm/CRABServer/issues/8699#issuecomment-2377222298

text pasted here for convenience:
**site.ad vs. site.ad.json**

manipulation of `site.ad` in AdjustSites,py is unchanged since Brian's commit in 2013.
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/scripts/AdjustSites.py#L481-L487
But I can't find any other place in the code base which references to CRAB_SiteAdUpdate.
Is that code simply "never executed" ?

PreJob uses `site.ad.json` to create site lists `avalaible` (where we can run) and ``datasites` (where data is).
If it does not find it, falls back to `site.ad` to create list of available sites, only, and at first sight it should crash since `datasites` is unconditionally used in following code

There is also this very interesting commit from Brain 10y ago  https://github.com/dmwm/CRABServer/commit/75b85ca950219a823d92121eb231d1d50c2d4a2a which looks like he introduced the JSON, leaving the old code for temporary compatibility (?) and then.. change stuck.

So I am leaning to `site.ad` can be removed.

AFAICT those two files are created by DagmanCreator
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L1089-L1090
Yet I can't be sure nor figure out how they are populated from reading the code. Need to run it step-by-step.

`site.ad.json` contains `siteinfo` structure
`site.ad` contains `sitead` strucutre
those structures are initialized to "empty" in
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L805-L816
(when DagmanCreator runs in TW, there are no files to read)

so in particular we start with
```python
siteinfo = {'group_sites': {}, 'group_datasites': {}}
```
Then DagmanCreator calls createSubdag() which gets the list of data sites and available sites for each job groups (one job group for each set of locations, IIUC)
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L891
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L896
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L910
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L933
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L943-L944
 and calls  makeDagSpecs() where those are added to `siteinfo` dictionary
https://github.com/dmwm/CRABServer/blob/e8149dda5ff7a4fee80d3b25d5c038ead60c711d/src/python/TaskWorker/Actions/DagmanCreator.py#L599-L601
(no comment on the what looks like a horrible dirty trick with L599)

My conclusion from the above is that `site.ad` is old, obsolete, useless and can be simply removed.
