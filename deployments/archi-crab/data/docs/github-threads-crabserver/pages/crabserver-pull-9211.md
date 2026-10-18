# dmwm/CRABServer pull request #9211: Bump python-ldap from 3.4.3 to 3.4.5 in /cicd/crabtaskworker_pypi

State: closed
Opened: 2025-10-10T22:54:51Z
Closed: 2026-01-30T11:12:00Z
Labels: dependencies, python
URL: https://github.com/dmwm/CRABServer/pull/9211

## Opening post (dependabot[bot], 2025-10-10T22:54:51Z)

Bumps [python-ldap](https://github.com/python-ldap/python-ldap) from 3.4.3 to 3.4.5.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/python-ldap/python-ldap/releases">python-ldap's releases</a>.</em></p>
<blockquote>
<h2>3.4.5</h2>
<p>Released 3.4.5 2025-10-10</p>
<p>Security fixes:</p>
<ul>
<li>CVE-2025-61911 (GHSA-r7r6-cc7p-4v5m): Enforce <code>str</code> input in
<code>ldap.filter.escape_filter_chars</code> with <code>escape_mode=1</code>; ensure proper
escaping. (thanks to lukas-eu)</li>
<li>CVE-2025-61912 (GHSA-p34h-wq7j-h5v6): Correct NUL escaping in
<code>ldap.dn.escape_dn_chars</code> to <code>\00</code> per RFC 4514. (thanks to aradona91)</li>
</ul>
<p>Fixes:</p>
<ul>
<li>ReconnectLDAPObject now properly reconnects on UNAVAILABLE, CONNECT_ERROR
and TIMEOUT exceptions (previously only SERVER_DOWN), fixing reconnection
issues especially during server restarts</li>
<li>Fixed syncrepl.py to use named constants instead of raw decimal values
for result types</li>
<li>Fixed error handling in SearchNoOpMixIn to prevent a undefined variable error</li>
</ul>
<p>Tests:</p>
<ul>
<li>Added comprehensive reconnection test cases including concurrent operation
handling and server restart scenarios</li>
</ul>
<p>Doc/</p>
<ul>
<li>Updated installation docs and fixed various documentation typos</li>
<li>Added ReadTheDocs configuration file</li>
</ul>
<p>Infrastructure:</p>
<ul>
<li>Add testing and document support for Python 3.13</li>
</ul>
<h2>3.4.4</h2>
<p>Released 3.4.4 2023-11-17</p>
<p>Fixes:</p>
<ul>
<li>Reconnect race condition in ReconnectLDAPObject is now fixed</li>
<li>Socket ownership is now claimed once we've passed it to libldap</li>
<li>LDAP_set_option string formats are now compatible with Python 3.12</li>
</ul>
<p>Doc/</p>
<ul>
<li>Security Policy was created</li>
<li>Broken article links are fixed now</li>
<li>Bring Conscious Language improvements</li>
</ul>
<p>Infrastructure:</p>
<ul>
<li>Add testing and document support for Python 3.10, 3.11, and 3.12</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/python-ldap/python-ldap/blob/python-ldap-3.4.5/CHANGES">python-ldap's changelog</a>.</em></p>
<blockquote>
<p>Released 3.4.5 2025-10-10</p>
<p>Security fixes:</p>
<ul>
<li>CVE-2025-61911 (GHSA-r7r6-cc7p-4v5m): Enforce <code>str</code> input in
<code>ldap.filter.escape_filter_chars</code> with <code>escape_mode=1</code>; ensure proper
escaping. (thanks to lukas-eu)</li>
<li>CVE-2025-61912 (GHSA-p34h-wq7j-h5v6): Correct NUL escaping in
<code>ldap.dn.escape_dn_chars</code> to <code>\00</code> per RFC 4514. (thanks to aradona91)</li>
</ul>
<p>Fixes:</p>
<ul>
<li>ReconnectLDAPObject now properly reconnects on UNAVAILABLE, CONNECT_ERROR
and TIMEOUT exceptions (previously only SERVER_DOWN), fixing reconnection
issues especially during server restarts</li>
<li>Fixed syncrepl.py to use named constants instead of raw decimal values
for result types</li>
<li>Fixed error handling in SearchNoOpMixIn to prevent a undefined variable error</li>
</ul>
<p>Tests:</p>
<ul>
<li>Added comprehensive reconnection test cases including concurrent operation
handling and server restart scenarios</li>
</ul>
<p>Doc/</p>
<ul>
<li>Updated installation docs and fixed various documentation typos</li>
<li>Added ReadTheDocs configuration file</li>
</ul>
<p>Infrastructure:</p>
<ul>
<li>Add testing and document support for Python 3.13</li>
</ul>
<hr />
<p>Released 3.4.4 2022-11-17</p>
<p>Fixes:</p>
<ul>
<li>Reconnect race condition in ReconnectLDAPObject is now fixed</li>
<li>Socket ownership is now claimed once we've passed it to libldap</li>
<li>LDAP_set_option string formats are now compatible with Python 3.12</li>
</ul>
<p>Doc/</p>
<ul>
<li>Security Policy was created</li>
<li>Broken article links are fixed now</li>
<li>Bring Conscious Language improvements</li>
</ul>
<p>Infrastructure:</p>
<ul>
<li>Add testing and document support for Python 3.10, 3.11, and 3.12</li>
</ul>
<hr />
<p>Released 3.4.3 2022-09-15</p>
<p>This is a minor release to bring back the removed OPT_X_TLS option.
Please note, it's still a deprecated option and it will be removed in 3.5.0.</p>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/python-ldap/python-ldap/commit/bf666e918615b00dbcd1bbe71542522eedfdffc1"><code>bf666e9</code></a> Prepare a new release</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/464fddacd63092d6e01c62a38316a713c30ca98a"><code>464fdda</code></a> Merge commit from fork</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/9f5b2effbafdf7af0e7064a7aa42d2739d373bd7"><code>9f5b2ef</code></a> Merge commit from fork</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/f49bb2dd2234f25404ad1679786de007444ce219"><code>f49bb2d</code></a> Package python-ldap with pyproject.toml (<a href="https://redirect.github.com/python-ldap/python-ldap/issues/589">#589</a>)</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/6ee881c1d32d9589d68539021091fac19fa5a9e6"><code>6ee881c</code></a> Add support for Python 3.13 (<a href="https://redirect.github.com/python-ldap/python-ldap/issues/576">#576</a>)</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/74c6eeb52ed68f24a8a66937252ef213dd1ce85a"><code>74c6eeb</code></a> docs(ldapobject): fix typo in docstring</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/8a6586241e59b8154d3867dd8d0e7f96e42daa31"><code>8a65862</code></a> fix(controls): make sure msg_id is not undefined in error case</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/73b3ec338f81711ef04563f5d0a63b52615ae313"><code>73b3ec3</code></a> fix(ReconnectLDAPObject): Also reconnect on UNAVILABLE, CONNECT_ERROR and TIM...</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/94c6ab2d7f70bb88101428857b22fccb4d434ffd"><code>94c6ab2</code></a> test: Implement test cases for reconnection handling</li>
<li><a href="https://github.com/python-ldap/python-ldap/commit/cc987235309b3ec6ab0829b95ab3bd6ee1c40b2f"><code>cc98723</code></a> Add readthedocs configuration file</li>
<li>Additional commits viewable in <a href="https://github.com/python-ldap/python-ldap/compare/python-ldap-3.4.3...python-ldap-3.4.5">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=python-ldap&package-manager=pip&previous-version=3.4.3&new-version=3.4.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/dmwm/CRABServer/network/alerts).

</details>

> **Note**
> Automatic rebases have been disabled on this pull request as it has been open for over 30 days.

## Comment (cmsdmwmbot, 2025-10-10T22:55:02Z)

Can one of the admins verify this patch?

## Comment (belforte, 2026-01-30T11:12:00Z)

ldap dependency removed in #9224
