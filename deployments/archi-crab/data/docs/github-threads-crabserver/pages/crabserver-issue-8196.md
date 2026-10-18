# dmwm/CRABServer issue #8196: CMSRunAnalysis.py should accept a JSON file as arg

State: closed
Opened: 2024-01-29T10:32:01Z
Closed: 2024-01-30T17:26:05Z
Labels: Type: Bug, Status: Done, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/8196

## Opening post (belforte, 2024-01-29T10:32:01Z)

for https://github.com/dmwm/CRABClient/issues/5276

It is desirable to send a JSON file with the args value properly encoded and parse it inside the script.
So that we can make things work when usign preparelocal. Current procedure of passing a list of quoted strings as argument to bash and from there to python fails. Even if it works when the same list is passed to HTCondor as command argument and from HTCondor to the job wrapper.
