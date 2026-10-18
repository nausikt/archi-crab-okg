# dmwm/CRABClient issue #5308: allow to specify both inputDataset and userInputFiles in crabConfig

State: closed
Opened: 2024-05-02T15:51:47Z
Closed: 2024-05-13T21:19:02Z
Labels: enhancement, Done, HighPrio, Priority: TOP
URL: https://github.com/dmwm/CRABClient/issues/5308

## Opening post (belforte, 2024-05-02T15:51:47Z)

an in that case restrict processing of the dataset to the user-supplied list of files.
This will facilitate recovery tasks submission.
FYI @kandros
Wiill something like this in crabConfig.py do for you ?
```python
config.Data.inputDataset = '/DoubleMuon/Run2018B-17Sep2018-v1/MINIAOD'
config.Data.userInputFiles = [
'/store/data/Run2018B/DoubleMuon/MINIAOD/17Sep2018-v1/00000/3C66535E-5312-4544-98C4-4AC6F9FA1825.root',
'/store/data/Run2018B/DoubleMuon/MINIAOD/17Sep2018-v1/00000/E157977E-26C3-D341-8718-74E819E7B9AB.root',
]
```
