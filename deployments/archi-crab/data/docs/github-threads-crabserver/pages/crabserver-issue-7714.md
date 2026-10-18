# dmwm/CRABServer issue #7714: Parsing "ddm_quota" error in DBSDataDiscovery's taperecall

State: closed
Opened: 2023-07-05T06:54:27Z
Closed: 2023-08-17T10:18:40Z
Labels: Type: Bug, Status: Done, Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/7714

## Opening post (novicecpp, 2023-07-05T06:54:27Z)

Error I accidentially found in TW:
```
2023-07-05 07:49:18,260:DEBUG:Worker,120:Process-5: SUBMIT work on 230705_054818:alebihan_crab_WJetsToLNu_HT-400To600_recovery_2 completed in 15 seconds: Status: ERROR
Error = Problem handling 230705_054818:alebihan_crab_WJetsToLNu_HT-400To600_recovery_2 because of invalid literal for int() with base 10: '0.1394' failure, traceback follows
Traceback (most recent call last):
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/Handler.py", line 85, in executeAction
    output = work.execute(nextinput, task=self._task, tempDir=self.tempDir)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 103, in execute
    result = self.executeInternal(*args, **kwargs)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 332, in executeInternal
    self.requestTapeRecall(dataToRecall=dataToRecall, sizeToRecall=totalSizeBytes,
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 434, in requestTapeRecall
    self.requestRucioTapeRecall(dataToRecall, sizeToRecall, tapeLocations, msgHead=msg)
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 490, in requestRucioTapeRecall
    (RSE_EXPRESSION, grouping) = self.whereToRecall(
  File "/data/srv/TaskManager/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/slc7_amd64_gcc630/cms/crabtaskworker/v3.230616-6cb8f108e2d006dcaad44b2b98777a25/lib/python3.8/site-packages/TaskWorker/Actions/DBSDataDiscovery.py", line 560, in whereToRecall
    availableSpace = int(rucio.list_rse_attributes(rse)['ddm_quota'])  # bytes
ValueError: invalid literal for int() with base 10: '0.1394'
```
It cause by `rucio.list_rse_attributes(rse)['ddm_quota']` is a string and it can return floating point value which break `int()` function.

https://github.com/dmwm/CRABServer/blob/1223cef3f046f392c9bb7001c422f354024ae99d/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L560

This is easy to fix by replace with `int(float(rucio.list_rse_attributes(rse)['ddm_quota']))`.


But, I did not see where `freeRSEs` is used in `WhereToRecall` method. Maybe should replace `largeRSEs` at [line 576](https://github.com/dmwm/CRABServer/blob/1223cef3f046f392c9bb7001c422f354024ae99d/src/python/TaskWorker/Actions/DBSDataDiscovery.py#L560)?
And `freeRSEs` can be empty because all T1/T2 sites (except T2_GR_Ioannina is on the blacklist) reported ddm_quota less than 1,see below.

![Screenshot from 2023-07-05 08-41-03](https://github.com/dmwm/CRABServer/assets/2346664/8ecb9125-3a50-4180-a9d5-e46c382af9f6)

I leave this to @belforte hand to decide how to fix it.

## Comment (belforte, 2023-07-05T08:22:54Z)

Thanks Wa..
It looks like they changed ddm_quota in Rucio from number of bytes to a fracion (of total ?). Surely for good reasons. And as usual w/o asking if someone else was using this by any chance, @dciangot @dynamic-entropy @ericvaandering please remember us next time :-) 
Sorry Eric, I know that from Rucio developers POV ddm_quota is a custom attribute configured by CMS and Rucio does not care and it is for CMS Rucio Ops to rule.. .but I do not know who exactly "Rucio Ops" is, i.e. who takes decisions on this, so am hoping that in such cases they consult with CMS Rucio Developers. 

Useless complains aside, it is likely that `freeRSEs` is simply a leftover of some initial  implementation, in the end.. why not let Rucio decide where there is space and where not ? `largeRSE` is there as just another example of blacklisting unreliable sites w/o naming them explicitly. But `freeRSEs` ?

I will check history to be sure before I remove this freeRSEs.

## Comment (dynamic-entropy, 2023-07-05T08:31:27Z)

Hello @belforte 
Yes, I changed these numbers to percentages. If it is quicker for you to fix, I will let you go ahead or I can convert them back to integers.

I am not sure, why you are using this as a number at all. All you should be doing is specifying it as weight in a rule.

## Comment (belforte, 2023-07-05T08:31:58Z)

once upon a time I was telling Rucio to scatter largish datasets (>50 TB) in multiple sites and to avoid multiple to be many, I was sending a short list of RSE's (handful usually) so had to make sure that those had quota available.
Then two things happened:
1) old useless rules were removed and we stopped having sites with >90% locked space
2) we decided to use grouping=ALL for all datasets, and leave it to Rucio to pick the one RSE

Everything clear.

## Comment (belforte, 2023-07-05T08:34:48Z)

thanks @dynamic-entropy , I hope my last comment explains why we were using this explicly, in addition to using it as a weight. In current implementation we do not need it. And will remove this part.

@novicecpp I would expect that this fully breaks tapeRecall and we need to fix immediately. No ?

## Comment (belforte, 2023-07-05T08:37:11Z)

@dynamic-entropy when did you do this change ?

## Comment (dynamic-entropy, 2023-07-05T08:42:26Z)

Okay, now the ddm_quotas are back to integers

@belforte 3 June (the day before yesterday).

## Comment (belforte, 2023-07-05T09:00:39Z)

> @belforte 3 June (the day before yesterday).

no new TapeRecall request from CRAB since July 3rd, noon. So I guess it was lethal indeed.
We'll push a change on our side ASAP so you will be free to use and set ddm_quota the way which is better for you
I am at fault for having looked at the value and written the code w/o proper handshacking.

## Comment (belforte, 2023-07-05T09:01:29Z)

and these are the timestamps of CRAB tasks which failed to be submitted becasue of the 'invalid literal' error
```
230703_193615
230703_195125
230704_050134
230704_070854
230704_070912
230704_070931
230704_070949
230704_071008
230704_071450
230704_071655
230704_074022
230704_081502
230704_102617
230704_115433
230704_125812
230704_145650
230704_153604
230704_153702
230704_153717
230704_153744
230704_153801
230704_153812
230704_153923
230704_154653
230704_195830
230704_195926
230704_234841
230705_022314
230705_031633
230705_051220
230705_053746
230705_054818
230705_080056
230705_080423
```

raising priority to ciritcal

## Comment (belforte, 2023-07-05T09:09:36Z)

@novicecpp please have a quick look at my PR #7715 in case I missed something obvious, then I think you can tag/build/deploy. Since `freeRSEs` was not used, removing it should be pretty safe !

## Comment (belforte, 2023-07-05T09:11:08Z)

thanks @dynamic-entropy !!

## Comment (belforte, 2023-07-06T07:56:15Z)

@novicecpp did you find a problem ?

## Comment (novicecpp, 2023-07-06T08:02:44Z)

No, so far so good. But keep it open until we deploy on production. 
It will be serious error if Rahul decide to change back to percentages later.

## Comment (belforte, 2023-07-08T15:55:52Z)

change in new tag was [extensively tested](https://github.com/dmwm/CRABServer/releases/tag/v3.230705) (I was worried by CMSRunAnalysis.py cleanup)
Let'd deploy on production on Monday

## Comment (belforte, 2023-08-17T10:18:40Z)

Production TaskWorker has been running with this (acutally with following tag [v3.230714](https://github.com/dmwm/CRABServer/releases/tag/v3.230714) since  while now.
