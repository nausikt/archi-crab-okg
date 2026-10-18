# dmwm/CRABServer issue #9422: mail for dry-run of kill on too many ASO failed jobs

State: open
Opened: 2026-09-17T09:46:22Z
URL: https://github.com/dmwm/CRABServer/issues/9422

## Opening post (nausikt, 2026-09-17T09:46:22Z)

- [x] Query UserEmail by Username via existing CRIC accounts/user/query with preset=People.
```
curl --key "$X509_USER_PROXY" --cert "$X509_USER_PROXY"   "https://cms-cric.cern.ch/api/accounts/user/query/?json&preset=people"
```
- [x] attach UserEmail to classAds for further reusability. (CRAB_UserEmail)

## Comment (nausikt, 2026-09-24T15:18:21Z)

- [x] Then conditionally firing email inside PostJob, retrieving email from CRAB_UserEmail.
