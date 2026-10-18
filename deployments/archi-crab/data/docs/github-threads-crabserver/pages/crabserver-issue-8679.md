# dmwm/CRABServer issue #8679: CRAB monitoring diagram

State: closed
Opened: 2024-08-30T15:01:18Z
Closed: 2024-09-13T11:19:02Z
Labels: Type: Documentation
URL: https://github.com/dmwm/CRABServer/issues/8679

## Opening post (novicecpp, 2024-08-30T15:01:18Z)

We have 4 different log pipelines. 
We need to write it down and put into our docs. Otherwise we forget.

Diagram will serve as map how monitoring services are connected and starting point for debugging.

## Comment (belforte, 2024-08-30T15:28:44Z)

When I looked at the non-timber [one](https://monit-opensearch-lt.cern.ch/dashboards/goto/31d6e610962e003ce8adc89217e18896)  I was also annoyed by the fact that we have 7 CRAB indexes. I surely have some fault there. 
We may not want to call it "7 OS pipelines plus 3 FileBeat pipelines", but the need for clarification runs deep !
Or do we have 4 filebeat (log) pipelines ? REST, TW, Publisher + ?

## Comment (novicecpp, 2024-09-09T11:29:48Z)

https://cmscrab.docs.cern.ch/technical/crab-monitoring/monitoring-pipelines.html
Partially done. Next is to add grafana side (the [datasources.json](https://github.com/dmwm/CMSMonitoring/blob/master/static/datasources.json)),
and extras:
- TW metrics page. 
- REST metrics page.

## Comment (belforte, 2024-09-09T16:41:32Z)

great job ! English needs finessing though. Tastes a bit like "robotic translation from a Thai source". But I can understand none the less.
Hand to Vijay ?

## Comment (novicecpp, 2024-09-10T10:31:42Z)

No. Let me do it. It still not complete. 
Then feel free to changes whatever you want.

## Comment (novicecpp, 2024-09-13T11:19:02Z)

Done.
I am closing this issue. @belforte if you want @aspiringmind-code to modify it, feel free to reopen this issue.

## Comment (belforte, 2024-09-14T16:38:15Z)

looks good now. Thanks !
