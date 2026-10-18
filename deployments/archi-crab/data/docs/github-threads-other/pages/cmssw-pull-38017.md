# cms-sw/cmssw pull request #38017: [12_3_X] Use RAWEventContent parameter set for Repack output module

State: closed
Opened: 2022-05-19T14:29:16Z
Closed: 2022-05-20T00:33:49Z
Merged: 2022-05-20T00:33:49Z
Labels: operations-approved, fully-signed, tests-approved, orp-approved, allow-germanfgv
Milestone: CMSSW_12_3_X
URL: https://github.com/cms-sw/cmssw/pull/38017

## Opening post (germanfgv, 2022-05-19T14:29:16Z)

#### PR description:
Changes repack to use the defined [RAWEventContent](https://github.com/germanfgv/cmssw/blob/417d4ed121ff0a963bc4a29ef8423b3efbfe2fe6/Configuration/EventContent/python/EventContent_cff.py#L169-L178) output module configuration.

#### PR validation:
None beyond the tests in  #37791 

#### if this PR is a backport please specify the original PR and why you need to backport that PR:
Backport of #37791. Needed to use the right compression algorithm during 900 GeV collisions.

## Comment (cmsbuild, 2022-05-19T14:29:38Z)

A new Pull Request was created by  @germanfgv (Germán Felipe Giraldo Villa) for CMSSW_12_3_X.

It involves the following packages:

- Configuration/DataProcessing (**operations**)


@cmsbuild, @perrotta, @qliphy, @fabiocos, @davidlange6 can you please review it and eventually sign? Thanks.
@Martin-Grunewald, @missirol, @fabiocos this is something you requested to watch as well.
@perrotta, @dpiparo, @qliphy you are the release manager for this.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-cmds.html">here</a>

## Comment (germanfgv, 2022-05-19T14:33:00Z)

@drkovalskyi Here is the backport. @qliphy could you please trigger the tests?

## Comment (qliphy, 2022-05-19T14:45:33Z)

allow @germanfgv test rights

## Comment (qliphy, 2022-05-19T14:46:09Z)

please test

## Comment (cmsbuild, 2022-05-19T18:43:33Z)

+1

**Summary**: https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-f62d05/24867/summary.html
**COMMIT**: c2ea236eefc0cc9bf70cc91fd4aa1be33038a590
**CMSSW**: CMSSW_12_3_X_2022-05-19-1100/slc7_amd64_gcc10
**User test area**: For local testing, you can use `/cvmfs/cms-ci.cern.ch/week1/cms-sw/cmssw/38017/24867/install.sh` to create a dev area with all the needed externals and cmssw changes.


## Comparison Summary



**Summary**:
 - No significant changes to the logs found
 - Reco comparison results: 4 differences found in the comparisons
 - DQMHistoTests: Total files compared: 49
 - DQMHistoTests: Total histograms compared: 3628142
 - DQMHistoTests: Total failures: 7
 - DQMHistoTests: Total nulls: 1
 - DQMHistoTests: Total successes: 3628112
 - DQMHistoTests: Total skipped: 22
 - DQMHistoTests: Total Missing objects: 0
 - DQMHistoSizes: Histogram memory added: -0.004 KiB( 48 files compared)
 - DQMHistoSizes: changed ( 312.0 ): -0.004 KiB       MessageLogger/Warnings
 - Checked 205 log files, 45 edm output root files, 49 DQM output files
 - [TriggerResults](https://cmssdt.cern.ch/SDT/jenkins-artifacts/baseLineComparisons/CMSSW_12_3_X_2022-05-19-1100+f62d05/50410/triggerResults): no differences found

## Comment (germanfgv, 2022-05-19T21:52:33Z)

@perrotta @qliphy @davidlange6  All checks were successful. Can this be merged?

## Comment (qliphy, 2022-05-20T00:33:24Z)

+1
as requested by Tier0 offline to include LZMA4 RAW compression to be available before first collisions next week.

## Comment (cmsbuild, 2022-05-20T00:33:47Z)

This pull request is fully signed and it will be integrated in one of the next CMSSW_12_3_X IBs (tests are also fine) and once validation in the development release cycle CMSSW_12_5_X is complete. This pull request will be automatically merged.

## Comment (tvami, 2022-05-20T11:01:19Z)

For the record, we just identified that this breaks the ALCARAW files, for example the ECALPhiSym (noticed in the replay
https://github.com/dmwm/T0/pull/4664 )

## Comment (qliphy, 2022-05-20T11:26:22Z)

> For the record, we just identified that this breaks the ALCARAW files, for example the ECALPhiSym (noticed in the replay [dmwm/T0#4664](https://github.com/dmwm/T0/pull/4664) )

@germanfgv @drkovalskyi  Do you have any opinion on this?

## Comment (perrotta, 2022-05-20T12:40:34Z)

> For the record, we just identified that this breaks the ALCARAW files, for example the ECALPhiSym (noticed in the replay [dmwm/T0#4664](https://github.com/dmwm/T0/pull/4664) )

Should we revert this in 12_3_X, then? Or is it something you can deal with?
Is any fix expected soon (i.e. by today)?

## Comment (drkovalskyi, 2022-05-20T12:46:52Z)

We are working on it. Give us some time to finish a couple of tests to give the final answer later today.

## Comment (drkovalskyi, 2022-05-20T17:07:53Z)

Let's revert 12_3_X. We will propose a proper solution on 12_4_X first and then make a back port. We can live a bit longer with wrong compression.

## Comment (perrotta, 2022-05-20T17:14:01Z)

> Let's revert 12_3_X. We will propose a proper solution on 12_4_X first and then make a back port. We can live a bit longer with wrong compression.

@drkovalskyi just to be sure: are you proposing to revert this PR in 12_3_X?

## Comment (drkovalskyi, 2022-05-20T17:14:47Z)

yes
