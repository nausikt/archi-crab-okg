# dmwm/CRABServer issue #9241: make monit_recallquota scripts more robust

State: closed
Opened: 2025-12-08T11:04:59Z
Closed: 2025-12-12T17:34:58Z
Labels: Type: Enhancement
URL: https://github.com/dmwm/CRABServer/issues/9241

## Opening post (belforte, 2025-12-08T11:04:59Z)

We keep getting mails like the following from
`Cron <crab3@crab-dev-tw02> export loguuid=$(uuidgen); test -f /home/crab3/runContainer.sh && bash /home/crab3/runContainer.sh -v v3.latest -s TaskWorker_monit_reportrecallquota -u ${loguuid} -c 'python3 /data/srv/monit/ReportRecallQuota.py' >/dev/null 2>&1 ; [ -f /tmp/monit-${loguuid}.txt ] && cat /tmp/monit-${loguuid}.txt`

Is the script really failing due to a non-catched exception (But we are supposed to catch all HTTP exceptions and retry) ?
Or simply retry works, but we still get the exception printout on stderr and so it becomes a spam ?


```
Starting new HTTPS connection (1): cms-rucio-auth.cern.ch:443
[https://cms-rucio-auth.cern.ch:443](https://cms-rucio-auth.cern.ch/) "GET /auth/x509 HTTP/1.1" 200 0
Starting new HTTP connection (1): cms-rucio.cern.ch:80
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /ping HTTP/1.1" 200 21
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch/']"
NeedRegenerationException
no value, waiting for create lock
value creation lock <dogpile.cache.region.CacheRegion._LockWrapper object at 0x7f859e458c40> acquired
No value present for key: "host_to_choose_choice['http://cms-rucio.cern.ch/']"
Calling creation function for not-yet-present value
Cache value generated in 0.000 seconds for key(s): "host_to_choose_choice['http://cms-rucio.cern.ch/']"
Released creation lock
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /accounts/whoami HTTP/1.1" 303 209
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /accounts/crab_server HTTP/1.1" 200 226
rucio client initialized: {'version': '38.5.1'} {'status': 'ACTIVE', 'account_type': 'SERVICE', 'suspended_at': None, 'created_at': '2020-04-29T15:40:28', 'updated_at': '2020-04-29T15:40:28', 'account': 'crab_server', 'email': '[Stefano.Belforte@cern.ch](mailto:Stefano.Belforte@cern.ch)', 'deleted_at': None}
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/?activity=Analysis+TapeRecall HTTP/1.1" 200 None
Starting new HTTP connection (2): cms-rucio.cern.ch:80
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/93e1f860ec2349478ba73868c432eb35 HTTP/1.1" 200 1118
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024H-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/e33ea846cae14d6988e9b091287060e6 HTTP/1.1" 200 1118
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024C-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/68317730e70047cd8962dc280c45bc24 HTTP/1.1" 200 1116
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024E-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/2a0ec244c2ee48499f930112fcb0f924 HTTP/1.1" 200 1114
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024E-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/cfe3d597ca6c46c9b6bc7def723379cd HTTP/1.1" 200 1120
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024F-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/36f6ff902da644999ebd4d69ad1de8ba HTTP/1.1" 200 1076
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024G-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/68e64c8071e8446a8d05307962a0a2a1 HTTP/1.1" 200 1119
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024I-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/5dec1b62f50547b2b080204aad73f291 HTTP/1.1" 200 1076
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024F-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/21594b3b5b404e7a84da3ab6e5383e60 HTTP/1.1" 200 1144
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FCosmics%2FRun2022E-CosmicSP-PromptReco-v1%2FRAW-RECO/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/be4a33f19c9b498fa3ded2f227ec19f8 HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024I-EXOSoftDisplacedVertices-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/7be04d7cc9bb49fa9fa6d68c14ab08d8 HTTP/1.1" 200 1251
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYJetsToMuMu_H2ErratumFix_PDFExt_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/e7eab09a4b8b4db1a9ceb03953a1f4f6 HTTP/1.1" 200 1259
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8%2FRunIISummer16MiniAODv3-PUMoriond17_plus10percentMaterial_94X_mcRun2_asymptotic_v3-v2%2FMINIAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/1d7009b9588f4eb39492fb6c060b1a33 HTTP/1.1" 200 1461
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYJetsToMuMu_H2ErratumFix_PDFExt_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos%2FRunIISummer20UL17RECO-106X_mc2017_realistic_v6-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/0a2f29da7a5e4c058783f921f107050d HTTP/1.1" 200 1114
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024B-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/70f6bc9e8b9041cb9e38bc2ceeebbf05 HTTP/1.1" 200 1117
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024E-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/353c7e70d0c443a68c0310d897e99ba0 HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/5e851d638b2c446998f4583f5f1ecbcd HTTP/1.1" 200 1119
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024D-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/dbfba49ed04f4a65bd2f402a536861da HTTP/1.1" 200 1113
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024C-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/5cf897ee15d74d879725117940af93ad HTTP/1.1" 200 1134
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FPAMinimumBias5%2FPARun2016C-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/61ff6f5234e54dc192616cbdf3467ed3 HTTP/1.1" 200 1117
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024F-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/8d0d06a7a8d84fa789f7a6a6baf800ef HTTP/1.1" 200 1136
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FPAMinimumBias5%2FPARun2016C-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/39785b9626e5466a877499b4c17eceef HTTP/1.1" 200 1116
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024H-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/f2af2b93f65e4d12b010ed8410f92499 HTTP/1.1" 200 1135
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FZeroBias%2FRun2016H-21Feb2020_UL2016-v1%2FMINIAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/64242b116ba44a48865a0d05e2aedca4 HTTP/1.1" 200 1076
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024G-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/b43af0c9de774537a2e37a196074139a HTTP/1.1" 200 1326
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024E-EXOSoftDisplacedVertices-2024CDEReprocessing-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/f378aa704294478187dc1ddb9e6a0cb1 HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024H-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/a54a73e66e9c44f586f98cd17d84f8fa HTTP/1.1" 200 1677
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FQCD_Bin-Pt-80to120_TuneCP5_13p6TeV_pythia8%2FRun3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2%2FGEN-SIM-RAW/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/c0014137dea2420888fb00f6459fded9 HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024H-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/76794c813b8743baa6a7cae3456ec35c HTTP/1.1" 200 1222
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYTo2L_Bin-M-50_TuneCP5_14TeV_pythia8%2FPhase2Spring24GS-140X_mcRun4_realistic_v5-v1%2FGEN-SIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/d76b872e687b465084298db19f198efc HTTP/1.1" 200 1025
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET%2FRun2022G-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/c22c42a96c97416ba53d5c71f8274545 HTTP/1.1" 200 1192
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYToLL_M_1_TuneCUETP8M1_13TeV_pythia8%2FRunIISummer17MiniAOD-NZSFlatPU28to62_92X_upgrade2017_realistic_v10-v1%2FMINIAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/bab8e8ce76bf4fb19b0c00facbc325aa HTTP/1.1" 200 1492
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHIPhysicsRawPrime9%2FHIRun2024B-PbPbHighPtJets-PromptReco-v2%2FRAW-RECO/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/e64e5582d7cd4213a075f1ec63b60312 HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024I-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/fd5b72bc80b34b2088790b7586115105 HTTP/1.1" 200 1157
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024F-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/7315a75cf6984efc936fe916628724eb HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024I-EXOSoftDisplacedVertices-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/437bc1998961459d8e9b1d1dfdf59631 HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-3_M-1600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/9300d99f092b44cdb4bb553065ffaae8 HTTP/1.1" 200 1341
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251205_090756.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes0_part3%2FUSER/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/3df55100b3f24902983dced5e4b6c0e1 HTTP/1.1" 200 1074
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024I-EXOSoftDisplacedVertices-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/db2a59c4faac49dab3e4aee5441296e2 HTTP/1.1" 200 1101
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHIPhysicsRawPrime43%2FHIRun2024A-PbPbZMu-OfflinePromptReco-v1%2FRAW-RECO/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/c055eab80b514397a69a515f5f75a635 HTTP/1.1" 200 1117
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024I-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/7077bf6223634813b4dee516a2d9f728 HTTP/1.1" 200 1305
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYjetstoee_01234jets_Pt-0ToInf_13TeV-sherpa%2FRunIISummer16MiniAODv3-PUMoriond17_QCDEWNLO_correct_94X_mcRun2_asymptotic_v3-v1%2FMINIAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/52ff2cc8bb744ef9a2f117a5fa71dca3 HTTP/1.1" 200 1313
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FDYjetstotautau_01234jets_Pt-0ToInf_13TeV-sherpa%2FRunIISummer16MiniAODv3-PUMoriond17_QCDEWNLO_correct_94X_mcRun2_asymptotic_v3-v1%2FMINIAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/490edc438a4044a888bc7a1e92a8a50f HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHIPhysicsRawPrime33%2FHIRun2024A-PbPbZMu-OfflinePromptReco-v1%2FRAW-RECO/files HTTP/1.1" 200 None
value creation lock <dogpile.cache.region.CacheRegion._LockWrapper object at 0x7f859e378700> acquired
Calling creation function for previously expired value
Cache value generated in 0.000 seconds for key(s): "host_to_choose_choice['http://cms-rucio.cern.ch/']"
Released creation lock
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/9296584645a4438b8140568c705720b8 HTTP/1.1" 200 1113
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024E-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/d06a76da694d4859bb72c176ca512c4f HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-6_M-1600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/bd730443ecad4024be5313fcb22d4056 HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-18_M-1200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/1060294cfb8c492f922daf3e56bea154 HTTP/1.1" 200 1404
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FQCD_Bin-Pt-30to50_TuneCP5_13p6TeV_pythia8%2FRun3Winter25Digi-142X_mcRun3_2025_realistic_v7-v3%2FGEN-SIM-RAW/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/de849deeb1444bc3bc192bc92d460d85 HTTP/1.1" 200 1123
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET0%2FRun2024G-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/de9ffc21e0094d8888a66dc32be4b026 HTTP/1.1" 200 1341
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/user.crab_tape_recall/%2FTapeRecall%2F251205_080818.lamartik_crab_Run3_2024_pbpbreco_DATA_PPRefHardProbes0_part2%2FUSER/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/dde184f1725f475b9d8c6273d264cbc4 HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-18_M-100_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/11715f9172584a6eb20330324467101b HTTP/1.1" 200 1093
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024G-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/7679fdfa1bac4538a540729770be17d5 HTTP/1.1" 200 1114
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024D-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/b5bde7c273f2460b8b72ffb83a408d10 HTTP/1.1" 200 1088
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024I-PromptReco-v2%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/a0bb8af37f5c4f9aa1a8765e9b9011f4 HTTP/1.1" 200 1121
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2025D-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/fed927d132a742a988faf3d3e8faba8e HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-18_M-2000_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/ccd8d271dddb4721adb1ce9f90e05448 HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-21_M-1600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/3e4ba53c559d411e87ceb02fff4e0386 HTTP/1.1" 200 1180
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-6_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/f91c39a8fcfc445d9e65f0d8a3c16b08 HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-1600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/69ea782d10f94d73b141db1eadd7f8be HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-15_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/052ee68d12cb4871a6126db5c84f036b HTTP/1.1" 200 1111
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FJetMET1%2FRun2024B-PromptReco-v1%2FAOD/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/922bf4b9423f40e9bc4db3bfa711f9bf HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-18_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/8de099d04e824a67a070b740ea9cdf12 HTTP/1.1" 200 1263
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-21_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/857598d3b77241d0adbd6fb265fb8fd4 HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-15_M-600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/252427a0a3f4429ea6372e4ea25059af HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-1200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/84be050fdaed4a589ab173c20b5aa95f HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-600_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/bf5d2193d21845a6bcfa595973fd8fdb HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-12_M-2400_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/957673435c844864a0edabd9ad99dc20 HTTP/1.1" 200 1180
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-3_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/2a2282b5203448c3b7d53c5057d9dc10 HTTP/1.1" 200 1180
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-3_M-400_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/4bdbde4945ac418fa6ec966ac0447f1a HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/da18acefa73445aba8d71d7d3834394d HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-21_M-1200_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/a7d36ef4e5254cf9bea0d88ff14a3967 HTTP/1.1" 200 1182
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-24_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/ff51650f81a845a984e74f64af9ffe05 HTTP/1.1" 200 1180
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-3_M-800_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/3209f1193991489f9108df93d5431033 HTTP/1.1" 200 1632
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-6_M-100_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /rules/ee3d2dcd2a0348ef851fb5fc0d307255 HTTP/1.1" 200 1184
[http://cms-rucio.cern.ch:80](http://cms-rucio.cern.ch/) "GET /dids/cms/%2FHSCPmchamp_Q-21_M-2400_TuneCP2_13TeV_pythia8%2FRunIISummer20UL18RECO-106X_upgrade2018_realistic_v11_L1v1-v2%2FAODSIM/files HTTP/1.1" 200 None
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 697, in _update_chunk_length
    self.chunk_left = int(line, 16)
ValueError: invalid literal for int() with base 16: b''

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 438, in _error_catcher
    yield
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 764, in read_chunked
    self._update_chunk_length()
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 701, in _update_chunk_length
    raise InvalidChunkLength(self, line)
urllib3.exceptions.InvalidChunkLength: InvalidChunkLength(got length b'', 0 bytes read)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 760, in generate
    for chunk in self.raw.stream(chunk_size, decode_content=True):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 572, in stream
    for line in self.read_chunked(amt, decode_content=decode_content):
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 793, in read_chunked
    self._original_response.close()
  File "/usr/local/lib/python3.8/contextlib.py", line 131, in __exit__
    self.gen.throw(type, value, traceback)
  File "/usr/local/lib/python3.8/site-packages/urllib3/response.py", line 455, in _error_catcher
    raise ProtocolError("Connection broken: %r" % e, e)
urllib3.exceptions.ProtocolError: ("Connection broken: InvalidChunkLength(got length b'', 0 bytes read)", InvalidChunkLength(got length b'', 0 bytes read))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/data/srv/monit/ReportRecallQuota.py", line 110, in <module>
    main(logger)
  File "/data/srv/monit/ReportRecallQuota.py", line 86, in main
    report = createQuotaReport(rucioClient=rucioClient,
  File "/data/srv/monit/ReportRecallQuota.py", line 35, in createQuotaReport
    totalBytes = getRucioUsage(rucioClient=rucioClient,account=account,activity=activity)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 190, in getRucioUsage
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 190, in <genexpr>
    totalusage = sum(getRuleQuota(rucioClient, rule['id']) for rule in rules if rule['state'] in valid_states)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 158, in getRuleQuota
    size = sum(file['bytes'] for file in files)
  File "/data/srv/current/lib/python/site-packages/RucioUtils.py", line 158, in <genexpr>
    size = sum(file['bytes'] for file in files)
  File "/usr/local/lib/python3.8/site-packages/rucio/client/baseclient.py", line 329, in _load_json_data
    for line in response.iter_lines():
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 804, in iter_lines
    for chunk in self.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode):
  File "/usr/local/lib/python3.8/site-packages/requests/models.py", line 763, in generate
    raise ChunkedEncodingError(e)
requests.exceptions.ChunkedEncodingError: ("Connection broken: InvalidChunkLength(got length b'', 0 bytes read)", InvalidChunkLength(got length b'', 0 bytes read))
```

## Comment (belforte, 2025-12-08T11:09:12Z)

@nausikt this may be as easy as running the script and looking at stdout, since it seems to send this mail almost every time now. Or you can instrument the crontab with some debugging log. Feel free to adjust priority to make it fit your "holes".
