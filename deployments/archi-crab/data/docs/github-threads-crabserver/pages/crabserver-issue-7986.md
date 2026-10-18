# dmwm/CRABServer issue #7986: rationalize use of HTTPRequests across Server and Client

State: open
Opened: 2023-10-27T09:20:11Z
Labels: Priority: Medium, Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/7986

## Opening post (belforte, 2023-10-27T09:20:11Z)

There is too much duplication and name confusion now.
I propose the following structure:

* HTTPRequests is a file of its own with different implementation in Cient and Server 
  * Server: HTTPRequestsPycurl.py
  * CLient: HTTPRequestsCurl.py
* usage: `from HTTPRequestsPycurl import HTTPRequests` etc.
* CRABRest becomes a common file/class (in ServerUtilities ? So it goes to Client as well w/o any other change)
* getDBSRest (only in Client atm) becames a new class DBSRest (how knows, may be useful in server too) (in ServerUtilities again?)

Problem/Question
  HTTPRequestsCurl  could be useful in Server as well as fallback ... who knows... so a single file/class with an extra argument ?
  beware that "import pycurl" breaks Client on some CMSSW versions and surely we do not want to import from WMCore.
 I.e. On server it may be good to have access to everyghing, buy on client we need "curl only", which is why back then we
 went for some code duplication and no file sharing.

@novicecpp @mapellidario opinions ? Is this worth pursuing ?

## Comment (novicecpp, 2023-10-27T13:46:24Z)

This should do together with https://github.com/dmwm/CRABServer/issues/7765

I think it good to refactor but I cannot say it ok or agree with your proposal due to my limited knowledge (need to research and sleep on it for some time).

> HTTPRequestsCurl could be useful in Server.

IMO, no. Because of what you said `beware that "import pycurl" breaks Client`.
On servers, we have a single version that runs at a time, so we do not need to care much about backward compatibility. If it breaks, just hot-patch it and think about a long-term solution later.

## Comment (belforte, 2023-10-27T14:10:40Z)

thanks for pointing out to #7765 !

Indeed, let's sleep on it and take our time. It is little code and main thing is to avoid headaches
