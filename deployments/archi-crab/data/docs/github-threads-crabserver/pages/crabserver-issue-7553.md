# dmwm/CRABServer issue #7553: document inputblocks

State: closed
Opened: 2023-02-26T18:02:18Z
Closed: 2023-03-14T12:11:51Z
Labels: Type: Documentation, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7553

## Opening post (belforte, 2023-02-26T18:02:18Z)

new `inputblocks` feature needs to be documented in
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

ref #7528

## Comment (novicecpp, 2023-03-02T17:50:30Z)

(draft)

config
```
| =inputBlocks= | list of string | (Analysis) Specify blocks to process in the form of DBS block name or block UUID string. CRAB will only discover (do tape recall if necessary) and process these blocks. See [[this FAQ,https://linktofaq]] about tape recall. Require =Data.inputDataset= to be set.|
```

faq
```
---+++ How can I request tape recall for RAW data tier in CRAB?

%TWISTY{mode="div" showlink="Show" hidelink="Hide"}%
Now you can request tape recall for *any data tier*, but CRAB only allows recall on blocks via =Data.inputBlocks= configuration parameter with the sum of block size must not exceed 5 TB.

In example, we want to recall =/ZeroBias/Commissioning2021-v1/RAW#214fbb11-2d5c-4b8c-8ee5-b68de1d89153= and =/ZeroBias/Commissioning2021-v1/RAW#8760f6e6-6c5e-4c65-854d-02d4bc3312c5= from [[https://cmsweb.cern.ch/das/request?instance=prod/global&input=block+dataset%3D%2FZeroBias%2FCommissioning2021-v1%2FRAW,/ZeroBias/Commissioning2021-v1/RAW]] dataset.

CRAB config will be:

<verbatim class='config'>
config.JobType.pluginName = 'Analysis'
config.Data.inputDataset = '/ZeroBias/Commissioning2021-v1/RAW'
config.Data.inputBlocks = [
    '/ZeroBias/Commissioning2021-v1/RAW#214fbb11-2d5c-4b8c-8ee5-b68de1d89153',
    '/ZeroBias/Commissioning2021-v1/RAW#8760f6e6-6c5e-4c65-854d-02d4bc3312c5',
]
# or provide only block UUID
#config.Data.inputBlocks = [
#    '214fbb11-2d5c-4b8c-8ee5-b68de1d89153',
#    '8760f6e6-6c5e-4c65-854d-02d4bc3312c5',
#]
</verbatim>

Note that you still can request tape recall for whole dataset from =*AOD*= tier.

%ENDTWISTY%
```

## Comment (belforte, 2023-03-11T21:00:37Z)

Sorry. I had not noticed the first line and have independently put a description of inputBlocks in the config, param twiki. Feel free to change it. 

you should not be afraid of putting this in the twiki. We can always edit it again ! Few people if any will read unless/until we point them to it.

This is actually more than I asked for, but it is good. I think we should expand it be general FAQ about "my data is (partially) on tape (and partially on disk)".

## Comment (novicecpp, 2023-03-13T17:24:28Z)

I have updated FAQ https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#My_dataset_is_partially_on_tape, make it more general as you suggested, include how tape recall work (not sure if it too technical) and small mention to Data.partialDataset.

## Comment (belforte, 2023-03-13T17:55:23Z)

very nice thanks. But le me rephrase a bit for clarity.

## Comment (belforte, 2023-03-13T18:04:49Z)

Done. Check if you still like it. Then feel free to close.
With hindsight, 5TB is really very small, let's set config.TaskWorker.maxTierToBlockRecallSizeTB = 10

## Comment (novicecpp, 2023-03-13T18:45:53Z)

Thanks a lot for rephrasing. I will change config tomorrow and close this issue.

## Comment (novicecpp, 2023-03-14T12:11:51Z)

Done. 
https://gitlab.cern.ch/ai/it-puppet-hostgroup-vocmsglidein/-/commit/a8773a9070dc64df253c75156499653a065f328e
