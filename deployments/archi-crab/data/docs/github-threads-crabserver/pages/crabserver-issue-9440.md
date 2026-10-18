# dmwm/CRABServer issue #9440: set safe upper limit to job stdout retrieved to disk

State: open
Opened: 2026-10-12T10:58:38Z
Labels: OPERATION
URL: https://github.com/dmwm/CRABServer/issues/9440

## Opening post (belforte, 2026-10-12T10:58:38Z)

as per #9438 we should make sure that no matter what happens, we limit the side of the flle retrieved to out disks.
Steps are

- [ ] look at `jfr_out.X.Y.txt` size distribution in our AP's WEB_DIRs to figure out a correct limit
- [ ] work with SI to set the value of `MAX_TRANSFER_OUTPUT_MB` in the `schedd` config
