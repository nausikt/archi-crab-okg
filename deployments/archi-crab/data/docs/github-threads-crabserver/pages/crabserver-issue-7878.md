# dmwm/CRABServer issue #7878: support for `/store/group/rucio` in Rucio ASO

State: closed
Opened: 2023-09-14T17:18:13Z
Closed: 2023-09-19T14:42:22Z
Labels: RUCIO, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7878

## Opening post (belforte, 2023-09-14T17:18:13Z)

it should almost "work out of the box" aside from using proper account for Rucio client
(see [not from Rahul](https://its.cern.ch/jira/browse/CMSTRANSF-713?focusedId=4937867&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-4937867)  )
* to manage destination `/store/group/rucio/group_name`, RUCIO_Transfer script needs to use
   * `account="group_name"` (still authenticating with user's X509 proxy)
   * `scope="group.group_name"`

But for sure we need to test ! And for that we need our own group. See  [CMSTRANSF-713](https://its.cern.ch/jira/browse/CMSTRANSF-713)

let's make a list of tasks
- [x] change code - Wa
- [x] get test group/quota and test via CLI - Stefano
- [x] test with CRAB - both

## Comment (novicecpp, 2023-09-19T14:43:59Z)

Work perfectly.

https://cmsweb-test12.cern.ch/crabserver/ui/task/230919_133715:tseethon_crab_rucio_transfers_groupaccount_publication_test12_20230919_153707
https://cms-rucio-webui.cern.ch/rule?rule_id=af864f28274f445eac288afe9a685a14#locks

## Comment (novicecpp, 2023-09-19T14:57:22Z)

It is worth noting the naming convention for group users (thanks @dynamic-entropy for explaining this morning):
- If `RUCIO_ACCOUNT` is `crab_test_group`:
  - Scope: `group.crab_test`
  - Path: `/store/group/rucio/crab_test/....`
