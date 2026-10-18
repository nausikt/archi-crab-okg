# dmwm/CRABServer pull request #9327: remove core dumps and better msgs. Fix #9325

State: closed
Opened: 2026-06-22T15:46:10Z
Closed: 2026-06-22T17:20:55Z
Merged: 2026-06-22T17:20:55Z
URL: https://github.com/dmwm/CRABServer/pull/9327

## Opening post (belforte, 2026-06-22T15:46:10Z)

(no text)

## Comment (belforte, 2026-06-22T15:48:27Z)

@nausikt I did
` git config --global gpg.format ssh`
on my laptop and then created again the branch, the commit, the PR, but apparently my commit does not have a verified signature. My ssh key is known to GH, that's how I push to my fork.
Can you share the recipe that you  used ?
Thanks

## Comment (cmsdmwmbot, 2026-06-22T15:49:02Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2843/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-22T15:51:36Z)

maybe I should have used `commit -S`, so tried to amend, but...
```console
LapSB:CRABServer$ git commit --amend --no-edit -S
fatal: either user.signingkey or gpg.ssh.defaultKeyCommand needs to be configured
LapSB:CRABServer$ 
```

## Comment (belforte, 2026-06-22T16:00:01Z)

thanks for approving, but I need to sign :crying_cat_face:

## Comment (nausikt, 2026-06-22T16:01:49Z)

This is few cmds, i got from ChatGPT this morning.
*please, point to your own ` ~/.ssh/id_rsa.pub` public key.*

2. Configure SSH signing key
```
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_rsa.pub
git config --global commit.gpgsign true
```

3. Fix local SSH signature verification
```
mkdir -p ~/.config/git
echo "yourname@example.com $(cat ~/.ssh/id_rsa.pub)" > ~/.config/git/allowed_signers
git config --global gpg.ssh.allowedSignersFile ~/.config/git/allowed_signers
```

4. Re-sign all commits in your branch, in cases
```
git branch backup-before-resign
BASE=$(git merge-base HEAD delete-core-dumps-in-wn-9325)
git rebase --exec 'git commit --amend --no-edit -S' "$BASE"
```

```
git push --force-with-lease origin delete-core-dumps-in-wn-9325
```

## Comment (belforte, 2026-06-22T16:53:34Z)

I did all of that but apparently it is not enough.
When I do `git log --show-signature --oneline ` I see your signatures, but not the one which I should have added with the `git commit --amend -S`

<img width="769" height="405" alt="image" src="https://github.com/user-attachments/assets/b9033fa5-1938-47eb-8dd4-f8667e629cff" />

 I will try more after dinner, or tomorrow

## Comment (cmsdmwmbot, 2026-06-22T17:04:01Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2844/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-22T17:05:10Z)

small progress, in my local
LapSB:CRABServer$ git log --show-signature --oneline
4220a238 (HEAD -> delete-core-dumps-in-wn-9325, origin/delete-core-dumps-in-wn-9325) Good "git" signature for stefano.belforte@cern.ch with RSA key SHA256:MR60NmRkImnq+Widwym0o9mDZVYlsB4wIHHqw7DS19M
remove core dumps and better msgs. Fix #9325

but after push --force this PR is still blocked

## Comment (cmsdmwmbot, 2026-06-22T17:05:59Z)

Jenkins results:
 * Python3 Pylint check: succeeded
 * Pycodestyle check: succeeded

Details at https://cmssdt.cern.ch/dmwm-jenkins/view/All/job/DMWM-CRABServer-PR-test/2845/artifact/artifacts/PullRequestReport.html

## Comment (belforte, 2026-06-22T17:07:32Z)

hmm...
<img width="1024" height="342" alt="image" src="https://github.com/user-attachments/assets/dd877d96-20ce-4cb9-9924-ee4d10d98d43" />

my ssh key is uploaded as authorization key. What more do I need to do ?

## Comment (belforte, 2026-06-22T17:10:10Z)

clicking on the link in above screenshot shows
<img width="1175" height="682" alt="image" src="https://github.com/user-attachments/assets/55628cf1-6345-4f27-96a4-3a762210108c" />

Do I need to upload my ssh key as a gpg key ? or upload this file `/home/belforte/.config/git/allowed_signers` ?

## Comment (belforte, 2026-06-22T17:20:25Z)

OK. I had to add again my ssh key in that page, selecting type signing instead of authorization .
I will have to do the same on lxplus since occasionally I commit from there.
<img width="542" height="562" alt="image" src="https://github.com/user-attachments/assets/24c740c4-541c-4db4-93f8-bd35ed73e1c8" />

## Comment (nausikt, 2026-06-22T18:30:54Z)

Ahh, yeah have to added again as `signing` was obsecure for me too, back then when i also re-used same pub. 

I will revise https://cmscrab.docs.cern.ch/development/environment/git-best-practices.html accordingly na.
