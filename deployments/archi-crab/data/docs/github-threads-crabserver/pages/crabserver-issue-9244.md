# dmwm/CRABServer issue #9244: create a dev branch and profile for puppet and put crab-dev-tw04 in it

State: closed
Opened: 2025-12-09T16:44:46Z
Closed: 2026-03-26T16:27:31Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9244

## Opening post (belforte, 2025-12-09T16:44:46Z)

see also
https://cmscrab.docs.cern.ch/inventory/crab-inventory.html#tw-vms

somehow at some point we had another use for tw04, but now it is "safely spare".

schedd's are a bit more annoying to move around in puppet profiles due to the connection with SI repo, we can do one when needed.

Helpful documentation:
https://cmscrab.docs.cern.ch/crab-infrastructure/crab-puppet/using-puppet-in-crab.html#create-new-puppet-environment

## Comment (belforte, 2026-03-26T16:27:31Z)

Done. Created puppet environemnt `crabdev` which points to `dev` branch.
As per https://cmscrab.docs.cern.ch/crab-infrastructure/crab-puppet/using-puppet-in-crab.html#puppet-enviromnet and https://cmscrab.docs.cern.ch/crab-infrastructure/crab-puppet/introduction.html#environmentbranch

See updated https://cmscrab.docs.cern.ch/inventory/crab-inventory.html
* schedd (AP)

<img width="472" height="63" alt="Image" src="https://github.com/user-attachments/assets/e4b8f288-2df7-464e-8352-ccd7ae371068" />

* TW

<img width="470" height="62" alt="Image" src="https://github.com/user-attachments/assets/4ed1725f-7ab8-4ecf-abcf-f9afe9e13eb1" />
