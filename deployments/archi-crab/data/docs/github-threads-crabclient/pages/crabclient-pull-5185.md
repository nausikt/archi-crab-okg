# dmwm/CRABClient pull request #5185: new Data.inputBlocks parameter

State: closed
Opened: 2023-02-07T12:44:46Z
Closed: 2023-02-10T14:59:38Z
Merged: 2023-02-10T14:59:37Z
URL: https://github.com/dmwm/CRABClient/pull/5185

## Opening post (novicecpp, 2023-02-07T12:44:46Z)

Fix https://github.com/dmwm/CRABServer/issues/7203

Client side of https://github.com/dmwm/CRABServer/pull/7525
`Data.inputBlocks` as list of input blocks that users want to processes. 

~~Currrently drafting. We can lets users supply only blocks uuid then we concat its with inputDataset in client side.~~
~~And/or lets user supply full block name but we need to verify if dataset's name in block is same as inputDataset~~

I decide to allow users to provide either full block name or block UUID. 
- If it match UUID format, client will append dataset name for users before sending to server.
- If not, let server report error in case they forget to change dataset name.

## Comment (cmsdmwmbot, 2023-02-07T12:48:05Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 5 warnings and errors that must be fixed
   * 1 warnings
   * 131 comments to review
 * Pycodestyle check: succeeded
   * 441 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/925/artifact/artifacts/PullRequestReport.html

## Comment (cmsdmwmbot, 2023-02-07T18:32:15Z)

Jenkins results:
 * Python3 Pylint check: failed
   * 9 warnings and errors that must be fixed
   * 2 warnings
   * 179 comments to review
 * Pycodestyle check: succeeded
   * 540 comments to review

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABClient-PR-test/926/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2023-02-10T14:39:38Z)

Looks very good, thanks.
Hey... super nice to users !
> I decide to allow users to provide either full block name or block UUID.

## Comment (novicecpp, 2023-02-10T14:59:31Z)

Thanks Stefano.
Merging.
