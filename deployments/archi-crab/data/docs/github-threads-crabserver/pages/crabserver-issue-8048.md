# dmwm/CRABServer issue #8048: Validate latest CRABClient on all releases

State: closed
Opened: 2023-11-30T11:58:22Z
Closed: 2023-12-01T10:56:39Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/8048

## Opening post (belforte, 2023-11-30T11:58:22Z)

After the changes to [Jenkins](#8025) and for py2/3 compatibility in Client ([#5261](https://github.com/dmwm/CRABClient/issues/5261) and [#5233](https://github.com/dmwm/CRABClient/issues/5233)) and Server ( #8028 )

I am doing an exhaustive check with Jenkins of all CMSSW releases in our list with current CrabClientValidation

- [x] 7_1_29 #8033 OK
- [x] 7_6_7 #8035 OK
- [x] 8_0_36  #8037 OK
- [x] 9_4_21 #8039 OK
- [x] 10_1_0 #8041 **FAIL** - to b investigate
- [x] 10_6_26 #8043 OK
- [x] 12_5_0 #8045 OK
- [x] 12_6_4 #8046 Failed (task had not completed). Try again.
    - [x] #8049 OK (as expected)
- [x] 13_0_2 #8031 and #8032 . Failed to bootstrap (!). Try again.
   - [x] #8050 OK (confirming that the failed to bootstrap was some transient problem)

- [x] make sure that CMSSW_7 was using client from HEAD (ref #8029 ) **FAIL** both used production crab instead
   - [x] back to #8029 with increased priority

## Comment (belforte, 2023-11-30T23:35:52Z)

all problems understood and hopefully fixed.
One last round of validation

- [ ] https://github.com/dmwm/CRABServer/issues/8059
- [x] https://github.com/dmwm/CRABServer/issues/8060
- [x] https://github.com/dmwm/CRABServer/issues/8061
- [x] https://github.com/dmwm/CRABServer/issues/8062

## Comment (belforte, 2023-11-30T23:42:27Z)

oh damn CMSSW_13 now fails with
00:35:01 /build/cmsbld/jenkins/workspace/CRABServer_ExecuteTests/CRABClient/bin/crab: line 10: [: -ge: unary operator expected

that line is the one I just changed in CRABClient/bin/crab

bloody typo !!!
```
[ $CMSSW_Major -ge 10 ] && [ $CMSSSW_Serie -ge 2 ] && python_cmd="python3"

```
there is one `S` too many . :-(
Note that test was working for CMSSW_10_6 because in that case it falls back to using `python crab.py` and in older CMSSW which still have python2, `python` is defined. Only in CMSSW_12/13 it goes away

## Comment (belforte, 2023-11-30T23:51:13Z)

pff.. now CMSSW_13 fails with
```
Will use CRAB configuration file ./crabConfiguration.py ERROR: ImportError: No module named FWCore.ParameterSet.Types 
```
yeah the logic of this line plainly wrong. 
```bash
[ $CMSSW_Major -ge 10 ] && [ $CMSSW_Serie -ge 2 ] && python_cmd="python3"
```

## Comment (belforte, 2023-12-01T09:51:34Z)

try again after fix in https://github.com/dmwm/CRABClient/pull/5266/commits/ad464adebfce38ef52de25dd0a32130b1c558e74

- [x] https://github.com/dmwm/CRABServer/issues/8069
- [x] https://github.com/dmwm/CRABServer/issues/8078
- [x] https://github.com/dmwm/CRABServer/issues/8070
- [x] https://github.com/dmwm/CRABServer/issues/8071
- [x] https://github.com/dmwm/CRABServer/issues/8072
- [x] https://github.com/dmwm/CRABServer/issues/8073
- [x] https://github.com/dmwm/CRABServer/issues/8074
- [x] https://github.com/dmwm/CRABServer/issues/8075
- [x] https://github.com/dmwm/CRABServer/issues/8076
- [x] https://github.com/dmwm/CRABServer/issues/8077

## Comment (belforte, 2023-12-01T10:56:39Z)

Finally submission and ClientValidation succeeds on all releases in our list (10).
