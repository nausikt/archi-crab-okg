# dmwm/CRABServer issue #7833: in publication check in Jenkins skip automatic splitting probes

State: closed
Opened: 2023-08-17T07:15:45Z
Closed: 2023-08-17T07:34:21Z
URL: https://github.com/dmwm/CRABServer/issues/7833

## Opening post (belforte, 2023-08-17T07:15:45Z)

probe jobs will not be published ! Should not [wait for them](https://github.com/dmwm/CRABServer/issues/7831#issuecomment-1681328056)
```
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1000}, 'TN': '230816_161342:cmsbot_crab_20230816_181341', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1000/1000'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestRunning', 'jobsPerStatus': {'finished': 6}, 'TN': '230816_161344:cmsbot_crab_20230816_181343', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 1}, 'TN': '230816_161345:cmsbot_crab_20230816_181345', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/1/1'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230816_161347:cmsbot_crab_20230816_181346', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 100}, 'TN': '230816_161348:cmsbot_crab_20230816_181348', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/100/100'}
{'dbStatus': u'SUBMITTED', 'testResult': 'TestPassed', 'jobsPerStatus': {'finished': 10}, 'TN': '230816_161352:cmsbot_crab_20230816_181350', 'combinedStatus': 'COMPLETED', 'publication (fail/tdb/DBS)': '0/10/10'}

```
