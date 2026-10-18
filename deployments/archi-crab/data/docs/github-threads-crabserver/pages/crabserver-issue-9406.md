# dmwm/CRABServer issue #9406: Schedds under duty-cycle pressure, started to be recurring pattern

State: open
Opened: 2026-08-31T13:59:51Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9406

## Opening post (nausikt, 2026-08-31T13:59:51Z)

Today, i got a report from Noy.

That HammerCloud status were missing/fragmenting since yesterday which we later found likely due to intensive duty cycles spikes across our schedd pool. [1,2]

We need to investigate the signature of the throttling workflow that spiked and caused this recurring pattern.

[1] HammerCloud fragmented status.
<img width="290" height="590" alt="Image" src="https://github.com/user-attachments/assets/d65d01a7-5487-4e1b-b081-720ec7004ba1" />

[2] CRAB Schedds duty cycles spikes.
<img width="1275" height="606" alt="Image" src="https://github.com/user-attachments/assets/e9912cfc-03fe-47ac-8407-7ddcbe08cfcb" />

## Comment (belforte, 2026-08-31T14:28:20Z)

Is the problem that job were not executed at expected constant intervals ? Or was the monitoring delayed ?
Anyhow in the current ways HC jobs are executed we can not guarantee constant steady behavior.
It would be nice that schedd's duty cycle never reaches 100%, for all things, not only HC. But I do not think we can do more that what we are doing already in that respect.
