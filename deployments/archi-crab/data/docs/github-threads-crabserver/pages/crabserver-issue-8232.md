# dmwm/CRABServer issue #8232: HTCondor updates ?

State: closed
Opened: 2024-02-07T10:59:38Z
Closed: 2024-02-29T13:38:32Z
URL: https://github.com/dmwm/CRABServer/issues/8232

## Opening post (belforte, 2024-02-07T10:59:38Z)

need to talk with SI about new HTCondor version with new JDL format and possible move of scheduler VM's from SL7 to SL8 or Alma9

## Comment (aperezca, 2024-02-07T11:14:07Z)

Hi Stefano, yes, SI is already working on providing a test environment (ITB-Dev pool) with Alma9 and HTCondor v23 in order to test and adapt CRAB and WMAgents to the new versions. Let's coordinate on the next steps.

## Comment (belforte, 2024-02-07T13:15:01Z)

thanks Antonio !

## Comment (belforte, 2024-02-07T14:25:55Z)

On this topic, some new HTC version comes with a new JDL syntax IIUC (e.g. no `+` signs any more). Do we have to do change things on our  end ? Which version is that ? @mmascher

## Comment (belforte, 2024-02-07T16:55:17Z)

looks like  HTCondor23 is indeed where all big changes happen https://indico.cern.ch/event/1225117/contributions/5587842/attachments/2732315/4750236/Whats_New_european_workshop_2023%20-%20Copy.pdf

It is not clear to me if e.g. `condor_q` will stay or will stop working !

## Comment (belforte, 2024-02-29T13:37:26Z)

questions here have been aswered and work is now tracked in #8258
