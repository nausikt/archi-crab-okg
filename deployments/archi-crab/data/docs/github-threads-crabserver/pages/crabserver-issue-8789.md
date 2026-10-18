# dmwm/CRABServer issue #8789: adapt ProcessBadFilesList to new format

State: closed
Opened: 2024-11-13T20:13:09Z
Closed: 2024-11-18T14:54:00Z
URL: https://github.com/dmwm/CRABServer/issues/8789

## Opening post (belforte, 2024-11-13T20:13:09Z)

now there is subdir for each task
```console
belforte@lxplus830/new> ls /eos/cms/store/temp/user/BadInputFiles/suspicious/new |tail   
241113_160939:woji_crab_ParkingDoubleMuonLowMass2022_ParkingDoubleMuonLowMass4_Run2022F_2024Nov14241113_160939:woji_crab_ParkingDoubleMuonLowMass2022_ParkingDoubleMuonLowMass4_Run2022F_2024Nov14.job.119.0.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.0.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.1.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.2.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.3.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.4.json
241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1241113_162113:gcoulon_crab_Analysis_SingleMuon_Run2017E_CodeV2p10_v1.job.1208.5.json
241113_183514:kaho_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asvkUwbzv4/
241113_183745:kaho_crab_20241113_193743/
241113_193255:kdeleo_crab_test7_Prime22/
belforte@lxplus830/new> 


```

## Comment (belforte, 2024-11-13T21:23:59Z)

closed via #8791

## Comment (belforte, 2024-11-18T10:37:54Z)

That fix was  not good enough :
```text
The cron command
     /usr/bin/eosfusebind;/afs/cern.ch/user/b/belforte/utils/list-bad-input-files.sh
produced the following output:
ProcessBadFilesListfailed: here's log
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
error: MGM root://localhost not online/reachable
Traceback (most recent call last):
  File "ProcessBadFilesList.py", line 314, in <module>
    main()
  File "ProcessBadFilesList.py", line 60, in main
    shutil.move(taskDir, doneFilesDir)
  File "/usr/lib64/python3.6/shutil.py", line 548, in move
    raise Error("Destination path '%s' already exists" % real_dst)
shutil.Error: Destination path '/eos/cms/store/temp/user/BadInputFiles/corrupted/done/241114_060810:sciaba_crab_HC-205-T2_US_MIT-109864-20241114070701' already exists
```

## Comment (belforte, 2024-11-18T14:54:00Z)

closed via #8799
