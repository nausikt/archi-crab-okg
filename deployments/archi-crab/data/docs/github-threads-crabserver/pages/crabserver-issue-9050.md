# dmwm/CRABServer issue #9050: use RSE downtime status to decide where to send jobs

State: open
Opened: 2025-04-16T16:59:41Z
URL: https://github.com/dmwm/CRABServer/issues/9050

## Opening post (belforte, 2025-04-16T16:59:41Z)

see
https://twiki.cern.ch/twiki/bin/view/CMS/SiteSupportRucioStatus

and discussion in
https://cms-talk.web.cern.ch/t/all-jobs-using-crab-fail/123866/19

## Comment (stlammel, 2025-04-17T21:52:27Z)

found the old email exchange of last November:


No problem writing those JSONs. The web area might be
longer lived than the Apache ecosystem for monitoring at
CERN. I was going to write the Grafana python access
yesterday evening and discovered i already had it. Allowed
me to go home early!
 - Stephan



________________________________________
From: Stefano Belforte <Stefano.Belforte@cern.ch>
Sent: Thursday, November 21, 2024 07:26
To: Stephan Lammel
Cc: Stefano Belforte
Subject: Re: Rucio metric

thanks for this new JSON file Stephan.

I still do not want to add a dependency on this direct Grafana query.
Your code is not trivial, and besides the need to manged another
secrete, supporting this on our side would mean a new skill and a new
point of failure added to a tool which already has too many.

I will add to our todo list to use this information when checking
stageout destination.

Stefano


On 21/11/2024 00:02, Stephan Lammel wrote:
> Hallo Stefano,
>     so, i added writing of a file similar to usableSites.json
> but based on the RucioStatus metric values. The "dependable"
> and "enabled" are yielding a usable/green all other states
> a not_usable/red.
> https://cmssst.web.cern.ch/ssb_metric/usableRucio.json
>
>     If you want to switch to using Grafana instead you would
> need something like in the attached script. (I think i made it
> for you in 2020 but you preferred to stay with the JSON on
> the web page.) I have updated it adding the rucio_status
> metric. Take a look and let me know if you have any questions
> or if something isn't clear. Please keep the token for the
> header of the Grafana query confidential/don't put into a
> repository, etc.
>
>     I'll fix SiteReadiness adding the metric next.
>     Thanks,
>             cheers,  Stephan
>
>
>
>
> ________________________________________
> From: Stefano Belforte <Stefano.Belforte@cern.ch>
> Sent: Monday, November 18, 2024 08:51
> To: Stephan Lammel
> Cc: Stefano Belforte
> Subject: Re: Rucio metric
>
> happy to switch if the other way is preferred and less work for you.
> Maybe you can put instructions in the twiki ?
>
> On 18/11/2024 15:49, Stephan Lammel wrote:
>> Ahhh, i didn't realize you are (still) using the usableSites.json

## Comment (belforte, 2026-07-13T14:36:46Z)

I doubt that we want to make this kind of changes in CRAB. It is not well defined and may lead to more problems than solutions.
