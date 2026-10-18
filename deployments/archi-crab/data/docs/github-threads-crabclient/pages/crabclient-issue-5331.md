# dmwm/CRABClient issue #5331: refuse to submit if myproxy validity is < 5 days

State: closed
Opened: 2024-09-06T13:50:04Z
Closed: 2024-11-11T15:04:06Z
Labels: enhancement, Support, HighPrio
URL: https://github.com/dmwm/CRABClient/issues/5331

## Opening post (belforte, 2024-09-06T13:50:04Z)

current TW raises submit failure in this case. So.. no point.

Better yet, make min myproxy credential validity one constant in ServerUtilities and share it in TW and Client

## Comment (belforte, 2024-11-09T18:02:39Z)

Now that we are about to make a new client, let's do this so hopefully we avoid being annoyed again in this way
![image](https://github.com/user-attachments/assets/32d48fe4-9292-4ad1-a36f-f2893f14b078)

where all failures are of the kind

 ["youngwan", "241109_171721:youngwan_crab_WRtoNTautoTauTauJJ_WR5000_N4300_TuneCP5_13TeV_madgraph-pythia8__RunIISummer20UL17MiniAODv2--c_v9-v2", "Could not get a proxy valid for at least 5-days from myproxy.cern.ch for /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=youngwan/CN=848372/CN=Youngwan Kim."]

## Comment (belforte, 2024-11-11T10:22:54Z)

Client requests a 2 week credential in myproxy, but it accepts less if user cert is about to expire. Relevant code is
https://github.com/dmwm/CRABClient/blob/653bafe0f37f50459b3d785eb76be361b7fc6acd/src/python/CRABClient/CredentialInteractions.py#L170-L182

## Comment (belforte, 2024-11-11T10:25:59Z)

should exit with error if `usercertDayLeft < 5 days`

## Comment (belforte, 2024-11-11T10:35:08Z)

currently client exits only if 0 days are left, which is OK for status but not for submit !
https://github.com/dmwm/CRABClient/blob/653bafe0f37f50459b3d785eb76be361b7fc6acd/src/python/CRABClient/CredentialInteractions.py#L163-L168
