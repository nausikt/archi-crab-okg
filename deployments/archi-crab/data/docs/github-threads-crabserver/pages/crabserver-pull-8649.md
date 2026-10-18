# dmwm/CRABServer pull request #8649: fix .gitlab-ci.yml comment

State: closed
Opened: 2024-08-26T11:35:16Z
Closed: 2024-08-26T11:35:36Z
Merged: 2024-08-26T11:35:36Z
URL: https://github.com/dmwm/CRABServer/pull/8649

## Opening post (novicecpp, 2024-08-26T11:35:16Z)

My bad.

## Comment (belforte, 2024-08-26T13:33:49Z)

I have to ask... did you simply remove white spaces at the end of comment lines  ? aren't those harmless  ? or was there some odd character which made YAML parser fail ?

## Comment (novicecpp, 2024-08-26T13:42:26Z)

I forgot `#` in front of comment at line 16.

White space at the end is harmless. My editor removes it every time I save the file.
