# dmwm/CRABServer issue #7570: JobWrapper should accept file:filename as PFN

State: open
Opened: 2023-03-17T14:02:58Z
Labels: Type: Enhancement, Priority: Medium, Area: JobWrapper
URL: https://github.com/dmwm/CRABServer/issues/7570

## Opening post (belforte, 2023-03-17T14:02:58Z)

see https://cms-talk.web.cern.ch/t/crab-failing-with-unable-to-parse-wmcores-jobreport-json-fjr-will-not-be-useful-message/21517/5

since cmsRun allows users to indicate `file:filepath` as output, and that is what we extract from framework job report, we should protect against dumbly pass it to e.g. `os.stat`

## Comment (belforte, 2023-03-17T14:04:12Z)

@mapellidario hopefully a one line change in CMSRunAnalysis.py
