# dmwm/CRABServer issue #8925: remove backward compatibility code from CMSRunAnalysis

State: closed
Opened: 2025-02-17T09:47:11Z
Closed: 2025-06-06T09:08:00Z
Labels: Area: Code Cleanup
URL: https://github.com/dmwm/CRABServer/issues/8925

## Opening post (belforte, 2025-02-17T09:47:11Z)

Once new client https://github.com/dmwm/CRABClient/releases/tag/v3.250217 will be in production, can
- [x] remove support for all input arguments in CMSRunAnalysis with exception of `--jobId` 
- [x] replace use of `opts.` for arguments read from `input_args.json` and use more descriptinve naming
- [x] remove extra args added in DagmanCreator for backward compatibility
- [ ] more cleanup ?
