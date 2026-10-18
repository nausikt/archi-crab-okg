# dmwm/CRABServer issue #9316: High number of DNS queries on APs

State: open
Opened: 2026-05-15T10:27:22Z
Labels: Type: Enhancement, Priority: Low
URL: https://github.com/dmwm/CRABServer/issues/9316

## Opening post (nausikt, 2026-05-15T10:27:22Z)

When APs reconnect, e.g. after a reboot, many tasks may restart at the same time and generate High number of DNS queries. This is similar to what happened once in TW side.

It may be in our interest to partially adopt Vijay's previous DNS caching solution for this issue as well.

More info: vocms0197
|                   |                |                                                        On IP DNS servers | queries/sec during 15 min |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                           --- TOTAL ---  |       74 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                        [vocms4100.cern.ch](http://vocms4100.cern.ch/) |      15.3 queries/sec     |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                      [cmssrv2313.fnal.gov](http://cmssrv2313.fnal.gov/) |      15.2 queries/sec     |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                      [cmssrv2314.fnal.gov](http://cmssrv2314.fnal.gov/) |      11.8 queries/sec     |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                        [vocms0815.cern.ch](http://vocms0815.cern.ch/) |      11.6 queries/sec     |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 | 5.6.1.0.9.8.1.0.0.0.0.0.0.f.0.0.1.2.4.8.0.0.0.0.a.6.0.0.0.2.6.2.ip6.arpa |      3.9 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 | 4.7.0.0.0.0.1.0.0.0.0.0.0.0.0.0.f.4.0.0.1.0.3.0.8.5.4.1.1.0.0.2.ip6.arpa |      3.9 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                           [cmsweb.cern.ch](http://cmsweb.cern.ch/) |      3.2 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                      [cmssrv2221.fnal.gov](http://cmssrv2221.fnal.gov/) |      2.1 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                        [vocms0825.cern.ch](http://vocms0825.cern.ch/) |      2.1 queries/sec      |
| [vocms0197.cern.ch](http://vocms0197.cern.ch/) | 188.184.31.249 |                                                         [fts3-cms.cern.ch](http://fts3-cms.cern.ch/) |      1.9 queries/sec      |

## Comment (belforte, 2026-05-15T13:14:26Z)

What Vijay addressed was DNS caching not being propagated to inside container. There is no container running in AP's. So this must be different. But the investigation from that have some useful command to tell if cache is working. Need to find the proper issue to find out.
