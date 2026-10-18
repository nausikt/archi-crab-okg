# dmwm/CRABClient issue #5400: enforce users to specify SiteWhitelis for data w/o location

State: closed
Opened: 2025-07-01T15:53:24Z
Closed: 2025-07-02T06:33:25Z
URL: https://github.com/dmwm/CRABClient/issues/5400

## Opening post (belforte, 2025-07-01T15:53:24Z)

ref https://github.com/dmwm/CRABServer/issues/9116

we must have user specify a site white list when they ask to process data for which we do not have locations in Rucio:
- [x] with `ignoreLocality = True` 
   * this was done already in #4646 ! https://github.com/dmwm/CRABClient/blob/64b0373ce7912719936fdea7c37fdbe7d831b962/src/python/CRABClient/Commands/submit.py#L371-L375
- [x] using `config.Data.userInputFiles`
   * semantics of this has changed, need to fix documentation
       1. if both userInputFiles and inputDataset are specified, it acts as a "fileMask" on the dataset and location comes from Rucio
           - [x] fix twiki 
       3. if inputDataset is missing, if is just a list of LFN/PFN and a white site list must be required
           - [x] change code
- [x] look if there's any other use case for this

## Comment (belforte, 2025-07-01T19:06:56Z)

I could not find any other situation where this is needed. If we find it, we'll open a new issue.
