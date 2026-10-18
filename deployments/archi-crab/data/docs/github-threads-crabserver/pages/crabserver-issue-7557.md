# dmwm/CRABServer issue #7557: allow f-strings in logging in pylint

State: closed
Opened: 2023-02-27T22:13:29Z
Closed: 2024-09-13T10:54:28Z
Labels: Area: CI/CD
URL: https://github.com/dmwm/CRABServer/issues/7557

## Opening post (belforte, 2023-02-27T22:13:29Z)

we should tell our pylint not to complain about use of f-string in logging
So that we can use
```python
logging.info(f"something wrong with {aParam}")
```
which allows for consistent use of  f-strings in the code

see
https://pylint.pycqa.org/en/latest/user_guide/messages/warning/logging-format-interpolation.html
and if you care, the horrendous discussion in the rational there and further down the chain
In the end there's a lot of nitty-picking there, but I am for cutting the noise
