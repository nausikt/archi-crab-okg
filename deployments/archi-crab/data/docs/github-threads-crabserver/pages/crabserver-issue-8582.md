# dmwm/CRABServer issue #8582: [PyPI] Build from WMCore private repository

State: closed
Opened: 2024-08-02T16:19:58Z
Closed: 2024-09-04T19:14:53Z
Labels: PyPI
URL: https://github.com/dmwm/CRABServer/issues/8582

## Opening post (novicecpp, 2024-08-02T16:19:58Z)

Last task from https://github.com/dmwm/CRABServer/issues/8224

Now, only data files are built by pull from source code. We need ability to install it from forked repo to enable ability to automated ci testing and hot-patching.

Look like the solution would be:
- Simply copy src/python to install_dir directly.
- For release, install from pipy server.
