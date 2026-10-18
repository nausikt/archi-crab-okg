# dmwm/CRABServer issue #8870: use FQDN when sending data to MONIT

State: closed
Opened: 2025-01-08T14:42:52Z
Closed: 2025-04-07T08:45:01Z
URL: https://github.com/dmwm/CRABServer/issues/8870

## Opening post (belforte, 2025-01-08T14:42:52Z)

On 08/01/2025 15:32, Nikodemas Tuckus wrote:
>
> Dear all,
>
> IT Messaging team will stop supporting messaging broker endpoints using non fully qualified names (e.g. cms-mb, instead of cms-mb.cern.ch). Please check if any of your pipelines are using the short names and switch them to fully qualified endpoints as soon
>  as possible. You can read more about this here: 
> [OTG0153206](https://cern.service-now.com/service-portal?id=outage&n=OTG0153206).
>
> Best regards, Federica and Nikodemas
>
>

## Comment (belforte, 2025-01-08T14:49:37Z)

see also thread in https://mattermost.web.cern.ch/cms-o-and-c/pl/yq9g6uzy5tyu8fgax7dkjy44aw

## Comment (aspiringmind-code, 2025-04-07T08:45:01Z)

Does not need any work. See Nikodemas's [message](https://mattermost.web.cern.ch/cms-o-and-c/pl/wpt59wyn13g9zd5x5p6tx85zua)

## Comment (belforte, 2025-04-07T09:12:39Z)

i would still add `.cern.ch`, just in case things change in the future
