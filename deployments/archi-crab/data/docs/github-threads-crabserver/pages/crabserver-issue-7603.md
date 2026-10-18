# dmwm/CRABServer issue #7603: improve TapeRecall Rucio rule handling

State: closed
Opened: 2023-04-17T20:27:05Z
Closed: 2023-05-25T08:38:24Z
Labels: Type: Question, Status: On Hold, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7603

## Opening post (belforte, 2023-04-17T20:27:05Z)

as noted in #7530 , must improve the handling of Rucio rule for tape recall

- [x] whenever possible use the DBS dataset name and scope for the container #7641
- [x] try to avoid rule duplication (requires the above) #7641
- [x] make rule expire 30 days after data is recalled #7590 and  https://github.com/dmwm/CRABServer/commit/bbd2caba3073c50f7acdb6f6fa0536be547a01bd
- [x] allow 30 days for tape recall (this can be questioned) part of #7590
   * eventually we decided to make it 15 days before task expires and leave rule there 7 more days in case we want to debug somehting

## Comment (belforte, 2023-04-20T11:01:49Z)

we reviewed this in todays CRAB meeting. All in all could not find a strong motivation for doing this and changing from current setup has drawbacks too.
 * dataset name is now in the rule comments field
 * since we allow to recall list of blocks, at times we need am ad-hoc container name anyhow
 * it is good to be able to connect rule to task
 * not clear that having multiple rules on same set of files (with different container name) is a problem in/for Rucio, all in all it is working now.
    * But let's make sure that there will not be multiple request to FTS to copy same file to same destination

## Comment (belforte, 2023-04-25T09:03:07Z)

thinking more about duplicate rules, even if they do not harm, they annoy at least, by resulting in duplicated lines in the HTML table which lists pending rules from https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/CheckTapeRecall.py
![image](https://user-images.githubusercontent.com/1837785/234227119-d38be857-d8c9-4b71-8296-92e21e0a0042.png)


finding tasks which waits on a given rule can be done via Task table, since we store rule id in one column. So we only need a new API and then can easily add a column in the HTML table with pointers to task(s)

There is also a clear benefit aside avoiding duplicates :
 * using `cms:/...` container name whenever possible, will make it easy to connect with rules from DM ops

So I am inclided again about doing this change, even if we make the extra effort of adding one new API. @mapellidario @novicecpp I welcome your advice

## Comment (belforte, 2023-05-08T09:58:18Z)

plan (discussed in chat Stefano, Dario, Wa on May 8)
 - [ ] change the tape request to use as container name in the rule `cms:DBSdatasetNameHere'
    - [ ] use `name =DBSDatasetName_partial` and if we detect that this container already exist, simply add the new blocks to it
     - [ ] Extend the rule LIFETIME 
     - [ ] Update size info in the comment
 - [ ] Add a new REST API (or a new subresource to Task API) to list all tasks which have a given value of `tm_ddm_reqid`
 - [ ] more ?

## Comment (belforte, 2023-05-17T16:46:29Z)

Above plan can not work
1. container name has to end with `/TIER` and `TIER` has to be one of the predefined ones. Can not have `/blah/blahblah/AOD_partial`
2. can't reuse containers which ask for single block recalls, would recall also all blocks asked for years ago... need a unique name every time

## Comment (belforte, 2023-05-18T09:35:35Z)

New plan:
 - [x] modify `requestTapeRecall` to accept either a dataset name or a list of blocks #7641
    * when full dataset recall is sent, use `cms:datasetname` ad DID and if rule already exist, extend lifetime
    * when a list of block is sent do like now and create a DID in our scope using taskname
 - [x] modify `DBSDataDiscovery` to send dataset name when appropriate #7641
 - [x]     Update size info in the comment
    * the question is which size ! If a recall is issued for a dataset which is already partially on disk I decided to list the size of the data to be recalled, not of the full dataset
 - [x] Add a new REST API (or a new subresource to Task API) to list all tasks which have a given value of tm_ddm_reqid . Moved to https://github.com/dmwm/CRABServer/issues/7646
 - [x] Modify https://github.com/dmwm/CRABServer/blob/master/scripts/Utils/CheckTapeRecall.py  to adapt to new rule format and use new REST API above. Moved to https://github.com/dmwm/CRABServer/issues/7646
