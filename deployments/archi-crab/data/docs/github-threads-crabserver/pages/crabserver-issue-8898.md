# dmwm/CRABServer issue #8898: Rewrite CCV test in python instead of bash using client API

State: open
Opened: 2025-01-29T08:56:07Z
URL: https://github.com/dmwm/CRABServer/issues/8898

## Opening post (aspiringmind-code, 2025-01-29T08:56:07Z)

[makeTests.py](https://github.com/aspiringmind-code/CRABServer/blob/c54b1bd15ad1574678db551932ace2218e39707f/test/makeTests.py) uses bash currently for the validation scripts. We wish to explore if python would be better suited for it. For example see usage of CRAB CLIENT API [here](https://github.com/aspiringmind-code/CRABServer/blob/c54b1bd15ad1574678db551932ace2218e39707f/cicd/gitlab/st/statusTracking.py#L161C1-L161C74)
