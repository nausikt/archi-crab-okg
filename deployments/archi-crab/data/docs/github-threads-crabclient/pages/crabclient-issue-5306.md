# dmwm/CRABClient issue #5306: improve JSON report from crab status

State: open
Opened: 2024-05-02T15:26:33Z
Labels: enhancement, MediumPrio
URL: https://github.com/dmwm/CRABClient/issues/5306

## Opening post (belforte, 2024-05-02T15:26:33Z)

As Konstantin Androsov @kandrosov reported 

-------- Forwarded Message --------
Subject: Re: out of quota !
Date: Thu, 2 May 2024 10:29:30 +0200
From: Konstantin Androsov <konstantin.androsov@cern.ch>
To: Stefano Belforte <Stefano.Belforte@cern.ch>


About the JSON API. Yes, I'm currently using "crab status --json" to parse the statuses of individual jobs. However, JSON doesn't contain the same amount of information as the full output: there is no status on scheduler, status on server, various warnings (that sometimes can be actionable), url to dashboard etc. For that reason, I am still parsing txt output... If all commands had a complete json interface it would be a big improvement.
