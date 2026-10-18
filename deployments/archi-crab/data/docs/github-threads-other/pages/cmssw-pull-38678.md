# cms-sw/cmssw pull request #38678:  Modifiers not being set properly in EventConfig for data (backport of #38622, 12_3_X)

State: closed
Opened: 2022-07-11T05:18:51Z
Closed: 2022-07-12T01:02:01Z
Merged: 2022-07-12T01:02:01Z
Labels: operations-approved, fully-signed, tests-approved, orp-approved, backport-ok
Milestone: CMSSW_12_3_X
URL: https://github.com/cms-sw/cmssw/pull/38678

## Opening post (seungjin-yang, 2022-07-11T05:18:51Z)

#### PR description:
This PR is a backport of #38622. This PR intoduces the lazy import of `Configuration.EventContent.EventContent_cff` to avoid calling `Modifier.toModify` before `Process.__init__`. The issue is well described in #38622.

#### PR validation:
Same as #38622.

#### If this PR is a backport please specify the original PR and why you need to backport that PR. If this PR will be backported please specify to which release cycle the backport is meant for:
This PR is a backport of #38622. This fix should be applied to releases for Run2022.


@jshlee  @watson-ij

## Comment (cmsbuild, 2022-07-11T05:19:15Z)

A new Pull Request was created by  @seungjin-yang (Seungjin Yang) for CMSSW_12_3_X.

It involves the following packages:

- Configuration/DataProcessing (**operations**)


@perrotta, @rappoccio, @cmsbuild, @qliphy, @fabiocos, @davidlange6 can you please review it and eventually sign? Thanks.
@Martin-Grunewald, @missirol, @fabiocos this is something you requested to watch as well.
@perrotta, @dpiparo, @qliphy, @rappoccio you are the release manager for this.

cms-bot commands are listed <a href="http://cms-sw.github.io/cms-bot-cmssw-cmds.html">here</a>

- Backported from #38622

## Comment (qliphy, 2022-07-11T09:11:31Z)

please test

## Comment (cmsbuild, 2022-07-11T13:35:29Z)

+1

**Summary**: https://cmssdt.cern.ch/SDT/jenkins-artifacts/pull-request-integration/PR-8e412f/26125/summary.html
**COMMIT**: 41d564b9dadd772514997130f144e765daa54fc7
**CMSSW**: CMSSW_12_3_X_2022-07-10-2300/slc7_amd64_gcc10
**User test area**: For local testing, you can use `/cvmfs/cms-ci.cern.ch/week1/cms-sw/cmssw/38678/26125/install.sh` to create a dev area with all the needed externals and cmssw changes.


## Comparison Summary



**Summary**:
 - No significant changes to the logs found
 - Reco comparison results: 2994 differences found in the comparisons
 - DQMHistoTests: Total files compared: 49
 - DQMHistoTests: Total histograms compared: 3626403
 - DQMHistoTests: Total failures: 7703
 - DQMHistoTests: Total nulls: 0
 - DQMHistoTests: Total successes: 3618678
 - DQMHistoTests: Total skipped: 22
 - DQMHistoTests: Total Missing objects: 0
 - DQMHistoSizes: Histogram memory added: 0.0 KiB( 48 files compared)
 - Checked 205 log files, 45 edm output root files, 49 DQM output files
 - [TriggerResults](https://cmssdt.cern.ch/SDT/jenkins-artifacts/baseLineComparisons/CMSSW_12_3_X_2022-07-10-2300+8e412f/51513/triggerResults): found differences in 1 / 48 workflows

## Comment (perrotta, 2022-07-11T17:39:17Z)

backport of https://github.com/cms-sw/cmssw/pull/38622

## Comment (qliphy, 2022-07-12T01:01:39Z)

+1

## Comment (cmsbuild, 2022-07-12T01:02:00Z)

This pull request is fully signed and it will be integrated in one of the next CMSSW_12_3_X IBs (tests are also fine) and once validation in the development release cycle CMSSW_12_5_X is complete. This pull request will be automatically merged.

## Comment (seungjin-yang, 2022-07-12T09:53:04Z)

@perrotta can you let me know when this fix will be applied to T0?

## Comment (perrotta, 2022-07-12T09:58:25Z)

> @perrotta can you let me know when this fix will be applied to T0?

One of the item to be discussed at today's ORP meeting (https://indico.cern.ch/event/1179450/) is exactly whether and when a new 12_3_X release will be needed, and by whom (i.e. T0). Even if we decide to build a new release, it will last just a few days, since the plan is to move T0 to 12_4 soon.

## Comment (seungjin-yang, 2022-07-12T10:09:30Z)

@perrotta Many thanks!
