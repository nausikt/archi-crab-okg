# dmwm/CRABServer issue #7626: PostJob incorrectly sets ExitCode to 50664 (WallClockLimit)

State: open
Opened: 2023-05-03T23:04:17Z
Labels: Type: Bug, Priority: Medium
URL: https://github.com/dmwm/CRABServer/issues/7626

## Opening post (belforte, 2023-05-03T23:04:17Z)

see this postjob log
https://cmsweb.cern.ch:8443/scheddmon/0194/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/postjob.82.0.txt
from task https://cmsweb.cern.ch/crabserver/ui/task/230425_152339%3Aguttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/dbver/prod
(PJ log pasted below in case it is needed one month from now)
in particular these lines which makes no sense to me

Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob Job or stageout wrapper finished with exit code 8021. Trying to determine the meaning of the exit code and if it is a recoverable or fatal error.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob New job_fjr.82.0.json file content: {"exitMsg": "Not retrying job due to wall clock limit (job automatically killed on the worker node)", "jobExitCode": 50664, "exitCode": 50664}
Mon, 01 May 2023 02:36:36 CEST(+0200):ERROR:RetryJob Original error: Job failed to open local and fallback files.
Mon, 01 May 2023 02:36:36 CEST(+0200):ERROR:RetryJob Not retrying job due to wall clock limit (job automatically killed on the worker node)

This is rare, but not isolated, see e.g. this
![image](https://user-images.githubusercontent.com/1837785/236069291-5180975f-417c-4535-bd65-e3d274e5586d.png)



<details><summary>Full log</summary>
<p>

```
Mon, 01 May 2023 02:36:34 CEST(+0200):INFO:PostJob ======== Starting execution on vocms0194.cern.ch. Task Worker Version v3.230221
Mon, 01 May 2023 02:36:34 CEST(+0200):DEBUG:PostJob Creating symbolic link in task web directory to post-job log file: /home/grid/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/postjob.82.0.txt -> postjob.82.0.txt
Mon, 01 May 2023 02:36:34 CEST(+0200):DEBUG:PostJob Copying job stdout from job_out.82 to /home/grid/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/job_out.82.0.txt.
Mon, 01 May 2023 02:36:34 CEST(+0200):DEBUG:PostJob Copying job report from jobReport.json.82 to job_fjr.82.0.json.
Mon, 01 May 2023 02:36:34 CEST(+0200):DEBUG:PostJob Creating symbolic link in task web directory to job report file: /home/grid/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/job_fjr.82.0.json -> job_fjr.82.0.json
Mon, 01 May 2023 02:36:34 CEST(+0200):INFO:PostJob This is job retry number 0. The maximum allowed number of retries is 2.
Mon, 01 May 2023 02:36:34 CEST(+0200):DEBUG:PostJob This post-job corresponds to job with Condor ID 90369867.
Mon, 01 May 2023 02:36:34 CEST(+0200):INFO:PostJob PER_JOB_HISTORY file /data/srv/glidecondor/condor_local/job_history/history.90369867.0 not found , look in ./finished_jobs
Mon, 01 May 2023 02:36:34 CEST(+0200):INFO:PostJob History file not found in ./finished_jobs. Create it by querying schedd
Mon, 01 May 2023 02:36:34 CEST(+0200):INFO:PostJob Executing condor_q -l 90369867.0 > ./finished_jobs/job.82.0
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob History file ./finished_jobs/job.82.0 created
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to parse job ad file ./finished_jobs/job.82.0.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        -----> Attempt # 0 of 1 -----
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        -----> Succeeded to parse job ad file -----
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Finished to parse job ad.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to analyze job exit status.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        -----> RetryJob log start -----
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:RetryJob Job ads already present. Will not use condor_q, but will load previous jobs ads.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob This is job retry number 0. Will not try to search and load previous job ads.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob Job or stageout wrapper finished with exit code 8021. Trying to determine the meaning of the exit code and if it is a recoverable or fatal error.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob job_fjr.82.0.json file exists and it is not empty! CRAB3 will overwrite it, because the job got FatalError
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob Old job_fjr.82.0.json file content: {"WorkerNodeInfo": {"HostName": "", "MachineFeatures": {}, "JobFeatures": {}}, "task": null, "steps": {"cmsRun": {"status": 8021, "start": null, "stop": null, "performance": {"storage": {"readCachePercentageOps": 0.0, "readTotalMB": 13470.7, "readNumOps": 443621.0, "writeTotalSecs": 0.141433, "readPercentageOps": 1.0000202875878283, "readMaxMSec": 7.13906, "readAveragekB": 31.095434195517605, "readTotalSecs": 0.0, "writeTotalMB": 233.467, "readMBSec": 3123.553663434293}, "memory": {"PeakValueVsize": "1812.56", "PeakValueRss": "1051.43"}, "cpu": {"TotalInitCPU": "4.45863", "EventThroughput": "0.0841401", "AvgEventTime": "10.4585", "TotalLoopTime": "4872.82", "TotalJobTime": "4887.04", "EventSetup Lock": "1.50204e-05", "NumberOfThreads": "1", "TotalJobCPU": "4278.79", "TotalLoopCPU": "4271.32", "NumberOfStreams": "1", "EventSetup Get": "4.16", "MaxEventTime": "25.8767", "MinEventTime": "1.63707", "TotalInitTime": "9.94694"}, "multicore": {}}, "output": {"RAWSIMoutput": [{"events": 410, "output_module_class": "PoolOutputModule", "branch_hash": "6a165b58676ed985c284d2a0353b38e8", "input": ["/store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root"], "pfn": "SIM.root", "guid": "BADC4F5F-FC8D-B04B-AB94-EFE1482929D0", "runs": {"1": {"811": 100, "812": 100, "813": 100, "814": 100, "815": 10}}, "lfn": "", "module_label": "RAWSIMoutput", "catalog": "", "inputpfns": ["root://xrootd-cms.infn.it//store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root"]}], "analysis": []}, "input": {"source": [{"input_source_class": "PoolSource", "events": 410, "pfn": "root://xrootd-cms.infn.it//store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root", "input_type": "primaryFiles", "guid": "26E10B23-F204-8E4D-B343-3BEDCFE89AC5", "runs": {"1": {"811": null, "812": null, "813": null, "814": null, "815": null}}, "lfn": "/store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root", "module_label": "source", "catalog": ""}]}, "errors": [{"type": "Fatal Exception", "details": "An exception of category 'FileReadError' occurred while\n   [0] Calling InputSource::getNextItemType\n   [1] Reading branch EventAuxiliary\n   [2] Calling XrdFile::readv()\n   [3] XrdAdaptor::ClientRequest::HandleResponse() failure while running connection recovery\n   [4] Handling XrdAdaptor::RequestManager::requestFailure()\n   [5] In XrdAdaptor::RequestManager::OpenHandler::HandleResponseWithHosts()\nException Message:\nXrdCl::File::Open(name='root://xrootd-cms.infn.it//store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root', flags=0x10, permissions=0660) => error '[ERROR] Operation expired' (errno=0, code=206)\n   Additional Info:\n      [a] Original error: '[ERROR] Operation expired' (errno=0, code=206, source=sedsk10.grid.hep.ph.ic.ac.uk:22138 (unknown site)).\n      [b] Original failed source is sedsk10.grid.hep.ph.ic.ac.uk:22138 (unknown site)\n      [c] Disabled source: sedsk10.grid.hep.ph.ic.ac.uk:22138", "exitCode": 8021}], "cleanup": {}, "parameters": {}, "site": {}, "analysis": {}, "logs": {}}}, "skippedFiles": [], "fallbackFiles": ["/store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root"], "Campaign": "", "PrepID": "", "EOSLogURL": "", "jobExitCode": 8021, "exitAcronym": "FAILED", "exitCode": 8021, "exitMsg": "Error while running CMSSW:\nFatal Exception\nAn exception of category 'FileReadError' occurred while\n   [0] Calling InputSource::getNextItemType\n   [1] Reading branch EventAuxiliary\n   [2] Calling XrdFile::readv()\n   [3] XrdAdaptor::ClientRequest::HandleResponse() failure while running connection recovery\n   [4] Handling XrdAdaptor::RequestManager::requestFailure()\n   [5] In XrdAdaptor::RequestManager::OpenHandler::HandleResponseWithHosts()\nException Message:\nXrdCl::File::Open(name='root://xrootd-cms.infn.it//store/user/guttley/ZstarTophi200A70To4Tau_ext1_LHEGEN_2016_preVFP/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1/230406_113153/0000/GEN_163.root', flags=0x10, permissions=0660) => error '[ERROR] Operation expired' (errno=0, code=206)\n   Additional Info:\n      [a] Original error: '[ERROR] Operation expired' (errno=0, code=206, source=sedsk10.grid.hep.ph.ic.ac.uk:22138 (unknown site)).\n      [b] Original failed source is sedsk10.grid.hep.ph.ic.ac.uk:22138 (unknown site)\n      [c] Disabled source: sedsk10.grid.hep.ph.ic.ac.uk:22138\n", "executed_site": "T2_DE_DESY", "phedex_node": "T2_DE_DESY"}
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:RetryJob New job_fjr.82.0.json file content: {"exitMsg": "Not retrying job due to wall clock limit (job automatically killed on the worker node)", "jobExitCode": 50664, "exitCode": 50664}
Mon, 01 May 2023 02:36:36 CEST(+0200):ERROR:RetryJob Original error: Job failed to open local and fallback files.
Mon, 01 May 2023 02:36:36 CEST(+0200):ERROR:RetryJob Not retrying job due to wall clock limit (job automatically killed on the worker node)
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        <----- RetryJob log finish ----
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob The retry handler indicated this was a fatal error.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to prepare/send report to dashboard.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to update job ClassAd.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob status: FAILED. ClassAd attributes to set are: {'CRAB_PostJobStatus': '"FAILED"', 'JobExitCode': 50664, 'ExeExitCode': 50664}
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        -----> Started attempt 1 out of 5 -----
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob        -----> Finished attempt 1 out of 5 -----
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Finished to update job ClassAd.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Finished to analyze job exit status.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to prepare error report.
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob Acquiring lock on error summary file.
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob Acquired lock on error summary file.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob 'steps' key not found in the report
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob Updating error summary for jobid 82 retry 0 with following information:
'exit code' = 50664
'exit message' = Not retrying job due to wall clock limit (job automatically killed on the worker node)
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob Writing error summary file
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob Written error summary file
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Finished to prepare error report.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Starting to prepare WMArchive report.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob WMArchiveReport.82.0.json , /data/srv/WMArchiveWD/new/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM_WMArchiveReport.82.0.json
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ====== Finished to prepare WMArchive report.
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob Will not write postjob_env.txt file. Continue.
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob ------ Job classad values for debug purposes:
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob ----------------------------------------------------------------------------------------------------
                    AccountingGroup    analysis.guttley
                          AcctGroup    analysis
                      AcctGroupUser    guttley
                          Arguments    -a sandbox.tar.gz --sourceURL=https://cmsweb.cern.ch/S3/crabcache_prod --jobNumber=82 --cmsswVersion=CMSSW_10_6_17_patch1 --scramArch=slc7_amd64_gcc700 --inputFile=job_input_file_list_82.txt --runAndLumis=job_lumis_82.json --lheInputFiles=False --firstEvent=None --firstLumi=None --lastEvent=None --firstRun=None --seeding=AutomaticSeeding --scriptExe=None --eventsPerLumi=None --maxRuntime=-60 --scriptArgs=[] -o {}
                    BlockReadKbytes    0
                         BlockReads    0
                   BlockWriteKbytes    0
                        BlockWrites    0
                ChirpCMSSWCPUModels    AMD EPYC 74F3 24-Core Processor
                  ChirpCMSSWElapsed    4874
                   ChirpCMSSWEvents    410
                    ChirpCMSSWFiles    1
ChirpCMSSWIOSite_gridhepphicacuk_ReadBytes    53321356
ChirpCMSSWIOSite_gridhepphicacuk_ReadTimeMS    381976
               ChirpCMSSWLastUpdate    1682901387
                    ChirpCMSSWLumis    5
                ChirpCMSSWMaxEvents    -1
                 ChirpCMSSWMaxFiles    2
                 ChirpCMSSWMaxLumis    2
                ChirpCMSSWReadBytes    14168755455
                  ChirpCMSSWReadOps    443621
             ChirpCMSSWReadSegments    37
            ChirpCMSSWReadTimeMsecs    200048
                 ChirpCMSSWReadVOps    8
                     ChirpCMSSWRuns    1
               ChirpCMSSWWriteBytes    244808267
           ChirpCMSSWWriteTimeMsecs    140
           Chirp_CRAB3_Job_ExitCode    8021
                          ClusterId    90369867
                                Cmd    /data/srv/glidecondor/condor_local/spool/9784/0/cluster90369784.proc0.subproc0/gWMS-CMSRunAnalysis.sh
                          CMSGroups    /cms
                 CMS_ALLOW_OVERFLOW    True
                        CMS_JobType    Analysis
                 CMS_SubmissionTool    CRAB
                       CMS_TaskType    cmsRun
                           CMS_Type    Analysis
                         CMS_WMTool    User
            CommittedSuspensionTime    0
                      CommittedTime    4917
                     CompletionDate    1682901393
                     CondorPlatform    $CondorPlatform: x86_64_CentOS7 $
                      CondorVersion    $CondorVersion: 9.1.2 Jul 29 2021 BuildID: 552044 PackageID: 9.1.2-1 $
                           CoreSize    0
                    CPUInstructions    51150711567306
                    CpusProvisioned    8
                      CRAB_AlgoArgs    {\halt_job_on_file_boundaries\: false, \splitOnRun\: false, \events_per_job\: {\halt_job_on_file_boundaries\: false, \splitOnRun\: false, \events_per_job\: 1000, \runs\: [], \lumis\: [], \algorithm\: \EventAwareLumiBased\, \total_events\: -199999, \applyLumiCorrection\: true}}
                    CRAB_ASOTimeout    86400
                     CRAB_AsyncDest    T2_UK_London_IC
                     CRAB_DataBlock    /ZstarTophi200A70To4Tau_ext1/guttley-ZstarTophi200A70To4Tau_ext1-d838e5b405163e5ad046f094b9db26e2/USER#7279d07c-3841-4a3a-a504-ede64b7f87dc
                    CRAB_DbInstance    prod
                        CRAB_DBSURL    https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader
                   CRAB_Destination    davs://gfe02.grid.hep.ph.ic.ac.uk:2880/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/guttley/SIM/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/230425_152339/0000/log/cmsRun_82.log.tar.gz, davs://gfe02.grid.hep.ph.ic.ac.uk:2880/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/guttley/SIM/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/230425_152339/0000/SIM_82.root
                            CRAB_Id    82
                           CRAB_ISB    https://cmsweb.cern.ch/S3/crabcache_prod
                       CRAB_JobArch    slc7_amd64_gcc700
                      CRAB_JobCount    200
                     CRAB_JobLogURL    https://cmsweb.cern.ch:8443/scheddmon/0194/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/job_out.82.0.txt
                         CRAB_JobSW    CMSSW_10_6_17_patch1
              CRAB_localOutputFiles    SIM.root=SIM_82.root
            CRAB_NumAutomJobRetries    2
                  CRAB_oneEventMode    0
                     CRAB_OutLFNDir    /store/user/guttley/SIM/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/230425_152339
                 CRAB_OutTempLFNDir    /store/temp/user/guttley.270659944833590f7e5973adec851d2e96c457a1/SIM/ZstarTophi200A70To4Tau_ext1/ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/230425_152339
             CRAB_PostJobLastUpdate    0
                 CRAB_PostJobLogURL    https://cmsweb.cern.ch:8443/scheddmon/0194/guttley/230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM/postjob.82.0.txt
                 CRAB_PostJobStatus    NOT RUN
                CRAB_PrimaryDataset    ZstarTophi200A70To4Tau_ext1
                       CRAB_Publish    1
                 CRAB_PublishDBSURL    https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter
                   CRAB_PublishName    ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM-00000000000000000000000000000000
                       CRAB_ReqName    230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM
                      CRAB_RestHost    cmsweb.cern.ch:8443
                         CRAB_Retry    0
            CRAB_RetryOnASOFailures    1
                  CRAB_SaveLogsFlag    1
                     CRAB_SplitAlgo    EventAwareLumiBased
                CRAB_StageoutPolicy    local,remote
               CRAB_SubmitterIpAddr    188.185.89.194
                   CRAB_TaskEndTime    1685028219
              CRAB_TaskLifetimeDays    30
                    CRAB_TaskWorker    crab-prod-tw01
               CRAB_TransferOutputs    1
                        CRAB_UserDN    /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=guttley/CN=846010/CN=George Peter Uttley
                     CRAB_UserGroup    undefined
                        CRAB_UserHN    guttley
                      CRAB_UserRole    undefined
                      CRAB_Workflow    230425_152339:guttley_crab_ZstarTophi200A70To4Tau_ext1_2016_preVFP_SIM
           CumulativeSuspensionTime    0
                       CurrentHosts    0
                        DAGManJobId    90369784
                     DAGManNodesLog    /data/srv/glidecondor/condor_local/spool/9784/0/cluster90369784.proc0.subproc0/RunJobs.dag.nodes.log
                    DAGManNodesMask    0,1,2,4,5,7,9,10,11,12,13,16,17,24,27,35,36
                        DAGNodeName    Job82
                 DAGParentNodeNames    
                      DESIRED_Archs    X86_64
           DESIRED_CMSDataLocations    T2_UK_London_IC,T3_UK_London_QMUL,T3_UK_London_RHUL,T3_UK_SGrid_Oxford,T3_UK_ScotGrid_GLA
                 DESIRED_CMSDataset    /ZstarTophi200A70To4Tau_ext1/guttley-ZstarTophi200A70To4Tau_ext1-d838e5b405163e5ad046f094b9db26e2/USER
                      DESIRED_SITES    T1_DE_KIT,T1_ES_PIC,T1_FR_CCIN2P3,T1_IT_CNAF,T1_RU_JINR,T1_UK_RAL,T1_US_FNAL,T2_AT_Vienna,T2_BE_IIHE,T2_BE_UCL,T2_BR_SPRACE,T2_BR_UERJ,T2_CH_CERN,T2_CH_CSCS,T2_DE_DESY,T2_DE_RWTH,T2_EE_Estonia,T2_ES_CIEMAT,T2_ES_IFCA,T2_FI_HIP,T2_FR_GRIF_IRFU,T2_FR_IPHC,T2_HU_Budapest,T2_IT_Bari,T2_IT_Legnaro,T2_IT_Pisa,T2_IT_Rome,T2_KR_KISTI,T2_PK_NCP,T2_PL_Cyfronet,T2_PL_Swierk,T2_RU_IHEP,T2_RU_INR,T2_RU_ITEP,T2_RU_JINR,T2_TR_METU,T2_TW_NCHC,T2_UK_London_IC,T2_UK_SGrid_Bristol,T2_UK_SGrid_RALPP,T2_US_Caltech,T2_US_Florida,T2_US_MIT,T2_US_Nebraska,T2_US_Purdue,T2_US_UCSD,T2_US_Vanderbilt,T2_US_Wisconsin,T3_CH_CERN_DOMA,T3_CN_THU,T3_ES_Oviedo,T3_ES_PIC_BSC,T3_HU_Debrecen,T3_IN_IOPB,T3_IT_Bologna,T3_IT_Perugia,T3_IT_Trieste,T3_KR_KNU,T3_MX_Cinvestav,T3_RU_MEPhI,T3_TW_NCU,T3_UK_London_QMUL,T3_UK_London_RHUL,T3_UK_ScotGrid_GLA,T3_US_Baylor,T3_US_Colorado,T3_US_FIT,T3_US_FNALLPC,T3_US_FNALWILSON,T3_US_ORNL,T3_US_OSU,T3_US_PuertoRico,T3_US_Rice,T3_US_UMD,T3_US_VC3_NotreDame
                    DiskProvisioned    1516589
                          DiskUsage    250000
                      DiskUsage_RAW    244608
               EnteredCurrentStatus    1682901393
                        Environment    SCRAM_ARCH=slc7_amd64_gcc700 CRAB_RUNTIME_TARBALL=local CRAB_TASKMANAGER_TARBALL=local
                                Err    job_err.82
              EstimatedWallTimeMins    1250
                     ExecutableSize    10
                 ExecutableSize_RAW    8
                           ExitCode    85
                         ExitStatus    0
                        GlobalJobId    crab3@vocms0194.cern.ch#90369867.0#1682436369
                          ImageSize    7500000
                      ImageSize_RAW    5662096
                                 In    /dev/null
                                Iwd    /data/srv/glidecondor/condor_local/spool/9784/0/cluster90369784.proc0.subproc0
              JobAdInformationAttrs    MATCH_EXP_JOBGLIDEIN_CMSSite, JOBGLIDEIN_CMSSite, RemoteSysCpu, RemoteUserCpu
                         JobBatchId    90369784.0
                       JobBatchName    RunJobs.dag+90369784
  JobCurrentFinishTransferInputDate    1682896498
 JobCurrentFinishTransferOutputDate    1682901392
                JobCurrentStartDate    1682896476
       JobCurrentStartExecutingDate    1682896498
   JobCurrentStartTransferInputDate    1682896498
  JobCurrentStartTransferOutputDate    1682901392
                JobDisconnectedDate    1682892431
                JobFinishedHookDone    1682901393
                 JOBGLIDEIN_CMSSite    $$([ifThenElse(GLIDEIN_CMSSite is undefined, \Unknown\, GLIDEIN_CMSSite)])
                   JobLastStartDate    1682817679
                   JobLeaseDuration    2400
                    JobNotification    0
                            JobPrio    10
                        JobRunCount    2
                       JobStartDate    1682817679
                          JobStatus    4
                        JobUniverse    5
                        JOB_CMSSite    $$(GLIDEIN_CMSSite:Unknown)
               JOB_GLIDECLIENT_Name    $$(GLIDECLIENT_Name:Unknown)
              JOB_GLIDEIN_ClusterId    $$(GLIDEIN_ClusterId:Unknown)
                JOB_GLIDEIN_CMSSite    $$(GLIDEIN_CMSSite:Unknown)
             JOB_GLIDEIN_Entry_Name    $$(GLIDEIN_Entry_Name:Unknown)
                JOB_GLIDEIN_Factory    $$(GLIDEIN_Factory:Unknown)
           JOB_GLIDEIN_Job_Max_Time    $$(GLIDEIN_Job_Max_Time:Unknown)
              JOB_GLIDEIN_MaxMemMBs    $$(GLIDEIN_MaxMemMBs:Unknown)
           JOB_GLIDEIN_Max_Walltime    $$(GLIDEIN_Max_Walltime:Unknown)
                 JOB_GLIDEIN_Memory    $$(Memory:Unknown)
                   JOB_GLIDEIN_Name    $$(GLIDEIN_Name:Unknown)
                 JOB_GLIDEIN_ProcId    $$(GLIDEIN_ProcId:Unknown)
                 JOB_GLIDEIN_Schedd    $$(GLIDEIN_Schedd:Unknown)
                    JOB_GLIDEIN_SEs    $$(GLIDEIN_SEs:Unknown)
                   JOB_GLIDEIN_Site    $$(GLIDEIN_Site:Unknown)
                JOB_GLIDEIN_SiteWMS    $$(GLIDEIN_SiteWMS:Unknown)
          JOB_GLIDEIN_SiteWMS_JobId    $$(GLIDEIN_SiteWMS_JobId:Unknown)
          JOB_GLIDEIN_SiteWMS_Queue    $$(GLIDEIN_SiteWMS_Queue:Unknown)
           JOB_GLIDEIN_SiteWMS_Slot    $$(GLIDEIN_SiteWMS_Slot:Unknown)
                  JOB_GLIDEIN_ToDie    $$(GLIDEIN_ToDie:Unknown)
               JOB_GLIDEIN_ToRetire    $$(GLIDEIN_ToRetire:Unknown)
                           JOB_Site    $$(GLIDEIN_Site:Unknown)
                LastJobLeaseRenewal    1682901392
                      LastJobStatus    2
                      LastMatchTime    1682896476
                  LastPublicClaimId    <131.169.165.2:42694?CCBID=128.142.194.25:9618%3faddrs%3d[2001-1458-301-cd--100-364]-9618+128.142.194.25-9618%26alias%3dvocms0813.cern.ch%26noUDP%26sock%3dcollector9673#6973471%20131.225.189.210:9618%3faddrs%3d[2620-6a-0-8421--cd]-9618+131.225.189.210-9618%26alias%3dcmssrvz03.fnal.gov%26noUDP%26sock%3dcollector9679#5548927&PrivNet=batch1402.desy.de&addrs=[2001-638-700-10a0--1-502]-42694+131.169.165.2-42694&alias=batch1402.desy.de&noUDP>#1682840172#3#...
                 LastRejMatchReason    no match found 
                   LastRejMatchTime    1682896424
                     LastRemoteHost    slot1_1@glidein_84497_41168400@batch1402.desy.de
                 LastSuspensionTime    0
  MachineAttrCMSProcessingSiteName0    T2_DE_DESY
         MachineAttrCMSSubSiteName0    undefined
                   MachineAttrCpus0    8
         MachineAttrCUDACapability0    undefined
           MachineAttrCUDAClockMhz0    undefined
       MachineAttrCUDAComputeUnits0    undefined
         MachineAttrCUDACoresPerCU0    undefined
         MachineAttrCUDADeviceName0    undefined
      MachineAttrCUDADriverVersion0    undefined
         MachineAttrCUDAECCEnabled0    undefined
     MachineAttrCUDAGlobalMemoryMb0    undefined
       MachineAttrMJF_JOB_HS06_JOB0    Unknown
             MachineAttrSlotWeight0    8
          MachineAttrTotalSlotCpus0    8
       MATCH_EXP_JOBGLIDEIN_CMSSite    T2_DE_DESY
              MATCH_EXP_JOB_CMSSite    T2_DE_DESY
     MATCH_EXP_JOB_GLIDECLIENT_Name    CMSG-v1_0.main-token
    MATCH_EXP_JOB_GLIDEIN_ClusterId    7267461
      MATCH_EXP_JOB_GLIDEIN_CMSSite    T2_DE_DESY
   MATCH_EXP_JOB_GLIDEIN_Entry_Name    CMSHTPC_T2_DE_DESY_grid-htcondorce2
      MATCH_EXP_JOB_GLIDEIN_Factory    CERN-Prod
 MATCH_EXP_JOB_GLIDEIN_Job_Max_Time    14400
    MATCH_EXP_JOB_GLIDEIN_MaxMemMBs    20000
 MATCH_EXP_JOB_GLIDEIN_Max_Walltime    171000
       MATCH_EXP_JOB_GLIDEIN_Memory    15000
         MATCH_EXP_JOB_GLIDEIN_Name    gfactory_instance
       MATCH_EXP_JOB_GLIDEIN_ProcId    0
       MATCH_EXP_JOB_GLIDEIN_Schedd    schedd_glideins4@vocms0207.cern.ch
          MATCH_EXP_JOB_GLIDEIN_SEs    Unknown
         MATCH_EXP_JOB_GLIDEIN_Site    DESY
      MATCH_EXP_JOB_GLIDEIN_SiteWMS    HTCondor
MATCH_EXP_JOB_GLIDEIN_SiteWMS_JobId    843846.0
MATCH_EXP_JOB_GLIDEIN_SiteWMS_Queue    grid-htcondorce2.desy.de
 MATCH_EXP_JOB_GLIDEIN_SiteWMS_Slot    slot1_1@batch1402.desy.de
        MATCH_EXP_JOB_GLIDEIN_ToDie    1683006648
     MATCH_EXP_JOB_GLIDEIN_ToRetire    1682992248
                 MATCH_EXP_JOB_Site    DESY
          MATCH_EXP_Used_Gatekeeper    grid-htcondorce2.desy.de grid-htcondorce2.desy.de:9619
             MATCH_GLIDECLIENT_Name    CMSG-v1_0.main-token
            MATCH_GLIDEIN_ClusterId    7267461
              MATCH_GLIDEIN_CMSSite    T2_DE_DESY
           MATCH_GLIDEIN_Entry_Name    CMSHTPC_T2_DE_DESY_grid-htcondorce2
              MATCH_GLIDEIN_Factory    CERN-Prod
           MATCH_GLIDEIN_Gatekeeper    grid-htcondorce2.desy.de grid-htcondorce2.desy.de:9619
         MATCH_GLIDEIN_Job_Max_Time    14400
            MATCH_GLIDEIN_MaxMemMBs    20000
         MATCH_GLIDEIN_Max_Walltime    171000
                 MATCH_GLIDEIN_Name    gfactory_instance
               MATCH_GLIDEIN_ProcId    0
               MATCH_GLIDEIN_Schedd    schedd_glideins4@vocms0207.cern.ch
                  MATCH_GLIDEIN_SEs    Unknown
                 MATCH_GLIDEIN_Site    DESY
              MATCH_GLIDEIN_SiteWMS    HTCondor
        MATCH_GLIDEIN_SiteWMS_JobId    843846.0
        MATCH_GLIDEIN_SiteWMS_Queue    grid-htcondorce2.desy.de
         MATCH_GLIDEIN_SiteWMS_Slot    slot1_1@batch1402.desy.de
                MATCH_GLIDEIN_ToDie    1683006648
             MATCH_GLIDEIN_ToRetire    1682992248
                       MATCH_Memory    15000
                           MaxHosts    1
                    MaxWallTimeMins    1250
                 MaxWallTimeMinsRun    1250
                MaxWallTimeMins_RAW    1250
                  MemoryProvisioned    15104
                           MinHosts    1
                             MyType    Job
                           NumCkpts    0
                       NumCkpts_RAW    0
                  NumJobCompletions    1
                      NumJobMatches    2
                       NumJobStarts    2
                        NumRestarts    0
                    NumShadowStarts    2
                     NumSystemHolds    0
                       OrigMaxHosts    1
                                Out    job_out.82
                              Owner    crabtw
                       PostJobPrio1    -1682436313
                       PostJobPrio2    0
                        PreJobPrio1    1
                             ProcId    0
              ProportionalSetSizeKb    1250000
          ProportionalSetSizeKb_RAW    1078650
                              QDate    1682436369
              RecentBlockReadKbytes    0
                   RecentBlockReads    0
             RecentBlockWriteKbytes    0
                  RecentBlockWrites    0
         RecentStatsLifetimeStarter    1200
                       RemoveReason    Removed due to wall clock limit
                        RequestCpus    8
                        RequestDisk    100000
                    RequestDisk_RAW    1
                      RequestMemory    15000
                  RequestMemory_RAW    15000
                        REQUIRED_OS    rhel7
                    ResidentSetSize    1250000
                ResidentSetSize_RAW    1094056
                            RootDir    /
                ScratchDirFileCount    1157
                         ServerTime    1682901394
                ShouldTransferFiles    YES
                 SpooledOutputFiles    jobReport.json.82,WMArchiveReport.json.82
                    StartdPrincipal    execute-side@matchsession/2001:638:700:10a0::1:502
               StatsLifetimeStarter    4894
                   SubmitEventNotes    DAG Node: Job82
                         TargetType    Machine
                           TaskType    Job
                   TotalSubmitProcs    1
                   TotalSuspensions    0
                 TransferInFinished    1682896498
                      TransferInput    CMSRunAnalysis.sh,cmscp.py,CMSRunAnalysis.tar.gz,sandbox.tar.gz,run_and_lumis.tar.gz,input_files.tar.gz,submit_env.sh
                TransferInputSizeMB    0
                  TransferInStarted    1682896498
                TransferOutFinished    1682901392
                     TransferOutput    jobReport.json.82,WMArchiveReport.json.82
                 TransferOutStarted    1682901392
                    Used_Gatekeeper    $$(GLIDEIN_Gatekeeper:Unknown)
                               User    crabtw@cms
                            UserLog    /data/srv/glidecondor/condor_local/spool/9784/0/cluster90369784.proc0.subproc0/job_log
               WhenToTransferOutput    ON_EXIT_OR_EVICT
                      x509userproxy    /data/srv/glidecondor/condor_local/spool/9784/0/cluster90369784.proc0.subproc0/70bb58faa3b4a3ae1e011071b2ba800f7b39570c
                 x509UserProxyEmail    george.peter.uttley@cern.ch
            x509UserProxyExpiration    1682949313
             x509UserProxyFirstFQAN    /cms/Role=NULL/Capability=NULL
                  x509UserProxyFQAN    /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=guttley/CN=846010/CN=George Peter Uttley,/cms/Role=NULL/Capability=NULL
               x509userproxysubject    /DC=ch/DC=cern/OU=Organic Units/OU=Users/CN=guttley/CN=846010/CN=George Peter Uttley
                x509UserProxyVOName    cms
Mon, 01 May 2023 02:36:36 CEST(+0200):DEBUG:PostJob ----------------------------------------------------------------------------------------------------
Mon, 01 May 2023 02:36:36 CEST(+0200):INFO:PostJob ********************************************************************************
======== Finished post-job execution with status code 2  : NON-RECOVERABLE JOB FAIL. No retries
Ended TaskManagerBootstrap with code 2

```

</p>
</details>

## Comment (belforte, 2023-05-03T23:22:02Z)

same for exit code 50660
from e.g. https://cmsweb.cern.ch:8443/scheddmon/0107/idutta/230427_194025:idutta_crab_PrivateProduction_Fall17_DR_step2_ggHH_BM8_JHEP04_batch1_v1/postjob.7319.2.txt

Fri, 28 Apr 2023 06:27:04 CEST(+0200):INFO:RetryJob New job_fjr.7319.2.json file content: {"exitMsg": "Not retrying job due to excessive memory use (2080 MB vs 2000 MB requested)", "jobExitCode": 50660, "exitCode": 50660}
Fri, 28 Apr 2023 06:27:04 CEST(+0200):ERROR:RetryJob Original error: Job failed to open local and fallback files.
Fri, 28 Apr 2023 06:27:04 CEST(+0200):ERROR:RetryJob Not retrying job due to excessive memory use (2080 MB vs 2000 MB requested)

looks like PJ wrongly overrides a correct exit code becasue accidentally memory usage is close to limit ?
