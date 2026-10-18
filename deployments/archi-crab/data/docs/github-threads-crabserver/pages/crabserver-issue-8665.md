# dmwm/CRABServer issue #8665: add a GIT Etiquette section to crab-docs

State: closed
Opened: 2024-08-28T15:54:19Z
Closed: 2025-08-19T19:00:30Z
Labels: Type: Documentation
URL: https://github.com/dmwm/CRABServer/issues/8665

## Opening post (belforte, 2024-08-28T15:54:19Z)

something like this from Eric
```text
The setup should be like this (pseudo-code)

git clone github/belforte/crab (is now called “origin”)
git add remote upstream github/dmwm/crab (is now called upstream)

Then when your repository is out of date with the central:

git checkout master
git fetch upstream            # fetch commits history
git fetch --tags upstream     # also the tags (need two commands)
git merge upstream/master     # merge upstream on your local
git push  origin              # move those changes up
git push --tags origin        # also the tags

To develop something (version 1)

git checkout master # start with latest master
git checkout -b my_feature # checkout and start a new branch
git push --set-upstream origin my_feature # track new branch in your github
# [code]
git commit -m “My feature is awesome”
git push origin # put on your github

Then visit github and make a pull request.

To develop something (version 2)
git checkout master
git checkout -b my_feature
# code
git commit -m “My feature is awesome”
git push origin my_feature  # i.e. use the name of the branch

Then visit github and make a pull request.


You’ll notice in my schemed your changes follow this route:

begin on local branch
pushed to remote branch
pulled/merged onto upstream (DMWM repo) by Marco
only arrive on your local master with the merge of upstream/master
then pushed to your github master
```

## Comment (belforte, 2025-08-19T19:00:30Z)

done in https://cmscrab.docs.cern.ch/development/environment/git-best-practices.html
