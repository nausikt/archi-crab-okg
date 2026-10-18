# dmwm/CRABServer issue #9064: use  `ignore_availability` flag when creating rules in Rucio-ASO

State: closed
Opened: 2025-05-07T13:29:21Z
Closed: 2025-05-09T15:38:39Z
Labels: Type: Enhancement, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9064

## Opening post (belforte, 2025-05-07T13:29:21Z)

from a thread in MatterMost just now:

Stefano Belforte
[3:08 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/4d1tpcaqj7fu9p6pk9yugfxtsr)
I found this when CRAB ASO was trying to create a rule to transfer job output to T2_IT_Legnaro, where I have free quota:

  File "/cvmfs/cms.cern.ch/rucio/x86_64/rhel9/py3/current/lib/python3.9/site-packages/rucio/client/ruleclient
.py", line 92, in add_replication_rule
    raise exc_cls(exc_msg)
rucio.common.exception.RSEWriteBlocked: RSE excluded; not available for writing.
Details: RSE excluded; not available for writing.
can you explain ?

is this something like "it was disabled by TranferOps and it affects also users" ? Or a misconfiguration ? 


Stefano Belforte
[3:14 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/u85za3wueb8jtyfm5fp43xkm1w)
A new feature maybe ? I am prepared for a rule to take time to complete if an RSE has problems, but if I can't create the rule...what can I do ?


Hasan Ozturk
[3:15 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/a7azbmb5sj8j9mywbfe1njzrqo)
When site isn't green in SSB, we disable writes https://cmssst.web.cern.ch/sitereadiness/report.html#T1_IT_Legnaro


Stefano Belforte
[3:16 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/153c94xcy7f4pyn1wk9jtmwa8h)
I'd expect "disable writes" as "do not try FTS", not "not create rule".


Hasan Ozturk
[3:16 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/bgqyrotfttgodbz83fi5owoo4w)
Perhaps, you can create the rule with ignore_availability flag? https://rucio.github.io/documentation/html/client_api/ruleclient.html#rucio.client.ruleclient.RuleClient.add_replication_rule


Hasan Ozturk
[3:16 PM](https://mattermost.web.cern.ch/cms-o-and-c/pl/nrzyogu157ge8phe4hi1qpqjaw)
Then rucio should accept the rule and submit to FTS when the site is back
