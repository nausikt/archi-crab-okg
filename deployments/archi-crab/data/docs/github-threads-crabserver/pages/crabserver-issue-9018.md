# dmwm/CRABServer issue #9018: CheckTapeRecall monitoring failed when tasks list was empty.

State: closed
Opened: 2025-03-28T11:33:18Z
Closed: 2025-03-28T13:25:07Z
Labels: Area: MONIT
URL: https://github.com/dmwm/CRABServer/issues/9018

## Opening post (nausikt, 2025-03-28T11:33:18Z)

The empty tasks list rule was created by Jenkins task. So, it would be great to have some better protection on this kind of unexpected empty list.

```
30    [250327_154807:tmenezes_crab_crab_MC_2016_Mono...
31    [250327_154520:tmenezes_crab_crab_MC_2016_Mono...
32    [250327_125440:ccollard_crab_Analysis_SpecialZ...
33                                                   []
34    [250327_154847:tmenezes_crab_crab_MC_2016_Mono...
35    [250327_125529:ccollard_crab_Analysis_SpecialZ...
36    [250327_154831:tmenezes_crab_crab_MC_2016_Mono...
37    [250327_154537:tmenezes_crab_crab_MC_2016_Mono...
38    [250327_154839:tmenezes_crab_crab_MC_2016_Mono...
dtype: object
(Pdb) df.apply(lambda x: x.tasks[-1], axis=1)
```

Noted from Stefano: Beside having pandas protenction, the solution is to delete that problematic rule, of course, which was created  by a Jenkins task which is trying to recall that HC datasaet for CMSSW_7 `/GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/AODSIM`
