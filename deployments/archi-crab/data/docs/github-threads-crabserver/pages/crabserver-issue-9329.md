# dmwm/CRABServer issue #9329: automatically fail publication when migrations are stuck

State: closed
Opened: 2026-06-23T17:44:48Z
Closed: 2026-06-26T10:01:06Z
Labels: Priority: TOP
URL: https://github.com/dmwm/CRABServer/issues/9329

## Opening post (belforte, 2026-06-23T17:44:48Z)

We keep having situations where migrations permanently fail no matter how many times we retry them, and there is no hope that the problem get fixed in DBS.

So we need to add code to identify when a migration fail for e.g. > N days and in that case record the failing block and from that point on set as publication failed all files which require that parent.
Hopefully we do not need to blacklist tasks.

## Comment (belforte, 2026-06-23T17:52:58Z)

e.g. here's a block which is failing migration at least since May 1st
```console
[crab3@crab-prod-tw01 migrations]$ grep "/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258" TerminallyFailedLog.txt |head -2
6513736,2026-05-01,00:21:10,/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258,260413_175924:jroloff_crab_run2025G_Apr26_v11
6513736,2026-05-01,00:21:10,/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258,260403_172046:jroloff_crab_run2025G_Apr26_v3
[crab3@crab-prod-tw01 migrations]$ grep "/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258" TerminallyFailedLog.txt |tail -2
7580916,2026-06-23,19:22:17,/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258,260604_155205:jroloff_crab_run2025G_June26_pileup_run397954_noGRL_v4
7581033,2026-06-23,19:29:25,/JetMET0/Run2025G-PromptReco-v1/AOD#2149f597-8e88-4195-b9b9-5633d8ba6258,260602_135945:jroloff_crab_run2025G_June26_pileup_run398903_noGRL
[crab3@crab-prod-tw01 migrations]$ 

```

## Comment (belforte, 2026-06-24T08:18:35Z)

in the end we'll need to have a place where score is kept which is used by all TaskPublish scripts. Time for SQLite ? Is that something you know how to use already @nausikt ?

## Comment (belforte, 2026-06-24T12:42:23Z)

The way Publisher design is, there is no relation between individual files to be published and single parent blocks, so the only thing that I can do is that when a migration is deemed beyond salvation, all the current files in input to TaskPublish are marked as failed.
i.e. `raise CannotMigrateException` inside `migrateByBlockDBS3` in [PublisherDbsUtils](https://github.com/dmwm/CRABServer/blob/846d2725e7599183dea5563748b756a1e4fdb79f/src/python/Publisher/PublisherDbsUtils.py#L326) so that TaskPublish falls through:
https://github.com/dmwm/CRABServer/blob/846d2725e7599183dea5563748b756a1e4fdb79f/src/python/Publisher/TaskPublish.py#L197-L204
and similarly for TaskPublishRucio, thought code is structured a bit differently
https://github.com/dmwm/CRABServer/blob/846d2725e7599183dea5563748b756a1e4fdb79f/src/python/Publisher/TaskPublishRucio.py#L90-L98

## Comment (belforte, 2026-06-24T17:25:47Z)

first crude implementation in my branch https://github.com/belforte/CRABServer/tree/stop-trying-failing-migrations-9329
