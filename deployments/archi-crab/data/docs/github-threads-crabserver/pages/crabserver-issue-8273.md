# dmwm/CRABServer issue #8273: test HTCondor 23.0.8 (in April)

State: closed
Opened: 2024-03-06T23:27:39Z
Closed: 2024-05-23T11:10:21Z
Labels: Type: Enhancement, Priority: High, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8273

## Opening post (belforte, 2024-03-06T23:27:39Z)

I will be released "in the first half of April"
it should fix the problem with reading user log which appeared in 23.0

References: 
the [thread](https://lists.cs.wisc.edu/archive/htcondor-users/2024-March/msg00023.shtml) which I started on HTCondor user forum, 
and this thread in [MatterMost] (https://mattermost.web.cern.ch/cms-o-and-c/pl/43s8jaj35frnuj5o3o9z5rfqjo)

quick summay is that sometimes a pilot fails to start with gldeInWMS sending a message
like [this](https://github.com/glideinWMS/glideinwms/blob/999602bcab33f8b1fd9ffd933abc6600acb6db18/creation/web_base/singularity_lib.sh#L1887-L1890) which is logged by the shadow as a multiline attribute which can not
be parsed by JEL. New condor version should suppress the newline.

## Comment (belforte, 2024-03-06T23:35:47Z)

more or less on same time frame there will also be a [fix from glideInWMS](https://lists.cs.wisc.edu/archive/htcondor-users/2024-March/msg00032.shtml)

## Comment (belforte, 2024-05-23T11:10:21Z)

since this was fixed in glideInWMS, we can simply move to HTCondor 23 with our time, w/o hurry
