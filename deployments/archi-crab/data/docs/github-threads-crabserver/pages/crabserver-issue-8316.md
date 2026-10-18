# dmwm/CRABServer issue #8316: use robot certificate to retrieve proxies from myproxy

State: closed
Opened: 2024-04-03T21:09:08Z
Closed: 2024-06-24T10:44:20Z
Labels: Type: Enhancement, OPERATION
URL: https://github.com/dmwm/CRABServer/issues/8316

## Opening post (belforte, 2024-04-03T21:09:08Z)

* Maarten [says](https://ggus.eu/index.php?mode=ticket_info&ticket_id=166121) that a robot cert is fine 
* we can use the [current one](https://cmscrab.docs.cern.ch/technical/cmscrab-service-account.html#create-robot-certificate) which is already available in TW 
   * of course need to have it added to authorized retrievers via e.g. GGUS
* need simply to change the [TW config](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb#L114-115) in puppet in order to use it 
* then there will be no need to ask for adding host cert etc.  Everything taken care of by [puppet](https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/manifests/crabtaskworker/certificate.pp#L97-113)
* we should update documentation of what the robot cert. is used for

## Comment (belforte, 2024-04-03T21:11:21Z)

@novicecpp may I assign this to you ?

## Comment (belforte, 2024-04-04T09:53:41Z)

I have added the request to enable the robot certificate to [GGUS](https://ggus.eu/index.php?mode=ticket_info&ticket_id=166121)

Once they say that they did it, please give it a try

## Comment (belforte, 2024-06-17T10:57:20Z)

it was tested and added to delegation list.
What is needed is to update the TW configuration. These two lines
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/blob/qa/code/templates/crabtaskworker/taskworker/TaskWorkerConfig.py.erb?ref_type=heads#L117-118
should point to `/data/certs/robotcert.pem` and `/data/certs/robotkey.pem`

## Comment (belforte, 2024-06-17T14:26:30Z)

reference: https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/merge_requests/208

## Comment (belforte, 2024-06-24T10:41:58Z)

@mapellidario @novicecpp can we close this ?

## Comment (novicecpp, 2024-06-24T10:44:20Z)

Yes. Thanks to Dario for taking care deployment.
https://cms-talk.web.cern.ch/t/prod-tw-uses-new-robot-cert-for-myproxy/42569

## Comment (belforte, 2024-06-24T10:45:29Z)

thanks !
