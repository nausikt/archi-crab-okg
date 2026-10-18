# dmwm/CRABServer issue #9379: Wrong message from TW when site with USER data is blacklisted

State: open
Opened: 2026-08-07T10:41:26Z
URL: https://github.com/dmwm/CRABServer/issues/9379

## Opening post (belforte, 2026-08-07T10:41:26Z)

e.g. https://cmsweb.cern.ch/crabserver/ui/task/260806_145805%3Abibehera_crab_NeNe_v0pT_V0_weff_v1_IP10
shows this taskWarningMs

> The CRAB server backend refuses to send jobs to the Grid scheduler. No locations found for dataset /IonPhysics10/bibehera-2pc_NeNe25_V0_v1_IP10-270449d3132be18177651c80f5f48d72/USER. (or at least for what passed the lumi-mask and/or run-range selection). Use `crab checkdataset` command to find block locations and compare with your black/white list Found 5 (out of 5) blocks present only at blacklisted not-whitelisted, and/or non-accelerator sites. Global blacklist contain these T1/T2: ['T2_CN_Beijing', 'T2_PT_NCG_Lisbon', 'T2_US_Nebraska', 'T2_GR_Ioannina', 'T2_RU_IHEP', 'T2_LV_HPCNET', 'T2_AT_Vienna', 'T2_RU_INR', 'T2_CH_CERN_P5', 'T2_PL_Swierk', 'T2_FR_GRIF', 'T2_US_Vanderbilt', 'T2_PK_NCP', 'T2_RU_ITEP', 'T2_CH_CERN_HLT', 'T2_TW_NCHC'] and 41 T3's Full list at https://cmssst.web.cern.ch/cmssst/analysis/usableSites.json 

But the real cause is that the input dataset is in Phys03 and [located at T2_US_Vanderbilt](https://cmsweb.cern.ch/das/request?instance=prod/phys03&input=origin_site+dataset%3D%2FIonPhysics0%2Fbibehera-2pc_NeNe25_V0_v1_IP0-270449d3132be18177651c80f5f48d72%2FUSER) which was in downtime when the task was submitted (as shown in the Global blacklist).

The TaskWorker did everything correctly, found location in DBS/Phys03, prepared the jobs, and when submitting compared the deisred sites for each block of jobs (only Vanderbilt here) with the blacklist and refused to submit.

But the message fails to convey this.

Message is OK for datasets in DBS/Global with locations in Rucio. so we need to be careful not to break that part.
